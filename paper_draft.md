# Gone But Not Forgotten? Competitive Effects of Spirit Airlines' Bankruptcy on U.S. Domestic Airfares

**Aryan Goel**

University of Chicago, Department of Economics and Computer Science

May 2026

---

## 1. Introduction

On May 2, 2026, Spirit Airlines ceased all operations, ending more than three decades as a pioneer of the ultra-low-cost carrier (ULCC) model in the United States. The shutdown marked the culmination of a prolonged financial decline: Spirit filed for Chapter 11 bankruptcy in November 2024, emerged briefly in April 2025, filed again in August 2025, and ultimately failed to secure sufficient financing to continue operations. Consumer advocates warned that Spirit's disappearance would harm travelers even beyond its own passengers, because Spirit's presence on a route disciplined incumbent carriers' fares — a phenomenon documented as the "Spirit Effect" by Shrago (2024) and cited by the Department of Justice in its successful challenge to JetBlue's proposed acquisition of Spirit in January 2024.

This paper asks a natural follow-up question: if Spirit's presence reduced fares, did its exit raise them? Using the Bureau of Transportation Statistics' Airline Origin and Destination Survey (DB1B) from 2022 through 2025, I compare the evolution of fares on 176 routes that Spirit exited during its bankruptcy to fares on comparable routes that Spirit never served. Across four increasingly rigorous specifications — from simple OLS to a difference-in-differences framework with route and quarter fixed effects — I find a small but statistically insignificant effect on competitor fares, ranging from −1.5% to +1.3% depending on specification.

I then investigate why the fare effect appears muted, and find that competition on Spirit-exited routes was largely maintained: Delta, American, and Southwest grew their passenger volumes on these routes by 13–16% after Spirit's bankruptcy filing, effectively backfilling the competitive gap. This finding suggests that the Spirit Effect, while real during Spirit's period of healthy expansion (Shrago, 2024), may be partially sustained through competitive reallocation even after Spirit's exit — at least in the short run.

These results contribute to the literature on ULCC competition and merger policy in two ways. First, they provide the first empirical evidence on fare dynamics during Spirit's collapse, complementing the extensive literature on the Spirit Effect during Spirit's expansion. Second, the competitive backfill finding complicates the policy narrative surrounding the DOJ's 2024 blocking of the JetBlue-Spirit merger: the DOJ argued that preserving Spirit as an independent competitor was essential to maintaining low fares, yet Spirit's subsequent bankruptcy raises the question of whether the competitive benefit the DOJ sought to protect was durable.

The remainder of this paper proceeds as follows. Section 2 provides background on Spirit Airlines and the ULCC model. Section 3 describes the data and methodology. Section 4 presents the results. Section 5 discusses the findings and their limitations.


## 2. Background

### 2.1 Spirit Airlines and the ULCC Model

Spirit Airlines was the largest ultra-low-cost carrier in the United States and a pioneer of the business model in the domestic market. ULCCs are distinguished from traditional low-cost carriers (LCCs) such as Southwest and JetBlue by their significantly lower unit costs, extensive unbundling of ancillary services from base fares, and near-exclusive focus on price-sensitive leisure travelers (Bachwich and Wittman, 2017). Between 2012 and 2019, ULCCs grew from 3.5% to 11.2% of domestic passenger itineraries, with Spirit alone accounting for nearly half of that growth (Shrago, 2024).

The competitive impact of ULCCs differs meaningfully from that of traditional LCCs. Shrago (2024) documents that Spirit's nonstop presence on a route is associated with approximately 15% lower fares at the 10th percentile of the fare distribution but only 8% lower fares at the median, with no significant effect at the 90th percentile. This asymmetric effect — concentrated at the bottom of the fare distribution — reflects ULCCs' targeting of the most price-sensitive travelers. Legacy carriers responded to ULCC expansion by introducing "Basic Economy" fares, with Delta CEO Ed Bastian explicitly describing the product as their "Spirit match fare" (Shrago, 2024).

