# I will use tkinter to create the interface to the application cataloguing the history of the league.
from tkinter import *
from tkinter import ttk
import csvFunctions
import teamFunctions
import dfFunctions

# - Universal Text Traits:
text_font = ("Myriad", 10)
button_width = 30
button_height = 2

# UI Function definitions:
def titleDesign():
    # First the title
    label_text = "Official Hoopland Tracker"
    label_font = ("Myriad", 16, "bold")
    Label(root, text = label_text, font= label_font).pack()

    # Second the short description
    label_text = "Est. 2024"
    label_font = ("Myriad", 10, "italic")
    Label(root, text = label_text, font= label_font).pack()

def menuOptions():
    description_text = "Choose from one of the following:\n\n"
    Label(root, text = description_text, font= text_font).pack(pady=10)

    # Option 1: Review every year
    button_text = "View Timeline"
    Button(root, text= button_text, font= text_font, width= button_width, height= button_height, command= on_timeline_click).pack()

    # Option 2: Review all the award races and accolades possible
    button_text = "View Yearly Awards"
    Button(root, text= button_text, font= text_font, width= button_width, height= button_height, command=on_award_click).pack()

    # Option 3: View the careers of retired players
    button_text = "View Hall of Fame"
    Button(root, text= button_text, font= text_font, width= button_width, height= button_height, command=on_hof_click).pack()

def createScrollWheel(yearsArr, prev_func):
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=True)

    # Create a Canvas widget with a scrollbar
    canvas = Canvas(main_frame)
    canvas.pack(side= LEFT, fill= BOTH, expand=True)

    # Create a scrollbar
    scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the Canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame to hold the content
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor= NW)

    # Example content inside the frame
    for element in yearsArr:
        Button(frame, text=f"{element}", font= text_font, width= button_width, height= button_height).pack(padx= 180)

    Button(frame, text = "Go Back", font= text_font, width= button_width, height= button_height, command= prev_func).pack()

    # Update the canvas to show the content
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def on_timeline_click():
    clear_window()
    titleDesign()

    # Describe what timeline does
    description_text = "The timeline recounts season by season stats and championships for each team.\nSelecting graph will preview a selection of graphs you can view.\nSelecting Year by Year will show championship winners and final rankings."
    Label(root, text = description_text, font= text_font).pack(pady= 10)
    
    # Show options
    button_text = "View Seasons & Champions"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_seasons_and_champions).pack()

    button_text = "View Team Graphics"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_team_graphics).pack()

    button_text = "Go Back"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_return).pack()

def on_award_click():
    clear_window()
    titleDesign()

    # Describe what awards does
    description_text = "In this section we observe yearly awards and accolades.\nSelecting an award will preview all years.\nAfter year selection, a preview appears with the top 10 candidates in a respective year and the winner."
    Label(root, text = description_text, font= text_font).pack(pady=10)
    
    # Show options
    button_text = "View Most Valuable Players"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View Defensive Player of the Years"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View Rookie of the Years"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View 6th Man of the Years"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View Scoring Champions"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View Rebound Champions"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View Steals Leader"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()
    
    button_text = "View Assists Leader"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View Block Champions"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View More ..."
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_viewMore).pack()

    button_text = "Go Back"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_return).pack()

def on_hof_click():
    clear_window()
    titleDesign()
    description_text = "Here lie the careers of all players worthy of recognition.\nAdmire.\nAcknoledge."
    styled_desciption = Label(root, text = description_text, font= text_font)

    button_text = "Go Back"
    styled_return = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_return)
    
    # pack
    styled_desciption.pack()
    styled_return.pack()

def on_return():
    clear_window()
    titleDesign()
    menuOptions()

def on_viewMore():
    clear_window()
    titleDesign()

    description_text = "In this section we observe yearly awards and accolades.\nSelecting an award will preview all years.\nAfter year selection, a preview appears with the top 10 candidates in a respective year and the winner."
    Label(root, text = description_text, font= text_font).pack(pady= 10)

    # Show options
    button_text = "View 1st All-Hoopland Teams"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View 2nd All-Hoopland Teams"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()
    
    button_text = "View 3rd All-Hoopland Teams"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View 1st All-Defense Teams"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View 2nd All-Defense Teams"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()
    
    button_text = "View 3rd All-Defense Teams"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View Eastern Conference All-Stars"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "View Western Conference All-Stars"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award).pack()

    button_text = "Go Back"
    Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_award_click).pack()

