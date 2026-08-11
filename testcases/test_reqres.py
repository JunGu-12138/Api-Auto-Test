import pytest
import yaml
import os
from common.request_handler import RequestHandler

# 初始化请求处理器
handler = RequestHandler(base_url="https://jsonplaceholder.typicode.com")

# ========== 加载 YAML 数据文件的辅助函数 ==========
def load_test_data(filename):
    """从 testdata 文件夹加载 YAML 测试数据"""
    # 获取当前文件所在目录，然后拼出 testdata 的完整路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, "testdata", filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# ========== 1. 数据驱动：测试获取不同帖子 ==========
# 从 YAML 文件加载 post_ids 列表
test_data = load_test_data("../testdata/posts_data.yaml")
post_ids = test_data["post_ids"]

@pytest.mark.parametrize("post_id", post_ids)
def test_get_post_by_id(post_id):
    """数据驱动：测试获取多个不同ID的帖子"""
    response = handler.get(f"/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    print(f"  ✓ 帖子 {post_id} 获取成功: {data['title'][:30]}...")

# ========== 2. 数据驱动：测试创建多个帖子 ==========
create_data = test_data["create_posts"]

@pytest.mark.parametrize("post_data", create_data)
def test_create_post(post_data):
    """数据驱动：测试创建多个不同的帖子"""
    response = handler.post("/posts", json=post_data)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == post_data["title"]
    print(f"  ✓ 帖子创建成功，标题: {data['title']}")

# ========== 3. 保留原有的简单测试 ==========
def test_get_posts():
    """测试获取帖子列表"""
    response = handler.get("/posts")
    assert response.status_code == 200
    print(f"  ✓ 帖子总数: {len(response.json())}")