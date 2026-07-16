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
        # Specifies whether a user has administrative permissions after logging on to the cloud computer.
        # 
        # > This feature is in invitational preview and is not available to the public.
        self.admin_access = admin_access
        # Specifies whether to enable the anti-screenshot feature.
        self.app_content_protection = app_content_protection
        # The client IP address whitelist. After you configure this parameter, only IP addresses in the whitelist can access the cloud computer.
        self.authorize_access_policy_rule = authorize_access_policy_rule
        # The list of security group rules.
        self.authorize_security_policy_rule = authorize_security_policy_rule
        # Specifies whether to enable local camera redirection.
        self.camera_redirect = camera_redirect
        # The list of logon method control rules. These rules control which clients can be used to access the cloud computer.
        self.client_type = client_type
        # The clipboard permission.
        self.clipboard = clipboard
        # The list of device redirection rules.
        self.device_redirects = device_redirects
        # The list of custom peripheral rules.
        self.device_rules = device_rules
        # The policy for controlling access to domain names. You can use a wildcard character (\\*). Separate multiple domain names with commas (,).
        self.domain_list = domain_list
        # The details of the domain name resolution policy.
        self.domain_resolve_rule = domain_resolve_rule
        # The type of the domain name resolution policy.
        self.domain_resolve_rule_type = domain_resolve_rule_type
        # Specifies whether to allow end users to request assistance from administrators.
        self.end_user_apply_admin_coordinate = end_user_apply_admin_coordinate
        # Specifies whether to enable stream collaboration between users.
        self.end_user_group_coordinate = end_user_group_coordinate
        # Specifies whether to enable the image quality policy for graphics cloud computers. Enable this policy for scenarios that require high performance and user experience, such as professional design.
        self.gpu_acceleration = gpu_acceleration
        # The policy for access from web clients.
        # 
        # > Use the `ClientType` parameters to manage logon methods.
        self.html_5access = html_5access
        # The file transfer policy for web clients.
        self.html_5file_transfer = html_5file_transfer
        # The network communication protocol.
        self.internet_communication_protocol = internet_communication_protocol
        # The local disk mapping permission.
        self.local_drive = local_drive
        # The maximum amount of time to retry the connection if the cloud computer is disconnected due to an unexpected event. Valid values: 30 to 7200. Unit: seconds.
        self.max_reconnect_time = max_reconnect_time
        # The policy name.
        self.name = name
        # Specifies whether to enable network redirection.
        # 
        # > This feature is in invitational preview and is not available to the public.
        self.net_redirect = net_redirect
        # The preemption policy.
        # 
        # > To ensure the user experience and data security of the end users who are using cloud computers, mutual preemption among multiple users is not allowed. This parameter is set to `off` by default and cannot be changed.
        self.preempt_login = preempt_login
        # The usernames of the users that are allowed to preempt the cloud computer. You can specify up to five usernames.
        # 
        # > To ensure the user experience and data security of the end users who are using cloud computers, mutual preemption among multiple users is not allowed.
        self.preempt_login_user = preempt_login_user
        # The printer redirection policy.
        self.printer_redirection = printer_redirection
        # Specifies whether to enable custom screen recording.
        self.record_content = record_content
        # The expiration time of custom recording files. The default value is 30. Unit: days.
        self.record_content_expires = record_content_expires
        # Specifies whether to enable screen recording.
        self.recording = recording
        # The option to record audio from the cloud computer.
        self.recording_audio = recording_audio
        # The duration for viewing the recording file. Unit: minutes. The recording file is automatically split based on the specified duration and uploaded to a bucket. If a file reaches 300 MB, it is rolled over first.
        self.recording_duration = recording_duration
        # The time when screen recording ends. The value is in the HH:MM:SS format. This parameter is valid only when \\`Recording\\` is set to \\`PERIOD\\`.
        self.recording_end_time = recording_end_time
        # The retention period of the recording file. Valid values: 1 to 180. Unit: days.
        self.recording_expires = recording_expires
        # The frame rate for screen recording. Unit: frames per second (fps).
        self.recording_fps = recording_fps
        # The time when screen recording starts. The value is in the HH:MM:SS format. This parameter is valid only when \\`Recording\\` is set to \\`PERIOD\\`.
        self.recording_start_time = recording_start_time
        # The feature that sends notifications to the client when screen recording is in progress.
        self.recording_user_notify = recording_user_notify
        # The content of the notification that is sent to the client when screen recording is in progress. You do not need to specify this parameter.
        self.recording_user_notify_message = recording_user_notify_message
        # The region ID. Call the [DescribeRegions](~~DescribeRegions~~) operation to obtain the list of regions that support WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The keyboard and mouse control permissions for remote assistance.
        self.remote_coordinate = remote_coordinate
        # The scope of the policy.
        self.scope = scope
        # This parameter is required when `Scope` is set to `IP`. It takes effect only when `Scope` is set to `IP`.
        self.scope_value = scope_value
        # USB redirection.
        self.usb_redirect = usb_redirect
        # The USB redirection rules.
        self.usb_supply_redirect_rule = usb_supply_redirect_rule
        # Multimedia redirection.
        self.video_redirect = video_redirect
        # The image display quality policy.
        self.visual_quality = visual_quality
        # The watermark feature.
        self.watermark = watermark
        # The anti-screen-recording feature for invisible watermarks.
        self.watermark_anti_cam = watermark_anti_cam
        # The font color of the watermark. Valid values: 0 to 16777215.
        self.watermark_color = watermark_color
        # The rotation angle of the watermark. Valid values: -10 to -30.
        self.watermark_degree = watermark_degree
        # The font size of the watermark. Valid values: 10 to 20.
        self.watermark_font_size = watermark_font_size
        # The font style of the watermark.
        self.watermark_font_style = watermark_font_style
        # The enhanced feature for invisible watermarks.
        self.watermark_power = watermark_power
        # The number of watermark rows.
        # 
        # > This parameter is not yet available.
        self.watermark_row_amount = watermark_row_amount
        # The security priority rule for invisible watermarks.
        self.watermark_security = watermark_security
        # The transparency of the watermark.
        self.watermark_transparency = watermark_transparency
        # The opacity of the watermark. A larger value indicates lower transparency. Valid values: 10 to 100.
        self.watermark_transparency_value = watermark_transparency_value
        # The type of watermark. You can specify up to three types. Separate multiple types with commas (,).
        # 
        # > If you set this parameter to `custom`, you must also specify the `WatermarkCustomText` parameter.
        self.watermark_type = watermark_type
        # When you connect to a cloud computer from a desktop client (including a Windows client and a macOS client), specifies whether to display the entry for the WUYING AI assistant in the floating ball on the cloud computer.
        # 
        # > This feature is available only for desktop clients of V7.7 or later.
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
        # The rule description.
        self.description = description
        # The device class. This parameter is required when `usbRuleType` is set to 1. For more information, see [Defined Class Codes](https://www.usb.org/defined-class-codes).
        self.device_class = device_class
        # The device subclass. This parameter is required when `usbRuleType` is set to 1. For more information, see [Defined Class Codes](https://www.usb.org/defined-class-codes).
        self.device_subclass = device_subclass
        # The product ID (PID).
        self.product_id = product_id
        # The USB redirection type.
        self.usb_redirect_type = usb_redirect_type
        # The USB redirection rule type.
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
        self.device_type = device_type
        # The vendor ID (VID). For more information, see [Valid USB Vendor IDs (VIDs)](https://www.usb.org/sites/default/files/vendor_ids032322.pdf_1.pdf).
        self.device_vid = device_vid
        # The link optimization instruction.
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

