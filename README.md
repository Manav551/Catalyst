# Catalyst AI - AI-Powered Content Generation Platform

A modern, full-stack AI content generation platform inspired by Jasper.ai. Built with React, Node.js, Express, and OpenAI API.

## ✨ Features

- 🤖 **AI-Powered Content Generation** - Create high-quality content using OpenAI's GPT models
- 📝 **50+ Content Templates** - Blog posts, social media, emails, ads, and more
- 🎯 **Brand Voice Management** - Define and maintain consistent brand identity
- ⚡ **Real-time Generation** - Fast content creation with instant results
- 📊 **Content History** - Track and manage all generated content
- 🔐 **User Authentication** - Secure JWT-based authentication
- 💅 **Modern UI/UX** - Beautiful, responsive design with Tailwind CSS
- 🚀 **Production Ready** - Scalable architecture with error handling

## 🏗️ Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Vite** - Next-generation frontend tooling
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Smooth animations
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **React Hot Toast** - Beautiful notifications

### Backend
- **Node.js & Express** - Server framework
- **OpenAI API** - AI content generation
- **JWT** - Authentication
- **bcryptjs** - Password hashing
- **Helmet** - Security middleware
- **Rate Limiting** - API protection

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Node.js** (v16 or higher) - [Download here](https://nodejs.org/)
- **npm** or **yarn** - Comes with Node.js
- **OpenAI API Key** - [Get one here](https://platform.openai.com/api-keys)

## 🚀 Installation & Setup

### 1. Clone or Navigate to the Project

```bash
cd C:\Users\Palash\ai-content-platform
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
npm install

# Create .env file
copy .env.example .env
```

**Edit the `.env` file** and add your configuration:

```env
PORT=5000
NODE_ENV=development
FRONTEND_URL=http://localhost:3000

# IMPORTANT: Add your OpenAI API key here
OPENAI_API_KEY=sk-your-actual-openai-api-key-here

# Generate a random JWT secret (or use this example)
JWT_SECRET=your_super_secret_jwt_key_change_this_in_production
```

### 3. Frontend Setup

```bash
# Open a new terminal and navigate to frontend directory
cd C:\Users\Palash\ai-content-platform\frontend

# Install dependencies
npm install
```

## 🎮 Running the Application

### Start Backend Server

```bash
# In the backend directory
cd C:\Users\Palash\ai-content-platform\backend
npm start
```

You should see:
```
🚀 Server is running on port 5000
📝 Environment: development
```

### Start Frontend Development Server

```bash
# In a new terminal, navigate to frontend directory
cd C:\Users\Palash\ai-content-platform\frontend
npm run dev
```

You should see:
```
  VITE v5.0.8  ready in XXX ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
```

### Access the Application

Open your browser and go to:
**http://localhost:3000**

## 👤 Getting Started

1. **Register** - Create a new account on the registration page
2. **Set up Brand Voice** - Define your brand's tone and style
3. **Choose a Template** - Select from 50+ content templates
4. **Generate Content** - Fill in the details and let AI create your content
5. **Copy & Use** - Copy the generated content and use it anywhere

## 📚 Available Templates

- **Blog Posts** - Comprehensive articles on any topic
- **Social Media** - Engaging posts for all platforms
- **Email Campaigns** - Marketing and promotional emails
- **Product Descriptions** - Persuasive product copy
- **Ad Copy** - High-converting advertisement content
- **SEO Content** - Search-optimized articles
- **Video Scripts** - Engaging video content
- **Landing Pages** - High-converting page copy

## 🔑 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user

### Content
- `POST /api/content/generate` - Generate new content
- `POST /api/content/improve` - Improve existing content
- `POST /api/content/variations` - Generate content variations
- `GET /api/content/history` - Get content history
- `GET /api/content/:id` - Get specific content
- `DELETE /api/content/:id` - Delete content

### Templates
- `GET /api/templates` - Get all templates
- `GET /api/templates/:id` - Get specific template

### Brand Voice
- `POST /api/brand/voice` - Save brand voice
- `GET /api/brand/voice` - Get brand voice
- `DELETE /api/brand/voice` - Delete brand voice

## 🛠️ Development Scripts

### Backend
```bash
npm start          # Start production server
npm run dev        # Start development server with nodemon
```

### Frontend
```bash
npm run dev        # Start development server
npm run build      # Build for production
npm run preview    # Preview production build
```

## 🔒 Security Features

- JWT-based authentication
- Password hashing with bcrypt
- Rate limiting on API endpoints
- Helmet.js security headers
- CORS protection
- Input validation

## 🎨 Customization

### Change Colors
Edit `frontend/tailwind.config.js` to customize the color scheme:

```js
colors: {
  primary: {
    500: '#your-color',
    // ... more shades
  }
}
```

### Add New Templates
Edit `backend/routes/templates.js` and add your template:

```js
{
  id: 'your_template',
  name: 'Your Template Name',
  description: 'Template description',
  category: 'Category Name',
  icon: '🎨',
  fields: [
    { name: 'field1', label: 'Field Label', type: 'text', required: true }
  ]
}
```

## 📝 Environment Variables

### Backend (.env)
| Variable | Description | Required |
|----------|-------------|----------|
| PORT | Server port | No (default: 5000) |
| NODE_ENV | Environment mode | No (default: development) |
| FRONTEND_URL | Frontend URL for CORS | No (default: http://localhost:3000) |
| OPENAI_API_KEY | OpenAI API key | **Yes** |
| JWT_SECRET | JWT secret key | **Yes** |

### Frontend
The frontend automatically proxies API requests to the backend in development mode via Vite configuration.

## 🚨 Troubleshooting

### Backend won't start
- Make sure Node.js is installed: `node --version`
- Check if port 5000 is available
- Verify `.env` file exists and contains OPENAI_API_KEY

### Frontend won't start
- Delete `node_modules` and run `npm install` again
- Make sure backend is running on port 5000
- Check browser console for errors

### OpenAI API errors
- Verify your API key is correct
- Check your OpenAI account has credits
- Ensure you have access to GPT-4 models (or change to GPT-3.5 in `backend/services/openai.js`)

### Database issues
- This app uses in-memory storage by default
- Data is reset when the server restarts
- For production, implement a proper database (MongoDB, PostgreSQL, etc.)

## 🌐 Deployment

### Backend Deployment (e.g., Heroku, Railway, Render)
1. Set environment variables on your hosting platform
2. Set `NODE_ENV=production`
3. Deploy the `backend` directory

### Frontend Deployment (e.g., Vercel, Netlify)
1. Build the frontend: `npm run build`
2. Deploy the `dist` folder
3. Set environment variable `VITE_API_URL` to your backend URL

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🤝 Contributing

This is an educational project. Feel free to fork and customize it for your needs!

## 💡 Tips

- Start with the "Blog Post" template to test the system
- Define your brand voice for consistent content across all generations
- Use specific, detailed prompts for better results
- Generate multiple variations to find the perfect version
- Keep your OpenAI API key secure and never commit it to version control

## 🎯 Next Steps

- Add database integration (MongoDB/PostgreSQL)
- Implement user teams and collaboration
- Add content scheduling features
- Integrate with social media platforms
- Add analytics and usage tracking
- Implement payment/subscription system

## 📧 Support

For issues or questions, please check the code comments or create an issue in your repository.

---

**Built with ❤️ using React, Node.js, and OpenAI**

