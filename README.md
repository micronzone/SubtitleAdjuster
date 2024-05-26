# SubtitleAdjuster

SubtitleAdjuster는 smi 및 srt 자막 파일의 인코딩을 변환하고 싱크 시간을 조정하는 스크립트입니다. 이 도구는 여러 개의 자막 파일을 개별 또는 일괄 변환하거나 사용자에게 자막 파일을 변환할지 미리 보여주고 선택하게 하며, 상세한 디버깅 기능을 제공합니다.

> 시즌 전체 자막 파일의 인코딩 변환, 싱크 시간 조정을 한 번의 실행으로 할 수 있으면 좋을 것 같아서 만들었습니다. 


### 주요 기능

- 자막 파일 인코딩 변환 (`euc-kr` ↔ `utf-8`)
- 자막 싱크 시간 조정 (milliseconds 단위로 증가 또는 감소)
- 대화형 모드에서 순차적으로 옵션 실행
- 자막 파일 개별 변환 또는 일괄 변환
- 디버그 모드를 통한 상세 로그 출력

<img width="682" alt="ss" src="https://github.com/micronzone/SubtitleAdjuster/assets/47780105/3ff994df-b690-43f1-ad2e-7ee73236bd11">

### 설치 방법

이 리포지토리를 클론합니다:
  ```sh
  git clone https://github.com/micronzone/SubtitleAdjuster.git
  cd SubtitleAdjuster
  ```

(선택 사항) 가상 환경을 생성하고 활성화합니다:
  ```sh
  python3 -m venv myenv
  source myenv/bin/activate  # Linux 또는 macOS
  .\myenv\Scripts\activate   # Windows
  ```

`chardet` 모듈을 설치합니다.

pip 통해 설치하려면:
```sh
pip install chardet
```

homebrew 통해 설치하려면:
```sh
brew install python-chardet
```

### 사용 방법

자막 파일 개별 변환:
```sh
python3 subtitle_adjuster.py [옵션] [자막 파일 경로]
```

여러 개의 자막 파일 일괄 변환:
```sh
python3 subtitle_adjuster.py [옵션] [디렉토리 경로]
```

### 옵션

- `-a` : 대화형 모드로 모든 옵션을 순차적으로 실행합니다.
- `-e` : 인코딩을 변환합니다. `euc-kr` 또는 `utf-8`을 지정할 수 있습니다. 예: `-e euc-kr` 또는 `-e utf-8`
- `-d` : 자막 싱크 시간을 milliseconds 단위로 감소시킵니다. 예: `-d 1000` (1000ms 감소)
- `-i` : 자막 싱크 시간을 milliseconds 단위로 증가시킵니다. 예: `-i 1000` (1000ms 증가)
- `--debug` : 디버그 모드를 활성화하여 상세 로그를 출력합니다.

### 예시

대화형 모드에서 모든 옵션을 순차적으로 실행:
```sh
python3 subtitle_adjuster.py -a /path/to/dir/ or /path/to/file
```

자막 파일의 인코딩을 `euc-kr`로 변환:
```sh
python3 subtitle_adjuster.py -e euc-kr /path/to/dir/ or /path/to/file
```


자막 파일의 인코딩을 `utf-8`로 변환:
```sh
python3 subtitle_adjuster.py -e utf-8 /path/to/dir/ or /path/to/file
```

자막 파일의 싱크 시간을 1000ms 증가 (1초=`1000`, 원하는 값으로 조정 가능):
```sh
python3 subtitle_adjuster.py -i 1000 /path/to/dir/ or /path/to/file
```

자막 파일의 싱크 시간을 1000ms 감소 (1초=`1000`, 원하는 값으로 조정 가능):
```sh
python3 subtitle_adjuster.py -d 1000 /path/to/dir/ or /path/to/file
```

디버그 모드를 사용하여 변환:
```sh
python3 subtitle_adjuster.py -a --debug /path/to/dir/ or /path/to/file
```

### 업데이트

SubtitleAdjuster 리포지토리 업데이트를 확인하는 것이 좋습니다!

```sh
cd SubtitleAdjuster
git status
```

변경 사항 가져오기:

```sh
git pull origin main
```

### 기여 방법

기여해주셔서 감사합니다! 이 프로젝트에 기여하시려면 아래 단계를 따라 주세요:

1. 이 리포지토리를 포크하세요
2. 기능 브랜치(micronzone 브랜치)를 생성하세요 (`git checkout -b micronzone/SubtitleAdjuster`)
3. 변경 사항을 커밋하세요 (`git commit -m 'Add some SubtitleAdjuster'`)
4. 브랜치에 푸시하세요 (`git push origin micronzone/SubtitleAdjuster`)
5. 풀 리퀘스트를 여세요

### 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.
