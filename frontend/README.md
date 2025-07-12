# Edu One - Education Platform

This is a [T3 Stack](https://create.t3.gg/) project with AI-powered chat functionality and document ingestion capabilities.

## Features

- **AI Chat Interface**: Integrated sidebar chat with conversation management
- **Smart Title Generation**: AI-powered conversation titles using Groq
- **Document Search**: Vector search through uploaded documents
- **Web Search**: Real-time web search capabilities
- **Message Persistence**: All conversations stored in database

## Environment Variables

Make sure to set up the following environment variables in your `.env` file:

```bash
# Required for AI chat functionality
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key

# Database
DATABASE_URL=your_database_url

# Document processing
UPSTASH_VECTOR_REST_TOKEN=your_upstash_token
UPSTASH_VECTOR_REST_URL=your_upstash_url
LLAMA_CLOUD_API_KEY=your_llama_cloud_key

# File storage
BLOB_READ_WRITE_TOKEN=your_blob_token

# Background jobs
TRIGGER_SECRET_KEY=your_trigger_secret
```

## What's next? How do I make an app with this?

We try to keep this project as simple as possible, so you can start with just the scaffolding we set up for you, and add additional things later when they become necessary.

If you are not familiar with the different technologies used in this project, please refer to the respective docs. If you still are in the wind, please join our [Discord](https://t3.gg/discord) and ask for help.

- [Next.js](https://nextjs.org)
- [NextAuth.js](https://next-auth.js.org)
- [Prisma](https://prisma.io)
- [Drizzle](https://orm.drizzle.team)
- [Tailwind CSS](https://tailwindcss.com)
- [tRPC](https://trpc.io)

## Learn More

To learn more about the [T3 Stack](https://create.t3.gg/), take a look at the following resources:

- [Documentation](https://create.t3.gg/)
- [Learn the T3 Stack](https://create.t3.gg/en/faq#what-learning-resources-are-currently-available) — Check out these awesome tutorials

You can check out the [create-t3-app GitHub repository](https://github.com/t3-oss/create-t3-app) — your feedback and contributions are welcome!

## How do I deploy this?

Follow our deployment guides for [Vercel](https://create.t3.gg/en/deployment/vercel), [Netlify](https://create.t3.gg/en/deployment/netlify) and [Docker](https://create.t3.gg/en/deployment/docker) for more information.
