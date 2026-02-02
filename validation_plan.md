# Validation & QA Plan

## Purpose
Ensure that all metrics, visuals, and narrative statements are:
- numerically correct,
- reproducible from raw inputs, and
- responsibly interpreted.

## A. Data QA (before metrics)
- Missingness profile for each dataset (raw vs processed)
- Field type consistency checks (ratings numeric, dates parseable)
- Outlier checks (rating bounds, negative lengths, impossible coords)

## B. Metric QA (critical calculations)
1) **Percent poor segments**
- Definition: rating ≤ 4
- Test: known small sample where manual computation matches output

2) **Neighborhood totals**
- Pavement: sum of neighborhood segment counts equals citywide segment count
- Hydrants: sum of neighborhood hydrant counts equals citywide hydrant count
- If mismatch occurs: investigate boundary overlaps, unassigned points, or invalid geometries

3) **Density normalization**
- If using hydrants per street-mile:
  - validate denominator (street miles) is computed consistently
- If using area-based fallback:
  - confirm neighborhood areas are in consistent units

## C. Visual QA (dashboard/report)
- Cross-check KPI cards vs curated table totals
- Confirm filters change only relevant visuals
- Tooltips match definitions in Technical Notes

## D. Narrative QA (LLM + human authored)
- Every claim maps to one or more metrics
- Avoid causal language
- Include uncertainty notes for proxies and missing fields
- Use neutral language to avoid stigmatizing neighborhoods

## E. Evidence artifacts (keep for handoff)
- A saved snapshot of curated metric tables
- Prompt log with validation outcomes
- Unit test results summary
