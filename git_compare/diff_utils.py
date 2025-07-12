import difflib
import streamlit as st


@st.cache_data
def quick_diff_lines(content1: str, content2: str) -> int:
    """นับบรรทัดที่ต่างกันแบบเร็ว (ไม่ต้องสร้าง Side-by-Side Diff)"""
    if content1 is None:
        content1 = ""
    if content2 is None:
        content2 = ""

    lines1 = content1.splitlines()
    lines2 = content2.splitlines()

    if not lines1 and not lines2:
        return 0
    if not lines1:
        return len(lines2)
    if not lines2:
        return len(lines1)

    diffs = list(difflib.ndiff(lines1, lines2))
    changed = sum(1 for d in diffs if d.startswith("+") or d.startswith("-"))
    return changed


@st.cache_data
def make_side_by_side_diff(content1: str, content2: str, desc1: str, desc2: str) -> str:
    """สร้าง Diff แบบ Side-by-Side (HTML)"""
    differ = difflib.HtmlDiff(wrapcolumn=80, tabsize=4)
    return differ.make_file(
        content1.splitlines(),
        content2.splitlines(),
        fromdesc=desc1,
        todesc=desc2,
        context=False,
        numlines=0,
    )
