# HNG Stage 0 Backend Task

## Description
A simple Django API that returns a JSON response containing personal details, the current datetime (West Africa Time), and a random cat fact.

## Endpoint
**GET** `/api/`

### Sample Response
```json
{
  "full_name": "Paul Ebonka",
  "email": "paulebonka4sure@gmail.com",
  "github_url": "https://github.com/Clever2Sure/hng_stage_zero_backend",
  "current_datetime": "2025-10-23T20:10:15.234123+01:00",
  "cat_fact": "Cats sleep for 70% of their lives."
}
