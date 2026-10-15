from __future__ import annotations

from html import escape
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1] / "docs" / "boxwhere"
STORE = "https://apps.apple.com/app/id6818778988"
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
EMAIL = "wf8.8@qq.com"

# Each entry is a complete customer-facing localization of the four public pages.
DATA = {
"zh-Hans": {
  "folder":"", "html":"zh-CN", "language":"简体中文", "brand":"箱里 · CrateNote",
  "nav":["首页","隐私政策","技术支持","使用条款","语言"], "updated":"更新于 2026-10-15", "store":"在 App Store 查看", "eula":"Apple 标准最终用户许可协议",
  "home": {"title":"箱里：搬家和收纳，东西放哪一搜就知道", "lead":"给箱子编号，记下物品、数量和可选照片。搬家后搜索名称、备注或箱号，马上知道要打开哪只箱子。", "sections":[
    ["当前版本", "目前 App Store 提供 1.0：箱子与物品清单、备注和可选照片、搬家清单、PDF 清单与标签，以及本机备份和恢复。应用无需注册，没有广告或订阅；价格以 App Store 页面为准。"],
    ["2.0 更新准备中", "2.0 版本草稿新增位置层级、设备端照片与语音录入、物品图谱、最近删除恢复和开箱视频。只有更新获 Apple 批准并发布后，这些功能才会提供；请以 App Store 当前版本为准。"]]},
  "privacy": {"title":"隐私政策", "lead":"本政策说明箱里 / CrateNote 如何处理应用数据和本网站请求信息。", "sections":[
    ["更新日期与范围", "更新日期：2026-10-15。政策覆盖 CrateNote iOS App 及本网站。功能会随版本变化；以下内容说明目前 1.0 与正在准备的 2.0。"],
    ["本机记录", "物品、位置、备注、清单和照片保存在设备上的 App 数据中。开发者没有用于收集这些内容的服务器，也不使用广告、分析或追踪 SDK。iOS 设备备份是否包含 App 数据由系统设置决定。"],
    ["照片与相机", "系统照片选择器只向 App 提供你主动选中的图片，不请求完整相册访问权限；仅在你选择拍照时请求相机权限。1.0 中主动附加的照片保存在本机。2.0 的照片识别在设备端完成，原图默认不保留；你可选择为每件物品保留约 60 KB 的压缩缩略图。照片不会发送到开发者服务器。"],
    ["语音与视频", "如果你使用的版本包含这些功能，语音识别强制在设备端进行，不上传或保存录音；设备不支持离线识别时，App 会提示改用打字或照片。开箱视频最长 30 秒，保存在本机且不包含在 App 导出的备份中。"],
    ["导出、分享与删除", "你主动导出的备份和 PDF 会包含所选记录；接收方或你选择的云端文件服务可能取得这些内容。二维码只含本机记录 ID，不提供远程查询。2.0 删除的记录保留 30 天供恢复；卸载 App 会删除本机数据和安全快照。系统备份及导出文件需自行管理。"],
    ["外部服务与联系", "Apple 处理 App Store 购买和退款请求。本网站由 GitHub Pages 托管；GitHub 的隐私说明称其可能处理 IP 地址、设备及访问日志等服务使用信息。发送支持邮件会向支持方提供邮件中包含的信息，请勿发送密码或不必要的私人资料。"]]},
  "support": {"title":"技术支持", "lead":"需要帮助时，请先查看下面的常见问题。", "sections":[
    ["联系支持", f"支持邮箱：{EMAIL}。请写明设备型号、iOS 版本、App 版本、问题和复现步骤。除非排查确有需要，请勿发送物品照片、完整备份或密码。"],
    ["怎么找到物品？", "1.0 在箱子页可按物品名称、箱号或备注搜索；如果没有结果，清除筛选条件再试。较新的版本还可按位置搜索并查看完整位置路径。"],
    ["拍照识别和照片", "在支持该功能的版本中，可拍照或从系统照片选择器选图，检查并编辑识别建议后再保存。识别在设备端完成；原图默认不保留。系统设置可调整相机权限。"],
    ["语音录入", "语音功能需要麦克风和语音识别权限，并只使用设备端识别。若设备不支持离线识别，请改用打字或拍照；App 不会切换到联网识别。"],
    ["换设备或恢复备份", "在旧设备把备份导出到“文件”，再在新设备导入。导入前会要求确认替换当前数据，并先保留安全副本。开箱视频不在导出备份内，需要在新设备重新录制。"],
    ["文件无法读取", "App 会保护无法读取的原文件，避免用空数据覆盖。先在设置中导出原文件留存，再导入有效备份恢复。"],
    ["购买与退款", "购买和退款由 Apple 处理。请在 Apple 购买记录中查看订单，或访问 reportaproblem.apple.com 申请退款。"]]},
  "terms": {"title":"使用条款", "lead":"使用箱里 / CrateNote 即表示你同意遵守适用的 App Store 使用条款。", "sections":[
    ["用途与版本", "CrateNote 是个人搬家与居家收纳记录工具。功能以你安装的版本为准；当前 1.0 已在 App Store 提供，2.0 功能只有在 Apple 批准并发布后才会提供。搬家清单仅作一般提醒，不替代专业意见、搬运安排或合同。"],
    ["数据与备份", "记录默认保存在你的设备上。请在换机、卸载、删除或恢复数据前导出备份。你负责选择分享内容、接收方及外部存储位置。设备故障、系统恢复或外部文件丢失后，数据未必可以恢复。"],
    ["购买", "应用通过 App Store 一次性付费下载，不含订阅或应用内功能付费。实际价格、付款、退款和购买记录以 Apple 商店页面与规则为准。"],
    ["标签与服务限制", "箱号、易碎等标签是给你自己的记录提示，不保证搬运方按标签处理。请勿把应用作为专业搬家或安全建议的替代品。"],
    ["许可与消费者权利", "Apple 标准最终用户许可协议适用于本 App；本页不限制适用法律赋予你的消费者权利。"]]},
},
"en-US": {
  "folder":"en", "html":"en", "language":"English", "brand":"CrateNote",
  "nav":["Home","Privacy","Support","Terms","Language"], "updated":"Updated October 15, 2026", "store":"View on the App Store", "eula":"Apple Standard End User License Agreement",
  "home": {"title":"CrateNote: know what is in every box", "lead":"Number boxes and record items, quantities, notes, and optional photos. Search by item, note, or box number to know what to open.", "sections":[
    ["Available version", "Version 1.0 is currently on the App Store. It includes box and item lists, notes and optional photos, a moving checklist, PDF lists and labels, and local backup and restore. No account, ads, or subscriptions. See the App Store for the current price."],
    ["Version 2.0 in preparation", "The 2.0 draft adds a place hierarchy, on-device photo and speech entry, an item graph, recently deleted recovery, and unboxing clips. These features will be available only if Apple approves and releases the update. Check the App Store for the version currently available."]]},
  "privacy": {"title":"Privacy policy", "lead":"This policy explains how CrateNote handles app data and information from visits to this website.", "sections":[
    ["Updated and scope", "Updated October 15, 2026. This policy covers the CrateNote iOS app and this website. Features vary by version; this policy describes version 1.0 and the 2.0 update in preparation."],
    ["Records on your device", "Items, places, notes, checklists, and photos are stored in app data on your device. The developer has no server used to collect this content and the app has no advertising, analytics, or tracking SDKs. Whether an iOS device backup includes app data depends on your system settings."],
    ["Photos and camera", "The system photo picker provides only images you select; the app does not request full photo-library access. Camera permission is requested only when you choose to take a photo. Photos you attach in version 1.0 stay on your device. Version 2.0 photo recognition runs on device; the original image is not kept by default, and you may choose to keep a compressed thumbnail of about 60 KB per item. Photos are not sent to developer servers."],
    ["Speech and video", "If included in your app version, speech recognition is forced to run on device; audio is not uploaded or saved. If offline recognition is unavailable, the app asks you to type or use a photo. Unboxing clips are up to 30 seconds, stay on your device, and are not included in app-exported backups."],
    ["Exports, sharing, and deletion", "Backups and PDFs you choose to export contain the selected records. Recipients or cloud file services you choose may receive that content. QR codes contain only a local record ID and do not provide remote lookup. Version 2.0 keeps deleted records for 30 days for recovery. Uninstalling removes local app data and safety copies; manage system backups and exported files separately."],
    ["External services and contact", "Apple handles App Store purchases and refund requests. This website is hosted on GitHub Pages; GitHub’s privacy statement says it may process IP addresses, device details, and website usage logs as service usage information. Emailing support shares the information in your message. Do not send passwords or unnecessary private information."]]},
  "support": {"title":"Support", "lead":"Try these answers first. If you still need help, email support.", "sections":[
    ["Contact", f"Support email: {EMAIL}. Include your device model, iOS version, app version, the issue, and steps to reproduce it. Do not send item photos, a full backup, or passwords unless they are strictly needed to resolve the issue."],
    ["Finding an item", "In version 1.0, search by item name, box number, or note on the Boxes tab. Clear filters if no results appear. Newer versions can also search places and show the full place path."],
    ["Photo recognition and photos", "In versions with this feature, take a photo or select one with the system photo picker, then review and edit suggestions before saving. Recognition runs on device and the original image is not kept by default. Change camera permission in system Settings."],
    ["Speech entry", "Speech entry needs microphone and speech recognition permission and uses on-device recognition only. If your device does not support offline recognition, type the item or use a photo; the app does not switch to online recognition."],
    ["Moving or restoring a backup", "Export a backup to Files on the old device and import it on the new one. The app asks before replacing current data and keeps a safety copy first. Unboxing clips are not in exported backups and must be recorded again on the new device."],
    ["A file cannot be read", "The app protects an unreadable original file instead of overwriting it with empty data. Export the original from Settings, then restore a valid backup."],
    ["Purchases and refunds", "Apple handles purchases and refunds. Check your Apple purchase history or visit reportaproblem.apple.com to request a refund."]]},
  "terms": {"title":"Terms of use", "lead":"Use of CrateNote is subject to the applicable App Store terms.", "sections":[
    ["Purpose and app versions", "CrateNote is a personal moving and home-storage record tool. Features depend on the version installed. Version 1.0 is on the App Store; version 2.0 features will be available only if Apple approves and releases that update. The checklist is for general reminders, not professional advice or a substitute for moving arrangements or contracts."],
    ["Your data and backups", "Records are stored on your device by default. Export a backup before changing devices, uninstalling, deleting, or restoring data. You choose what to share, with whom, and where to store it. Data may not be recoverable after device failure, a system restore, or loss of an external file."],
    ["Purchases", "The app is a one-time paid download from the App Store, with no subscription or in-app feature purchases. Apple’s storefront shows the applicable price and handles payment, refunds, and purchase history."],
    ["Labels and service limits", "Box numbers and labels such as Fragile are reminders for your own records; they do not guarantee how a carrier handles a box. Do not treat the app as professional moving or safety advice."],
    ["License and consumer rights", "Apple’s Standard End User License Agreement applies to the app. Nothing on this page limits consumer rights provided by applicable law."]]},
},
"zh-Hant": {
  "folder":"zh-Hant", "html":"zh-Hant", "language":"繁體中文", "brand":"箱裡 · CrateNote",
  "nav":["首頁","隱私權","技術支援","使用條款","語言"], "updated":"更新日期：2026-10-15", "store":"前往 App Store", "eula":"Apple 標準終端使用者授權協議",
  "home": {"title":"箱裡：搬家與收納，東西放哪一搜就知道", "lead":"替箱子編號，記下物品、數量與可選照片。搬家後搜尋名稱、備註或箱號，立刻知道要打開哪個箱子。", "sections":[
    ["目前版本", "App Store 目前提供 1.0：箱子與物品清單、備註與可選照片、搬家清單、PDF 清單與標籤，以及本機備份與還原。無須註冊，沒有廣告或訂閱；價格請以 App Store 頁面為準。"],
    ["2.0 更新準備中", "2.0 草稿新增位置階層、裝置端照片與語音輸入、物品圖譜、最近刪除還原及開箱影片。只有在更新獲 Apple 核准並發布後，這些功能才會提供；請以 App Store 目前版本為準。"]]},
  "privacy": {"title":"隱私權政策", "lead":"本政策說明箱裡 / CrateNote 如何處理 App 資料及本網站的瀏覽資訊。", "sections":[
    ["更新日期與適用範圍", "更新日期：2026-10-15。本政策適用於 CrateNote iOS App 及本網站。功能依版本而異；以下說明目前的 1.0 與準備中的 2.0。"],
    ["裝置上的記錄", "物品、位置、備註、清單和照片儲存在裝置上的 App 資料中。開發者沒有用來收集這些內容的伺服器，也不使用廣告、分析或追蹤 SDK。iOS 裝置備份是否包含 App 資料，取決於系統設定。"],
    ["照片與相機", "系統照片選擇器只提供你主動選取的圖片；App 不會要求完整相簿存取權。只有在你選擇拍照時才會要求相機權限。1.0 中主動附加的照片會儲存在本機。2.0 照片辨識在裝置端完成，原始照片預設不保留；你可選擇為每件物品保留約 60 KB 的壓縮縮圖。照片不會傳送到開發者伺服器。"],
    ["語音與影片", "如果你使用的版本含有這些功能，語音辨識會強制在裝置端執行，不會上傳或儲存錄音；裝置不支援離線辨識時，App 會請你改用打字或照片。開箱影片最長 30 秒，儲存在本機，不包含於 App 匯出的備份。"],
    ["匯出、分享與刪除", "你主動匯出的備份和 PDF 會包含所選記錄；接收者或你選擇的雲端檔案服務可能取得這些內容。QR Code 只包含本機記錄 ID，無法遠端查詢。2.0 刪除的記錄會保留 30 天供還原。解除安裝會刪除本機 App 資料與安全副本；系統備份和匯出檔案請自行管理。"],
    ["外部服務與聯絡", "Apple 處理 App Store 購買及退款申請。本網站由 GitHub Pages 託管；GitHub 隱私聲明指出，服務可能處理 IP 位址、裝置資訊和網站瀏覽記錄等服務使用資訊。寄送支援郵件會提供郵件中的資訊，請勿寄送密碼或不必要的私人資料。"]]},
  "support": {"title":"技術支援", "lead":"遇到問題時，請先查看以下常見解答。", "sections":[
    ["聯絡支援", f"支援信箱：{EMAIL}。請提供裝置型號、iOS 版本、App 版本、問題內容和重現步驟。除非排查確實需要，請勿傳送物品照片、完整備份或密碼。"],
    ["如何找到物品？", "1.0 可在箱子頁依物品名稱、箱號或備註搜尋。若沒有結果，請先清除篩選條件。較新的版本也能搜尋位置並查看完整位置路徑。"],
    ["照片辨識與照片", "在支援此功能的版本中，可拍照或使用系統照片選擇器選取照片，確認並編輯辨識建議後再儲存。辨識在裝置端完成，原始照片預設不保留。可在系統設定調整相機權限。"],
    ["語音輸入", "語音輸入需要麥克風與語音辨識權限，且只使用裝置端辨識。如果裝置不支援離線辨識，請改用打字或拍照；App 不會改用網路辨識。"],
    ["更換裝置或還原備份", "在舊裝置將備份匯出到「檔案」，再於新裝置匯入。替換目前資料前會先請你確認，並保留安全副本。開箱影片不在匯出的備份中，需在新裝置重新錄製。"],
    ["檔案無法讀取", "App 會保護無法讀取的原始檔，避免用空資料覆蓋。請先在設定中匯出原始檔，再匯入有效備份還原。"],
    ["購買與退款", "Apple 處理購買與退款。請查看 Apple 購買記錄，或前往 reportaproblem.apple.com 申請退款。"]]},
  "terms": {"title":"使用條款", "lead":"使用箱裡 / CrateNote 即表示你同意遵守適用的 App Store 條款。", "sections":[
    ["用途與版本", "CrateNote 是個人搬家與居家收納記錄工具。功能依安裝的版本而異。1.0 已在 App Store 上架；2.0 功能只有在 Apple 核准並發布更新後才會提供。清單只提供一般提醒，不取代專業建議、搬運安排或合約。"],
    ["資料與備份", "記錄預設儲存在你的裝置上。更換裝置、解除安裝、刪除或還原資料前，請先匯出備份。由你選擇分享內容、接收者和外部儲存位置。裝置故障、系統還原或外部檔案遺失後，資料可能無法復原。"],
    ["購買", "App 透過 App Store 一次性付費下載，不含訂閱或 App 內功能付費。實際價格、付款、退款及購買記錄以 Apple 商店頁面與規則為準。"],
    ["標籤與服務限制", "箱號、易碎等標籤是個人記錄提示，不保證搬運業者會依標籤處理。請勿將 App 當成專業搬家或安全建議。"],
    ["授權與消費者權利", "本 App 適用 Apple 標準終端使用者授權協議。本頁不限制適用法律賦予你的消費者權利。"]]},
},
"ja": {
  "folder":"ja", "html":"ja", "language":"日本語", "brand":"CrateNote",
  "nav":["ホーム","プライバシー","サポート","利用条件","言語"], "updated":"更新日：2026年10月15日", "store":"App Storeで見る", "eula":"Apple標準エンドユーザー使用許諾契約",
  "home": {"title":"CrateNote：箱の中身を記録して、すぐ見つける", "lead":"箱に番号を付け、品物・数量・メモ・任意の写真を記録。名前、メモ、箱番号で検索すれば、開ける箱がすぐ分かります。", "sections":[
    ["現在のバージョン", "App Storeでは現在バージョン1.0を提供しています。箱と品物の一覧、メモと任意の写真、引っ越しチェックリスト、PDFリストとラベル、端末内のバックアップと復元が使えます。登録、広告、サブスクリプションはありません。価格はApp Storeをご確認ください。"],
    ["バージョン2.0を準備中", "2.0の草案では、場所の階層、端末上での写真・音声入力、アイテムグラフ、最近削除した記録の復元、開封動画を追加します。Appleの審査を通過して公開された場合に利用できます。提供中の機能はApp Storeのバージョンをご確認ください。"]]},
  "privacy": {"title":"プライバシーポリシー", "lead":"CrateNoteがアプリ内データと本ウェブサイトのアクセス情報をどのように扱うかを説明します。", "sections":[
    ["更新日と対象", "更新日：2026年10月15日。本ポリシーはCrateNote iOSアプリと本ウェブサイトに適用されます。機能はバージョンによって異なります。現在の1.0と準備中の2.0について説明します。"],
    ["端末内の記録", "品物、場所、メモ、チェックリスト、写真は端末上のアプリデータに保存されます。開発者はこれらの内容を収集するサーバーを運用しておらず、広告、分析、トラッキングSDKも使用しません。iOSの端末バックアップにアプリデータが含まれるかはシステム設定によります。"],
    ["写真とカメラ", "システムの写真ピッカーからアプリに渡るのは、あなたが選んだ画像だけです。写真ライブラリ全体へのアクセスは求めません。カメラ権限は撮影を選んだときだけ求めます。1.0で自分で添付した写真は端末に保存されます。2.0の写真認識は端末上で行い、元画像は通常保存されません。任意で品物ごとに約60 KBの圧縮サムネイルを残せます。写真は開発者のサーバーに送信されません。"],
    ["音声と動画", "お使いのバージョンに機能が含まれる場合、音声認識は端末上で行い、音声をアップロードまたは保存しません。オフライン認識に対応しない端末では、文字入力か写真の利用を案内します。開封動画は最長30秒で端末内に保存され、アプリから書き出すバックアップには含まれません。"],
    ["書き出し・共有・削除", "自分で書き出すバックアップやPDFには選択した記録が含まれます。受信者や選択したクラウドストレージが内容を取得する場合があります。QRコードには端末内の記録IDだけが含まれ、遠隔検索はできません。2.0では削除した記録を復元用に30日間保持します。アプリを削除すると端末内データと安全コピーが消えます。"],
    ["外部サービスと連絡先", "App Storeでの購入と返金申請はAppleが処理します。本サイトはGitHub Pagesでホストされています。GitHubのプライバシー説明によると、IPアドレス、端末情報、ウェブサイトの利用ログなどをサービス利用情報として処理する場合があります。サポートメールを送ると、本文の情報がサポート担当者に届きます。パスワードなど不要な個人情報は送らないでください。"]]},
  "support": {"title":"サポート", "lead":"まずはよくある質問をご確認ください。", "sections":[
    ["お問い合わせ", f"サポート窓口：{EMAIL}。端末機種、iOSとアプリのバージョン、問題の内容、再現手順をお知らせください。解決に必要な場合を除き、品物の写真、完全なバックアップ、パスワードは送らないでください。"],
    ["品物を探す", "バージョン1.0では「箱」タブで品名、箱番号、メモを検索できます。見つからない場合はフィルタを解除してください。新しいバージョンでは場所も検索でき、場所の階層を確認できます。"],
    ["写真認識と写真", "対応バージョンでは撮影するか、システムの写真ピッカーから画像を選び、認識候補を確認・編集してから保存します。認識は端末上で行われ、元画像は通常保存されません。カメラ権限はシステム設定で変更できます。"],
    ["音声入力", "音声入力にはマイクと音声認識の許可が必要で、端末上の認識だけを使います。端末がオフライン認識に対応しない場合は文字入力か写真をご利用ください。オンライン認識には切り替わりません。"],
    ["機種変更とバックアップ復元", "旧端末でバックアップを「ファイル」に書き出し、新端末から読み込みます。現在の記録を置き換える前に確認があり、安全コピーも保存されます。開封動画はバックアップに含まれないため、新端末で撮り直してください。"],
    ["ファイルを読み込めない", "アプリは読み込めない元ファイルを保護し、空のデータで上書きしません。設定から元ファイルを書き出して保管し、有効なバックアップを復元してください。"],
    ["購入と返金", "購入と返金はAppleが対応します。Appleの購入履歴を確認するか、reportaproblem.apple.comから返金を申請してください。"]]},
  "terms": {"title":"利用条件", "lead":"CrateNoteの利用には、適用されるApp Storeの利用条件が適用されます。", "sections":[
    ["用途とバージョン", "CrateNoteは引っ越しと自宅の収納を記録する個人向けアプリです。機能はインストールしたバージョンによって異なります。1.0はApp Storeで提供中です。2.0の機能はAppleの審査を通過して公開された場合に利用できます。チェックリストは一般的な備忘用で、専門的助言、引っ越しの手配、契約の代わりにはなりません。"],
    ["データとバックアップ", "記録は初期設定で端末に保存されます。機種変更、アプリの削除、記録の削除や復元の前にバックアップを書き出してください。共有する内容、相手、外部保存先はご自身で選択してください。端末の故障、システム復元、外部ファイルの紛失後にデータを復元できない場合があります。"],
    ["購入", "App Storeからの買い切りダウンロードで、サブスクリプションやアプリ内の機能購入はありません。価格、支払い、返金、購入履歴はAppleのストア表示と規則に従います。"],
    ["ラベルとサービスの制限", "箱番号や「割れ物」などのラベルは自分用の記録であり、運送業者の取り扱いを保証しません。専門的な引っ越しや安全の助言として利用しないでください。"],
    ["ライセンスと消費者の権利", "本アプリにはApple標準のエンドユーザー使用許諾契約が適用されます。本ページは適用法で認められる消費者の権利を制限しません。"]]},
},
"ko": {
  "folder":"ko", "html":"ko", "language":"한국어", "brand":"CrateNote",
  "nav":["홈","개인정보","지원","이용 약관","언어"], "updated":"업데이트: 2026년 10월 15일", "store":"App Store에서 보기", "eula":"Apple 표준 최종 사용자 사용권 계약",
  "home": {"title":"CrateNote: 상자마다 무엇이 들었는지 기록하세요", "lead":"상자에 번호를 붙이고 물품, 수량, 메모, 선택 사진을 기록하세요. 이름, 메모, 상자 번호로 검색하면 열 상자를 바로 찾을 수 있습니다.", "sections":[
    ["현재 버전", "현재 App Store에서 버전 1.0을 제공합니다. 상자와 물품 목록, 메모와 선택 사진, 이사 체크리스트, PDF 목록과 라벨, 기기 내 백업 및 복원을 지원합니다. 가입, 광고, 구독은 없습니다. 가격은 App Store에서 확인하세요."],
    ["버전 2.0 준비 중", "2.0 초안에는 위치 계층, 기기 내 사진·음성 입력, 물품 그래프, 최근 삭제 복구, 개봉 영상이 추가됩니다. Apple 심사를 통과해 업데이트가 출시된 뒤에만 사용할 수 있습니다. 현재 제공되는 기능은 App Store 버전을 확인하세요."]]},
  "privacy": {"title":"개인정보 처리방침", "lead":"CrateNote 앱 데이터와 이 웹사이트 방문 정보를 어떻게 처리하는지 설명합니다.", "sections":[
    ["업데이트 및 적용 범위", "업데이트: 2026년 10월 15일. 이 방침은 CrateNote iOS 앱과 이 웹사이트에 적용됩니다. 기능은 버전에 따라 다르며, 현재 버전 1.0과 준비 중인 2.0을 설명합니다."],
    ["기기에 저장되는 기록", "물품, 위치, 메모, 체크리스트, 사진은 기기의 앱 데이터에 저장됩니다. 개발자는 이 내용을 수집하는 서버를 운영하지 않으며 광고, 분석, 추적 SDK도 사용하지 않습니다. iOS 기기 백업에 앱 데이터가 포함되는지는 시스템 설정에 따라 다릅니다."],
    ["사진 및 카메라", "시스템 사진 선택기는 사용자가 고른 사진만 앱에 제공합니다. 전체 사진 보관함 접근 권한은 요청하지 않습니다. 카메라 권한은 직접 촬영을 선택할 때만 요청합니다. 버전 1.0에서 직접 첨부한 사진은 기기에 저장됩니다. 버전 2.0의 사진 인식은 기기에서 처리하며 원본 이미지는 기본적으로 보관하지 않습니다. 원하면 물품마다 약 60KB의 압축 썸네일을 저장할 수 있습니다. 사진은 개발자 서버로 전송되지 않습니다."],
    ["음성 및 동영상", "사용 중인 버전에 기능이 포함된 경우 음성 인식은 기기에서만 실행되며 음성은 업로드되거나 저장되지 않습니다. 오프라인 인식을 지원하지 않는 기기에서는 글 입력이나 사진 사용을 안내합니다. 개봉 영상은 최대 30초이며 기기에 저장되고 앱에서 내보내는 백업에는 포함되지 않습니다."],
    ["내보내기, 공유, 삭제", "직접 내보내는 백업과 PDF에는 선택한 기록이 들어갑니다. 수신자나 선택한 클라우드 파일 서비스가 내용을 받을 수 있습니다. QR 코드에는 기기의 기록 ID만 포함되며 원격 조회 기능은 없습니다. 버전 2.0은 삭제한 기록을 복구할 수 있도록 30일간 보관합니다. 앱을 삭제하면 기기의 앱 데이터와 안전 사본도 삭제됩니다."],
    ["외부 서비스 및 문의", "App Store 구매와 환불 요청은 Apple이 처리합니다. 이 웹사이트는 GitHub Pages에서 호스팅됩니다. GitHub 개인정보 안내에 따르면 IP 주소, 기기 정보, 웹사이트 이용 로그 등을 서비스 이용 정보로 처리할 수 있습니다. 지원 메일을 보내면 본문 정보가 지원 담당자에게 전달됩니다. 비밀번호나 불필요한 개인정보는 보내지 마세요."]]},
  "support": {"title":"지원", "lead":"먼저 자주 묻는 질문을 확인해 보세요.", "sections":[
    ["문의하기", f"지원 이메일: {EMAIL}. 기기 모델, iOS 및 앱 버전, 문제 내용, 재현 방법을 적어 주세요. 해결에 꼭 필요한 경우가 아니라면 물품 사진, 전체 백업, 비밀번호를 보내지 마세요."],
    ["물품 찾기", "버전 1.0에서는 상자 탭에서 물품 이름, 상자 번호, 메모로 검색합니다. 결과가 없으면 필터를 지워 보세요. 최신 버전에서는 위치와 전체 보관 경로도 검색할 수 있습니다."],
    ["사진 인식과 사진", "해당 기능이 있는 버전에서는 사진을 찍거나 시스템 사진 선택기에서 이미지를 골라 인식 제안을 확인하고 수정한 뒤 저장합니다. 인식은 기기에서 실행되며 원본은 기본적으로 보관하지 않습니다. 카메라 권한은 시스템 설정에서 변경할 수 있습니다."],
    ["음성 입력", "음성 입력에는 마이크 및 음성 인식 권한이 필요하며 기기 내 인식만 사용합니다. 오프라인 인식을 지원하지 않으면 글을 입력하거나 사진을 사용하세요. 온라인 인식으로 전환하지 않습니다."],
    ["기기 변경 및 백업 복원", "이전 기기에서 백업을 파일 앱으로 내보낸 뒤 새 기기에서 가져오세요. 현재 기록을 바꾸기 전에 확인을 요청하고 안전 사본을 보관합니다. 개봉 영상은 내보낸 백업에 포함되지 않으므로 새 기기에서 다시 촬영해야 합니다."],
    ["파일을 읽을 수 없음", "앱은 읽을 수 없는 원본 파일을 보호하며 빈 데이터로 덮어쓰지 않습니다. 설정에서 원본을 내보내 보관한 다음 유효한 백업을 복원하세요."],
    ["구매 및 환불", "구매와 환불은 Apple이 처리합니다. Apple 구매 내역을 확인하거나 reportaproblem.apple.com에서 환불을 요청하세요."]]},
  "terms": {"title":"이용 약관", "lead":"CrateNote 이용에는 적용되는 App Store 이용 약관이 적용됩니다.", "sections":[
    ["목적 및 버전", "CrateNote는 개인의 이사와 집안 수납 기록을 위한 앱입니다. 기능은 설치한 버전에 따라 다릅니다. 버전 1.0은 App Store에서 제공 중이며, 2.0 기능은 Apple 심사를 통과해 업데이트가 출시된 뒤 사용할 수 있습니다. 체크리스트는 일반적인 알림이며 전문 조언, 이사 계약이나 운송 준비를 대신하지 않습니다."],
    ["데이터와 백업", "기록은 기본적으로 기기에 저장됩니다. 기기 변경, 앱 삭제, 기록 삭제 또는 복원 전에 백업을 내보내세요. 공유할 내용, 수신자, 외부 저장 위치는 사용자가 선택합니다. 기기 고장, 시스템 복원, 외부 파일 분실 후에는 데이터를 복구하지 못할 수 있습니다."],
    ["구매", "App Store에서 한 번 결제해 다운로드하며 구독이나 앱 내 기능 구매는 없습니다. 실제 가격, 결제, 환불, 구매 내역은 Apple 스토어와 정책에 따릅니다."],
    ["라벨 및 서비스 제한", "상자 번호와 파손주의 같은 표시는 개인 기록용이며 운송업체가 그대로 처리한다고 보장하지 않습니다. 전문 이사 또는 안전 조언을 대신하는 용도로 사용하지 마세요."],
    ["라이선스 및 소비자 권리", "앱에는 Apple 표준 최종 사용자 사용권 계약이 적용됩니다. 이 페이지는 관련 법률에 따른 소비자 권리를 제한하지 않습니다."]]},
},
"es-ES": {
  "folder":"es", "html":"es", "language":"Español", "brand":"CrateNote",
  "nav":["Inicio","Privacidad","Soporte","Condiciones","Idioma"], "updated":"Actualizado el 15 de octubre de 2026", "store":"Ver en App Store", "eula":"Contrato de licencia de usuario final estándar de Apple",
  "home": {"title":"CrateNote: descubre qué hay en cada caja", "lead":"Numera las cajas y anota los objetos, las cantidades, las notas y las fotos que quieras. Busca por nombre, nota o número de caja para saber cuál abrir.", "sections":[
    ["Versión disponible", "La versión 1.0 está actualmente en App Store. Incluye listas de cajas y objetos, notas y fotos opcionales, lista de mudanza, listas y etiquetas en PDF, y copia de seguridad y restauración locales. Sin cuenta, anuncios ni suscripciones. Consulta el precio en App Store."],
    ["Versión 2.0 en preparación", "El borrador de la versión 2.0 añade una jerarquía de lugares, entrada de fotos y voz en el dispositivo, un mapa de objetos, recuperación de elementos eliminados y vídeos de apertura. Estas funciones solo estarán disponibles si Apple aprueba y publica la actualización. Comprueba en App Store qué versión está disponible."]]},
  "privacy": {"title":"Política de privacidad", "lead":"Esta política explica cómo CrateNote trata los datos de la app y la información de acceso a este sitio web.", "sections":[
    ["Actualización y alcance", "Actualizada el 15 de octubre de 2026. Se aplica a la app CrateNote para iOS y a este sitio web. Las funciones cambian según la versión; aquí se describen la versión 1.0 y la actualización 2.0 en preparación."],
    ["Registros en el dispositivo", "Los objetos, lugares, notas, listas y fotos se guardan como datos de la app en tu dispositivo. El desarrollador no tiene un servidor para recopilar este contenido y la app no utiliza publicidad, analítica ni SDK de seguimiento. La copia de seguridad de iOS puede incluir datos de la app según la configuración del sistema."],
    ["Fotos y cámara", "El selector de fotos del sistema solo proporciona las imágenes que eliges; la app no solicita acceso completo a la fototeca. Solo pide permiso para la cámara cuando eliges hacer una foto. Las fotos que adjuntes en la versión 1.0 se guardan en el dispositivo. El reconocimiento de fotos de la versión 2.0 se realiza en el dispositivo y no conserva la imagen original por defecto; puedes guardar una miniatura comprimida de unos 60 KB por objeto. Las fotos no se envían a servidores del desarrollador."],
    ["Voz y vídeo", "Si tu versión incluye estas funciones, el reconocimiento de voz se realiza en el dispositivo y el audio no se sube ni se guarda. Si no se admite el reconocimiento sin conexión, la app te pedirá que escribas o uses una foto. Los vídeos de apertura duran hasta 30 segundos, se quedan en el dispositivo y no se incluyen en las copias exportadas."],
    ["Exportación, uso compartido y eliminación", "Las copias de seguridad y los PDF que exportes contienen los registros seleccionados. Los destinatarios o servicios de archivos en la nube que elijas podrían recibirlos. Los códigos QR solo contienen un ID local del registro y no permiten consultas remotas. La versión 2.0 conserva durante 30 días los registros eliminados para poder recuperarlos. Al desinstalar se eliminan los datos locales y las copias de seguridad de seguridad."],
    ["Servicios externos y contacto", "Apple gestiona las compras de App Store y las solicitudes de reembolso. Este sitio está alojado en GitHub Pages; la declaración de privacidad de GitHub indica que puede tratar direcciones IP, datos del dispositivo y registros de uso del sitio como información de uso del servicio. Si escribes a soporte, compartes la información del mensaje. No envíes contraseñas ni datos privados innecesarios."]]},
  "support": {"title":"Soporte", "lead":"Consulta estas respuestas antes de escribirnos.", "sections":[
    ["Contacto", f"Correo de soporte: {EMAIL}. Incluye el modelo del dispositivo, las versiones de iOS y de la app, el problema y los pasos para reproducirlo. No envíes fotos, copias de seguridad completas ni contraseñas salvo que sean imprescindibles para resolver el problema."],
    ["Encontrar un objeto", "En la versión 1.0, busca por nombre del objeto, número de caja o nota en la pestaña Cajas. Si no aparece nada, borra los filtros. Las versiones posteriores también permiten buscar lugares y ver la ruta completa."],
    ["Reconocimiento y fotos", "En las versiones que lo incluyen, haz una foto o elige una en el selector del sistema; revisa y edita las sugerencias antes de guardar. El reconocimiento se realiza en el dispositivo y la imagen original no se conserva por defecto. Puedes cambiar el permiso de cámara en Ajustes del sistema."],
    ["Entrada por voz", "La entrada por voz requiere permiso para el micrófono y el reconocimiento de voz, y solo usa reconocimiento en el dispositivo. Si no se admite sin conexión, escribe el objeto o usa una foto; la app no recurrirá al reconocimiento en línea."],
    ["Cambiar de dispositivo o restaurar", "Exporta una copia a Archivos desde el dispositivo antiguo e impórtala en el nuevo. Antes de reemplazar los datos actuales, la app pide confirmación y guarda una copia de seguridad. Los vídeos de apertura no se incluyen y tendrás que grabarlos de nuevo."],
    ["No se puede leer un archivo", "La app protege el archivo original ilegible y evita sobrescribirlo con datos vacíos. Expórtalo desde Ajustes y después restaura una copia válida."],
    ["Compras y reembolsos", "Apple gestiona las compras y los reembolsos. Consulta tu historial de compras de Apple o visita reportaproblem.apple.com para solicitar un reembolso."]]},
  "terms": {"title":"Condiciones de uso", "lead":"El uso de CrateNote está sujeto a las condiciones de App Store que correspondan.", "sections":[
    ["Finalidad y versiones", "CrateNote es una herramienta personal para registrar mudanzas y almacenamiento en casa. Las funciones dependen de la versión instalada. La versión 1.0 está en App Store; las funciones de la 2.0 solo estarán disponibles si Apple aprueba y publica la actualización. La lista de mudanza ofrece recordatorios generales, no asesoramiento profesional ni sustituye acuerdos o contratos de mudanza."],
    ["Datos y copias de seguridad", "Los registros se guardan en tu dispositivo por defecto. Exporta una copia antes de cambiar de dispositivo, desinstalar, borrar o restaurar datos. Tú eliges qué compartir, con quién y dónde guardarlo. Es posible que no se puedan recuperar datos tras un fallo del dispositivo, una restauración del sistema o la pérdida de archivos externos."],
    ["Compras", "La app se descarga mediante un pago único en App Store, sin suscripciones ni compras de funciones dentro de la app. El precio aplicable, el pago, los reembolsos y el historial dependen de Apple."],
    ["Etiquetas y límites del servicio", "Los números de caja y marcas como Frágil son recordatorios para tus registros; no garantizan que el transportista manipule la caja de una forma concreta. No sustituyen consejos profesionales de mudanza o seguridad."],
    ["Licencia y derechos del consumidor", "La app está sujeta al Contrato de licencia de usuario final estándar de Apple. Esta página no limita los derechos que te reconoce la legislación aplicable."]]},
},
"de-DE": {
  "folder":"de", "html":"de", "language":"Deutsch", "brand":"CrateNote",
  "nav":["Startseite","Datenschutz","Support","Nutzungsbedingungen","Sprache"], "updated":"Aktualisiert am 15. Oktober 2026", "store":"Im App Store ansehen", "eula":"Apples Standard-Endbenutzer-Lizenzvertrag",
  "home": {"title":"CrateNote: Finde heraus, was in jeder Kiste ist", "lead":"Nummeriere deine Kisten und notiere Gegenstände, Mengen, Hinweise und optionale Fotos. Suche nach Name, Hinweis oder Kistennummer und weißt sofort, welche Kiste du öffnen musst.", "sections":[
    ["Verfügbare Version", "Version 1.0 ist derzeit im App Store verfügbar. Sie bietet Kisten- und Artikellisten, Hinweise und optionale Fotos, eine Umzugs-Checkliste, PDF-Listen und Etiketten sowie lokale Sicherung und Wiederherstellung. Ohne Konto, Werbung oder Abonnement. Den aktuellen Preis findest du im App Store."],
    ["Version 2.0 in Vorbereitung", "Der Entwurf für Version 2.0 ergänzt eine Ortsstruktur, Foto- und Spracheingabe auf dem Gerät, eine Inventargrafik, die Wiederherstellung kürzlich gelöschter Einträge und Auspackvideos. Diese Funktionen sind erst verfügbar, wenn Apple das Update genehmigt und veröffentlicht. Maßgeblich ist die aktuell im App Store verfügbare Version."]]},
  "privacy": {"title":"Datenschutzerklärung", "lead":"Diese Erklärung beschreibt, wie CrateNote App-Daten und Informationen über Besuche dieser Website behandelt.", "sections":[
    ["Aktualisierung und Geltungsbereich", "Aktualisiert am 15. Oktober 2026. Diese Erklärung gilt für die CrateNote iOS-App und diese Website. Funktionen unterscheiden sich je nach Version; beschrieben werden Version 1.0 und das vorbereitete Update 2.0."],
    ["Einträge auf deinem Gerät", "Gegenstände, Orte, Notizen, Checklisten und Fotos werden als App-Daten auf deinem Gerät gespeichert. Der Entwickler betreibt keinen Server, der diese Inhalte sammelt, und verwendet keine Werbung, Analyse- oder Tracking-SDKs. Ob ein iOS-Gerätebackup App-Daten enthält, hängt von deinen Systemeinstellungen ab."],
    ["Fotos und Kamera", "Der systemeigene Fotoauswahldialog gibt der App nur die von dir ausgewählten Bilder. Ein vollständiger Zugriff auf die Fotomediathek wird nicht angefordert. Die Kameraerlaubnis wird nur angefragt, wenn du ein Foto aufnehmen möchtest. In Version 1.0 angehängte Fotos bleiben auf dem Gerät. Die Fotoerkennung in Version 2.0 läuft auf dem Gerät; das Originalbild wird standardmäßig nicht behalten. Optional kannst du pro Artikel ein komprimiertes Vorschaubild von etwa 60 KB speichern. Fotos werden nicht an Entwickler-Server gesendet."],
    ["Sprache und Video", "Wenn deine Version diese Funktionen enthält, erfolgt die Spracherkennung ausschließlich auf dem Gerät; Audio wird weder hochgeladen noch gespeichert. Unterstützt das Gerät keine Offline-Erkennung, bittet die App dich um Texteingabe oder ein Foto. Auspackvideos sind bis zu 30 Sekunden lang, bleiben auf dem Gerät und sind nicht in exportierten Backups enthalten."],
    ["Export, Teilen und Löschen", "Von dir exportierte Backups und PDFs enthalten die ausgewählten Einträge. Empfänger oder von dir gewählte Cloud-Dateidienste können diese Inhalte erhalten. QR-Codes enthalten nur eine lokale Datensatz-ID und ermöglichen keine Abfrage über das Internet. Version 2.0 bewahrt gelöschte Einträge 30 Tage lang zur Wiederherstellung auf. Bei der Deinstallation werden lokale App-Daten und Sicherheitskopien entfernt."],
    ["Externe Dienste und Kontakt", "Apple bearbeitet App-Store-Käufe und Rückerstattungsanfragen. Diese Website wird von GitHub Pages gehostet. Laut GitHubs Datenschutzerklärung kann GitHub IP-Adressen, Geräteinformationen und Website-Nutzungsprotokolle als Dienstnutzungsdaten verarbeiten. Wenn du dem Support schreibst, erhält er die Angaben aus deiner Nachricht. Sende keine Passwörter oder unnötigen privaten Daten."]]},
  "support": {"title":"Support", "lead":"Vielleicht findest du hier schon die passende Antwort.", "sections":[
    ["Kontakt", f"Support-E-Mail: {EMAIL}. Bitte nenne Gerätemodell, iOS- und App-Version, das Problem und die Schritte zur Reproduktion. Sende keine Fotos, vollständigen Backups oder Passwörter, sofern sie zur Lösung nicht unbedingt erforderlich sind."],
    ["Einen Gegenstand finden", "Suche in Version 1.0 im Tab „Kisten“ nach Artikelname, Kistennummer oder Notiz. Wenn nichts erscheint, entferne die Filter. Neuere Versionen können zusätzlich Orte durchsuchen und den vollständigen Pfad anzeigen."],
    ["Fotoerkennung und Fotos", "In Versionen mit dieser Funktion kannst du ein Foto aufnehmen oder über die Systemauswahl auswählen, Vorschläge prüfen und bearbeiten und anschließend speichern. Die Erkennung läuft auf dem Gerät; das Originalbild wird standardmäßig nicht behalten. Die Kameraberechtigung änderst du in den Systemeinstellungen."],
    ["Spracheingabe", "Für die Spracheingabe sind Mikrofon- und Spracherkennungsberechtigungen erforderlich. Sie nutzt nur geräteinterne Erkennung. Unterstützt dein Gerät keine Offline-Erkennung, tippe den Gegenstand ein oder verwende ein Foto; die App wechselt nicht zur Online-Erkennung."],
    ["Gerätewechsel und Backup-Wiederherstellung", "Exportiere auf dem alten Gerät ein Backup in die Dateien-App und importiere es auf dem neuen Gerät. Vor dem Ersetzen der aktuellen Daten fragt die App nach deiner Bestätigung und legt eine Sicherheitskopie an. Auspackvideos sind nicht im Backup enthalten und müssen neu aufgenommen werden."],
    ["Datei kann nicht gelesen werden", "Die App schützt eine unlesbare Originaldatei davor, mit leeren Daten überschrieben zu werden. Exportiere sie in den Einstellungen und stelle anschließend ein gültiges Backup wieder her."],
    ["Käufe und Rückerstattungen", "Apple bearbeitet Käufe und Rückerstattungen. Prüfe deinen Apple-Kaufverlauf oder beantrage die Rückerstattung unter reportaproblem.apple.com."]]},
  "terms": {"title":"Nutzungsbedingungen", "lead":"Für CrateNote gelten die jeweils anwendbaren App-Store-Bedingungen.", "sections":[
    ["Zweck und Versionen", "CrateNote ist ein persönliches Werkzeug für Umzug und Aufbewahrung zu Hause. Die Funktionen richten sich nach der installierten Version. Version 1.0 ist im App Store verfügbar; Funktionen aus Version 2.0 gibt es erst, wenn Apple das Update genehmigt und veröffentlicht. Die Checkliste enthält allgemeine Erinnerungen und ersetzt weder Fachberatung noch Umzugsvereinbarungen oder Verträge."],
    ["Daten und Backups", "Einträge werden standardmäßig auf deinem Gerät gespeichert. Exportiere ein Backup, bevor du das Gerät wechselst, die App deinstallierst, Daten löschst oder wiederherstellst. Du entscheidest, welche Inhalte du mit wem und wo teilst. Nach einem Geräteausfall, einer Systemwiederherstellung oder dem Verlust externer Dateien sind Daten möglicherweise nicht wiederherstellbar."],
    ["Käufe", "Die App wird gegen eine einmalige Zahlung im App Store geladen. Es gibt keine Abonnements und keine In-App-Käufe für Funktionen. Preis, Zahlung, Rückerstattung und Kaufverlauf richten sich nach den Angaben und Regeln von Apple."],
    ["Etiketten und Grenzen", "Kistennummern und Hinweise wie „Zerbrechlich“ dienen deiner eigenen Dokumentation und garantieren keine bestimmte Behandlung durch Transportunternehmen. Die App ersetzt keine professionelle Umzugs- oder Sicherheitsberatung."],
    ["Lizenz und Verbraucherrechte", "Für die App gilt Apples Standard-Endbenutzer-Lizenzvertrag. Gesetzliche Verbraucherrechte bleiben unberührt."]]},
},
"fr-FR": {
  "folder":"fr", "html":"fr", "language":"Français", "brand":"CrateNote",
  "nav":["Accueil","Confidentialité","Assistance","Conditions","Langue"], "updated":"Mis à jour le 15 octobre 2026", "store":"Voir sur l’App Store", "eula":"Contrat de licence utilisateur final standard d’Apple",
  "home": {"title":"CrateNote : retrouvez le contenu de chaque carton", "lead":"Numérotez vos cartons et notez les objets, les quantités, les remarques et les photos facultatives. Recherchez par nom, remarque ou numéro pour savoir quel carton ouvrir.", "sections":[
    ["Version disponible", "La version 1.0 est actuellement disponible sur l’App Store. Elle comprend les listes de cartons et d’objets, les remarques et photos facultatives, une liste de déménagement, des listes et étiquettes PDF, ainsi que la sauvegarde et la restauration locales. Sans compte, publicité ni abonnement. Consultez l’App Store pour connaître le prix."],
    ["Version 2.0 en préparation", "Le projet de version 2.0 ajoute une arborescence de lieux, la saisie photo et vocale sur l’appareil, un graphique des objets, la récupération des éléments récemment supprimés et des vidéos de déballage. Ces fonctions ne seront disponibles qu’après l’approbation et la publication de la mise à jour par Apple. Vérifiez la version proposée sur l’App Store."]]},
  "privacy": {"title":"Politique de confidentialité", "lead":"Cette politique explique comment CrateNote traite les données de l’app et les informations de visite de ce site.", "sections":[
    ["Mise à jour et portée", "Mise à jour : 15 octobre 2026. Cette politique concerne l’app iOS CrateNote et ce site web. Les fonctions varient selon la version ; elle décrit la version 1.0 et la mise à jour 2.0 en préparation."],
    ["Données sur votre appareil", "Les objets, lieux, notes, listes et photos sont enregistrés dans les données de l’app sur votre appareil. Le développeur n’exploite aucun serveur destiné à collecter ces contenus et l’app n’utilise ni publicité, ni analytique, ni SDK de suivi. La sauvegarde iOS peut inclure les données de l’app selon vos réglages système."],
    ["Photos et appareil photo", "Le sélecteur de photos du système ne fournit à l’app que les images que vous choisissez ; l’accès complet à la photothèque n’est pas demandé. L’autorisation de l’appareil photo est demandée uniquement lorsque vous choisissez de prendre une photo. Les photos jointes dans la version 1.0 restent sur l’appareil. La reconnaissance photo de la version 2.0 est effectuée sur l’appareil ; l’image originale n’est pas conservée par défaut. Vous pouvez choisir de garder une miniature compressée d’environ 60 Ko par objet. Les photos ne sont pas envoyées aux serveurs du développeur."],
    ["Voix et vidéos", "Si votre version comprend ces fonctions, la reconnaissance vocale s’effectue sur l’appareil et aucun audio n’est envoyé ni conservé. Si la reconnaissance hors ligne n’est pas disponible, l’app vous propose de saisir le texte ou d’utiliser une photo. Les vidéos de déballage durent au maximum 30 secondes, restent sur l’appareil et ne figurent pas dans les sauvegardes exportées."],
    ["Exportation, partage et suppression", "Les sauvegardes et PDF que vous exportez contiennent les fiches sélectionnées. Les destinataires ou services cloud choisis peuvent recevoir ces contenus. Les QR codes contiennent uniquement un identifiant local et ne permettent aucune recherche à distance. La version 2.0 conserve les fiches supprimées pendant 30 jours pour permettre leur récupération. La désinstallation supprime les données locales et les copies de sécurité."],
    ["Services externes et contact", "Apple traite les achats App Store et les demandes de remboursement. Ce site est hébergé par GitHub Pages ; la déclaration de confidentialité de GitHub indique que des adresses IP, informations sur l’appareil et journaux d’utilisation du site peuvent être traités comme informations d’utilisation du service. Un e-mail au support transmet les informations de votre message. N’envoyez pas de mots de passe ni de données privées inutiles."]]},
  "support": {"title":"Assistance", "lead":"Consultez ces réponses avant de contacter le support.", "sections":[
    ["Nous contacter", f"Adresse d’assistance : {EMAIL}. Indiquez le modèle de l’appareil, les versions d’iOS et de l’app, le problème et les étapes pour le reproduire. N’envoyez pas de photos, de sauvegarde complète ou de mot de passe sauf si cela est indispensable au dépannage."],
    ["Retrouver un objet", "Dans la version 1.0, recherchez un nom d’objet, un numéro de carton ou une note dans l’onglet Cartons. Si rien n’apparaît, effacez les filtres. Les versions ultérieures permettent aussi de rechercher des lieux et d’afficher leur chemin complet."],
    ["Reconnaissance et photos", "Dans les versions compatibles, prenez une photo ou choisissez-en une avec le sélecteur du système, vérifiez et modifiez les suggestions puis enregistrez. La reconnaissance se fait sur l’appareil ; l’image originale n’est pas conservée par défaut. Modifiez l’autorisation de l’appareil photo dans les Réglages système."],
    ["Saisie vocale", "La saisie vocale nécessite les autorisations du micro et de la reconnaissance vocale et utilise uniquement la reconnaissance sur l’appareil. Si la reconnaissance hors ligne n’est pas prise en charge, saisissez le texte ou utilisez une photo ; l’app ne bascule pas vers un service en ligne."],
    ["Changer d’appareil ou restaurer", "Exportez une sauvegarde dans Fichiers sur l’ancien appareil, puis importez-la sur le nouveau. L’app demande confirmation avant de remplacer les données et conserve d’abord une copie de sécurité. Les vidéos de déballage ne sont pas incluses et doivent être enregistrées à nouveau."],
    ["Fichier illisible", "L’app protège le fichier original illisible et évite de le remplacer par des données vides. Exportez-le depuis les Réglages, puis restaurez une sauvegarde valide."],
    ["Achats et remboursements", "Apple traite les achats et remboursements. Consultez l’historique des achats Apple ou rendez-vous sur reportaproblem.apple.com pour demander un remboursement."]]},
  "terms": {"title":"Conditions d’utilisation", "lead":"L’utilisation de CrateNote est soumise aux conditions applicables de l’App Store.", "sections":[
    ["Objet et versions", "CrateNote est un outil personnel pour noter un déménagement et le rangement à la maison. Les fonctions dépendent de la version installée. La version 1.0 est disponible sur l’App Store ; les fonctions de la 2.0 seront disponibles uniquement si Apple approuve et publie la mise à jour. La liste de déménagement fournit des rappels généraux, pas des conseils professionnels ni un remplacement des arrangements ou contrats de déménagement."],
    ["Données et sauvegardes", "Les fiches sont enregistrées par défaut sur votre appareil. Exportez une sauvegarde avant de changer d’appareil, de désinstaller l’app, de supprimer ou restaurer des données. Vous choisissez les éléments à partager, les destinataires et le lieu de stockage externe. Les données peuvent être irrécupérables après une panne de l’appareil, une restauration système ou la perte d’un fichier externe."],
    ["Achats", "L’app est téléchargée contre un paiement unique sur l’App Store, sans abonnement ni achat de fonctionnalités dans l’app. Le prix, le paiement, les remboursements et l’historique dépendent des informations et règles d’Apple."],
    ["Étiquettes et limites", "Les numéros de carton et mentions comme « Fragile » sont des rappels personnels et ne garantissent pas la manière dont un transporteur manipulera le carton. L’app ne remplace pas des conseils professionnels de déménagement ou de sécurité."],
    ["Licence et droits des consommateurs", "Le contrat de licence utilisateur final standard d’Apple s’applique à l’app. Rien sur cette page ne limite les droits des consommateurs prévus par la loi applicable."]]},
},
"it": {
  "folder":"it", "html":"it", "language":"Italiano", "brand":"CrateNote",
  "nav":["Home","Privacy","Supporto","Termini","Lingua"], "updated":"Aggiornato il 15 ottobre 2026", "store":"Vedi su App Store", "eula":"Contratto di licenza per l’utente finale standard di Apple",
  "home": {"title":"CrateNote: scopri cosa contiene ogni scatolone", "lead":"Numera gli scatoloni e annota oggetti, quantità, note e foto facoltative. Cerca per nome, nota o numero per sapere quale scatolone aprire.", "sections":[
    ["Versione disponibile", "La versione 1.0 è attualmente disponibile su App Store. Include elenchi di scatoloni e oggetti, note e foto facoltative, una lista per il trasloco, elenchi ed etichette PDF, oltre a backup e ripristino locali. Nessun account, pubblicità o abbonamento. Controlla il prezzo su App Store."],
    ["Versione 2.0 in preparazione", "La bozza della versione 2.0 aggiunge una gerarchia di luoghi, inserimento di foto e voce sul dispositivo, una mappa degli oggetti, il recupero degli elementi eliminati di recente e video di apertura. Queste funzioni saranno disponibili solo se Apple approva e pubblica l’aggiornamento. Verifica su App Store quale versione è disponibile."]]},
  "privacy": {"title":"Informativa sulla privacy", "lead":"Questa informativa spiega come CrateNote tratta i dati dell’app e le informazioni sulle visite a questo sito.", "sections":[
    ["Aggiornamento e ambito", "Aggiornata il 15 ottobre 2026. Si applica all’app iOS CrateNote e a questo sito web. Le funzioni cambiano in base alla versione; qui sono descritte la versione 1.0 e l’aggiornamento 2.0 in preparazione."],
    ["Dati sul dispositivo", "Oggetti, luoghi, note, liste e foto sono salvati nei dati dell’app sul dispositivo. Lo sviluppatore non gestisce server per raccogliere questi contenuti e l’app non usa pubblicità, analisi o SDK di tracciamento. Il backup iOS può includere i dati dell’app in base alle impostazioni di sistema."],
    ["Foto e fotocamera", "Il selettore di foto del sistema fornisce all’app solo le immagini che scegli; non viene richiesto l’accesso completo alla libreria. Il permesso della fotocamera viene chiesto solo quando scegli di scattare una foto. Le foto allegate nella versione 1.0 restano sul dispositivo. Il riconoscimento fotografico della versione 2.0 avviene sul dispositivo e l’immagine originale non viene conservata per impostazione predefinita. Puoi scegliere di salvare una miniatura compressa di circa 60 KB per oggetto. Le foto non vengono inviate ai server dello sviluppatore."],
    ["Voce e video", "Se la tua versione include queste funzioni, il riconoscimento vocale avviene sul dispositivo e l’audio non viene caricato né salvato. Se il riconoscimento offline non è disponibile, l’app ti chiederà di digitare o usare una foto. I video di apertura durano al massimo 30 secondi, restano sul dispositivo e non sono inclusi nei backup esportati."],
    ["Esportazione, condivisione ed eliminazione", "I backup e i PDF che esporti contengono le schede selezionate. I destinatari o i servizi cloud che scegli potrebbero ricevere questi contenuti. I codici QR contengono solo un ID locale e non consentono ricerche da remoto. La versione 2.0 conserva per 30 giorni le schede eliminate, così puoi recuperarle. Disinstallando l’app vengono rimossi i dati locali e le copie di sicurezza."],
    ["Servizi esterni e contatti", "Apple gestisce gli acquisti App Store e le richieste di rimborso. Questo sito è ospitato da GitHub Pages; l’informativa di GitHub indica che può trattare indirizzi IP, dati del dispositivo e log di utilizzo del sito come informazioni sull’uso del servizio. Scrivendo al supporto condividi le informazioni contenute nel messaggio. Non inviare password o dati privati non necessari."]]},
  "support": {"title":"Supporto", "lead":"Consulta prima le risposte alle domande più comuni.", "sections":[
    ["Contatti", f"Email di supporto: {EMAIL}. Indica modello del dispositivo, versioni di iOS e dell’app, problema e passaggi per riprodurlo. Non inviare foto, backup completi o password salvo che siano indispensabili per risolvere il problema."],
    ["Trovare un oggetto", "Nella versione 1.0, cerca per nome dell’oggetto, numero dello scatolone o nota nella scheda Scatoloni. Se non trovi nulla, rimuovi i filtri. Le versioni successive consentono di cercare anche i luoghi e vedere il percorso completo."],
    ["Riconoscimento e foto", "Nelle versioni che includono la funzione, scatta una foto o selezionala dal selettore di sistema; controlla e modifica i suggerimenti prima di salvare. Il riconoscimento avviene sul dispositivo e l’immagine originale non viene conservata per impostazione predefinita. Puoi cambiare il permesso della fotocamera nelle Impostazioni di sistema."],
    ["Inserimento vocale", "L’inserimento vocale richiede i permessi per microfono e riconoscimento vocale e usa solo il riconoscimento sul dispositivo. Se il dispositivo non supporta il riconoscimento offline, digita o usa una foto; l’app non passerà al riconoscimento online."],
    ["Cambiare dispositivo o ripristinare", "Esporta un backup in File dal vecchio dispositivo e importalo su quello nuovo. Prima di sostituire i dati attuali, l’app chiede conferma e conserva una copia di sicurezza. I video di apertura non sono inclusi nel backup e dovrai registrarli di nuovo."],
    ["File non leggibile", "L’app protegge il file originale illeggibile ed evita di sovrascriverlo con dati vuoti. Esporta il file dalle Impostazioni, poi ripristina un backup valido."],
    ["Acquisti e rimborsi", "Apple gestisce acquisti e rimborsi. Consulta la cronologia acquisti Apple o visita reportaproblem.apple.com per chiedere un rimborso."]]},
  "terms": {"title":"Termini di utilizzo", "lead":"L’uso di CrateNote è soggetto ai termini App Store applicabili.", "sections":[
    ["Scopo e versioni", "CrateNote è uno strumento personale per registrare traslochi e organizzazione della casa. Le funzioni dipendono dalla versione installata. La versione 1.0 è su App Store; le funzioni della 2.0 saranno disponibili solo se Apple approva e pubblica l’aggiornamento. La lista per il trasloco offre promemoria generali e non sostituisce consulenze professionali, accordi o contratti."],
    ["Dati e backup", "I dati vengono salvati sul dispositivo per impostazione predefinita. Esporta un backup prima di cambiare dispositivo, disinstallare l’app, eliminare o ripristinare dati. Scegli tu cosa condividere, con chi e dove conservarlo. I dati potrebbero non essere recuperabili dopo un guasto del dispositivo, un ripristino del sistema o la perdita di file esterni."],
    ["Acquisti", "L’app si scarica con un pagamento una tantum su App Store, senza abbonamenti né acquisti di funzioni nell’app. Prezzo, pagamento, rimborsi e cronologia acquisti seguono le informazioni e le regole di Apple."],
    ["Etichette e limiti", "I numeri degli scatoloni e le diciture come Fragile sono promemoria personali e non garantiscono come il trasportatore tratterà il pacco. L’app non sostituisce consigli professionali per traslochi o sicurezza."],
    ["Licenza e diritti dei consumatori", "All’app si applica il contratto di licenza per l’utente finale standard di Apple. Questa pagina non limita i diritti dei consumatori previsti dalla legge applicabile."]]},
},
"pt-BR": {
  "folder":"pt-BR", "html":"pt-BR", "language":"Português (Brasil)", "brand":"CrateNote",
  "nav":["Início","Privacidade","Suporte","Termos","Idioma"], "updated":"Atualizado em 15 de outubro de 2026", "store":"Ver na App Store", "eula":"Contrato de Licença de Usuário Final padrão da Apple",
  "home": {"title":"CrateNote: saiba o que está em cada caixa", "lead":"Numere as caixas e anote itens, quantidades, observações e fotos opcionais. Pesquise por nome, observação ou número para saber qual caixa abrir.", "sections":[
    ["Versão disponível", "A versão 1.0 está disponível na App Store. Ela inclui listas de caixas e itens, observações e fotos opcionais, checklist de mudança, listas e etiquetas em PDF, além de backup e restauração locais. Sem conta, anúncios ou assinaturas. Consulte o preço na App Store."],
    ["Versão 2.0 em preparação", "O rascunho da versão 2.0 adiciona uma hierarquia de locais, entrada de fotos e voz no aparelho, um gráfico de itens, recuperação de registros excluídos recentemente e vídeos de abertura. Esses recursos só estarão disponíveis se a Apple aprovar e publicar a atualização. Confira na App Store qual versão está disponível."]]},
  "privacy": {"title":"Política de privacidade", "lead":"Esta política explica como o CrateNote trata os dados do app e as informações de acesso a este site.", "sections":[
    ["Atualização e escopo", "Atualizada em 15 de outubro de 2026. Esta política se aplica ao app CrateNote para iOS e a este site. Os recursos variam conforme a versão; descrevemos a versão 1.0 e a atualização 2.0 em preparação."],
    ["Registros no aparelho", "Itens, locais, observações, listas e fotos ficam nos dados do app no aparelho. O desenvolvedor não mantém servidor para coletar esse conteúdo, e o app não usa anúncios, análise ou SDKs de rastreamento. O backup do dispositivo iOS pode incluir dados do app, conforme os ajustes do sistema."],
    ["Fotos e câmera", "O seletor de fotos do sistema fornece ao app apenas as imagens que você escolher; o app não pede acesso completo à fototeca. A permissão da câmera é solicitada apenas quando você escolhe tirar uma foto. Fotos anexadas na versão 1.0 ficam no aparelho. O reconhecimento de fotos da versão 2.0 acontece no aparelho e a imagem original não é mantida por padrão. Se quiser, você pode guardar uma miniatura comprimida de cerca de 60 KB por item. As fotos não são enviadas aos servidores do desenvolvedor."],
    ["Voz e vídeos", "Se a sua versão incluir esses recursos, o reconhecimento de voz acontece no aparelho e o áudio não é enviado nem salvo. Se o reconhecimento offline não estiver disponível, o app pedirá que você digite ou use uma foto. Vídeos de abertura têm até 30 segundos, ficam no aparelho e não entram nos backups exportados pelo app."],
    ["Exportação, compartilhamento e exclusão", "Os backups e PDFs que você exportar contêm os registros selecionados. Destinatários ou serviços de arquivos na nuvem escolhidos por você podem receber esse conteúdo. QR codes contêm somente um ID local do registro e não permitem consulta remota. A versão 2.0 mantém registros excluídos por 30 dias para recuperação. Ao desinstalar, os dados locais do app e as cópias de segurança são removidos."],
    ["Serviços externos e contato", "A Apple processa compras na App Store e pedidos de reembolso. Este site é hospedado pelo GitHub Pages; a declaração de privacidade do GitHub informa que ele pode tratar endereços IP, dados do aparelho e registros de uso do site como informações de utilização do serviço. Ao enviar um e-mail ao suporte, você compartilha as informações da mensagem. Não envie senhas nem dados privados desnecessários."]]},
  "support": {"title":"Suporte", "lead":"Confira estas respostas antes de entrar em contato.", "sections":[
    ["Contato", f"E-mail de suporte: {EMAIL}. Informe o modelo do aparelho, as versões do iOS e do app, o problema e os passos para reproduzi-lo. Não envie fotos, backups completos ou senhas, a menos que sejam indispensáveis para resolver o problema."],
    ["Encontrar um item", "Na versão 1.0, pesquise por nome do item, número da caixa ou observação na aba Caixas. Se nada aparecer, limpe os filtros. Versões mais novas também permitem pesquisar locais e ver o caminho completo."],
    ["Reconhecimento e fotos", "Nas versões com esse recurso, tire uma foto ou escolha uma pelo seletor do sistema, revise e edite as sugestões e depois salve. O reconhecimento é feito no aparelho e a imagem original não é mantida por padrão. Altere a permissão da câmera nos Ajustes do sistema."],
    ["Entrada por voz", "A entrada por voz exige permissão do microfone e do reconhecimento de fala e usa somente o reconhecimento no aparelho. Se o aparelho não oferecer reconhecimento offline, digite ou use uma foto; o app não muda para reconhecimento online."],
    ["Trocar de aparelho ou restaurar backup", "Exporte um backup para Arquivos no aparelho antigo e importe no novo. O app pede confirmação antes de substituir os dados atuais e guarda uma cópia de segurança primeiro. Vídeos de abertura não entram no backup exportado e precisam ser gravados novamente."],
    ["Arquivo não pode ser lido", "O app protege o arquivo original ilegível e evita sobrescrevê-lo com dados vazios. Exporte o arquivo original em Ajustes e depois restaure um backup válido."],
    ["Compras e reembolsos", "A Apple processa compras e reembolsos. Consulte o histórico de compras da Apple ou acesse reportaproblem.apple.com para solicitar um reembolso."]]},
  "terms": {"title":"Termos de uso", "lead":"O uso do CrateNote está sujeito aos termos aplicáveis da App Store.", "sections":[
    ["Finalidade e versões", "O CrateNote é uma ferramenta pessoal para registrar mudanças e organização da casa. Os recursos dependem da versão instalada. A versão 1.0 está na App Store; os recursos da versão 2.0 só estarão disponíveis se a Apple aprovar e publicar a atualização. O checklist oferece lembretes gerais e não substitui orientação profissional, acordos ou contratos de mudança."],
    ["Dados e backups", "Por padrão, os registros ficam no aparelho. Exporte um backup antes de trocar de aparelho, desinstalar o app, excluir ou restaurar dados. Você escolhe o que compartilhar, com quem e onde guardar. Os dados talvez não possam ser recuperados após falha do aparelho, restauração do sistema ou perda de arquivos externos."],
    ["Compras", "O app é baixado mediante pagamento único na App Store, sem assinaturas nem compras de recursos dentro do app. Preço, pagamento, reembolsos e histórico de compras seguem as informações e regras da Apple."],
    ["Etiquetas e limites", "Números de caixa e avisos como Frágil são lembretes para seus registros e não garantem como a transportadora vai manusear a caixa. O app não substitui orientação profissional de mudança ou segurança."],
    ["Licença e direitos do consumidor", "O Contrato de Licença de Usuário Final padrão da Apple se aplica ao app. Esta página não limita os direitos do consumidor previstos na legislação aplicável."]]},
},
}

