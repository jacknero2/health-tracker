import pandas

def generate_file(file_name: str) -> None:
    try:
        open(file_name,"r")
    except FileNotFoundError:
        with open(file_name,"a") as file:
            file.write("name,age,screen_time,mood,mood_quality,sleep_time,sleep_quality,sleep_interruptions,mental_time,mental_acuity,mental_focus,creative_time,creative_quality,upper_body_time,upper_body_quality,lower_body_time,lower_body_quality,endurance_time,endurance_quality,sexual_time,sexual_quality,protein_intake,carbohydrate_intake,fat_intake,food_list\n")

def load_data(file_name: str) -> pandas.DataFrame:
    try:
        dataframe = pandas.read_csv(file_name)
        return dataframe
    except pandas.errors.EmptyDataError:
        print("File error in opening with pandas library")
        return None

def new_data(file_name: str) -> None:
    with open(file_name, "a") as file:
        name = input("Name: ")
        age = input("Age: ")
        screen_time = input("Screen time (hrs): ")
        mood = input("Brief description of your mood (1-5 words): ")
        mood_quality = input("Mood quality [0,10]: ")
        sleep_time = input("Amount of sleep (hrs): ")
        sleep_quality = input("Quality of sleep [0,10]: ")
        sleep_interruptions = input("Number of sleep interruptions [0,infin): ")
        mental_time = input("Number of hours of high function mental activity: ")
        mental_acuity  = input("Quality of mental acuity [0,10]: ")
        mental_focus  = input("Quality of mental focus [0,10]: ")
        creative_time = input("Number of hours of creativity: ")
        creative_quality = input("Quality of creative acuity [0,10]: ")
        upper_body_time = input("Upper body exercise time (minutes): ")
        upper_body_quality = input("Upper body exercise acuity [0,10]: ")
        lower_body_time = input("Lower body exercise time (minutes): ")
        lower_body_quality = input("Lower body exercise acuity [0,10]: ")
        endurance_time = input("Endurance exercise time (minutes): ")
        endurance_quality = input("Endurance exercise quality [0,10]: ")
        sexual_time = input("Sexual activity instances [0, infin): ")
        sexual_quality = input("Sexual acuity [0,10]: ")
        protein_intake = input("Protein (grams): ")
        carbohydrate_intake = input("Carbohydrates (grams): ")
        fat_intake = input("Fat (grams): ")
        food_list = input("Enter foods eaten with commas in between and no spaces after commas: ").split(",")
        file.write(f"{name},{age},{screen_time},{mood},{mood_quality},{sleep_time},{sleep_quality},{sleep_interruptions},{mental_time},{mental_acuity},{mental_focus},{creative_time},{creative_quality},{upper_body_time},{upper_body_quality},{lower_body_time},{lower_body_quality},{endurance_time},{endurance_quality},{sexual_time},{sexual_quality},{protein_intake},{carbohydrate_intake},{fat_intake},\"{food_list}\"\n")

def main():
    file_name = "health_data.csv"
    generate_file(file_name)
    #new_data(file_name)
    data = load_data(file_name)

    headers = ["name","age","screen_time","mood","mood_quality","sleep_time","sleep_quality","sleep_interruptions","mental_time","mental_acuity","mental_focus","creative_time","creative_quality","upper_body_time","upper_body_quality","lower_body_time","lower_body_quality","endurance_time","endurance_quality","sexual_time","sexual_quality","protein_intake","carbohydrate_intake","fat_intake","food_list"]

    data.head()

if __name__ == "__main__":
    main()