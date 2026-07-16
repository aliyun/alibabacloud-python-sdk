# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyCenterPolicyRequest(DaraModel):
    def __init__(
        self,
        academic_proxy: str = None,
        admin_access: str = None,
        admin_keyboard_on_full_screen: str = None,
        admin_keyboard_on_windows: str = None,
        app_content_protection: str = None,
        authorize_access_policy_rule: List[main_models.ModifyCenterPolicyRequestAuthorizeAccessPolicyRule] = None,
        authorize_security_policy_rule: List[main_models.ModifyCenterPolicyRequestAuthorizeSecurityPolicyRule] = None,
        auto_reconnect: str = None,
        business_channel: str = None,
        business_type: int = None,
        camera_redirect: str = None,
        client_control_menu: str = None,
        client_create_snapshot: str = None,
        client_type: List[main_models.ModifyCenterPolicyRequestClientType] = None,
        clipboard: str = None,
        clipboard_graineds: List[main_models.ModifyCenterPolicyRequestClipboardGraineds] = None,
        clipboard_scope: str = None,
        color_enhancement: str = None,
        cpd_drive_clipboard: str = None,
        cpu_down_grade_duration: int = None,
        cpu_overload: str = None,
        cpu_processors: List[str] = None,
        cpu_protected_mode: str = None,
        cpu_rate_limit: int = None,
        cpu_sample_duration: int = None,
        cpu_single_rate_limit: int = None,
        description: str = None,
        device_connect_hint: str = None,
        device_redirects: List[main_models.ModifyCenterPolicyRequestDeviceRedirects] = None,
        device_rules: List[main_models.ModifyCenterPolicyRequestDeviceRules] = None,
        disconnect_keep_session: str = None,
        disconnect_keep_session_time: int = None,
        disk_overload: str = None,
        display_mode: str = None,
        domain_resolve_rule: List[main_models.ModifyCenterPolicyRequestDomainResolveRule] = None,
        domain_resolve_rule_type: str = None,
        enable_session_rate_limiting: str = None,
        end_user_apply_admin_coordinate: str = None,
        end_user_group_coordinate: str = None,
        external_drive: str = None,
        file_migrate: str = None,
        file_transfer_address: str = None,
        file_transfer_speed: str = None,
        file_transfer_speed_location: str = None,
        gpu_acceleration: str = None,
        hover_config_msg: str = None,
        html_5file_transfer: str = None,
        internet_communication_protocol: str = None,
        internet_printer: str = None,
        local_drive: str = None,
        max_reconnect_time: int = None,
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
        net_redirect_rule: List[main_models.ModifyCenterPolicyRequestNetRedirectRule] = None,
        no_operation_disconnect: str = None,
        no_operation_disconnect_time: int = None,
        policy_group_id: str = None,
        port_proxy: str = None,
        printer_redirect: str = None,
        quality_enhancement: str = None,
        record_event_duration: int = None,
        record_event_file_exts: List[str] = None,
        record_event_file_paths: List[str] = None,
        record_event_levels: List[main_models.ModifyCenterPolicyRequestRecordEventLevels] = None,
        record_event_registers: List[str] = None,
        record_events: List[str] = None,
        recording: str = None,
        recording_audio: str = None,
        recording_duration: int = None,
        recording_end_time: str = None,
        recording_expires: int = None,
        recording_fps: str = None,
        recording_start_time: str = None,
        recording_user_notify: str = None,
        recording_user_notify_message: str = None,
        region_id: str = None,
        remote_coordinate: str = None,
        reset_desktop: str = None,
        resolution_dpi: int = None,
        resolution_height: int = None,
        resolution_model: str = None,
        resolution_width: int = None,
        resource_type: str = None,
        revoke_access_policy_rule: List[main_models.ModifyCenterPolicyRequestRevokeAccessPolicyRule] = None,
        revoke_security_policy_rule: List[main_models.ModifyCenterPolicyRequestRevokeSecurityPolicyRule] = None,
        safe_menu: str = None,
        scope: str = None,
        scope_value: List[str] = None,
        screen_display_mode: str = None,
        session_max_rate_kbps: int = None,
        smooth_enhancement: str = None,
        status_monitor: str = None,
        streaming_mode: str = None,
        target_fps: int = None,
        taskbar: str = None,
        usb_redirect: str = None,
        usb_supply_redirect_rule: List[main_models.ModifyCenterPolicyRequestUsbSupplyRedirectRule] = None,
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
        watermark_column_amount: int = None,
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
        self.academic_proxy = academic_proxy
        # Specifies whether users have administrator permissions after logging on to cloud computers.
        # 
        # > This feature is in invitational preview and not available to the public.
        self.admin_access = admin_access
        self.admin_keyboard_on_full_screen = admin_keyboard_on_full_screen
        self.admin_keyboard_on_windows = admin_keyboard_on_windows
        # Specifies whether to enable anti-screenshot protection.
        self.app_content_protection = app_content_protection
        # List of new client IP address whitelists.
        self.authorize_access_policy_rule = authorize_access_policy_rule
        # List of new security group control rules.
        self.authorize_security_policy_rule = authorize_security_policy_rule
        # Automatically reconnect after disconnection
        self.auto_reconnect = auto_reconnect
        self.business_channel = business_channel
        # The business type.
        # 
        # This parameter is required.
        self.business_type = business_type
        # Local camera redirection. This parameter takes effect only if DeviceRedirects does not include a local camera redirection policy.
        self.camera_redirect = camera_redirect
        # Event level for screen recording
        self.client_control_menu = client_control_menu
        self.client_create_snapshot = client_create_snapshot
        # List of client login control rules. Controls which clients can access cloud computers.
        self.client_type = client_type
        # The clipboard permissions.
        self.clipboard = clipboard
        self.clipboard_graineds = clipboard_graineds
        self.clipboard_scope = clipboard_scope
        # Specifies whether to enable color enhancement for design and 3D applications.
        self.color_enhancement = color_enhancement
        self.cpd_drive_clipboard = cpd_drive_clipboard
        # CPU downclocking duration. Valid values: 30 to 120. Unit: seconds.
        self.cpu_down_grade_duration = cpu_down_grade_duration
        self.cpu_overload = cpu_overload
        # The name of the process.
        self.cpu_processors = cpu_processors
        # CPU protection mode switch.
        self.cpu_protected_mode = cpu_protected_mode
        # Overall CPU usage percentage. Valid values: 70 to 90.
        self.cpu_rate_limit = cpu_rate_limit
        # Overall CPU sampling duration. Valid values: 10 to 60. Unit: seconds.
        self.cpu_sample_duration = cpu_sample_duration
        # Single-core CPU usage percentage. Valid values: 70 to 100.
        self.cpu_single_rate_limit = cpu_single_rate_limit
        self.description = description
        # Peripheral connection prompt control.
        self.device_connect_hint = device_connect_hint
        # Device redirection rules.
        self.device_redirects = device_redirects
        # Custom peripheral rules.
        self.device_rules = device_rules
        # Session retention after disconnection.
        # 
        # > This parameter applies only to cloud application policies.
        self.disconnect_keep_session = disconnect_keep_session
        # Session retention duration after disconnection. Valid values: 30 to 7200. Unit: seconds.
        # 
        # > This parameter applies only to cloud application policies.
        self.disconnect_keep_session_time = disconnect_keep_session_time
        self.disk_overload = disk_overload
        # Display mode.
        self.display_mode = display_mode
        # Domain name resolution policies.
        self.domain_resolve_rule = domain_resolve_rule
        # Domain name resolution policy type.
        self.domain_resolve_rule_type = domain_resolve_rule_type
        # Session bandwidth throttling.
        self.enable_session_rate_limiting = enable_session_rate_limiting
        # User requests administrator assistance.
        self.end_user_apply_admin_coordinate = end_user_apply_admin_coordinate
        # Users on the same office network share cloud computers.
        self.end_user_group_coordinate = end_user_group_coordinate
        self.external_drive = external_drive
        # File migration.
        self.file_migrate = file_migrate
        self.file_transfer_address = file_transfer_address
        self.file_transfer_speed = file_transfer_speed
        # Screen recording event suffix
        self.file_transfer_speed_location = file_transfer_speed_location
        # Specifies whether to enable the image quality policy for graphics-intensive cloud computers. Enable this policy for scenarios such as professional design where high performance and user experience are required.
        self.gpu_acceleration = gpu_acceleration
        self.hover_config_msg = hover_config_msg
        # The file transfer policy for web clients.
        self.html_5file_transfer = html_5file_transfer
        # Network communication protocol.
        self.internet_communication_protocol = internet_communication_protocol
        # Wuying Keeper toggle for mobile devices
        self.internet_printer = internet_printer
        # The local disk mapping permissions.
        self.local_drive = local_drive
        # Maximum reconnection retry time after an unexpected disconnection. Valid values: 30 to 7200. Unit: seconds.
        self.max_reconnect_time = max_reconnect_time
        # Memory downclocking duration per process. Valid values: 30 to 120. Unit: seconds.
        self.memory_down_grade_duration = memory_down_grade_duration
        self.memory_overload = memory_overload
        # The name of the process.
        self.memory_processors = memory_processors
        # Memory protection mode switch.
        self.memory_protected_mode = memory_protected_mode
        # Overall memory usage percentage. Valid values: 70 to 90.
        self.memory_rate_limit = memory_rate_limit
        # Overall memory sampling duration. Valid values: 30 to 60. Unit: seconds.
        self.memory_sample_duration = memory_sample_duration
        # Memory usage per process percentage. Valid values: 30 to 60.
        self.memory_single_rate_limit = memory_single_rate_limit
        # Specifies whether to provide the Restart button in the cloud computer floating ball when connecting via mobile clients (Android and iOS clients).
        # 
        # > This feature applies only to mobile clients of version 7.4 or later.
        self.mobile_restart = mobile_restart
        # The security button toggle for Windows systems on mobile devices
        self.mobile_safe_menu = mobile_safe_menu
        # Specifies whether to provide the Shutdown button in the cloud computer floating ball when connecting via mobile clients (Android and iOS clients).
        # 
        # > This feature applies only to mobile clients of version 7.4 or later.
        self.mobile_shutdown = mobile_shutdown
        # Wuying Keeper toggle for mobile devices
        self.mobile_wuying_keeper = mobile_wuying_keeper
        # Mobile Wy Assistant Toggle
        self.mobile_wy_assistant = mobile_wy_assistant
        self.model_library = model_library
        self.multi_screen = multi_screen
        # The policy name.
        self.name = name
        # Specifies whether to enable network redirection.
        # 
        # > This feature is in invitational preview and not available to the public.
        self.net_redirect = net_redirect
        # Network redirection policy details.
        # 
        # > This feature is in invitational preview and not available to the public.
        self.net_redirect_rule = net_redirect_rule
        # Disconnect on inactivity.
        # 
        # > This parameter applies only to cloud application policies.
        self.no_operation_disconnect = no_operation_disconnect
        # Inactivity disconnect duration. Valid values: 120 to 7200. Unit: seconds.
        # 
        # > This parameter applies only to cloud application policies.
        self.no_operation_disconnect_time = no_operation_disconnect_time
        # The cloud computer policy ID.
        # 
        # This parameter is required.
        self.policy_group_id = policy_group_id
        self.port_proxy = port_proxy
        # The printer redirection policy. This parameter takes effect only if DeviceRedirects does not include a printer redirection policy.
        self.printer_redirect = printer_redirect
        # Specifies whether to enable image quality enhancement for design and 3D applications.
        self.quality_enhancement = quality_enhancement
        # Screen recording duration after an event is detected in audit. Unit: minutes. Valid values: 10 to 60.
        self.record_event_duration = record_event_duration
        # File extensions for screen recording events
        self.record_event_file_exts = record_event_file_exts
        # Absolute paths for file monitoring in screen recording audit.
        self.record_event_file_paths = record_event_file_paths
        # Levels of screen recording events
        self.record_event_levels = record_event_levels
        # Absolute paths for registry monitoring in screen recording audit.
        self.record_event_registers = record_event_registers
        # List of screen recording events.
        self.record_events = record_events
        # Specifies whether to enable screen recording.
        self.recording = recording
        # Cloud computer audio recording option.
        self.recording_audio = recording_audio
        # Screen recording file viewing duration in minutes. Recording files are automatically split based on the specified duration and uploaded to the storage bucket. When a file reaches 300 MB, it is prioritized for rolling updates. Valid values: 10 to 60.
        self.recording_duration = recording_duration
        # Screen recording end time in HH:MM:SS format. This parameter is meaningful only when `Recording` is set to `PERIOD`.
        self.recording_end_time = recording_end_time
        # Retention period of screen recording files. Valid values: 1 to 180 days.
        self.recording_expires = recording_expires
        # Screen recording frame rate. Unit: FPS.
        self.recording_fps = recording_fps
        # Screen recording start time in HH:MM:SS format. This parameter is meaningful only when `Recording` is set to `PERIOD`.
        self.recording_start_time = recording_start_time
        # Notify end users when screen recording is enabled.
        self.recording_user_notify = recording_user_notify
        # Message to notify end users when screen recording is enabled.
        self.recording_user_notify_message = recording_user_notify_message
        # The region ID. Set the value to `cn-shanghai`.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Keyboard and mouse control permissions for remote assistance.
        self.remote_coordinate = remote_coordinate
        # Reset cloud computer.
        self.reset_desktop = reset_desktop
        self.resolution_dpi = resolution_dpi
        # Resolution height. Unit: pixels. Valid values for cloud applications: 500 to 50000. Valid values for cloud computers: 480 to 4096.
        self.resolution_height = resolution_height
        # Resolution type.
        self.resolution_model = resolution_model
        # Resolution width. Unit: pixels. Valid values for cloud applications: 500 to 50000. Valid values for cloud computers: 480 to 4096.
        self.resolution_width = resolution_width
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of client IP address whitelists to delete.
        self.revoke_access_policy_rule = revoke_access_policy_rule
        # List of security group control rules to delete.
        self.revoke_security_policy_rule = revoke_security_policy_rule
        # Security button toggle for Windows systems on mobile devices
        self.safe_menu = safe_menu
        # The effective scope of the policy.
        self.scope = scope
        # Specify when `Scope` is set to `IP`. Takes effect only when `Scope` is `IP`.
        self.scope_value = scope_value
        # Xiao Ying toggle for mobile devices
        self.screen_display_mode = screen_display_mode
        # Maximum session bandwidth throttling value. Unit: Kbps. Valid values: 2000 to 100000.
        self.session_max_rate_kbps = session_max_rate_kbps
        # Specifies whether to enable smoothness enhancement for daily office scenarios.
        self.smooth_enhancement = smooth_enhancement
        # Specifies whether to provide the status monitoring entry in the cloud computer floating ball.
        self.status_monitor = status_monitor
        # Streaming mode adaptation scenario.
        self.streaming_mode = streaming_mode
        # Target frame rate. Valid values: 10 to 60.
        self.target_fps = target_fps
        # Application taskbar.
        # 
        # > This parameter applies only to cloud application policies.
        self.taskbar = taskbar
        # USB redirection.
        self.usb_redirect = usb_redirect
        # USB redirection rules.
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        self.use_time = use_time
        # Average bitrate for video encoding. Unit: Kbps. Valid values: 1000 to 50000.
        self.video_enc_avg_kbps = video_enc_avg_kbps
        # Maximum QP for video encoding, representing lowest quality. Valid values: 0 to 51.
        self.video_enc_max_qp = video_enc_max_qp
        # Minimum QP for video encoding, representing highest quality. Valid values: 0 to 51.
        self.video_enc_min_qp = video_enc_min_qp
        # Peak bitrate for video encoding. Unit: Kbps. Valid values: 1000 to 50000.
        self.video_enc_peak_kbps = video_enc_peak_kbps
        # Video encoding policy.
        self.video_enc_policy = video_enc_policy
        # Multimedia redirection.
        self.video_redirect = video_redirect
        # The image display quality policy.
        self.visual_quality = visual_quality
        # Watermark.
        self.watermark = watermark
        # Blind watermark anti-photo feature.
        self.watermark_anti_cam = watermark_anti_cam
        # Watermark font color. Valid values: 0 to 16777215.
        self.watermark_color = watermark_color
        # Number of watermark columns. Valid values: 3 to 10.
        self.watermark_column_amount = watermark_column_amount
        # If you set `WatermarkType` to `custom`, you must also specify custom text using the `WatermarkCustomText` parameter.
        self.watermark_custom_text = watermark_custom_text
        # Watermark tilt angle. Valid values: -10 to -30.
        self.watermark_degree = watermark_degree
        # Watermark font size. Valid values: 10 to 20.
        self.watermark_font_size = watermark_font_size
        # Watermark font style.
        self.watermark_font_style = watermark_font_style
        # Blind watermark enhancement feature.
        self.watermark_power = watermark_power
        # Number of watermark rows. Valid values: 3 to 10.
        self.watermark_row_amount = watermark_row_amount
        # Blind watermark security priority rule.
        self.watermark_security = watermark_security
        self.watermark_shadow = watermark_shadow
        # Watermark opacity. A higher value means lower transparency. Valid values: 10 to 100.
        self.watermark_transparency_value = watermark_transparency_value
        # The watermark type. You can select up to three types, separated by commas.
        # 
        # > If you set this parameter to `custom`, you must also specify custom text using the `WatermarkCustomText` parameter.
        self.watermark_type = watermark_type
        # Wuying Keeper switch.
        self.wuying_keeper = wuying_keeper
        # Specifies whether to provide the Wuying AI Assistant entry in the cloud computer floating ball when connecting via desktop clients (including Windows and macOS clients).
        # 
        # > This feature applies only to desktop clients of version 7.7 or later.
        self.wy_assistant = wy_assistant

    def validate(self):
        if self.authorize_access_policy_rule:
            for v1 in self.authorize_access_policy_rule:
                 if v1:
                    v1.validate()
        if self.authorize_security_policy_rule:
            for v1 in self.authorize_security_policy_rule:
                 if v1:
                    v1.validate()
        if self.client_type:
            for v1 in self.client_type:
                 if v1:
                    v1.validate()
        if self.clipboard_graineds:
            for v1 in self.clipboard_graineds:
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
        if self.record_event_levels:
            for v1 in self.record_event_levels:
                 if v1:
                    v1.validate()
        if self.revoke_access_policy_rule:
            for v1 in self.revoke_access_policy_rule:
                 if v1:
                    v1.validate()
        if self.revoke_security_policy_rule:
            for v1 in self.revoke_security_policy_rule:
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

        if self.app_content_protection is not None:
            result['AppContentProtection'] = self.app_content_protection

        result['AuthorizeAccessPolicyRule'] = []
        if self.authorize_access_policy_rule is not None:
            for k1 in self.authorize_access_policy_rule:
                result['AuthorizeAccessPolicyRule'].append(k1.to_map() if k1 else None)

        result['AuthorizeSecurityPolicyRule'] = []
        if self.authorize_security_policy_rule is not None:
            for k1 in self.authorize_security_policy_rule:
                result['AuthorizeSecurityPolicyRule'].append(k1.to_map() if k1 else None)

        if self.auto_reconnect is not None:
            result['AutoReconnect'] = self.auto_reconnect

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect

        if self.client_control_menu is not None:
            result['ClientControlMenu'] = self.client_control_menu

        if self.client_create_snapshot is not None:
            result['ClientCreateSnapshot'] = self.client_create_snapshot

        result['ClientType'] = []
        if self.client_type is not None:
            for k1 in self.client_type:
                result['ClientType'].append(k1.to_map() if k1 else None)

        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        result['ClipboardGraineds'] = []
        if self.clipboard_graineds is not None:
            for k1 in self.clipboard_graineds:
                result['ClipboardGraineds'].append(k1.to_map() if k1 else None)

        if self.clipboard_scope is not None:
            result['ClipboardScope'] = self.clipboard_scope

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

        if self.description is not None:
            result['Description'] = self.description

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

        result['DomainResolveRule'] = []
        if self.domain_resolve_rule is not None:
            for k1 in self.domain_resolve_rule:
                result['DomainResolveRule'].append(k1.to_map() if k1 else None)

        if self.domain_resolve_rule_type is not None:
            result['DomainResolveRuleType'] = self.domain_resolve_rule_type

        if self.enable_session_rate_limiting is not None:
            result['EnableSessionRateLimiting'] = self.enable_session_rate_limiting

        if self.end_user_apply_admin_coordinate is not None:
            result['EndUserApplyAdminCoordinate'] = self.end_user_apply_admin_coordinate

        if self.end_user_group_coordinate is not None:
            result['EndUserGroupCoordinate'] = self.end_user_group_coordinate

        if self.external_drive is not None:
            result['ExternalDrive'] = self.external_drive

        if self.file_migrate is not None:
            result['FileMigrate'] = self.file_migrate

        if self.file_transfer_address is not None:
            result['FileTransferAddress'] = self.file_transfer_address

        if self.file_transfer_speed is not None:
            result['FileTransferSpeed'] = self.file_transfer_speed

        if self.file_transfer_speed_location is not None:
            result['FileTransferSpeedLocation'] = self.file_transfer_speed_location

        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration

        if self.hover_config_msg is not None:
            result['HoverConfigMsg'] = self.hover_config_msg

        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer

        if self.internet_communication_protocol is not None:
            result['InternetCommunicationProtocol'] = self.internet_communication_protocol

        if self.internet_printer is not None:
            result['InternetPrinter'] = self.internet_printer

        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive

        if self.max_reconnect_time is not None:
            result['MaxReconnectTime'] = self.max_reconnect_time

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

        if self.no_operation_disconnect is not None:
            result['NoOperationDisconnect'] = self.no_operation_disconnect

        if self.no_operation_disconnect_time is not None:
            result['NoOperationDisconnectTime'] = self.no_operation_disconnect_time

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.port_proxy is not None:
            result['PortProxy'] = self.port_proxy

        if self.printer_redirect is not None:
            result['PrinterRedirect'] = self.printer_redirect

        if self.quality_enhancement is not None:
            result['QualityEnhancement'] = self.quality_enhancement

        if self.record_event_duration is not None:
            result['RecordEventDuration'] = self.record_event_duration

        if self.record_event_file_exts is not None:
            result['RecordEventFileExts'] = self.record_event_file_exts

        if self.record_event_file_paths is not None:
            result['RecordEventFilePaths'] = self.record_event_file_paths

        result['RecordEventLevels'] = []
        if self.record_event_levels is not None:
            for k1 in self.record_event_levels:
                result['RecordEventLevels'].append(k1.to_map() if k1 else None)

        if self.record_event_registers is not None:
            result['RecordEventRegisters'] = self.record_event_registers

        if self.record_events is not None:
            result['RecordEvents'] = self.record_events

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['RevokeAccessPolicyRule'] = []
        if self.revoke_access_policy_rule is not None:
            for k1 in self.revoke_access_policy_rule:
                result['RevokeAccessPolicyRule'].append(k1.to_map() if k1 else None)

        result['RevokeSecurityPolicyRule'] = []
        if self.revoke_security_policy_rule is not None:
            for k1 in self.revoke_security_policy_rule:
                result['RevokeSecurityPolicyRule'].append(k1.to_map() if k1 else None)

        if self.safe_menu is not None:
            result['SafeMenu'] = self.safe_menu

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.scope_value is not None:
            result['ScopeValue'] = self.scope_value

        if self.screen_display_mode is not None:
            result['ScreenDisplayMode'] = self.screen_display_mode

        if self.session_max_rate_kbps is not None:
            result['SessionMaxRateKbps'] = self.session_max_rate_kbps

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

        if self.watermark_column_amount is not None:
            result['WatermarkColumnAmount'] = self.watermark_column_amount

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

        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')

        self.authorize_access_policy_rule = []
        if m.get('AuthorizeAccessPolicyRule') is not None:
            for k1 in m.get('AuthorizeAccessPolicyRule'):
                temp_model = main_models.ModifyCenterPolicyRequestAuthorizeAccessPolicyRule()
                self.authorize_access_policy_rule.append(temp_model.from_map(k1))

        self.authorize_security_policy_rule = []
        if m.get('AuthorizeSecurityPolicyRule') is not None:
            for k1 in m.get('AuthorizeSecurityPolicyRule'):
                temp_model = main_models.ModifyCenterPolicyRequestAuthorizeSecurityPolicyRule()
                self.authorize_security_policy_rule.append(temp_model.from_map(k1))

        if m.get('AutoReconnect') is not None:
            self.auto_reconnect = m.get('AutoReconnect')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')

        if m.get('ClientControlMenu') is not None:
            self.client_control_menu = m.get('ClientControlMenu')

        if m.get('ClientCreateSnapshot') is not None:
            self.client_create_snapshot = m.get('ClientCreateSnapshot')

        self.client_type = []
        if m.get('ClientType') is not None:
            for k1 in m.get('ClientType'):
                temp_model = main_models.ModifyCenterPolicyRequestClientType()
                self.client_type.append(temp_model.from_map(k1))

        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        self.clipboard_graineds = []
        if m.get('ClipboardGraineds') is not None:
            for k1 in m.get('ClipboardGraineds'):
                temp_model = main_models.ModifyCenterPolicyRequestClipboardGraineds()
                self.clipboard_graineds.append(temp_model.from_map(k1))

        if m.get('ClipboardScope') is not None:
            self.clipboard_scope = m.get('ClipboardScope')

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

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceConnectHint') is not None:
            self.device_connect_hint = m.get('DeviceConnectHint')

        self.device_redirects = []
        if m.get('DeviceRedirects') is not None:
            for k1 in m.get('DeviceRedirects'):
                temp_model = main_models.ModifyCenterPolicyRequestDeviceRedirects()
                self.device_redirects.append(temp_model.from_map(k1))

        self.device_rules = []
        if m.get('DeviceRules') is not None:
            for k1 in m.get('DeviceRules'):
                temp_model = main_models.ModifyCenterPolicyRequestDeviceRules()
                self.device_rules.append(temp_model.from_map(k1))

        if m.get('DisconnectKeepSession') is not None:
            self.disconnect_keep_session = m.get('DisconnectKeepSession')

        if m.get('DisconnectKeepSessionTime') is not None:
            self.disconnect_keep_session_time = m.get('DisconnectKeepSessionTime')

        if m.get('DiskOverload') is not None:
            self.disk_overload = m.get('DiskOverload')

        if m.get('DisplayMode') is not None:
            self.display_mode = m.get('DisplayMode')

        self.domain_resolve_rule = []
        if m.get('DomainResolveRule') is not None:
            for k1 in m.get('DomainResolveRule'):
                temp_model = main_models.ModifyCenterPolicyRequestDomainResolveRule()
                self.domain_resolve_rule.append(temp_model.from_map(k1))

        if m.get('DomainResolveRuleType') is not None:
            self.domain_resolve_rule_type = m.get('DomainResolveRuleType')

        if m.get('EnableSessionRateLimiting') is not None:
            self.enable_session_rate_limiting = m.get('EnableSessionRateLimiting')

        if m.get('EndUserApplyAdminCoordinate') is not None:
            self.end_user_apply_admin_coordinate = m.get('EndUserApplyAdminCoordinate')

        if m.get('EndUserGroupCoordinate') is not None:
            self.end_user_group_coordinate = m.get('EndUserGroupCoordinate')

        if m.get('ExternalDrive') is not None:
            self.external_drive = m.get('ExternalDrive')

        if m.get('FileMigrate') is not None:
            self.file_migrate = m.get('FileMigrate')

        if m.get('FileTransferAddress') is not None:
            self.file_transfer_address = m.get('FileTransferAddress')

        if m.get('FileTransferSpeed') is not None:
            self.file_transfer_speed = m.get('FileTransferSpeed')

        if m.get('FileTransferSpeedLocation') is not None:
            self.file_transfer_speed_location = m.get('FileTransferSpeedLocation')

        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')

        if m.get('HoverConfigMsg') is not None:
            self.hover_config_msg = m.get('HoverConfigMsg')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('InternetCommunicationProtocol') is not None:
            self.internet_communication_protocol = m.get('InternetCommunicationProtocol')

        if m.get('InternetPrinter') is not None:
            self.internet_printer = m.get('InternetPrinter')

        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')

        if m.get('MaxReconnectTime') is not None:
            self.max_reconnect_time = m.get('MaxReconnectTime')

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
                temp_model = main_models.ModifyCenterPolicyRequestNetRedirectRule()
                self.net_redirect_rule.append(temp_model.from_map(k1))

        if m.get('NoOperationDisconnect') is not None:
            self.no_operation_disconnect = m.get('NoOperationDisconnect')

        if m.get('NoOperationDisconnectTime') is not None:
            self.no_operation_disconnect_time = m.get('NoOperationDisconnectTime')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PortProxy') is not None:
            self.port_proxy = m.get('PortProxy')

        if m.get('PrinterRedirect') is not None:
            self.printer_redirect = m.get('PrinterRedirect')

        if m.get('QualityEnhancement') is not None:
            self.quality_enhancement = m.get('QualityEnhancement')

        if m.get('RecordEventDuration') is not None:
            self.record_event_duration = m.get('RecordEventDuration')

        if m.get('RecordEventFileExts') is not None:
            self.record_event_file_exts = m.get('RecordEventFileExts')

        if m.get('RecordEventFilePaths') is not None:
            self.record_event_file_paths = m.get('RecordEventFilePaths')

        self.record_event_levels = []
        if m.get('RecordEventLevels') is not None:
            for k1 in m.get('RecordEventLevels'):
                temp_model = main_models.ModifyCenterPolicyRequestRecordEventLevels()
                self.record_event_levels.append(temp_model.from_map(k1))

        if m.get('RecordEventRegisters') is not None:
            self.record_event_registers = m.get('RecordEventRegisters')

        if m.get('RecordEvents') is not None:
            self.record_events = m.get('RecordEvents')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.revoke_access_policy_rule = []
        if m.get('RevokeAccessPolicyRule') is not None:
            for k1 in m.get('RevokeAccessPolicyRule'):
                temp_model = main_models.ModifyCenterPolicyRequestRevokeAccessPolicyRule()
                self.revoke_access_policy_rule.append(temp_model.from_map(k1))

        self.revoke_security_policy_rule = []
        if m.get('RevokeSecurityPolicyRule') is not None:
            for k1 in m.get('RevokeSecurityPolicyRule'):
                temp_model = main_models.ModifyCenterPolicyRequestRevokeSecurityPolicyRule()
                self.revoke_security_policy_rule.append(temp_model.from_map(k1))

        if m.get('SafeMenu') is not None:
            self.safe_menu = m.get('SafeMenu')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ScopeValue') is not None:
            self.scope_value = m.get('ScopeValue')

        if m.get('ScreenDisplayMode') is not None:
            self.screen_display_mode = m.get('ScreenDisplayMode')

        if m.get('SessionMaxRateKbps') is not None:
            self.session_max_rate_kbps = m.get('SessionMaxRateKbps')

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

        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')

        self.usb_supply_redirect_rule = []
        if m.get('UsbSupplyRedirectRule') is not None:
            for k1 in m.get('UsbSupplyRedirectRule'):
                temp_model = main_models.ModifyCenterPolicyRequestUsbSupplyRedirectRule()
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

        if m.get('WatermarkColumnAmount') is not None:
            self.watermark_column_amount = m.get('WatermarkColumnAmount')

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

class ModifyCenterPolicyRequestUsbSupplyRedirectRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        product_id: str = None,
        usb_redirect_type: str = None,
        usb_rule_type: str = None,
        vendor_id: str = None,
    ):
        # Rule description.
        self.description = description
        # Product ID.
        self.product_id = product_id
        # USB redirection type.
        self.usb_redirect_type = usb_redirect_type
        # USB redirection rule type.
        self.usb_rule_type = usb_rule_type
        # Vendor ID. For more information, see [Valid USB Vendor IDs (VIDs)](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf).
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

