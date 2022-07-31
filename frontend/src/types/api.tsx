export interface Contribution {
  date: string;
  count: number;
}

export interface ContributionResponse {
  contributions: Contribution[];
  weeks: number[][];
}
