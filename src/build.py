# -*- coding: utf-8 -*-
"""ARTUS 정적 페이지 생성기.
python src/build.py  → 저장소 루트에 index.html 등 7개 페이지와 404.html을 쓴다.
헤더·푸터·메타를 한 곳에서 관리하기 위한 것이며, 산출 HTML은 의존성 없이 그대로 서비스된다."""
import os, datetime, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pages_ax import AX, DECISIONMAKER
from pages_insights import HUB, ENERGY, SPACE, AI, BIO
from pages_philosophy import PHILOSOPHY as PHILOSOPHY_NEW, VALUES_INTRO

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def _v(*files):
    h = hashlib.md5()
    for f in files:
        h.update(open(os.path.join(ROOT, f), "rb").read())
    return h.hexdigest()[:8]
V = _v("css/site.css", "css/site-extra.css", "js/site.js")
SITE = "https://artus.kr"
YEAR = datetime.date.today().year

NAV = [("index.html", "홈"), ("philosophy.html", "투자 철학"), ("services.html", "업무 분야"),
       ("ax.html", "AX 컨설팅"), ("decisionmaker.html", "디시전메이커"), ("achievements.html", "주요 성과"),
       ("insights.html", "인사이트"), ("team.html", "구성원")]
FOOT_EXTRA = [("values.html", "핵심 가치")]

HEAD = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B1E3A">
<link rel="canonical" href="{site}/{file}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ARTUS">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{site}/{file}">
<meta property="og:image" content="{site}/images/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Noto+Serif+KR:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="stylesheet" href="css/site.css?v={v}">
<link rel="stylesheet" href="css/site-extra.css?v={v}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FinancialService","name":"ARTUS (주식회사 아르투스)","url":"{site}","email":"contact@artus.kr","telephone":"+82-2-761-2025","faxNumber":"+82-2-761-2035","address":{{"@type":"PostalAddress","streetAddress":"여의나루로 53-1 대오빌딩 14층","addressLocality":"영등포구","addressRegion":"서울","addressCountry":"KR"}},"description":"{desc}"}}</script>
</head>
<body>
<a class="skip" href="#main">본문으로 건너뛰기</a>
<header class="nav" role="banner">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="ARTUS 홈">
      <span class="mark">ART<b>US</b></span>
      <span class="sub">Private Equity · AI Transformation</span>
    </a>
    <button class="burger" aria-label="메뉴 열기" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav-links" aria-label="주 메뉴">
{navlinks}
      <a class="cta" href="contact.html">문의하기</a>
    </nav>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<section class="cta-band">
  <div class="wrap">
    <div>
      <div class="eyebrow">Contact</div>
      <h2 class="h-l">함께 성장할 파트너를 찾고 있다면</h2>
      <p class="lead" style="margin-top:14px;max-width:52ch">투자 제안, 인수·매각, 자금 조달, 승계 설계까지. 어떤 단계든 편하게 연락 주십시오.</p>
    </div>
    <a class="btn solid" href="contact.html">문의하기 <span class="arr">→</span></a>
  </div>
</section>
<footer class="footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="brand"><span class="mark">ART<b>US</b></span></div>
        <p class="blurb">Intelligence Meets Capital. 주식회사 아르투스는 AI로 사람을 사람의 일로 돌려보내고 그 변화에 자본을 더하는 프라이빗 에쿼티 파트너입니다. 책임·정직·신뢰·이해·전문성.</p>
      </div>
      <div>
        <h4>Menu</h4>
        <ul>
{footlinks}
          <li><a href="contact.html">문의하기</a></li>
        </ul>
      </div>
      <div>
        <h4>Office</h4>
        <ul>
          <li>서울시 영등포구 여의나루로 53-1 대오빌딩 14층</li>
          <li>Tel <a href="tel:027612025">02-761-2025</a> · Fax 02-761-2035</li>
          <li><a href="mailto:contact@artus.kr">contact@artus.kr</a></li>
        </ul>
      </div>
    </div>
    <div class="legal">
      <span>© {year} ARTUS · 주식회사 아르투스. All rights reserved.</span>
      <span>Seoul, Korea</span>
    </div>
  </div>
</footer>
<script src="js/site.js?v={v}" defer></script>
</body>
</html>
"""

def page(file, title, desc, body):
    navlinks = "\n".join(f'      <a href="{f}">{n}</a>' for f, n in NAV)
    footlinks = "\n".join(f'          <li><a href="{f}">{n}</a></li>' for f, n in NAV[1:] + FOOT_EXTRA)
    html = HEAD.format(title=title, desc=desc, site=SITE, file=file, navlinks=navlinks, v=V) + body + FOOT.format(footlinks=footlinks, year=YEAR, v=V)
    with open(os.path.join(ROOT, file), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", file)

ORN = """<svg class="orn" viewBox="0 0 520 520" fill="none" aria-hidden="true">
  <circle cx="260" cy="260" r="258" stroke="rgba(180,151,90,.25)"/>
  <circle cx="260" cy="260" r="200" stroke="rgba(180,151,90,.18)"/>
  <circle cx="260" cy="260" r="140" stroke="rgba(180,151,90,.14)"/>
  <path d="M260 2v516M2 260h516" stroke="rgba(180,151,90,.14)"/>
  <path d="M78 78l364 364M442 78L78 442" stroke="rgba(180,151,90,.1)"/>
  <circle cx="260" cy="60" r="4" fill="#B4975A"/>
  <circle cx="460" cy="260" r="3" fill="#B4975A" opacity=".7"/>
  <circle cx="120" cy="400" r="2.5" fill="#B4975A" opacity=".6"/>
</svg>"""

# ───────────────────────── index ─────────────────────────
INDEX = f"""
<section class="hero">
  <div class="wrap">
    <div class="eyebrow rv">Private Equity · AI Transformation · Seoul</div>
    <h1 class="h-xl rv d1 latin" style="font-size:clamp(2.6rem,6.2vw,5.4rem);letter-spacing:.01em">Intelligence<br>Meets Capital.</h1>
    <p class="lead rv d2">지성과 자본이 만나는 곳. AI로 사람을 사람의 일로 돌려보내고, 그 변화에 자본을 더합니다. 우리 자신부터 그렇게 바꿨습니다.</p>
    <div class="actions rv d3">
      <a class="btn solid" href="philosophy.html">투자 철학 <span class="arr">→</span></a>
      <a class="btn" href="ax.html">AX 컨설팅</a>
    </div>
  </div>
  {ORN}
  <div class="since">Intelligence Meets Capital · Yeouido</div>
  <div class="scroll-cue"><i></i>Scroll</div>
