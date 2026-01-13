# Hukamnama Screen

A Flask-based web application for displaying Gurbani (Hukamnama) on digital screens with remote management capabilities. Designed for Gurdwaras and Sikh organizations to showcase sacred verses on dedicated display screens using single-board computers like Raspberry Pi.

## Overview

Hukamnama Screen enables you to:

- Display Gurbani verses on dedicated screens (TVs, monitors, or projectors)
- Remotely search and update displayed content from any device
- Automatically sync updates across all connected displays in real-time
- Run on low-cost hardware like Raspberry Pi in kiosk mode

## Features

- **Real-time Updates**: Uses Socket.IO to instantly push changes to all connected displays
- **Remote Management**: Control displays from any web browser (desktop, tablet, or smartphone)
- **Search Functionality**: Find specific pankti (verses) from the database
- **User Authentication**: Secure login system to manage who can update content
- **Responsive Design**: Optimized display for various screen sizes
- **Low Resource Usage**: Runs efficiently on single-board computers

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Real-time Communication**: Socket.IO with gevent server
- **Frontend**: HTML templates with Socket.IO client
- **Database**: SQLite (via Flask extensions)
- **Package Management**: UV (fast Python package manager)

> [!NOTE]
> This project uses the Socket.IO gevent server instead of uWSGI due to compatibility issues with OpenSSL headers on macOS.

## Installation

### Prerequisites

- Python 3.8 or higher
- UV package manager (or use pip as an alternative)
- Git

### Quick Start

1. **Clone the repository**

   ```bash
   git clone https://github.com/tjgurwara99/hukamnama-screen.git
   cd hukamnama-screen
   ```

2. **Set up virtual environment**

   ```bash
   uv venv
   ```

   The virtual environment will be created in the `.venv` directory.

3. **Start the application**

   ```bash
   uv run python app.py
   ```

   The server will start on `http://127.0.0.1:8000`

4. **Create an account**

   - Navigate to `http://127.0.0.1:8000/signup`
   - Register a new user account

5. **Set your first Hukamnama**

   - Log in with your credentials
   - Use the search page to find a pankti
   - Click "Save as current hukamnama" to publish it

6. **View the display**
   - Open `http://127.0.0.1:8000` on your display device
   - The page will show the current Hukamnama and auto-refresh on updates

## Deployment

### Production Setup (Raspberry Pi/Linux)

#### 1. Application Server

Set up the Flask application as a systemd service for automatic startup:

1. Create a systemd service file (refer to `.example.systemd.conf`)
2. Enable the service to start on boot:
   ```bash
   sudo systemctl enable hukamnama-screen.service
   sudo systemctl start hukamnama-screen.service
   ```

#### 2. Reverse Proxy (Recommended)

For production deployments, especially when accessing remotely, set up Nginx as a reverse proxy:

1. Configure Nginx using the example in `.example.hukamnama.nginx`
2. Enable SSL/TLS for secure remote access
3. Set up firewall rules as needed

#### 3. Kiosk Mode Display

Configure the Raspberry Pi to automatically show the Hukamnama screen on startup:

1. **Configure auto-login** (if not already enabled):

   ```bash
   sudo raspi-config
   ```

   Navigate to: System Options → Boot / Auto Login → Desktop Autologin

2. **Edit the autostart configuration**:

   ```bash
   mkdir -p ~/.config/lxsession/LXDE-pi
   nano ~/.config/lxsession/LXDE-pi/autostart
   ```

3. **Add the following lines**:

   ```bash
   @xset s off
   @xset -dpms
   @xset s noblank
   @chromium-browser --kiosk --noerrdialogs --disable-infobars --disable-session-crashed-bubble http://127.0.0.1:8000
   ```

   This configuration:

   - Disables screen blanking and power management
   - Launches Chromium in kiosk mode pointing to your application
   - Suppresses error dialogs and crash notifications

4. **Reboot to test**:
   ```bash
   sudo reboot
   ```

> [!TIP]
> If using a different desktop environment (LXDE, XFCE, etc.), the autostart path may vary. Common alternatives include:
>
> - `~/.config/autostart/hukamnama.desktop` (create a .desktop file)
> - `~/.config/lxsession/LXDE/autostart` (for standard LXDE)

### Alternative Deployment

For simpler setups without systemd (development or testing):

1. Run the application manually: `uv run python app.py`
2. Access via local network using the server's IP address
3. Open browser in fullscreen mode on display device

## Usage

### For Administrators

1. **Login**: Access the admin panel at `/login`
2. **Search**: Navigate to `/search` to find verses
3. **Update Display**: Select a verse and click "Save as current hukamnama"
4. **Profile Management**: Manage your account at `/profile`

### For Display Screens

1. Point browser to the root URL (`/`)
2. Screen automatically updates when content changes
3. No interaction needed - runs autonomously

## Architecture

```
┌─────────────────┐
│  Admin Device   │──── Search & Update ────┐
│ (Phone/Tablet)  │                         │
└─────────────────┘                         │
                                            ▼
                                    ┌───────────────┐
                                    │  Flask Server │
                                    │  + Socket.IO  │
                                    └───────────────┘
                                            │
                        ┌───────────────────┴───────────────────┐
                        │                                       │
                        ▼                                       ▼
                ┌───────────────┐                      ┌───────────────┐
                │ Display #1    │                      │ Display #2    │
                │ (Raspberry Pi)│                      │ (Raspberry Pi)│
                └───────────────┘                      └───────────────┘
```

The application uses a client-server architecture:

- **Server**: Flask application handling authentication, search, and data management
- **Real-time Layer**: Socket.IO broadcasts updates to all connected clients
- **Displays**: Browser-based clients listening for updates via Socket.IO

## Screenshots

![Screenshot of the Index page](./example-screenshot.png)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/tjgurwara99/hukamnama-screen).
