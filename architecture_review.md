# Week 6 Architecture Review — Streets & Safety (Syracuse Open Data)
**Project:** Streets & Safety: Neighborhood-Level Pavement Condition + Fire Hydrant Coverage  

---

## 1. System Overview

This project produces a neighborhood-level view of:
- street pavement condition (multi-year: 2022–2024), and
- fire hydrant coverage (citywide inventory)

The system is designed as a transparent, reproducible pipeline that separates:
1) raw data acquisition,  
2) transformation/cleaning,  
3) analysis/aggregation, and  
4) presentation (dashboard + reports).

Primary end users include residents, community organizations, and city staff who need an accessible, defensible way to discuss infrastructure patterns without over-claiming causality.

---

## 2. Data Flow Diagram

```mermaid
flowchart LR
  A[Raw Syracuse Open Data CSVs] --> B[Staging: raw/]
  B --> C[Cleaning & Standardization]
  C --> D[Analysis & Aggregation]
  D --> E[Presentation Layer]

  subgraph Cleaning & Standardization
    C1[Normalize schemas across years]
    C2[Parse dates & standardize categories]
    C3[QA checks: missingness, ranges]
  end

  subgraph Analysis & Aggregation
    D1[Pavement metrics per neighborhood]
    D2[Hydrant count per neighborhood]
    D3[Hydrant density normalization]
    D4[Trend metrics 2022–2024]
  end

  E --> E1[Interactive Dashboard (Power BI)]
  E --> E2[Analytical Report (PDF/MD)]
  E --> E3[Technical Notes + README]
```

> If Mermaid rendering is not available in your environment, include the same diagram as an image or keep the text description below.

### Text description (fallback)
Raw datasets are saved to `data/raw/` without modification. A transformation step produces standardized, cleaned tables in `data/processed/`. Aggregation produces neighborhood-level metrics in `data/curated/`. The dashboard and reports read only from curated outputs to prevent accidental leakage of uncleaned or inconsistent inputs.

---

## 3. Key Design Decisions (and Rationale)

### 3.1 Neighborhood as the primary aggregation unit
**Decision:** Aggregate both pavement segments and hydrants to neighborhood boundaries.  
**Rationale:** Neighborhoods are understandable to residents and stable enough for city communication. Pavement segments and hydrant points are too granular for most non-technical audiences.

### 3.2 Clear separation of “presence” vs “performance”
**Decision:** Treat hydrant density as *coverage proxy*, not response capacity.  
**Rationale:** Hydrant location does not measure water pressure, staffing, turnout time, or operational readiness. The project avoids causal claims by design.

### 3.3 Multi-year pavement trend support
**Decision:** Standardize 2022–2024 pavement schemas into a single unified representation.  
**Rationale:** Trend analysis prevents overreacting to one-year snapshots and enables identification of persistent low-condition areas.

---

## 4. Metric Definitions (Contract)

### Pavement (Neighborhood-level)
- **Average pavement rating:** mean of segment ratings (optionally length-weighted if segment length is reliable)
- **Percent poor segments:** share of segments with rating ≤ 4 (threshold documented and adjustable)
- **Trend metrics:** year-over-year changes in mean rating and percent poor

### Hydrants (Neighborhood-level)
- **Hydrant count:** number of hydrants within neighborhood boundaries
- **Hydrant density (optional):** hydrants per street-mile (preferred) or per neighborhood area (fallback), with explicit labeling

---

## 5. Dependencies and Deployment Considerations

### Data dependencies
- Pavement ratings (2022–2024) CSVs  
- Fire hydrants CSV  
- Neighborhood boundary layer (GeoJSON / Shapefile / Feature layer export)

### Tooling dependencies (typical)
- Python environment for data prep and QA
- Power BI Desktop for dashboard authoring
- Optional: a lightweight scheduled refresh process for future updates

### Deployment / sharing options
- Publish dashboard to a workspace or share `.pbix` file
- Export report as PDF for portal inclusion
- Provide curated CSV outputs so non-PowerBI users can reproduce visuals

---

## 6. Quality Assurance Approach

### Validation checks (examples)
- Row counts stable year-to-year for pavement segments
- Rating range sanity checks (expected 0–10)
- Category values consistent across years
- No large unexpected increase in missingness after standardization
- Hydrant coordinate completeness checks

### Unit tests (critical calculations)
- “Percent poor” calculation correctness
- Aggregation totals consistency (sum of neighborhood counts equals global counts)
- Density normalization correctness (if used)

### Narrative validation
Any narrative statements in reports or dashboard tooltips must be traceable to computed metrics. Claims are phrased descriptively (“higher/lower”, “increased/decreased”) with uncertainty notes when appropriate.

---

## 7. Current Progress (Week 6)

- Completed Phase 2 exploration report and data dictionaries
- Confirmed multi-year pavement comparability at a high level
- Identified hydrant operational-field missingness and scoped hydrant metrics to presence/density
- Prepared standardized multi-year pavement structure for aggregation

---

## 8. Blockers / Risks

### Blocker: Neighborhood boundary integration
Neighborhood aggregation requires a boundary dataset and spatial assignment. If boundary data is not available in a compatible format, a fallback aggregation (ward-based) can be used temporarily for prototype development.

### Risk: Proxy misinterpretation
Hydrant density can be mistakenly interpreted as response effectiveness. Mitigation: strong labeling, disclaimers, and careful default views.

---

