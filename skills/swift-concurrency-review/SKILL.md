---
name: swift-concurrency-review
description: Review Swift 6 actor isolation, Sendable correctness, structured concurrency, cancellation, and SwiftUI task lifecycles.
---

# Swift concurrency review

## Compiler and API context
Record Swift language mode, strict concurrency settings, deployment target, framework isolation annotations, and whether code uses Swift 5 compatibility behavior. Distinguish compiler diagnostics from runtime correctness.

## Isolation map
For every mutable type, annotate actor/global actor ownership, `Sendable` conformance, escaping closures, nonisolated members, and cross-actor calls. Do not use `@unchecked Sendable` as a diagnostic silencer without proving synchronization.

## Review passes
1. **Actor reentrancy:** every `await` is an interleaving boundary. Revalidate assumptions or reserve state before suspension.
2. **MainActor:** keep UI state updates isolated; avoid expensive synchronous work on the main actor. `Task { }` inherits current actor context; `Task.detached` does not.
3. **Structured concurrency:** prefer `async let` for fixed independent children, `withThrowingTaskGroup` for dynamic fan-out; ensure children complete/cancel with their scope.
4. **Cancellation:** `Task.checkCancellation()` and `Task.isCancelled` are cooperative. A cancelled URL request may still have already produced a result; guard before applying state.
5. **SwiftUI lifetime:** `.task(id:)` restarts when identity changes and cancels previous task; view-owned unstructured tasks need explicit lifecycle management.
6. **Ordering:** prevent stale network responses from overwriting newer state using a request generation or identity check.

## Example — stale view model refresh
```swift
@MainActor
@Observable
final class StoreModel {
    var stores: [Store] = []
    private var generation = 0

    func refresh() async throws {
        generation += 1
        let request = generation
        let result = try await service.fetchStores()
        guard request == generation, !Task.isCancelled else { return }
        stores = result
    }
}
```
Here `service` is an injected dependency assumed to be declared separately. Generation prevents out-of-order completion. Consider whether errors from stale requests should also be ignored and how loading indicators are coordinated.

## Report
Include compiler settings, isolation table, exact suspension/interleaving, reproducible issue, corrected snippet, and tests. Never assert that `@MainActor` alone prevents stale-result races.
