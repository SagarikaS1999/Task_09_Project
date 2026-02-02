# Technical Notes — Streets & Safety

## Datasets
- Pavement ratings (2022–2024): street-segment inspection snapshots
- Fire hydrants: point locations of hydrants maintained by the city
- Neighborhood boundaries: used for aggregation

## Core metrics
### Pavement
- Mean rating by neighborhood (optionally length-weighted)
- Percent of segments rated poor (rating ≤ 4)
- Trend metrics across years

### Hydrants
- Hydrant count by neighborhood
- Hydrant density (normalized) when a defensible denominator is available

## Interpretation constraints
- Hydrant density is a proxy for infrastructure presence, not response effectiveness.
- Pavement ratings are periodic inspections, not real-time conditions.
- Neighborhood aggregation smooths within-neighborhood variability.

## Known data limitations
- No shared join key across datasets
- Some hydrant operational fields have high missingness; location fields are reliable for presence analysis
