# Create Separate Admin User - Instructions

## Option A: Via Render Shell (Recommended)

1. **Go to your Render dashboard**: https://dashboard.render.com/
2. **Select your backend service**: `aurora-grand-hotel-backend`
3. **Click "Shell"** in the top right
4. **Run these commands**:

```bash
python manage.py shell
```

Then paste this code:

```python
from django.contrib.auth.models import User

# Create admin user
username = 'hoteladmin'
email = 'admin@aurorагrandhotel.com'  # Optional, you can change this
password = 'ChangeThisPassword123!'  # CHANGE THIS!

# Check if user exists
if User.objects.filter(username=username).exists():
    print(f"User '{username}' already exists!")
else:
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"✅ Admin created!")
    print(f"Username: {username}")
    print(f"Password: {password}")
```

Press `Ctrl+D` to exit the shell.

---

## Option B: Create via Django Admin (If you have access)

If you can access the Django admin with your current account:

1. Go to: https://aurora-grand-hotel-backend.onrender.com/admin/
2. Click **"Users"** → **"Add User"**
3. Create user:
   - Username: `hoteladmin`
   - Password: [choose a strong password]
4. After saving, check these boxes:
   - ✅ **Staff status**
   - ✅ **Superuser status**
5. Save

---

## Option C: Remove Frontend User Account

If you want to stop using `nnamdieze849@gmail.com` for frontend:

1. Go to Django admin
2. Find the user with email `nnamdieze849@gmail.com`
3. Either:
   - **Delete it** (if you don't need it for frontend testing)
   - **Change the email** to something generic like `test@example.com`

---

## After Creating Admin User

**Login with your new admin credentials:**
- URL: https://aurora-grand-hotel-backend.onrender.com/admin/
- Username: `hoteladmin`
- Password: [the password you set]

**Then logout from `nnamdieze849@gmail.com`** so Django doesn't remember that session.

---

## Security Note

⚠️ **Change the default password** immediately after first login!

Go to: **Admin** → **Users** → **hoteladmin** → **Change password**