### 2.2 The JetBlue-Spirit Merger and Aftermath

In July 2022, JetBlue and Spirit announced a merger agreement valued at $3.8 billion. The Department of Justice sued to block the deal, arguing that combining JetBlue and Spirit on approximately 99 metropolitan-overlap routes would eliminate the Spirit Effect and raise fares for millions of consumers. On January 16, 2024, Judge William G. Young of the District of Massachusetts ruled in favor of the DOJ, finding the merger anticompetitive (United States v. JetBlue Airways Corp., Civil Action No. 23-10511-WGY).

The merger's collapse left Spirit in a precarious financial position. The airline filed for Chapter 11 bankruptcy on November 18, 2024, emerged in April 2025 under new CEO Dave Davis, but filed again in August 2025. Throughout 2024 and 2025, Spirit progressively reduced its domestic footprint, cutting over 24% of its flights by mid-2025 and exiting markets including Denver, Houston, Hartford, and Minneapolis. On May 2, 2026, Spirit ceased all operations, citing the inability to sustain operations amid rising fuel costs driven by the war in Iran.


## 3. Data and Methodology

### 3.1 Data

My primary data source is the Bureau of Transportation Statistics' Airline Origin and Destination Survey (DB1B), a 10% sample of domestic airline tickets. I use the DB1B Market table, which reports prorated one-way-equivalent fares for each market segment within an itinerary. I supplement the DB1B with jet fuel spot prices from the Energy Information Administration.

I prepared data from 2022Q1 through 2025Q2, comprising 14 quarters. Following the data cleaning conventions established in Shrago (2024), I applied the following restrictions: I retained only domestic, nonstop itineraries (market coupons equal to one); dropped bulk-fare and tour-operator tickets; excluded fares below $15 and above $1,500 per one-way segment; and dropped observations with missing fare, passenger, distance, or carrier information. After cleaning, the dataset contains approximately 57 million individual ticket observations across 14 quarters.

I aggregated the cleaned data to the route-carrier-quarter level, where a route is defined as a directional airport pair. The aggregated dataset contains 176,405 observations across 12,848 unique routes and 59 ticketing carriers. For each route-carrier-quarter, I computed total passengers, average fare, median fare, and nonstop distance.

### 3.2 Treatment and Control Groups

I define "Spirit-exited routes" as routes where Spirit Airlines operated nonstop service in any quarter of 2022 but did not operate nonstop service in any quarter of 2025. This yields 176 treatment routes. The control group comprises all routes that Spirit did not serve in 2022. In a robustness specification, I restrict the control group to routes with characteristics similar to Spirit's route network: at least two competing carriers and nonstop distance between 400 and 2,000 miles.

I define the post-treatment period as 2024Q4 through 2025Q2, beginning with the quarter of Spirit's Chapter 11 filing in November 2024. The pre-treatment period spans 2022Q1 through 2024Q3.

Table 1 presents summary statistics for the pre-period (2022–2023). Spirit-exited routes have average fares ($224) comparable to control routes ($234), but are systematically different in two respects: they carry more passengers (1,345 per carrier-quarter vs. 620) and face more competition (2.15 carriers per route-quarter vs. 1.43). These differences reflect Spirit's strategy of targeting dense, competitive leisure corridors.

### 3.3 Empirical Strategy

I estimate the effect of Spirit's exit on competitor fares using a difference-in-differences framework. My preferred specification is:

log(fare_rt) = β(SpiritExited_r × Post_t) + γ(LogPassengers_rt) + α_r + δ_t + ε_rt

where r indexes routes and t indexes year-quarters. SpiritExited_r is an indicator equal to one for routes that Spirit exited, Post_t is an indicator for the post-bankruptcy period (2024Q4 onward), α_r represents route fixed effects, and δ_t represents quarter fixed effects. The coefficient of interest is β, which captures the differential change in fares on Spirit-exited routes relative to control routes after the bankruptcy filing, controlling for route-level and quarter-level unobserved heterogeneity.

