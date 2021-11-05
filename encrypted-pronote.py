import json
import os
import pronotepy
import telegram
import time
from pronotepy.dataClasses import *

client = pronotepy.Client('https://3500002a.index-education.net/pronote/eleve.html',
                          username=str(os.environ.get('username')),
                          password=str(os.environ.get('password')))

i = 0
while i == 0:
    if client.logged_in:
        notes = []
        periods = client.periods
        filename = "grades.json"
        for grade in periods[-1].grades:
            notes.append(grade.grade)

        with open(filename, "r") as read_file:
            notes_old = json.load(read_file)

        with open(filename, 'w') as file_object:
            json.dump(notes, file_object, indent=3)

        s = set(notes_old)
        diff = [x for x in notes if x not in s]

        if diff != []:
            token = '2139097942:AAGV2nDtmGmKGF0MXuH3o-qU7vf-PL0Htg8'
            chat_id = '971617548'
            bot = telegram.Bot(token=token)
            message = f"Vous avez une nouvelle note de {periods[-1].grades[-1].grade}/{periods[-1].grades[-1].out_of} en {periods[-1].grades[-1].subject.name} et votre moyenne est maintenant de {periods[-1].overall_average}"
            note_last = periods[-1].grades[-1].grade
            bot.sendMessage(chat_id=chat_id, text=message)
        else:
            token = '2139097942:AAGV2nDtmGmKGF0MXuH3o-qU7vf-PL0Htg8'
            chat_id = '971617548'
            bot = telegram.Bot(token=token)
            message="rien de nouveau..."
            bot.sendMessage(chat_id=chat_id, text=message)
    time.sleep(600)
        # with open(filename, "r") as read_file:

            #notes_old = json.load(read_file)
    """
        with open(filename, 'wb') as f:
            pickle.dump(notes, f, protocol=pickle.HIGHEST_PROTOCOL)
        def load_object(filename):
            try:
                with open(filename, "rb") as f:
                    return pickle.load(f)
            except Exception as ex:
                print("Error during unpickling object (Possibly unsupported):", ex)
        obj = load_object("data.pickle")
        print(obj)
    """
    # s = set(notes_old)

    #  diff = [x for x in notes if x not in s]
    """
        if diff == []:
            print("no change here...")
        elif diff!=[]:
            print("You got a new mark in" + diff.subject)

        for grade in diff:
            print(grade.subject)

            note_outof = f'{grade.grade}/{grade.out_of}'
            note_date = str(grade.date)
            notes = [grade.subject.name, note_outof, note_date]
            print(notes)
            with open(filename, 'a+') as file_object:
                json.dump(notes, file_object, indent=3)
            print(f'{grade.subject.name}:   {grade.grade}/{grade.out_of}     {grade.date}')
        """
    """
    The subject class has three atributes,  name, id and groups
    class Subject(Object):

        Represents a subject. You shouldn't have to create this class manually.
        Attributes
        ----------
        id : str
            the id of the subject (used internally)
        name : str
            name of the subject
        groups : bool
            if the subject is in groups
        

        __slots__ = ['id', 'name', 'groups']

        def __init__(self, parsed_json):
            super().__init__(parsed_json)

            self.id = self._resolver(str, "N")
            self.name = self._resolver(str, "L")
            self.groups = self._resolver(bool, "estServiceGroupe", default=False)

            del self._resolver
    """