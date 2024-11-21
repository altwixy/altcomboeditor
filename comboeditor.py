import customtkinter as ctk #line:1
import os #line:2
from tkinter import messagebox ,filedialog ,simpledialog #line:3
import re #line:4
### ------ This Code Is Obfuscated To Prevent Skidding ------ ###
version =5 #line:7
changelog =["Version 1: Initial version with basic functionality.","Version 2: Added 24 combo features.","Version 3: Integrated capture remover and other advanced features.","Version 4: Cleaned up GUI, replaced permanent text boxes with pop-up windows.","Version 5: Fixed buttons going out of the screen","Version 6: Updated Capture Remover to remove after pipe or space and removed the separate buttons for each."]#line:15
def load_combos (filename ="currentcombo.txt"):#line:18
    try :#line:19
        with open (filename ,"r",encoding ="utf-8")as O0O0OO000O0OO0OO0 :#line:20
            O0O00000OOOOOO0O0 =[O000OOO0O0OO0O00O .strip ()for O000OOO0O0OO0O00O in O0O0OO000O0OO0OO0 .readlines ()]#line:21
        return O0O00000OOOOOO0O0 #line:22
    except FileNotFoundError :#line:23
        messagebox .showerror ("Error",f"File {filename} not found!")#line:24
        return []#line:25
def save_combos (OOO0OO0O0OOOO00OO ,filename ="currentcombo.txt"):#line:28
    try :#line:29
        with open (filename ,"w",encoding ="utf-8")as OO0O00OO0OOO00O00 :#line:30
            for OOOO000OOOOO0OO0O in OOO0OO0O0OOOO00OO :#line:31
                OO0O00OO0OOO00O00 .write (OOOO000OOOOO0OO0O +"\n")#line:32
    except Exception as O00O0O00000OOO00O :#line:33
        messagebox .showerror ("Error",f"Failed to save file: {str(O00O0O00000OOO00O)}")#line:34
def display_combos ():#line:37
    text_area .delete (1.0 ,ctk .END )#line:38
    for O0O00OO0O00OOOOOO in combos :#line:39
        text_area .insert (ctk .END ,O0O00OO0O00OOOOOO +"\n")#line:40
def load_file ():#line:43
    OOOO0000OO00OOOO0 =filedialog .askopenfilename (filetypes =[("Text Files","*.txt")])#line:44
    if OOOO0000OO00OOOO0 :#line:45
        global combos #line:46
        combos =load_combos (OOOO0000OO00OOOO0 )#line:47
        display_combos ()#line:48
def save_file ():#line:51
    O00O0OO00000OO00O =filedialog .asksaveasfilename (defaultextension =".txt",filetypes =[("Text Files","*.txt")])#line:52
    if O00O0OO00000OO00O :#line:53
        save_combos (combos ,O00O0OO00000OO00O )#line:54
def open_input_window (OOOOOO0OO00O000OO ,O0OO000OO0OOO000O ):#line:57
    OO0OO0O0OOOOOO0O0 =ctk .CTkToplevel (root )#line:58
    OO0OO0O0OOOOOO0O0 .title (OOOOOO0OO00O000OO )#line:59
    OOO00OO000OOOO0O0 =ctk .CTkLabel (OO0OO0O0OOOOOO0O0 ,text ="Enter Text:")#line:61
    OOO00OO000OOOO0O0 .pack (padx =10 ,pady =10 )#line:62
    O0O00O0000O0O0OOO =ctk .CTkEntry (OO0OO0O0OOOOOO0O0 )#line:64
    O0O00O0000O0O0OOO .pack (padx =10 ,pady =10 )#line:65
    def O0OO0O0OOOO0OO00O ():#line:67
        O0OO000OO0OOO000O (O0O00O0000O0O0OOO .get ())#line:68
        OO0OO0O0OOOOOO0O0 .destroy ()#line:69
    O00OO0OOO000O00O0 =ctk .CTkButton (OO0OO0O0OOOOOO0O0 ,text ="Apply",command =O0OO0O0OOOO0OO00O )#line:71
    O00OO0OOO000O00O0 .pack (padx =10 ,pady =10 )#line:72
