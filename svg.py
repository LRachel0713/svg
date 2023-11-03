# -*- coding: utf-8 -*-
import os
import requests
import base64
import hashlib

# 替换以下变量为你自己的 GitHub 用户名、仓库名和 Personal Access Token
github_username = "LRachel0713"
github_repo = "svg"
github_token = "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"

# SVG 文件所在的目录
svg_directory = "/Users/liu/svg"

# 使用 GitHub API 上传文件
def upload_svgs_to_github():
    # 获取目录中所有 SVG 文件
    svg_files = [f for f in os.listdir(svg_directory) if f.endswith('.svg')]

    for svg_file in svg_files:
        svg_file_path = os.path.join(svg_directory, svg_file)

        with open(svg_file_path, "rb") as file:
            content = file.read()

        # 计算 SHA-1 哈希
        sha1_hash = hashlib.sha1(content).hexdigest()

        # 获取已存在文件的信息
        existing_file_url = f"https://api.github.com/repos/LRachel0713/svg/contents/{svg_file}"
        existing_file_response = requests.get(existing_file_url, headers={"Authorization": f"token {github_token}"})
        existing_file_data = existing_file_response.json()

        # 创建文件
        response = requests.put(
            f"https://api.github.com/repos/LRachel0713/svg/contents/{svg_file}",
            headers={
                "Authorization": f"token {github_token}",
                "Accept": "application/vnd.github.v3+json",
            },
            json={
                "message": f"Upload/Update {svg_file}",
                "content": base64.b64encode(content).decode("utf-8"),
                "sha": sha1_hash,
            } if existing_file_response.ok else {
                "message": f"Upload {svg_file}",
                "content": base64.b64encode(content).decode("utf-8"),
            },
        )

        response_data = response.json()

        if response.status_code == 201:
            print(f"SVG 文件 {svg_file} 上传成功")
        else:
            print(f"上传 {svg_file} 失败，错误信息：{response_data['message']}")

# 生成 HTML 页面
def generate_html(download_urls):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SVG 图标展示</title>
    </head>
    <body>
        <h1>SVG 图标展示</h1>
    """

    for download_url in download_urls:
        html_content += f"""
        <div>
            <object type="image/svg+xml" data="{download_url}" width="100" height="100"></object>
            <div>
                <input type="text" id="copyText" value='<object type="image/svg+xml" data="{download_url}" width="100" height="100"></object>' readonly>
                <button onclick="copyToClipboard()">复制</button>
            </div>
        </div>
        """

    html_content += """
        <script>
            function copyToClipboard() {
                var copyText = document.getElementById("copyText");
                copyText.select();
                document.execCommand("copy");
                alert("复制成功！");
            }
        </script>
    </body>
    </html>
    """

    with open("index.html", "w") as html_file:
        html_file.write(html_content)

# 执行上传
download_urls = []
upload_svgs_to_github()

# 获取上传后的下载链接
for svg_file in os.listdir(svg_directory):
    download_urls.append(f"https://raw.githubusercontent.com/LRachel0713/svg/main/{svg_file}")

# 生成 HTML 页面
def generate_html(download_urls):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SVG 图标展示</title>
        <style>
            .icon-container {
                display: inline-block;
                margin: 10px;
                text-align: center;
            }
            .icon-preview {
                width: 100px;
                height: 100px;
                border: 1px solid #ccc;
            }
        </style>
    </head>
    <body>
        <h1>SVG 图标展示</h1>
    """

    for download_url in download_urls:
        html_content += f"""
        <div class="icon-container">
            <div class="icon-preview" style="background: url('{download_url}') center/contain no-repeat;"></div>
            <div class="column">
                <label for="copyText">图标：</label>         
                <button onclick="copyToClipboard()">复制svg代码</button>
            </div>
        </div>
        """

    html_content += """
        <script>
            function copyToClipboard() {
                var copyText = document.getElementById("copyText");
                copyText.select();
                document.execCommand("copy");
                alert("复制成功！");
            }
        </script>
    </body>
    </html>
    """

    with open("index.html", "w") as html_file:
        html_file.write(html_content)

# 执行上传
download_urls = []
upload_svgs_to_github()

# 获取上传后的下载链接
for svg_file in os.listdir(svg_directory):
    download_urls.append(f"https://raw.githubusercontent.com/LRachel0713/svg/main/{svg_file}")

# 生成 HTML 页面
generate_html(download_urls)


