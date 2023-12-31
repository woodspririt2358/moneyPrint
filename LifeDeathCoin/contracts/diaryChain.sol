// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DiaryChain {
    struct DiaryEntry {
        string date;           // Datum im Format "YYYY-MM-DD"
        string time;           // Uhrzeit im Format "HH:MM"
        string category;       // Kategorie des Eintrags
        string name;           // Name oder Titel des Eintrags
        string description;    // Beschreibung oder Inhalt des Eintrags
        bool isLifeEvent;      // Boolean für Leben oder Tod
    }

    DiaryEntry[] private entries;

    function addEntry(
        string memory _date, 
        string memory _time, 
        string memory _category, 
        string memory _name, 
        string memory _description,
        bool _isLifeEvent
    ) public {
        entries.push(DiaryEntry(_date, _time, _category, _name, _description, _isLifeEvent));
    }

    function getEntry(uint index) public view returns (string memory, string memory, string memory, string memory, string memory, bool) {
        require(index < entries.length, "Index ausserhalb der Reichweite");
        DiaryEntry memory entry = entries[index];
        return (entry.date, entry.time, entry.category, entry.name, entry.description, entry.isLifeEvent);
    }

    function getEntryCount() public view returns (uint) {
        return entries.length;
    }
}
