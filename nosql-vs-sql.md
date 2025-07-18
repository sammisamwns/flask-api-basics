# NoSQL vs SQL

Understanding the difference between NoSQL and SQL databases is essential when designing data-driven applications. Here's a breakdown based on key aspects:

| Feature             | SQL (Relational DB)                           | NoSQL (Non-relational DB)                                     |
| ------------------- | --------------------------------------------- | ------------------------------------------------------------- |
| **Data Structure**  | Tables (rows and columns)                     | Documents, key-value pairs, graphs, wide-columns              |
| **Schema**          | Fixed schema (predefined structure)           | Dynamic schema (flexible, schema-less)                        |
| **Scalability**     | Vertical (scale-up: add more power to server) | Horizontal (scale-out: add more servers)                      |
| **Examples**        | MySQL, PostgreSQL, Oracle, MS SQL Server      | MongoDB, Redis, Cassandra, Firebase, CouchDB                  |
| **Query Language**  | SQL (Structured Query Language)               | Varies: MongoDB uses JSON-like query syntax                   |
| **ACID Compliance** | Strong ACID (Atomicity, Consistency, etc.)    | BASE (Basically Available, Soft state, Eventually consistent) |
| **Joins Support**   | Supports JOIN operations                      | Generally does not support JOINs                              |
| **Use Cases**       | Financial systems, legacy enterprise apps     | Real-time apps, IoT, big data, content management             |
| **Data Integrity**  | Enforced via constraints, relations           | Handled at application level (if needed)                      |
| **Performance**     | Slower on large, distributed datasets         | High performance for read/write-heavy apps                    |

## Summary

* **Use SQL databases** when your application requires strong consistency, complex queries, and structured data with relationships.
* **Use NoSQL databases** when you need scalability, fast development, and flexibility in storing unstructured or semi-structured data.

## Reference Example

```json
// Example MongoDB Document
{
  "name": "Sam",
  "email": "sam@example.com",
  "roles": ["admin", "user"],
  "profile": {
    "age": 24,
    "location": "India"
  }
}
```

```sql
-- Equivalent SQL Table Structure
CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  age INT,
  location VARCHAR(100)
);
```

## Suggested Tools

* **SQL GUI**: DBeaver, MySQL Workbench, pgAdmin
* **NoSQL GUI**: MongoDB Compass, RedisInsight

---
