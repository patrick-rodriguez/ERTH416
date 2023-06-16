import database_functions
import environment_gauges
import arduino_functions
import UI

def main():
    ui = UI.create_ui()
    ui.mainloop()

if __name__ == "__main__":
    main()