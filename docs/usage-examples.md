# Usage Examples

This guide provides comprehensive examples of how to use Django Easy Icons in various real-world scenarios.

## Basic Usage

### Template Tag Basics

```django
{% load easy_icons %}

<!-- Simple icon -->
{% icon 'home' %}

<!-- Icon with CSS class -->
{% icon 'home' class='nav-icon' %}

<!-- Icon with multiple attributes -->
{% icon 'home' class='nav-icon' height='2em' title='Go Home' %}

<!-- Icon with specific renderer -->
{% icon 'heart' renderer='fontawesome' class='text-red' %}
```

### Python Function Usage

```python
from easy_icons import icon

# In views
def dashboard_view(request):
    home_icon = icon('home', class_='page-icon')
    return render(request, 'dashboard.html', {'home_icon': home_icon})

# In forms
class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = f"{icon('info')} Enter your email address"
```

## Navigation Examples

### Sidebar Navigation

```django
{% load easy_icons %}

<nav class="sidebar">
    <div class="sidebar-header">
        {% icon 'logo' renderer='brand' class='site-logo' %}
        <h3>My App</h3>
    </div>
    
    <ul class="nav flex-column">
        <li class="nav-item">
            <a href="{% url 'dashboard' %}" class="nav-link {% if request.resolver_match.url_name == 'dashboard' %}active{% endif %}">
                {% icon 'dashboard' class='me-2' %}
                Dashboard
            </a>
        </li>
        <li class="nav-item">
            <a href="{% url 'users' %}" class="nav-link {% if request.resolver_match.url_name == 'users' %}active{% endif %}">
                {% icon 'users' class='me-2' %}
                Users
            </a>
        </li>
        <li class="nav-item">
            <a href="{% url 'reports' %}" class="nav-link {% if request.resolver_match.url_name == 'reports' %}active{% endif %}">
                {% icon 'chart' class='me-2' %}
                Reports
            </a>
        </li>
        <li class="nav-item">
            <a href="{% url 'settings' %}" class="nav-link {% if request.resolver_match.url_name == 'settings' %}active{% endif %}">
                {% icon 'settings' class='me-2' %}
                Settings
            </a>
        </li>
    </ul>
    
    <div class="sidebar-footer">
        <a href="{% url 'logout' %}" class="nav-link text-danger">
            {% icon 'logout' class='me-2' %}
            Logout
        </a>
    </div>
</nav>
```

### Breadcrumb Navigation

```django
{% load easy_icons %}

<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="breadcrumb-item">
            <a href="{% url 'dashboard' %}">
                {% icon 'home' class='me-1' %}
                Home
            </a>
        </li>
        <li class="breadcrumb-item">
            <a href="{% url 'users' %}">
                {% icon 'users' class='me-1' %}
                Users
            </a>
        </li>
        <li class="breadcrumb-item active" aria-current="page">
            {% icon 'edit' class='me-1' %}
            Edit User
        </li>
    </ol>
</nav>
```

### Tab Navigation

```django
{% load easy_icons %}

<ul class="nav nav-tabs" id="myTab" role="tablist">
    <li class="nav-item" role="presentation">
        <button class="nav-link active" id="profile-tab" data-bs-toggle="tab" data-bs-target="#profile" type="button">
            {% icon 'user' class='me-2' %}
            Profile
        </button>
    </li>
    <li class="nav-item" role="presentation">
        <button class="nav-link" id="security-tab" data-bs-toggle="tab" data-bs-target="#security" type="button">
            {% icon 'shield' class='me-2' %}
            Security
        </button>
    </li>
    <li class="nav-item" role="presentation">
        <button class="nav-link" id="notifications-tab" data-bs-toggle="tab" data-bs-target="#notifications" type="button">
            {% icon 'bell' class='me-2' %}
            Notifications
        </button>
    </li>
</ul>
```

## Form Examples

### Form with Icon Labels