# Locale folders used by the public pages and corresponding App Store Connect locale codes.
LANGS = list(DATA)
PAGE_FILES = {"home":"index.html", "privacy":"privacy.html", "support":"support.html", "terms":"terms.html"}

def page_dir(code: str) -> Path:
    return ROOT / DATA[code]["folder"]

def rel_page(source_code: str, target_code: str, target_page: str) -> str:
    src = page_dir(source_code)
    dst = page_dir(target_code) / PAGE_FILES[target_page]
    return os.path.relpath(dst, src).replace(os.sep, "/")

def section_html(sections: list[list[str]]) -> str:
    return "\n".join(f"<section><h2>{escape(h)}</h2><p>{escape(p)}</p></section>" for h,p in sections)

def make_page(code: str, which: str) -> str:
    d = DATA[code]
    page = d[which]
    path = page_dir(code)
    css = "./site.css" if not d["folder"] else "../site.css"
    nav = d["nav"]
    home_href = rel_page(code, code, "home")
    language_links = "\n".join(
        f'<a lang="{DATA[target]["html"]}" href="{escape(rel_page(code,target,which), quote=True)}">{escape(DATA[target]["language"])}</a>'
        for target in LANGS
    )
    nav_links = "\n".join(
        f'<a href="{escape(rel_page(code,code,key), quote=True)}">{escape(nav[i])}</a>'
        for i,key in enumerate(("home","privacy","support","terms"))
    )
    lead = f'<p class="lead">{escape(page["lead"])}</p>' if page.get("lead") else ""
    sections = section_html(page.get("sections", []))
    extras = ""
    if which == "home":
        extras = f'<p class="store"><a href="{STORE}">{escape(d["store"])}</a></p>'
    elif which == "support":
        extras = f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>'
    elif which == "terms":
        extras = f'<p><a href="{EULA}">{escape(d["eula"])}</a></p>'
    return f'''<!doctype html>
<html lang="{escape(d["html"], quote=True)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(page["title"])}</title>
<meta name="description" content="{escape(page["lead"], quote=True)}">
<link rel="stylesheet" href="{css}">
</head>
<body>
<main>
<header>
<a href="{escape(home_href, quote=True)}">{escape(d["brand"])}</a>
<details class="language-picker"><summary>{escape(nav[4])}: {escape(d["language"])}</summary><nav class="language-list" aria-label="{escape(nav[4], quote=True)}">{language_links}</nav></details>
</header>
<h1>{escape(page["title"])}</h1>
{lead}
{sections}
{extras}
<footer>
<nav aria-label="{escape(nav[0], quote=True)}">{nav_links}</nav>
<p class="note">© 2026 · {escape(d["updated"])}</p>
</footer>
</main>
</body>
</html>
'''

for code in LANGS:
    folder = page_dir(code)
    folder.mkdir(parents=True, exist_ok=True)
    for which, filename in PAGE_FILES.items():
        (folder / filename).write_text(make_page(code, which), encoding="utf-8")
print(f"Generated {len(LANGS) * len(PAGE_FILES)} localized pages under {ROOT}")
