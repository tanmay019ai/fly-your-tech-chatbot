from langchain.tools import tool

COMPANY_INFO = """
Fly Your Tech (FYT) is a technology company focused on powering digital transformation.

Services:
- Mobile App Development using Flutter, React Native, and Native technologies
- Website Development using React, Next.js, Node.js, and Custom CMS
- Ecommerce Website Development with secure payments and admin dashboards
- Business Process Automation using n8n, Zapier, and AI workflows
- AI Chatbots and Smart Agents including WhatsApp and in-app bots
- SEO and Digital Marketing services
- Custom Software Development tailored to business needs

Technology Stack:
Frontend: React, Next.js, Tailwind CSS, ShadCN UI
Backend: Node.js, Express.js, PostgreSQL, MongoDB
AI & Automation: LangChain, OpenAI, Zapier, n8n
Mobile: Flutter, React Native, Kotlin

Contact Details:
Email: contact@flyyourtech.com
Phone: 7470391011
Website: https://flyyourtech.com
Instagram: @flyyourtech
"""

@tool
def company_info_tool(query: str) -> str:
    """
    Provides information about Fly Your Tech including services, technology stack, and contact details.
    """
    return COMPANY_INFO