```django
{% load easy_icons %}

<form method="post">
    {% csrf_token %}
    
    <div class="mb-3">
        <label for="email" class="form-label">
            {% icon 'email' class='me-2 text-muted' %}
            Email Address
        </label>
        <input type="email" class="form-control" id="email" name="email" required>
    </div>
    
    <div class="mb-3">
        <label for="password" class="form-label">
            {% icon 'lock' class='me-2 text-muted' %}
            Password
        </label>
        <input type="password" class="form-control" id="password" name="password" required>
    </div>
    
    <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="remember">
        <label class="form-check-label" for="remember">
            {% icon 'check' class='me-2 text-success' %}
            Remember me
        </label>
    </div>
    
    <button type="submit" class="btn btn-primary">
        {% icon 'login' class='me-2' %}
        Sign In
    </button>
</form>
```

### Form Action Buttons

```django
{% load easy_icons %}

<div class="form-actions d-flex gap-2">
    <button type="submit" class="btn btn-primary">
        {% icon 'save' class='me-2' %}
        Save Changes
    </button>
    
    <button type="button" class="btn btn-secondary" onclick="history.back()">
        {% icon 'cancel' class='me-2' %}
        Cancel
    </button>
    
    <button type="button" class="btn btn-outline-primary" onclick="previewForm()">
        {% icon 'preview' class='me-2' %}
        Preview
    </button>
    
    <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#deleteModal">
        {% icon 'delete' class='me-2' %}
        Delete
    </button>
</div>
```

### Search Form

```django
{% load easy_icons %}

<form class="d-flex" role="search" method="get">
    <div class="input-group">
        <span class="input-group-text">
            {% icon 'search' %}
        </span>
        <input class="form-control" type="search" name="q" placeholder="Search..." value="{{ request.GET.q }}">
        
        {% if request.GET.q %}
        <a href="?" class="btn btn-outline-secondary" title="Clear search">
            {% icon 'x' %}
        </a>
        {% endif %}
        
        <button class="btn btn-primary" type="submit">
            {% icon 'search' class='me-2' %}
            Search
        </button>
    </div>
</form>
```

## Data Display Examples

### Data Table with Actions

```django
{% load easy_icons %}

<div class="table-responsive">
    <table class="table table-striped">
        <thead>
            <tr>
                <th>
                    {% icon 'user' class='me-2' %}
                    Name
                </th>
                <th>
                    {% icon 'email' class='me-2' %}
                    Email
                </th>
                <th>
                    {% icon 'calendar' class='me-2' %}
                    Joined
                </th>
                <th>
                    {% icon 'shield' class='me-2' %}
                    Status
                </th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <td>
                    {% if user.avatar %}
                        <img src="{{ user.avatar.url }}" class="rounded-circle me-2" width="32" height="32">
                    {% else %}
                        {% icon 'user-circle' class='me-2 text-muted' %}
                    {% endif %}
                    {{ user.name }}
                </td>
                <td>{{ user.email }}</td>
                <td>{{ user.date_joined|date:"M d, Y" }}</td>
                <td>
                    {% if user.is_active %}
                        {% icon 'check-circle' class='text-success me-1' %}
                        Active
                    {% else %}
                        {% icon 'x-circle' class='text-danger me-1' %}
                        Inactive
                    {% endif %}
                </td>
                <td>
                    <div class="btn-group" role="group">
                        <a href="{% url 'user_detail' user.id %}" class="btn btn-sm btn-outline-info" title="View">
                            {% icon 'eye' %}
                        </a>
                        <a href="{% url 'user_edit' user.id %}" class="btn btn-sm btn-outline-warning" title="Edit">
                            {% icon 'edit' %}
                        </a>
                        <a href="{% url 'user_delete' user.id %}" class="btn btn-sm btn-outline-danger" title="Delete" onclick="return confirm('Are you sure?')">
                            {% icon 'trash' %}
                        </a>
                    </div>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="5" class="text-center text-muted py-4">
                    {% icon 'inbox' class='me-2' %}
                    No users found
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
```

### Card Layout

