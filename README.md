# coffeedates

A little utility for generating matches for coffee dates.

Matches are optimized for people who haven't been matched before, or if that is not possible, for matches in the more distant past.

Run the utility to create a new dataset:
```
$> ./coffeeDates.py
No Datasets available.  You must create one first...
What is the new dataset called? KitchenerOffice
Dataset has been created for KitchenerOffice. Please add participants to the file ./KitchenerOffice/participants.txt
$>
```
Add your participants to the participants.txt file:
```
Simon Clark:sclark
Dana Loy:dloy
Albert Zhong:azhong
Miriam Novotny:mnovot
```
Run the utility again to generate the matches:
```
$> ./coffeeDates.py

1: KitchenerOffice
C: Create new dataset...

Which dataset do you want to generate matches for? 1
Generating matches for ./data/KitchenerOffice
4 Participants found.
2020-09-25 15:17:58.777407

@azhong is paired with @dloy
@mnovot is paired with @sclark

Weighting: 0.000000
Do you wish to proceed? (Y/N) y
Committing matches
$>
```
Copy and paste the matches to your slack channel