def add_text (OOOO00OO00O00000O ):#line:75
    global combos #line:76
    combos =[O0O0000O00000000O +OOOO00OO00O00000O for O0O0000O00000000O in combos ]#line:77
    display_combos ()#line:78
def remove_duplicates ():#line:81
    global combos #line:82
    combos =list (set (combos ))#line:83
    display_combos ()#line:84
def filter_combos (OOOOO000000OOOOO0 ):#line:87
    global combos #line:88
    combos =[O00O0O0OO000000O0 for O00O0O0OO000000O0 in combos if OOOOO000000OOOOO0 in O00O0O0OO000000O0 ]#line:89
    display_combos ()#line:90
def clear_combos ():#line:93
    global combos #line:94
    combos =[]#line:95
    display_combos ()#line:96
def capture_remover ():#line:99
    global combos #line:100
    combos =[OO0O0O00OO00O0O00 .split ("|")[0 ].split (" ")[0 ]for OO0O0O00OO00O0O00 in combos ]#line:101
    display_combos ()#line:102
def replace_text (O0O0O0000O0O00OOO ,O00O00OO0OO0OOOOO ):#line:105
    global combos #line:106
    combos =[O0OOO0OOOO00O00O0 .replace (O0O0O0000O0O00OOO ,O00O00OO0OO0OOOOO )for O0OOO0OOOO00O00O0 in combos ]#line:107
    display_combos ()#line:108
def add_prefix (O000OOO000OO0O0O0 ):#line:111
    global combos #line:112
    combos =[O000OOO000OO0O0O0 +O00OOOOOOO00OO00O for O00OOOOOOO00OO00O in combos ]#line:113
    display_combos ()#line:114
def remove_lines_with_text (O0000OOOO00O00O00 ):#line:117
    global combos #line:118
    combos =[O00OOO0000O000000 for O00OOO0000O000000 in combos if O0000OOOO00O00O00 not in O00OOO0000O000000 ]#line:119
    display_combos ()#line:120
def add_suffix (O000O00OOOO00O00O ):#line:123
    global combos #line:124
    combos =[OOO00OO000O000O0O +O000O00OOOO00O00O for OOO00OO000O000O0O in combos ]#line:125
    display_combos ()#line:126
def convert_to_uppercase ():#line:129
    global combos #line:130
    combos =[OO000OOOO0OOO0O0O .upper ()for OO000OOOO0OOO0O0O in combos ]#line:131
    display_combos ()#line:132
def convert_to_lowercase ():#line:135
    global combos #line:136
    combos =[O000O000OOO0OOO00 .lower ()for O000O000OOO0OOO00 in combos ]#line:137
    display_combos ()#line:138
def reverse_combos ():#line:141
    global combos #line:142
    combos =[OO0OOO00O00OOOO0O [::-1 ]for OO0OOO00O00OOOO0O in combos ]#line:143
    display_combos ()#line:144
def trim_spaces ():#line:147
    global combos #line:148
    combos =[O0O00O0O0O0OO0OO0 .strip ()for O0O00O0O0O0OO0OO0 in combos ]#line:149
    display_combos ()#line:150
def remove_lines_with_length (OOO0O0O0000000O00 ):#line:153
    global combos #line:154
    combos =[O0000O0OO000OO0OO for O0000O0OO000OO0OO in combos if len (O0000O0OO000OO0OO )!=OOO0O0O0000000O00 ]#line:155
    display_combos ()#line:156
def sort_combos ():#line:159
    global combos #line:160
    combos =sorted (combos )#line:161
    display_combos ()#line:162
def shuffle_combos ():#line:165
    import random #line:166
    global combos #line:167
    random .shuffle (combos )#line:168
    display_combos ()#line:169
def select_random_combos (OO000OO0O0OO000O0 ):#line:172
    import random #line:173
    global combos #line:174
    if OO000OO0O0OO000O0 <=len (combos ):#line:175
        combos =random .sample (combos ,OO000OO0O0OO000O0 )#line:176
    display_combos ()#line:177