```django
{% load easy_icons %}

<div class="row">
    {% for product in products %}
    <div class="col-md-4 mb-4">
        <div class="card">
            {% if product.image %}
            <img src="{{ product.image.url }}" class="card-img-top" alt="{{ product.name }}">
            {% else %}
            <div class="card-img-top bg-light d-flex align-items-center justify-content-center" style="height: 200px;">
                {% icon 'image' class='text-muted' height='3em' %}
            </div>
            {% endif %}
            
            <div class="card-body">
                <h5 class="card-title">{{ product.name }}</h5>
                <p class="card-text">{{ product.description|truncatewords:20 }}</p>
                
                <div class="d-flex justify-content-between align-items-center">
                    <span class="text-primary fw-bold">${{ product.price }}</span>
                    
                    <div class="btn-group">
                        <button class="btn btn-sm btn-outline-primary">
                            {% icon 'cart-plus' class='me-1' %}
                            Add to Cart
                        </button>
                        <a href="{% url 'product_detail' product.id %}" class="btn btn-sm btn-outline-secondary">
                            {% icon 'eye' %}
                        </a>
                    </div>
                </div>
                
                <div class="mt-2">
                    {% icon 'star-fill' class='text-warning' %}
                    {% icon 'star-fill' class='text-warning' %}
                    {% icon 'star-fill' class='text-warning' %}
                    {% icon 'star-fill' class='text-warning' %}
                    {% icon 'star' class='text-muted' %}
                    <small class="text-muted ms-1">({{ product.reviews.count }} reviews)</small>
                </div>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
```

### Statistics Dashboard

```django
{% load easy_icons %}

<div class="row mb-4">
    <div class="col-lg-3 col-md-6 mb-3">
        <div class="card bg-primary text-white">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <div class="fs-6 text-uppercase">Total Users</div>
                        <div class="fs-2 fw-bold">{{ total_users }}</div>
                    </div>
                    {% icon 'users' height='3em' class='text-white-50' %}
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-lg-3 col-md-6 mb-3">
        <div class="card bg-success text-white">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <div class="fs-6 text-uppercase">Revenue</div>
                        <div class="fs-2 fw-bold">${{ total_revenue }}</div>
                    </div>
                    {% icon 'currency-dollar' height='3em' class='text-white-50' %}
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-lg-3 col-md-6 mb-3">
        <div class="card bg-warning text-white">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <div class="fs-6 text-uppercase">Orders</div>
                        <div class="fs-2 fw-bold">{{ total_orders }}</div>
                    </div>
                    {% icon 'shopping-cart' height='3em' class='text-white-50' %}
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-lg-3 col-md-6 mb-3">
        <div class="card bg-info text-white">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <div class="fs-6 text-uppercase">Products</div>
                        <div class="fs-2 fw-bold">{{ total_products }}</div>
                    </div>
                    {% icon 'box' height='3em' class='text-white-50' %}
                </div>
            </div>
        </div>
    </div>
</div>
```

## Modal and Alert Examples

### Confirmation Modal

```django
{% load easy_icons %}

<!-- Delete Confirmation Modal -->
<div class="modal fade" id="deleteModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">
                    {% icon 'exclamation-triangle' class='text-warning me-2' %}
                    Confirm Deletion
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <p>Are you sure you want to delete this item? This action cannot be undone.</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                    {% icon 'x' class='me-2' %}
                    Cancel
                </button>
                <button type="button" class="btn btn-danger" id="confirmDelete">
                    {% icon 'trash' class='me-2' %}
                    Delete
                </button>
            </div>
        </div>
    </div>
</div>
```

### Alert Messages

```django
{% load easy_icons %}

{% if messages %}
<div class="alerts-container">
    {% for message in messages %}
    <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
        {% if message.tags == 'success' %}
            {% icon 'check-circle' class='me-2' %}
        {% elif message.tags == 'error' %}
            {% icon 'x-circle' class='me-2' %}
        {% elif message.tags == 'warning' %}
            {% icon 'exclamation-triangle' class='me-2' %}
        {% elif message.tags == 'info' %}
            {% icon 'info-circle' class='me-2' %}
        {% endif %}
        
        {{ message }}
        
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
    {% endfor %}
</div>
{% endif %}
```

