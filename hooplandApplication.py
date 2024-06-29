# I will use tkinter to create the interface to the application cataloguing the history of the league.
from tkinter import *
import csvFunctions
import teamFunctions

# Universal Text Traits:
text_font = ("Myriad", 10)
button_width = 30
button_height = 2

# Function defintions:
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

def createScrollWheel(yearsArr):
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
        Button(frame, text=f"{element}", font= text_font, width= button_width, height= button_height, command= on_year_clicked).pack(padx= 180)

    Button(frame, text = "Go Back", font= text_font, width= button_width, height= button_height, command= on_return).pack()

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

    button_text = "View Sixth Man of the Years"
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
    styled_desciption = Label(root, text = description_text, font= text_font)

    # Show options
    button_text = "View 1st All-Hoopland Teams"
    styled_hlf = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award)

    button_text = "View 2nd All-Hoopland Teams"
    styled_hls = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award)
    
    button_text = "View 3rd All-Hoopland Teams"
    styled_hlt = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award)

    button_text = "View 1st All-Defense Teams"
    styled_dff = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award)

    button_text = "View 2nd All-Defense Teams"
    styled_dfs = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award)
    
    button_text = "View 3rd All-Defense Teams"
    styled_dft = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award)

    button_text = "View Eastern Conference All-Stars"
    styled_eas = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award)

    button_text = "View Western Conference All-Stars"
    styled_was = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_any_award)

    button_text = "Go Back"
    styled_return = Button(root, text = button_text, font= text_font, width= button_width, height= button_height, command= on_award_click)

    # pack
    styled_desciption.pack(pady= 10)
    styled_hlf.pack()
    styled_hls.pack()
    styled_hlt.pack()
    styled_dff.pack()
    styled_dfs.pack()
    styled_dft.pack()
    styled_eas.pack()
    styled_was.pack()
    styled_return.pack()

def on_seasons_and_champions():
    clear_window()
    titleDesign()

    description_text = "Select a year to view.\n\n"
    Label(root, text = description_text, font= text_font).pack(pady=10)
    
    yrs = csvFunctions.listYears()
    if (len(yrs) != 1):
        createScrollWheel(yrs)
    else:
        Button(root, text = "2024", font= text_font, width= button_width, height= button_height).pack()
        Button(root, text = "Go Back", font= text_font, width= button_width, height= button_height, command= on_timeline_click).pack()
        
def on_team_graphics():
    clear_window()
    titleDesign()

    description_text = "Select a team to view.\n\n"
    Label(root, text = description_text, font= text_font).pack(pady=10)
    
    temp = teamFunctions.teamArr
    temp.sort()

    createScrollWheel(temp)
    
def on_any_award():
    clear_window()
    titleDesign()

    description_text = "Select An Award Year.\n\n"
    Label(root, text = description_text, font= text_font).pack(pady=10)
    yrs = csvFunctions.listYears()
    if (len(yrs) != 1):
        createScrollWheel(yrs)
    else:
        Button(root, text = "2024", font= text_font, width= button_width, height= button_height).pack()
        Button(root, text = "Go Back", font= text_font, width= button_width, height= button_height, command= on_award_click).pack()

def on_year_clicked():
    clear_window()
    titleDesign()



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