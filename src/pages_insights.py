# -*- coding: utf-8 -*-
"""산업 인사이트 4편 — 에너지 · 스페이스 · 인공지능 · 바이오.
수치는 각 편 하단 출처에 근거한다(헌법 12). 조사일 2026-09-11."""

def article(slug, num, tag, title, lead, kpis, body, sources, prev, nxt):
    k = "".join(f'<div class="kpi"><span>{a}</span><b>{b}</b></div>' for a, b in kpis)
    s = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in sources)
    return f"""
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><b>Insight {num}</b> · {tag}</div>
    <h1 class="h-xl rv">{title}</h1>
    <p class="lead rv d1">{lead}</p>
  </div>
</section>
<section class="section on-ivory">
  <div class="wrap">
    <div class="article">
      <div class="body rv">{body}
        <div class="sources"><h4>Sources</h4><ol>{s}</ol>
        <p class="disclaimer">조사 시점 2026년 9월. 인용 수치는 각 출처의 원문을 따르며, 아르투스의 해석은 투자 권유가 아닙니다.</p></div>
        <div class="next-prev"><a class="btn" href="{prev[0]}">← {prev[1]}</a><a class="btn" href="{nxt[0]}">{nxt[1]} →</a></div>
      </div>
      <aside class="aside rv d1">
        <div class="box"><div class="t">At a glance</div>{k}</div>
        <div class="box"><div class="t">ARTUS view</div><p style="margin:0;font-size:.95rem;color:var(--mist-2)">{{view}}</p></div>
      </aside>
    </div>
  </div>
</section>
"""

ENERGY_VIEW = "전력은 더 이상 유틸리티가 아니라 병목 자산입니다. 우리는 발전원보다 계통·저장·수요지 인접성에 프리미엄이 붙는 자산을 봅니다."
ENERGY = article("insight-energy", "01", "Energy",
  "전기를 구하는 쪽이<br>협상력을 잃는 시대",
  "AI 데이터센터가 전력을 빨아들이면서, 에너지 투자의 질문은 \"무엇으로 발전하는가\"에서 \"어디에, 언제, 얼마나 확실하게 공급되는가\"로 옮겨 갔습니다.",
  [("데이터센터·AI 전력수요 (IEA)", "460→1,000 TWh"), ("기준 연도", "2022→2026"), ("SMR 특별법 통과", "2026.02"), ("i-SMR 표준설계인가 목표", "2028")],
  """<p>국제에너지기구는 데이터센터와 인공지능이 쓰는 전력이 2022년 460테라와트시에서 2026년 최대 1,000테라와트시까지 늘어날 수 있다고 봅니다. 4년 만에 두 배가 넘는 수요가 한 산업에서 생기는 일은 드뭅니다. 문제는 발전소를 짓는 속도가 아니라 <strong>송전선과 계통</strong>입니다. 국내에서는 수도권 전력망이 포화되어 데이터센터의 전력 신청이 거부되는 사례가 이미 나왔습니다.</p>
  <h2>원전과 SMR: 빅테크가 먼저 움직였다</h2>
  <p>마이크로소프트, 아마존, 메타는 탄소 배출 없이 24시간 공급되는 전력원으로 원자력과 소형모듈원자로(SMR)에 눈을 돌렸습니다. 국내에서는 2026년 2월 SMR 특별법이 통과되었고, 한국형 i-SMR(170MWe)은 2028년 표준설계인가를 목표로 합니다. 다만 실제 상용 발전은 2030년대 초반 이후라는 점을 잊으면 안 됩니다. 단기(2026~2028)에는 LNG 연료전지와 가스터빈이 현실적 대안이고, 중기(2028~2032)에는 재생에너지와 ESS 조합이 중심이 됩니다.</p>
  <h2>재생에너지: 해상풍력과 저장</h2>
  <p>유럽을 중심으로 부유식 해상풍력 상업 단지가 2026년 가속되고, 국내 서남해안과 울산 동해안도 대규모 프로젝트가 추진됩니다. 그러나 발전량이 늘수록 계통 수용성이 병목이 되고, 그래서 저장장치와 송전 인프라가 발전소보다 먼저 가격을 받는 국면이 옵니다.</p>
  <h2>우리가 보는 투자 지점</h2>
  <p>첫째, <strong>수요지에 인접한 확정 전력</strong>을 가진 부지와 사업권. 둘째, 계통 병목을 푸는 저장·변전·송전 인프라와 그 시공 역량. 셋째, SMR 상용화 전까지 공백을 메우는 가스 기반 분산전원. 발전원 자체의 기술 우위보다 "전기를 확실히 받을 수 있는 권리"가 프리미엄을 받는다는 것이 2026년 에너지 시장의 핵심 변화입니다.</p>""",
  [("투데이에너지 — 2026년 에너지 전망② SMR과 신재생에너지의 상생시대", "https://www.todayenergy.kr/news/articleView.html?idxno=293118"),
   ("삼일PwC — 국내외 에너지 및 전력 인프라 투자기회 모색 (2026.03)", "https://www.pwc.com/kr/ko/event/event-presentation/event_260318_3-1.pdf"),
   ("한국데이터경제신문 — 12차 전기본 데이터센터 전력수요 시나리오 2026~2030", "https://www.dataeconomy.co.kr/news/articleView.html?idxno=40190"),
   ("에너지안전신문 — SMR 및 첨단 원자로 2026", "https://www.esnews.kr/news/articleView.html?idxno=3704")],
  ("insights.html", "인사이트"), ("insight-space.html", "스페이스")).replace("{view}", ENERGY_VIEW)

