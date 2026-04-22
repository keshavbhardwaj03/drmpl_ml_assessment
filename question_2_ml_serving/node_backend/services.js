const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());

app.post("/api/predict", async (req, res) => {
  try {
    const response = await axios.post("http://ml_service:8000/predict", {
      text: req.body.text
    });

    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: "ML service error" });
  }
});

app.listen(3000, () => {
  console.log("Node backend running on port 3000");
});