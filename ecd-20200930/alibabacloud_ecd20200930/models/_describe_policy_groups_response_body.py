# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribePolicyGroupsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        describe_policy_groups: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroups] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        self.count = count
        # The details of the cloud computer policies.
        self.describe_policy_groups = describe_policy_groups
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id

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
        if self.count is not None:
            result['Count'] = self.count

        result['DescribePolicyGroups'] = []
        if self.describe_policy_groups is not None:
            for k1 in self.describe_policy_groups:
                result['DescribePolicyGroups'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.describe_policy_groups = []
        if m.get('DescribePolicyGroups') is not None:
            for k1 in m.get('DescribePolicyGroups'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroups()
                self.describe_policy_groups.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePolicyGroupsResponseBodyDescribePolicyGroups(DaraModel):
    def __init__(
        self,
        academic_proxy: str = None,
        admin_access: str = None,
        app_content_protection: str = None,
        authorize_access_policy_rules: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules] = None,
        authorize_security_policy_rules: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules] = None,
        auto_reconnect: str = None,
        camera_redirect: str = None,
        client_control_menu: str = None,
        client_create_snapshot: str = None,
        client_types: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsClientTypes] = None,
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
        device_redirects: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsDeviceRedirects] = None,
        device_rules: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsDeviceRules] = None,
        disk_overload: str = None,
        display_mode: str = None,
        domain_list: str = None,
        domain_resolve_rule: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsDomainResolveRule] = None,
        domain_resolve_rule_type: str = None,
        eds_count: int = None,
        end_user_apply_admin_coordinate: str = None,
        end_user_group_coordinate: str = None,
        external_drive: str = None,
        file_migrate: str = None,
        file_transfer: str = None,
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
        name: str = None,
        net_redirect: str = None,
        net_redirect_rule: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsNetRedirectRule] = None,
        policy_group_id: str = None,
        policy_group_type: str = None,
        policy_status: str = None,
        port_proxy: str = None,
        preempt_login: str = None,
        preempt_login_users: List[str] = None,
        printer_redirection: str = None,
        quality_enhancement: str = None,
        record_content: str = None,
        record_content_expires: int = None,
        record_event_duration: int = None,
        record_event_file_exts: List[str] = None,
        record_event_file_paths: List[str] = None,
        record_event_levels: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsRecordEventLevels] = None,
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
        resolution_height: int = None,
        resolution_model: str = None,
        resolution_width: int = None,
        resource_group_count: int = None,
        resource_region_id: str = None,
        safe_menu: str = None,
        scope: str = None,
        scope_value: List[str] = None,
        screen_display_mode: str = None,
        smooth_enhancement: str = None,
        status_monitor: str = None,
        streaming_mode: str = None,
        target_fps: int = None,
        usb_redirect: str = None,
        usb_supply_redirect_rule: List[main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule] = None,
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
        watermark_transparency: str = None,
        watermark_transparency_value: int = None,
        watermark_type: str = None,
        wuying_keeper: str = None,
        wy_assistant: str = None,
    ):
        self.academic_proxy = academic_proxy
        # Indicates whether end users are granted the administrator permissions.
        # 
        # >  This parameter is in invitational preview for specific users and not available to the public.
        self.admin_access = admin_access
        # Indicates whether the anti-screenshot feature is enabled.
        # 
        # Valid values:
        # 
        # *   off (default)
        # *   on
        self.app_content_protection = app_content_protection
        # The client IP address whitelist. End users can access cloud computers only from the IP addresses in the whitelist.
        self.authorize_access_policy_rules = authorize_access_policy_rules
        # The security group rules.
        self.authorize_security_policy_rules = authorize_security_policy_rules
        # The automatic client connection recovery configurations.
        self.auto_reconnect = auto_reconnect
        # Indicates whether the webcam redirection feature is enabled.
        # 
        # Valid values:
        # 
        # *   off
        # *   on (default)
        self.camera_redirect = camera_redirect
        self.client_control_menu = client_control_menu
        self.client_create_snapshot = client_create_snapshot
        # The logon method control rules to limit the type of the Alibaba Cloud Workspace client used by end users to connect to cloud computers.
        self.client_types = client_types
        # The permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: specifies one-way transfer. You can copy files only from local devices to cloud computers.
        # *   readwrite: specifies two-way transfer. You can copy files between local devices and cloud computers.
        # *   write: specifies one-way transfer. You can only copy files from cloud computers to local devices.
        # *   off: disables both one-way and two-way transfer. Files cannot be copied between local devices and cloud computers.
        self.clipboard = clipboard
        # Indicates whether the Color Enhancement switch is turned on in design and 3D scenarios.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.color_enhancement = color_enhancement
        self.cpd_drive_clipboard = cpd_drive_clipboard
        # The CPU underclocking duration. Valid values: 30 to 120. Unit: seconds.
        self.cpu_down_grade_duration = cpu_down_grade_duration
        self.cpu_overload = cpu_overload
        # The process whitelist that is not restricted by the CPU usage limit.
        self.cpu_processors = cpu_processors
        # Indicates whether the CPU spike protection switch is turned on.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.cpu_protected_mode = cpu_protected_mode
        # The overall CPU usage. Valid values: 70 to 90. Unit: percentage (%).
        self.cpu_rate_limit = cpu_rate_limit
        # The overall CPU sampling duration. Valid values: 10 to 60. Unit: seconds.
        self.cpu_sample_duration = cpu_sample_duration
        # The single-CPU usage. Valid values: 70 to 100. Unit: %.
        self.cpu_single_rate_limit = cpu_single_rate_limit
        # The number of cloud computers bound with this policy.
        self.desktop_count = desktop_count
        # The number of shared cloud computers bound with this policy.
        self.desktop_group_count = desktop_group_count
        self.device_connect_hint = device_connect_hint
        # The device redirection rules.
        self.device_redirects = device_redirects
        # The custom peripheral rules.
        self.device_rules = device_rules
        self.disk_overload = disk_overload
        # The display mode.
        # 
        # Valid values:
        # 
        # *   clientCustom: suitable for user-defined scenarios.
        # *   adminOffice: suitable for daily office scenarios.
        # *   adminDesign: suitable for 3D application scenarios.
        # *   adminCustom: administrator-customized scenarios
        self.display_mode = display_mode
        # Specifies whether to enable the access control for domain names. Domain names support wildcards (\\*). Separate multiple domain names with commas (,).
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.domain_list = domain_list
        # The domain name resolution rules.
        self.domain_resolve_rule = domain_resolve_rule
        # Indicates whether the switch for domain name resolution is turned on.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.domain_resolve_rule_type = domain_resolve_rule_type
        # The number of cloud computers that are associated with the policy. The number of cloud computers that are associated only with custom policies is returned.
        self.eds_count = eds_count
        # Indicates whether the Contact Administrator for Help switch is turned on.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.end_user_apply_admin_coordinate = end_user_apply_admin_coordinate
        # Indicates whether the User Stream Collaboration switch is turned on.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.end_user_group_coordinate = end_user_group_coordinate
        self.external_drive = external_drive
        self.file_migrate = file_migrate
        # Transfers files.
        self.file_transfer = file_transfer
        self.file_transfer_address = file_transfer_address
        self.file_transfer_speed = file_transfer_speed
        self.file_transfer_speed_location = file_transfer_speed_location
        # Indicates whether the Image Quality Control feature is enabled. If you have high requirements on the performance and user experience in scenarios such as professional design, we recommend that you enable this feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.gpu_acceleration = gpu_acceleration
        # Specifies whether to allow web client access.
        # 
        # Valid values:
        # 
        # *   off (default)
        # *   on
        self.html_5access = html_5access
        # The file transfer feature on the web client.
        # 
        # Valid values:
        # 
        # *   all: Files can be uploaded and downloaded between local computers and the web client.
        # *   download: Files on the web client can be downloaded to local computers.
        # *   upload: Files on local computers can be uploaded to the web client.
        # *   off (default): Files cannot be transferred between the web client and local computers.
        self.html_5file_transfer = html_5file_transfer
        # The protocol for network communication.
        # 
        # Valid values:
        # 
        # *   TCP (default): TCP.
        # *   BOTH: TCP and UDP.
        self.internet_communication_protocol = internet_communication_protocol
        self.internet_printer = internet_printer
        # The permissions on local disk mapping.
        # 
        # Valid values:
        # 
        # *   read: read-only. Local disk mapping is available on cloud computers. However, you can only read (copy) local files but cannot modify the files.
        # *   readwrite: read and write. Local disk mapping is available on cloud computers. You can read (copy) and write (modify) local files.
        # *   off (default): none.
        self.local_drive = local_drive
        # The maximum retry period for reconnecting to cloud computers when the cloud computers are disconnected due to none-human reasons. Valid values: 30 to 7200. Unit: seconds.
        self.max_reconnect_time = max_reconnect_time
        # The memory underclocking duration for a single process. Valid values: 30 to 120. Unit: seconds.
        self.memory_down_grade_duration = memory_down_grade_duration
        self.memory_overload = memory_overload
        # The whitelist of processes that are not restricted by the memory usage limit.
        self.memory_processors = memory_processors
        # Indicates whether the memory spike protection switch is turned on.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.memory_protected_mode = memory_protected_mode
        # The overall memory usage. Valid values: 70 to 90. Unit: %.
        self.memory_rate_limit = memory_rate_limit
        # The overall memory sampling duration. Valid values: 30 to 60. Unit: seconds.
        self.memory_sample_duration = memory_sample_duration
        # The memory usage of a single process. Valid values: 30 to 60. Unit: %.
        self.memory_single_rate_limit = memory_single_rate_limit
        # Specifies whether to display the restart button in the DesktopAssistant when the cloud computer is accessed from the Alibaba Cloud Workspace mobile clients (including the Android client and the iOS client).
        # 
        # > Mobile clients of V7.4 and higher versions required.
        # 
        # Valid values:
        # 
        # - off: not provided.
        # - on: provided.
        self.mobile_restart = mobile_restart
        # Indicates whether the Windows security control is enabled for mobile clients.
        self.mobile_safe_menu = mobile_safe_menu
        # Specifies whether to display the shut down button in the DesktopAssistant when the cloud computer is accessed from the Alibaba Cloud Workspace mobile clients (including the Android client and the iOS client).
        # 
        # > Mobile clients of V7.4 and higher versions required.
        # 
        # Valid values:
        # 
        # - off: not provided.
        # - on: provided.
        self.mobile_shutdown = mobile_shutdown
        # Indicates whether the Cloud Computer Manager is enabled for mobile clients.
        self.mobile_wuying_keeper = mobile_wuying_keeper
        # Indicates whether the Xiaoying AI Assistant is enabled for mobile clients.
        self.mobile_wy_assistant = mobile_wy_assistant
        self.model_library = model_library
        # The name of the cloud computer policy.
        self.name = name
        # Indicates whether the network redirection feature is enabled.
        # 
        # >  This parameter is in invitational preview for specific users and not available to the public.
        # 
        # Valid values:
        # 
        # *   off (default)
        # *   on
        self.net_redirect = net_redirect
        # The network redirection rule.
        # 
        # >  This parameter is in invitational preview for specific users and not available to the public.
        self.net_redirect_rule = net_redirect_rule
        # The ID of the cloud computer policy.
        self.policy_group_id = policy_group_id
        # The type of the cloud computer policy.
        # 
        # Valid values:
        # 
        # *   SYSTEM
        # *   CUSTOM
        self.policy_group_type = policy_group_type
        # The status of the cloud computer policy.
        # 
        # Valid values:
        # 
        # *   AVAILABLE
        # *   CREATING
        self.policy_status = policy_status
        self.port_proxy = port_proxy
        # The cloud computer preemption feature.
        # 
        # >  To ensure user experience and data security, when a cloud computer is used by an end user, other end users cannot connect to the cloud computer. By default, this parameter is set to `off`, which cannot be modified.
        # 
        # Valid values:
        # 
        # *   off: Preemption is not allowed.
        self.preempt_login = preempt_login
        # The usernames that can preempt to connect to the cloud computer.
        self.preempt_login_users = preempt_login_users
        # Indicates whether the printer redirection feature is enabled.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.printer_redirection = printer_redirection
        # Indicates whether the Image Quality Enhancement switch is turned on for design and 3D scenarios.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.quality_enhancement = quality_enhancement
        # Indicates whether the custom screen recording feature is enabled.
        # 
        # Valid values:
        # 
        # *   off (default)
        # *   on
        self.record_content = record_content
        # The period when the custom screen recording can be retained before expiration. Default value: 30 days.
        self.record_content_expires = record_content_expires
        # The recording duration since a target event is detected by the screen recording audit policy. Unit: Minute. Valid values: 10-60.
        self.record_event_duration = record_event_duration
        # The screen recording file suffix.
        self.record_event_file_exts = record_event_file_exts
        # The array of absolute paths of the monitored files in the screen recording audit policy.
        self.record_event_file_paths = record_event_file_paths
        # Indicates whether the screen recording event severity is enabled.
        self.record_event_levels = record_event_levels
        # The array of absolute paths of the monitored registry entries in the screen recording audit policy.
        self.record_event_registers = record_event_registers
        # Indicates whether the screen recording feature is enabled.
        # 
        # Valid values:
        # 
        # *   byaction_cmd_ft: enables the operation-triggered screen recording upon command execution and file transfer.
        # *   ALLTIME: enables the whole-process screen recording. That is, the recording starts when cloud computers are connected and ends when the cloud computers are disconnected.
        # *   PERIOD: enables the interval-based screen recording. You must specify an interval between the start time and end time of this type of recording.
        # *   byaction_commands: enables the operation-triggered screen recording upon command execution.
        # *   OFF: disables the screen recording feature.
        # *   byaction_file_transfer: enables the operation-triggered screen recording upon file transfer.
        self.recording = recording
        # Indicates whether audio files generated from cloud computers are recorded.
        # 
        # Valid values:
        # 
        # *   off (default): records only video files.
        # *   on: records video and audio files.
        self.recording_audio = recording_audio
        # The file length of the screen recording. Unit: minutes. Screen recording files are split based on the specified file length and uploaded to Object Storage Service (OSS) buckets. When a screen recording file reaches 300 MB in size, the system preferentially performs rolling update for the file.
        # 
        # Valid values:
        # 
        # *   10
        # *   20
        # *   30
        # *   60
        self.recording_duration = recording_duration
        # The time when the screen recording ended. The value is in the HH:MM:SS format. The value takes effect only when Recording is set to PERIOD.
        self.recording_end_time = recording_end_time
        # The retention period of the screen recording file. Valid values: 1 to 180. Unit: days.
        self.recording_expires = recording_expires
        # The frame rate of screen recording. Unit: fps.
        # 
        # Valid values:
        # 
        # *   2
        # *   5
        # *   10
        # *   15
        self.recording_fps = recording_fps
        # The time when the screen recording was started. The value is in the HH:MM:SS format. The value takes effect only when Recording is set to PERIOD.
        self.recording_start_time = recording_start_time
        # Indicates whether the screen recording notification feature is enabled after end users log on to the Alibaba Cloud Workspace client.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.recording_user_notify = recording_user_notify
        # The notification content of screen recording. By default, this parameter is left empty.
        self.recording_user_notify_message = recording_user_notify_message
        # The permissions on keyboard and mouse control during remote assistance.
        # 
        # Valid values:
        # 
        # *   optionalControl: By default, you are not granted the permissions. You can apply for the permissions.
        # *   fullControl: You are granted the full permissions.
        # *   disableControl: You are not granted the permissions.
        self.remote_coordinate = remote_coordinate
        # Resets the cloud computer.
        self.reset_desktop = reset_desktop
        self.resolution_height = resolution_height
        self.resolution_model = resolution_model
        self.resolution_width = resolution_width
        # The number of resource groups bound with this policy.
        self.resource_group_count = resource_group_count
        # The region of the cloud computer policy.
        # 
        # > The value of a region-less policy is `center`.
        self.resource_region_id = resource_region_id
        self.safe_menu = safe_menu
        # The effective scope of the policy.
        # 
        # Valid values:
        # 
        # *   IP: The policy takes effect based on the IP address.
        # *   GLOBAL: The policy takes effect globally.
        self.scope = scope
        # This parameter is required when the `Scope` parameter is set to `IP`.````
        self.scope_value = scope_value
        self.screen_display_mode = screen_display_mode
        # Indicates whether the Smooth Enhancement switch is turned on.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.smooth_enhancement = smooth_enhancement
        # Specifies whether to provide the Metrics function in the DesktopAssistant. Valid values:
        # 
        # - off: not provided.
        # - on: provided.
        self.status_monitor = status_monitor
        # The streaming mode.
        # 
        # Valid values:
        # 
        # *   intelligent: suitable for daily office scenarios (Intelligent Mode).
        # *   smooth: suitable for design and 3D application scenarios (Smooth Mode).
        self.streaming_mode = streaming_mode
        # The destination frame rate. Valid values: 10 to 60. Unit: fps.
        self.target_fps = target_fps
        # Indicates whether the USB redirection feature is enabled.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.usb_redirect = usb_redirect
        # The USB redirection rule.
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        self.use_time = use_time
        # The average bitrate for video encoding. Valid values: 1000 to 50000.
        self.video_enc_avg_kbps = video_enc_avg_kbps
        # The maximum quantizer parameter (QP) of video files. A larger QP value indicates worse video quality. Valid values: 0 to 51.
        self.video_enc_max_qp = video_enc_max_qp
        # The minimum quantizer parameter (QP) of video files. A smaller QP value indicates higher video quality. Valid values: 0 to 51.
        self.video_enc_min_qp = video_enc_min_qp
        # The peak bitrate for video encoding. Valid values: 1000 to 50000.
        self.video_enc_peak_kbps = video_enc_peak_kbps
        # The video encoding feature.
        # 
        # Valid values:
        # 
        # *   qualityFirst: The priority given to the image quality.
        # *   bandwidthFirst: The priority given to the bitrate.
        self.video_enc_policy = video_enc_policy
        # Indicates whether the multimedia redirection feature is enabled.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.video_redirect = video_redirect
        # The image display quality.
        # 
        # Valid values:
        # 
        # *   high: high-definition (HD)
        # *   low: fluent
        # *   medium (default): adaptive
        # *   lossless: no quality loss
        self.visual_quality = visual_quality
        # The watermarking feature.
        # 
        # Valid values:
        # 
        # *   blind: Invisible watermarks are applied.
        # *   off: The watermarking feature is disabled.
        # *   on: Visible watermarks are applied.
        self.watermark = watermark
        # Indicates whether the anti-screen photo feature is enabled for invisible watermarks.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.watermark_anti_cam = watermark_anti_cam
        # The font color in red, green, and blue (RGB) of the watermark. Valid values: 0 to 16777215.
        self.watermark_color = watermark_color
        # If you set `WatermarkType` to `custom`, you must also specify `WatermarkCustomText`.
        self.watermark_custom_text = watermark_custom_text
        # The slope of the watermark. Valid values: -10 to -30.
        self.watermark_degree = watermark_degree
        # The font size of the watermark. Valid values: 10 to 20.
        self.watermark_font_size = watermark_font_size
        # The watermark font style.
        # 
        # Valid values:
        # 
        # *   plain
        # *   bold
        self.watermark_font_style = watermark_font_style
        # The watermark enhancement feature.
        # 
        # Valid values:
        # 
        # *   high
        # *   low
        # *   medium
        self.watermark_power = watermark_power
        # The number of watermark rows.
        # 
        # >  This parameter is not available for public use.
        self.watermark_row_amount = watermark_row_amount
        # Indicates whether the security priority feature is enabled for invisible watermarks.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.watermark_security = watermark_security
        self.watermark_shadow = watermark_shadow
        # The watermark transparency.
        # 
        # Valid values:
        # 
        # *   LIGHT
        # *   DARK
        # *   MIDDLE
        self.watermark_transparency = watermark_transparency
        # The watermark transparency. A greater value indicates that the watermark is less transparent. Valid values: 10 to 100.
        self.watermark_transparency_value = watermark_transparency_value
        # The watermark content.
        # 
        # Valid values:
        # 
        # *   EndUserId: the username.
        # *   Custom
        # *   DesktopIp: the IP address of the cloud computer.
        # *   ClientIp: the IP address of the Alibaba Cloud Workspace client.
        # *   HostName: the rightmost 15 digits of the cloud computer ID.
        # *   ClientTime: the current time displayed on the cloud computer.
        self.watermark_type = watermark_type
        self.wuying_keeper = wuying_keeper
        # Specifies whether to provide the AI Assistant function in the DesktopAssistant when the cloud computer is accessed from the Alibaba Cloud Workspace desktop clients (including the Windows client and the macOS client).
        # 
        # > Desktop clients of V7.7 and higher versions required.
        # 
        # Valid values:
        # 
        # - off: the AI Aisstant function is not provided.
        # - on: the AI Aisstant function is provided.
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
        if self.record_event_levels:
            for v1 in self.record_event_levels:
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

        if self.auto_reconnect is not None:
            result['AutoReconnect'] = self.auto_reconnect

        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect

        if self.client_control_menu is not None:
            result['ClientControlMenu'] = self.client_control_menu

        if self.client_create_snapshot is not None:
            result['ClientCreateSnapshot'] = self.client_create_snapshot

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

        if self.disk_overload is not None:
            result['DiskOverload'] = self.disk_overload

        if self.display_mode is not None:
            result['DisplayMode'] = self.display_mode

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

        result['DomainResolveRule'] = []
        if self.domain_resolve_rule is not None:
            for k1 in self.domain_resolve_rule:
                result['DomainResolveRule'].append(k1.to_map() if k1 else None)

        if self.domain_resolve_rule_type is not None:
            result['DomainResolveRuleType'] = self.domain_resolve_rule_type

        if self.eds_count is not None:
            result['EdsCount'] = self.eds_count

        if self.end_user_apply_admin_coordinate is not None:
            result['EndUserApplyAdminCoordinate'] = self.end_user_apply_admin_coordinate

        if self.end_user_group_coordinate is not None:
            result['EndUserGroupCoordinate'] = self.end_user_group_coordinate

        if self.external_drive is not None:
            result['ExternalDrive'] = self.external_drive

        if self.file_migrate is not None:
            result['FileMigrate'] = self.file_migrate

        if self.file_transfer is not None:
            result['FileTransfer'] = self.file_transfer

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

        if self.name is not None:
            result['Name'] = self.name

        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect

        result['NetRedirectRule'] = []
        if self.net_redirect_rule is not None:
            for k1 in self.net_redirect_rule:
                result['NetRedirectRule'].append(k1.to_map() if k1 else None)

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_type is not None:
            result['PolicyGroupType'] = self.policy_group_type

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.port_proxy is not None:
            result['PortProxy'] = self.port_proxy

        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login

        if self.preempt_login_users is not None:
            result['PreemptLoginUsers'] = self.preempt_login_users

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

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_model is not None:
            result['ResolutionModel'] = self.resolution_model

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        if self.resource_group_count is not None:
            result['ResourceGroupCount'] = self.resource_group_count

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

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

        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency

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

        if m.get('AppContentProtection') is not None:
            self.app_content_protection = m.get('AppContentProtection')

        self.authorize_access_policy_rules = []
        if m.get('AuthorizeAccessPolicyRules') is not None:
            for k1 in m.get('AuthorizeAccessPolicyRules'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules()
                self.authorize_access_policy_rules.append(temp_model.from_map(k1))

        self.authorize_security_policy_rules = []
        if m.get('AuthorizeSecurityPolicyRules') is not None:
            for k1 in m.get('AuthorizeSecurityPolicyRules'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules()
                self.authorize_security_policy_rules.append(temp_model.from_map(k1))

        if m.get('AutoReconnect') is not None:
            self.auto_reconnect = m.get('AutoReconnect')

        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')

        if m.get('ClientControlMenu') is not None:
            self.client_control_menu = m.get('ClientControlMenu')

        if m.get('ClientCreateSnapshot') is not None:
            self.client_create_snapshot = m.get('ClientCreateSnapshot')

        self.client_types = []
        if m.get('ClientTypes') is not None:
            for k1 in m.get('ClientTypes'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsClientTypes()
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
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsDeviceRedirects()
                self.device_redirects.append(temp_model.from_map(k1))

        self.device_rules = []
        if m.get('DeviceRules') is not None:
            for k1 in m.get('DeviceRules'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsDeviceRules()
                self.device_rules.append(temp_model.from_map(k1))

        if m.get('DiskOverload') is not None:
            self.disk_overload = m.get('DiskOverload')

        if m.get('DisplayMode') is not None:
            self.display_mode = m.get('DisplayMode')

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        self.domain_resolve_rule = []
        if m.get('DomainResolveRule') is not None:
            for k1 in m.get('DomainResolveRule'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsDomainResolveRule()
                self.domain_resolve_rule.append(temp_model.from_map(k1))

        if m.get('DomainResolveRuleType') is not None:
            self.domain_resolve_rule_type = m.get('DomainResolveRuleType')

        if m.get('EdsCount') is not None:
            self.eds_count = m.get('EdsCount')

        if m.get('EndUserApplyAdminCoordinate') is not None:
            self.end_user_apply_admin_coordinate = m.get('EndUserApplyAdminCoordinate')

        if m.get('EndUserGroupCoordinate') is not None:
            self.end_user_group_coordinate = m.get('EndUserGroupCoordinate')

        if m.get('ExternalDrive') is not None:
            self.external_drive = m.get('ExternalDrive')

        if m.get('FileMigrate') is not None:
            self.file_migrate = m.get('FileMigrate')

        if m.get('FileTransfer') is not None:
            self.file_transfer = m.get('FileTransfer')

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')

        self.net_redirect_rule = []
        if m.get('NetRedirectRule') is not None:
            for k1 in m.get('NetRedirectRule'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsNetRedirectRule()
                self.net_redirect_rule.append(temp_model.from_map(k1))

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupType') is not None:
            self.policy_group_type = m.get('PolicyGroupType')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('PortProxy') is not None:
            self.port_proxy = m.get('PortProxy')

        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')

        if m.get('PreemptLoginUsers') is not None:
            self.preempt_login_users = m.get('PreemptLoginUsers')

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

        if m.get('RecordEventFileExts') is not None:
            self.record_event_file_exts = m.get('RecordEventFileExts')

        if m.get('RecordEventFilePaths') is not None:
            self.record_event_file_paths = m.get('RecordEventFilePaths')

        self.record_event_levels = []
        if m.get('RecordEventLevels') is not None:
            for k1 in m.get('RecordEventLevels'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsRecordEventLevels()
                self.record_event_levels.append(temp_model.from_map(k1))

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

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionModel') is not None:
            self.resolution_model = m.get('ResolutionModel')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        if m.get('ResourceGroupCount') is not None:
            self.resource_group_count = m.get('ResourceGroupCount')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

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

        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')

        self.usb_supply_redirect_rule = []
        if m.get('UsbSupplyRedirectRule') is not None:
            for k1 in m.get('UsbSupplyRedirectRule'):
                temp_model = main_models.DescribePolicyGroupsResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule()
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

        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')

        if m.get('WatermarkTransparencyValue') is not None:
            self.watermark_transparency_value = m.get('WatermarkTransparencyValue')

        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')

        if m.get('WuyingKeeper') is not None:
            self.wuying_keeper = m.get('WuyingKeeper')

        if m.get('WyAssistant') is not None:
            self.wy_assistant = m.get('WyAssistant')

        return self

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsUsbSupplyRedirectRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        device_class: str = None,
        device_subclass: str = None,
        product_id: str = None,
        usb_redirect_type: int = None,
        usb_rule_type: int = None,
        vendor_id: str = None,
    ):
        # The rule description.
        self.description = description
        # The device class. This parameter is required when `usbRuleType` is set to 1. For more information, see [Defined Class Codes](https://www.usb.org/defined-class-codes).
        self.device_class = device_class
        # The subclass of the device. This parameter is required when `usbRuleType` is set to 1. For more information, see [Defined Class Codes](https://www.usb.org/defined-class-codes).
        self.device_subclass = device_subclass
        # The product ID.
        self.product_id = product_id
        # Indicates whether USB redirection is allowed.
        # 
        # Valid values:
        # 
        # *   1: allowed
        # *   2: not allowed
        self.usb_redirect_type = usb_redirect_type
        # The type of the USB redirection rule.
        # 
        # Valid values:
        # 
        # *   1: by device class
        # *   2: by device vendor
        self.usb_rule_type = usb_rule_type
        # The vendor ID (VID). For more information, see [Valid USB VIDs](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf).
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

        if self.device_class is not None:
            result['DeviceClass'] = self.device_class

        if self.device_subclass is not None:
            result['DeviceSubclass'] = self.device_subclass

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

        if m.get('DeviceClass') is not None:
            self.device_class = m.get('DeviceClass')

        if m.get('DeviceSubclass') is not None:
            self.device_subclass = m.get('DeviceSubclass')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('UsbRedirectType') is not None:
            self.usb_redirect_type = m.get('UsbRedirectType')

        if m.get('UsbRuleType') is not None:
            self.usb_rule_type = m.get('UsbRuleType')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsRecordEventLevels(DaraModel):
    def __init__(
        self,
        event_level: str = None,
        event_type: str = None,
    ):
        # The event severity.
        self.event_level = event_level
        # The event type.
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

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsNetRedirectRule(DaraModel):
    def __init__(
        self,
        domain: str = None,
        policy: str = None,
        rule_type: str = None,
    ):
        # The rule content.
        self.domain = domain
        # Indicates whether the rule is allowed.
        # 
        # Valid values:
        # 
        # *   allow
        # *   block
        self.policy = policy
        # The rule type.
        # 
        # Valid values:
        # 
        # *   prc: process
        # *   domain: domain name
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

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsDomainResolveRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain: str = None,
        policy: str = None,
    ):
        # The rule description.
        self.description = description
        # The destination domain name.
        self.domain = domain
        # Indicates whether the domain name resolution rule is allowed.
        # 
        # Valid values:
        # 
        # *   allow
        # *   block
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

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsDeviceRules(DaraModel):
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
        # 
        # Valid values:
        # 
        # *   usbKey
        # *   other
        # *   graphicsTablet
        # *   printer
        # *   cardReader
        # *   scanner
        # *   storage
        # *   camera
        # *   adb
        # *   networkInterfaceCard: the NIC device.
        self.device_type = device_type
        # The vendor ID (VID). For more information, see [Valid USB VIDs](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf).
        self.device_vid = device_vid
        # The link optimization command.
        self.opt_command = opt_command
        self.platforms = platforms
        # The redirection type.
        # 
        # Valid values:
        # 
        # *   deviceRedirect
        # *   usbRedirect
        # *   off: redirection disabled.
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

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsDeviceRedirects(DaraModel):
    def __init__(
        self,
        device_type: str = None,
        redirect_type: str = None,
    ):
        # The peripheral type.
        # 
        # Valid values:
        # 
        # *   printer
        # *   scanner
        # *   camera
        # *   adb: the Android Debug Bridge (ADB) device.
        self.device_type = device_type
        # The redirection type. Valid values:
        # 
        # *   usbRedirect
        # *   deviceRedirect
        # *   off: direction disabled.
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

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsClientTypes(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # The client type.
        # 
        # Valid values:
        # 
        # *   html5: web client
        # *   android: Android client
        # *   windows: Windows client
        # *   ios: iOS client
        # *   macos: macOS client
        self.client_type = client_type
        # Indicates whether end users are allowed to use a specific type of the client to connect to cloud computers.
        # 
        # Valid values:
        # 
        # *   OFF
        # *   ON
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

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeSecurityPolicyRules(DaraModel):
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
        # 
        # Valid values:
        # 
        # *   tcp: Transmission Control Protocol (TCP)
        # *   udp: User Datagram Protocol (UDP)
        # *   all: all protocols
        # *   gre: Generic Routing Encapsulation (GRE)
        # *   icmp: Internet Control Message Protocol (ICMP) for IPv4
        self.ip_protocol = ip_protocol
        # The authorization of the security group rule.
        # 
        # Valid values:
        # 
        # *   drop: denies all access requests.
        # *   accept: accepts all requests.
        self.policy = policy
        # The port range of the security group rule.
        self.port_range = port_range
        # The priority of the security group rule. A smaller value indicates a higher priority.
        self.priority = priority
        # The direction of the security group rule.
        # 
        # Valid values:
        # 
        # *   outflow: outbound
        # *   inflow: inbound
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

class DescribePolicyGroupsResponseBodyDescribePolicyGroupsAuthorizeAccessPolicyRules(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        # The CIDR block that is allowed to access the client. The value is an IPv4 CIDR block.
        self.cidr_ip = cidr_ip
        # The remarks on the CIDR block that is allowed to access the client.
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

