# Google Dorking

Simple utility that generates Google dorks from a list of domains.

<img width="421" height="135" align="center" alt="image" src="https://github.com/user-attachments/assets/194af851-9b09-4615-82dd-cf93ff62e600" />


What it does

* Reads `domains.txt` (one domain per line, `*.example.com` allowed).
* Normalizes domains by removing a leading `*.`.
* Groups domains into batches (default: 6 per batch).
* Builds a dork for each batch in the form:

<img width="1343" height="145" alt="image" src="https://github.com/user-attachments/assets/fb0fc6c7-5bed-4201-b25f-e522ccb57496" />

  (the trailing filter is configurable).
* Writes all generated dorks to `dorks.txt`.


Usage

* Put input domains in `domains.txt` (one per line).
* Run the script. It generates `dorks.txt` with one dork per line.
* Change `batch_size` or the `suffix` (e.g., `inurl:".git/config"`) in the script to produce other dork variants.
