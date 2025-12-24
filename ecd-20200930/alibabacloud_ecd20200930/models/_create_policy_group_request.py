# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreatePolicyGroupRequest(DaraModel):
    def __init__(
        self,
        admin_access: str = None,
        app_content_protection: str = None,
        authorize_access_policy_rule: List[main_models.CreatePolicyGroupRequestAuthorizeAccessPolicyRule] = None,
        authorize_security_policy_rule: List[main_models.CreatePolicyGroupRequestAuthorizeSecurityPolicyRule] = None,
        camera_redirect: str = None,
        client_type: List[main_models.CreatePolicyGroupRequestClientType] = None,
        clipboard: str = None,
        device_redirects: List[main_models.CreatePolicyGroupRequestDeviceRedirects] = None,
        device_rules: List[main_models.CreatePolicyGroupRequestDeviceRules] = None,
        domain_list: str = None,
        domain_resolve_rule: List[main_models.CreatePolicyGroupRequestDomainResolveRule] = None,
        domain_resolve_rule_type: str = None,
        end_user_apply_admin_coordinate: str = None,
        end_user_group_coordinate: str = None,
        gpu_acceleration: str = None,
        html_5access: str = None,
        html_5file_transfer: str = None,
        internet_communication_protocol: str = None,
        local_drive: str = None,
        max_reconnect_time: int = None,
        name: str = None,
        net_redirect: str = None,
        preempt_login: str = None,
        preempt_login_user: List[str] = None,
        printer_redirection: str = None,
        record_content: str = None,
        record_content_expires: int = None,
        recording: str = None,
        recording_audio: str = None,
        recording_duration: int = None,
        recording_end_time: str = None,
        recording_expires: int = None,
        recording_fps: int = None,
        recording_start_time: str = None,
        recording_user_notify: str = None,
        recording_user_notify_message: str = None,
        region_id: str = None,
        remote_coordinate: str = None,
        scope: str = None,
        scope_value: List[str] = None,
        usb_redirect: str = None,
        usb_supply_redirect_rule: List[main_models.CreatePolicyGroupRequestUsbSupplyRedirectRule] = None,
        video_redirect: str = None,
        visual_quality: str = None,
        watermark: str = None,
        watermark_anti_cam: str = None,
        watermark_color: int = None,
        watermark_degree: float = None,
        watermark_font_size: int = None,
        watermark_font_style: str = None,
        watermark_power: str = None,
        watermark_row_amount: int = None,
        watermark_security: str = None,
        watermark_transparency: str = None,
        watermark_transparency_value: int = None,
        watermark_type: str = None,
        wy_assistant: str = None,
    ):
        # Specifies whether end users have the administrator permissions.
        # 
        # >  This parameter is in invitational preview for specific users and not available to the public.
        self.admin_access = admin_access
        # Specifies whether to enable the anti-screenshot feature.
        # 
        # Valid values:
        # 
        # *   off: Anti-screenshot is disabled. This value is the default value.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   on: Anti-screenshot is enabled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.app_content_protection = app_content_protection
        # The client IP address whitelist. After you configure the whitelist, end users can access cloud computers only from the IP addresses in the whitelist.
        self.authorize_access_policy_rule = authorize_access_policy_rule
        # The security group rules.
        self.authorize_security_policy_rule = authorize_security_policy_rule
        # Specifies whether to enable the webcam redirection feature.
        # 
        # Valid values:
        # 
        # *   off: Webcam redirection is disabled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   on: Webcam redirection is enabled. This value is the default value.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.camera_redirect = camera_redirect
        # The logon method control rules to limit the type of the Alibaba Cloud Workspace client used by end users to connect to cloud computers.
        self.client_type = client_type
        # The permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: specifies one-way transfer. You can copy files only from local devices to cloud computers.
        # *   readwrite: specifies two-way transfer. You can copy files between local devices and cloud computers.
        # *   write: specifies one-way transfer. You can only copy files from cloud computers to local devices.
        # *   off (default): disables both one-way and two-way transfer. Files cannot be copied between local devices and cloud computers.
        self.clipboard = clipboard
        # The device redirection rules.
        self.device_redirects = device_redirects
        # The custom peripheral rules.
        self.device_rules = device_rules
        # Specifies whether the access control for domain names is enabled. Domain names support wildcards (\\*). Separate multiple domain names with commas (,).
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.domain_list = domain_list
        # The details of the domain name resolution rule.
        self.domain_resolve_rule = domain_resolve_rule
        # The type of the domain name resolution policy.
        # 
        # Valid values:
        # 
        # *   OFF
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ON
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.domain_resolve_rule_type = domain_resolve_rule_type
        # Specifies whether to turn on the Contact Administrator for Help switch.
        # 
        # Valid values:
        # 
        # *   OFF
        # *   ON
        self.end_user_apply_admin_coordinate = end_user_apply_admin_coordinate
        # Specifies whether to turn on the User Stream Collaboration switch.
        # 
        # Valid values:
        # 
        # *   OFF
        # *   ON
        self.end_user_group_coordinate = end_user_group_coordinate
        # Specifies whether to enable the Image Quality Control feature. If you have high requirements on the performance and user experience in scenarios such as professional design, we recommend that you enable this feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.gpu_acceleration = gpu_acceleration
        # Specifies whether to allow web client access.
        # 
        # >  We recommend that you use the ClientType-related parameters to control the Alibaba Cloud Workspace client type for cloud computer logon.``
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
        # *   TCP (default): TCP
        # *   BOTH: TCP and UDP
        self.internet_communication_protocol = internet_communication_protocol
        # The permissions on local disk mapping.
        # 
        # Valid values:
        # 
        # *   read: read-only. Local disk mapping is available on cloud computers. However, you can only read (copy) local files but cannot modify the files.
        # *   readwrite: read and write. Local disk mapping is available on cloud computers. You can read (copy) and write (modify) local files.
        # *   off (default): disabled. Local disk mapping is unavailable on cloud computers.
        self.local_drive = local_drive
        # The maximum retry period for reconnecting to cloud computers when the cloud computers are disconnected due to none-human reasons. Valid values: 30 to 7200. Unit: seconds.
        self.max_reconnect_time = max_reconnect_time
        # The name of the policy.
        self.name = name
        # Specifies whether to enable the network redirection feature.
        # 
        # > This feature is in invitational preview and is not available to the public.
        # 
        # Valid values:
        # 
        # *   off (default): The network redirection feature is disabled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   on: The network redirection feature is enabled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.net_redirect = net_redirect
        # The cloud computer preemption feature.
        # 
        # >  To ensure user experience and data security, when a cloud computer is used by an end user, other end users cannot connect to the cloud computer. By default, this parameter is set to `off`, which cannot be modified.
        # 
        # Valid values:
        # 
        # *   off (default): Multiple end users cannot connect to the same cloud computer at the same time.
        self.preempt_login = preempt_login
        # The usernames that are allowed to connect to the cloud computer in use. You can specify up to five usernames.
        # 
        # >  To ensure user experience and data security, other end users cannot connect to the cloud computer that is used by an end user.
        self.preempt_login_user = preempt_login_user
        # The policy for printer redirection.
        # 
        # Valid values:
        # 
        # *   off: Printer redirection is disabled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   on: Printer redirection is enabled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.printer_redirection = printer_redirection
        # Specifies whether to enable the custom screen recording feature.
        # 
        # Valid values:
        # 
        # *   off: Custom screen recording is disabled. This value is the default value.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   on: Custom screen recording is enabled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.record_content = record_content
        # The duration in which the custom screen recording is valid. Default value: 30. Unit: days.
        self.record_content_expires = record_content_expires
        # Specifies whether to enable the screen recording feature.
        # 
        # Valid values:
        # 
        # *   byaction_cmd_ft: enables the operation-triggered screen recording upon command execution and file transfer.
        # *   ALLTIME: enables the whole-process screen recording. That is, the recording starts when cloud computers are connected and ends when the cloud computers are disconnected.
        # *   session: enables the screen recording for session lifecycle listening.
        # *   PERIOD: enables the interval-based screen recording. You must specify an interval between the start time and end time of this type of recording.
        # *   byaction_commands: enables the operation-triggered screen recording upon command execution.
        # *   OFF: disables the screen recording feature.
        # *   byaction_file_transfer: enables the operation-triggered screen recording upon file transfer.
        self.recording = recording
        # Specifies whether to record audio files generated from cloud computers.
        # 
        # Valid values:
        # 
        # *   off: records only video files.
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
        # The time when the screen recording ends. The value is in the HH:MM:SS format. The value is meaningful only when you set the `Recording` parameter to `PERIOD`.
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
        # The time when the screen recording starts. The value is in the HH:MM:SS format. The value is meaningful only when you set the `Recording` parameter to `PERIOD`.
        self.recording_start_time = recording_start_time
        # Specifies whether to enable the screen recording notification feature after end users log on to the Alibaba Cloud Workspace client.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.recording_user_notify = recording_user_notify
        # The notification content of screen recording. By default, this parameter is left empty.
        self.recording_user_notify_message = recording_user_notify_message
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service (EDS).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The permission to control the keyboard and the mouse during remote assistance.
        # 
        # Valid values:
        # 
        # *    optionalControl: By default, this feature is disabled. You can enable it by applying permissions.
        # 
        # *   fullControl: The permission is granted.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   disableControl: The permission is revoked.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.remote_coordinate = remote_coordinate
        # The effective scope of the policy.
        # 
        # Valid values:
        # 
        # *   IP: The policy takes effect based on the IP address.
        # *   GLOBAL: The policy takes effect globally.
        self.scope = scope
        # This parameter is required when the `Scope` parameter is set to `IP`.````
        self.scope_value = scope_value
        # Specifies whether to enable USB redirection.
        # 
        # Valid values:
        # 
        # *   off: USB redirection is disabled. This value is the default value.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   on: USB redirection is enabled.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.usb_redirect = usb_redirect
        # The USB redirection rules.
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        # Specifies whether to enable the multimedia redirection switch.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.video_redirect = video_redirect
        # The policy for image display quality.
        # 
        # Valid values:
        # 
        # *   high
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   low
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   lossless
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   medium: adaptive. This value is the default value.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.visual_quality = visual_quality
        # The watermarking feature.
        # 
        # Valid values:
        # 
        # *   blind: Invisible watermarks are applied.
        # *   off (default): The watermarking feature is disabled.
        # *   on: Visible watermarks are applied.
        self.watermark = watermark
        # Specifies whether to enable the anti-screen photo feature for invisible watermarks.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.watermark_anti_cam = watermark_anti_cam
        # The font color in red, green, and blue (RGB) of the watermark. Valid values: 0 to 16777215.
        self.watermark_color = watermark_color
        # The watermark rotation. Valid values: -10 to -30.
        self.watermark_degree = watermark_degree
        # The watermark font size. Valid values: 10 to 20.
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
        # Specifies whether to enable the security priority feature for invisible watermarks.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.watermark_security = watermark_security
        # The transparency of the watermark.
        # 
        # Valid values:
        # 
        # *   LIGHT
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DARK
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MIDDLE
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.watermark_transparency = watermark_transparency
        # The watermark opacity. A larger value indicates more opaque watermarks. Valid values: 10 to 100.
        self.watermark_transparency_value = watermark_transparency_value
        # The watermark content. You can select up to three items as the watermark content. Separate multiple items with commas (,).
        # 
        # >  If you set this parameter to `Custom`, specify `WatermarkCustomText`
        # 
        # Valid values:
        # 
        # *   EndUserId: the username.
        # *   Custom: the custom text.
        # *   DesktopIp: the IP address of the cloud computer.
        # *   ClientIp: the IP address of the Alibaba Cloud Workspace client.
        # *   HostName: the rightmost 15 digits of the cloud computer ID.
        # *   ClientTime: the current time displayed on the cloud computer.
        self.watermark_type = watermark_type
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

        result['AuthorizeAccessPolicyRule'] = []
        if self.authorize_access_policy_rule is not None:
            for k1 in self.authorize_access_policy_rule:
                result['AuthorizeAccessPolicyRule'].append(k1.to_map() if k1 else None)

        result['AuthorizeSecurityPolicyRule'] = []
        if self.authorize_security_policy_rule is not None:
            for k1 in self.authorize_security_policy_rule:
                result['AuthorizeSecurityPolicyRule'].append(k1.to_map() if k1 else None)

        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect

        result['ClientType'] = []
        if self.client_type is not None:
            for k1 in self.client_type:
                result['ClientType'].append(k1.to_map() if k1 else None)

        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        result['DeviceRedirects'] = []
        if self.device_redirects is not None:
            for k1 in self.device_redirects:
                result['DeviceRedirects'].append(k1.to_map() if k1 else None)

        result['DeviceRules'] = []
        if self.device_rules is not None:
            for k1 in self.device_rules:
                result['DeviceRules'].append(k1.to_map() if k1 else None)

        if self.domain_list is not None:
            result['DomainList'] = self.domain_list

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

        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration

        if self.html_5access is not None:
            result['Html5Access'] = self.html_5access

        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer

        if self.internet_communication_protocol is not None:
            result['InternetCommunicationProtocol'] = self.internet_communication_protocol

        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive

        if self.max_reconnect_time is not None:
            result['MaxReconnectTime'] = self.max_reconnect_time

        if self.name is not None:
            result['Name'] = self.name

        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect

        if self.preempt_login is not None:
            result['PreemptLogin'] = self.preempt_login

        if self.preempt_login_user is not None:
            result['PreemptLoginUser'] = self.preempt_login_user

        if self.printer_redirection is not None:
            result['PrinterRedirection'] = self.printer_redirection

        if self.record_content is not None:
            result['RecordContent'] = self.record_content

        if self.record_content_expires is not None:
            result['RecordContentExpires'] = self.record_content_expires

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

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.scope_value is not None:
            result['ScopeValue'] = self.scope_value

        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect

        result['UsbSupplyRedirectRule'] = []
        if self.usb_supply_redirect_rule is not None:
            for k1 in self.usb_supply_redirect_rule:
                result['UsbSupplyRedirectRule'].append(k1.to_map() if k1 else None)

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

        if self.watermark_transparency is not None:
            result['WatermarkTransparency'] = self.watermark_transparency

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

        self.authorize_access_policy_rule = []
        if m.get('AuthorizeAccessPolicyRule') is not None:
            for k1 in m.get('AuthorizeAccessPolicyRule'):
                temp_model = main_models.CreatePolicyGroupRequestAuthorizeAccessPolicyRule()
                self.authorize_access_policy_rule.append(temp_model.from_map(k1))

        self.authorize_security_policy_rule = []
        if m.get('AuthorizeSecurityPolicyRule') is not None:
            for k1 in m.get('AuthorizeSecurityPolicyRule'):
                temp_model = main_models.CreatePolicyGroupRequestAuthorizeSecurityPolicyRule()
                self.authorize_security_policy_rule.append(temp_model.from_map(k1))

        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')

        self.client_type = []
        if m.get('ClientType') is not None:
            for k1 in m.get('ClientType'):
                temp_model = main_models.CreatePolicyGroupRequestClientType()
                self.client_type.append(temp_model.from_map(k1))

        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        self.device_redirects = []
        if m.get('DeviceRedirects') is not None:
            for k1 in m.get('DeviceRedirects'):
                temp_model = main_models.CreatePolicyGroupRequestDeviceRedirects()
                self.device_redirects.append(temp_model.from_map(k1))

        self.device_rules = []
        if m.get('DeviceRules') is not None:
            for k1 in m.get('DeviceRules'):
                temp_model = main_models.CreatePolicyGroupRequestDeviceRules()
                self.device_rules.append(temp_model.from_map(k1))

        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')

        self.domain_resolve_rule = []
        if m.get('DomainResolveRule') is not None:
            for k1 in m.get('DomainResolveRule'):
                temp_model = main_models.CreatePolicyGroupRequestDomainResolveRule()
                self.domain_resolve_rule.append(temp_model.from_map(k1))

        if m.get('DomainResolveRuleType') is not None:
            self.domain_resolve_rule_type = m.get('DomainResolveRuleType')

        if m.get('EndUserApplyAdminCoordinate') is not None:
            self.end_user_apply_admin_coordinate = m.get('EndUserApplyAdminCoordinate')

        if m.get('EndUserGroupCoordinate') is not None:
            self.end_user_group_coordinate = m.get('EndUserGroupCoordinate')

        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')

        if m.get('Html5Access') is not None:
            self.html_5access = m.get('Html5Access')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('InternetCommunicationProtocol') is not None:
            self.internet_communication_protocol = m.get('InternetCommunicationProtocol')

        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')

        if m.get('MaxReconnectTime') is not None:
            self.max_reconnect_time = m.get('MaxReconnectTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')

        if m.get('PreemptLogin') is not None:
            self.preempt_login = m.get('PreemptLogin')

        if m.get('PreemptLoginUser') is not None:
            self.preempt_login_user = m.get('PreemptLoginUser')

        if m.get('PrinterRedirection') is not None:
            self.printer_redirection = m.get('PrinterRedirection')

        if m.get('RecordContent') is not None:
            self.record_content = m.get('RecordContent')

        if m.get('RecordContentExpires') is not None:
            self.record_content_expires = m.get('RecordContentExpires')

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

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ScopeValue') is not None:
            self.scope_value = m.get('ScopeValue')

        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')

        self.usb_supply_redirect_rule = []
        if m.get('UsbSupplyRedirectRule') is not None:
            for k1 in m.get('UsbSupplyRedirectRule'):
                temp_model = main_models.CreatePolicyGroupRequestUsbSupplyRedirectRule()
                self.usb_supply_redirect_rule.append(temp_model.from_map(k1))

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

        if m.get('WatermarkTransparency') is not None:
            self.watermark_transparency = m.get('WatermarkTransparency')

        if m.get('WatermarkTransparencyValue') is not None:
            self.watermark_transparency_value = m.get('WatermarkTransparencyValue')

        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')

        if m.get('WyAssistant') is not None:
            self.wy_assistant = m.get('WyAssistant')

        return self

