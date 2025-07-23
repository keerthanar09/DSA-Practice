## Getting Started

Welcome to the VS Code Java world. Here is a guideline to help you get started to write Java code in Visual Studio Code.

## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

Meanwhile, the compiled output files will be generated in the `bin` folder by default.

> If you want to customize the folder structure, open `.vscode/settings.json` and update the related settings there.

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).


## HASHING

Hashing is a technique used to effectively store and retrieve data and allows for quick access of data. It makes use of the concept of MAPPING, where the data is mapped to a specific index in a hash table ( an array of items) using a hash function. 

The retrieval of information is done based on it's key.

Search, insert and delete operations all can be performed with an average of O(1) time even for large datasets.

It's mainly used to implement a set of distinct items (keys) and dictionaries (key value pairs).

The key's information content is used to determine a unique value called the hash code. This hash code is used as the index at which the data associated with the key is stored. The transformation of the key to its hashcode is not seen by the user and is performed automatically - you never see the hash code itself. 