def on_seasons_and_champions():
    clear_window()
    titleDesign()

    description_text = "Select a year to view.\n\n"
    Label(root, text = description_text, font= text_font).pack(pady=10)
    
    yrs = csvFunctions.listYears()
    if (len(yrs) != 1):
        createScrollWheel(yrs, on_timeline_click)
    else:
        Button(root, text = "2024", font= text_font, width= button_width, height= button_height, command= lambda: displaySeason(1)).pack()
        Button(root, text = "Go Back", font= text_font, width= button_width, height= button_height, command= on_timeline_click).pack()
        
def on_team_graphics():
    clear_window()
    titleDesign()

    description_text = "Select a team to view.\n\n"
    Label(root, text = description_text, font= text_font).pack(pady=10)
    
    temp = teamFunctions.teamArr
    temp.sort()

    createScrollWheel(temp, on_timeline_click)
    
def on_any_award():
    clear_window()
    titleDesign()

    description_text = "Select An Award Year.\n\n"
    Label(root, text = description_text, font= text_font).pack(pady=10)

    yrs = csvFunctions.listYears()
    if (len(yrs) != 1):
        createScrollWheel(yrs, on_award_click)
    else:
        Button(root, text = "2024", font= text_font, width= button_width, height= button_height).pack()
        Button(root, text = "Go Back", font= text_font, width= button_width, height= button_height, command= on_award_click).pack()

