## How It Works

Celika DB uses a **local, file-based NoSQL architecture** where database information is organized and stored using JSON files. When the system is initialized, it creates the required database environment and separates its responsibilities into three main areas: **DATA, INDEX, and LOG**. The DATA directory contains the actual database records, the INDEX directory is used to maintain information for identifying and organizing records, and the LOG directory stores important database metadata and update information.

When Celika DB connects, it loads the stored database information into its temporary in-memory database. This allows operations to be performed efficiently while the system is running. Users can create groups to organize related records, insert key-value data into those groups, update existing values, retrieve specific information, and search through the stored data. Groups are identified using their titles and identities, allowing the database to distinguish between different sets of records.

After changes are made, Celika DB can synchronize the current in-memory database with its persistent JSON storage. This allows the data to remain available even after the program is closed and started again. The database can also remove specific groups when necessary, while its clearing mechanism provides verification before permanently clearing stored data and indexes.

Celika DB also maintains a logging system that records important information about the database, including its name, version, file name, creation date, creation time, and most recent update. The initial log information is created when the database environment is initialized, while later operations update only the **Last Updated** value. This keeps the original creation information intact while providing a record of when the database was last modified.

The architecture is intentionally designed to be simple, modular, and expandable. The current local implementation serves as the core foundation for the planned **Celika DB Web Database**, allowing the project to potentially grow into a web-based or cloud-enabled database system while maintaining the same underlying database concepts.

speical thanks to my girlfriend for being the inspiration of CelikaDB because she is very organized.