</section>

<section class="acro">
  <div class="wrap">
    <div class="cell rv"><span class="l">A</span><span class="w">Accountability</span><span class="k">책임 · 수탁자 의무</span></div>
    <div class="cell rv d1"><span class="l">R</span><span class="w">Righteousness</span><span class="k">정직 · 투명한 운용</span></div>
    <div class="cell rv d2"><span class="l">T</span><span class="w">Trust</span><span class="k">신뢰 · 성과로 입증</span></div>
    <div class="cell rv d3"><span class="l">U</span><span class="w">Understanding</span><span class="k">이해 · 고객과 시장</span></div>
    <div class="cell rv d4"><span class="l">S</span><span class="w">Specialty</span><span class="k">전문성 · 차별화된 전략</span></div>
  </div>
</section>

<section class="section on-ivory">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow rv">01 — Who we are</div>
        <h2 class="h-l rv d1">이름에 담은<br>다섯 가지 약속</h2>
      </div>
      <div class="prose">
        <p class="rv">ARTUS는 고객 자산의 안정적인 성장을 추구하는 프라이빗 에쿼티 파트너입니다. 우리의 이름에 담긴 각 글자는 회사의 핵심 가치를 상징합니다.</p>
        <p class="rv d1"><strong>Accountability</strong>(책임)과 <strong>Righteousness</strong>(정직)을 기반으로, <strong>Trust</strong>(신뢰)와 <strong>Understanding</strong>(이해)를 바탕으로 한 <strong>Specialty</strong>(전문성)을 추구합니다.</p>
        <p class="rv d2">ARTUS는 단순한 회사명이 아닌, 고객과 함께 성장하는 진정한 자산운용 파트너로서 다섯 가지 핵심 가치를 실천하며, 이를 통해 고객 자산의 안정적인 성장을 실현하는 것을 궁극적인 목표로 합니다.</p>
        <a class="btn rv d3" href="values.html" style="margin-top:10px">핵심 가치 자세히 <span class="arr">→</span></a>
      </div>
    </div>
  </div>
</section>

<section class="section tight on-paper">
  <div class="wrap">
    <div class="eyebrow rv">02 — Track record</div>
    <div class="stats rv d1">
      <div class="stat"><div class="n"><span data-count="59">0</span><small>%</small></div><div class="t">최고 연환산 수익률</div><div class="s">만나코퍼레이션 · 스트라이커 스카이 제1호</div></div>
      <div class="stat"><div class="n"><span data-count="2.52" data-dec="2">0</span><small>x</small></div><div class="t">최고 투자 배수</div><div class="s">원금 대비 회수 배수</div></div>
      <div class="stat"><div class="n"><span data-count="4">0</span><small>건</small></div><div class="t">운용 완료 펀드</div><div class="s">모르가르텐 · 파밍 · 아레나 · 스카이</div></div>
      <div class="stat"><div class="n"><span data-count="0">0</span><small>건</small></div><div class="t">원금 손실</div><div class="s">풋옵션 등 구조적 위험관리</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="sticky">
        <div class="eyebrow rv">03 — What we do</div>
        <h2 class="h-l rv d1">자본을 효율적으로<br>배치하는 네 가지 방식</h2>
        <p class="lead rv d2" style="margin-top:20px">기업을 중심으로 구상하고, 기업을 중심으로 구현합니다.</p>
        <a class="btn rv d3" href="services.html" style="margin-top:8px">업무 분야 전체 보기 <span class="arr">→</span></a>
      </div>
      <div class="grid grid-2">
        <a class="card rv" href="services.html#ma"><div class="num">01</div><h3>기업인수합병 (M&amp;A)</h3><p>가치 분석과 적정 인수가격 산정, 실사, 거래구조 설계와 협상, 인수 후 통합(PMI)까지 한 팀이 끝까지 맡습니다.</p><span class="more">자세히 →</span></a>
        <a class="card rv d1" href="services.html#equity"><div class="num">02</div><h3>지분투자</h3><p>성장 잠재력 있는 기업을 발굴해 지분을 인수하고, 이사회 참여와 재무구조 개선으로 기업가치를 높인 뒤 회수합니다.</p><span class="more">자세히 →</span></a>
        <a class="card rv d2" href="services.html#syndication"><div class="num">03</div><h3>신디케이션</h3><p>인프라·부동산·인수금융 등 대규모 자금을 복수 금융기관과 함께 조달하고, 주간사로서 조건을 설계하고 대주단을 운영합니다.</p><span class="more">자세히 →</span></a>
        <a class="card rv d3" href="services.html#succession"><div class="num">04</div><h3>상속·증여 설계</h3><p>기업 오너 지분의 승계 방안을 세무·법률 전문가와 함께 설계하고, 가업승계와 지배구조 개선, 납부 자금까지 계획합니다.</p><span class="more">자세히 →</span></a>
      </div>
    </div>
  </div>
</section>