Route fixed effects absorb all time-invariant characteristics of each route, including distance, endpoint city characteristics, and the baseline level of competition. This ensures that identification comes from within-route changes over time rather than cross-route comparisons. Quarter fixed effects absorb industry-wide shocks that affect all routes equally in a given quarter, including national fuel price movements and macroeconomic conditions.

I estimate the route and quarter fixed effects using the iterative demeaning procedure of Correia (2016), which is the standard approach for high-dimensional two-way fixed effects estimation.

I also estimate three alternative specifications to assess robustness: a simple OLS regression with distance and passenger controls (Model 1); OLS with route fixed effects only, restricted to routes where Spirit carried at least 500 passengers per quarter (Model 2); and the full two-way fixed effects specification restricted to a matched control group of routes with comparable competitive and distance characteristics (Model 4).

All regressions exclude Spirit's own fares to isolate the effect on competitors' pricing behavior.


## 4. Results

### 4.1 Descriptive Evidence

Figure 1 plots the evolution of passenger-weighted average fares on Spirit-exited routes, Spirit-served routes, and never-Spirit routes from 2022Q1 through 2025Q2, indexed to 100 in 2022Q1. Two patterns emerge. First, all three groups exhibit similar seasonal fluctuations, with fares peaking in Q2 and dipping in Q3 — a pattern consistent with the leisure-heavy nature of domestic air travel. Second, Spirit-exited routes (shown in red) consistently underperform the other two groups in fare growth through the pre-bankruptcy period: by 2024Q3, fares on Spirit-exited routes had grown only 0–7% from their 2022Q1 baseline, compared to 10–18% on control routes and Spirit-served routes. At the point of Spirit's bankruptcy filing, Spirit-exited fares briefly converge toward the control group level, rising sharply in 2024Q4 before falling back by 2025Q2. This suggestive visual pattern motivates the formal regression analysis.

Figure 2 illustrates Spirit's domestic operations from 2022 through 2025. Despite expanding its route network through mid-2024 (reaching approximately 620 routes and 850,000 quarterly passengers), Spirit's operations contracted sharply after the bankruptcy filing: by 2025Q2, quarterly passengers had fallen below 650,000, with the steepest declines at airports including Boston (−44%), Los Angeles (−37%), and Chicago O'Hare (−30%).

### 4.2 Regression Results

Table 2 presents the main results across four specifications. The coefficient of interest — the interaction of Spirit route exit with the post-bankruptcy indicator — is small and statistically insignificant in every specification.

In the simple OLS (Model 1), the coefficient is −0.015 (t = −0.58), suggesting a statistically insignificant 1.5% fare decline on Spirit-exited routes relative to controls. However, this estimate is likely biased by unobserved differences between Spirit-exited routes and the broader control group. When I add route fixed effects (Model 2), restricting identification to within-route variation and limiting the treatment to routes where Spirit had strong presence (500+ passengers per quarter), the coefficient becomes +0.013 (t = 1.04) — positive, as hypothesized, but still insignificant.

The preferred two-way fixed effects specification (Model 3) yields a coefficient of +0.013 (t = 0.99), virtually identical to Model 2. Restricting the control group to matched routes with similar competitive characteristics (Model 4) produces a coefficient of −0.009 (t = −1.28). Across all four specifications, the 95% confidence intervals include zero, and I cannot reject the null hypothesis that Spirit's exit had no effect on competitor fares.

Figure 3 presents the coefficient estimates and 95% confidence intervals across all four models visually, illustrating both the small magnitude of the point estimates and the width of the confidence intervals.

### 4.3 Competitive Backfill

