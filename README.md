# DS 게임 입체 3D + 5:3 와이드스크린 (New 3DS)

New 3DS에서 TWiLight Menu++로 실행하는 DS 게임을 **입체 3D**와 **위 화면 가로 전체(400픽셀, 5:3) 와이드스크린**으로 표시하는 패치입니다.
롬 파일은 수정하지 않고, 실행 중 메모리에만 적용됩니다.

*Stereoscopic 3D + full-width (5:3) widescreen for a few DS games on New 3DS with TWiLight Menu++ and TWPatch. Korean ROM versions only. Documentation is in Korean.*

> **이 저장소에 없는 것, 공유하지 않는 것**
>
> - **게임 롬 파일은 포함하지 않으며 공유하지 않습니다.** 롬을 구하는 방법도 안내하지 않습니다. 본인이 소유한 게임 카드에서 직접 덤프한 롬이 필요합니다.
> - **닌텐도의 시스템 파일(TwlBg, 펌웨어)은 포함하지 않습니다.** 3D용 `Widescreen.cxi`는 본인 본체에서 TWPatch로 만든 파일을 `tools/make_widescreen_3d.py`로 고쳐서 직접 만듭니다.
> - 이 프로젝트는 닌텐도와 관계가 없는 비공식 개인 프로젝트입니다. 사용에 따른 책임은 사용자에게 있습니다.

기준일: 2026-11-16 · 확인 환경: New 3DS(한국판), Luma3DS, TWiLight Menu++ v27.25.1, nds-bootstrap v2.17.0

---

## 1. 지원 게임

| 게임 (한국어판) | 파일 | 실행 모드 | ARM9 CPU 속도 | 추가 기능 |
|---|---|---|---|---|
| 포켓몬스터 화이트 | `IRAK-3D1C.bin` | DSi 모드 | 설정 불필요 | — |
| 포켓몬스터 블랙 2 | `IREK-8ED6.bin` | DSi 모드 | 설정 불필요 | — |
| 포켓몬스터 하트골드 | `IPKK-C645.bin` | 기본값 | **133MHz (TWL) 필수** | — |
| 포켓몬스터 Pt 기라티나 | `CPUK-260F.bin` | 기본값 | **133MHz (TWL) 필수** | — |
| 슈퍼 마리오 64 DS | `ASMK-53AF.bin` | 기본값 | **133MHz (TWL) 필수** | 서클 패드 이동, C스틱·ZL·ZR 카메라 (선택, 4-4 참고) |

- 파일 이름은 `게임코드-헤더CRC.bin`입니다. TWiLight Menu가 이 이름으로 파일을 찾으므로 **이름을 바꾸면 안 됩니다.**
- 롬 버전이 다르면(일본판, 북미판, 다른 리비전) 적용되지 않습니다. 이름만 맞춰도 내부 주소가 달라 동작하지 않습니다.
- 표에 없는 게임은 3D가 되지 않습니다.

## 2. 전제 조건

이 가이드는 아래가 **이미 되어 있다**고 가정합니다.

1. **New 3DS 또는 New 3DS XL.** 구형 3DS·2DS·New 2DS XL은 안 됩니다 (3D 화면 제어 칩이 다릅니다).
2. **Luma3DS** 설정에서 `Enable loading external FIRMs and modules`가 켜져 있음.
3. **TWiLight Menu++**와 nds-bootstrap이 설치되어 DS 게임이 실행됨.
4. **TWPatch 와이드스크린**(RTCom 옵션 포함)이 설치되어 2D 와이드스크린이 동작함. 즉 아래 두 파일이 있음.
   - `sd:/luma/sysmodules/TwlBg.cxi`
   - `sd:/_nds/TWiLightMenu/TwlBg/Widescreen.cxi`
5. PC에 **Python 3** (도구 실행용, 추가 라이브러리 불필요).

### 지원하는 TwlBg 빌드

3D용 `Widescreen.cxi`는 TWPatch가 만든 파일의 코드를 630바이트 고쳐서 만듭니다. 고칠 위치가 고정되어 있어서, **제작자의 본체에서 나온 것과 같은 빌드**에만 적용됩니다.

| 항목 | 값 |
|---|---|
| 입력 파일 (TWPatch 결과물) SHA-256 | `082a9e569ebf5aac…` (1,292,800바이트) |
| 압축을 푼 코드 SHA-256 | 도구가 자동으로 확인 |

시스템 버전, TWPatch 버전이나 선택한 옵션이 달라 빌드가 다르면 도구가 아무것도 쓰지 않고 멈춥니다. 그 경우는 지원하지 않습니다.

## 3. 저장소 구성

