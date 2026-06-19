# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams['font.family'] = 'DejaVu Sans'

OUT = '/tmp/mock-document/diagrams'
import os
os.makedirs(OUT, exist_ok=True)

def rbox(ax, x, y, w, h, color, edge='none', lw=0):
    p = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.02,rounding_size=0.06',
                        linewidth=lw, edgecolor=edge, facecolor=color)
    ax.add_patch(p)

def arrow(ax, x0, y0, x1, y1, color='#9aa5b1', style='-|>', lw=1.6, connection='arc3,rad=0'):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=14,
                         linewidth=lw, color=color, connectionstyle=connection)
    ax.add_patch(a)

# ---------- Diagram 1: Project lifecycle banner (light theme) ----------
fig, ax = plt.subplots(figsize=(10, 3.6), dpi=200)
ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis('off')
fig.patch.set_facecolor('white')

ax.text(5, 3.35, 'Financial Advisor — Vòng đời dự án (AI Project Lifecycle)',
        ha='center', va='top', fontsize=13, fontweight='bold', color='#1a1a2e')
ax.text(5, 3.0, 'Discover → Design → Develop → Deliver → Evaluate', ha='center', va='top',
        fontsize=9.5, color='#444')

stages = [
    ('1 · Discover', '#f0a02c', [
        'Vấn đề: chọn sai SP tài chính',
        'Người dùng: trẻ, ít KT TC',
        'Mục tiêu: so khớp minh bạch',
        'Định vị: matching engine',
    ]),
    ('2 · Design', '#2f7fd6', [
        'LangGraph DAG cố định',
        'SQL filter + RAG lai',
        'LLM pluggable (auto)',
        'Stub mode chạy đủ',
    ]),
    ('3 · Develop', '#7b4fd6', [
        'Catalog 15 sản phẩm',
        'Hybrid retrieval/product',
        'Scoring 5 chiều',
        'Diversity cap top-5',
    ]),
    ('4 · Deliver', '#1f9d6b', [
        'Next.js form hồ sơ',
        'So sánh top-3',
        'Trace panel agent',
        'Report in/PDF',
    ]),
    ('5 · Evaluate', '#d6455f', [
        'pytest, stub LLM',
        'Đánh giá ranking',
        'Citation đúng nguồn',
        'Compliance đúng lọc',
    ]),
]
n = len(stages)
margin = 0.25
gap = 0.18
w = (10 - 2*margin - gap*(n-1)) / n
y0, h = 0.25, 2.45
for i, (title, color, lines) in enumerate(stages):
    x = margin + i*(w+gap)
    rbox(ax, x, y0, w, h, color)
    ax.text(x + w/2, y0 + h - 0.18, title, ha='center', va='top', fontsize=9.5,
            fontweight='bold', color='white')
    ty = y0 + h - 0.5
    for line in lines:
        ax.text(x + 0.1, ty, '•  ' + line, ha='left', va='top', fontsize=6.8, color='white',
                wrap=True)
        ty -= 0.27
    if i < n - 1:
        arrow(ax, x + w + 0.02, y0 + h*0.55, x + w + gap - 0.02, y0 + h*0.55, color='#999')

ax.annotate('', xy=(margin, y0 + h + 0.18), xytext=(margin + n*(w+gap) - gap, y0 + h + 0.18),
            arrowprops=dict(arrowstyle='-|>', color='#aaaaaa', lw=1.2,
                             connectionstyle='arc3,rad=-0.35'))
ax.text(5, y0 + h + 0.32, 'lặp lại để cải thiện (dữ liệu / scoring / prompt)',
        ha='center', fontsize=7, color='#888', style='italic')
ax.text(5, 0.05, 'Hybrid Retrieval (SQL + RAG) · LLM chỉ gọi ở Recommender · Stub mode = demo không cần API key',
        ha='center', fontsize=7, color='#666')

plt.tight_layout()
fig.savefig(f'{OUT}/lifecycle.png', facecolor='white', bbox_inches='tight')
plt.close(fig)

