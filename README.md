# DS 게임 입체 3D + 5:3 와이드스크린 (New 3DS)

New 3DS에서 TWiLight Menu++로 실행하는 DS 게임을 **입체 3D**와 **위 화면 가로 전체(400픽셀, 5:3) 와이드스크린**으로 표시하는 패치입니다. 롬 파일은 수정하지 않습니다.

*Stereoscopic 3D + full-width (5:3) widescreen for a few DS games on New 3DS with TWiLight Menu++ and TWPatch. Korean ROM versions only. Documentation is in Korean.*

> **이 저장소에 없는 것, 공유하지 않는 것**
>
> - **게임 롬 파일은 포함하지 않으며 공유하지 않습니다.** 롬을 구하는 방법도 안내하지 않습니다. 본인이 소유한 게임 카드에서 직접 덤프한 롬이 필요합니다.
> - **닌텐도의 시스템 파일(TwlBg, 펌웨어)은 포함하지 않습니다.** 3D용 `Widescreen.cxi`는 본인 본체에서 TWPatch로 만든 파일을 `DS3D_Patcher.exe`로 고쳐서 직접 만듭니다.
> - 닌텐도와 관계없는 비공식 개인 프로젝트입니다. 사용에 따른 책임은 사용자에게 있습니다.

---

## 시작하기 전에 — 미리 설치되어 있어야 하는 것

이 패치는 아래 두 가지가 **이미 설치되어 정상 동작하는 상태**에 덧붙이는 것입니다. 이 저장소는 이 둘의 설치 방법을 다루지 않습니다.