```
├─ README.md
├─ sd/                                SD 카드에 복사할 폴더
│  └─ _nds/TWiLightMenu/extras/widescreen/
│     ├─ IRAK-3D1C.bin                포켓몬스터 화이트
│     ├─ IREK-8ED6.bin                포켓몬스터 블랙 2
│     ├─ IPKK-C645.bin                포켓몬스터 하트골드
│     ├─ CPUK-260F.bin                포켓몬스터 Pt 기라티나
│     └─ ASMK-53AF.bin                슈퍼 마리오 64 DS (3D만, 서클 패드·C스틱 기능 없음)
└─ tools/
   ├─ make_widescreen_3d.py           내 Widescreen.cxi → 3D용 Widescreen.cxi
   └─ add_sm64_cstick.py              마리오 64 DS 파일에 서클 패드·C스틱 기능 추가
```

각 `.bin`에는 그 게임의 3D 엔진과 5:3 와이드스크린 코드가 함께 들어 있습니다.

## 4. 설치

### 4-1. 백업

SD 카드의 `sd:/_nds/TWiLightMenu/TwlBg/Widescreen.cxi`를 PC에 복사해 둡니다. 되돌릴 때 필요합니다.

### 4-2. 3D용 Widescreen.cxi 만들기

백업한 파일을 입력으로 도구를 실행합니다.

```
python tools/make_widescreen_3d.py Widescreen.cxi Widescreen_3D.cxi
```

`written: … identical to the reference build`가 나오면 성공입니다. 만들어진 파일의 이름을 `Widescreen.cxi`로 바꿔 아래 위치에 덮어씁니다.

```
sd:/_nds/TWiLightMenu/TwlBg/Widescreen.cxi
```

`sd:/luma/sysmodules/TwlBg.cxi`는 **건드리지 않습니다** (TWiLight 메뉴 화면용 2D 와이드스크린).

### 4-3. 게임 파일 복사

저장소의 `sd` 폴더 **안에 있는** `_nds` 폴더를 SD 카드 최상위에 복사합니다. `.bin` 파일이 아래 위치에 들어가면 됩니다.

```
sd:/_nds/TWiLightMenu/extras/widescreen/
```

폴더가 없으면 만들어 주세요. 가지고 있지 않은 게임의 `.bin`은 넣지 않아도 됩니다.

### 4-4. (선택) 슈퍼 마리오 64 DS — 서클 패드·C스틱 추가

