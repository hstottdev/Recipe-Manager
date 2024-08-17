import json
import os
cwd = os.getcwd()
recipeFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'recipes'))

class Recipe:
    def __init__(self,title, ingredients,instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    def print(self):
        print("\nRECIPE: ",self.title)
        print("\nINGREDIENTS:\n")
        for ingred in self.ingredients:
            print("- {0} of {1}\n".format(self.ingredients[ingred],ingred))

        print("\nINSTRUCTIONS:\n")
        stepNumber = 1
        for step in self.instructions:
            print("{0}. {1}\n".format(stepNumber,step))
            stepNumber += 1

    def saveToFile(self):
        filePath = os.path.abspath(os.path.join(recipeFolder,self.title+'.json'))
        with open(filePath, 'w') as f:
            data = json.dumps(self.__dict__)
            json.dump(data,f)

    def openFromFile(fileName):
        filePath = os.path.abspath(os.path.join(recipeFolder,fileName+'.json'))
        f = open(filePath)
        data = json.loads(json.load(f))
        recipe = Recipe(data['title'],data['ingredients'],data['instructions'])
        return recipe
        
    

class RecipeManager:

    def start():
        print(recipeFolder)
        print("\nWelcome to your recipe book!")
        choice = input("\nWhat would you like to do?"+
    """I think
    1. Add new recipe.
    2. View all recipes.
    3. Search for recipe.
    4. Edit a recipe.
    5. Delete a recipe.
    
    : """)

        if(choice == "1"):
            RecipeManager.addRecipe()
            
    def addRecipe():
        title = input("What is the name of your recipe?: ")
        ingredients = {}
        instructions = []
               
        #ADD INGREDIENTS
        adding = True
        count = 1
        while(adding):
            ingred = input("\nWhat is ingredient #{}?: ".format(count))
            amount = input("How much {} is required?: ".format(ingred))
            confirm = input("Confirm ingredient? (y or n): ")

            if(confirm[0] == 'y'):             
                ingredients[ingred] = amount 
                more = input("\nWould you like to add another ingredient? (y or n): ")
                #If no more ingredients
                if(more[0] == 'n'):
                    adding = False
                else:
                    count += 1
                    
        #ADD INSTRUCTION STEPS
        adding = True
        count = 1 
        while(adding):
            step = input("\nWhat is step #{}?: ".format(count))
            confirm = input("Confirm step? (y or n): ")

            if(confirm[0] == 'y'):             
                instructions.append(step)
                more = input("\nWould you like to add another step? (y or n): ")
                #If no more steps
                if(more[0] == 'n'):
                    adding = False
                else:
                    count += 1

        newRecipe = Recipe(title,ingredients,instructions)
        newRecipe.print()
        newRecipe.saveToFile()

       
recipe = Recipe.openFromFile("fluf")
recipe.print()

