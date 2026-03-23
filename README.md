# Map Navigation Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://riverbankcomputing.com/software/pyqt/)
[![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey.svg)](https://www.sqlite.org/)

A PyQt5-based map navigation application with user management, path finding, and graphical interface.

## Features

- **User Authentication**: Login and registration system with SQLite database
- **Map Display**: Visual map interface with custom backgrounds
- **Path Finding**: Shortest path calculation between locations
- **Interactive UI**: User-friendly graphical interface with PyQt5
- **Database Storage**: User information and location data stored in SQLite

## Project Structure

```
.
├── map.py              # Main application entry point with UI
├── Mainwce.py          # Additional UI components
├── database_option.py  # Database operations (SQLite)
├── dis33.py           # Path finding algorithm (Dijkstra/Floyd)
├── picture/           # Image resources (icons, backgrounds)
└── __pycache__/       # Python cache files
```

## Requirements

- Python 3.8+
- PyQt5
- SQLite3 (built-in with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/liangc001/map.git
cd map
```

2. Install dependencies:
```bash
pip install PyQt5
```

3. Run the application:
```bash
python map.py
```

## Usage

1. **Login/Register**: Create an account or login with existing credentials
2. **Browse Map**: View the map with various locations
3. **Search Route**: Enter start and destination to find the shortest path
4. **View Results**: See the calculated route and distance

## Technical Details

### Database Schema

The application uses SQLite with the following tables:
- `user_mes`: Stores user login information (id, password)

### Path Finding Algorithm

The `dis33.py` module implements shortest path algorithms:
- Floyd-Warshall algorithm for all-pairs shortest paths
- Dijkstra's algorithm for single-source shortest paths

### UI Components

- **Main Window**: Primary application window with map display
- **Login Dialog**: User authentication interface
- **Route Search**: Input fields for start and destination
- **Result Display**: Shows calculated path and distance

## Screenshots

*(Screenshots to be added)*

## Development

This project was developed as a practice exercise for:
- Learning PyQt5 GUI development
- Understanding database operations with SQLite
- Implementing graph algorithms for path finding
- Building a complete desktop application

## Future Improvements

- [ ] Add more map data and locations
- [ ] Implement real map integration (e.g., OpenStreetMap)
- [ ] Add route visualization on map
- [ ] Support for multiple transportation modes
- [ ] Save favorite routes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- PyQt5 Documentation
- SQLite Documentation
- Algorithm references for shortest path calculation

## Note

This is a learning project created for educational purposes. The map data is simulated and not based on real geographic information.
