# Project Structure & Reproducibility Notes

This structure supports a clean separation of concerns:

```
project/
  data/
    raw/            # untouched downloads from data.syr.gov
    processed/      # cleaned/standardized tables
    curated/        # neighborhood-level metric tables used by dashboards/reports
  notebooks/        # exploration + development notebooks (optional)
  reports/
    phase2_exploration_report.md
    phase3_analytical_report.md
  dashboards/
    streets_safety.pbix
    prompt_log.md   # prompt iterations + validation notes
    test_metrics.py
    technical_notes.md
  README.md
  requirements.txt
```

## Reproducibility Rules
- Raw data is never edited in-place.
- Processed/curated outputs can always be regenerated from raw inputs.
- Dashboard connects only to curated outputs (contract tables).

