---
name: concurrency-audit
description: Audit async code for data races, actor reentrancy, stale responses, deadlocks, cancellation, and bounded resource usage.
---

# Concurrency audit — state and interleavings

## Model first
Identify shared mutable state, its owner, all readers/writers, and the synchronization mechanism. Draw a happens-before graph for critical operations. Mark every `await`, callback, lock boundary, task spawn, and cross-thread hop.

## Inspect six failure families
1. **Data races:** unsynchronized read/write or write/write to shared state.
2. **Logical races:** individually synchronized operations violate a multi-step invariant.
3. **Reentrancy:** state changes while an actor method is suspended.
4. **Stale completion:** older work overwrites newer state.
5. **Liveness:** deadlocks, starvation, unbounded task growth, blocking actor threads.
6. **Lifecycle:** missing cancellation, detached tasks outliving owners, leaked continuations.

## Required evidence for each finding
Name tasks A/B; write a numbered interleaving; identify the violated invariant; specify whether the issue is demonstrable or hypothetical. Propose an atomic boundary or ordering rule. Describe a deterministic test harness.

## Swift actor example
```swift
actor Wallet {
    private var balance = 100

    func spend(_ amount: Int) async -> Bool {
        guard balance >= amount else { return false }
        await verifyPurchase()  // actor may run another spend here
        balance -= amount
        return true
    }
}
```
Two concurrent `spend(80)` calls can both pass the guard before either subtracts, leaving `balance == -60`. Actor isolation prevents data races but **not** this logical race. Solutions depend on business semantics: reserve funds before suspension and compensate on failure; or verify outside the actor then perform an atomic check-and-decrement without suspension. A simple second balance check after `await` is sufficient only if no other suspension occurs between the check and decrement.

## Cancellation
Cancellation is cooperative. Check whether work is cancelled at ownership boundaries, whether cancellation propagates through child tasks, and whether a cancelled task can still mutate visible state. Avoid `Task.detached` for ordinary view-owned work.

## Testing
Use barriers, manually controlled continuations, and injected clocks to force interleavings. Stress tests and Thread Sanitizer supplement but do not replace deterministic tests. Report exactly which tests ran.

## Output
State ownership table; findings with interleaving and severity; minimal fixes; tests; residual risk. Do not confuse thread safety with operation-level correctness.