와이드스크린 패치를 아직 설치하지 않았다면 DS-Homebrew 위키의 안내를 따라 먼저 설치하세요: **[TWiLight Menu++ — 와이드스크린으로 플레이하기](https://wiki.ds-homebrew.com/ko-KR/twilightmenu/playing-in-widescreen)**

| 미리 필요한 것 | 확인 방법 |
|---|---|
| **TWiLight Menu++** (확인 버전 v27.25.1, nds-bootstrap v2.17.0) | TWiLight Menu에서 DS 게임이 실행됨 |
| **TWPatch 와이드스크린 패치** (RTCom 옵션 포함) — [설치 안내](https://wiki.ds-homebrew.com/ko-KR/twilightmenu/playing-in-widescreen) | 게임 화면 비율을 16:10으로 하면 2D 와이드스크린으로 나옴. SD 카드에 `sd:/_nds/TWiLightMenu/TwlBg/Widescreen.cxi`가 있음 |

다른 버전의 TWiLight Menu++에서는 확인하지 못했습니다. 본체와 롬에 대한 조건은 아래 [조건](#조건)을 보세요.

## 설치 — 3단계

**준비물:** 이 저장소(초록색 `Code` 버튼 → `Download ZIP` → 압축 풀기), SD 카드, 윈도우 PC

### 1단계. 3D용 `Widescreen.cxi` 만들기

1. SD 카드의 `sd:/_nds/TWiLightMenu/TwlBg/Widescreen.cxi`를 PC의 아무 폴더에 복사합니다. **이 파일은 지우지 말고 보관하세요** (되돌릴 때 필요).
2. 복사한 파일을 **`DS3D_Patcher.exe` 위에 끌어다 놓습니다.**
3. `[완료]`가 나오면 저장소 폴더 안에 `sd/_nds/TWiLightMenu/TwlBg/Widescreen.cxi`가 만들어진 것입니다.

`[실패] 지원하는 TwlBg 빌드가 아닙니다`가 나오면 아래 [조건](#조건)의 4번을 확인하세요.

### 2단계. SD 카드에 복사

저장소의 **`sd` 폴더 안에 있는 `_nds` 폴더**를 SD 카드 최상위에 복사해 덮어씁니다. 그러면 아래처럼 들어갑니다.

| 파일 | SD 카드 위치 | 게임 |
|---|---|---|
| `Widescreen.cxi` (1단계에서 만든 것) | `sd:/_nds/TWiLightMenu/TwlBg/` | 공통 (기존 파일 덮어쓰기) |
| `IRAK-3D1C.bin` | `sd:/_nds/TWiLightMenu/extras/widescreen/` | 포켓몬스터 화이트 |
| `IREK-8ED6.bin` | `sd:/_nds/TWiLightMenu/extras/widescreen/` | 포켓몬스터 블랙 2 |
| `IPKK-C645.bin` | `sd:/_nds/TWiLightMenu/extras/widescreen/` | 포켓몬스터 하트골드 |
| `CPUK-260F.bin` | `sd:/_nds/TWiLightMenu/extras/widescreen/` | 포켓몬스터 Pt 기라티나 |
| `ASMK-53AF.bin` | `sd:/_nds/TWiLightMenu/extras/widescreen/` | 슈퍼 마리오 64 DS |

- `.bin` 파일 이름은 바꾸면 안 됩니다. 없는 게임의 `.bin`은 넣지 않아도 됩니다.
- `sd:/luma/sysmodules/TwlBg.cxi`는 건드리지 않습니다.

### 3단계. 게임별 설정

게임별 설정 메뉴(TWiLight Menu에서 게임을 고르고 Y 버튼)에서 아래처럼 맞춥니다.

| 게임 | 화면 비율 | 실행 모드 (Run in) | ARM9 CPU 속도 |
|---|---|---|---|
| 포켓몬스터 화이트 | **16:10** | **DSi 모드** | 기본값 |
| 포켓몬스터 블랙 2 | **16:10** | **DSi 모드** | 기본값 |
| 포켓몬스터 하트골드 | **16:10** | 기본값 | **133MHz (TWL)** |
| 포켓몬스터 Pt 기라티나 | **16:10** | 기본값 | **133MHz (TWL)** |
| 슈퍼 마리오 64 DS | **16:10** | 기본값 | **133MHz (TWL)** |

**HOME 메뉴 포워더(아이콘)로 실행한다면 포워더의 게임별 설정에도 똑같이 설정해야 합니다.** TWiLight Menu의 설정과 포워더의 설정은 서로 별개입니다.

화면 비율 메뉴에는 16:10으로 표시되지만 실제 그림은 5:3(400픽셀)로 나옵니다. 정상입니다.

이제 게임을 실행하고 3D 슬라이더를 올리면 됩니다.

### (선택) 슈퍼 마리오 64 DS — 서클 패드·C스틱 추가

저장소의 `ASMK-53AF.bin`은 3D와 와이드스크린만 들어 있습니다. 서클 패드 이동과 C스틱·ZL·ZR 카메라를 쓰려면 2단계 **전에** 아래를 합니다.

1. shocoman의 [Analog Controls for NDS Games on 3DS](https://github.com/shocoman/Analog-Controls-for-NDS-Games-on-3DS) 저장소의 `action_replay_codes` 폴더에서 이 파일을 받습니다.
   `ASMK-3C73EADE (Korea v1.0) [with Nub stick, ZL and ZR].txt`
2. 받은 파일을 **`DS3D_Patcher.exe` 위에 끌어다 놓습니다.**
3. `[완료]`가 나오면 `sd` 폴더 안의 `ASMK-53AF.bin`이 C스틱 버전으로 바뀐 것입니다.

---

## 조건

1. **New 3DS 또는 New 3DS XL.** 구형 3DS·2DS·New 2DS XL은 안 됩니다 (3D 화면 제어 칩이 다릅니다).
2. **Luma3DS** 설정에서 `Enable loading external FIRMs and modules`가 켜져 있음.
3. **TWiLight Menu++**와 nds-bootstrap이 설치되어 DS 게임이 실행됨. (확인 버전: TWiLight Menu++ v27.25.1, nds-bootstrap v2.17.0)
4. **TWPatch 와이드스크린**(RTCom 옵션 포함)이 설치되어 2D 와이드스크린이 동작함. ([설치 안내](https://wiki.ds-homebrew.com/ko-KR/twilightmenu/playing-in-widescreen))
   패처는 TWPatch가 만든 파일의 코드를 630바이트 고칩니다. 고칠 위치가 고정되어 있어서 **제작자 본체에서 나온 것과 같은 빌드**(파일 SHA-256 `082a9e569ebf5aac…`, 1,292,800바이트)에만 적용됩니다. 시스템 버전, TWPatch 버전이나 옵션이 달라 빌드가 다르면 패처가 아무것도 쓰지 않고 멈추며, 그 경우는 지원하지 않습니다.

### 롬 조건

| 게임 | 필요한 롬 |
|---|---|
| 다섯 게임 공통 | **한국어판**, 수정하지 않은 **클린 롬**. 다른 지역판·다른 리비전·패치된 롬은 내부 주소가 달라 적용되지 않습니다 |
| 포켓몬스터 화이트, 블랙 2 | 위 조건에 더해 **DSi 모드를 지원하는 클린 롬**이어야 합니다. 이 두 게임의 엔진은 DSi 모드로 실행될 때만 동작합니다. DSi용 데이터가 잘려 나갔거나(트림) 수정되어 DSi 모드로 실행되지 않는 롬에는 적용할 수 없습니다 |

TWiLight Menu는 `게임코드-헤더CRC.bin`이라는 파일 이름으로 그 게임의 파일을 찾습니다. 롬이 조건과 다르면 CRC가 달라 파일이 아예 읽히지 않습니다.

## 사용법

### 3D 슬라이더

- 올리면 3D가 켜지고, 슬라이더 위치가 깊이입니다. 끝까지 내리면 2D입니다.
- 3D일 때 위 화면 밝기는 본체의 3D용 보정값으로 자동으로 올라갑니다.
- 슬라이더를 올린 채 게임을 켜면 약 10초 뒤에 3D가 켜집니다.
- 화면 정면에서 봐야 합니다 (DS 모드에서는 얼굴 추적 3D가 동작하지 않습니다).

### 단축키

| 게임 | 조작 | 기능 |
|---|---|---|
| 화이트, 블랙 2 | SELECT + 오른쪽 / 왼쪽 | 깊이 ±25% |
| | SELECT + 위 / 아래 | 초점 거리 |
| | L + R + SELECT | 좌우 눈 바꾸기 |
| | SELECT + START | 눈 테스트 (한쪽 눈 화면 끄기, 다시 누르면 복귀) |
| 하트골드, 기라티나, 마리오 64 DS | L + R + 오른쪽 / 왼쪽 | 깊이 ±25% |
| | L + R + 위 / 아래 | 초점 거리 |
| | L + R + START | 좌우 눈 바꾸기 |

- 입체감이 뒤집혀 보이면(가까운 것이 멀게 보임) "좌우 눈 바꾸기"를 한 번 누릅니다.
- 하트골드·기라티나·마리오 64 DS에서 L+R을 누르고 있는 동안 십자키와 START는 게임에 전달되지 않습니다.
- 단축키로 바꾼 값은 게임을 끄면 기본값으로 돌아갑니다.

### 슈퍼 마리오 64 DS 조작 (C스틱 버전)

| 입력 | 기능 |
|---|---|
| 서클 패드 | 마리오 이동 (아날로그) |
| C스틱 좌 / 우, ZL / ZR | 카메라 회전 |

C스틱·ZL·ZR은 잘못된 입력을 걸러내기 위해 약 0.1초 누르고 있어야 반응합니다. 십자키와 터치 조작도 그대로 쓸 수 있습니다.

## 알려진 문제

- **화이트, 블랙 2:** NPC에게 말을 걸어 말풍선이 뜨는 순간 화면이 한 번 흔들립니다.
- **하트골드, 기라티나:** 프레임이 계속 밀리면 3D가 약 3초(반복되면 최대 48초) 꺼졌다가 다시 켜집니다.
- **위 다섯 게임이 아닌 와이드스크린 게임**은 3D가 되지 않으며, 3D용 `Widescreen.cxi`의 영향을 받습니다.
  - 그림이 가로로 약 4% 늘어나 보입니다.
  - 3D 슬라이더를 움직이면 약 0.1초 동안 가짜 버튼 입력이 들어가고 화면이 밝아집니다. **이런 게임에서는 슬라이더를 끝까지 내려 두세요** (내려 두면 영향 없음).
- **와이드스크린을 끈(4:3) 게임**은 일반 TwlBg로 실행되므로 영향이 없고 3D도 되지 않습니다.

## 원래대로 되돌리기

1. 1단계에서 보관한 원래 `Widescreen.cxi`를 `sd:/_nds/TWiLightMenu/TwlBg/Widescreen.cxi`에 덮어씁니다.
2. `sd:/_nds/TWiLightMenu/extras/widescreen/`에서 이 저장소의 `.bin` 파일을 지웁니다.

## 문제 해결

| 증상 | 확인할 것 |
|---|---|
| 패처가 `지원하는 TwlBg 빌드가 아닙니다`로 멈춤 | TwlBg 빌드가 다릅니다 ([조건](#조건) 4번). 지원하지 않습니다 |
| 패처가 `이미 3D 용입니다`라고 함 | 이미 고친 파일을 넣었습니다. 고치기 전의 TWPatch 파일을 넣어 주세요 |
| 3D가 전혀 안 됨, 2D 와이드스크린만 나옴 | `.bin` 이름과 위치, 롬 조건(한국어판 클린 롬), 화면 비율 16:10, `Widescreen.cxi`를 3D용으로 바꿨는지 |
| 화이트·블랙 2만 3D가 안 됨 | 실행 모드가 DSi 모드인지, 롬이 DSi 모드를 지원하는 클린 롬인지 |
| 화면이 심하게 흔들리거나 3D가 금방 꺼짐 (하트골드, 기라티나, 마리오 64 DS) | ARM9 CPU 속도 133MHz. **포워더로 실행했다면 포워더 쪽 설정** |
| 입체감이 반대로 보임 | 좌우 눈 바꾸기 단축키 |
| TWiLight 실행 후 화면이 안 나옴 | 보관해 둔 원래 `Widescreen.cxi`로 되돌린 뒤 다시 시도 |

## 패처에 대해

- `DS3D_Patcher.exe`는 `tools/ds3d_patcher.py`를 PyInstaller로 묶은 것입니다. 넣어 준 파일을 검사한 뒤 정해진 위치의 바이트만 바꾸고, 지원하지 않는 파일이면 아무것도 쓰지 않습니다. 인터넷에 접속하지 않습니다.
- 서명되지 않은 실행 파일이라 윈도우가 "알 수 없는 게시자" 경고를 띄울 수 있습니다. 실행 파일이 꺼려지거나 윈도우가 아니면 Python 3로 같은 일을 할 수 있습니다.

  ```
  python tools/ds3d_patcher.py Widescreen.cxi
  ```

## 저장소 구성

```
├─ DS3D_Patcher.exe                   패처 (파일을 끌어다 놓기)
├─ sd/_nds/TWiLightMenu/extras/widescreen/
│  ├─ IRAK-3D1C.bin                   포켓몬스터 화이트
│  ├─ IREK-8ED6.bin                   포켓몬스터 블랙 2
│  ├─ IPKK-C645.bin                   포켓몬스터 하트골드
│  ├─ CPUK-260F.bin                   포켓몬스터 Pt 기라티나
│  └─ ASMK-53AF.bin                   슈퍼 마리오 64 DS (3D만)
└─ tools/ds3d_patcher.py              패처의 소스
```

각 `.bin`에는 그 게임의 3D 엔진과 5:3 와이드스크린 코드가 함께 들어 있습니다.

| 파일 | 크기 | SHA-256 (앞 16자리) |
|---|---|---|
| `IRAK-3D1C.bin` | 4,432 | `7a2da9b003ad1ee3` |
| `IREK-8ED6.bin` | 4,576 | `b86b83f91199ec29` |
| `IPKK-C645.bin` | 3,944 | `601a069ef269efdd` |
| `CPUK-260F.bin` | 3,904 | `f77a945382509378` |
| `ASMK-53AF.bin` (저장소, 3D만) | 4,648 | `b615ae56232b2eb8` |
| `ASMK-53AF.bin` (C스틱 추가 후) | 7,456 | `a6f95989475aa299` |
| `Widescreen.cxi` (1단계 결과, 입력이 제작자 파일과 같을 때) | 1,750,016 | `052bfa98621c4185` |

## 동작 원리 (요약)

- **3D용 `Widescreen.cxi`** — TwlBg는 DS 화면을 3DS 화면에 그려 주는 시스템 모듈입니다. 고친 TwlBg는 DS가 번갈아 보내는 프레임을 왼쪽·오른쪽 눈 화면으로 나눠 표시하고, 3D 슬라이더 값을 게임 쪽 엔진에 전달하고, 3D일 때 백라이트를 보정하고, 그림을 400픽셀 폭으로 그립니다.
- **게임별 `.bin`** — TWiLight Menu의 와이드스크린 치트 자리에 들어가는 코드입니다. 원래의 와이드스크린 코드(5:3으로 수정)에 더해, 게임이 매 프레임 왼쪽·오른쪽 눈 시점을 번갈아(또는 두 번) 그리게 하는 3D 엔진이 들어 있습니다. 실행 중 메모리에만 적용됩니다.

## 출처

| 구성 요소 | 출처 |
|---|---|
| TWiLight Menu++, nds-bootstrap | DS-Homebrew — https://github.com/DS-Homebrew/TWiLightMenu |
| TWPatch (와이드스크린 TwlBg, RTCom) | Sono |
| 와이드스크린 기본 코드 (`.bin` 앞부분) | TWiLight Menu++의 와이드스크린 치트 데이터 |
| 마리오 64 DS 서클 패드·C스틱 패치 (포함하지 않음) | shocoman — https://github.com/shocoman/Analog-Controls-for-NDS-Games-on-3DS |

## 버전

TwlBg 패치 stereo29 · 화이트 v23 · 블랙 2 v4 · 하트골드 v3 · 기라티나 v1 · 마리오 64 DS v10 (2026-11-16)