To investigate the null fare result, I examine whether other carriers expanded service on Spirit-exited routes after the bankruptcy. Table 3 presents the change in average quarterly passengers per route for the carriers that grew the most on Spirit-exited routes. Delta Air Lines increased its passenger volume by 15.3%, American Airlines by 16.3%, and Southwest Airlines by 13.2%. Frontier Airlines, the other major ULCC, grew by 6.7%.

A difference-in-differences calculation on the number of non-Spirit carriers per route confirms that competitive backfill was complete: Spirit-exited routes gained the same number of carriers as control routes (both +0.02), yielding a DiD of exactly zero. In other words, while Spirit exited these routes, other carriers stepped in to maintain the same level of competition. This finding provides a direct, data-driven explanation for the null fare result: competition was sustained through a different channel.


## 5. Discussion

### 5.1 Interpretation

I find no statistically significant evidence that Spirit Airlines' bankruptcy and route exits raised competitor fares during the initial phase of Spirit's collapse (2024Q4–2025Q2). The point estimates across specifications range from −1.5% to +1.3%, all statistically indistinguishable from zero. This null result is consistent with several explanations that I cannot fully disentangle with the available data.

First, and most directly supported by the data, competition on Spirit-exited routes was largely maintained through competitive reallocation. Delta, American, and Southwest each grew their presence on these routes by 13–16%, effectively replacing the competitive pressure Spirit had provided. This suggests that while the Spirit Effect is real during Spirit's active operation (Shrago, 2024), the competitive discipline it reflects is not solely attributable to Spirit — other carriers are willing and able to fill the gap, at least in the short term and on sufficiently dense routes.

Second, Spirit's competitive withdrawal was gradual rather than sudden. Spirit was financially distressed for nearly two years before its formal bankruptcy filing, and its route network contracted progressively through 2024 and 2025. A gradual erosion of competitive pressure would produce a more diffuse effect that is harder to detect in a difference-in-differences framework than a clean, sudden exit.

Third, the structural response of legacy carriers to ULCC competition — particularly the industry-wide rollout of Basic Economy fares — may have permanently lowered the floor of the fare distribution regardless of Spirit's continued presence. As Shrago (2024) notes, by 2019 all three legacy carriers had deployed Basic Economy fares across their domestic networks, including on routes without ULCC competition. If the competitive response became structural, Spirit's exit would not mechanically reverse it.

Fourth, the available data extends only through 2025Q2 — well before Spirit's complete operational shutdown on May 2, 2026. The full long-run effect of Spirit's disappearance on fares cannot be measured until post-2025Q2 data becomes available.

### 5.2 Implications for Merger Policy

These findings, while preliminary, add nuance to the policy debate surrounding the DOJ's blocking of the JetBlue-Spirit merger. The DOJ's theory of harm rested on the premise that preserving Spirit as an independent competitor was essential to maintaining low fares on overlap routes. Yet Spirit filed for bankruptcy ten months after the merger was blocked, and ultimately ceased operations entirely. If my finding of competitive backfill holds in the long run — that is, if other carriers continue to discipline fares on former Spirit routes — then the competitive benefit may persist even without Spirit, albeit through a different mechanism than the one the DOJ sought to protect.

However, this interpretation warrants significant caution. The backfill I observe occurred on Spirit's existing routes, many of which are dense leisure corridors that are inherently attractive to multiple carriers. Spirit's competitive impact may have been larger on thinner routes or routes where it was the marginal entrant — exactly the markets where backfill is least likely. Additionally, the long-run effect of Spirit's permanent exit may differ from the short-run effect I measure, particularly if the backfilling carriers eventually consolidate or reduce service.

### 5.3 Limitations