<section class="section on-ivory">
  <div class="wrap">
    <div class="eyebrow rv">04 — Selected investments</div>
    <div class="split" style="align-items:end;margin-bottom:40px">
      <h2 class="h-l rv d1">숫자로 남은 원칙</h2>
      <p class="lead rv d2">시작이 좋았던 딜도, 팬데믹을 만난 딜도 있었습니다. 어느 경우든 투자자에게 약속한 것을 지켰습니다.</p>
    </div>
    <div class="grid grid-2">
      <div class="deal rv"><div><div class="fund">스트라이커 스카이 제1호</div><h3>만나코퍼레이션</h3><p>배달 대행 상위 5개사 중 성장률과 CEO 전문성이 가장 높은 기업. 2년 만에 5위에서 2위로 올라섰고, 전략적 투자자에게 회수했습니다.</p></div><div class="kpi"><div class="n">59<small>%</small></div><div class="x">2.52x</div><div class="lbl">IRR · MOIC</div></div></div>
      <div class="deal rv d1"><div><div class="fund">스트라이커 파밍 제1호</div><h3>에이치앤비아시아</h3><p>창업자이자 2대 주주의 MBO를 구현한 구조화 딜. 사과 '엔비'의 아시아 독점 판권을 가진 과일 유통사에서 안정적인 현금흐름을 확인했습니다.</p></div><div class="kpi"><div class="n">39<small>%</small></div><div class="x">2.32x</div><div class="lbl">IRR · MOIC</div></div></div>
      <div class="deal rv d2"><div><div class="fund">스트라이커 모르가르텐 제1호</div><h3>마제스티 골프 코리아</h3><p>하이엔드 골프 장비 제조사. 당사가 해외 기업을 인수한 첫 사례로, 스마트스코어·SGPE와 컨소시엄을 구성했습니다.</p></div><div class="kpi"><div class="n">9<small>%</small></div><div class="x">1.09x</div><div class="lbl">IRR · MOIC</div></div></div>
      <div class="deal rv d3"><div><div class="fund">스트라이커 아레나 제1호</div><h3>아프리카 오픈스튜디오</h3><p>스트리밍 기업의 PC방 진출에 FI로 참여. 팬데믹으로 시장이 닫혔지만 풋옵션으로 손실 없이 마무리한 위험관리 사례입니다.</p></div><div class="kpi"><div class="n">0</div><div class="x">손실 없음</div><div class="lbl">Downside protected</div></div></div>
    </div>
    <div style="margin-top:36px" class="rv"><a class="btn" href="achievements.html">주요 성과 전체 보기 <span class="arr">→</span></a></div>
  </div>
</section>

<section class="section on-ink">
  <div class="wrap">
    <div class="split">
      <div class="sticky">
        <div class="chapter">AX</div>
        <div class="eyebrow rv">05 — AI Transformation</div>
        <h2 class="h-l rv d1">일은 기계에게,<br>판단은 사람에게.</h2>
        <p class="lead rv d2" style="margin-top:20px">우리 안에서 먼저 완성한 방식을 다른 회사 안에 세웁니다. 반복과 기다림은 기계가 맡고, 사람은 판단과 관계로 돌아갑니다.</p>
        <div class="rv d3" style="display:flex;gap:14px;flex-wrap:wrap;margin-top:8px"><a class="btn solid" href="ax.html">AX 컨설팅 <span class="arr">→</span></a><a class="btn" href="decisionmaker.html">디시전메이커</a></div>
      </div>
      <div class="grid grid-2">
        <div class="card rv"><div class="num">태버내클</div><h3>그림이 먼저, 검사를 못 넘으면 산출물이 아니다</h3><p>헌법 12조, 방 여덟, 사람이 들어오는 문 셋. 직원이 채팅방에서 이름을 부르면 30초 안에 개발이 시작되고, 새벽에는 감사 에이전트가 어제 만든 것을 사용자 관점으로 다시 써 봅니다.</p></div>
        <div class="card rv d1"><div class="num">디시전메이커</div><h3>운용업 자체를 AX했다</h3><p>접수·분류·심사·로드맵·투심위·서명. 20년의 투자 기준을 실측 가능한 규범으로 옮기고, 대표 한 사람이 여러 딜을 놓치지 않게 만든 한 회사·한 화면.</p></div>
        <div class="card rv d2"><div class="num">Engagements</div><h3>122개 지점 프랜차이즈 · 3개국 공장 · 미디어 딜룸</h3><p>세차 프랜차이즈 통합 플랫폼, 제조기업 생산 통합 관제, 텔레그램 릴레이 구축, 투자 유치 딜룸까지. 첫날의 산출물은 코드가 아니라 질문 목록입니다.</p></div>
        <div class="card rv d3"><div class="num">Principle</div><h3>준비는 기계가, 판단과 도장은 사람이</h3><p>기계 산출은 제안·할 일·[결정 필요]로만 사람에게 갑니다. 밖으로 나가는 것은 사람이 승인하고, 원본과 실명은 사무실 PC를 떠나지 않습니다.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section on-ivory">
  <div class="wrap">
    <div class="split" style="align-items:end;margin-bottom:40px">
      <div><div class="eyebrow rv">06 — Insights</div><h2 class="h-l rv d1">우리가 보는 네 개의 산업</h2></div>
      <p class="lead rv d2">에너지, 스페이스, 인공지능, 바이오. 2026년의 숫자를 출처와 함께 읽습니다.</p>
    </div>
    <div class="insight-grid">
      <a class="icard rv" href="insight-energy.html"><div class="num">01</div><div class="t">Energy</div><h3>전기를 구하는 쪽이 협상력을 잃는 시대</h3><p>데이터센터 전력수요 460→1,000 TWh. 발전원보다 계통·저장·수요지 인접성이 프리미엄을 받는다.</p><span class="more">읽기 →</span></a>
      <a class="icard rv d1" href="insight-space.html"><div class="num">02</div><div class="t">Space</div><h3>기술 자립에서 시장 자립으로</h3><p>우주청 예산 1조 1,201억, 뉴스페이스 펀드 81억→2,000억. 민간의 첫 계약이 어디서 나오는가.</p><span class="more">읽기 →</span></a>
      <a class="icard rv d2" href="insight-ai.html"><div class="num">03</div><div class="t">Artificial Intelligence</div><h3>에이전트가 일하는 회사와 발표만 한 회사</h3><p>기업 앱의 40%가 에이전트를 품는 해. 도입과 전환의 차이는 프로그램을 고칠 사람이 안에 있는가다.</p><span class="more">읽기 →</span></a>
      <a class="icard rv d3" href="insight-bio.html"><div class="num">04</div><div class="t">Bio</div><h3>신약보다 먼저 움직이는 것</h3><p>기술수출 8조→28조, GLP-1 연 20% 성장. 과학이 맞았을 때 돈이 흐르는 배관을 먼저 잡는다.</p><span class="more">읽기 →</span></a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:end;margin-bottom:40px">
      <div><div class="eyebrow rv">07 — People</div><h2 class="h-l rv d1">투자은행, 프라이빗 뱅킹,<br>리서치, 법률이 한 테이블에</h2></div>
      <p class="lead rv d2">국내외 금융권에서 20년 이상 쌓은 경력이 투자심의위원회에 모입니다.</p>
    </div>
    <div class="team-teaser">
      <a class="tcard rv" href="team.html#so"><div class="mono">BS</div><h3>소병운</h3><div class="role">부회장 · 파트너 · 투자심의위원</div></a>
      <a class="tcard rv d1" href="team.html#han"><div class="mono">HH</div><h3>한현철</h3><div class="role">대표이사 · 파트너 · 투자심의위원</div></a>
      <a class="tcard rv d2" href="team.html#lee"><div class="mono">TL</div><h3>이태경</h3><div class="role">대표이사 · 파트너 · 투자심의위원</div></a>
      <a class="tcard rv d3" href="team.html#jung"><div class="mono">SJ</div><h3>정상훈</h3><div class="role">글로벌대표 · 파트너</div></a>
    </div>
  </div>
