import { MongoClient } from "mongodb";

const connectionString = process.env.MONGODB_URI || "";

const client = new MongoClient(connectionString, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

let conn;
try {
  conn = await client.connect();
  console.log("Connected successfully to MongoDB");
} catch (e) {
  console.error("Failed to connect to MongoDB", e);
  process.exit(1);
}

let db = conn.db("sample_training");

export default db;