# ---------- Diagram 2: Architecture (dark theme flowchart) ----------
fig, ax = plt.subplots(figsize=(9, 6.2), dpi=200)
ax.set_xlim(0, 9); ax.set_ylim(0, 6.2); ax.axis('off')
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

ax.text(4.5, 5.95, 'Financial Advisor — Kiến trúc hệ thống (LangGraph DAG)', ha='center',
        va='top', fontsize=12, fontweight='bold', color='#e8e8f0')
ax.text(4.5, 5.65, 'UserProfile → Profiler → Researcher → Recommender → Compliance → RecommendResponse',
        ha='center', va='top', fontsize=8, color='#9aa5b1')

main_x, main_w = 2.5, 4.0
boxes = [
    ('UserProfile (đầu vào)', '#3a3f4b', 'Tuổi, thu nhập, mục tiêu, risk, horizon — stateless, không log PII'),
    ('Profiler', '#d99b2b', 'income_band + age_band · KHÔNG gọi LLM'),
    ('Researcher', '#2fa6a6', 'SQL filter_eligible() + RAG per-candidate (scoped product_id) · KHÔNG gọi LLM'),
    ('Recommender', '#7b5fd6', '5-dim scoring + diversity cap (≤2/provider) + LLM rationale 2 câu · CHỈ ĐÂY GỌI LLM'),
    ('Compliance', '#3f9d5c', 'Lọc risk=high khi risk_appetite=low · cảnh báo tập trung · disclaimer · KHÔNG gọi LLM'),
    ('RecommendResponse (đầu ra)', '#3a3f4b', 'Recommendations + Citations + Trace + ComplianceCheck'),
]
y = 5.25
bh = 0.62
for i, (title, color, desc) in enumerate(boxes):
    rbox(ax, main_x, y - bh, main_w, bh, color)
    ax.text(main_x + 0.15, y - 0.16, title, fontsize=9.5, fontweight='bold', color='white', va='top')
    ax.text(main_x + 0.15, y - 0.4, desc, fontsize=6.6, color='#eee', va='top', wrap=True)
    if i < len(boxes) - 1:
        arrow(ax, main_x + main_w/2, y - bh - 0.02, main_x + main_w/2, y - bh - 0.18, color='#7d8590')
    y -= (bh + 0.2)

# side annotation boxes
rbox(ax, 0.15, 3.55, 1.95, 1.05, '#1f6feb')
ax.text(0.25, 4.5, 'KHO DỮ LIỆU', fontsize=7.5, fontweight='bold', color='white', va='top')
ax.text(0.25, 4.28, '• catalog.json (15 SP)\n  SQLite/PostgreSQL\n• 15 file T&C → ChromaDB\n  (e5-small, chunk 600)',
        fontsize=6.2, color='white', va='top')
arrow(ax, 2.1, 4.0, main_x, 4.0, color='#1f6feb')

rbox(ax, 6.9, 2.2, 1.95, 1.0, '#b5482a')
ax.text(7.0, 3.1, 'LLM (pluggable)', fontsize=7.5, fontweight='bold', color='white', va='top')
ax.text(7.0, 2.9, 'Anthropic → OpenAI\n→ Ollama → Stub\n(tự dò qua .env)', fontsize=6.2, color='white', va='top')
arrow(ax, 6.85, 2.7, main_x + main_w, 2.7, color='#b5482a')

ax.text(4.5, 0.18, 'Stack: FastAPI · LangGraph · SQLAlchemy 2 · ChromaDB · multilingual-e5-small · structlog',
        ha='center', fontsize=6.8, color='#9aa5b1')

plt.tight_layout()
fig.savefig(f'{OUT}/architecture.png', facecolor='#0d1117', bbox_inches='tight')
plt.close(fig)

# ---------- Diagram 3: Hybrid retrieval two-stage (dark theme) ----------
fig, ax = plt.subplots(figsize=(9, 5.2), dpi=200)
ax.set_xlim(0, 9); ax.set_ylim(0, 5.2); ax.axis('off')
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