</section>
"""

# ───────────────────────── philosophy ─────────────────────────
PHILOSOPHY = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><b>01</b> · Philosophy</div>
    <h1 class="h-xl rv">투자 철학</h1>
    <p class="lead rv d1">우리는 자본 활동에 의한 지속가능한 공동 가치를 창출하고자 합니다. 우리의 주요사업은 자본을 효율적으로 배치하는 것이며, 기업을 중심으로 이 일을 구상하고, 구현합니다.</p>
  </div>
</section>

<section class="section on-ivory">
  <div class="wrap">
    <div class="split">
      <div class="sticky">
        <div class="eyebrow rv">세 주체</div>
        <h2 class="h-l rv d1">고객, 임직원, 주주</h2>
        <div class="trio rv d2">
          <div><div class="t">Customers</div><div class="v">고객</div></div>
          <div><div class="t">Employees</div><div class="v">임직원</div></div>
          <div><div class="t">Shareholders</div><div class="v">주주</div></div>
        </div>
      </div>
      <div class="prose">
        <p class="rv">기업을 이루고 있는 세 주체는 고객, 임직원, 주주이며 각각은 경제적 이기심을 기본적으로 가지고 있습니다. 자신들을 제외한 나머지의 이익을 제한하고 자신들의 이익을 극대화 하려는 본능을 가지고 있는 것입니다.</p>
        <p class="rv d1">주주에 의한 임직원 정리해고, 회사가 고객을 교묘히 활용하는 것, 고객이 임직원에게 부당한 요구를 하는 것 등이 실제 사례들입니다. 쉽게 구현할 수 있지만 지속 가능하지 않은 경우가 많아 큰 가치가 만들어지지 않습니다.</p>
        <p class="rv d2">우리는 이 세 주체들이 동시에 이익과 가치가 늘어나는 방법을 항상 연구합니다. 가치 있는 일이며, 동작하기만 하면 크고 좋은 이익이 창출될 것이라 믿기 때문입니다. 가장 유효한 수단은 회사의 지배구조를 컨트롤하는 것이며, 잘 알려진 방법은 바이아웃 펀드를 운영하는 것입니다. 그래서 바이아웃 PEF가 우리들의 <strong>"업"</strong>이 된 것입니다.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="sticky">
        <div class="eyebrow rv">사명</div>
        <h2 class="h-l rv d1">중급일자리와<br>두 번째 기회</h2>
      </div>
      <div class="prose">
        <p class="pull rv">누구나 중위소득의 평생직장을 가질 수 있도록.</p>
        <p class="rv d1">특히, 임직원 부문의 일자리에 주목합니다. 우리는 <strong>"중급일자리"</strong>를 통해 누구나 중위소득의 평생직장을 가질 수 있도록 노력하고, <strong>second chance</strong>를 보장하는 역할을 하려고 합니다. 사회적으로 부여받은 우리의 사명으로 생각하고 있습니다.</p>
        <p class="rv d2">저희를 믿고 투자자금을 맡겨 주신 투자자와 주주들께 다른 이의 희생에 기반하지 않은, 정당하고 가치 있는 수익을 창출하는 것이 우리의 목표입니다. 이렇게 구현되는 휴머니즘을 <strong>"자본에 의한 휴머니즘"</strong>이라 명명하고, 우리의 철학이자 사업의 근간으로 삼았습니다. 아르투스의 임직원은 이 일을 하기 위해 모여서 노력하고 있습니다.</p>
      </div>
    </div>
  </div>
</section>
"""

# ───────────────────────── values ─────────────────────────
VALUES = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><b>02</b> · Core values</div>
    <h1 class="h-xl rv">핵심 가치</h1>
    <p class="lead rv d1">ARTUS라는 이름의 다섯 글자는 우리가 일하는 방식입니다. 모든 투자 결정과 운용 과정에서 이 순서대로 스스로에게 묻습니다.</p>
  </div>
</section>
<section class="section on-ivory">
  <div class="wrap">
    <div class="vrow rv"><div class="big">A</div><div><h3>책임<span>Accountability</span></h3><ul><li>고객 자산에 대한 책임감과 수탁자 의무를 다합니다.</li><li>모든 투자 결정과 프로세스에 명확한 책임소재를 둡니다.</li></ul></div></div>
    <div class="vrow rv"><div class="big">R</div><div><h3>정직<span>Righteousness</span></h3><ul><li>투명하고 정직한 운용 원칙을 지킵니다.</li><li>윤리적이고 올바른 자산운용을 실천합니다.</li></ul></div></div>
    <div class="vrow rv"><div class="big">T</div><div><h3>신뢰<span>Trust</span></h3><ul><li>정직하고 투명한 운용으로 신뢰관계를 구축합니다.</li><li>안정적이고 지속가능한 성과로 신뢰를 입증합니다.</li></ul></div></div>
    <div class="vrow rv"><div class="big">U</div><div><h3>이해<span>Understanding</span></h3><ul><li>고객의 투자 목표와 니즈를 깊이 이해합니다.</li><li>시장 상황과 리스크 요인을 정확히 파악합니다.</li></ul></div></div>
    <div class="vrow rv"><div class="big">S</div><div><h3>전문성<span>Specialty</span></h3><ul><li>차별화된 투자 전략과 운용 역량을 보유합니다.</li><li>지속적인 연구와 혁신으로 전문성을 강화합니다.</li></ul></div></div>
  </div>
