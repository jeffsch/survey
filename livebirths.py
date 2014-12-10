import survey

table = survey.Pregnancies()
table.ReadRecords()
livebirths = 0
for record in table.records:
    if (record.nbrnaliv != 'NA'):
        livebirths += record.nbrnaliv

print livebirths
