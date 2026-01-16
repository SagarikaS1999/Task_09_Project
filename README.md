# Research Task 9: Syracuse Open Data Civic Project
# Streets & Safety: Pavement Condition and Fire Hydrant Coverage in Syracuse
## Project Overview
Streets & Safety is a civic data project built using Syracuse Open Data to help residents, community organizations, and city officials better understand the condition of street infrastructure and the distribution of fire hydrants across the city.

The project combines multiple publicly available datasets into a unified analytical framework that highlights patterns, disparities, and trends at the neighborhood level. By presenting infrastructure quality and safety coverage together, the project supports more informed public discussion and transparent decision-making.

## Project Goals
- Provide a clear, neighborhood-level view of pavement condition across Syracuse
- Examine the distribution of fire hydrants as a proxy for public safety infrastructure coverage
- Identify persistent infrastructure challenges that may not be visible in citywide averages
- Create an analysis that is accessible, reproducible, and responsibly interpreted
This project is exploratory and descriptive. It does not make causal claims about safety outcomes or service quality.

## Data Sources
All data used in this project comes from the City of Syracuse Open Data Portal:
- Pavement Ratings (2022–2024)
  - Street segment–level condition inspections conducted by the city
- Fire Hydrants
  - City-maintained inventory of hydrant locations and attributes
Each dataset has known limitations, which are explicitly documented in the exploration report.

## Project Structure
This repository/project includes:
- Exploration Report
A narrative report documenting:
  - Data acquisition and quality assessment
  - Key descriptive statistics
  - Visual analysis of trends and distributions
  - Findings and hypotheses for further investigation
- Data Dictionary
Field-level documentation generated to support transparency and future reuse
- Prepared Datasets
Cleaned and standardized versions of the original data, suitable for aggregation and visualization
- Dashboard (Planned / Phase 3)
An interactive visualization tool presenting neighborhood-level infrastructure patterns

## Key Findings (Phase 2 Summary)
- Pavement inspection coverage is consistent across 2022–2024
- Median pavement condition remains stable, but:
  - The share of poorly rated street segments increased after 2022
  - Poor conditions persist in the same locations across multiple years
- Fire hydrant coverage is geographically comprehensive, but density varies by area

These findings suggest that citywide averages may obscure localized infrastructure challenges.

## Responsible Use and Interpretation
This project follows several guiding principles:
- No causal claims
Pavement condition and hydrant density are descriptive indicators, not measures of service effectiveness or safety outcomes.
- Avoiding neighborhood stigmatization
Results emphasize patterns and disparities rather than rankings or “worst neighborhood” labels.
- Clear documentation of limitations
All known data gaps and assumptions are disclosed.

Users are encouraged to interpret findings as a starting point for discussion, planning, and further analysis—not as definitive evaluations.

## Intended Audience
- Syracuse residents seeking to understand infrastructure conditions in their neighborhood
- Community organizations advocating for targeted improvements
- City staff and officials supporting planning, communication, and transparency
- Journalists and researchers studying urban infrastructure patterns

## Future Work
Planned next steps include:
  - Spatially assigning street segments and hydrants to neighborhoods
  - Aggregating metrics at the neighborhood level
  - Publishing an interactive dashboard for public use
  - Updating the analysis as new pavement rating data becomes available

## Acknowledgments
This project uses data provided by the City of Syracuse Open Data Program and was developed as part of a civic data science initiative aimed at turning open data into actionable public insight.