</section>
"""

# ───────────────────────── services ─────────────────────────
def svc(id_, idx, title, desc, steps, open_=False):
    parts = []
    for n, (h, items) in enumerate(steps, 1):
        lis = "".join(f"<li>{i}</li>" for i in items)
        parts.append(f'<div class="step"><h4><i>{n:02d}</i>{h}</h4><ul>{lis}</ul></div>')
    return f"""    <details class="svc rv" id="{id_}"{' open' if open_ else ''}>
      <summary><span class="idx">{idx}</span><div><h3>{title}</h3><div class="desc">{desc}</div></div><span class="plus" aria-hidden="true"></span></summary>
      <div class="body">{''.join(parts)}</div>
    </details>
"""

SERVICES = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><b>03</b> · Services</div>
    <h1 class="h-xl rv">업무 분야</h1>
    <p class="lead rv d1">인수와 투자, 자금 조달, 승계. 네 가지 업무는 서로 다른 일처럼 보이지만, 모두 "자본을 기업 중심으로 효율적으로 배치한다"는 하나의 원칙에서 나옵니다.</p>
  </div>
</section>
<section class="section on-ivory">
  <div class="wrap">
""" + svc("ma", "01", "기업인수합병(M&amp;A)", "가치 분석부터 인수 후 통합까지, 한 팀이 끝까지 맡습니다.", [
    ("대상 기업 가치 분석 및 적정 인수가격 산정", [
        "<b>재무분석</b>: 최소 3~5년간의 손익계산서, 재무상태표, 현금흐름표를 검토해 매출 추이, 부채 비율, 영업이익률 등을 종합적으로 평가",
        "<b>시장환경 조사</b>: 산업 동향, 경쟁사 비교, 규제 및 기술 트렌드를 고려해 성장 가능성을 예측",
        "기업 가치평가 모델(DCF, EV/EBITDA, PER 등)을 활용하여 적정 인수가격 범위를 설정"]),
    ("실사(Due Diligence) 수행", [
        "<b>재무 실사</b>: 과거 재무제표 신뢰성, 숨겨진 부채, 운전자본 흐름 등을 면밀히 점검",
        "<b>법률 실사</b>: 지적재산권, 계약관계, 소송 이력, 컴플라이언스 준수 여부 등을 검토",
        "<b>세무 실사</b>: 세금 납부 이력, 결손금 이월, 추징 가능성 등을 파악",
        "<b>인력·조직 실사</b>: 핵심 인력 역량, 노사관계 안정성 등을 확인"]),
    ("거래구조 설계 및 협상", [
        "<b>거래 구조</b>: Stock Deal(주식인수) vs. Asset Deal(사업부 인수) 등 다양한 방식을 검토",
        "<b>계약서 작성</b>: 주식매매계약(SPA), 진술·보장(Representations &amp; Warranties), 손해배상(Indemnification) 조항 등을 협의",
        "<b>협상 전략</b>: 인수가격, 지급 조건, 에스크로·언아웃 등의 활용으로 위험 분산"]),
    ("인수 후 통합(PMI)", [
        "<b>조직·문화 통합</b>: 양사 조직구조 재정비, 핵심 인력 유출 방지, 보상체계 조정",
        "<b>시너지 극대화</b>: 중복 부서 통합, 제품·서비스 라인 교차판매, 추가 수익원 발굴",
        "<b>가치 제고 전략</b>: 재무구조 개선, 신사업 발굴, 해외시장 진출, 추가 투자 유치 등"]),
], open_=True) + svc("equity", "02", "지분투자", "성장 잠재력 있는 기업을 발굴하고, 경영에 참여해 가치를 높인 뒤 회수합니다.", [
    ("성장 잠재력 있는 기업 발굴 및 지분 인수", [
        "<b>투자 대상 선정</b>: 시장규모, 기술력, 경영진 역량, 경쟁우위 등을 종합 평가",
        "<b>투자 구조 설계</b>: 보통주, 우선주, 전환사채(CB), 신주인수권부사채(BW) 등 다양한 방식 검토"]),
    ("경영 참여 및 기업가치 제고", [
        "<b>이사회 참여</b>: 주요 경영 의사결정에 대한 직접적인 영향력 행사",
        "<b>재무구조 개선</b>: 추가 자금 조달, 비효율 자산 정리 등으로 재무 안정성 제고",
        "<b>사업전략 수립</b>: 신사업 개발, 해외시장 진출, M&amp;A 연계를 통한 규모 확장 등"]),
    ("투자금 회수(Exit) 전략", [
        "<b>IPO</b>: 상장 준비(내부통제, 지배구조 투명성), 수요예측(Book Building)을 통한 공모가 산정",
        "<b>전략적 매각(Trade Sale)</b>: 경쟁사·협력사 등에 지분 매각으로 프리미엄 창출",
        "<b>메자닌 회수</b>: 전환사채, 신주인수권부사채의 권리 행사 또는 원금·이자 상환을 통한 투자 회수"]),
]) + svc("syndication", "03", "신디케이션", "복수 금융기관과 함께 대규모 자금을 조달하고, 주간사로서 대주단을 운영합니다.", [
    ("복수 금융기관 대상 대규모 자금 조달", [
        "<b>자금 수요 분석</b>: 프로젝트 성격(인프라, 부동산 개발, 인수금융 등)에 따라 재무 모델링",
        "<b>참여기관 모집</b>: 은행, 증권사, 보험사 등 유관 금융기관에 투자안을 제시하고 참여 의향 타진"]),
    ("주간사로서 조건 설계 및 협상", [
        "<b>대출 조건 수립</b>: 금리(고정·변동), 만기, 담보·보증 구조, 상환 스케줄 결정",
        "<b>리스크 분산</b>: 대출액 분산, 손실 발생 시 책임 분담 구조 합의",
        "<b>PF, 인수금융 등 특화 구조 설계</b>: 비소구(Non-Recourse) 구조, 레버리지 활용 등"]),
    ("대주단 구성 및 사후 관리", [
        "<b>대출약정 체결</b>: 참여기관 간 약정서 작성, 대출 실행 프로세스 완료",
        "<b>사후 모니터링</b>: 채무자(프로젝트) 실적·현금흐름 보고, 필요 시 조건 변경·리파이낸싱 검토",
        "<b>대주단 운영</b>: 추가 대출이나 채무 불이행 시 담보 실행, 자산 매각 등 공동 대응"]),
]) + svc("succession", "04", "상속·증여 설계", "기업 오너 지분의 승계를 세무·법률 전문가와 함께 설계하고, 납부 자금까지 계획합니다.", [
    ("기업 오너 지분 상속·증여 방안 수립", [
        "<b>사전 조사</b>: 가족 지배구조, 기업 가치평가, 보유 지분 현황 등을 종합 분석",
        "<b>증여 vs. 상속</b>: 세금 부담, 경영권 공백, 기업 성장 과실 등 비교 검토"]),
    ("세무·법률 전문가와 협업", [
        "<b>조세 효율적 구조</b>: 지주회사 설립, 가업상속 공제 등 절세 방안 활용",
        "<b>법률 자문</b>: 주주간 계약, 유언·신탁, 상속·증여세 신고 등 법적 분쟁 예방"]),
    ("가업승계와 연계한 지배구조 개선", [
        "<b>후계자 선정</b>: 핵심 후계자의 역량, 경영 철학, 조직 융화 능력 등을 고려",
        "<b>사업 포트폴리오 조정</b>: 비핵심 사업 정리, 신성장 동력 확보 등으로 기업 경쟁력 강화"]),
    ("상속·증여세 납부 자금조달 방안 마련", [
        "<b>자금 마련 전략</b>: 배당, 자산 매각, 사채 발행 등 다양한 방식 검토",
        "<b>스케줄 관리</b>: 과세 시점, 연부연납, 세액 공제 등을 고려한 적시 납부 계획 수립"]),
]) + """  </div>
</section>
"""

