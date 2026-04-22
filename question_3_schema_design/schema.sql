-- User Inputs Table
CREATE TABLE user_inputs (
    id UUID PRIMARY KEY,
    user_id UUID,
    input_text TEXT,
    input_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Predictions Table
CREATE TABLE predictions (
    id UUID PRIMARY KEY,
    input_id UUID REFERENCES user_inputs(id),
    prediction_text TEXT,
    confidence_score FLOAT,
    model_version VARCHAR(50),
    latency_ms INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);