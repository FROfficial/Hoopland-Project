# I will use tkinter to navigate the history collected from the simulated years.
from tkinter import *

# function Definitions used:
def titleDesign():
    # First the title
    label_text = "Official Hoopland Tracker"
    label_font = ("Myriad", 16, "bold")
    styled_title = Label(root, text = label_text, font= label_font)
    styled_title.pack()

    # Second the short description
    label_text = "Est. 2024"
    label_font = ("Myriad", 10, "italic")
    styled_description = Label(root, text = label_text, font= label_font)
    styled_description.pack()

def menuOptions():
    # Set universal button traits
    button_font = ("Myriad", 10)
    button_width = 30
    button_height = 2

    # Option 1: Review every year
    button_text = "View Timeline"
    styled_timeline = Button(root, text= button_text, font= button_font, width= button_width, height= button_height, command= on_timeline_click)
    styled_timeline.pack()

    # Option 2: Review all the award races and accolades possible
    button_text = "View Yearly Awards"
    styled_awards = Button(root, text= button_text, font= button_font, width= button_width, height= button_height, command=on_award_click)
    styled_awards.pack()

    # Option 3: View the careers of retired players
    button_text = "View Hall of Fame"
    styled_hof = Button(root, text= button_text, font= button_font, width= button_width, height= button_height, command=on_hof_click)
    styled_hof.pack()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def on_timeline_click():
    clear_window()
    titleDesign()

    # Describe what timeline does
    description_text = "The timeline recounts season by season stats and championships for each team.\nSelecting graph will preview a selection of graphs you can view.\nSelecting Year by Year will show championship winners and final rankings."
    description_font = ("Myriad", 10)
    styled_desciption = Label(root, text = description_text, font= description_font)
    
    # Show options
    button_text = "View Seasons & Champions"
    styled_yby = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Team Graphics"
    styled_graphics = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "Go Back"
    styled_return = Button(root, text = button_text, font= description_font, width= 30, height= 2, command= on_return)

    # pack
    styled_desciption.pack(pady= 10)
    styled_yby.pack()
    styled_graphics.pack()
    styled_return.pack()

def on_award_click():
    clear_window()
    titleDesign()

    # Describe what awards does
    description_text = "In this section we observe yearly awards and accolades.\nSelecting an award will preview all years.\nAfter year selection, a preview appears with the top 10 candidates in a respective year and the winner."
    description_font = ("Myriad", 10)
    styled_desciption = Label(root, text = description_text, font= description_font)
    
    # Show options
    button_text = "View Most Valuable Players"
    styled_mvp = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Defensive Player of the Years"
    styled_dpoy = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Rookie of the Years"
    styled_roty = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Sixth Man of the Years"
    styled_smoty = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Scoring Champions"
    styled_pts_champ = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Rebound Champions"
    styled_reb_champ = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Steals Leader"
    styled_stl_leader = Button(root, text = button_text, font= description_font, width= 30, height= 2)
    
    button_text = "View Assists Leader"
    styled_ast_leader = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Block Champions"
    styled_blk_champ = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View More ..."
    styled_more = Button(root, text = button_text, font= description_font, width= 30, height= 2, command= on_viewMore)

    button_text = "Go Back"
    styled_return = Button(root, text = button_text, font= description_font, width= 30, height= 2, command= on_return)

    # pack
    styled_desciption.pack(pady= 10)
    styled_mvp.pack()
    styled_dpoy.pack()
    styled_roty.pack()
    styled_smoty.pack()
    styled_pts_champ.pack()
    styled_reb_champ.pack()
    styled_stl_leader.pack()
    styled_ast_leader.pack()
    styled_blk_champ.pack()
    styled_more.pack()
    styled_return.pack()

def on_hof_click():
    clear_window()
    titleDesign()
    description_font = ("Myriad", 10)
    button_text = "Go Back"
    styled_return = Button(root, text = button_text, font= description_font, width= 30, height= 2, command= on_return)
    
    # pack
    styled_return.pack()

def on_return():
    clear_window()
    titleDesign()
    menuOptions()

def on_viewMore():
    clear_window()
    titleDesign()
    
    description_text = "In this section we observe yearly awards and accolades.\nSelecting an award will preview all years.\nAfter year selection, a preview appears with the top 10 candidates in a respective year and the winner."
    description_font = ("Myriad", 10)
    styled_desciption = Label(root, text = description_text, font= description_font)

    # Show options
    button_text = "View 1st All-Hoopland Teams"
    styled_hlf = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View 2nd All-Hoopland Teams"
    styled_hls = Button(root, text = button_text, font= description_font, width= 30, height= 2)
    
    button_text = "View 3rd All-Hoopland Teams"
    styled_hlt = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View 1st All-Defense Teams"
    styled_dff = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View 2nd All-Defense Teams"
    styled_dfs = Button(root, text = button_text, font= description_font, width= 30, height= 2)
    
    button_text = "View 3rd All-Defense Teams"
    styled_dft = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Eastern Conference All-Stars"
    styled_eas = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "View Western Conference All-Stars"
    styled_was = Button(root, text = button_text, font= description_font, width= 30, height= 2)

    button_text = "Go Back"
    styled_return = Button(root, text = button_text, font= description_font, width= 30, height= 2, command= on_return)

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