Several limitations of this analysis should be noted. The DB1B is a 10% sample of tickets, and the sampling variance is large for thin markets. I mitigate this by focusing on routes with sufficient traffic, but some noise remains. DB1B fares do not include ancillary fees for baggage and seat selection, which are a significant revenue component for ULCCs; to the extent that legacy carriers' fares include more bundled services, fare comparisons may understate the true cost differential (Shrago, 2024). The post-treatment period is short — only three quarters — and Spirit's exit was staggered rather than simultaneous, which attenuates the estimated treatment effect. Finally, the 2025–2026 period saw significant fuel price increases tied to geopolitical events, which I control for through quarter fixed effects but which add noise to the fare data. I cut my sample at 2025Q2 specifically to avoid confounding my estimates with the June 2025 fuel shock.


## References

Bachwich, A. R., and Wittman, M. D. (2017). The emergence and effects of the ultra-low cost carrier (ULCC) business model in the U.S. airline industry. *Journal of Air Transport Management*, 62, 155–164.

Borenstein, S., and Rose, N. L. (1994). Competition and price dispersion in the U.S. airline industry. *Journal of Political Economy*, 102(4), 653–682.

Correia, S. (2016). A feasible estimator for linear models with multi-way fixed effects. Working paper.

Kwoka, J., and Shumilkina, E. (2010). The price effect of eliminating potential competition: Evidence from an airline merger. *Journal of Industrial Economics*, 58(4), 748–770.

Luo, D. (2014). The price effects of the Delta/Northwest airline merger. *Review of Industrial Organization*, 44(1), 27–48.

Morrison, S. A. (2001). Actual, adjacent, and potential competition: Estimating the full effect of Southwest Airlines. *Journal of Transport Economics and Policy*, 35(2), 239–256.

Shrago, B. (2024). The Spirit Effect: Ultra-low cost carriers and fare dispersion in the U.S. airline industry. *Review of Industrial Organization*, 64, 549–579.

United States v. JetBlue Airways Corp., Civil Action No. 23-10511-WGY (D. Mass. Jan. 16, 2024).


## Figures and Tables

[Figure 1: Fare Trends Indexed to 2022 Q1 — figure1b_indexed_trends.png]

[Figure 2: Spirit Airlines' Domestic Operations, 2022–2025 — figure4_spirit_footprint.png]

[Figure 3: Effect of Spirit Exit on Competitor Fares Across Specifications — figure3_coefficients.png]

[Table 1: Pre-Period Summary Statistics]

| | Control Routes | Spirit-Exited Routes | Spirit-Stayed Routes |
|---|---|---|---|
| Average Fare ($) | 233.80 | 223.80 | 221.70 |
| Median Fare ($) | 225.40 | 219.80 | 218.10 |
| Average Distance (mi) | 1,027 | 1,176 | 1,051 |
| Average Passengers/Qtr | 620 | 1,345 | 1,818 |
| Average Carriers/Route | 1.43 | 2.15 | 2.47 |
| N (route-carrier-quarters) | 86,686 | 2,318 | 8,248 |

[Table 2: Regression Results]

| | M1: OLS | M2: Route FE | M3: Route+Qtr FE | M4: Matched Control |
|---|---|---|---|---|
| SpiritExited × Post | −0.015 | +0.013 | +0.013 | −0.009 |
| | (0.026) | (0.013) | (0.013) | (0.007) |
| | t = −0.58 | t = 1.04 | t = 0.99 | t = −1.28 |
| Route FE | No | Yes | Yes | Yes |
| Quarter FE | No | No | Yes | Yes |
| Treatment Routes | 176 | 86 | 86 | 160 |
| N | 112,794 | 112,794 | 112,794 | 20,869 |

[Table 3: Carrier Growth on Spirit-Exited Routes]

| Carrier | Pre (Avg Qtr Pax) | Post (Avg Qtr Pax) | Change | % Change |
|---|---|---|---|---|
| Delta | 2,455 | 2,832 | +377 | +15.3% |
| American | 1,067 | 1,240 | +174 | +16.3% |
| Southwest | 1,119 | 1,268 | +148 | +13.2% |
| Frontier | 1,353 | 1,443 | +90 | +6.7% |
| JetBlue | 1,410 | 1,479 | +69 | +4.9% |
