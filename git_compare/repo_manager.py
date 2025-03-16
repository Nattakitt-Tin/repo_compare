import os
import shutil
import git
import streamlit as st


def remove_dir(path: str):
    """ลบโฟลเดอร์ (recursive)"""
    if os.path.exists(path):
        shutil.rmtree(path)


@st.cache_data
def clone_repo_if_not_exists(repo_url: str, repo_dir: str):
    """Clone ถ้าโฟลเดอร์ยังไม่มี"""
    if not os.path.exists(repo_dir):
        git.Repo.clone_from(repo_url, repo_dir)
    return True


@st.cache_data
def get_all_branches_and_tags(repo_dir: str):
    """ดึงรายการ Branch/Tag จาก Local Repo"""
    repo = git.Repo(repo_dir)
    branches = [str(b) for b in repo.branches]
    tags = [str(t) for t in repo.tags]
    return branches, tags


@st.cache_data
def list_files_in_ref(repo_dir: str, ref: str):
    """ดึงรายชื่อไฟล์ใน Branch หรือ Tag (เรียก 'ref')"""
    repo = git.Repo(repo_dir)
    file_list = repo.git.ls_tree("-r", "--name-only", ref).split("\n")
    return set(file_list)


@st.cache_data
def get_file_content(repo_dir: str, ref: str, file_path: str) -> str:
    """ดึงเนื้อหาไฟล์จาก ref (Branch/Tag)"""
    repo = git.Repo(repo_dir)
    try:
        return repo.git.show(f"{ref}:{file_path}")
    except git.exc.GitCommandError:
        return ""
