# Database Management System (DBMS)

## What is a Database?

- A **database** is a structured collection of inter-related data that is stored and accessed electronically.
- Common operations on databases include:
    - Insertion
    - Deletion
    - Retrieval

- Data is organized using tables, schemas, views, and reports.

**Example**: A college database may store information about administrators, staff, students, and faculty members in an organized format.

---

## What is a Database Management System (DBMS)?

- A **DBMS** is software used to manage and interact with databases.
- Popular examples: **MySQL**, **Oracle**, **PostgreSQL**, **MongoDB**.
- A DBMS provides functionalities such as:
  - Creating databases and tables
  - Storing and updating data
  - Enforcing security and access controls
  - Maintaining data consistency during concurrent access
  - Performing backups and recovery

---

## Tasks Performed by Users in a DBMS

- **Data Definition**
  - Creating, modifying, and removing database schema or tables

- **Data Updation**
  - Inserting, modifying, and deleting data records

- **Data Retrieval**
  - Querying the database to retrieve relevant data for applications or reports

- **User Administration**
  - Registering and managing users
  - Enforcing data security and access controls
  - Maintaining data integrity
  - Managing concurrency
  - Monitoring performance
  - Handling failure recovery

---

| Feature | DBMS | File System |
|--------|------|-------------|
| **Data Handling** | Collection of data; user doesn't need to write procedures to manage data | Collection of data; user must write procedures to manage data |
| **Data Sharing** | Centralized approach makes sharing easy | Data is distributed across files in various formats, making sharing difficult |
| **Abstraction** | Provides abstraction; hides data storage details | Exposes how data is stored and represented |
| **Crash Recovery** | Offers recovery mechanisms to protect data in case of system failure | Lacks built-in crash recovery features |
| **Data Manipulation** | Provides various efficient manipulation techniques | Limited capabilities for efficient data manipulation |
| **Concurrent Access** | Supports safe concurrent access via locking mechanisms | Prone to problems during concurrent access |
| **Data Volume Handling** | Handles large volumes of interrelated data effectively | Struggles with large and interrelated datasets |
| **Cost** | Generally more expensive due to added features | Typically cheaper to implement |
| **Redundancy & Inconsistency** | Controlled via centralization and constraints | High chance of duplication and inconsistency |
| **Structure** | Complex structure to support advanced functionalities | Simple structure with fewer features |
| **Data Independence** | Supports: <br> - Logical Data Independence <br> - Physical Data Independence | No concept of data independence |
| **Integration** | Easy integration with other systems and tools | Difficult to integrate with modern applications |
| **Data Models** | Supports models like: <br> - Hierarchical Model <br> - Network Model <br> - Relational Model | No formal data model approach |
| **Flexibility** | High flexibility in modification, retrieval, and storage | Limited flexibility |
| **Query Language** | Supports complex querying through SQL | No built-in query language |
| **Examples** | Oracle, MySQL, SQL Server | COBOL, C++ file-based systems |

---

## Key Characteristics of DBMS

- Centralized digital repository to store structured data
- Logical and consistent view of data with abstraction from low-level details
- Automatic backup and recovery systems
- Follows **ACID properties** for transaction safety:
  - **A**tomicity
  - **C**onsistency
  - **I**solation
  - **D**urability
- Reduces complex data relationships
- Offers secure multi-user access
- Allows multiple views depending on user roles

---

## Advantages of DBMS

- **Minimizes Redundancy**: Stores all data in one place to reduce duplication
- **Data Sharing**: Enables multiple authorized users to access the data
- **Easy Maintenance**: Centralized system is easier to maintain and update
- **Development Efficiency**: Reduces development time
- **Automatic Backup**: Supports backup and recovery for data safety
- **Multiple Interfaces**: Offers graphical and programmatic interfaces

---

## Disadvantages of DBMS

- **High Cost**: Requires advanced hardware, software, and trained personnel
- **Storage Requirements**: Occupies significant disk and memory space
- **System Complexity**: Adds complexity to system design and architecture
- **Failure Impact**: A failure in a centralized DBMS can impact the entire organization’s data

---