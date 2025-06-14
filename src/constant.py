SUMMARY_LENGTH_MIN = 200
SUMMARY_LENGTH_RANGE1 = 500
SUMMARY_LENGTH_RANGE2 = 1500
SUMMARY_LENGTH_MAX = 3000


LANG_OPTIONS = {
    "🇰🇷 한국어": "ko",
    "🇺🇸 English": "en",
    "🇯🇵 日本語": "ja",
    "🇨🇳 中文": "zh",
    "🇫🇷 Français": "fr",
    "🇩🇪 Deutsch": "de",
    "🇪🇸 Español": "es",
}


UI_LABELS = {
    "ko": {
        "app_title": "유튜브 대본 요약 서비스",
        "sidebar_title": "⚙️ 설정 패널",
        "model_provider": "모델 제공자 선택:",
        "model_select": "요약 모델 선택:",
        "lang_select": "요약 언어 선택:",
        "lang_display": lambda x: x.split(" ")[1],
        "yt_input": "유튜브 링크 입력",
        "yt_input_placeholder": "https://www.youtube.com/watch?v=...",
        "invalid_yt": "유효하지 않은 유튜브 링크입니다.",
        "notion_settings": "⚙️ Notion 설정 입력",
        "notion_token": "🔑 Notion API Token",
        "notion_token_placeholder": "ntn_...",
        "notion_db": "📄 Notion Database URL OR ID",
        "notion_db_placeholder": "URL 또는 32자리 ID",
        "notion_save_btn": "✅ OK - 설정 저장",
        "notion_save_success": "✅ Notion 설정이 저장되었습니다.",
        "notion_save_fail": "📄 DB URL/ID 형식이 올바르지 않습니다.",
        "notion_token_fail": "🔑 Token은 'ntn_' 또는 'secret_'으로 시작해야 합니다.",
        "notion_field_warn": "⚠️ 모든 필드를 입력해야 합니다.",
        "auto_save": "✅ 요약 후 자동 Notion 저장",
        "summary_tab": "핵심 요약",
        "section_tab": "섹션별 요약",
        "chat_tab": "AI 채팅",
        "summarize_btn": "대본 요약하기",
        "sectionwise_btn": "섹션별 요약 생성",
        "summary_download": "요약 노트 다운로드",
        "sectionwise_download": "섹션별 요약 다운로드",
        "notion_save_summary": "Notion에 저장",
        "notion_save_sectionwise": "Notion에 저장",
        "original_transcript": "원본 대본",
        "summary_expander": "🔍 요약 결과 보기",
        "sectionwise_expander": "🔍 섹션별 요약 결과 보기",
        "summarizing": "요약 생성 중…",
        "sectionwise_summarizing": "섹션별 요약 생성 중…",
        "notion_saved": "채팅 내용이 Notion에 저장되었습니다.",
        "api_key_warning": "{}를 먼저 환경변수(.env)에 등록하세요.",
        "missing_api_key": "⚠️ {} API 키가 설정되지 않았습니다.",
        "missing_data": "⚠️ 필요한 데이터가 없습니다: {}",
        "memory_info": "💭 메모리: {}개 메시지",
        "reset_chat": "대화 기록 초기화",
        "reset_chat_msg": "👋 대화 기록이 초기화되었습니다. 새로운 질문을 해주세요!",
        "streaming_response": "스트리밍 응답 사용",
        "suggested_questions": "💡 추천 질문:",
        "save_chat_notion": "💾 전체 채팅을 Notion에 저장",
        "save_chat_notion_success": "채팅 내용이 Notion에 저장되었습니다.",
        "chat_input_placeholder": "영상 내용에 대해 궁금한 점을 질문해 주세요...",
        "chat_send_btn": "전송",
        "chat_welcome": "👋 안녕하세요! 이 영상 요약을 바탕으로 궁금한 점을 자유롭게 질문해 주세요.",
        "chat_loading": "AI가 답변을 생성하고 있습니다...",
        "transcript_fallback": "기본 대본 추출 실패, 백업 방식으로 재시도합니다.",
        "transcript_fail": "대본 추출 실패",
        "summary_error": "⚠️ 요약 생성 중 오류가 발생했습니다",
        "overall_summary_error": "⚠️ 전체 요약 생성 중 오류가 발생했습니다",
        "openai_import_error": "langchain-openai 패키지가 설치되어 있지 않습니다. pip install langchain-openai 후 이용하세요.",
        "unsupported_model": "지원하지 않는 모델입니다.",
        "summary_fail": "⚠️ 요약 생성에 실패했습니다. 입력 텍스트를 확인하세요.",
        "sectionwise_done": "✅ 섹션별 요약 완료! 이제 전체 요약을 생성합니다.",
        "overall_summary_done": "✅ 전체 요약 생성 완료!",
        "gemini_quota_exceeded": "⚠️ Google Generative AI API 사용량이 초과되었습니다. 잠시 후 다시 시도하거나, API 할당량을 확인하세요.",
        "openai_summary_error": "⚠️ OpenAI 요약 생성 중 오류가 발생했습니다",
        # === 대본 처리 과정 메시지 ===
        "transcript_apify_try": "⚡ [1단계] Apify 자막 시도",
        "transcript_apify_success": "🟢 [1단계] Apify 자막 성공",
        "transcript_apify_fail": "⚠️ [1단계] Apify 자막 실패, Whisper 전사 시도",
        "transcript_audio_download_try": "⏬ [2단계] 오디오 다운로드 시도",
        "transcript_audio_download_fail": "⚠️ [2단계] 오디오 다운로드 실패",
        "transcript_audio_too_large": "⚠️ [2단계] 파일 크기가 25MB를 초과합니다",
        "transcript_whisper_try": "🔊⏳ [3단계] Whisper 전사(음성 인식) 시작 - 최대 수 분 소요될 수 있습니다.",
        "transcript_whisper_fail": "⚠️ [3단계] Whisper 전사 실패",
        "transcript_whisper_no_result": "⚠️ [3단계] Whisper 전사 결과 없음",
        "transcript_whisper_success": "✅ [3단계] Whisper 전사 성공",
    },
    "en": {
        "app_title": "YouTube Transcript Summarizer",
        "sidebar_title": "⚙️ Settings Panel",
        "model_provider": "Select Model Provider:",
        "model_select": "Select Summary Model:",
        "lang_select": "Select Summary Language:",
        "lang_display": lambda x: x.split(" ")[1],
        "yt_input": "Enter YouTube Link",
        "yt_input_placeholder": "https://www.youtube.com/watch?v=...",
        "invalid_yt": "Invalid YouTube link.",
        "notion_settings": "⚙️ Notion Settings",
        "notion_token": "🔑 Notion API Token",
        "notion_token_placeholder": "ntn_...",
        "notion_db": "📄 Notion Database URL OR ID",
        "notion_db_placeholder": "URL or 32-character ID",
        "notion_save_btn": "✅ OK - Save Settings",
        "notion_save_success": "✅ Notion settings saved.",
        "notion_save_fail": "📄 Invalid DB URL/ID format.",
        "notion_token_fail": "🔑 Token must start with 'ntn_' or 'secret_'.",
        "notion_field_warn": "⚠️ All fields are required.",
        "auto_save": "✅ Auto-save to Notion after summary",
        "summary_tab": "Summary",
        "section_tab": "Sectionwise Summary",
        "chat_tab": "AI Chat",
        "summarize_btn": "Summarize Transcript",
        "sectionwise_btn": "Generate Sectionwise Summary",
        "summary_download": "Download Summary Note",
        "sectionwise_download": "Download Sectionwise Summary",
        "notion_save_summary": "Save to Notion",
        "notion_save_sectionwise": "Save to Notion",
        "original_transcript": "Original Transcript",
        "summary_expander": "🔍 View Summary Result",
        "sectionwise_expander": "🔍 View Sectionwise Summary",
        "summarizing": "Generating summary…",
        "sectionwise_summarizing": "Generating sectionwise summary…",
        "notion_saved": "Chat saved to Notion.",
        "api_key_warning": "Please register {} in your .env file first.",
        "missing_api_key": "⚠️ {} API key is not set.",
        "missing_data": "⚠️ Missing required data: {}",
        "memory_info": "💭 Memory: {} messages",
        "reset_chat": "Reset Chat History",
        "reset_chat_msg": "👋 Chat history reset. Please ask a new question!",
        "streaming_response": "Use Streaming Response",
        "suggested_questions": "💡 Suggested Questions:",
        "save_chat_notion": "💾 Save all chat to Notion",
        "save_chat_notion_success": "Chat saved to Notion.",
        "chat_input_placeholder": "Ask anything about the video content...",
        "chat_send_btn": "Send",
        "chat_welcome": "👋 Hello! Feel free to ask anything based on this video summary.",
        "chat_loading": "AI is generating a response...",
        "transcript_fallback": "Default transcript extraction failed, retrying with backup method.",
        "transcript_fail": "Transcript extraction failed",
        "summary_error": "⚠️ Error occurred during summary generation",
        "overall_summary_error": "⚠️ Error occurred during overall summary generation",
        "openai_import_error": "langchain-openai package is not installed. Please install with pip install langchain-openai.",
        "unsupported_model": "Unsupported model.",
        "summary_fail": "⚠️ Failed to generate summary. Please check the input text.",
        "sectionwise_done": "✅ Sectionwise summary done! Now generating overall summary.",
        "overall_summary_done": "✅ Overall summary generation complete!",
        "gemini_quota_exceeded": "⚠️ Google Generative AI API quota exceeded. Please try again later or check your API quota.",
        "openai_summary_error": "⚠️ Error occurred during OpenAI summary generation",
        # === Transcript process messages ===
        "transcript_apify_try": "⚡ [Step 1] Trying Apify transcript",
        "transcript_apify_success": "🟢 [Step 1] Apify transcript success",
        "transcript_apify_fail": "⚠️ [Step 1] Apify transcript failed, trying Whisper",
        "transcript_audio_download_try": "⏬ [Step 2] Downloading audio",
        "transcript_audio_download_fail": "⚠️ [Step 2] Audio download failed",
        "transcript_audio_too_large": "⚠️ [Step 2] Audio file exceeds 25MB",
        "transcript_whisper_try": "🔊⏳ [Step 3] Whisper transcription (speech-to-text) started - may take several minutes.",
        "transcript_whisper_fail": "⚠️ [Step 3] Whisper transcription failed",
        "transcript_whisper_no_result": "⚠️ [Step 3] No result from Whisper",
        "transcript_whisper_success": "✅ [Step 3] Whisper transcription success",
    },
    "ja": {
        "app_title": "YouTube 字幕要約サービス",
        "sidebar_title": "⚙️ 設定パネル",
        "model_provider": "モデルプロバイダーを選択:",
        "model_select": "要約モデルを選択:",
        "lang_select": "要約言語を選択:",
        "lang_display": lambda x: x.split(" ")[1],
        "yt_input": "YouTubeリンクを入力",
        "yt_input_placeholder": "https://www.youtube.com/watch?v=...",
        "invalid_yt": "無効なYouTubeリンクです。",
        "notion_settings": "⚙️ Notion設定入力",
        "notion_token": "🔑 Notion APIトークン",
        "notion_token_placeholder": "ntn_...",
        "notion_db": "📄 NotionデータベースURLまたはID",
        "notion_db_placeholder": "URLまたは32桁のID",
        "notion_save_btn": "✅ OK - 設定を保存",
        "notion_save_success": "✅ Notion設定が保存されました。",
        "notion_save_fail": "📄 DB URL/IDの形式が正しくありません。",
        "notion_token_fail": "🔑 トークンは 'ntn_' または 'secret_' で始まる必要があります。",
        "notion_field_warn": "⚠️ すべてのフィールドを入力してください。",
        "auto_save": "✅ 要約後に自動でNotionに保存",
        "summary_tab": "要約",
        "section_tab": "セクションごとの要約",
        "chat_tab": "AIチャット",
        "summarize_btn": "字幕を要約する",
        "sectionwise_btn": "セクションごとの要約を生成",
        "summary_download": "要約ノートをダウンロード",
        "sectionwise_download": "セクションごとの要約をダウンロード",
        "notion_save_summary": "Notionに保存",
        "notion_save_sectionwise": "Notionに保存",
        "original_transcript": "元の字幕",
        "summary_expander": "🔍 要約結果を見る",
        "sectionwise_expander": "🔍 セクションごとの要約を見る",
        "summarizing": "要約を生成中…",
        "sectionwise_summarizing": "セクションごとの要約を生成中…",
        "notion_saved": "チャット内容がNotionに保存されました。",
        "api_key_warning": "{} を先に環境変数(.env)に登録してください。",
        "missing_api_key": "⚠️ {} APIキーが設定されていません。",
        "missing_data": "⚠️ 必要なデータがありません: {}",
        "memory_info": "💭 メモリ: {}件のメッセージ",
        "reset_chat": "チャット履歴をリセット",
        "reset_chat_msg": "👋 チャット履歴がリセットされました。新しい質問をしてください！",
        "streaming_response": "ストリーミング応答を使用",
        "suggested_questions": "💡 推奨質問:",
        "save_chat_notion": "💾 チャット全体をNotionに保存",
        "save_chat_notion_success": "チャット内容がNotionに保存されました。",
        "chat_input_placeholder": "動画内容について質問してください...",
        "chat_send_btn": "送信",
        "chat_welcome": "👋 こんにちは！この動画要約をもとに自由に質問してください。",
        "chat_loading": "AIが回答を生成しています...",
        "transcript_fallback": "デフォルトの字幕抽出に失敗、バックアップ方式で再試行します。",
        "transcript_fail": "字幕抽出に失敗しました",
        "summary_error": "⚠️ 要約生成中にエラーが発生しました",
        "overall_summary_error": "⚠️ 全体要約生成中にエラーが発生しました",
        "openai_import_error": "langchain-openaiパッケージがインストールされていません。pip install langchain-openai を実行してください。",
        "unsupported_model": "サポートされていないモデルです。",
        "summary_fail": "⚠️ 要約生成に失敗しました。入力テキストを確認してください。",
        "sectionwise_done": "✅ セクションごとの要約が完了しました！次に全体要約を生成します。",
        "overall_summary_done": "✅ 全体要約の生成が完了しました！",
        "gemini_quota_exceeded": "⚠️ Google Generative AI APIの利用上限を超えました。しばらくしてから再試行するか、APIの割り当てを確認してください。",
        "openai_summary_error": "⚠️ OpenAI要約生成中にエラーが発生しました",
        # === 字幕処理プロセスメッセージ ===
        "transcript_apify_try": "⚡ [ステップ1] Apify字幕取得を試行中",
        "transcript_apify_success": "🟢 [ステップ1] Apify字幕取得成功",
        "transcript_apify_fail": "⚠️ [ステップ1] Apify字幕失敗、Whisperを試行",
        "transcript_audio_download_try": "⏬ [ステップ2] 音声ダウンロード中",
        "transcript_audio_download_fail": "⚠️ [ステップ2] 音声ダウンロード失敗",
        "transcript_audio_too_large": "⚠️ [ステップ2] 音声ファイルが25MBを超えています",
        "transcript_whisper_try": "🔊⏳ [ステップ3] Whisper書き起こし開始 - 数分かかる場合があります。",
        "transcript_whisper_fail": "⚠️ [ステップ3] Whisper書き起こし失敗",
        "transcript_whisper_no_result": "⚠️ [ステップ3] Whisperから結果なし",
        "transcript_whisper_success": "✅ [ステップ3] Whisper書き起こし成功",
    },
    "zh": {
        "app_title": "YouTube 字幕摘要服务",
        "sidebar_title": "⚙️ 设置面板",
        "model_provider": "选择模型提供者:",
        "model_select": "选择摘要模型:",
        "lang_select": "选择摘要语言:",
        "lang_display": lambda x: x.split(" ")[1],
        "yt_input": "输入YouTube链接",
        "yt_input_placeholder": "https://www.youtube.com/watch?v=...",
        "invalid_yt": "无效的YouTube链接。",
        "notion_settings": "⚙️ Notion设置输入",
        "notion_token": "🔑 Notion API令牌",
        "notion_token_placeholder": "ntn_...",
        "notion_db": "📄 Notion数据库URL或ID",
        "notion_db_placeholder": "URL或32位ID",
        "notion_save_btn": "✅ OK - 保存设置",
        "notion_save_success": "✅ Notion设置已保存。",
        "notion_save_fail": "📄 数据库URL/ID格式不正确。",
        "notion_token_fail": "🔑 令牌必须以 'ntn_' 或 'secret_' 开头。",
        "notion_field_warn": "⚠️ 所有字段均为必填项。",
        "auto_save": "✅ 摘要后自动保存到Notion",
        "summary_tab": "摘要",
        "section_tab": "分段摘要",
        "chat_tab": "AI聊天",
        "summarize_btn": "生成字幕摘要",
        "sectionwise_btn": "生成分段摘要",
        "summary_download": "下载摘要笔记",
        "sectionwise_download": "下载分段摘要",
        "notion_save_summary": "保存到Notion",
        "notion_save_sectionwise": "保存到Notion",
        "original_transcript": "原始字幕",
        "summary_expander": "🔍 查看摘要结果",
        "sectionwise_expander": "🔍 查看分段摘要结果",
        "summarizing": "正在生成摘要…",
        "sectionwise_summarizing": "正在生成分段摘要…",
        "notion_saved": "聊天内容已保存到Notion。",
        "api_key_warning": "请先在.env文件中注册 {}。",
        "missing_api_key": "⚠️ 未设置 {} API密钥。",
        "missing_data": "⚠️ 缺少必要数据: {}",
        "memory_info": "💭 内存: {}条消息",
        "reset_chat": "重置聊天记录",
        "reset_chat_msg": "👋 聊天记录已重置。请提出新问题！",
        "streaming_response": "使用流式响应",
        "suggested_questions": "💡 推荐问题:",
        "save_chat_notion": "💾 保存全部聊天到Notion",
        "save_chat_notion_success": "聊天内容已保存到Notion。",
        "chat_input_placeholder": "请就视频内容提问...",
        "chat_send_btn": "发送",
        "chat_welcome": "👋 您好！欢迎基于本视频摘要自由提问。",
        "chat_loading": "AI正在生成回答...",
        "transcript_fallback": "默认字幕提取失败，正在使用备用方式重试。",
        "transcript_fail": "字幕提取失败",
        "summary_error": "⚠️ 摘要生成时发生错误",
        "overall_summary_error": "⚠️ 整体摘要生成时发生错误",
        "openai_import_error": "未安装langchain-openai包。请运行 pip install langchain-openai。",
        "unsupported_model": "不支持的模型。",
        "summary_fail": "⚠️ 摘要生成失败。请检查输入文本。",
        "sectionwise_done": "✅ 分段摘要完成！现在生成整体摘要。",
        "overall_summary_done": "✅ 整体摘要生成完成！",
        "gemini_quota_exceeded": "⚠️ Google Generative AI API配额已超出。请稍后再试或检查API配额。",
        "openai_summary_error": "⚠️ OpenAI摘要生成时发生错误",
        # === 字幕处理流程消息 ===
        "transcript_apify_try": "⚡ [步骤1] 正在尝试Apify字幕",
        "transcript_apify_success": "🟢 [步骤1] Apify字幕成功",
        "transcript_apify_fail": "⚠️ [步骤1] Apify字幕失败，尝试Whisper",
        "transcript_audio_download_try": "⏬ [步骤2] 正在下载音频",
        "transcript_audio_download_fail": "⚠️ [步骤2] 音频下载失败",
        "transcript_audio_too_large": "⚠️ [步骤2] 音频文件超过25MB",
        "transcript_whisper_try": "🔊⏳ [步骤3] 开始Whisper转录（语音识别），可能需要几分钟。",
        "transcript_whisper_fail": "⚠️ [步骤3] Whisper转录失败",
        "transcript_whisper_no_result": "⚠️ [步骤3] Whisper无结果",
        "transcript_whisper_success": "✅ [步骤3] Whisper转录成功",
    },
    "fr": {
        "app_title": "Service de résumé de transcription YouTube",
        "sidebar_title": "⚙️ Panneau de configuration",
        "model_provider": "Sélectionner le fournisseur de modèle :",
        "model_select": "Sélectionner le modèle de résumé :",
        "lang_select": "Sélectionner la langue du résumé :",
        "lang_display": lambda x: x.split(" ")[1],
        "yt_input": "Entrer le lien YouTube",
        "yt_input_placeholder": "https://www.youtube.com/watch?v=...",
        "invalid_yt": "Lien YouTube invalide.",
        "notion_settings": "⚙️ Paramètres Notion",
        "notion_token": "🔑 Jeton API Notion",
        "notion_token_placeholder": "ntn_...",
        "notion_db": "📄 URL ou ID de la base Notion",
        "notion_db_placeholder": "URL ou ID de 32 caractères",
        "notion_save_btn": "✅ OK - Enregistrer les paramètres",
        "notion_save_success": "✅ Paramètres Notion enregistrés.",
        "notion_save_fail": "📄 Format d'URL/ID de base invalide.",
        "notion_token_fail": "🔑 Le jeton doit commencer par 'ntn_' ou 'secret_'.",
        "notion_field_warn": "⚠️ Tous les champs sont obligatoires.",
        "auto_save": "✅ Sauvegarde automatique dans Notion après résumé",
        "summary_tab": "Résumé",
        "section_tab": "Résumé par section",
        "chat_tab": "Chat IA",
        "summarize_btn": "Résumer la transcription",
        "sectionwise_btn": "Générer un résumé par section",
        "summary_download": "Télécharger la note de résumé",
        "sectionwise_download": "Télécharger le résumé par section",
        "notion_save_summary": "Enregistrer dans Notion",
        "notion_save_sectionwise": "Enregistrer dans Notion",
        "original_transcript": "Transcription originale",
        "summary_expander": "🔍 Voir le résultat du résumé",
        "sectionwise_expander": "🔍 Voir le résumé par section",
        "summarizing": "Génération du résumé…",
        "sectionwise_summarizing": "Génération du résumé par section…",
        "notion_saved": "Chat enregistré dans Notion.",
        "api_key_warning": "Veuillez d'abord enregistrer {} dans votre fichier .env.",
        "missing_api_key": "⚠️ La clé API {} n'est pas définie.",
        "missing_data": "⚠️ Données requises manquantes : {}",
        "memory_info": "💭 Mémoire : {} messages",
        "reset_chat": "Réinitialiser l'historique du chat",
        "reset_chat_msg": "👋 Historique du chat réinitialisé. Posez une nouvelle question !",
        "streaming_response": "Utiliser la réponse en streaming",
        "suggested_questions": "💡 Questions suggérées :",
        "save_chat_notion": "💾 Enregistrer tout le chat dans Notion",
        "save_chat_notion_success": "Chat enregistré dans Notion.",
        "chat_input_placeholder": "Posez vos questions sur le contenu de la vidéo...",
        "chat_send_btn": "Envoyer",
        "chat_welcome": "👋 Bonjour ! N'hésitez pas à poser vos questions sur ce résumé vidéo.",
        "chat_loading": "L'IA génère une réponse...",
        "transcript_fallback": "Échec de l'extraction par défaut, nouvelle tentative avec la méthode de secours.",
        "transcript_fail": "Échec de l'extraction de la transcription",
        "summary_error": "⚠️ Une erreur est survenue lors de la génération du résumé",
        "overall_summary_error": "⚠️ Une erreur est survenue lors de la génération du résumé global",
        "openai_import_error": "Le package langchain-openai n'est pas installé. Veuillez installer avec pip install langchain-openai.",
        "unsupported_model": "Modèle non pris en charge.",
        "summary_fail": "⚠️ Échec de la génération du résumé. Veuillez vérifier le texte d'entrée.",
        "sectionwise_done": "✅ Résumé par section terminé ! Génération du résumé global.",
        "overall_summary_done": "✅ Résumé global généré !",
        "gemini_quota_exceeded": "⚠️ Quota Google Generative AI API dépassé. Veuillez réessayer plus tard ou vérifier votre quota.",
        "openai_summary_error": "⚠️ Erreur lors de la génération du résumé OpenAI",
        # === Messages de processus de transcription ===
        "transcript_apify_try": "⚡ [Étape 1] Tentative de transcription Apify",
        "transcript_apify_success": "🟢 [Étape 1] Transcription Apify réussie",
        "transcript_apify_fail": "⚠️ [Étape 1] Échec Apify, tentative Whisper",
        "transcript_audio_download_try": "⏬ [Étape 2] Téléchargement audio",
        "transcript_audio_download_fail": "⚠️ [Étape 2] Échec du téléchargement audio",
        "transcript_audio_too_large": "⚠️ [Étape 2] Fichier audio > 25 Mo",
        "transcript_whisper_try": "🔊⏳ [Étape 3] Transcription Whisper (reconnaissance vocale) en cours - cela peut prendre plusieurs minutes.",
        "transcript_whisper_fail": "⚠️ [Étape 3] Échec de la transcription Whisper",
        "transcript_whisper_no_result": "⚠️ [Étape 3] Aucun résultat de Whisper",
        "transcript_whisper_success": "✅ [Étape 3] Transcription Whisper réussie",
    },
    "de": {
        "app_title": "YouTube Transkript-Zusammenfassung",
        "sidebar_title": "⚙️ Einstellungsfeld",
        "model_provider": "Modellanbieter auswählen:",
        "model_select": "Zusammenfassungsmodell auswählen:",
        "lang_select": "Zusammenfassungssprache auswählen:",
        "lang_display": lambda x: x.split(" ")[1],
        "yt_input": "YouTube-Link eingeben",
        "yt_input_placeholder": "https://www.youtube.com/watch?v=...",
        "invalid_yt": "Ungültiger YouTube-Link.",
        "notion_settings": "⚙️ Notion-Einstellungen",
        "notion_token": "🔑 Notion API-Token",
        "notion_token_placeholder": "ntn_...",
        "notion_db": "📄 Notion-Datenbank-URL oder ID",
        "notion_db_placeholder": "URL oder 32-stellige ID",
        "notion_save_btn": "✅ OK - Einstellungen speichern",
        "notion_save_success": "✅ Notion-Einstellungen gespeichert.",
        "notion_save_fail": "📄 Ungültiges DB-URL/ID-Format.",
        "notion_token_fail": "🔑 Token muss mit 'ntn_' oder 'secret_' beginnen.",
        "notion_field_warn": "⚠️ Alle Felder sind erforderlich.",
        "auto_save": "✅ Nach Zusammenfassung automatisch in Notion speichern",
        "summary_tab": "Zusammenfassung",
        "section_tab": "Abschnittsweise Zusammenfassung",
        "chat_tab": "KI-Chat",
        "summarize_btn": "Transkript zusammenfassen",
        "sectionwise_btn": "Abschnittsweise Zusammenfassung generieren",
        "summary_download": "Zusammenfassungsnotiz herunterladen",
        "sectionwise_download": "Abschnittsweise Zusammenfassung herunterladen",
        "notion_save_summary": "In Notion speichern",
        "notion_save_sectionwise": "In Notion speichern",
        "original_transcript": "Originaltranskript",
        "summary_expander": "🔍 Zusammenfassungsergebnis anzeigen",
        "sectionwise_expander": "🔍 Abschnittsweise Zusammenfassung anzeigen",
        "summarizing": "Zusammenfassung wird erstellt…",
        "sectionwise_summarizing": "Abschnittsweise Zusammenfassung wird erstellt…",
        "notion_saved": "Chat in Notion gespeichert.",
        "api_key_warning": "Bitte registrieren Sie {} zuerst in Ihrer .env-Datei.",
        "missing_api_key": "⚠️ {} API-Schlüssel ist nicht gesetzt.",
        "missing_data": "⚠️ Fehlende erforderliche Daten: {}",
        "memory_info": "💭 Speicher: {} Nachrichten",
        "reset_chat": "Chatverlauf zurücksetzen",
        "reset_chat_msg": "👋 Chatverlauf zurückgesetzt. Bitte stellen Sie eine neue Frage!",
        "streaming_response": "Streaming-Antwort verwenden",
        "suggested_questions": "💡 Vorgeschlagene Fragen:",
        "save_chat_notion": "💾 Gesamten Chat in Notion speichern",
        "save_chat_notion_success": "Chat in Notion gespeichert.",
        "chat_input_placeholder": "Stellen Sie Fragen zum Videoinhalt...",
        "chat_send_btn": "Senden",
        "chat_welcome": "👋 Hallo! Stellen Sie gerne Fragen basierend auf dieser Videozusammenfassung.",
        "chat_loading": "KI generiert eine Antwort...",
        "transcript_fallback": "Standard-Transkriptextraktion fehlgeschlagen, erneuter Versuch mit Backup-Methode.",
        "transcript_fail": "Transkriptextraktion fehlgeschlagen",
        "summary_error": "⚠️ Fehler bei der Zusammenfassungserstellung",
        "overall_summary_error": "⚠️ Fehler bei der Gesamterstellung der Zusammenfassung",
        "openai_import_error": "langchain-openai-Paket ist nicht installiert. Bitte mit pip install langchain-openai installieren.",
        "unsupported_model": "Nicht unterstütztes Modell.",
        "summary_fail": "⚠️ Zusammenfassung konnte nicht erstellt werden. Bitte überprüfen Sie den Eingabetext.",
        "sectionwise_done": "✅ Abschnittsweise Zusammenfassung abgeschlossen! Jetzt wird die Gesamtzusammenfassung erstellt.",
        "overall_summary_done": "✅ Gesamte Zusammenfassung abgeschlossen!",
        "gemini_quota_exceeded": "⚠️ Google Generative AI API-Kontingent überschritten. Bitte versuchen Sie es später erneut oder überprüfen Sie Ihr API-Kontingent.",
        "openai_summary_error": "⚠️ Fehler bei der OpenAI-Zusammenfassungserstellung",
        # === Transkriptprozess-Meldungen ===
        "transcript_apify_try": "⚡ [Schritt 1] Apify-Transkript wird versucht",
        "transcript_apify_success": "🟢 [Schritt 1] Apify-Transkript erfolgreich",
        "transcript_apify_fail": "⚠️ [Schritt 1] Apify-Transkript fehlgeschlagen, Whisper wird versucht",
        "transcript_audio_download_try": "⏬ [Schritt 2] Audio wird heruntergeladen",
        "transcript_audio_download_fail": "⚠️ [Schritt 2] Audio-Download fehlgeschlagen",
        "transcript_audio_too_large": "⚠️ [Schritt 2] Audiodatei > 25MB",
        "transcript_whisper_try": "🔊⏳ [Schritt 3] Whisper-Transkription (Spracherkennung) gestartet – dies kann mehrere Minuten dauern.",
        "transcript_whisper_fail": "⚠️ [Schritt 3] Whisper-Transkription fehlgeschlagen",
        "transcript_whisper_no_result": "⚠️ [Schritt 3] Kein Ergebnis von Whisper",
        "transcript_whisper_success": "✅ [Schritt 3] Whisper-Transkription erfolgreich",
    },
    "es": {
        "app_title": "Servicio de resumen de transcripciones de YouTube",
        "sidebar_title": "⚙️ Panel de configuración",
        "model_provider": "Seleccionar proveedor de modelo:",
        "model_select": "Seleccionar modelo de resumen:",
        "lang_select": "Seleccionar idioma del resumen:",
        "lang_display": lambda x: x.split(" ")[1],
        "yt_input": "Introducir enlace de YouTube",
        "yt_input_placeholder": "https://www.youtube.com/watch?v=...",
        "invalid_yt": "Enlace de YouTube no válido.",
        "notion_settings": "⚙️ Configuración de Notion",
        "notion_token": "🔑 Token de API de Notion",
        "notion_token_placeholder": "ntn_...",
        "notion_db": "📄 URL o ID de la base de datos de Notion",
        "notion_db_placeholder": "URL o ID de 32 caracteres",
        "notion_save_btn": "✅ OK - Guardar configuración",
        "notion_save_success": "✅ Configuración de Notion guardada.",
        "notion_save_fail": "📄 Formato de URL/ID de base de datos no válido.",
        "notion_token_fail": "🔑 El token debe comenzar con 'ntn_' o 'secret_'.",
        "notion_field_warn": "⚠️ Todos los campos son obligatorios.",
        "auto_save": "✅ Guardar automáticamente en Notion después del resumen",
        "summary_tab": "Resumen",
        "section_tab": "Resumen por secciones",
        "chat_tab": "Chat IA",
        "summarize_btn": "Resumir transcripción",
        "sectionwise_btn": "Generar resumen por secciones",
        "summary_download": "Descargar nota de resumen",
        "sectionwise_download": "Descargar resumen por secciones",
        "notion_save_summary": "Guardar en Notion",
        "notion_save_sectionwise": "Guardar en Notion",
        "original_transcript": "Transcripción original",
        "summary_expander": "🔍 Ver resultado del resumen",
        "sectionwise_expander": "🔍 Ver resumen por secciones",
        "summarizing": "Generando resumen…",
        "sectionwise_summarizing": "Generando resumen por secciones…",
        "notion_saved": "Chat guardado en Notion.",
        "api_key_warning": "Por favor, registre {} primero en su archivo .env.",
        "missing_api_key": "⚠️ No se ha establecido la clave API de {}.",
        "missing_data": "⚠️ Faltan datos requeridos: {}",
        "memory_info": "💭 Memoria: {} mensajes",
        "reset_chat": "Restablecer historial de chat",
        "reset_chat_msg": "👋 Historial de chat restablecido. ¡Haz una nueva pregunta!",
        "streaming_response": "Usar respuesta en streaming",
        "suggested_questions": "💡 Preguntas sugeridas:",
        "save_chat_notion": "💾 Guardar todo el chat en Notion",
        "save_chat_notion_success": "Chat guardado en Notion.",
        "chat_input_placeholder": "Pregunta cualquier cosa sobre el contenido del video...",
        "chat_send_btn": "Enviar",
        "chat_welcome": "👋 ¡Hola! Siéntete libre de preguntar cualquier cosa basada en este resumen de video.",
        "chat_loading": "La IA está generando una respuesta...",
        "transcript_fallback": "La extracción predeterminada de la transcripción falló, reintentando con el método de respaldo.",
        "transcript_fail": "Error al extraer la transcripción",
        "summary_error": "⚠️ Error durante la generación del resumen",
        "overall_summary_error": "⚠️ Error durante la generación del resumen general",
        "openai_import_error": "El paquete langchain-openai no está instalado. Instale con pip install langchain-openai.",
        "unsupported_model": "Modelo no soportado.",
        "summary_fail": "⚠️ Error al generar el resumen. Por favor, revise el texto de entrada.",
        "sectionwise_done": "✅ Resumen por secciones completado. Ahora generando el resumen general.",
        "overall_summary_done": "✅ ¡Resumen general completado!",
        "gemini_quota_exceeded": "⚠️ Se ha superado la cuota de la API de Google Generative AI. Inténtelo de nuevo más tarde o revise su cuota.",
        "openai_summary_error": "⚠️ Error durante la generación del resumen de OpenAI",
        # === Mensajes del proceso de transcripción ===
        "transcript_apify_try": "⚡ [Paso 1] Intentando transcripción con Apify",
        "transcript_apify_success": "🟢 [Paso 1] Transcripción de Apify exitosa",
        "transcript_apify_fail": "⚠️ [Paso 1] Falló Apify, intentando Whisper",
        "transcript_audio_download_try": "⏬ [Paso 2] Descargando audio",
        "transcript_audio_download_fail": "⚠️ [Paso 2] Falló la descarga de audio",
        "transcript_audio_too_large": "⚠️ [Paso 2] Archivo de audio > 25MB",
        "transcript_whisper_try": "🔊⏳ [Paso 3] Iniciando transcripción Whisper (voz a texto), esto puede tardar varios minutos.",
        "transcript_whisper_fail": "⚠️ [Paso 3] Falló la transcripción de Whisper",
        "transcript_whisper_no_result": "⚠️ [Paso 3] Sin resultado de Whisper",
        "transcript_whisper_success": "✅ [Paso 3] Transcripción de Whisper exitosa",
    },
}