저장소의 `ASMK-53AF.bin`은 3D와 와이드스크린만 들어 있습니다. 서클 패드 이동과 C스틱·ZL·ZR 카메라는 shocoman의 [Analog Controls for NDS Games on 3DS](https://github.com/shocoman/Analog-Controls-for-NDS-Games-on-3DS) 패치를 합쳐서 추가합니다. 그 패치는 이 저장소에 들어 있지 않으므로 직접 받아야 합니다.

1. 위 저장소의 `action_replay_codes` 폴더에서 아래 파일을 받습니다.
   `ASMK-3C73EADE (Korea v1.0) [with Nub stick, ZL and ZR].txt`
2. 도구를 실행합니다.

   ```
   python tools/add_sm64_cstick.py sd/_nds/TWiLightMenu/extras/widescreen/ASMK-53AF.bin "ASMK-3C73EADE (Korea v1.0) [with Nub stick, ZL and ZR].txt" ASMK-53AF_cstick.bin
   ```
3. 만들어진 파일의 이름을 `ASMK-53AF.bin`으로 바꿔 `sd:/_nds/TWiLightMenu/extras/widescreen/`에 넣습니다.

도구는 그 패치를 3D 엔진 파일 뒤에 붙이고 76바이트를 고칩니다 (잘못된 입력을 걸러내는 필터 연결, 3DS 쪽 C스틱 읽기를 가볍게 해서 화면 끊김 방지). TwlBg에 RTCom이 들어 있어야 동작합니다.

### 4-5. 게임별 설정

5번 항목대로 설정합니다.

## 5. 게임별 설정

게임마다 **두 가지**를 설정합니다.

| 설정 항목 | 값 | 대상 |
|---|---|---|
| 화면 비율 (Screen Aspect Ratio) | **16:10 (와이드스크린)** | 다섯 게임 모두 |
| ARM9 CPU 속도 (ARM9 CPU Speed) | **133MHz (TWL)** | 하트골드, 기라티나, 마리오 64 DS |

화이트와 블랙 2는 DSi 모드로 실행되어 CPU가 자동으로 빠른 속도가 되므로 CPU 설정이 필요 없습니다. 실행 모드(Run in)를 "DS 모드"로 바꿔 두었다면 "DSi 모드"로 되돌려 주세요.

화면 비율 메뉴에는 16:10으로 표시되지만 실제 그림은 5:3(400픽셀)로 나옵니다. 정상입니다.

### 설정하는 곳 — 실행 방법에 따라 다릅니다

**TWiLight Menu에서 실행하는 경우와 HOME 메뉴 포워더(아이콘)로 실행하는 경우의 설정은 서로 별개입니다.** 둘 다 쓴다면 양쪽 모두 설정해야 합니다.

| 실행 방법 | 설정 여는 법 | 설정 파일 |
|---|---|---|
| TWiLight Menu | 게임을 고른 뒤 게임별 설정 메뉴 (Y 버튼) | `sd:/_nds/TWiLightMenu/gamesettings/<롬 파일명>.ini` |
| HOME 메뉴 포워더 | 포워더의 게임별 설정 메뉴 | `sd:/_nds/ntr-forwarder/gamesettings/<롬 파일명>.ini` |

PC에서 ini 파일을 직접 고쳐도 됩니다. 해당 줄만 아래 값으로 바꿉니다.

```ini
WIDESCREEN = 1      ; 화면 비율 16:10 — 다섯 게임 모두
BOOST_CPU = 1       ; ARM9 133MHz — 하트골드, 기라티나, 마리오 64 DS만
```

ini 파일은 그 게임의 게임별 설정을 한 번 열었다 닫으면 만들어집니다.

### 설정 요약

| 게임 | `WIDESCREEN` | `BOOST_CPU` | `DSI_MODE` |
|---|---|---|---|
| 포켓몬스터 화이트 | 1 | 기본값(-1) | DSi 모드 |
| 포켓몬스터 블랙 2 | 1 | 기본값(-1) | DSi 모드 |
| 포켓몬스터 하트골드 | 1 | **1** | 기본값(-1) |
| 포켓몬스터 Pt 기라티나 | 1 | **1** | 기본값(-1) |
| 슈퍼 마리오 64 DS | 1 | **1** | 기본값(-1) |

133MHz가 필요한 이유: 이 세 게임은 화면을 왼쪽·오른쪽 눈용으로 두 번 그리는데, 기본 속도(67MHz)에서는 한 프레임 안에 끝나지 않아 화면이 흔들리거나 3D가 꺼집니다.

## 6. 사용법

### 3D 슬라이더

- 올리면 3D가 켜지고, 슬라이더 위치가 깊이입니다.
- 끝까지 내리면 2D입니다 (3D 화면 장치도 꺼짐).
- 3D일 때 위 화면 밝기는 본체의 3D용 보정값으로 자동으로 올라갑니다.
- 슬라이더를 올린 채 게임을 켜면 약 10초 뒤에 3D가 켜집니다.

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

### 슈퍼 마리오 64 DS 조작 (4-4를 적용한 경우)

| 입력 | 기능 |
|---|---|
| 서클 패드 | 마리오 이동 (아날로그) |
| C스틱 좌 / 우 | 카메라 회전 |
| ZL / ZR | 카메라 회전 |

- C스틱·ZL·ZR은 잘못된 입력을 걸러내기 위해 약 0.1초 누르고 있어야 반응합니다.
- 십자키와 터치 조작도 그대로 쓸 수 있습니다.

## 7. 알려진 문제

- **화이트, 블랙 2:** NPC에게 말을 걸어 말풍선이 뜨는 순간 화면이 한 번 흔들립니다.
- **하트골드, 기라티나:** 필드 화면만 입체입니다 (전투, 메뉴는 평면). 프레임이 계속 밀리면 3D가 약 3초(반복되면 최대 48초) 꺼졌다가 다시 켜집니다.
- **3D 엔진 파일이 없는 다른 와이드스크린 게임:**
  - 그림이 가로로 약 4% 늘어나 보입니다 (TwlBg는 400픽셀로 그리는데 게임의 와이드 코드는 16:10 기준이라서).
  - 3D 슬라이더를 움직이면 약 0.1초 동안 가짜 버튼 입력이 들어가고 화면이 밝아집니다. **이런 게임에서는 슬라이더를 끝까지 내려 두세요** (내려 두면 영향 없음).
- **와이드스크린을 끈(4:3) 게임**은 일반 TwlBg로 실행되므로 3D도 되지 않습니다.
- **마리오 카트 DS**는 지원하지 않습니다 (위·아래 화면을 번갈아 3D로 그리는 게임이라 이 방식으로는 불가능).

## 8. 원래대로 되돌리기

1. 4-1에서 백업한 `Widescreen.cxi`를 `sd:/_nds/TWiLightMenu/TwlBg/Widescreen.cxi`에 덮어씁니다.
2. `sd:/_nds/TWiLightMenu/extras/widescreen/`에서 이 저장소의 `.bin` 파일을 지웁니다.
3. CPU 속도 설정은 그대로 두어도 문제없습니다. 되돌리려면 `BOOST_CPU = -1`.

PC 없이 임시로 끄려면: 전원을 켤 때 SELECT를 누르고 있어 Luma 설정에 들어가 `Enable loading external FIRMs and modules`를 끕니다 (와이드스크린도 함께 꺼짐).

## 9. 문제 해결

| 증상 | 확인할 것 |
|---|---|
| `make_widescreen_3d.py`가 "not the build the patch was made for"로 멈춤 | TwlBg 빌드가 다릅니다 (2번 "지원하는 TwlBg 빌드"). 지원하지 않습니다 |
| 3D가 전혀 안 됨, 2D 와이드스크린만 나옴 | `.bin` 파일 이름과 위치, 롬이 한국어판인지, 화면 비율이 16:10인지, `Widescreen.cxi`를 3D용으로 바꿨는지 |
| 화면이 심하게 흔들리거나 3D가 금방 꺼짐 (하트골드, 기라티나, 마리오 64 DS) | ARM9 CPU 속도 133MHz. **포워더로 실행했다면 포워더 쪽 설정**을 확인 |
| 입체감이 반대로 보임 | 좌우 눈 바꾸기 단축키 |
| 게임이 4:3으로 나오고 3D도 안 됨 | 화면 비율 설정, Luma의 external FIRMs 옵션 |
| TWiLight 실행 후 화면이 안 나옴 | 백업한 `Widescreen.cxi`로 되돌린 뒤 다시 시도 |

파일 확인용 SHA-256 (앞 16자리):

| 파일 | 크기 | SHA-256 |
|---|---|---|
| `IRAK-3D1C.bin` | 4,432 | `7a2da9b003ad1ee3` |
| `IREK-8ED6.bin` | 4,576 | `b86b83f91199ec29` |
| `IPKK-C645.bin` | 3,944 | `601a069ef269efdd` |
| `CPUK-260F.bin` | 3,904 | `f77a945382509378` |
| `ASMK-53AF.bin` (저장소, 3D만) | 4,648 | `b615ae56232b2eb8` |
| `ASMK-53AF.bin` (4-4 적용 후) | 7,456 | `a6f95989475aa299` |
| `Widescreen.cxi` (4-2 결과, 입력이 제작자 파일과 같을 때) | 1,750,016 | `052bfa98621c4185` |

## 10. 동작 원리 (요약)

- **3D용 `Widescreen.cxi`** — TwlBg는 DS 화면을 3DS 화면에 그려 주는 시스템 모듈입니다. 고친 TwlBg는 DS가 번갈아 보내는 프레임을 왼쪽·오른쪽 눈 화면으로 나눠 표시하고, 3D 슬라이더 값을 게임 쪽 엔진에 전달하고, 3D일 때 백라이트를 보정하고, 그림을 400픽셀 폭으로 그립니다.
- **게임별 `.bin`** — TWiLight Menu의 와이드스크린 치트 자리에 들어가는 코드입니다. 원래의 와이드스크린 코드(5:3으로 수정)에 더해, 게임이 매 프레임 왼쪽·오른쪽 눈 시점을 번갈아(또는 두 번) 그리게 하는 3D 엔진이 들어 있습니다.
- **3D 화면 장치(패럴랙스 배리어)** 는 DS 쪽에서 I2C로 켜고 끕니다. New 3DS의 얼굴 추적 3D는 DS 모드에서 동작하지 않으므로 화면 정면에서 봐야 합니다.

## 11. 출처

| 구성 요소 | 출처 |
|---|---|
| TWiLight Menu++, nds-bootstrap | DS-Homebrew — https://github.com/DS-Homebrew/TWiLightMenu |
| TWPatch (와이드스크린 TwlBg, RTCom) | Sono |
| 와이드스크린 기본 코드 (`.bin` 앞부분) | TWiLight Menu++의 와이드스크린 치트 데이터 |
| 마리오 64 DS 서클 패드·C스틱 패치 (포함하지 않음) | shocoman — https://github.com/shocoman/Analog-Controls-for-NDS-Games-on-3DS |

## 12. 버전

| 구성 요소 | 버전 |
|---|---|
| TwlBg 패치 | stereo29 |
| 포켓몬스터 화이트 엔진 | v23 |
| 포켓몬스터 블랙 2 엔진 | v4 |
| 포켓몬스터 하트골드 엔진 | v3 |
| 포켓몬스터 Pt 기라티나 엔진 | v1 |
| 슈퍼 마리오 64 DS 엔진 | v10 |
