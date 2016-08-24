# Homeserver Backup

This is a small pyhton application which will execute a backup using an rsync pull. The application is meant to be run on the server, and the target hosts should be configured such that the server can pull files and use these as a backup. 

## Features

- Backup specific folders
- Configure multiple machines
- Use the latest backup with hard links, to preserve hard disk space