# ───────────────────────── achievements ─────────────────────────
def deal(fund, name, irr, moic, lbl, text, cls=""):
    return f"""      <div class="deal rv {cls}"><div><div class="fund">{fund}</div><h3>{name}</h3><p>{text}</p></div><div class="kpi"><div class="n">{irr}</div><div class="x">{moic}</div><div class="lbl">{lbl}</div></div></div>
"""

ACHIEVEMENTS = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><b>04</b> · Track record</div>
    <h1 class="h-xl rv">주요 성과</h1>
    <p class="lead rv d1">네 개의 펀드, 네 가지 다른 상황. 높은 수익률을 낸 딜과 위기를 손실 없이 넘긴 딜을 함께 기록합니다. 어느 쪽이든 투자자에게 약속한 것을 지켰다는 점은 같습니다.</p>
  </div>
</section>
<section class="section on-ivory">
  <div class="wrap">
    <div class="grid grid-2" style="grid-template-columns:1fr">
""" + deal("스트라이커 스카이 제1호", "만나코퍼레이션", '59<small>%</small>', "2.52x", "IRR · MOIC",
  "딜리버리 히어로, 배달의 민족 등은 전 세계에서 오토바이 라이더를 고용합니다. 한국에서도 배달 대행이 필수 유틸리티가 될 것은 자명해 보였습니다. 상위 5개 기업 중 성장률이 가장 높고 CEO의 전문성이 높은 업체를 찾아냈습니다. 이 회사는 2년 만에 5위에서 2위로 올라섰습니다. 결과적으로 이 사업에 진출하고자 하는 전략적 투자자에게 exit을 할 수 있었습니다. 연환산 수익률은 59%로 모든 투자 사례 중 가장 높았고, 원금 대비 투자 수익 배수는 2.52배에 달했습니다.") \
  + deal("스트라이커 파밍 제1호", "에이치앤비아시아", '39<small>%</small>', "2.32x", "IRR · MOIC",
  "스트라이커 PEF는 2019년에 에이치앤비아시아의 최대 주주가 되었습니다. 창업자이자 2대 주주의 MBO를 시현하는 구조화딜이었습니다. 당도 높은 사과 '엔비'의 아시아 독점 판권을 보유하고 있으며, 다양한 해외 과일을 수입해 국내에 유통하고 있습니다. 한국에서 사과는 쌀 다음으로 수입량이 많은 작물인데, 이 시스템을 통해 수년간 안정적인 수익을 낼 수 있다는 점에 주목했습니다. 2대 주주에게 약속한 경영권을 넘겨주고 약정한 수익을 실현했습니다. 연환산 수익률은 39%, 원금 대비 수익률은 원금의 2.32배에 달했습니다.", "d1") \
  + deal("스트라이커 모르가르텐 제1호", "마제스티 골프 코리아", '9<small>%</small>', "1.09x", "IRR · MOIC",
  "마제스티골프코리아는 하이엔드 골프 장비 제조업체입니다. 오케스트라 PE의 세컨더리 딜로, 당사가 해외 기업을 인수한 첫 사례였습니다. 골프 산업, 특히 하이엔드 시장의 높은 성장성에 주목해 투자했습니다. 스마트스코어, SGPE와 컨소시엄을 구성해 투자했습니다. 연 수익률 9%, 투자 원금 대비 1.09배의 수익률을 기록했습니다.", "d2") \
  + deal("스트라이커 아레나 제1호", "아프리카 오픈스튜디오", "0", "손실 없음", "Downside protected",
  "한국의 게임 산업은 세계에서 가장 열정적인 산업 중 하나입니다. 40대 중반의 나이에도 집과 PC방에서 게임을 즐기는 사람들이 많습니다. e스포츠는 항저우 아시안게임에서 정식 종목으로 채택되었고, 올림픽에서도 종목 채택 가능성이 거론되고 있습니다. 한국의 게임, 음악 등 스트리밍 업체인 아프리카는 이러한 수요에 대응하기 위해 PC방 업계에 진출하기로 결정하였고, 스트라이커는 FI로 참여를 하였습니다. 시작은 좋았지만 팬데믹이 닥치면서 PC방은 몇 년 동안 문을 닫아야 했습니다. 다행히 풋옵션을 활용해 손실 없이 투자를 마무리할 수 있었습니다. 위험관리를 잘 한 사례입니다.", "d3") + """    </div>
    <p class="muted rv" style="margin-top:28px;font-size:.88rem">IRR은 연환산 수익률, MOIC는 투자 원금 대비 회수 배수입니다. 과거의 성과가 미래의 수익을 보장하지 않습니다.</p>
  </div>
