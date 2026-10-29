// Intentionally defective: no server-side idempotency.
type Gateway = { charge: (user: string, cents: number) => Promise<string> };
export class Checkout {
  constructor(private gateway: Gateway) {}
  async pay(user: string, cents: number) {
    if (cents <= 0) throw new Error("invalid amount");
    return this.gateway.charge(user, cents);
  }
}
// Two concurrent pay("u1", 1000) calls can create two charges.
