"""
Main entry point for the Semi-Annotation Tool.
"""

import sys
import os
from utils.qt_compat import QApplication, QMessageBox, Qt, QIcon

from gui.main_window import MainWindow
from utils.config import config


def main():
    """Main application entry point."""
    # Create QApplication
    app = QApplication(sys.argv)
    app.setApplicationName("Semi-Annotation Tool")
    app.setApplicationVersion("1.0")
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show main window
    try:
        main_window = MainWindow()
        main_window.show()
        
        # Run application
        sys.exit(app.exec_())
        
    except Exception as e:
        QMessageBox.critical(
            None, "Application Error", 
            f"Failed to start application: {str(e)}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()





