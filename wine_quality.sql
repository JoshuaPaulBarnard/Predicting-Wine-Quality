DROP TABLE IF EXISTS wine_quality;
CREATE TABLE IF NOT EXISTS wine_quality (
    wine_ID INTEGER PRIMARY KEY,
    quality INTEGER,
    Red_Wine INTEGER,
    White_Wine INTEGER,
    wine_type STRING,
    fixed_acidity DECIMAL,
    volatile_acidity DECIMAL,
    citric_acid DECIMAL,
    residual_sugar DECIMAL,
    chlorides DECIMAL,
    free_sulfur_dioxide DECIMAL,
    total_sulfur_dioxide DECIMAL,
    density DECIMAL,
    pH DECIMAL,
    sulphates DECIMAL,
    alcohol DECIMAL
);