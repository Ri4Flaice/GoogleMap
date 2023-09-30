import tkinter
import customtkinter
import tkintermapview

def find_location():
    location = entry.get()
    map_widget.set_address(location)

window = tkinter.Tk()
window.title('Google Maps')
window.geometry('1000x800')
window.resizable(False, False)

map_widget = tkintermapview.TkinterMapView(window, width=1000, height=800, corner_radius=0)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
map_widget.place(x=0, y=0)

entry = customtkinter.CTkEntry(window, width=600)
entry.place(x=200, y=20)

button = customtkinter.CTkButton(window, text='find', width=50, bg_color='black', fg_color='black', corner_radius=0, command=find_location)
button.place(x=820, y=20)

window.mainloop()