</section>
"""

# ───────────────────────── team ─────────────────────────
def person(id_, ini, name, role, paras):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f"""    <article class="person rv" id="{id_}"><div class="mono">{ini}</div><div><h3>{name}</h3><div class="role">{role}</div>{ps}</div></article>
"""

TEAM = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><b>05</b> · People</div>
    <h1 class="h-xl rv">구성원</h1>
    <p class="lead rv d1">투자은행, 프라이빗 뱅킹, 리서치, 법률. 서로 다른 자리에서 20년 이상 일해 온 네 사람이 투자심의위원회에 모입니다.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
""" + person("so", "BS", "소병운", "부회장 · 파트너 · 투자심의위원", [
  "소병운 부회장은 서울대학교 경제학과를 졸업하고 미국 보스턴 아서디리틀 연수와 미시간대학교 MBA 과정을 마친 뒤, 하나은행 투자은행그룹 본부장과 하나IB증권 투자은행본부 전무 등을 거치며 국내 금융권에서 20년 이상 활약한 투자은행(IB)·M&amp;A 전문가입니다.",
  "현대증권에서는 2013년부터 2015년까지 투자은행부문 대표를 맡아 대형 프로젝트 투자와 사모펀드 운영을 주도했고, 이후 2016년부터 2019년까지 SVN Korea 대표이사로 재직하며 부동산 투자금융 자문 분야에서 역량을 발휘했습니다. 2020년부터는 스트라이커 캐피탈 매니지먼트 부회장으로서 기업금융 자문과 신규 투자처 발굴, 펀드 운영 등을 총괄하고 있으며, 에이팩트 이사회에서 3년 임기로 재선임되어 거버넌스 체계 확립과 전략적 의사결정 과정에 참여하고 있습니다."]) \
+ person("han", "HH", "한현철", "대표이사 · 파트너 · 투자심의위원", [
  "한현철 대표는 한국 금융투자업계를 대표하는 프라이빗 뱅커로, 20여 년간 다수의 주요 증권사에서 탁월한 경력을 쌓아 명성을 확립하였습니다. 고려대학교 경영학과를 졸업한 그는 미래에셋증권(구 대우증권) 재직 당시 최연소 지점장에 발탁되며 주목받기 시작했습니다. 이후 NH투자증권에서 프리미어블루 대치센터장을, 메리츠증권에서는 도곡금융센터장을 역임하며, 고객 중심의 혁신적인 금융 솔루션을 제시해 왔습니다.",
  "최근에는 다올투자증권 리테일금융센터 PIB전무로 재직하며, 리테일 금융 분야에서도 새로운 기준을 제시하고 업계의 변화를 선도했습니다. 한 대표는 탁월한 리더십과 금융 투자에 대한 깊은 통찰력을 바탕으로, 고객의 자산 관리와 투자 목표 실현에 기여하며 한국 금융업계의 중요한 인물로 자리매김하고 있습니다."]) \
+ person("lee", "TL", "이태경", "대표이사 · 파트너 · 투자심의위원", [
  "이태경 대표는 Striker Capital Management의 창업자이자 대표로, 금융 업계에서 폭넓은 경력과 전문성을 바탕으로 탁월한 성과를 이루어 왔습니다. 서울대학교 경영학과를 졸업한 그는 키움증권에서 보험 산업 애널리스트로 커리어를 시작하며 업계에서 두각을 나타냈습니다. 이후 현대증권으로 자리를 옮겨 금융 및 스몰캡 애널리스트로 활동하며 날카로운 분석력과 통찰력을 인정받았습니다.",
  "마이다스에셋자산운용에서는 PEF 부문을 이끌며 국내외 투자 프로젝트를 성공적으로 수행하며 리더십을 발휘했습니다. 또한, 국내 인사 컨설팅 회사에서 컨설턴트로 활동하며 경영 전략 및 조직 관리에 대한 다각적인 경험을 쌓아 기업 운영과 투자 활동에 새로운 시각을 더했습니다.",
  "그의 업적은 국내를 넘어 글로벌 금융계에서도 인정받아 월스트리트 선정 아시아 베스트 애널리스트로 선정되는 영예를 안았습니다. 이러한 전문성과 경험을 바탕으로 그는 Striker Capital Management를 설립, 금융과 투자, 컨설팅을 융합한 혁신적인 비즈니스 모델을 통해 업계를 선도하며 새로운 기준을 제시하고 있습니다."]) \
+ person("jung", "SJ", "정상훈", "글로벌대표 · 파트너", [
  "정상훈 대표는 변호사로 한국과 중국 변호사 자격을 모두 보유하고 있습니다. 현재 법무법인 율촌의 중국대표를 겸임하고 있습니다. 한샘의 중국 대표를 역임했습니다. 중국 로펌인 링크와 킹앤우드에서 근무했습니다. 미래에셋캐피탈 투자본부와 국내 로펌인 법무법인 서정에서 근무했습니다. 서울대학교 법대를 졸업하였습니다."]) + """  </div>
</section>
"""

# ───────────────────────── contact ─────────────────────────
CONTACT = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><b>06</b> · Contact</div>
    <h1 class="h-xl rv">문의하기</h1>
    <p class="lead rv d1">투자 제안, 인수·매각, 자금 조달, 승계 설계. 어떤 단계든 편하게 연락 주십시오. 영업일 기준 하루 안에 답을 드립니다.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="contact-grid">
      <div class="cbox rv"><div class="t">Email</div><div class="v"><a href="mailto:contact@artus.kr">contact@artus.kr</a></div><div class="s">투자 제안서와 자료는 이메일로 보내 주십시오.</div></div>
      <div class="cbox rv d1"><div class="t">Phone · Fax</div><div class="v"><a href="tel:027612025">02-761-2025</a></div><div class="s">Fax 02-761-2035 · 평일 09:00–18:00</div></div>
      <div class="cbox rv d2"><div class="t">Office</div><div class="v">서울시 영등포구 여의나루로 53-1<br>대오빌딩 14층</div><div class="s"><a href="https://map.naver.com/p/search/%EC%97%AC%EC%9D%98%EB%82%98%EB%A3%A8%EB%A1%9C%2053-1" target="_blank" rel="noopener">네이버 지도에서 보기 →</a></div></div>
      <div class="cbox rv d3"><div class="t">Company</div><div class="v">주식회사 아르투스<br><span class="latin" style="font-size:1rem;letter-spacing:.14em">ARTUS Private Equity Partners</span></div><div class="s">여의도, 서울</div></div>
    </div>
  </div>
