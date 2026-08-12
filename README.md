# Api-Auto-Test

> 一套基于 Python 的接口自动化测试框架，集成 FastAPI 后端与 Vue 前端看板，具备数据驱动、专业报告与 CI/CD 能力。

## 🎯 解决了什么问题？

传统手工测试效率低、不可复用、结果不直观。本框架实现了：

- **接口自动化**：封装了请求发送、断言、日志，降低用例编写成本
- **数据驱动**：测试数据与代码分离，新增用例只需修改 YAML 文件
- **可视化报告**：Allure 生成专业报告，Vue 看板让非技术人员也能看懂结果
- **持续集成**：GitHub Actions 自动运行测试，代码提交即触发

## 🛠️ 技术栈

| 模块 | 技术 |
|------|------|
| 测试框架 | pytest、requests、PyYAML |
| 测试报告 | Allure |
| 后端 API | FastAPI + uvicorn |
| 前端看板 | Vue 3 + Element Plus + axios |
| 持续集成 | GitHub Actions |
| 包管理 | pip + venv |

## 📁 项目结构
Api_Auto_Test/
├── common/ # 公共模块（请求封装、日志）
│ └── request_handler.py
├── testcases/ # 测试用例
│ └── test_reqres.py
├── testdata/ # 测试数据（YAML 驱动）
│ └── posts_data.yaml
├── reports/ # Allure 报告原始数据
├── api_server.py # FastAPI 后端服务
├── conftest.py # pytest 全局配置
├── requirements.txt # Python 依赖
└── .github/workflows/ # CI 配置


## 🚀 快速开始

1. 克隆项目并安装依赖

```bash
git clone https://github.com/你的用户名/Api-Auto-Test.git
cd Api-Auto-Test
python -m venv venv

# Windows 激活虚拟环境
venv\Scripts\activate

# Mac/Linux 激活虚拟环境
source venv/bin/activate

pip install -r requirements.txt

2. 运行测试
python -m pytest testcases/ --alluredir=reports -v

3. 查看 Allure 报告
allure serve reports

4. 启动后端 API
python api_server.py

5. 启动前端看板
bash
cd ../api_auto_web
npm install
npm run serve
#浏览器访问 http://localhost:8080 查看测试看板。

📊 前端看板
配套前端项目：api_auto_web
基于 Vue 3 + Element Plus，提供：
📈 测试通过率、总数、失败数卡片展示
📋 用例详情列表（名称、状态、耗时）
🔄 一键刷新，实时获取最新测试结果

🔄 CI/CD
每次推送代码到 main 分支，GitHub Actions 会自动：
安装 Python 依赖
运行全部测试用例
上传测试报告