class CreatePolicyGroupRequestUsbSupplyRedirectRule(DaraModel):
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
        # The description of the rule.
        self.description = description
        # The class of the device. If you set the `usbRuleType` parameter to 1, you must specify this parameter. For more information, see [Defined Class Codes](https://www.usb.org/defined-class-codes).
        self.device_class = device_class
        # The subclass of the device. If you set the `usbRuleType` parameter to 1, you must specify this parameter. For more information, see [Defined Class Codes](https://www.usb.org/defined-class-codes).
        self.device_subclass = device_subclass
        # The ID of the service.
        self.product_id = product_id
        # The type of USB redirection.
        # 
        # Valid values:
        # 
        # *   1: allows USB redirection
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   2: forbids USB redirection
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.usb_redirect_type = usb_redirect_type
        # The type of the USB redirection rule.
        # 
        # Valid values:
        # 
        # *   1: by device class
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   2: by device vendor
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.usb_rule_type = usb_rule_type
        # The ID of the vendor. For more information, see [Valid USB Vendor IDs (VIDs)](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf).
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

class CreatePolicyGroupRequestDomainResolveRule(DaraModel):
    def __init__(
        self,
        description: str = None,
        domain: str = None,
        policy: str = None,
    ):
        # The description of domain name resolution rule.
        self.description = description
        # The domain name.
        self.domain = domain
        # Specifies whether to allow the domain name resolution rule.
        # 
        # Valid values:
        # 
        # *   allow: allows the rule.
        # *   block: denies the rule.
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