SPACE_VIEW = "발사체·위성의 기술 자립은 끝났고, 다음은 매출 자립입니다. 정부 펀드가 25배로 커지는 해에 민간 서비스 회사의 첫 계약이 어디서 나오는지를 봅니다."
SPACE = article("insight-space", "02", "Space",
  "기술 자립에서<br>시장 자립으로",
  "2026년은 한국 우주산업이 \"만들 수 있는가\"에서 \"팔 수 있는가\"로 질문을 바꾼 해입니다. 정부 예산의 무게중심이 기술 확보에서 민간 생태계 조성으로 옮겨 갔습니다.",
  [("우주항공청 2026 예산", "1조 1,201억"), ("R&D 투자 (53개 사업)", "9,495억"), ("뉴스페이스 펀드", "81억→2,000억"), ("누리호 고도화 / 차세대 발사체", "1,253 / 1,204억")],
  """<p>우주항공청은 2026년 53개 세부사업에 9,495억원을 투자하는 연구개발 종합시행계획을 확정했고, 청 전체 예산은 1조 1,201억원입니다. 핵심은 누리호 고도화(1,253억)와 차세대 발사체 개발(1,204억)입니다. 숫자만 보면 기술 개발 예산이지만, 방향은 다릅니다. 정부는 우주정책의 무게중심을 <strong>기술 확보에서 민간 주도 생태계 조성</strong>으로 옮기고 있다고 명시했습니다.</p>
  <h2>25배로 커지는 펀드</h2>
  <p>뉴스페이스 투자 펀드는 2025년 81억원에서 2026년 2,000억원 규모로 확대됩니다. 정부가 1,000억원을 출자하고 민간과 해외 투자자 자금을 매칭하는 구조입니다. 발사체와 위성 개발 역량은 확보했지만 그것이 민간의 매출과 서비스로 이어지는 시장 자립은 아직 본격화되지 않았다는 진단이 이 펀드의 배경입니다.</p>
  <h2>발사체는 인프라다</h2>
  <p>증권가 산업분석은 우주발사체를 "우주산업의 필수 인프라"로 규정합니다. 발사 능력을 가진 기업은 위성·서비스 기업들의 공급망 상류에 서게 되고, 방위산업과의 접점도 큽니다. 국회도서관 국가전략포털은 우주항공산업 데이터를 별도로 묶어 국가전략 과제로 다루고 있습니다.</p>
  <h2>우리가 보는 투자 지점</h2>
  <p>첫째, 발사 서비스와 위성 부품에서 <strong>정부 과제 매출을 민간 계약으로 전환</strong>하는 첫 사례를 만드는 기업. 둘째, 위성 데이터를 농업·해양·보험 같은 지상 산업에 파는 서비스 계층. 셋째, 2,000억 펀드의 매칭 구조에 올라탈 수 있는 중간 규모 딜. 우주는 아직 기관투자자 대부분에게 낯선 자산이라, 실사 체계를 먼저 갖춘 쪽이 가격을 정합니다.</p>""",
  [("우주항공청 — 2026년 우주항공청 업무계획", "https://www.kasa.go.kr/bbs/BBSMSTR_000000000010/view.do?nttId=B000000002579Ec2zP0"),
   ("아이뉴스24(다음) — K-스페이스로 달리는 2026, 우주청 9495억 R&D 투자", "https://v.daum.net/v/20260104120206499"),
   ("뉴스페이스 코리아 — 기술 자립 넘어 시장 자립으로, 2026년은 우주산업 대전환 원년", "https://v.daum.net/v/20260420055802926"),
   ("하나증권 — 우주 관점에서 본 한화에어로스페이스 (2026.01)", "https://www.hanaw.com/download/research/FileServer/WEB/industry/industry/2026/01/05/Defense_260106_1.pdf"),
   ("국회도서관 국가전략포털 — 데이터로 보는 우주항공산업", "https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000048129")],
  ("insight-energy.html", "에너지"), ("insight-ai.html", "인공지능")).replace("{view}", SPACE_VIEW)