</section>
"""

NOTFOUND = """
<section class="page-hero" style="min-height:70vh;display:flex;align-items:center">
  <div class="wrap">
    <div class="crumb"><b>404</b> · Not found</div>
    <h1 class="h-xl">찾으시는 페이지가 없습니다</h1>
    <p class="lead" style="margin-top:20px">주소가 바뀌었거나 삭제된 페이지입니다.</p>
    <a class="btn solid" href="index.html" style="margin-top:30px">홈으로 <span class="arr">→</span></a>
  </div>
</section>
"""

DEAL_COUNT = "열 몇 개의"
DEAL_SOURCE = ""
DESC = "Intelligence Meets Capital. ARTUS(주식회사 아르투스)는 AI로 사람을 사람의 일로 돌려보내고 그 변화에 자본을 더하는 프라이빗 에쿼티 파트너입니다. AX 컨설팅, 기업인수합병, 지분투자, 신디케이션."

page("index.html", "ARTUS — Intelligence Meets Capital", DESC, INDEX)
page("philosophy.html", "투자 철학 — 사람을 사람의 일로 돌려보냅니다 · ARTUS", "한 사람이 열 몇 개의 딜을 손실 없이 굴리는 방식을 밖으로 옮깁니다. 자본과 AI에 의한 휴머니즘. 우리가 바꾸는 회사와 우리가 지켜보는 산업.", PHILOSOPHY_NEW.replace("[DEAL_COUNT]", DEAL_COUNT).replace("[DEAL_SOURCE]", DEAL_SOURCE))
page("values.html", "핵심 가치 — ARTUS", "Accountability, Righteousness, Trust, Understanding, Specialty. 원래의 뜻 위에 AI 시대의 뜻을 한 겹 더 입힌 다섯 가지 핵심 가치.", VALUES_INTRO)
page("services.html", "업무 분야 — ARTUS", "기업인수합병(M&A), 지분투자, 신디케이션, 상속·증여 설계. 아르투스의 네 가지 업무 분야와 수행 절차.", SERVICES)
page("achievements.html", "주요 성과 — ARTUS", "만나코퍼레이션 IRR 59%, 에이치앤비아시아 IRR 39% 등 스트라이커 PEF의 투자 성과와 위험관리 사례.", ACHIEVEMENTS)
page("team.html", "구성원 — ARTUS", "소병운 부회장, 한현철 대표, 이태경 대표, 정상훈 글로벌대표. 투자은행·프라이빗 뱅킹·리서치·법률 전문가로 구성된 아르투스의 파트너.", TEAM)
page("contact.html", "문의하기 — ARTUS", "ARTUS 연락처. 서울 영등포구 여의나루로 53-1 대오빌딩 14층, 02-761-2025, contact@artus.kr", CONTACT)
page("ax.html", "AX 컨설팅 — 회사 전체를 수시간 안에 AX합니다 · ARTUS", "코딩을 모르는 구성원 전원이 자기 말로 회사의 프로그램을 짓고 고치는 체계, 태버내클. 세차 프랜차이즈 122개 지점 플랫폼, 3개국 공장 통합 관제, 텔레그램 AI 릴레이 구축 사례.", AX)
page("decisionmaker.html", "디시전메이커 — 운용업 자체를 AX했습니다 · ARTUS", "투자 의사결정의 준비를 완성하는 기계. 접수·분류·심사·로드맵·투심위·서명을 한 회사·한 화면으로. 판단과 도장은 사람이 합니다.", DECISIONMAKER)
page("insights.html", "인사이트 — 우리가 보는 네 개의 산업 · ARTUS", "에너지, 스페이스, 인공지능, 바이오. 2026년의 숫자를 출처와 함께 읽고 아르투스가 보는 투자 지점을 적었습니다.", HUB)
page("insight-energy.html", "에너지 — 전기를 구하는 쪽이 협상력을 잃는 시대 · ARTUS Insight", "데이터센터 전력수요 460→1,000 TWh, SMR 특별법, 해상풍력과 계통 병목. 2026년 에너지 투자 지점.", ENERGY)
page("insight-space.html", "스페이스 — 기술 자립에서 시장 자립으로 · ARTUS Insight", "우주항공청 2026 예산 1조 1,201억, 뉴스페이스 펀드 2,000억. 한국 우주산업의 시장 자립과 투자 지점.", SPACE)
page("insight-ai.html", "인공지능 — 에이전트가 일하는 회사와 발표만 한 회사 · ARTUS Insight", "2026년 기업 앱의 40%가 AI 에이전트를 통합. 도입과 전환의 차이, 그리고 투자 지점.", AI)
page("insight-bio.html", "바이오 — 신약보다 먼저 움직이는 것 · ARTUS Insight", "GLP-1 연 20% 성장, 기술수출 8조→28조, ADC와 뉴모달리티. 2026년 바이오 투자 지점.", BIO)
page("404.html", "페이지를 찾을 수 없습니다 — ARTUS", DESC, NOTFOUND)

# sitemap / robots
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for fn, _ in NAV + FOOT_EXTRA + [("contact.html", ""), ("insight-energy.html", ""), ("insight-space.html", ""), ("insight-ai.html", ""), ("insight-bio.html", "")]:
        loc = SITE + "/" if fn == "index.html" else f"{SITE}/{fn}"
        f.write(f"  <url><loc>{loc}</loc></url>\n")
    f.write("</urlset>\n")
with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("sitemap.xml, robots.txt")
