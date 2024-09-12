# Music Player Application
Python based Music Player Application with a modern design, responsive layout and enhanced UI.  

The Enhanced Music Player is a simple yet functional desktop music player application built using Python's tkinter for the GUI and pygame for audio playback. The application allows users to create a playlist, play, pause, stop, and navigate between songs. This player also includes a responsive interface and user-friendly controls, making it a great choice for users who want a straightforward music playback experience.

FEATURES :-
1. Playlist Management:
   (i). Add songs to the playlist from your local files.
   (ii). Remove songs from the playlist.
2. Playback Controls:
   (i). Play/Pause: Toggle between playing and pausing the current song.
   (ii). Stop: Stop the current song and clear the selection.
   (iii). Previous/Next: Navigate through the songs in the playlist.
3. Alerts and Notifications: The application provides alert dialogs for important actions, such as when no songs are selected or available in the playlist.
4. Graphical User Interface (GUI):
   (i). Responsive design that adjusts to different window sizes.
   (ii). Modern and clean look with custom styles.
   (iii). Scrollable playlist view with custom color themes.
   (iv). Intuitive control buttons with icons.
   
USAGE :-
1. Adding Songs: Use the "File" menu and select "Add Songs" to browse and add songs to your playlist. The songs will be displayed in the listbox.
2. Playing Music: Select a song from the playlist and use the play/pause button to start playback. Use the stop button to stop playback, or the previous/next buttons to navigate through the playlist.
3. Deleting Songs: Select a song from the playlist and use the "File" menu's "Delete Song" option to remove it from the list.
4. File Structure:
   (i). music_player.py: Main application script containing the GUI, playlist management, and playback logic.
   (ii). play_icon.png, pause_icon.png, stop_icon.png, prev_icon.png, next_icon.png: Icons for control buttons.

NOTES :-
1. Ensure that the songs you want to add are in .mp3 format.
2. Install os, pygame and PIL package from terminal if not installed already.
3. The application uses a fixed path "E:/Music Player/Songs/" for playback. Adjust this path in the code to match the location of your music files.
