# Vedischeck
Simple code that creates random values asynchronously, and writes and reads the database. 
Was made to check Vedis database if it is fine for my remote projects.

original project:

https://github.com/symisc/vedis

pythonised:

https://github.com/coleifer/vedis-python

issues, reported this trouble:

1) https://github.com/coleifer/vedis-python/issues/21
2) https://github.com/symisc/vedis/issues/21


Recieving trouble of this kind every time on different VPS, but works fine on home laptop:


----------------------------------
2022-12-21 12:16:48.042288
Traceback (most recent call last):
  File "/home/vedischeck/dbworker.py", line 30, in write_user_attribute
    db[f'{user_id}{attribute}'] = data
  File "vedis.pyx", line 383, in vedis.Vedis.__setitem__
  File "vedis.pyx", line 311, in vedis.Vedis.store
  File "vedis.pyx", line 425, in vedis.Vedis.check_call
OSError: b'IO error while opening journal file: /home/vedischeck/main.vdb_vedis_journal\n'

----------------------------------
2022-12-21 12:16:48.061854
Traceback (most recent call last):
  File "/home/vedischeck/dbworker.py", line 30, in write_user_attribute
    db[f'{user_id}{attribute}'] = data
  File "vedis.pyx", line 383, in vedis.Vedis.__setitem__
  File "vedis.pyx", line 311, in vedis.Vedis.store
  File "vedis.pyx", line 425, in vedis.Vedis.check_call
OSError: b'IO error while opening the target database file: /home/vedischeck/main.vdb\n'
(venv) root@vm3616877:/home/vedischeck#


async_read - None
1007
async_write - True
1008
async_read - None
1009
async_write - True
1010
async_read - None
1011
async_write - False
1012
async_read - 965939
1013
async_write - False
1014
async_read - False
1015
async_write - False
1016
async_read - False
1017
async_write - False 
