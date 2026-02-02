# Prompt Log & Validation Notes  
**Project:** Streets & Safety — Syracuse Open Data Civic Project  
**Phase:** Phase 3 (Architecture Review)

This log documents the controlled use of large language models (LLMs) in support of analysis, documentation, and communication. LLMs are not used for calculations, spatial joins, or metric generation. All numerical results originate from direct data analysis and are independently validated.

---

## Prompt Iteration 1: Plain-Language Summary of Pavement Trends

- **Date:** 2026-01-31  
- **Goal:**  
  Generate a plain-language summary of observed pavement condition trends across 2022–2024 for a non-technical audience.

- **Input context provided:**  
  - Computed summary statistics (mean rating, median rating, percent of segments rated poor)  
  - Instruction that results are descriptive and non-causal  
  - Guidance to avoid neighborhood rankings or stigmatizing language  

- **Prompt text:**  
  > “Using the following computed summary statistics for pavement ratings from 2022–2024, write a plain-language summary suitable for city residents. Do not make causal claims, do not rank neighborhoods, and clearly note that the data reflects inspection snapshots.”

- **Model output summary:**  
  - Described stability in median pavement ratings  
  - Noted an increase in the share of poorly rated segments after 2022  
  - Used cautious, non-causal phrasing

- **Validation method:**  
  - Cross-checked all numeric references against computed statistics  
  - Reviewed language for causal implications or unsupported claims  

- **Validation result:**  
  ✅ Pass

- **Edits made after validation:**  
  - Replaced causal language with descriptive phrasing  
  - Added an explicit note that pavement ratings reflect inspection snapshots

- **Notes on uncertainty / bias:**  
  - Avoided attributing responsibility or causes  
  - Ensured wording did not stigmatize specific neighborhoods

---

## Prompt Iteration 2: Identification of Hypotheses for Further Analysis

- **Date:** 2026-01-31  
- **Goal:**  
  Generate hypotheses for further investigation based on observed exploratory patterns.

- **Input context provided:**  
  - Summary of exploratory findings from Phase 2  
  - Explicit instruction to frame outputs as hypotheses, not conclusions  

- **Prompt text:**  
  > “Based on these exploratory findings, suggest 3–4 hypotheses that could be investigated next. Clearly label them as hypotheses and avoid definitive claims.”

- **Model output summary:**  
  - Suggested spatial concentration of poorly rated pavement segments  
  - Suggested persistence of low-condition segments across years  
  - Proposed examining alignment between pavement condition and hydrant density

- **Validation method:**  
  - Confirmed each hypothesis was consistent with observed patterns  
  - Checked that no hypothesis implied causation or policy recommendations  

- **Validation result:**  
  ✅ Pass

- **Edits made after validation:**  
  - Added clarification that hypotheses require neighborhood-level aggregation  
  - Removed speculative language about potential causes

- **Notes on uncertainty / bias:**  
  - Clearly labeled outputs as hypotheses  
  - Avoided deficit-based or judgmental framing

---

## Prompt Iteration 3: Drafting Dashboard Disclaimers and Tooltips

- **Date:** 2026-01-31  
- **Goal:**  
  Draft concise disclaimer language explaining proxy measures and data limitations for a public-facing dashboard.

- **Input context provided:**  
  - Definition of hydrant density as a proxy for infrastructure coverage  
  - Known limitations of pavement inspection data  

- **Prompt text:**  
  > “Draft short disclaimer text for a public dashboard explaining that hydrant density is a proxy for infrastructure coverage and does not measure emergency response effectiveness.”

- **Model output summary:**  
  - Produced clear, accessible disclaimer language  
  - Explicitly separated infrastructure presence from performance or effectiveness  

- **Validation method:**  
  - Reviewed alignment with documented assumptions and limitations  
  - Checked for clarity and absence of misleading implications  

- **Validation result:**  
  ✅ Pass

- **Edits made after validation:**  
  - Simplified language for non-technical audiences  
  - Added reference to inspection-based nature of pavement ratings

- **Notes on uncertainty / bias:**  
  - Ensured disclaimers are visible and explicit  
  - Avoided language that could falsely reassure or alarm users

---

## Summary of LLM Usage

- LLMs are used only for:
  - Plain-language summarization  
  - Hypothesis framing  
  - Documentation and disclaimer drafting  

- LLMs are **not** used for:
  - Calculations  
  - Spatial analysis  
  - Metric generation  
  - Decision-making or ranking  

- All LLM outputs are:
  - Validated against ground-truth calculations  
  - Reviewed for bias and over-claiming  
  - Edited prior to inclusion in any deliverable  

This approach ensures that LLM assistance improves clarity and accessibility while preserving analytical rigor and civic responsibility.