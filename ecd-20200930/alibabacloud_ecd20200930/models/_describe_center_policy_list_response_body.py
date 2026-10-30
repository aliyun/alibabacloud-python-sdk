# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeCenterPolicyListResponseBody(DaraModel):
    def __init__(
        self,
        describe_policy_groups: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # 雲端電腦原則的詳細資訊。
        self.describe_policy_groups = describe_policy_groups
        # 請求 ID。
        self.request_id = request_id
        # 查詢結果總數。
        self.total_count = total_count

    def validate(self):
        if self.describe_policy_groups:
            for v1 in self.describe_policy_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DescribePolicyGroups'] = []
        if self.describe_policy_groups is not None:
            for k1 in self.describe_policy_groups:
                result['DescribePolicyGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_policy_groups = []
        if m.get('DescribePolicyGroups') is not None:
            for k1 in m.get('DescribePolicyGroups'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroups()
                self.describe_policy_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroups(DaraModel):
    def __init__(
        self,
        academic_proxy: str = None,
        admin_access: str = None,
        admin_keyboard_on_full_screen: str = None,
        admin_keyboard_on_windows: str = None,
        admin_monitor: int = None,
        app_content_protection: str = None,
        app_screenshot_buckets: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAppScreenshotBuckets] = None,
        authorize_access_policy_rules: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules] = None,
        authorize_security_policy_rules: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules] = None,
        auto_reconnect: str = None,
        auto_save_app_screenshot: str = None,
        camera_redirect: str = None,
        client_control_menu: str = None,
        client_create_snapshot: str = None,
        client_hibernate: str = None,
        client_restart: str = None,
        client_shutdown: str = None,
        client_types: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsClientTypes] = None,
        clipboard: str = None,
        color_enhancement: str = None,
        cpd_drive_clipboard: str = None,
        cpu_down_grade_duration: int = None,
        cpu_overload: str = None,
        cpu_processors: List[str] = None,
        cpu_protected_mode: str = None,
        cpu_rate_limit: int = None,
        cpu_sample_duration: int = None,
        cpu_single_rate_limit: int = None,
        desktop_count: int = None,
        desktop_group_count: int = None,
        device_connect_hint: str = None,
        device_redirects: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDeviceRedirects] = None,
        device_rules: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDeviceRules] = None,
        disconnect_keep_session: str = None,
        disconnect_keep_session_time: int = None,
        disk_overload: str = None,
        display_mode: str = None,
        domain_register_value: str = None,
        domain_resolve_rule: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDomainResolveRule] = None,
        domain_resolve_rule_type: str = None,
        end_user_apply_admin_coordinate: str = None,
        end_user_count: str = None,
        end_user_group_coordinate: str = None,
        external_drive: str = None,
        file_migrate: str = None,
        file_transfer_address: str = None,
        file_transfer_in_size: str = None,
        file_transfer_in_unit: str = None,
        file_transfer_out_size: str = None,
        file_transfer_out_unit: str = None,
        file_transfer_size_limit: str = None,
        file_transfer_speed: str = None,
        file_transfer_speed_location: str = None,
        folder_sync: str = None,
        gpu_acceleration: str = None,
        hover_config_msg: str = None,
        hover_hibernate: str = None,
        hover_restart: str = None,
        hover_shutdown: str = None,
        html_5access: str = None,
        html_5file_transfer: str = None,
        internet_communication_protocol: str = None,
        internet_printer: str = None,
        keyboard_control: str = None,
        kms_server: str = None,
        kms_server_config: str = None,
        local_drive: str = None,
        max_reconnect_time: int = None,
        mcp_service: str = None,
        memory_down_grade_duration: int = None,
        memory_overload: str = None,
        memory_processors: List[str] = None,
        memory_protected_mode: str = None,
        memory_rate_limit: int = None,
        memory_sample_duration: int = None,
        memory_single_rate_limit: int = None,
        mobile_restart: str = None,
        mobile_safe_menu: str = None,
        mobile_shutdown: str = None,
        mobile_wuying_keeper: str = None,
        mobile_wy_assistant: str = None,
        model_library: str = None,
        multi_screen: str = None,
        name: str = None,
        net_redirect: str = None,
        net_redirect_rule: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsNetRedirectRule] = None,
        network_printer: str = None,
        no_operation_disconnect: str = None,
        no_operation_disconnect_time: int = None,
        organization_count: str = None,
        policy_group_id: str = None,
        policy_group_type: str = None,
        policy_status: str = None,
        port_proxy: str = None,
        printer_alert: str = None,
        printer_alert_content: str = None,
        printer_alert_title: str = None,
        printer_redirection: str = None,
        quality_enhancement: str = None,
        record_content: str = None,
        record_content_expires: int = None,
        record_event_duration: int = None,
        record_event_file_paths: List[str] = None,
        record_event_registers: List[str] = None,
        recording: str = None,
        recording_audio: str = None,
        recording_duration: int = None,
        recording_end_time: str = None,
        recording_expires: int = None,
        recording_fps: int = None,
        recording_start_time: str = None,
        recording_user_notify: str = None,
        recording_user_notify_message: str = None,
        remote_coordinate: str = None,
        reset_desktop: str = None,
        resolution_dpi: int = None,
        resolution_height: int = None,
        resolution_model: str = None,
        resolution_width: int = None,
        resource_group_count: int = None,
        safe_menu: str = None,
        scope: str = None,
        scope_value: List[str] = None,
        screen_display_mode: str = None,
        smooth_enhancement: str = None,
        status_monitor: str = None,
        streaming_mode: str = None,
        target_fps: int = None,
        taskbar: str = None,
        three_screen: str = None,
        usb_redirect: str = None,
        usb_supply_redirect_rule: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule] = None,
        use_time: str = None,
        video_enc_avg_kbps: int = None,
        video_enc_max_qp: int = None,
        video_enc_min_qp: int = None,
        video_enc_peak_kbps: int = None,
        video_enc_policy: str = None,
        video_redirect: str = None,
        visual_quality: str = None,
        watermark: str = None,
        watermark_anti_cam: str = None,
        watermark_color: int = None,
        watermark_custom_text: str = None,
        watermark_degree: float = None,
        watermark_font_size: int = None,
        watermark_font_style: str = None,
        watermark_power: str = None,
        watermark_row_amount: int = None,
        watermark_security: str = None,
        watermark_shadow: str = None,
        watermark_transparency_value: int = None,
        watermark_type: str = None,
        wuying_keeper: str = None,
        wy_assistant: str = None,
    ):
        # 學術代理功能開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.academic_proxy = academic_proxy
        # 使用者連線雲端電腦後是否具有管理員權限。
        # 
        # > 該功能處於定向邀測中，暫不對外開放。
        self.admin_access = admin_access
        # 全螢幕模式下管理員鍵盤控制開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.admin_keyboard_on_full_screen = admin_keyboard_on_full_screen
        # Windows 系統內管理員鍵盤控制開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.admin_keyboard_on_windows = admin_keyboard_on_windows
        # 管理員監控開關。取值範圍：
        # - 1：開啟。
        # - 0：關閉。
        self.admin_monitor = admin_monitor
        # 是否開啟防截圖功能。
        self.app_content_protection = app_content_protection
        # 防截圖行動裝置截圖自訂 OSS Bucket 清單。
        self.app_screenshot_buckets = app_screenshot_buckets
        # 用戶端存取 IP 白名單。
        self.authorize_access_policy_rules = authorize_access_policy_rules
        # 安全性群組管控規則清單。
        self.authorize_security_policy_rules = authorize_security_policy_rules
        # 用戶端自動重新連線開關。
        self.auto_reconnect = auto_reconnect
        # 自動儲存行動裝置截圖。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.auto_save_app_screenshot = auto_save_app_screenshot
        # 是否開啟本機攝影機重新導向。
        self.camera_redirect = camera_redirect
        # 用戶端控制選單顯示開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.client_control_menu = client_control_menu
        # 用戶端建立自訂快照功能開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.client_create_snapshot = client_create_snapshot
        # 用戶端休眠選單開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.client_hibernate = client_hibernate
        # 用戶端重新啟動選單開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.client_restart = client_restart
        # 用戶端關機選單開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.client_shutdown = client_shutdown
        # 登入方式管控規則。
        self.client_types = client_types
        # 剪貼簿權限。
        self.clipboard = clipboard
        # 設計及 3D 應用場景選擇是否開啟色彩增強。
        self.color_enhancement = color_enhancement
        # 本機驅動程式剪貼簿功能開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.cpd_drive_clipboard = cpd_drive_clipboard
        # CPU 降頻時長，取值範圍： 30\\~120。單位：秒。
        self.cpu_down_grade_duration = cpu_down_grade_duration
        # CPU 負載保護開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.cpu_overload = cpu_overload
        # 處理程序名稱。
        self.cpu_processors = cpu_processors
        # CPU 保護模式開關。
        self.cpu_protected_mode = cpu_protected_mode
        # CPU 整體使用率百分比，取值範圍： 70\\~90。
        self.cpu_rate_limit = cpu_rate_limit
        # CPU 整體取樣時長，取值範圍： 10\\~60。單位：秒。
        self.cpu_sample_duration = cpu_sample_duration
        # CPU 單核心使用率百分比，取值範圍： 70\\~100。
        self.cpu_single_rate_limit = cpu_single_rate_limit
        # 已關聯該原則的雲端電腦數量。
        self.desktop_count = desktop_count
        # 已關聯該原則的雲端電腦集區數量。
        self.desktop_group_count = desktop_group_count
        # 周邊裝置連線提示控制。
        self.device_connect_hint = device_connect_hint
        # 裝置重新導向規則。
        self.device_redirects = device_redirects
        # 自訂周邊裝置規則。
        self.device_rules = device_rules
        # 工作階段斷線保留。
        # > 僅適用於雲端應用程式原則。
        self.disconnect_keep_session = disconnect_keep_session
        # 工作階段斷線保留時長。單位：秒。
        # > 僅適用於雲端應用程式原則。
        self.disconnect_keep_session_time = disconnect_keep_session_time
        # 磁碟負載保護開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.disk_overload = disk_overload
        # 顯示模式。
        self.display_mode = display_mode
        # 網域解析生效欄位。
        self.domain_register_value = domain_register_value
        # 網域解析原則詳情。
        self.domain_resolve_rule = domain_resolve_rule
        # 網域解析原則開關。
        self.domain_resolve_rule_type = domain_resolve_rule_type
        # 使用者請求管理員協助。
        self.end_user_apply_admin_coordinate = end_user_apply_admin_coordinate
        # 關聯的終端使用者數量。
        self.end_user_count = end_user_count
        # 同一個辦公網路下使用者共享雲端電腦。
        self.end_user_group_coordinate = end_user_group_coordinate
        # 外接儲存裝置使用開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.external_drive = external_drive
        # 檔案遷移。
        self.file_migrate = file_migrate
        # 檔案傳輸功能的服務位址。
        self.file_transfer_address = file_transfer_address
        # 單次傳入雲端電腦的檔案大小限制，需與傳入單位參數配合使用。
        self.file_transfer_in_size = file_transfer_in_size
        # 單次傳入雲端電腦的檔案大小限制單位。
        self.file_transfer_in_unit = file_transfer_in_unit
        # 單次從雲端電腦傳出的檔案大小限制，需與傳出單位參數配合使用。
        self.file_transfer_out_size = file_transfer_out_size
        # 單次從雲端電腦傳出的檔案大小限制單位。
        self.file_transfer_out_unit = file_transfer_out_unit
        # 檔案傳輸大小限制開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.file_transfer_size_limit = file_transfer_size_limit
        # 檔案傳輸速度檔位。
        self.file_transfer_speed = file_transfer_speed
        # 用戶端設定的檔案傳輸速度生效位置。
        self.file_transfer_speed_location = file_transfer_speed_location
        # 檔案同步開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.folder_sync = folder_sync
        # 是否為圖形型規格雲端電腦開啟畫質策略。對雲端電腦效能和使用體驗要求較高時，例如專業設計場景下，建議開啟該策略。
        self.gpu_acceleration = gpu_acceleration
        # 懸浮球設定訊息提示開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.hover_config_msg = hover_config_msg
        # 懸浮球休眠按鈕開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.hover_hibernate = hover_hibernate
        # 懸浮球重新啟動按鈕開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.hover_restart = hover_restart
        # 懸浮球關機按鈕開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.hover_shutdown = hover_shutdown
        # Web用戶端存取策略。
        self.html_5access = html_5access
        # Web用戶端檔案傳輸策略。
        self.html_5file_transfer = html_5file_transfer
        # 網路通訊協定。
        self.internet_communication_protocol = internet_communication_protocol
        # 網路印表機功能開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.internet_printer = internet_printer
        # 懸浮球鍵盤控制開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.keyboard_control = keyboard_control
        # KMS 伺服器開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.kms_server = kms_server
        # KMS 伺服器設定，格式為位址:連接埠。
        self.kms_server_config = kms_server_config
        # 本機磁碟映射權限。
        self.local_drive = local_drive
        # 雲端電腦由於客觀原因造成中斷連線的最大連線重試時間。取值範圍：30\\~7200，單位：秒。
        self.max_reconnect_time = max_reconnect_time
        # 開啟 MCP 服務。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.mcp_service = mcp_service
        # 單個處理程序記憶體降頻時長，取值範圍： 30\\~120。單位：秒。
        self.memory_down_grade_duration = memory_down_grade_duration
        # 記憶體負載保護開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.memory_overload = memory_overload
        # 處理程序名稱。
        self.memory_processors = memory_processors
        # 記憶體保護模式開關。
        self.memory_protected_mode = memory_protected_mode
        # 記憶體整體使用率百分比，取值範圍： 70\\~90。
        self.memory_rate_limit = memory_rate_limit
        # 記憶體整體取樣時長，取值範圍： 30\\~60。單位：秒。
        self.memory_sample_duration = memory_sample_duration
        # 單個處理程序記憶體使用率百分比，取值範圍： 30\\~60。
        self.memory_single_rate_limit = memory_single_rate_limit
        # 透過行動端（Android用戶端<props="china">和iOS用戶端）連線雲端電腦時，是否在雲端電腦懸浮球內提供重新啟動按鈕。
        # 
        # > 僅適用於V7.4或更高版本的行動端。
        self.mobile_restart = mobile_restart
        # 行動端Windows 安全性控制開關。
        self.mobile_safe_menu = mobile_safe_menu
        # 透過行動端（Android用戶端<props="china">和iOS用戶端）連線雲端電腦時，是否在雲端電腦懸浮球內提供關機按鈕。
        # 
        # > 僅適用於V7.4或更高版本的行動端。
        self.mobile_shutdown = mobile_shutdown
        # 行動端無影管家開關。
        self.mobile_wuying_keeper = mobile_wuying_keeper
        # 行動端小穎的開關。
        self.mobile_wy_assistant = mobile_wy_assistant
        # 模型庫功能開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.model_library = model_library
        # 多螢幕顯示功能開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.multi_screen = multi_screen
        # 策略名稱。
        self.name = name
        # 網路重新導向。
        # 
        # > 該功能處於定向邀測中，暫不對外開放。
        self.net_redirect = net_redirect
        # 網路重新導向策略詳細資訊。
        # 
        # > 該功能處於定向邀測中，暫不對外開放。
        # >
        self.net_redirect_rule = net_redirect_rule
        # 網路印表機功能開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.network_printer = network_printer
        # 無操作中斷連線。
        # > 僅適用於雲端應用策略。
        self.no_operation_disconnect = no_operation_disconnect
        # 無操作中斷連線時長。單位：秒。
        # > 僅適用於雲端應用策略。
        self.no_operation_disconnect_time = no_operation_disconnect_time
        # 關聯的組織數量。
        self.organization_count = organization_count
        # 策略ID。
        self.policy_group_id = policy_group_id
        # 策略類型。
        self.policy_group_type = policy_group_type
        # 雲端電腦策略狀態。
        self.policy_status = policy_status
        # 連接埠代理功能開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.port_proxy = port_proxy
        # 印表機彈出視窗提示。取值範圍：
        # - default：預設值。
        # - off：關閉。
        # - custom：自訂。
        self.printer_alert = printer_alert
        # 印表機彈出視窗提示內容。
        self.printer_alert_content = printer_alert_content
        # 印表機彈出視窗提示標題。
        self.printer_alert_title = printer_alert_title
        # 印表機重新導向策略。
        self.printer_redirection = printer_redirection
        # 設計及3D應用場景選擇是否開啟畫質增強。
        self.quality_enhancement = quality_enhancement
        # 是否開啟自訂螢幕錄影。
        self.record_content = record_content
        # 自訂螢幕錄影的檔案過期時間，預設30天。
        self.record_content_expires = record_content_expires
        # 螢幕錄影稽核中偵測到事件發生後螢幕錄影的時長。單位：分鐘。取值範圍：10\\~60。
        self.record_event_duration = record_event_duration
        # 螢幕錄影稽核中的檔案監控絕對路徑。
        self.record_event_file_paths = record_event_file_paths
        # 螢幕錄影稽核中的登錄檔監控絕對路徑。
        self.record_event_registers = record_event_registers
        # 是否開啟螢幕錄影。
        self.recording = recording
        # 錄製雲端電腦聲音選項。
        self.recording_audio = recording_audio
        # 螢幕錄影檔案閱覽時長，單位為分鐘。錄製檔案會根據您設定的時長自動分割並上傳至儲存空間，檔案達到300MB時優先滾動更新。
        self.recording_duration = recording_duration
        # 螢幕錄影結束時間，取值：HH:MM:SS。只有Recording取值是period時，該傳回值有實際意義。
        self.recording_end_time = recording_end_time
        # 螢幕錄影檔案的保留時間。取值範圍為1\\~180天。
        self.recording_expires = recording_expires
        # 螢幕錄影幀率。單位：FPS（幀/秒）。
        self.recording_fps = recording_fps
        # 螢幕錄影開始時間，取值：HH:MM:SS。只有Recording取值是period時，該傳回值有實際意義。
        self.recording_start_time = recording_start_time
        # 提示終端客戶已開啟螢幕錄影。
        self.recording_user_notify = recording_user_notify
        # 提示終端客戶開啟螢幕錄影的資訊。
        self.recording_user_notify_message = recording_user_notify_message
        # 遠端協助鍵盤與滑鼠控制權限。
        self.remote_coordinate = remote_coordinate
        # 重置雲端電腦。
        self.reset_desktop = reset_desktop
        # 螢幕解析度的 DPI 值。
        self.resolution_dpi = resolution_dpi
        # 解析度的高度。單位：畫素。
        self.resolution_height = resolution_height
        # 解析度類型。
        self.resolution_model = resolution_model
        # 解析度的寬度。單位：畫素。
        self.resolution_width = resolution_width
        # 已關聯該策略的資源群組數量。
        self.resource_group_count = resource_group_count
        # 安全中心快速鍵開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.safe_menu = safe_menu
        # 策略的生效範圍。
        self.scope = scope
        # 生效的 CIDR Block。
        self.scope_value = scope_value
        # 螢幕顯示模式。
        self.screen_display_mode = screen_display_mode
        # 日常辦公場景選擇，是否開啟平滑度增強。
        self.smooth_enhancement = smooth_enhancement
        # 是否在雲端電腦懸浮球內提供狀態監控功能入口。
        self.status_monitor = status_monitor
        # 串流模式適配場景。
        self.streaming_mode = streaming_mode
        # 目標幀率，取值範圍：10\\~60。
        self.target_fps = target_fps
        # 應用程式工作列。
        # > 僅適用於雲端應用程式策略。
        self.taskbar = taskbar
        # 三螢幕開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.three_screen = three_screen
        # USB 重新導向。
        self.usb_redirect = usb_redirect
        # USB 重新導向規則。
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        # 懸浮球使用時長顯示開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.use_time = use_time
        # 影片編碼平均位元率。單位：Kbps。取值範圍：1000\\~50000。
        self.video_enc_avg_kbps = video_enc_avg_kbps
        # 影片編碼最大 QP，畫面最低品質，取值範圍：0\\~51。
        self.video_enc_max_qp = video_enc_max_qp
        # 影片編碼最小 QP，最高品質。取值範圍：0\\~51。
        self.video_enc_min_qp = video_enc_min_qp
        # 影片編碼峰值位元率。單位：Kbps。取值範圍：1000~50000。
        self.video_enc_peak_kbps = video_enc_peak_kbps
        # 影片編碼策略。
        self.video_enc_policy = video_enc_policy
        # 多媒體重新導向。
        self.video_redirect = video_redirect
        # 影像顯示品質策略。
        self.visual_quality = visual_quality
        # 浮水印。
        self.watermark = watermark
        # 隱藏式浮水印防拍照功能。
        self.watermark_anti_cam = watermark_anti_cam
        # 浮水印字型顏色。取值範圍：0\\~16777215。
        self.watermark_color = watermark_color
        # 若參數 `WatermarkType` 傳入 `custom`，則必須同時透過參數 `WatermarkCustomText` 傳入自訂文字的內容。
        self.watermark_custom_text = watermark_custom_text
        # 浮水印傾斜度。取值範圍：-10\\~-30。
        self.watermark_degree = watermark_degree
        # 浮水印字型大小。取值範圍：10\\~20。
        self.watermark_font_size = watermark_font_size
        # 浮水印字型樣式。
        self.watermark_font_style = watermark_font_style
        # 隱藏式浮水印增強功能。
        self.watermark_power = watermark_power
        # 浮水印行數。
        self.watermark_row_amount = watermark_row_amount
        # 隱藏式浮水印安全優先規則。
        self.watermark_security = watermark_security
        # 浮水印陰影效果開關。取值範圍：
        # - on：開啟。
        # - off：關閉。
        self.watermark_shadow = watermark_shadow
        # 浮水印透明度，值越大，透明度越小。取值範圍：10\\~100。
        self.watermark_transparency_value = watermark_transparency_value
        # 浮水印類型。
        self.watermark_type = watermark_type
        # 無影管家開關。
        self.wuying_keeper = wuying_keeper
        # 是否在雲端電腦懸浮球內提供無影 AI 助手功能入口。
        self.wy_assistant = wy_assistant

    def validate(self):
        if self.app_screenshot_buckets:
            for v1 in self.app_screenshot_buckets:
                 if v1:
                    v1.validate()
        if self.authorize_access_policy_rules:
            for v1 in self.authorize_access_policy_rules:
                 if v1:
                    v1.validate()
        if self.authorize_security_policy_rules:
            for v1 in self.authorize_security_policy_rules:
                 if v1:
                    v1.validate()
        if self.client_types:
            for v1 in self.client_types:
                 if v1:
                    v1.validate()
        if self.device_redirects:
            for v1 in self.device_redirects:
                 if v1:
                    v1.validate()
        if self.device_rules:
            for v1 in self.device_rules:
                 if v1:
                    v1.validate()
        if self.domain_resolve_rule:
            for v1 in self.domain_resolve_rule:
                 if v1:
                    v1.validate()
        if self.net_redirect_rule:
            for v1 in self.net_redirect_rule:
                 if v1:
                    v1.validate()
        if self.usb_supply_redirect_rule:
            for v1 in self.usb_supply_redirect_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.academic_proxy is not None:
            result['AcademicProxy'] = self.academic_proxy

        if self.admin_access is not None:
            result['AdminAccess'] = self.admin_access

        if self.admin_keyboard_on_full_screen is not None:
            result['AdminKeyboardOnFullScreen'] = self.admin_keyboard_on_full_screen

        if self.admin_keyboard_on_windows is not None:
            result['AdminKeyboardOnWindows'] = self.admin_keyboard_on_windows

        if self.admin_monitor is not None:
            result['AdminMonitor'] = self.admin_monitor

        if self.app_content_protection is not None:
            result['AppContentProtection'] = self.app_content_protection

        result['AppScreenshotBuckets'] = []
        if self.app_screenshot_buckets is not None:
            for k1 in self.app_screenshot_buckets:
                result['AppScreenshotBuckets'].append(k1.to_map() if k1 else None)

        result['AuthorizeAccessPolicyRules'] = []
        if self.authorize_access_policy_rules is not None:
            for k1 in self.authorize_access_policy_rules:
                result['AuthorizeAccessPolicyRules'].append(k1.to_map() if k1 else None)

        result['AuthorizeSecurityPolicyRules'] = []
        if self.authorize_security_policy_rules is not None:
            for k1 in self.authorize_security_policy_rules:
                result['AuthorizeSecurityPolicyRules'].append(k1.to_map() if k1 else None)

        if self.auto_reconnect is not None:
            result['AutoReconnect'] = self.auto_reconnect

        if self.auto_save_app_screenshot is not None:
            result['AutoSaveAppScreenshot'] = self.auto_save_app_screenshot

        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect

        if self.client_control_menu is not None:
            result['ClientControlMenu'] = self.client_control_menu

        if self.client_create_snapshot is not None:
            result['ClientCreateSnapshot'] = self.client_create_snapshot

        if self.client_hibernate is not None:
            result['ClientHibernate'] = self.client_hibernate

        if self.client_restart is not None:
            result['ClientRestart'] = self.client_restart

        if self.client_shutdown is not None:
            result['ClientShutdown'] = self.client_shutdown

        result['ClientTypes'] = []
        if self.client_types is not None:
            for k1 in self.client_types:
                result['ClientTypes'].append(k1.to_map() if k1 else None)

        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        if self.color_enhancement is not None:
            result['ColorEnhancement'] = self.color_enhancement

        if self.cpd_drive_clipboard is not None:
            result['CpdDriveClipboard'] = self.cpd_drive_clipboard

        if self.cpu_down_grade_duration is not None:
            result['CpuDownGradeDuration'] = self.cpu_down_grade_duration

        if self.cpu_overload is not None:
            result['CpuOverload'] = self.cpu_overload

        if self.cpu_processors is not None:
            result['CpuProcessors'] = self.cpu_processors

        if self.cpu_protected_mode is not None:
            result['CpuProtectedMode'] = self.cpu_protected_mode

        if self.cpu_rate_limit is not None:
            result['CpuRateLimit'] = self.cpu_rate_limit

        if self.cpu_sample_duration is not None:
            result['CpuSampleDuration'] = self.cpu_sample_duration

        if self.cpu_single_rate_limit is not None:
            result['CpuSingleRateLimit'] = self.cpu_single_rate_limit

        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count

        if self.desktop_group_count is not None:
            result['DesktopGroupCount'] = self.desktop_group_count

        if self.device_connect_hint is not None:
            result['DeviceConnectHint'] = self.device_connect_hint

        result['DeviceRedirects'] = []
        if self.device_redirects is not None:
            for k1 in self.device_redirects:
                result['DeviceRedirects'].append(k1.to_map() if k1 else None)

        result['DeviceRules'] = []
        if self.device_rules is not None:
            for k1 in self.device_rules:
                result['DeviceRules'].append(k1.to_map() if k1 else None)

        if self.disconnect_keep_session is not None:
            result['DisconnectKeepSession'] = self.disconnect_keep_session

        if self.disconnect_keep_session_time is not None:
            result['DisconnectKeepSessionTime'] = self.disconnect_keep_session_time

        if self.disk_overload is not None:
            result['DiskOverload'] = self.disk_overload

        if self.display_mode is not None:
            result['DisplayMode'] = self.display_mode

        if self.domain_register_value is not None:
            result['DomainRegisterValue'] = self.domain_register_value

        result['DomainResolveRule'] = []
        if self.domain_resolve_rule is not None:
            for k1 in self.domain_resolve_rule:
                result['DomainResolveRule'].append(k1.to_map() if k1 else None)

        if self.domain_resolve_rule_type is not None:
            result['DomainResolveRuleType'] = self.domain_resolve_rule_type

        if self.end_user_apply_admin_coordinate is not None:
            result['EndUserApplyAdminCoordinate'] = self.end_user_apply_admin_coordinate

        if self.end_user_count is not None:
            result['EndUserCount'] = self.end_user_count

        if self.end_user_group_coordinate is not None:
            result['EndUserGroupCoordinate'] = self.end_user_group_coordinate

        if self.external_drive is not None:
            result['ExternalDrive'] = self.external_drive

        if self.file_migrate is not None:
            result['FileMigrate'] = self.file_migrate

        if self.file_transfer_address is not None:
            result['FileTransferAddress'] = self.file_transfer_address

        if self.file_transfer_in_size is not None:
            result['FileTransferInSize'] = self.file_transfer_in_size

        if self.file_transfer_in_unit is not None:
            result['FileTransferInUnit'] = self.file_transfer_in_unit

        if self.file_transfer_out_size is not None:
            result['FileTransferOutSize'] = self.file_transfer_out_size

        if self.file_transfer_out_unit is not None:
            result['FileTransferOutUnit'] = self.file_transfer_out_unit

        if self.file_transfer_size_limit is not None:
            result['FileTransferSizeLimit'] = self.file_transfer_size_limit

        if self.file_transfer_speed is not None:
            result['FileTransferSpeed'] = self.file_transfer_speed

        if self.file_transfer_speed_location is not None:
            result['FileTransferSpeedLocation'] = self.file_transfer_speed_location

        if self.folder_sync is not None:
            result['FolderSync'] = self.folder_sync

        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration

        if self.hover_config_msg is not None:
            result['HoverConfigMsg'] = self.hover_config_msg

        if self.hover_hibernate is not None:
            result['HoverHibernate'] = self.hover_hibernate

        if self.hover_restart is not None:
            result['HoverRestart'] = self.hover_restart

        if self.hover_shutdown is not None:
            result['HoverShutdown'] = self.hover_shutdown

        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access

        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer

        if self.internet_communication_protocol is not None:
            result['InternetCommunicationProtocol'] = self.internet_communication_protocol

        if self.internet_printer is not None:
            result['InternetPrinter'] = self.internet_printer

        if self.keyboard_control is not None:
            result['KeyboardControl'] = self.keyboard_control

        if self.kms_server is not None:
            result['KmsServer'] = self.kms_server

        if self.kms_server_config is not None:
            result['KmsServerConfig'] = self.kms_server_config

        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive

        if self.max_reconnect_time is not None:
            result['MaxReconnectTime'] = self.max_reconnect_time

        if self.mcp_service is not None:
            result['McpService'] = self.mcp_service

        if self.memory_down_grade_duration is not None:
            result['MemoryDownGradeDuration'] = self.memory_down_grade_duration

        if self.memory_overload is not None:
            result['MemoryOverload'] = self.memory_overload

        if self.memory_processors is not None:
            result['MemoryProcessors'] = self.memory_processors

        if self.memory_protected_mode is not None:
            result['MemoryProtectedMode'] = self.memory_protected_mode

        if self.memory_rate_limit is not None:
            result['MemoryRateLimit'] = self.memory_rate_limit

        if self.memory_sample_duration is not None:
            result['MemorySampleDuration'] = self.memory_sample_duration

        if self.memory_single_rate_limit is not None:
            result['MemorySingleRateLimit'] = self.memory_single_rate_limit

        if self.mobile_restart is not None:
            result['MobileRestart'] = self.mobile_restart

        if self.mobile_safe_menu is not None:
            result['MobileSafeMenu'] = self.mobile_safe_menu

        if self.mobile_shutdown is not None:
            result['MobileShutdown'] = self.mobile_shutdown

        if self.mobile_wuying_keeper is not None:
            result['MobileWuyingKeeper'] = self.mobile_wuying_keeper

        if self.mobile_wy_assistant is not None:
            result['MobileWyAssistant'] = self.mobile_wy_assistant

        if self.model_library is not None:
            result['ModelLibrary'] = self.model_library

        if self.multi_screen is not None:
            result['MultiScreen'] = self.multi_screen

        if self.name is not None:
            result['Name'] = self.name

        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect

        result['NetRedirectRule'] = []
        if self.net_redirect_rule is not None:
            for k1 in self.net_redirect_rule:
                result['NetRedirectRule'].append(k1.to_map() if k1 else None)

        if self.network_printer is not None:
            result['NetworkPrinter'] = self.network_printer

        if self.no_operation_disconnect is not None:
            result['NoOperationDisconnect'] = self.no_operation_disconnect

        if self.no_operation_disconnect_time is not None:
            result['NoOperationDisconnectTime'] = self.no_operation_disconnect_time

        if self.organization_count is not None:
            result['OrganizationCount'] = self.organization_count

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.port_proxy is not None:
            result['PortProxy'] = self.port_proxy

        if self.printer_alert is not None:
            result['PrinterAlert'] = self.printer_alert

        if self.printer_alert_content is not None:
            result['PrinterAlertContent'] = self.printer_alert_content

        if self.printer_alert_title is not None:
            result['PrinterAlertTitle'] = self.printer_alert_title

        if self.printer_redirection is not None:
            result['PrinterRedirection'] = self.printer_redirection

        if self.quality_enhancement is not None:
            result['QualityEnhancement'] = self.quality_enhancement

        if self.record_content is not None:
            result['RecordContent'] = self.record_content

        if self.record_content_expires is not None:
            result['RecordContentExpires'] = self.record_content_expires

        if self.record_event_duration is not None:
            result['RecordEventDuration'] = self.record_event_duration

        if self.record_event_file_paths is not None:
            result['RecordEventFilePaths'] = self.record_event_file_paths

        if self.record_event_registers is not None:
            result['RecordEventRegisters'] = self.record_event_registers

        if self.recording is not None:
            result['Recording'] = self.recording

        if self.recording_audio is not None:
            result['RecordingAudio'] = self.recording_audio

        if self.recording_duration is not None:
            result['RecordingDuration'] = self.recording_duration

        if self.recording_end_time is not None:
            result['RecordingEndTime'] = self.recording_end_time

        if self.recording_expires is not None:
            result['RecordingExpires'] = self.recording_expires

        if self.recording_fps is not None:
            result['RecordingFps'] = self.recording_fps

        if self.recording_start_time is not None:
            result['RecordingStartTime'] = self.recording_start_time

        if self.recording_user_notify is not None:
            result['RecordingUserNotify'] = self.recording_user_notify

        if self.recording_user_notify_message is not None:
            result['RecordingUserNotifyMessage'] = self.recording_user_notify_message

        if self.remote_coordinate is not None:
            result['RemoteCoordinate'] = self.remote_coordinate

        if self.reset_desktop is not None:
            result['ResetDesktop'] = self.reset_desktop

        if self.resolution_dpi is not None:
            result['ResolutionDpi'] = self.resolution_dpi

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_model is not None:
            result['ResolutionModel'] = self.resolution_model

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        if self.resource_group_count is not None:
            result['ResourceGroupCount'] = self.resource_group_count

        if self.safe_menu is not None:
            result['SafeMenu'] = self.safe_menu

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.scope_value is not None:
            result['ScopeValue'] = self.scope_value

        if self.screen_display_mode is not None:
            result['ScreenDisplayMode'] = self.screen_display_mode

        if self.smooth_enhancement is not None:
            result['SmoothEnhancement'] = self.smooth_enhancement

        if self.status_monitor is not None:
            result['StatusMonitor'] = self.status_monitor

        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode

        if self.target_fps is not None:
            result['TargetFps'] = self.target_fps

        if self.taskbar is not None:
            result['Taskbar'] = self.taskbar

        if self.three_screen is not None:
            result['ThreeScreen'] = self.three_screen

        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect

        result['UsbSupplyRedirectRule'] = []
        if self.usb_supply_redirect_rule is not None:
            for k1 in self.usb_supply_redirect_rule:
                result['UsbSupplyRedirectRule'].append(k1.to_map() if k1 else None)

        if self.use_time is not None:
            result['UseTime'] = self.use_time

        if self.video_enc_avg_kbps is not None:
            result['VideoEncAvgKbps'] = self.video_enc_avg_kbps

        if self.video_enc_max_qp is not None:
            result['VideoEncMaxQP'] = self.video_enc_max_qp

        if self.video_enc_min_qp is not None:
            result['VideoEncMinQP'] = self.video_enc_min_qp

        if self.video_enc_peak_kbps is not None:
            result['VideoEncPeakKbps'] = self.video_enc_peak_kbps

        if self.video_enc_policy is not None:
            result['VideoEncPolicy'] = self.video_enc_policy

        if self.video_redirect is not None:
            result['VideoRedirect'] = self.video_redirect

        if self.visual_quality is not None:
            result['VisualQuality'] = self.visual_quality

        if self.watermark is not None:
            result['Watermark'] = self.watermark

        if self.watermark_anti_cam is not None:
            result['WatermarkAntiCam'] = self.watermark_anti_cam

        if self.watermark_color is not None:
            result['WatermarkColor'] = self.watermark_color

        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text

        if self.watermark_degree is not None:
            result['WatermarkDegree'] = self.watermark_degree

        if self.watermark_font_size is not None:
            result['WatermarkFontSize'] = self.watermark_font_size

        if self.watermark_font_style is not None:
            result['WatermarkFontStyle'] = self.watermark_font_style

        if self.watermark_power is not None:
            result['WatermarkPower'] = self.watermark_power

        if self.watermark_row_amount is not None:
            result['WatermarkRowAmount'] = self.watermark_row_amount

        if self.watermark_security is not None:
            result['WatermarkSecurity'] = self.watermark_security

        if self.watermark_shadow is not None:
            result['WatermarkShadow'] = self.watermark_shadow

        if self.watermark_transparency_value is not None:
            result['WatermarkTransparencyValue'] = self.watermark_transparency_value

        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type

        if self.wuying_keeper is not None:
            result['WuyingKeeper'] = self.wuying_keeper

        if self.wy_assistant is not None:
            result['WyAssistant'] = self.wy_assistant

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcademicProxy') is not None:
            self.academic_proxy = m.get('AcademicProxy')

        if m.get('AdminAccess') is not None:
            self.admin_access = m.get('AdminAccess')

        if m.get('AdminKeyboardOnFullScreen') is not None:
            self.admin_keyboard_on_full_screen = m.get('AdminKeyboardOnFullScreen')

        if m.get('AdminKeyboardOnWindows') is not None:
            self.admin_keyboard_on_windows = m.get('AdminKeyboardOnWindows')

        if m.get('AdminMonitor') is not None:
            self.admin_monitor = m.get('AdminMonitor')

        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')

        self.app_screenshot_buckets = []
        if m.get('AppScreenshotBuckets') is not None:
            for k1 in m.get('AppScreenshotBuckets'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAppScreenshotBuckets()
                self.app_screenshot_buckets.append(temp_model.from_map(k1))

        self.authorize_access_policy_rules = []
        if m.get('AuthorizeAccessPolicyRules') is not None:
            for k1 in m.get('AuthorizeAccessPolicyRules'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules()
                self.authorize_access_policy_rules.append(temp_model.from_map(k1))

        self.authorize_security_policy_rules = []
        if m.get('AuthorizeSecurityPolicyRules') is not None:
            for k1 in m.get('AuthorizeSecurityPolicyRules'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules()
                self.authorize_security_policy_rules.append(temp_model.from_map(k1))

        if m.get('AutoReconnect') is not None:
            self.auto_reconnect = m.get('AutoReconnect')

        if m.get('AutoSaveAppScreenshot') is not None:
            self.auto_save_app_screenshot = m.get('AutoSaveAppScreenshot')

        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')

        if m.get('ClientControlMenu') is not None:
            self.client_control_menu = m.get('ClientControlMenu')

        if m.get('ClientCreateSnapshot') is not None:
            self.client_create_snapshot = m.get('ClientCreateSnapshot')

        if m.get('ClientHibernate') is not None:
            self.client_hibernate = m.get('ClientHibernate')

        if m.get('ClientRestart') is not None:
            self.client_restart = m.get('ClientRestart')

        if m.get('ClientShutdown') is not None:
            self.client_shutdown = m.get('ClientShutdown')

        self.client_types = []
        if m.get('ClientTypes') is not None:
            for k1 in m.get('ClientTypes'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsClientTypes()
                self.client_types.append(temp_model.from_map(k1))

        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        if m.get('ColorEnhancement') is not None:
            self.color_enhancement = m.get('ColorEnhancement')

        if m.get('CpdDriveClipboard') is not None:
            self.cpd_drive_clipboard = m.get('CpdDriveClipboard')

        if m.get('CpuDownGradeDuration') is not None:
            self.cpu_down_grade_duration = m.get('CpuDownGradeDuration')

        if m.get('CpuOverload') is not None:
            self.cpu_overload = m.get('CpuOverload')

        if m.get('CpuProcessors') is not None:
            self.cpu_processors = m.get('CpuProcessors')

        if m.get('CpuProtectedMode') is not None:
            self.cpu_protected_mode = m.get('CpuProtectedMode')

        if m.get('CpuRateLimit') is not None:
            self.cpu_rate_limit = m.get('CpuRateLimit')

        if m.get('CpuSampleDuration') is not None:
            self.cpu_sample_duration = m.get('CpuSampleDuration')

        if m.get('CpuSingleRateLimit') is not None:
            self.cpu_single_rate_limit = m.get('CpuSingleRateLimit')

        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')

        if m.get('DesktopGroupCount') is not None:
            self.desktop_group_count = m.get('DesktopGroupCount')

        if m.get('DeviceConnectHint') is not None:
            self.device_connect_hint = m.get('DeviceConnectHint')

        self.device_redirects = []
        if m.get('DeviceRedirects') is not None:
            for k1 in m.get('DeviceRedirects'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDeviceRedirects()
                self.device_redirects.append(temp_model.from_map(k1))

        self.device_rules = []
        if m.get('DeviceRules') is not None:
            for k1 in m.get('DeviceRules'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDeviceRules()
                self.device_rules.append(temp_model.from_map(k1))

        if m.get('DisconnectKeepSession') is not None:
            self.disconnect_keep_session = m.get('DisconnectKeepSession')

        if m.get('DisconnectKeepSessionTime') is not None:
            self.disconnect_keep_session_time = m.get('DisconnectKeepSessionTime')

        if m.get('DiskOverload') is not None:
            self.disk_overload = m.get('DiskOverload')

        if m.get('DisplayMode') is not None:
            self.display_mode = m.get('DisplayMode')

        if m.get('DomainRegisterValue') is not None:
            self.domain_register_value = m.get('DomainRegisterValue')

        self.domain_resolve_rule = []
        if m.get('DomainResolveRule') is not None:
            for k1 in m.get('DomainResolveRule'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDomainResolveRule()
                self.domain_resolve_rule.append(temp_model.from_map(k1))

        if m.get('DomainResolveRuleType') is not None:
            self.domain_resolve_rule_type = m.get('DomainResolveRuleType')

        if m.get('EndUserApplyAdminCoordinate') is not None:
            self.end_user_apply_admin_coordinate = m.get('EndUserApplyAdminCoordinate')

        if m.get('EndUserCount') is not None:
            self.end_user_count = m.get('EndUserCount')

        if m.get('EndUserGroupCoordinate') is not None:
            self.end_user_group_coordinate = m.get('EndUserGroupCoordinate')

        if m.get('ExternalDrive') is not None:
            self.external_drive = m.get('ExternalDrive')

        if m.get('FileMigrate') is not None:
            self.file_migrate = m.get('FileMigrate')

        if m.get('FileTransferAddress') is not None:
            self.file_transfer_address = m.get('FileTransferAddress')

        if m.get('FileTransferInSize') is not None:
            self.file_transfer_in_size = m.get('FileTransferInSize')

        if m.get('FileTransferInUnit') is not None:
            self.file_transfer_in_unit = m.get('FileTransferInUnit')

        if m.get('FileTransferOutSize') is not None:
            self.file_transfer_out_size = m.get('FileTransferOutSize')

        if m.get('FileTransferOutUnit') is not None:
            self.file_transfer_out_unit = m.get('FileTransferOutUnit')

        if m.get('FileTransferSizeLimit') is not None:
            self.file_transfer_size_limit = m.get('FileTransferSizeLimit')

        if m.get('FileTransferSpeed') is not None:
            self.file_transfer_speed = m.get('FileTransferSpeed')

        if m.get('FileTransferSpeedLocation') is not None:
            self.file_transfer_speed_location = m.get('FileTransferSpeedLocation')

        if m.get('FolderSync') is not None:
            self.folder_sync = m.get('FolderSync')

        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')

        if m.get('HoverConfigMsg') is not None:
            self.hover_config_msg = m.get('HoverConfigMsg')

        if m.get('HoverHibernate') is not None:
            self.hover_hibernate = m.get('HoverHibernate')

        if m.get('HoverRestart') is not None:
            self.hover_restart = m.get('HoverRestart')

        if m.get('HoverShutdown') is not None:
            self.hover_shutdown = m.get('HoverShutdown')

        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('InternetCommunicationProtocol') is not None:
            self.internet_communication_protocol = m.get('InternetCommunicationProtocol')

        if m.get('InternetPrinter') is not None:
            self.internet_printer = m.get('InternetPrinter')

        if m.get('KeyboardControl') is not None:
            self.keyboard_control = m.get('KeyboardControl')

        if m.get('KmsServer') is not None:
            self.kms_server = m.get('KmsServer')

        if m.get('KmsServerConfig') is not None:
            self.kms_server_config = m.get('KmsServerConfig')

        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')

        if m.get('MaxReconnectTime') is not None:
            self.max_reconnect_time = m.get('MaxReconnectTime')

        if m.get('McpService') is not None:
            self.mcp_service = m.get('McpService')

        if m.get('MemoryDownGradeDuration') is not None:
            self.memory_down_grade_duration = m.get('MemoryDownGradeDuration')

        if m.get('MemoryOverload') is not None:
            self.memory_overload = m.get('MemoryOverload')

        if m.get('MemoryProcessors') is not None:
            self.memory_processors = m.get('MemoryProcessors')

        if m.get('MemoryProtectedMode') is not None:
            self.memory_protected_mode = m.get('MemoryProtectedMode')

        if m.get('MemoryRateLimit') is not None:
            self.memory_rate_limit = m.get('MemoryRateLimit')

        if m.get('MemorySampleDuration') is not None:
            self.memory_sample_duration = m.get('MemorySampleDuration')

        if m.get('MemorySingleRateLimit') is not None:
            self.memory_single_rate_limit = m.get('MemorySingleRateLimit')

        if m.get('MobileRestart') is not None:
            self.mobile_restart = m.get('MobileRestart')

        if m.get('MobileSafeMenu') is not None:
            self.mobile_safe_menu = m.get('MobileSafeMenu')

        if m.get('MobileShutdown') is not None:
            self.mobile_shutdown = m.get('MobileShutdown')

        if m.get('MobileWuyingKeeper') is not None:
            self.mobile_wuying_keeper = m.get('MobileWuyingKeeper')

        if m.get('MobileWyAssistant') is not None:
            self.mobile_wy_assistant = m.get('MobileWyAssistant')

        if m.get('ModelLibrary') is not None:
            self.model_library = m.get('ModelLibrary')

        if m.get('MultiScreen') is not None:
            self.multi_screen = m.get('MultiScreen')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')

        self.net_redirect_rule = []
        if m.get('NetRedirectRule') is not None:
            for k1 in m.get('NetRedirectRule'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsNetRedirectRule()
                self.net_redirect_rule.append(temp_model.from_map(k1))

        if m.get('NetworkPrinter') is not None:
            self.network_printer = m.get('NetworkPrinter')

        if m.get('NoOperationDisconnect') is not None:
            self.no_operation_disconnect = m.get('NoOperationDisconnect')

        if m.get('NoOperationDisconnectTime') is not None:
            self.no_operation_disconnect_time = m.get('NoOperationDisconnectTime')

        if m.get('OrganizationCount') is not None:
            self.organization_count = m.get('OrganizationCount')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('PortProxy') is not None:
            self.port_proxy = m.get('PortProxy')

        if m.get('PrinterAlert') is not None:
            self.printer_alert = m.get('PrinterAlert')

        if m.get('PrinterAlertContent') is not None:
            self.printer_alert_content = m.get('PrinterAlertContent')

        if m.get('PrinterAlertTitle') is not None:
            self.printer_alert_title = m.get('PrinterAlertTitle')

        if m.get('PrinterRedirection') is not None:
            self.printer_redirection = m.get('PrinterRedirection')

        if m.get('QualityEnhancement') is not None:
            self.quality_enhancement = m.get('QualityEnhancement')

        if m.get('RecordContent') is not None:
            self.record_content = m.get('RecordContent')

        if m.get('RecordContentExpires') is not None:
            self.record_content_expires = m.get('RecordContentExpires')

        if m.get('RecordEventDuration') is not None:
            self.record_event_duration = m.get('RecordEventDuration')

        if m.get('RecordEventFilePaths') is not None:
            self.record_event_file_paths = m.get('RecordEventFilePaths')

        if m.get('RecordEventRegisters') is not None:
            self.record_event_registers = m.get('RecordEventRegisters')

        if m.get('Recording') is not None:
            self.recording = m.get('Recording')

        if m.get('RecordingAudio') is not None:
            self.recording_audio = m.get('RecordingAudio')

        if m.get('RecordingDuration') is not None:
            self.recording_duration = m.get('RecordingDuration')

        if m.get('RecordingEndTime') is not None:
            self.recording_end_time = m.get('RecordingEndTime')

        if m.get('RecordingExpires') is not None:
            self.recording_expires = m.get('RecordingExpires')

        if m.get('RecordingFps') is not None:
            self.recording_fps = m.get('RecordingFps')

        if m.get('RecordingStartTime') is not None:
            self.recording_start_time = m.get('RecordingStartTime')

        if m.get('RecordingUserNotify') is not None:
            self.recording_user_notify = m.get('RecordingUserNotify')

        if m.get('RecordingUserNotifyMessage') is not None:
            self.recording_user_notify_message = m.get('RecordingUserNotifyMessage')

        if m.get('RemoteCoordinate') is not None:
            self.remote_coordinate = m.get('RemoteCoordinate')

        if m.get('ResetDesktop') is not None:
            self.reset_desktop = m.get('ResetDesktop')

        if m.get('ResolutionDpi') is not None:
            self.resolution_dpi = m.get('ResolutionDpi')

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionModel') is not None:
            self.resolution_model = m.get('ResolutionModel')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        if m.get('ResourceGroupCount') is not None:
            self.resource_group_count = m.get('ResourceGroupCount')

        if m.get('SafeMenu') is not None:
            self.safe_menu = m.get('SafeMenu')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ScopeValue') is not None:
            self.scope_value = m.get('ScopeValue')

        if m.get('ScreenDisplayMode') is not None:
            self.screen_display_mode = m.get('ScreenDisplayMode')

        if m.get('SmoothEnhancement') is not None:
            self.smooth_enhancement = m.get('SmoothEnhancement')

        if m.get('StatusMonitor') is not None:
            self.status_monitor = m.get('StatusMonitor')

        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')

        if m.get('TargetFps') is not None:
            self.target_fps = m.get('TargetFps')

        if m.get('Taskbar') is not None:
            self.taskbar = m.get('Taskbar')

        if m.get('ThreeScreen') is not None:
            self.three_screen = m.get('ThreeScreen')

        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')

        self.usb_supply_redirect_rule = []
        if m.get('UsbSupplyRedirectRule') is not None:
            for k1 in m.get('UsbSupplyRedirectRule'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule()
                self.usb_supply_redirect_rule.append(temp_model.from_map(k1))

        if m.get('UseTime') is not None:
            self.use_time = m.get('UseTime')

        if m.get('VideoEncAvgKbps') is not None:
            self.video_enc_avg_kbps = m.get('VideoEncAvgKbps')

        if m.get('VideoEncMaxQP') is not None:
            self.video_enc_max_qp = m.get('VideoEncMaxQP')

        if m.get('VideoEncMinQP') is not None:
            self.video_enc_min_qp = m.get('VideoEncMinQP')

        if m.get('VideoEncPeakKbps') is not None:
            self.video_enc_peak_kbps = m.get('VideoEncPeakKbps')

        if m.get('VideoEncPolicy') is not None:
            self.video_enc_policy = m.get('VideoEncPolicy')

        if m.get('VideoRedirect') is not None:
            self.video_redirect = m.get('VideoRedirect')

        if m.get('VisualQuality') is not None:
            self.visual_quality = m.get('VisualQuality')

        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')

        if m.get('WatermarkAntiCam') is not None:
            self.watermark_anti_cam = m.get('WatermarkAntiCam')

        if m.get('WatermarkColor') is not None:
            self.watermark_color = m.get('WatermarkColor')

        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')

        if m.get('WatermarkDegree') is not None:
            self.watermark_degree = m.get('WatermarkDegree')

        if m.get('WatermarkFontSize') is not None:
            self.watermark_font_size = m.get('WatermarkFontSize')

        if m.get('WatermarkFontStyle') is not None:
            self.watermark_font_style = m.get('WatermarkFontStyle')

        if m.get('WatermarkPower') is not None:
            self.watermark_power = m.get('WatermarkPower')

        if m.get('WatermarkRowAmount') is not None:
            self.watermark_row_amount = m.get('WatermarkRowAmount')

        if m.get('WatermarkSecurity') is not None:
            self.watermark_security = m.get('WatermarkSecurity')

        if m.get('WatermarkShadow') is not None:
            self.watermark_shadow = m.get('WatermarkShadow')

        if m.get('WatermarkTransparencyValue') is not None:
            self.watermark_transparency_value = m.get('WatermarkTransparencyValue')

        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')

        if m.get('WuyingKeeper') is not None:
            self.wuying_keeper = m.get('WuyingKeeper')

        if m.get('WyAssistant') is not None:
            self.wy_assistant = m.get('WyAssistant')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        product_id: str = None,
        usb_redirect_type: int = None,
        usb_rule_type: int = None,
        vendor_id: str = None,
    ):
        # 規則描述。
        self.description = description
        # 產品 ID。
        self.product_id = product_id
        # USB 重新導向類型。
        self.usb_redirect_type = usb_redirect_type
        # USB 重新導向規則類型。
        self.usb_rule_type = usb_rule_type
        # 生產廠商 ID。參見 [Valid USB Vendor IDs (VIDs)](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf)。
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.usb_redirect_type is not None:
            result['UsbRedirectType'] = self.usb_redirect_type

        if self.usb_rule_type is not None:
            result['UsbRuleType'] = self.usb_rule_type

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('UsbRedirectType') is not None:
            self.usb_redirect_type = m.get('UsbRedirectType')

        if m.get('UsbRuleType') is not None:
            self.usb_rule_type = m.get('UsbRuleType')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsNetRedirectRule(DaraModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
        rule_type: str = None,
    ):
        # 網域。
        self.domain = domain
        # 重新導向策略。
        self.policy = policy
        # 規則類型。
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDomainResolveRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain: str = None,
        policy: str = None,
    ):
        # 原則描述。
        self.description = description
        # 網域。
        self.domain = domain
        # 解析原則。
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDeviceRules(DaraModel):
    def __init__(
        self,
        device_name: str = None,
        device_pid: str = None,
        device_type: str = None,
        device_vid: str = None,
        opt_command: str = None,
        platforms: str = None,
        redirect_type: str = None,
    ):
        # 裝置名稱。
        self.device_name = device_name
        # 產品 ID。
        self.device_pid = device_pid
        # 周邊裝置類型。
        self.device_type = device_type
        # 生產廠商 ID。參見 [Valid USB Vendor IDs (VIDs)](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf)。
        self.device_vid = device_vid
        # 連結最佳化指令。
        self.opt_command = opt_command
        # 裝置規則適用的平台類型。
        self.platforms = platforms
        # 重新導向類型。
        self.redirect_type = redirect_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.device_pid is not None:
            result['DevicePid'] = self.device_pid

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.device_vid is not None:
            result['DeviceVid'] = self.device_vid

        if self.opt_command is not None:
            result['OptCommand'] = self.opt_command

        if self.platforms is not None:
            result['Platforms'] = self.platforms

        if self.redirect_type is not None:
            result['RedirectType'] = self.redirect_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('DevicePid') is not None:
            self.device_pid = m.get('DevicePid')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('DeviceVid') is not None:
            self.device_vid = m.get('DeviceVid')

        if m.get('OptCommand') is not None:
            self.opt_command = m.get('OptCommand')

        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')

        if m.get('RedirectType') is not None:
            self.redirect_type = m.get('RedirectType')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDeviceRedirects(DaraModel):
    def __init__(
        self,
        device_type: str = None,
        redirect_type: str = None,
    ):
        # 周邊裝置類型。
        self.device_type = device_type
        # 重新導向類型。
        self.redirect_type = redirect_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.redirect_type is not None:
            result['RedirectType'] = self.redirect_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('RedirectType') is not None:
            self.redirect_type = m.get('RedirectType')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsClientTypes(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # 用戶端類型。
        self.client_type = client_type
        # 是否允許某一類型的用戶端登入雲端桌面。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: str = None,
        type: str = None,
    ):
        # 安全性群組管控規則的對象，CIDR 格式的 IPv4 位址區段。
        self.cidr_ip = cidr_ip
        # 安全性群組管控規則的描述資訊。
        self.description = description
        # 安全性群組管控規則的通訊協定類型。
        self.ip_protocol = ip_protocol
        # 安全性群組管控規則的授權原則。
        self.policy = policy
        # 安全性群組管控規則的連接埠範圍。
        self.port_range = port_range
        # 安全性群組管控規則的優先順序，數字越小，代表優先順序越高。
        self.priority = priority
        # 安全性群組管控規則的規則方向。
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip

        if self.description is not None:
            result['Description'] = self.description

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        # 用戶端存取 IP 位址區段。格式為 CIDR 格式的 IPv4 位址區段。
        self.cidr_ip = cidr_ip
        # 用戶端存取 IP 位址區段備註資訊。
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

class DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAppScreenshotBuckets(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_region_id: str = None,
    ):
        # Bucket 名稱。
        self.bucket_name = bucket_name
        # 使用者 OSS Bucket 所在地域，必須與 Bucket 的實際地域一致。
        self.bucket_region_id = bucket_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.bucket_region_id is not None:
            result['BucketRegionId'] = self.bucket_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('BucketRegionId') is not None:
            self.bucket_region_id = m.get('BucketRegionId')

        return self

