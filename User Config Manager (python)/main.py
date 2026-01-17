def add_settings(settings, kv_dict):
    key, value = kv_dict
    value = value.lower()
    key = key.lower()

    if key in settings:
        return f"Settings '{key}' already exists!."
    else:
        settings[key] = value
        return f"Settings '{key}' added with value: '{value}' succesfully!"

def update_settings(settings, kv_dict):
    key , value = kv_dict
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return "Settings updated successfully!"
    else:
        return f"Settings '{key}' does not exist!"

def delete_settings(settings, key):
    key = key.lower()
    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting '{key}' does not exist!"

def view_settings(settings):
    if not settings:
        return "No settings available"
    else:
        result = "Current user settings:\n"
        for key,value in settings.items():
            result+= f"{key.capitalize()} : {value}\n"
        return result
settings = {
    'theme' : 'dark',
    'notifications' : 'enabled',
    'volume' : 'high'
    }

print(add_settings(settings, ('Brightness', 'Medium')))
print(update_settings(settings, ('volume', 'Low')))
print(view_settings(settings))
