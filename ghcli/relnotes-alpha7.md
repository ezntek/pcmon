## release notes for pcmon alpha 7

* bug fixes to the initial bring up:
  * Fix some file creation errors in DataIO
  * Return statement handling
* added pcmon-specific information, saved in the json/*pcmon_name*-metadata.json file.
* made the bring-up implementation more stable

WIP:
  * debug console
  * pcmod (mod framework)
In Testing:
  * ATM
  * DataIO
  * Debug Console


**Preferably ran with pypy3 version 3.7 (on our main machines).**
*also tested with cpython 3.10*
