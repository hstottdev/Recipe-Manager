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
        if('.json' in fileName):
            filePath = os.path.abspath(os.path.join(recipeFolder,fileName))
            f = open(filePath)
            data = json.loads(json.load(f))
            recipe = Recipe(data['title'],data['ingredients'],data['instructions'])
            return recipe
        else:
            return None
        
    

class RecipeManager:

    def start():
        print("\nWelcome to your recipe book!")
        choice = input("\nWhat would you like to do?"+
    """
    1. Add new recipe.
    2. View all recipes.
    3. Search for recipe.
    4. Edit a recipe.
    5. Delete a recipe.
    6. Close the recipe book.
    : """)

        if(choice == "1"):
            RecipeManager.addRecipe()
        elif(choice == "2"):
            allRecipes = lambda r : type(r) == Recipe
            RecipeManager.printRecipes(allRecipes)
        elif(choice == "3"):
            RecipeManager.searchRecipe()
        if(choice == "6"):
            return

        close = input("\nClose the recipe book? (y or n): ")

        if(close[0] == 'n'):
            RecipeManager.start()
            
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

    def getRecipeFiles():
        return os.listdir(recipeFolder)
        

    def printRecipes(searchCondition):
        print("\nRESULTS:")
        files = RecipeManager.getRecipeFiles()
        for f in files:           
                recipe = Recipe.openFromFile(f)
                if(searchCondition(recipe)):
                    print("\n==================================")
                    recipe.print()

    def searchRecipe():
        searchMode = input("Search recipe by?"+
    """
    1. Title
    2. Ingredients
    : """)
        results = []
        if(searchMode == "1"):
            term = input("Which recipe are you looking for?: ")
            searchCondition = lambda r : term.lower() in r.title.lower()
            RecipeManager.printRecipes(searchCondition)
        elif(searchMode == "2"):
            term = input("Which ingredient are you looking for?: ")
            searchCondition = lambda r : term.lower() in map(str.lower, r.ingredients)
            print("Recipes found with '{}'".format(term))
            RecipeManager.printRecipes(searchCondition)
                  
RecipeManager.start()

