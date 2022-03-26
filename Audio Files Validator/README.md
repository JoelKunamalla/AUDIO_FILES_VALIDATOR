# Validate Audio Files

Using this web application, Users can validate audio files and the associated recognized text. User can also mark wrongly recognized words (for further training on the backend).

## Tech Stack

- Flask (for backend)
- Bootstrap (Styling Framework)

## Development

- Create a virtual environment for this project.

  ```bash
  python3 -m venv venv
  ```

- Activate the virtual environment.

  ```bash
  source venv/bin/activate
  ```

- Install all the dependencies.

  ```bash
  pip3 install -r requirements.txt
  ```

- Start the flask app in debug mode.
  ```bash
  FLASK_APP=app.py FLASK_ENV=development flask run
  ```

## File Structure

- `static` folder contains the audio files that are for validating.
- `Mappings.json` contains a dictionary, with the keys as filename in `static` folder and value as the corresponding text.
- `UserFeedback.json` contains a dictionary, with the keys as filename for each feedback. Each feedback is stored as list of `text`, list of `wrong_words`, `submitted_at` time.

## Flow

- User visits the URL of the app: `http://localhost:5000`.
- A table is shown with the details of audio file name and associated text.
- By clicking on a audio file, user is taken to other page: `http://localhost:5000/feedback/filename`. This page is specific for each file and user can listen to the audio here.

  - User can also mark the incorrect words and submit his/her feedback.