## Complex UI Examples

### File Upload Interface

```django
{% load easy_icons %}

<div class="upload-area border border-2 border-dashed rounded p-4 text-center">
    <div class="upload-icon mb-3">
        {% icon 'cloud-upload' height='4em' class='text-muted' %}
    </div>
    
    <h4>Upload Files</h4>
    <p class="text-muted">Drag and drop files here or click to browse</p>
    
    <input type="file" id="fileInput" multiple hidden>
    <button type="button" class="btn btn-primary" onclick="document.getElementById('fileInput').click()">
        {% icon 'folder-open' class='me-2' %}
        Choose Files
    </button>
    
    <div class="uploaded-files mt-3" id="uploadedFiles" style="display: none;">
        <h6>
            {% icon 'files' class='me-2' %}
            Uploaded Files
        </h6>
        <div class="file-list"></div>
    </div>
</div>

<script>
document.getElementById('fileInput').addEventListener('change', function(e) {
    const fileList = document.querySelector('.file-list');
    const uploadedFiles = document.getElementById('uploadedFiles');
    
    fileList.innerHTML = '';
    
    Array.from(e.target.files).forEach(file => {
        const fileItem = document.createElement('div');
        fileItem.className = 'file-item d-flex justify-content-between align-items-center p-2 border rounded mb-2';
        fileItem.innerHTML = `
            <div>
                {% icon 'file' class='me-2' %}
                ${file.name}
                <small class="text-muted">(${Math.round(file.size / 1024)} KB)</small>
            </div>
            <button type="button" class="btn btn-sm btn-outline-danger" onclick="this.parentElement.remove()">
                {% icon 'x' %}
            </button>
        `;
        fileList.appendChild(fileItem);
    });
    
    uploadedFiles.style.display = e.target.files.length > 0 ? 'block' : 'none';
});
</script>
```

### Profile Page

```django
{% load easy_icons %}

<div class="container mt-4">
    <div class="row">
        <!-- Profile Sidebar -->
        <div class="col-md-4">
            <div class="card">
                <div class="card-body text-center">
                    {% if user.avatar %}
                    <img src="{{ user.avatar.url }}" class="rounded-circle mb-3" width="120" height="120">
                    {% else %}
                    <div class="rounded-circle bg-light d-inline-flex align-items-center justify-content-center mb-3" style="width: 120px; height: 120px;">
                        {% icon 'user' height='3em' class='text-muted' %}
                    </div>
                    {% endif %}
                    
                    <h4>{{ user.get_full_name }}</h4>
                    <p class="text-muted">{{ user.email }}</p>
                    
                    <div class="d-grid gap-2">
                        <a href="{% url 'profile_edit' %}" class="btn btn-primary">
                            {% icon 'edit' class='me-2' %}
                            Edit Profile
                        </a>
                        <a href="{% url 'change_password' %}" class="btn btn-outline-secondary">
                            {% icon 'key' class='me-2' %}
                            Change Password
                        </a>
                    </div>
                </div>
            </div>
            
            <!-- Quick Stats -->
            <div class="card mt-3">
                <div class="card-header">
                    {% icon 'chart-bar' class='me-2' %}
                    Quick Stats
                </div>
                <div class="card-body">
                    <div class="row text-center">
                        <div class="col-6">
                            <div class="border-end">
                                {% icon 'calendar' class='text-primary mb-2' %}
                                <div class="fw-bold">{{ user.date_joined|timesince }}</div>
                                <small class="text-muted">Member Since</small>
                            </div>
                        </div>
                        <div class="col-6">
                            {% icon 'activity' class='text-success mb-2' %}
                            <div class="fw-bold">{{ user.last_login|timesince }}</div>
                            <small class="text-muted">Last Active</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Main Content -->
        <div class="col-md-8">
            <!-- Recent Activity -->
            <div class="card">
                <div class="card-header">
                    {% icon 'clock' class='me-2' %}
                    Recent Activity
                </div>
                <div class="card-body">
                    {% for activity in recent_activities %}
                    <div class="d-flex align-items-start mb-3">
                        <div class="me-3">
                            {% if activity.type == 'login' %}
                                {% icon 'login' class='text-success' %}
                            {% elif activity.type == 'edit' %}
                                {% icon 'edit' class='text-warning' %}
                            {% elif activity.type == 'create' %}
                                {% icon 'plus' class='text-primary' %}
                            {% endif %}
                        </div>
                        <div class="flex-grow-1">
                            <div>{{ activity.description }}</div>
                            <small class="text-muted">{{ activity.timestamp|timesince }} ago</small>
                        </div>
                    </div>
                    {% empty %}
                    <div class="text-center text-muted py-4">
                        {% icon 'inbox' class='me-2' %}
                        No recent activity
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>
```