AI_VIEW = "우리는 AI를 투자 대상이기 전에 도구로 씁니다. 운용업을 스스로 AX한 경험이 있기에, 어떤 회사가 진짜로 바뀌고 어떤 회사가 도입 발표만 하는지 구분합니다."
AI = article("insight-ai", "03", "Artificial Intelligence",
  "에이전트가 일하는 회사와<br>발표만 한 회사",
  "생성형 AI가 글을 써 주던 시기는 끝났습니다. 2026년의 분기점은 에이전트가 업무를 끝까지 수행하느냐이고, 그 차이는 생산성 숫자로 벌어지고 있습니다.",
  [("에이전트 통합 기업 앱 (Gartner, 2026)", "40%"), ("2025년 기준", "<5%"), ("AI 자동화 생산성 향상 (OECD)", "15~40%"), ("한국 AI 특허, 10만 명당", "14.31건 · 세계 1위")],
  """<p>가트너는 2026년까지 전체 기업 애플리케이션의 40%가 작업 특화 AI 에이전트를 통합할 것으로 예측합니다. 2025년에 5% 미만이었으니 한 해 만에 여덟 배입니다. 한 글로벌 컨설팅사는 생성형 AI로 개발자 생산성이 30% 올랐지만, 에이전틱 AI 도입 뒤에는 200% 올랐다고 보고했습니다. OECD는 AI 자동화를 도입한 기업의 생산성이 평균 15~40% 향상됐다고 집계합니다.</p>
  <h2>한국: 혁신 밀도는 1위, 플랫폼은 과제</h2>
  <p>한국은 인구 10만 명당 AI 특허 건수 14.31건으로 세계 1위입니다. 기술 밀도는 검증됐습니다. 그러나 투자 규모와 플랫폼 경쟁력은 여전히 과제로 지적됩니다. 기업 설문에서는 생성형 AI와 AI 에이전트에 투자하겠다는 응답이 77.7%에 이릅니다. 돈은 들어가는데, 무엇이 바뀌는지는 회사마다 다릅니다.</p>
  <h2>도입과 전환의 차이</h2>
  <p>우리가 직접 겪은 기준은 하나입니다. <strong>프로그램을 고칠 수 있는 사람이 회사 안에 있는가.</strong> 챗봇을 붙이고 요약 기능을 켜는 회사와, 직원이 채팅방에서 한 줄을 말하면 30초 안에 시스템이 바뀌기 시작하는 회사는 여섯 달 뒤 생산성이 다릅니다. 에이전트가 판단까지 대신하는 것이 아니라, 준비를 완성하고 사람이 결정하는 구조가 가장 오래 갑니다.</p>
  <h2>우리가 보는 투자 지점</h2>
  <p>첫째, 특정 산업의 업무를 끝까지 수행하는 <strong>수직 에이전트</strong> 기업. 범용 모델 위에 도메인 규범과 검사 체계를 얹은 곳입니다. 둘째, 에이전트가 늘어날수록 커지는 전력·데이터센터·보안 인프라. 셋째, AX를 실제로 완수한 전통 기업의 밸류에이션 재평가. AI 기업을 사는 것보다, AI로 바뀐 기업을 먼저 알아보는 것이 더 큰 기회일 수 있습니다.</p>""",
  [("SK AX — 2026 에이전트 AI 트렌드: 에이전틱 AI가 기업 업무를 바꾸는 방식", "https://www.skax.co.kr/insight/trend/3624"),
   ("삼일PwC — 정부의 전략산업 정책으로 보는 2026년 산업 지도", "https://www.pwc.com/kr/ko/insights/samil-insight/samilpwc_industry-outlook2026.pdf"),
   ("CIO Korea — 생성형 AI가 IT 전략을 바꾼다, 2026 IT 전망 조사", "https://www.cio.com/article/4111617/"),
   ("국회도서관 국가전략포털 — Artificial Intelligence Index Report 2026", "https://nsp.nanet.go.kr/plan/subject/detail.do?nationalPlanControlNo=PLAN0000062343")],
  ("insight-space.html", "스페이스"), ("insight-bio.html", "바이오")).replace("{view}", AI_VIEW)