def add_line_break ():#line:180
    global combos #line:181
    combos =[OOOOOO00OOOOO0OO0 +"\n"for OOOOOO00OOOOO0OO0 in combos ]#line:182
    display_combos ()#line:183
def remove_combo_by_index (O0O0OOO000O000O00 ):#line:186
    global combos #line:187
    if 0 <=O0O0OOO000O000O00 <len (combos ):#line:188
        del combos [O0O0OOO000O000O00 ]#line:189
    display_combos ()#line:190
def find_longest_combo ():#line:193
    global combos #line:194
    O00OO000O0OOOOOO0 =max (combos ,key =len )#line:195
    messagebox .showinfo ("Longest Combo",f"The longest combo is: {O00OO000O0OOOOOO0}")#line:196
def find_shortest_combo ():#line:199
    global combos #line:200
    OOOOOOO0OO0O00O0O =min (combos ,key =len )#line:201
    messagebox .showinfo ("Shortest Combo",f"The shortest combo is: {OOOOOOO0OO0O00O0O}")#line:202
def exit_app ():#line:205
    root .quit ()#line:206
root =ctk .CTk ()#line:209
root .title (f"Alt Combo Edit | Version {version} | github.com/altwixy/altcomboeditor")#line:212
root .geometry ("800x600")#line:213
frame =ctk .CTkFrame (root )#line:216
frame .pack (pady =10 ,padx =20 ,fill ="both",expand =True )#line:217
text_area =ctk .CTkTextbox (frame ,wrap ="word",height =300 )#line:220
text_area .pack (padx =10 ,pady =10 ,fill ="both",expand =True )#line:221
button_frame =ctk .CTkFrame (root )#line:224
button_frame .pack (pady =10 ,padx =20 ,fill ="x")#line:225
button_frame .grid_columnconfigure (0 ,weight =1 )#line:228
button_frame .grid_columnconfigure (1 ,weight =1 )#line:229
button_frame .grid_columnconfigure (2 ,weight =1 )#line:230
button_frame .grid_columnconfigure (3 ,weight =1 )#line:231
buttons =[("Load Combos",load_file ),("Save Combos",save_file ),("Clear Combos",clear_combos ),("Exit",exit_app ),("Add Text to End",lambda :open_input_window ("Add Text",add_text )),("Remove Duplicates",remove_duplicates ),("Filter Combos",lambda :open_input_window ("Filter Combos",filter_combos )),("Capture Remover",capture_remover ),("Replace Text",lambda :open_input_window ("Replace Text",lambda O0OO0OOOO0O0O0O00 :replace_text ("old_text",O0OO0OOOO0O0O0O00 ))),("Add Prefix",lambda :open_input_window ("Add Prefix",add_prefix )),("Add Suffix",lambda :open_input_window ("Add Suffix",add_suffix )),("Convert to Uppercase",convert_to_uppercase ),("Convert to Lowercase",convert_to_lowercase ),("Reverse Combos",reverse_combos ),("Trim Spaces",trim_spaces ),("Remove Lines by Length",lambda :open_input_window ("Remove Lines by Length",remove_lines_with_length )),("Sort Combos",sort_combos ),("Shuffle Combos",shuffle_combos ),("Select Random Combos",lambda :open_input_window ("Select Random Combos",select_random_combos )),("Add Line Break",add_line_break ),("Remove Combo by Index",lambda :open_input_window ("Remove Combo by Index",remove_combo_by_index )),("Longest Combo",find_longest_combo ),("Shortest Combo",find_shortest_combo )]#line:258
for index ,(text ,command )in enumerate (buttons ):#line:261
    row =index //4 #line:262
    col =index %4 #line:263
    button =ctk .CTkButton (button_frame ,text =text ,command =command )#line:264
    button .grid (row =row ,column =col ,padx =5 ,pady =5 ,sticky ="ew")#line:265
combos =load_combos ()#line:268
root .mainloop ()#line:271