## Advanced Integration Examples

### Dynamic Icon Loading

```python
# views.py
from easy_icons import icon

def get_status_icon(status):
    """Return appropriate icon for status."""
    status_icons = {
        'active': icon('check-circle', class_='text-success'),
        'inactive': icon('x-circle', class_='text-danger'),
        'pending': icon('clock', class_='text-warning'),
        'processing': icon('gear', class_='text-info spinning'),
    }
    return status_icons.get(status, icon('question-circle', class_='text-muted'))

def dashboard_view(request):
    users = User.objects.all()
    user_data = []
    
    for user in users:
        user_data.append({
            'user': user,
            'status_icon': get_status_icon(user.status),
            'actions': [
                {
                    'icon': icon('eye', class_='text-info'),
                    'url': reverse('user_detail', args=[user.id]),
                    'title': 'View'
                },
                {
                    'icon': icon('edit', class_='text-warning'),
                    'url': reverse('user_edit', args=[user.id]),
                    'title': 'Edit'
                }
            ]
        })
    
    return render(request, 'dashboard.html', {'user_data': user_data})
```

### Custom Template Tags with Icons

```python
# templatetags/custom_tags.py
from django import template
from easy_icons import icon

register = template.Library()

@register.simple_tag
def status_badge(status):
    """Render a status badge with appropriate icon and color."""
    status_config = {
        'active': {'icon': 'check-circle', 'class': 'badge bg-success', 'text': 'Active'},
        'inactive': {'icon': 'x-circle', 'class': 'badge bg-danger', 'text': 'Inactive'},
        'pending': {'icon': 'clock', 'class': 'badge bg-warning', 'text': 'Pending'},
    }
    
    config = status_config.get(status, {'icon': 'question', 'class': 'badge bg-secondary', 'text': 'Unknown'})
    icon_html = icon(config['icon'], class_='me-1')
    
    return f'<span class="{config["class"]}">{icon_html}{config["text"]}</span>'

@register.simple_tag
def action_button(action_type, url, **kwargs):
    """Render an action button with appropriate icon."""
    actions = {
        'view': {'icon': 'eye', 'class': 'btn-outline-info', 'title': 'View'},
        'edit': {'icon': 'edit', 'class': 'btn-outline-warning', 'title': 'Edit'},
        'delete': {'icon': 'trash', 'class': 'btn-outline-danger', 'title': 'Delete'},
    }
    
    action = actions.get(action_type, {'icon': 'question', 'class': 'btn-outline-secondary', 'title': 'Action'})
    
    # Merge any additional kwargs
    action.update(kwargs)
    
    icon_html = icon(action['icon'])
    return f'<a href="{url}" class="btn btn-sm {action["class"]}" title="{action["title"]}">{icon_html}</a>'
```

```django
<!-- Usage in templates -->
{% load custom_tags %}

<!-- Status badge -->
{% status_badge user.status %}

<!-- Action buttons -->
{% action_button 'view' user.get_absolute_url %}
{% action_button 'edit' user.get_edit_url %}
{% action_button 'delete' user.get_delete_url %}
```

These examples demonstrate the flexibility and power of Django Easy Icons in real-world applications. The key is to think of icons as semantic elements that enhance user understanding and provide visual cues for different types of content and actions.
