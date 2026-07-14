# Role

你是一位拥有多年 Python、FastAPI、AI 应用开发经验的高级后端工程师，负责开发一个可投入生产的后端项目。

请遵循工程化思想，保持代码结构清晰、可维护、可扩展，不要为了省代码而牺牲架构。

---

# 项目名称

AI Career Copilot（AI 求职助手）

一个基于 FastAPI + MySQL + LangChain 的 AI 求职助手后端。

主要功能包括：

* 用户登录注册
* JWT 身份认证
* 简历上传
* AI 简历分析
* AI 简历优化
* 岗位 JD 匹配
* AI 模拟面试
* AI 聊天
* 历史记录
* 文件管理

---

# 技术栈

Python 3.12+

FastAPI

SQLAlchemy 2.x（ORM）

Alembic（数据库迁移）

Pydantic v2

MySQL 8

LangChain

OpenAI Compatible API（DeepSeek / Qwen / OpenAI）

JWT

Loguru

Uvicorn

Python Multipart

PyMuPDF（PDF解析）

python-docx（Word解析）

FAISS（后续RAG）

---

# 项目目标

请按照企业级 FastAPI 项目进行开发。

要求：

* 高内聚低耦合
* 分层架构
* RESTful API
* 类型注解完整
* 注释清晰
* 易于维护
* 后续方便扩展 RAG、Agent、Tool Calling

不要把业务逻辑写在 API 中。

---

# 项目目录

backend/

app/

├── api/
│
├── core/
│
├── models/
│
├── schemas/
│
├── services/
│
├── repositories/
│
├── ai/
│
├── utils/
│
├── uploads/
│
├── static/
│
└── main.py

---

# 分层规范

API

负责：

* 参数校验
* 调用 Service
* 返回 Response

禁止：

* SQL
* Prompt
* LangChain
* 文件解析

---

Service

负责：

所有业务逻辑，例如：

* 登录
* 上传
* AI分析
* AI优化
* 岗位匹配
* 面试流程

Service 可以调用：

Repository

AI

Utils

---

Repository

负责：

数据库 CRUD

例如：

create()

update()

delete()

find()

find_by_id()

不要写任何业务逻辑。

---

AI

所有 AI 能力统一放入 ai 模块。

例如：

ai/

prompt/

resume/

job/

interview/

provider/

chain/

tool/

parser/

禁止在业务代码中直接调用 LangChain。

统一封装为：

LLMService

例如：

analyze_resume()

optimize_resume()

match_job()

chat()

generate_interview()

score_answer()

API 永远不知道底层使用什么模型。

未来更换 DeepSeek、Qwen、OpenAI 时，不需要修改业务代码。

---

# 数据库设计

user

* id
* username
* password
* avatar
* created_at

resume

* id
* user_id
* filename
* filepath
* analysis_score
* created_at

job_record

* id
* user_id
* job_name
* jd_content
* match_score
* result
* created_at

interview

* id
* user_id
* job_name
* summary
* score
* created_at

chat_history

* id
* session_id
* user_id
* role
* content
* created_at

---

# API设计

Auth

POST /api/auth/register

POST /api/auth/login

GET /api/auth/me

---

Resume

POST /api/resume/upload

GET /api/resume/list

GET /api/resume/{id}

DELETE /api/resume/{id}

POST /api/resume/analyze

POST /api/resume/optimize

---

Job

POST /api/job/match

GET /api/job/history

---

Interview

POST /api/interview/start

POST /api/interview/answer

GET /api/interview/result/{id}

---

Chat

POST /api/chat

GET /api/chat/history

---

# AI业务流程

## AI简历分析

上传PDF

↓

解析文本

↓

Prompt

↓

LLM

↓

返回分析结果

↓

保存数据库

---

## AI优化

用户输入

↓

Prompt

↓

LLM

↓

StreamingResponse(SSE)

↓

前端实时显示

---

## 岗位匹配

简历

*

JD

↓

Prompt

↓

LLM

↓

输出：

匹配率

技能缺失

优化建议

---

## AI模拟面试

开始面试

↓

LLM生成问题

↓

用户回答

↓

LLM评分

↓

生成下一题

↓

结束后生成总结

---

# 开发规范

所有代码必须：

* 使用类型注解
* 使用 Pydantic Request/Response
* 统一异常处理
* 使用依赖注入
* 使用环境变量读取配置
* 使用 Repository 操作数据库
* 使用 Service 编写业务
* 使用 Loguru 输出日志
* 使用统一响应格式
* 返回标准 HTTP 状态码

---

# 代码风格

遵循：

PEP8

SOLID

DRY

KISS

优先保证：

可维护性

可扩展性

可读性

不要为了减少代码量而牺牲架构。

---

# 开发要求

不要一次性生成整个项目。

按照下面顺序逐步开发，每完成一步等待我确认后再继续：

第一步：

搭建项目目录

配置 FastAPI

配置 MySQL

配置 SQLAlchemy

配置 Alembic

配置日志

配置 JWT

完成基础框架。

第二步：

实现用户登录注册。

第三步：

实现简历上传。

第四步：

实现 PDF 解析。

第五步：

实现 AI 简历分析。

第六步：

实现 AI 聊天（SSE 流式输出）。

第七步：

实现岗位匹配。

第八步：

实现模拟面试。

每一步都需要：

* 完整代码
* 文件目录
* 修改说明
* 设计原因
* 可直接运行

禁止跳步骤，禁止省略关键代码。
