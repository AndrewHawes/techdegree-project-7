# User Profile with Django

#### Profile Page
- [x] Profile page displays all required details:
    - First Name
    - Last Name
    - Email
    - Date of Birth
    - Bio
    - Avatar
    - [x] (EC) Profile page contains additional profile data, 
such as city/state/country of residence, favorite animal, hobby, etc.

#### Edit Page
- [x] Form accepts and saves the required details:
    - First Name
    - Last Name
    - Email
    - Date of Birth
    - Bio
    - Avatar
    - [x] (EC) Form accepts and saves additional profile data.

#### Date of Birth Validation
- [x] Form validates that Date of Birth is a valid date format:
    - YYYY-MM-DD
    - MM/DD/YYYY
    - MM/DD/YY
    - [x] (EC) Integrates date dropdown.

#### Email Validation
- [x] Forms validate that email addresses match and are in a valid format.

#### Bio Validation
- [x] Validates that the bio is 10 characters or longer.
    - [x] (EC) Integrates text formatting capabilities

#### Avatar Upload
- [x] Form accepts and saves an avatar image.
    - [x] (EC) Basic image manipulation added for avatar.

#### Change Password Page
- [x] Form accepts and saves the new password.

#### Password Validation
- [x] Validates that the "current password" is correct, 
"new password" and "confirm password" fields match, and follows the password policy:
    - must not be the same as the current password
    - minimum password length of 14 characters
    - must use both uppercase and lowercase letters
    - must include one or more numerical digits
    - must include one or more of special characters, such as @, #, $
    - cannot contain the username or parts of the user's full name, 
    such as their first name
    - [x] (EC) Password strength meter for new password    
#### Python Coding Style
- [x] Code complies with most common PEP 8 standards of style

# Extras
- [x] Set up logging
- [x] Change ck editor to not take up so much width.
- [ ] Remove extraneous static files
- [ ] Rewrite views with class based views