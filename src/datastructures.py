from random import randint

class FamilyStructure:  
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
{
    "id": self._generateId(),
    "first_name": "John",
    "age": 33,
    "Lucky_number": [7, 13, 22]
},
{
    "id": self._generateId(),
    "first_name": "Jane",
    "age": 35,
    "Lucky_number": [10, 14, 3]
},
{
    "id": self._generateId(),
    "first_name": "Jimmy",
    "age": 5,
    "Lucky_number": [1]
}
 ]
 

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if not member.get("id"):
            member["id"] = self._generateId()
        self._members.append(member)
        

    def delete_member(self, id):
        print(id)
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
            
        return False


#ACTUALIZAR FAMILIA
    def update_member(self, id, member):
        print("Actualizando", id)
        for family_member in self._members: 
            if family_member["id"] == id:
                self._members.remove(family_member)
                member["id"] = id
                self._members.append(member)
                return True
        return False
  
        
    def get_member(self, id):
        for family_member in self._members:
            if family_member["id"] == id:
                return family_member
        return False
    


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members 