BIO_VIEW = "비만치료제는 신약이 아니라 인프라가 됐습니다. 우리는 그 파도의 2차 수혜인 CDMO, 경구 제형, 기술수출 구조에서 구조화 딜의 기회를 봅니다."
BIO = article("insight-bio", "04", "Bio",
  "신약보다 먼저 움직이는 것",
  "2026년 바이오는 항암과 비만이라는 두 축 위에서 기술수출 규모가 세 배 넘게 뛰었습니다. 신약 자체보다 제형, 생산, 거래 구조가 먼저 값을 받는 해입니다.",
  [("GLP-1 비만약 시장 연평균 성장 (~2030)", "20%"), ("기술수출 계약 규모", "8조→28조"), ("유망 분야 1위: 혁신 신약 (CEO 설문)", "81%"), ("AI 신약·진단 관심", "47.6%")],
  """<p>국내 바이오텍 CEO 설문에서 2026년 가장 유망한 분야로 81%가 혁신 기술 기반 신약을 꼽았고, AI 기반 신약 개발과 진단에 대한 관심도 47.6%였습니다. 신약 타깃은 여전히 항암이 핵심이며, ADC(항체약물접합체)에 이어 뉴모달리티가 주목받습니다. 기술수출은 건수뿐 아니라 계약 규모가 <strong>8조원에서 28조원</strong>으로 대폭 늘었습니다.</p>
  <h2>비만치료제 2.0: 제형의 진화</h2>
  <p>GLP-1 기반 비만약 시장은 2030년까지 연평균 20% 성장이 전망됩니다. 2026년의 관전 포인트는 효능이 아니라 제형입니다. 경구용 비만치료제가 임상 3상을 마치고 출시를 앞두고 있고, 주사에서 알약으로 바뀌는 순간 시장의 폭이 달라집니다. 이 파도는 신약 회사보다 <strong>CDMO와 원료·제형 기업</strong>에 먼저 도착합니다.</p>
  <h2>동시에 진행되는 다섯 변화</h2>
  <p>글로벌 의약품 시장의 구조적 성장, GLP-1 시장 확대, 빅파마의 특허 만료, M&amp;A와 라이선스 거래 활성화, 바이오시밀러 확대와 CDMO 생산능력 확장. 딜로이트는 이 변화들이 2026년에 동시에 진행된다고 봅니다. 여기에 미국의 중국 바이오 규제가 한국 CDMO와 위탁연구에 반사이익을 줄 가능성이 더해집니다.</p>
  <h2>우리가 보는 투자 지점</h2>
  <p>첫째, 임상 성패에 노출되지 않는 <strong>생산·제형·원료 계층</strong>. 둘째, 기술수출 계약의 마일스톤을 담보로 한 구조화 자금. 라이선스 수입이 예측 가능해질수록 채권형 구조가 성립합니다. 셋째, 바이오시밀러의 가격 경쟁을 버틸 규모를 가진 기업의 인수·합병. 바이오에서 우리의 역할은 과학을 맞히는 것이 아니라, 과학이 맞았을 때 돈이 흐르는 배관을 먼저 잡는 것입니다.</p>""",
  [("더벨 — 2026 바이오텍 CEO 시장 전망: 항암·ADC 잇는 뉴모달리티", "https://m.thebell.co.kr/m/newsview.asp?svccode=&newskey=202601051416481560105269"),
   ("Deloitte Korea — 2026 제약·바이오·의료기기 산업 전망", "https://www.deloitte.com/kr/ko/Industries/life-sciences-health-care/perspectives/2026-outlook-pharma-biotech-medical-devices.html"),
   ("히트뉴스 — 신약보다 '이것' 먼저 움직인다, 2026 바이오산업 5대 변수", "https://www.hitnews.co.kr/news/articleView.html?idxno=73096"),
   ("한국IT산업뉴스 — 2026 K-바이오 투자 지도", "https://www.koreaiin.com/news/900155")],
  ("insight-ai.html", "인공지능"), ("insights.html", "인사이트")).replace("{view}", BIO_VIEW)

