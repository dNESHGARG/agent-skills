// Intentional bug: response order can differ from request order.
type Search = (query: string) => Promise<string[]>;
export class SearchModel {
  results: string[] = [];
  constructor(private readonly search: Search) {}
  async update(query: string): Promise<void> {
    this.results = await this.search(query);
  }
}
// Reproduction: update("ca") starts, update("cat") starts,
// resolve "cat" first, then "ca". Final results incorrectly show "ca".
