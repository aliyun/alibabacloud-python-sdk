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
        # The details about the cloud computer policies.
        self.describe_policy_groups = describe_policy_groups
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        admin_access: str = None,
        app_content_protection: str = None,
        authorize_access_policy_rules: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules] = None,
        authorize_security_policy_rules: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules] = None,
        camera_redirect: str = None,
        client_control_menu: str = None,
        client_types: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsClientTypes] = None,
        clipboard: str = None,
        color_enhancement: str = None,
        cpd_drive_clipboard: str = None,
        cpu_down_grade_duration: int = None,
        cpu_processors: List[str] = None,
        cpu_protected_mode: str = None,
        cpu_rate_limit: int = None,
        cpu_sample_duration: int = None,
        cpu_single_rate_limit: int = None,
        desktop_count: int = None,
        desktop_group_count: int = None,
        device_redirects: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDeviceRedirects] = None,
        device_rules: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDeviceRules] = None,
        disconnect_keep_session: str = None,
        disconnect_keep_session_time: int = None,
        display_mode: str = None,
        domain_register_value: str = None,
        domain_resolve_rule: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsDomainResolveRule] = None,
        domain_resolve_rule_type: str = None,
        end_user_apply_admin_coordinate: str = None,
        end_user_group_coordinate: str = None,
        file_transfer_address: str = None,
        file_transfer_speed: str = None,
        file_transfer_speed_location: str = None,
        gpu_acceleration: str = None,
        html_5access: str = None,
        html_5file_transfer: str = None,
        internet_communication_protocol: str = None,
        internet_printer: str = None,
        local_drive: str = None,
        max_reconnect_time: int = None,
        memory_down_grade_duration: int = None,
        memory_processors: List[str] = None,
        memory_protected_mode: str = None,
        memory_rate_limit: int = None,
        memory_sample_duration: int = None,
        memory_single_rate_limit: int = None,
        mobile_restart: str = None,
        mobile_shutdown: str = None,
        name: str = None,
        net_redirect: str = None,
        net_redirect_rule: List[main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsNetRedirectRule] = None,
        no_operation_disconnect: str = None,
        no_operation_disconnect_time: int = None,
        policy_group_id: str = None,
        policy_group_type: str = None,
        policy_status: str = None,
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
        watermark_transparency_value: int = None,
        watermark_type: str = None,
        wy_assistant: str = None,
    ):
        # Indicates whether the admin permissions are granted to end users.
        # 
        # >  This parameter is in private preview and only available to specific users.
        self.admin_access = admin_access
        # Indicates whether anti-screenshot is enabled.
        self.app_content_protection = app_content_protection
        # The client IP address whitelists.
        self.authorize_access_policy_rules = authorize_access_policy_rules
        # The security group rules.
        self.authorize_security_policy_rules = authorize_security_policy_rules
        # Indicates whether on-premises webcam redirection is enabled.
        self.camera_redirect = camera_redirect
        self.client_control_menu = client_control_menu
        # The logon method control rules.
        self.client_types = client_types
        # The read/write permissions on the clipboard.
        self.clipboard = clipboard
        # Indicates whether color enhancement is enabled for design and 3D applications.
        self.color_enhancement = color_enhancement
        self.cpd_drive_clipboard = cpd_drive_clipboard
        # The CPU underclocking duration. Valid values: 30 to 120. Unit: seconds.
        self.cpu_down_grade_duration = cpu_down_grade_duration
        # The CPU processors.
        self.cpu_processors = cpu_processors
        # The CPU spike protection policy.
        self.cpu_protected_mode = cpu_protected_mode
        # The overall CPU usage. Valid values: 70 to 90. Unit: percentage (%).
        self.cpu_rate_limit = cpu_rate_limit
        # The overall CPU sampling duration. Valid values: 10 to 60. Unit: seconds.
        self.cpu_sample_duration = cpu_sample_duration
        # The single-CPU usage. Valid values: 70 to 100. Unit: %.
        self.cpu_single_rate_limit = cpu_single_rate_limit
        # The number of cloud computers that are associated with the policy.
        self.desktop_count = desktop_count
        # The number of cloud computer shares that are associated with the policy.
        self.desktop_group_count = desktop_group_count
        # The device redirection rules.
        self.device_redirects = device_redirects
        # The custom peripheral rules.
        self.device_rules = device_rules
        # Indicates whether the session is retained after disconnection.
        # 
        # >  This parameter applies only to cloud application policies.
        self.disconnect_keep_session = disconnect_keep_session
        # The retention period of the session after disconnection. Unit: seconds.
        # 
        # >  This parameter applies only to cloud application policies.
        self.disconnect_keep_session_time = disconnect_keep_session_time
        # The display mode.
        self.display_mode = display_mode
        # The field where the domain resolution policy is applied.
        self.domain_register_value = domain_register_value
        # The domain resolution policies.
        self.domain_resolve_rule = domain_resolve_rule
        # Indicates whether domain name resolution is allowed.
        self.domain_resolve_rule_type = domain_resolve_rule_type
        # Indicates whether end users are allowed to request administrator help.
        self.end_user_apply_admin_coordinate = end_user_apply_admin_coordinate
        # Indicates whether end users in the same office network can share cloud computers.
        self.end_user_group_coordinate = end_user_group_coordinate
        self.file_transfer_address = file_transfer_address
        self.file_transfer_speed = file_transfer_speed
        self.file_transfer_speed_location = file_transfer_speed_location
        # Indicates whether image quality control is enabled. For optimal computer performance and user experience in professional design scenarios, we recommend enabling this feature.
        self.gpu_acceleration = gpu_acceleration
        # The web client access policy.
        self.html_5access = html_5access
        # The file transfer feature on the web client.
        self.html_5file_transfer = html_5file_transfer
        # The network communication protocol.
        self.internet_communication_protocol = internet_communication_protocol
        self.internet_printer = internet_printer
        # The read/write permissions on the on-premises drive.
        self.local_drive = local_drive
        # The maximum duration to retry reconnecting to cloud computers after an unexpected disconnection (non-human causes). Valid values: 30 to 7200. Unit: seconds.
        self.max_reconnect_time = max_reconnect_time
        # The memory underclocking duration per process. Valid values: 30 to 120. Unit: seconds.
        self.memory_down_grade_duration = memory_down_grade_duration
        # The memory processors.
        self.memory_processors = memory_processors
        # The memory spike protection policy.
        self.memory_protected_mode = memory_protected_mode
        # The overall memory usage. Valid values: 70 to 90. Unit: %.
        self.memory_rate_limit = memory_rate_limit
        # The overall memory sampling duration. Valid values: 30 to 60. Unit: seconds.
        self.memory_sample_duration = memory_sample_duration
        # The memory usage per process. Valid values: 30 to 60. Unit: %.
        self.memory_single_rate_limit = memory_single_rate_limit
        # Indicates whether the Restart button is displayed in the DesktopAssistant menu when end users connect to cloud computers from Android clients.
        # 
        # >  This feature applies to only mobile clients of version 7.4.0 or later.
        self.mobile_restart = mobile_restart
        # Indicates whether the Stop button is displayed in the DesktopAssistant menu when end users connect to cloud computers from Android clients.
        # 
        # >  This feature applies to only mobile clients of version 7.4.0 or later.
        self.mobile_shutdown = mobile_shutdown
        # The policy name.
        self.name = name
        # The network redirection policy.
        # 
        # >  This parameter is in private preview and only available to specific users.
        self.net_redirect = net_redirect
        # The network redirection policies.
        # 
        # >  This parameter is in private preview and only available to specific users.
        self.net_redirect_rule = net_redirect_rule
        # Indicates whether a disconnection is enforced upon inactivity.
        # 
        # >  This parameter applies only to cloud application policies.
        self.no_operation_disconnect = no_operation_disconnect
        # The duration of disconnection after inactivity. Unit: seconds.
        # 
        # >  This parameter applies only to cloud application policies.
        self.no_operation_disconnect_time = no_operation_disconnect_time
        # The policy ID.
        self.policy_group_id = policy_group_id
        # The type of the policy.
        self.policy_group_type = policy_group_type
        # The status of the cloud computer policy.
        self.policy_status = policy_status
        # The printer redirection policy.
        self.printer_redirection = printer_redirection
        # Indicates whether image quality enhancement is enabled for design and 3D applications.
        self.quality_enhancement = quality_enhancement
        # Indicates whether custom screen recording is enabled.
        self.record_content = record_content
        # The duration for which custom screen recordings are kept before they expire. Default value: 30 days.
        self.record_content_expires = record_content_expires
        # The duration of screen recording after the specified event is detected. Unit: minutes. Valid values: 10 to 60.
        self.record_event_duration = record_event_duration
        # The absolute paths to screen recording files.
        self.record_event_file_paths = record_event_file_paths
        # The absolute paths to screen recording registries.
        self.record_event_registers = record_event_registers
        # Indicates whether screen recording is enabled.
        self.recording = recording
        # Indicates whether audio files generated on cloud computers are recorded.
        self.recording_audio = recording_audio
        # The length of the screen recording file. Unit: minutes. Screen recording files are split by the specified length and uploaded to OSS buckets. Once a file reaches 300 MB, the system prioritizes rolling updates for that file.
        self.recording_duration = recording_duration
        # The end time of screen recording. The value is in the HH:MM:SS format. The value is meaningful only when you set Recording to period.
        self.recording_end_time = recording_end_time
        # The retention period of the screen recording file. Valid values: 1 to 180. Unit: days.
        self.recording_expires = recording_expires
        # The frame rate of screen recording. Unit: fps.
        self.recording_fps = recording_fps
        # The start time of screen recording. The value is in the HH:MM:SS format. The value is meaningful only when you set Recording to period.
        self.recording_start_time = recording_start_time
        # Indicates whether to notify end users when screen recording is enabled.
        self.recording_user_notify = recording_user_notify
        # The notification sent to end users when screen recording is enabled.
        self.recording_user_notify_message = recording_user_notify_message
        # The keyboard and mouse control permissions during remote assistance.
        self.remote_coordinate = remote_coordinate
        # The height of the resolution. Unit: pixel.
        self.resolution_height = resolution_height
        # The resolution type.
        self.resolution_model = resolution_model
        # The width of the resolution. Unit: pixel.
        self.resolution_width = resolution_width
        # The number of resource groups that are associated with the policy.
        self.resource_group_count = resource_group_count
        self.safe_menu = safe_menu
        # The effective scope of the policy.
        self.scope = scope
        # The effective scopes specified by CIDR blocks.
        self.scope_value = scope_value
        self.screen_display_mode = screen_display_mode
        # Indicates whether smoothness enhancement is enabled for daily office use.
        self.smooth_enhancement = smooth_enhancement
        # Indicates whether the metric status entry is displayed in the DesktopAssistant menu.
        self.status_monitor = status_monitor
        # The streaming mode.
        self.streaming_mode = streaming_mode
        # The target frame rate. Valid values: 10 to 60. Unit: fps.
        self.target_fps = target_fps
        # Indicates whether the application taskbar is displayed.
        # 
        # >  This parameter applies only to cloud application policies.
        self.taskbar = taskbar
        # The USB redirection policy.
        self.usb_redirect = usb_redirect
        # The USB redirection rules.
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        self.use_time = use_time
        # The average bitrate for video encoding. Unit: Kbit/s. Valid values: 1000 to 50000.
        self.video_enc_avg_kbps = video_enc_avg_kbps
        # The maximum QP for video files. Higher QP values result in lower video quality. Valid values: 0 to 51.
        self.video_enc_max_qp = video_enc_max_qp
        # The minimum quantizer parameter (QP) for video files. A lower QP means better video quality. Valid values: 0 to 51.
        self.video_enc_min_qp = video_enc_min_qp
        # The peak bitrate for video encoding. Unit: Kbit/s. Valid values: 1000 to 50000.
        self.video_enc_peak_kbps = video_enc_peak_kbps
        # The video encoding policy.
        self.video_enc_policy = video_enc_policy
        # Indicates whether multimedia redirection is enabled.
        self.video_redirect = video_redirect
        # The image quality policy.
        self.visual_quality = visual_quality
        # The watermark policy.
        self.watermark = watermark
        # Indicates whether anti-screen capture is enabled for invisible watermarks.
        self.watermark_anti_cam = watermark_anti_cam
        # The font color of the watermark. Valid values: 0 to 16777215.
        self.watermark_color = watermark_color
        # If you set `WatermarkType` to `custom`, you must also specify `WatermarkCustomText`.
        self.watermark_custom_text = watermark_custom_text
        # The watermark rotation. Valid values: -10 to -30.
        self.watermark_degree = watermark_degree
        # The font size of the watermark. Valid values: 10 to 20.
        self.watermark_font_size = watermark_font_size
        # The font style of the watermark.
        self.watermark_font_style = watermark_font_style
        # The enhancement level for invisible watermarks.
        self.watermark_power = watermark_power
        # The number of watermark rows.
        self.watermark_row_amount = watermark_row_amount
        # Indicates whether security priority is enabled for invisible watermarks.
        self.watermark_security = watermark_security
        # The watermark transparency. A higher value means the watermark is less transparent. Valid values: 10 to 100.
        self.watermark_transparency_value = watermark_transparency_value
        # The watermark type.
        self.watermark_type = watermark_type
        # Indicates whether the Xiaoying AI Assistant entry is displayed in the DesktopAssistant menu.
        self.wy_assistant = wy_assistant

    def validate(self):
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
        if self.admin_access is not None:
            result['AdminAccess'] = self.admin_access

        if self.app_content_protection is not None:
            result['AppContentProtection'] = self.app_content_protection

        result['AuthorizeAccessPolicyRules'] = []
        if self.authorize_access_policy_rules is not None:
            for k1 in self.authorize_access_policy_rules:
                result['AuthorizeAccessPolicyRules'].append(k1.to_map() if k1 else None)

        result['AuthorizeSecurityPolicyRules'] = []
        if self.authorize_security_policy_rules is not None:
            for k1 in self.authorize_security_policy_rules:
                result['AuthorizeSecurityPolicyRules'].append(k1.to_map() if k1 else None)

        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect

        if self.client_control_menu is not None:
            result['ClientControlMenu'] = self.client_control_menu

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

        if self.end_user_group_coordinate is not None:
            result['EndUserGroupCoordinate'] = self.end_user_group_coordinate

        if self.file_transfer_address is not None:
            result['FileTransferAddress'] = self.file_transfer_address

        if self.file_transfer_speed is not None:
            result['FileTransferSpeed'] = self.file_transfer_speed

        if self.file_transfer_speed_location is not None:
            result['FileTransferSpeedLocation'] = self.file_transfer_speed_location

        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration

        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access

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

        if self.mobile_shutdown is not None:
            result['MobileShutdown'] = self.mobile_shutdown

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

        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

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

        if self.watermark_transparency_value is not None:
            result['WatermarkTransparencyValue'] = self.watermark_transparency_value

        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type

        if self.wy_assistant is not None:
            result['WyAssistant'] = self.wy_assistant

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminAccess') is not None:
            self.admin_access = m.get('AdminAccess')

        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')

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

        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')

        if m.get('ClientControlMenu') is not None:
            self.client_control_menu = m.get('ClientControlMenu')

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

        if m.get('EndUserGroupCoordinate') is not None:
            self.end_user_group_coordinate = m.get('EndUserGroupCoordinate')

        if m.get('FileTransferAddress') is not None:
            self.file_transfer_address = m.get('FileTransferAddress')

        if m.get('FileTransferSpeed') is not None:
            self.file_transfer_speed = m.get('FileTransferSpeed')

        if m.get('FileTransferSpeedLocation') is not None:
            self.file_transfer_speed_location = m.get('FileTransferSpeedLocation')

        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')

        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')

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

        if m.get('MobileShutdown') is not None:
            self.mobile_shutdown = m.get('MobileShutdown')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')

        self.net_redirect_rule = []
        if m.get('NetRedirectRule') is not None:
            for k1 in m.get('NetRedirectRule'):
                temp_model = main_models.DescribeCenterPolicyListResponseBodyDescribePolicyGroupsNetRedirectRule()
                self.net_redirect_rule.append(temp_model.from_map(k1))

        if m.get('NoOperationDisconnect') is not None:
            self.no_operation_disconnect = m.get('NoOperationDisconnect')

        if m.get('NoOperationDisconnectTime') is not None:
            self.no_operation_disconnect_time = m.get('NoOperationDisconnectTime')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

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

        if m.get('WatermarkTransparencyValue') is not None:
            self.watermark_transparency_value = m.get('WatermarkTransparencyValue')

        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')

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
        # The rule description.
        self.description = description
        # The product ID (PID).
        self.product_id = product_id
        # Indicates whether USB redirection is allowed.
        self.usb_redirect_type = usb_redirect_type
        # The type of the USB redirection rule.
        self.usb_rule_type = usb_rule_type
        # The vendor ID (VID). For more information, see [Valid USB Vendor IDs (VIDs)](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf).
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
        # The domain name.
        self.domain = domain
        # The redirection policy.
        self.policy = policy
        # The rule type.
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
        # The policy description.
        self.description = description
        # The domain name.
        self.domain = domain
        # The resolution policy.
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
        # The device name.
        self.device_name = device_name
        # The product ID (PID).
        self.device_pid = device_pid
        # The peripheral type.
        self.device_type = device_type
        # The vendor ID (VID). For more information, see [Valid USB VIDs](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf).
        self.device_vid = device_vid
        # The link optimization command.
        self.opt_command = opt_command
        self.platforms = platforms
        # The redirection type.
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
        # The peripheral type.
        self.device_type = device_type
        # The redirection type.
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
        # The client type.
        self.client_type = client_type
        # Indicates whether a specific client type can connect to cloud computers.
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
        # The object to which the security group rule applies. The value is an IPv4 CIDR block.
        self.cidr_ip = cidr_ip
        # The description of the security group rule.
        self.description = description
        # The protocol type of the security group rule.
        self.ip_protocol = ip_protocol
        # The authorization policy of the security group rule.
        self.policy = policy
        # The port range of the security group rule.
        self.port_range = port_range
        # The priority of the security group rule. A smaller value indicates a higher priority.
        self.priority = priority
        # The direction of the security group rule.
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
        # The client CIDR block from which end users can connect to cloud computers. The value is an IPv4 CIDR block.
        self.cidr_ip = cidr_ip
        # The remarks on the client CIDR block.
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