class CreatePolicyGroupRequestDeviceRules(DaraModel):
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
        # *   usbKey: UKeys.
        # *   other: other peripheral devices.
        # *   graphicsTablet: graphics tablets.
        # *   printer: printers.
        # *   cardReader: card readers.
        # *   scanner: scanners.
        # *   storage: storage devices.
        # *   camera: web cameras.
        # *   adb: Android Debug Bridge (ADB) devices.
        # *   networkInterfaceCard: NIC devices.
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
        # *   deviceRedirect: device redirection
        # *   usbRedirect: USB redirection
        # *   off: redirection disabled
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

class CreatePolicyGroupRequestDeviceRedirects(DaraModel):
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
        # The redirection type.
        # 
        # Valid values:
        # 
        # *   deviceRedirect: device redirection
        # *   usbRedirect: USB redirection
        # *   off: redirection disabled
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

class CreatePolicyGroupRequestClientType(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # The type of the Alibaba Cloud Workspace client.
        # 
        # >  If you do not specify the `ClientType` parameter, all types of the client are allowed by default.
        # 
        # Valid values:
        # 
        # *   html5: web client
        # *   android: Android client
        # *   ios: iOS client
        # *   windows: Windows client
        # *   macos: macOS client
        self.client_type = client_type
        # Specifies whether to allow end users to use a specific type of the client to connect to cloud computers.
        # 
        # >  If you do not specify the `ClientType` parameter, all types of the client are allowed by default.
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

class CreatePolicyGroupRequestAuthorizeSecurityPolicyRule(DaraModel):
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
        # *   TCP: the Transmission Control Protocol (TCP) protocol.
        # *   UDP: the User Datagram Protocol (UDP) protocol.
        # *   ALL: all protocols.
        # *   GRE: the Generic Routing Encapsulation (GRE) protocol.
        # *   ICMP: the Internet Control Message Protocol (ICMP) for IPv4.
        self.ip_protocol = ip_protocol
        # The authorization of the security group rule.
        # 
        # Valid values:
        # 
        # *   drop: denies all access requests. If no messages of access denied are returned, the requests timed out or failed.
        # *   accept (default): accepts all requests.
        self.policy = policy
        # The port range of the security group rule. The value range of this parameter varies based on the value of the IpProtocol parameter.
        # 
        # *   If the IpProtocol parameter is set to TCP or UDP, the port range is 1 to 65535. Separate the start port number and the end port number with a forward slash (/). Example: 1/200.
        # *   If the IpProtocol parameter is set to ICMP, set the value to -1/-1.
        # *   If the IpProtocol parameter is set to GRE, set the value to -1/-1.
        # *   If the IpProtocol parameter is set to ALL, set the value to -1/-1.
        # 
        # For more information about the common ports applied in EDS, see [Common ports](https://help.aliyun.com/document_detail/40724.html).
        self.port_range = port_range
        # The priority of the security group rule. A smaller value indicates a higher priority.\\
        # Valid values: 1 to 60.\\
        # Default value: 1.
        self.priority = priority
        # The direction of the security group rule.
        # 
        # Valid values:
        # 
        # *   outflow: outbound.
        # *   inflow: inbound.
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

class CreatePolicyGroupRequestAuthorizeAccessPolicyRule(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        # The client CIDR block from which end users can connect to cloud computers. The value is an IPv4 CIDR block.
        self.cidr_ip = cidr_ip
        # The description of the client IP address whitelist.
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