def displaySeason(yr):
    clear_window()
    titleDesign()

    description_text = f"{2023 + yr} Regular Season"
    Label(root, text = description_text, font= ("Myriad", 10, "bold")).pack()

    # Use a Treeview to view season record.
    szn = ttk.Treeview(root)
    szn['columns'] = ("Team Name", "Won", "Lost", "%", "STL", "BLK", "AST", "PTS", "TO", "PF", "OFF", "DEF", "OVR")

    # Define the columns
    szn.column("#0", width = 0, stretch= NO)
    szn.column("Team Name", width= 150, anchor= W)
    szn.column("Won", width= 40, anchor= CENTER)
    szn.column("Lost", width= 40, anchor= CENTER)
    szn.column("%", width= 40, anchor= CENTER)
    szn.column("STL", width= 30, anchor= CENTER)
    szn.column("BLK", width= 30, anchor= CENTER)
    szn.column("AST", width= 30, anchor= CENTER)
    szn.column("PTS", width= 30, anchor= CENTER)
    szn.column("TO", width= 30, anchor= CENTER)
    szn.column("PF", width= 30, anchor= CENTER)
    szn.column("OFF", width= 40, anchor= CENTER)
    szn.column("DEF", width= 40, anchor= CENTER)
    szn.column("OVR", width= 40, anchor= CENTER)
    
    # Create Headings
    szn.heading("#0", text= "", anchor= W)
    szn.heading("Team Name", text= "Team Name", anchor= W)
    szn.heading("Won", text= "Won", anchor= CENTER)
    szn.heading("Lost", text = "Lost", anchor= CENTER)
    szn.heading("%", text= "%", anchor= CENTER)
    szn.heading("STL", text = "STL", anchor= CENTER)
    szn.heading("BLK", text = "BLK", anchor= CENTER)
    szn.heading("AST", text = "AST", anchor= CENTER)
    szn.heading("PTS", text = "PTS", anchor= CENTER)
    szn.heading("TO", text = "TO", anchor= CENTER)
    szn.heading("PF", text = "PF", anchor= CENTER)
    szn.heading("OFF", text = "OFF", anchor= CENTER)
    szn.heading("DEF", text = "DEF", anchor= CENTER)
    szn.heading("OVR", text = "OVR", anchor= CENTER)

    season_df = dfFunctions.findSeason(yr)
    season_df = season_df.sort_values(by='GW', ascending=False)
    for row in season_df.itertuples(index= True, name= 'Pandas'):
        loss = 82 - season_df.at[row.Index, 'GW']
        winrate = round(season_df.at[row.Index, 'GW'] / 82, 2)
        szn.insert("", END, values= (season_df.at[row.Index, 'Team'], season_df.at[row.Index, 'GW'], loss, winrate, season_df.at[row.Index, 'STL'],
                                      season_df.at[row.Index, 'BLK'], season_df.at[row.Index, 'AST'], season_df.at[row.Index, 'PTS'], 
                                      season_df.at[row.Index, 'TO'], season_df.at[row.Index, 'PF'], int(season_df.at[row.Index, 'O NO.']),
                                      int(season_df.at[row.Index, 'D NO.']), int(season_df.at[row.Index, 'OVR NO.'])))
    post = ttk.Treeview(root)

    post['columns'] = ("Team Name", "Won", "Lost", "%", "STL", "BLK", "AST", "PTS", "TO", "PF", "OFF", "DEF", "OVR")

    # Define the columns
    post.column("#0", width = 0, stretch= NO)
    post.column("Team Name", width= 150, anchor= W)
    post.column("Won", width= 40, anchor= CENTER)
    post.column("Lost", width= 40, anchor= CENTER)
    post.column("%", width= 40, anchor= CENTER)
    post.column("STL", width= 30, anchor= CENTER)
    post.column("BLK", width= 30, anchor= CENTER)
    post.column("AST", width= 30, anchor= CENTER)
    post.column("PTS", width= 30, anchor= CENTER)
    post.column("TO", width= 30, anchor= CENTER)
    post.column("PF", width= 30, anchor= CENTER)
    post.column("OFF", width= 40, anchor= CENTER)
    post.column("DEF", width= 40, anchor= CENTER)
    post.column("OVR", width= 40, anchor= CENTER)
    
    # Create Headings
    post.heading("#0", text= "", anchor= W)
    post.heading("Team Name", text= "Team Name", anchor= W)
    post.heading("Won", text= "Won", anchor= CENTER)
    post.heading("Lost", text = "Lost", anchor= CENTER)
    post.heading("%", text = "%", anchor= CENTER)
    post.heading("STL", text = "STL", anchor= CENTER)
    post.heading("BLK", text = "BLK", anchor= CENTER)
    post.heading("AST", text = "AST", anchor= CENTER)
    post.heading("PTS", text = "PTS", anchor= CENTER)
    post.heading("TO", text = "TO", anchor= CENTER)
    post.heading("PF", text = "PF", anchor= CENTER)
    post.heading("OFF", text = "OFF", anchor= CENTER)
    post.heading("DEF", text = "DEF", anchor= CENTER)
    post.heading("OVR", text = "OVR", anchor= CENTER)

    post_df = dfFunctions.findPost(yr)
    post_df = post_df.sort_values(by='GW', ascending=False)
    post_df.sort_values(by='GW')
    for row in post_df.itertuples(index= True, name= 'Pandas'):
        loss = post_df.at[row.Index, 'GP'] - post_df.at[row.Index, 'GW']
        winrate = round(post_df.at[row.Index, 'GW'] / post_df.at[row.Index, 'GP'], 2)
        post.insert("", END, values= (post_df.at[row.Index, 'Team'], post_df.at[row.Index, 'GW'], loss, winrate, post_df.at[row.Index, 'STL'],
                                      post_df.at[row.Index, 'BLK'], post_df.at[row.Index, 'AST'], post_df.at[row.Index, 'PTS'], 
                                      post_df.at[row.Index, 'TO'], post_df.at[row.Index, 'PF'], int(post_df.at[row.Index, 'O NO.']),
                                      int(post_df.at[row.Index, 'D NO.']), int(post_df.at[row.Index, 'OVR NO.'])))

    # pack
    szn.pack()
    description_text = f"{2023 + yr} Post Season"
    Label(root, text = description_text, font= ("Myriad", 10, "bold")).pack()
    post.pack()
    Button(root, text = "Go Back", font= text_font, width= button_width, height= button_height, command= on_seasons_and_champions).pack()
    
# Create the window
root = Tk()
root.title('Hoopland Tracker Application')
window_width = 600
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Design the window
titleDesign()
menuOptions()

# Run the window
root.mainloop()