# Schema Design for User Inputs & Predictions

## Problem Statement

Design a simple database schema to store:

* User inputs (e.g., prompts, leads)
* Model predictions associated with those inputs

## Schema Design

### 1. User Inputs Table

| Field Name | Data Type  | Description                      |
| ---------- | ---------- | -------------------------------- |
| id         | UUID / INT | Primary key                      |
| user_id    | UUID / INT | Reference to user                |
| input_text | TEXT       | User input (prompt/lead text)    |
| input_type | VARCHAR    | Type (prompt, lead, query, etc.) |
| created_at | TIMESTAMP  | Input creation time              |
| updated_at | TIMESTAMP  | Last updated time                |

### 2. Predictions Table

| Field Name       | Data Type  | Description                    |
| ---------------- | ---------- | ------------------------------ |
| id               | UUID / INT | Primary key                    |
| input_id         | UUID / INT | Foreign key → User Inputs      |
| prediction_text  | TEXT       | Model output / prediction      |
| confidence_score | FLOAT      | Confidence / similarity score  |
| model_version    | VARCHAR    | Model version used             |
| latency_ms       | INT        | Time taken for prediction (ms) |
| created_at       | TIMESTAMP  | Prediction timestamp           |

## Relationship

* One **user input** can have **multiple predictions**
* `input_id` in the predictions table links back to the user input

## Design Considerations

* Supports multiple ML models via `model_version`
* Enables monitoring using `latency_ms`
* Allows tracking and auditing via timestamps
* Flexible for different input types (prompts, leads, queries)

## Possible Extensions

* Add `status` field (success/failure)
* Store embeddings (for similarity search)
* Add `response_metadata` (JSON field)
* Introduce indexing on `input_text` for faster search

## Files Included

* `schema.sql` → SQL table definitions
* `README.md` → Schema explanation
