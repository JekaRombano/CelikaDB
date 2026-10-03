from CELIKA.celika import *


db = celikaDB()


# Connect to the existing Celika DB database.
# This allows the program to access the database storage
# and load any previously saved data into memory.
# The connection must be established before performing
# database operations such as creating, inserting, or searching data.
db.connect()


# Create two separate groups that will represent users.
# Each group acts as a container for related information.
# The group title is used to identify and access the stored data.
# In this example, two users are created so that the database
# can demonstrate how multiple groups can exist at the same time.
db.createGroup(title="user1")
db.createGroup(title="user2")


# Insert information into the user groups.
# Each group can contain multiple key-value pairs that describe
# the information associated with that particular user.
# The "call" parameter identifies which group will receive the data.
# The "template" parameter contains the actual information being stored.
db.insertChildren(
    call="user1",
    template={
        "username": "jeka",
        "password": "1234",
        "age": 18
    }
)

db.insertChildren(
    call="user2",
    template={
        "username": "trini",
        "password": "5678",
        "age": 19
    }
)


# Update an existing value inside a group.
# This demonstrates that stored information can be modified
# without having to recreate the entire group.
# In this example, the age of user1 is changed from 18 to 19.
# The title identifies the group, while the key identifies
# the specific value that needs to be updated.
db.updateChildren(
    title="user1",
    key="age",
    value=19
)


# Retrieve a specific value from the database.
# Instead of displaying the entire user group, getChildren()
# can be used to access only the requested information.
# Here, the program retrieves the updated age of user1.
# This demonstrates how specific pieces of stored data can be accessed.
print("\nUser 1 Age:")
print(
    db.getChildren(
        title="user1",
        key="age"
    )
)


# Search for stored information using a group's title.
# The search operation allows the database to locate
# a specific group without manually accessing the database structure.
# In this example, the program searches for the group named user1.
# The returned result represents the information associated with that group.
print("\nSearch Result:")
print(
    db.search(
        title="user1"
    )
)


# Display all keys currently stored in the database.
# Keys represent the names or fields used to identify
# individual pieces of information inside the database.
# This is useful for examining the structure of the stored data
# without displaying every value associated with those keys.
print("\nAll Keys:")
print(db.showAllKeys())


# Display all values currently stored in the database.
# Values represent the actual information associated with
# the keys inside the database groups.
# This provides a simple way to inspect the data currently stored.
print("\nAll Values:")
print(db.showAllValue())


# Display the current database structure.
# This shows the database as it currently exists in memory
# after the groups have been created and the data has been modified.
# It allows the user to inspect the current state before
# the changes are saved to permanent storage.
print("\nCurrent Database:")
print(db.database())


# Save the current database state to permanent storage.
# The listen() operation synchronizes the current in-memory
# database with the stored database files.
# This ensures that the changes made during the program execution
# are preserved and can be loaded again in a future session.
db.listen()


# Display the database after it has been saved.
# This allows the user to verify that the current database
# has been successfully written to its storage.
# It also demonstrates the difference between the in-memory
# database and its persisted storage state.
print("\nStored Database:")
db.showDatabase()


# Remove a group from the database.
# In this example, user2 is removed from the database.
# The verify parameter is disabled so the operation can be
# performed directly without requesting an additional verification code.
# This demonstrates how an existing group can be deleted from the database.
db.removeChildren(
    title="user2",
    verify=False
)


# Save the database again after removing user2.
# The previous save stored both users, but the removal operation
# only changes the current database state in memory.
# Calling listen() again ensures that the deletion is also
# reflected in the permanent database storage.
db.listen()


# Display the final state of the database.
# This allows the user to confirm that user2 has been removed
# while user1 and its information remain available.
# It serves as the final verification of the create, insert,
# update, retrieve, search, save, and remove operations demonstrated above.
print("\nDatabase After Removal:")
db.showDatabase()