class CreatePolicyGroupRequestDeviceRedirects(DaraModel):
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

class CreatePolicyGroupRequestClientType(DaraModel):
    def __init__(
        self,
        client_type: str = None,
        status: str = None,
    ):
        # Logon method control. Specifies the client type.
        # 
        # > If you do not configure the `ClientType` parameters, all types of clients are allowed to log on to the cloud computer by default.
        self.client_type = client_type
        # Logon method control. Specifies whether to allow a specific type of client to log on to the cloud computer.
        # 
        # > If you do not configure the `ClientType` parameters, all types of clients are allowed to log on to the cloud computer by default.
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
        # The object of the security group rule. The value is an IPv4 CIDR block.
        self.cidr_ip = cidr_ip
        # The description of the security group rule.
        self.description = description
        # The protocol type of the security group rule.
        self.ip_protocol = ip_protocol
        # The authorization policy of the security group rule.
        self.policy = policy
        # The port range of the security group rule. The value of this parameter depends on the value of the \\`IpProtocol\\` parameter.
        # 
        # - If \\`IpProtocol\\` is set to TCP or UDP, the port range is 1 to 65535. Use a forward slash (/) to separate the start port and the end port. For example: 1/200.
        # 
        # - If \\`IpProtocol\\` is set to ICMP, the port range is -1/-1.
        # 
        # - If \\`IpProtocol\\` is set to GRE, the port range is -1/-1.
        # 
        # - If \\`IpProtocol\\` is set to all, the port range is -1/-1.
        # 
        # For more information about common ports, see [Common ports](https://help.aliyun.com/document_detail/40724.html).
        self.port_range = port_range
        # The priority of the security group rule. A smaller value indicates a higher priority.<br>
        # Valid values: 1 to 60.<br>
        # Default value: 1.<br><br>
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

class CreatePolicyGroupRequestAuthorizeAccessPolicyRule(DaraModel):
    def __init__(
        self,
        cidr_ip: str = None,
        description: str = None,
    ):
        # The client IP address CIDR block. The value is an IPv4 CIDR block.
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