ax.text(4.5, 5.0, 'Hybrid Retrieval — Hai giai đoạn (Seed ngoại tuyến + Truy vấn trực tuyến)',
        ha='center', va='top', fontsize=11.5, fontweight='bold', color='#e8e8f0')

# stage 1 frame
rbox(ax, 0.3, 3.15, 8.4, 1.35, '#161b22')
ax.text(0.5, 4.35, 'GIAI ĐOẠN 1 · SEED (ngoại tuyến, scripts/seed.py, idempotent)',
        fontsize=8, fontweight='bold', color='#79c0ff', va='top')
s1 = [
    ('catalog.json', '#2f7fd6', '15 sản phẩm → db.merge()'),
    ('tc_docs/*.md', '#2f7fd6', 'chunk 600 ký tự\n(paragraph-aware)'),
    ('Embedding', '#2fa6a6', 'e5-small\nprefix "passage: "'),
    ('ChromaDB', '#7b5fd6', 'metadata:\nproduct_id, type'),
]
x = 0.55
bw, bh = 1.85, 0.8
for i, (t, c, d) in enumerate(s1):
    rbox(ax, x, 3.3, bw, bh, c)
    ax.text(x + bw/2, 3.3 + bh - 0.12, t, ha='center', fontsize=7.5, fontweight='bold', color='white', va='top')
    ax.text(x + bw/2, 3.3 + bh - 0.35, d, ha='center', fontsize=6, color='white', va='top')
    if i < len(s1) - 1:
        arrow(ax, x + bw + 0.04, 3.3 + bh/2, x + bw + 0.2, 3.3 + bh/2, color='#7d8590')
    x += bw + 0.24

# stage 2 frame
rbox(ax, 0.3, 0.95, 8.4, 1.9, '#161b22')
ax.text(0.5, 2.75, 'GIAI ĐOẠN 2 · TRUY VẤN (trực tuyến, mỗi request, sau SQL filter)',
        fontsize=8, fontweight='bold', color='#79c0ff', va='top')
s2 = [
    ('UserProfile', '#3a3f4b', 'goal + risk_appetite\n+ age + income'),
    ('SQL filter', '#d99b2b', 'filter_eligible()\n→ candidates'),
    ('Query E5', '#2fa6a6', 'prefix "query: "\ntừ goal+risk (VI)'),
    ('Chroma search', '#7b5fd6', 'top-2/sản phẩm\nwhere product_id=...'),
    ('Citations', '#3f9d5c', '→ Recommender\n(scoring + LLM)'),
]
x = 0.55
bw, bh = 1.5, 1.05
for i, (t, c, d) in enumerate(s2):
    rbox(ax, x, 1.15, bw, bh, c)
    ax.text(x + bw/2, 1.15 + bh - 0.14, t, ha='center', fontsize=7.3, fontweight='bold', color='white', va='top')
    ax.text(x + bw/2, 1.15 + bh - 0.4, d, ha='center', fontsize=6, color='white', va='top')
    if i < len(s2) - 1:
        arrow(ax, x + bw + 0.03, 1.15 + bh/2, x + bw + 0.18, 1.15 + bh/2, color='#7d8590')
    x += bw + 0.2

arrow(ax, 4.5, 3.3, 4.5, 2.85, color='#b5482a', lw=1.8)
ax.text(4.65, 3.05, 'vector index đã sẵn sàng', fontsize=6, color='#b5482a', va='center')

ax.text(4.5, 0.12, 'Điểm mấu chốt: RAG scoped theo product_id → citation không lẫn nguồn giữa các sản phẩm khác nhau',
        ha='center', fontsize=6.8, color='#9aa5b1')

plt.tight_layout()
fig.savefig(f'{OUT}/retrieval.png', facecolor='#0d1117', bbox_inches='tight')
plt.close(fig)

print('diagrams saved')