class ModifyCenterPolicyRequestRevokeSecurityPolicyRule(DaraModel):
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
        # Target of the security group control rule to delete. Specify an IPv4 CIDR block.
        self.cidr_ip = cidr_ip
        # Description of the security group control rule to delete.
        self.description = description
        # Protocol type for the security group control rule to delete.
        self.ip_protocol = ip_protocol
        # Authorization policy for the security group control rule to delete.
        self.policy = policy
        # Port range for the security group control rule to delete. The port range depends on the protocol (IpProtocol):
        # 
        # - For TCP or UDP protocols: Port range is 1 to 65535. Separate the start and end ports with a forward slash (/). Example: 1/200.
        # 
        # - For ICMP protocol: Set to -1/-1.
        # 
        # - For GRE protocol: Set to -1/-1.
        # 
        # - When IpProtocol is set to all: Set to -1/-1.
        # 
        # For more information about common ports for typical applications, see [Common ports](https://help.aliyun.com/document_detail/40724.html).
        self.port_range = port_range
        # Priority of the security group control rule to delete. A smaller number indicates a higher priority. Valid values: 1 to 60. Default value: 1.
        self.priority = priority
        # Rule direction for the security group control rule to delete.
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

class ModifyCenterPolicyRequestRevokeAccessPolicyRule(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        # Client access IP address range to delete. Specify an IPv4 CIDR block.
        self.cidr_ip = cidr_ip
        # Description of the client IP address whitelist to delete.
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

class ModifyCenterPolicyRequestRecordEventLevels(DaraModel):
    def __init__(
        self,
        event_level: str = None,
        event_type: str = None,
    ):
        # Event level
        self.event_level = event_level
        # Event type
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_type is not None:
            result['EventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        return self

class ModifyCenterPolicyRequestNetRedirectRule(DaraModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
        rule_type: str = None,
    ):
        # Domain name.
        self.domain = domain
        # Redirection policy.
        self.policy = policy
        # Rule type.
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

class ModifyCenterPolicyRequestDomainResolveRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain: str = None,
        policy: str = None,
    ):
        # Policy description.
        self.description = description
        # Domain name.
        self.domain = domain
        # Resolution policy.
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

class ModifyCenterPolicyRequestDeviceRules(DaraModel):
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
        # Device name.
        self.device_name = device_name
        # Product ID.
        self.device_pid = device_pid
        # Peripheral type.
        self.device_type = device_type
        # Vendor ID. For more information, see [Valid USB Vendor IDs (VIDs)](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf).
        self.device_vid = device_vid
        # Link optimization command.
        self.opt_command = opt_command
        self.platforms = platforms
        # Redirection type.
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

class ModifyCenterPolicyRequestDeviceRedirects(DaraModel):
    def __init__(
        self,
        device_type: str = None,
        redirect_type: str = None,
    ):
        # Peripheral type.
        self.device_type = device_type
        # Redirection type.
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

class ModifyCenterPolicyRequestClipboardGraineds(DaraModel):
    def __init__(
        self,
        clipboard_size: int = None,
        clipboard_size_unit: str = None,
        clipboard_type: str = None,
        grained_type: str = None,
        in_clipboard_size: int = None,
        in_clipboard_size_unit: str = None,
        out_clipboard_size: int = None,
        out_clipboard_size_unit: str = None,
    ):
        self.clipboard_size = clipboard_size
        self.clipboard_size_unit = clipboard_size_unit
        self.clipboard_type = clipboard_type
        self.grained_type = grained_type
        self.in_clipboard_size = in_clipboard_size
        self.in_clipboard_size_unit = in_clipboard_size_unit
        self.out_clipboard_size = out_clipboard_size
        self.out_clipboard_size_unit = out_clipboard_size_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clipboard_size is not None:
            result['ClipboardSize'] = self.clipboard_size

        if self.clipboard_size_unit is not None:
            result['ClipboardSizeUnit'] = self.clipboard_size_unit

        if self.clipboard_type is not None:
            result['ClipboardType'] = self.clipboard_type

        if self.grained_type is not None:
            result['GrainedType'] = self.grained_type

        if self.in_clipboard_size is not None:
            result['InClipboardSize'] = self.in_clipboard_size

        if self.in_clipboard_size_unit is not None:
            result['InClipboardSizeUnit'] = self.in_clipboard_size_unit

        if self.out_clipboard_size is not None:
            result['OutClipboardSize'] = self.out_clipboard_size

        if self.out_clipboard_size_unit is not None:
            result['OutClipboardSizeUnit'] = self.out_clipboard_size_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipboardSize') is not None:
            self.clipboard_size = m.get('ClipboardSize')

        if m.get('ClipboardSizeUnit') is not None:
            self.clipboard_size_unit = m.get('ClipboardSizeUnit')

        if m.get('ClipboardType') is not None:
            self.clipboard_type = m.get('ClipboardType')

        if m.get('GrainedType') is not None:
            self.grained_type = m.get('GrainedType')

        if m.get('InClipboardSize') is not None:
            self.in_clipboard_size = m.get('InClipboardSize')

        if m.get('InClipboardSizeUnit') is not None:
            self.in_clipboard_size_unit = m.get('InClipboardSizeUnit')

        if m.get('OutClipboardSize') is not None:
            self.out_clipboard_size = m.get('OutClipboardSize')

        if m.get('OutClipboardSizeUnit') is not None:
            self.out_clipboard_size_unit = m.get('OutClipboardSizeUnit')

        return self

class ModifyCenterPolicyRequestClientType(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # Client login control. Specifies the client type.
        self.client_type = client_type
        # Client login control. Specifies whether to allow using a specific client type to log on to cloud computers.
        # 
        # > If you don\\"t configure `ClientType` parameters, all client types are allowed by default.
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

class ModifyCenterPolicyRequestAuthorizeSecurityPolicyRule(DaraModel):
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
        # Target of the security group control rule. Specify an IPv4 CIDR block.
        self.cidr_ip = cidr_ip
        # Description of the security group control rule.
        self.description = description
        # Protocol type for the security group control rule.
        self.ip_protocol = ip_protocol
        # Authorization policy for the security group control rule.
        self.policy = policy
        # Port range for the security group control rule. The port range depends on the protocol (IpProtocol):
        # 
        # - For TCP or UDP protocols: Port range is 1 to 65535. Separate the start and end ports with a forward slash (/). Example: 1/200.
        # 
        # - For ICMP protocol: Set to -1/-1.
        # 
        # - For GRE protocol: Set to -1/-1.
        # 
        # - When IpProtocol is set to all: Set to -1/-1.
        # 
        # For more information about common ports for typical applications, see [Common ports](https://help.aliyun.com/document_detail/40724.html).
        self.port_range = port_range
        # Priority of the security group control rule. A smaller number indicates a higher priority. Valid values: 1 to 60. Default value: 1.
        self.priority = priority
        # Rule direction for the security group control rule.
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

class ModifyCenterPolicyRequestAuthorizeAccessPolicyRule(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        # Client access IP address range. Specify an IPv4 CIDr block.
        self.cidr_ip = cidr_ip
        # Description of the client IP address whitelist.
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

