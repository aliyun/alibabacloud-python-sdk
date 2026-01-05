# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ModifyPolicyGroupRequest(DaraModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy: main_models.ModifyPolicyGroupRequestNetRedirectPolicy = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        resolution_height: int = None,
        resolution_width: int = None,
        watermark: main_models.ModifyPolicyGroupRequestWatermark = None,
    ):
        # Specifies whether to enable the webcam redirection feature.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.camera_redirect = camera_redirect
        # The read/write permissions on the clipboard.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.clipboard = clipboard
        # The file transfer policy of the Alibaba Cloud Workspace web client.
        # 
        # Valid values:
        # 
        # *   all: File upload and download are supported.
        # *   download: Only file download is supported.
        # *   upload: Only file upload is supported.
        # *   off: File upload or download is forbidden.
        self.html_5file_transfer = html_5file_transfer
        # The read/write permissions on the on-premises drive.
        # 
        # Valid values:
        # 
        # *   read: read-only.
        # *   readwrite: ready and write.
        # *   off: read/write disabled.
        self.local_drive = local_drive
        # Specifies whether to lock the resolution.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.lock_resolution = lock_resolution
        # The network redirection policy.
        self.net_redirect_policy = net_redirect_policy
        # The ID of the policy.
        self.policy_group_id = policy_group_id
        # The name of the policy.
        self.policy_group_name = policy_group_name
        # The height of the resolution. Unit: pixels.
        self.resolution_height = resolution_height
        # The width of the resolution. Unit: pixels.
        self.resolution_width = resolution_width
        self.watermark = watermark

    def validate(self):
        if self.net_redirect_policy:
            self.net_redirect_policy.validate()
        if self.watermark:
            self.watermark.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.camera_redirect is not None:
            result['CameraRedirect'] = self.camera_redirect

        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard

        if self.html_5file_transfer is not None:
            result['Html5FileTransfer'] = self.html_5file_transfer

        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive

        if self.lock_resolution is not None:
            result['LockResolution'] = self.lock_resolution

        if self.net_redirect_policy is not None:
            result['NetRedirectPolicy'] = self.net_redirect_policy.to_map()

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name

        if self.resolution_height is not None:
            result['ResolutionHeight'] = self.resolution_height

        if self.resolution_width is not None:
            result['ResolutionWidth'] = self.resolution_width

        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')

        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')

        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')

        if m.get('NetRedirectPolicy') is not None:
            temp_model = main_models.ModifyPolicyGroupRequestNetRedirectPolicy()
            self.net_redirect_policy = temp_model.from_map(m.get('NetRedirectPolicy'))

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')

        if m.get('ResolutionHeight') is not None:
            self.resolution_height = m.get('ResolutionHeight')

        if m.get('ResolutionWidth') is not None:
            self.resolution_width = m.get('ResolutionWidth')

        if m.get('Watermark') is not None:
            temp_model = main_models.ModifyPolicyGroupRequestWatermark()
            self.watermark = temp_model.from_map(m.get('Watermark'))

        return self

class ModifyPolicyGroupRequestWatermark(DaraModel):
    def __init__(
        self,
        watermark_color: int = None,
        watermark_custom_text: str = None,
        watermark_font_size: int = None,
        watermark_switch: str = None,
        watermark_transparency_value: int = None,
        watermark_types: List[str] = None,
    ):
        self.watermark_color = watermark_color
        self.watermark_custom_text = watermark_custom_text
        self.watermark_font_size = watermark_font_size
        self.watermark_switch = watermark_switch
        self.watermark_transparency_value = watermark_transparency_value
        self.watermark_types = watermark_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.watermark_color is not None:
            result['WatermarkColor'] = self.watermark_color

        if self.watermark_custom_text is not None:
            result['WatermarkCustomText'] = self.watermark_custom_text

        if self.watermark_font_size is not None:
            result['WatermarkFontSize'] = self.watermark_font_size

        if self.watermark_switch is not None:
            result['WatermarkSwitch'] = self.watermark_switch

        if self.watermark_transparency_value is not None:
            result['WatermarkTransparencyValue'] = self.watermark_transparency_value

        if self.watermark_types is not None:
            result['WatermarkTypes'] = self.watermark_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WatermarkColor') is not None:
            self.watermark_color = m.get('WatermarkColor')

        if m.get('WatermarkCustomText') is not None:
            self.watermark_custom_text = m.get('WatermarkCustomText')

        if m.get('WatermarkFontSize') is not None:
            self.watermark_font_size = m.get('WatermarkFontSize')

        if m.get('WatermarkSwitch') is not None:
            self.watermark_switch = m.get('WatermarkSwitch')

        if m.get('WatermarkTransparencyValue') is not None:
            self.watermark_transparency_value = m.get('WatermarkTransparencyValue')

        if m.get('WatermarkTypes') is not None:
            self.watermark_types = m.get('WatermarkTypes')

        return self

class ModifyPolicyGroupRequestNetRedirectPolicy(DaraModel):
    def __init__(
        self,
        custom_proxy: str = None,
        host_addr: str = None,
        net_redirect: str = None,
        port: str = None,
        proxy_password: str = None,
        proxy_type: str = None,
        proxy_user_name: str = None,
        rules: List[main_models.ModifyPolicyGroupRequestNetRedirectPolicyRules] = None,
    ):
        # Specifies whether to manually configure a custom proxy.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.custom_proxy = custom_proxy
        # The IPv4 address of the custom proxy.
        self.host_addr = host_addr
        # Specifies whether to enable network redirection.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.net_redirect = net_redirect
        # The port of the custom proxy. Valid values: 1 to 65535.
        self.port = port
        # The password of the proxy. The password must be 1 to 256 in length and cannot contain Chinese character or space characters.
        self.proxy_password = proxy_password
        # The type of the proxy protocol.
        # 
        # Valid values:
        # 
        # *   socks5.
        self.proxy_type = proxy_type
        # The username of the proxy. The name must be 1 to 256 in length and cannot contain Chinese character or space characters.
        self.proxy_user_name = proxy_user_name
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_proxy is not None:
            result['CustomProxy'] = self.custom_proxy

        if self.host_addr is not None:
            result['HostAddr'] = self.host_addr

        if self.net_redirect is not None:
            result['NetRedirect'] = self.net_redirect

        if self.port is not None:
            result['Port'] = self.port

        if self.proxy_password is not None:
            result['ProxyPassword'] = self.proxy_password

        if self.proxy_type is not None:
            result['ProxyType'] = self.proxy_type

        if self.proxy_user_name is not None:
            result['ProxyUserName'] = self.proxy_user_name

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomProxy') is not None:
            self.custom_proxy = m.get('CustomProxy')

        if m.get('HostAddr') is not None:
            self.host_addr = m.get('HostAddr')

        if m.get('NetRedirect') is not None:
            self.net_redirect = m.get('NetRedirect')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ProxyPassword') is not None:
            self.proxy_password = m.get('ProxyPassword')

        if m.get('ProxyType') is not None:
            self.proxy_type = m.get('ProxyType')

        if m.get('ProxyUserName') is not None:
            self.proxy_user_name = m.get('ProxyUserName')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ModifyPolicyGroupRequestNetRedirectPolicyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ModifyPolicyGroupRequestNetRedirectPolicyRules(DaraModel):
    def __init__(
        self,
        rule_type: str = None,
        target: str = None,
    ):
        self.rule_type = rule_type
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

