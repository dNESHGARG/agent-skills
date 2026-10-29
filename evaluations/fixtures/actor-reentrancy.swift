// Intentionally defective: actor isolation does not make check-then-act atomic.
actor Wallet {
    private var balance = 100
    func spend(_ amount: Int) async -> Bool {
        guard balance >= amount else { return false }
        await verify()
        balance -= amount
        return true
    }
    private func verify() async {}
}
// Two concurrent spend(80) calls may both pass the balance check.