HUB = """
<section class="page-hero">
  <div class="wrap">
    <div class="crumb"><b>Insights</b> · Industry perspectives</div>
    <h1 class="h-xl rv">AI가 수요를 바꾸는<br>네 산업</h1>
    <p class="lead rv d1">우리가 바꾸는 곳이 아니라 지켜보는 곳입니다. 에너지, 스페이스, 인공지능, 바이오. 2026년의 숫자를 출처와 함께 읽고, 확신이 서면 자본을 넣습니다. 수치는 출처가 있어야 씁니다.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="insight-grid">
      <a class="icard rv" href="insight-energy.html"><div class="num">01</div><div class="t">Energy</div><h3>전기를 구하는 쪽이 협상력을 잃는 시대</h3><p>데이터센터 전력수요 460→1,000 TWh. 발전원보다 계통·저장·수요지 인접성이 프리미엄을 받는다.</p><span class="more">읽기 →</span></a>
      <a class="icard rv d1" href="insight-space.html"><div class="num">02</div><div class="t">Space</div><h3>기술 자립에서 시장 자립으로</h3><p>우주청 예산 1조 1,201억, 뉴스페이스 펀드 81억→2,000억. 민간의 첫 계약이 어디서 나오는가.</p><span class="more">읽기 →</span></a>
      <a class="icard rv d2" href="insight-ai.html"><div class="num">03</div><div class="t">Artificial Intelligence</div><h3>에이전트가 일하는 회사와 발표만 한 회사</h3><p>기업 앱의 40%가 에이전트를 품는 해. 도입과 전환의 차이는 프로그램을 고칠 사람이 안에 있는가다.</p><span class="more">읽기 →</span></a>
      <a class="icard rv d3" href="insight-bio.html"><div class="num">04</div><div class="t">Bio</div><h3>신약보다 먼저 움직이는 것</h3><p>기술수출 8조→28조, GLP-1 연 20% 성장. 과학이 맞았을 때 돈이 흐르는 배관을 먼저 잡는다.</p><span class="more">읽기 →</span></a>
    </div>
  </div>
</section>
"""
