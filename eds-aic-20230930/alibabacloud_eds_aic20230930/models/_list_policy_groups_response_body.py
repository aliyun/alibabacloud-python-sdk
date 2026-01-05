# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ListPolicyGroupsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        policy_group_model: List[main_models.ListPolicyGroupsResponseBodyPolicyGroupModel] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The policies.
        self.policy_group_model = policy_group_model
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.policy_group_model:
            for v1 in self.policy_group_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PolicyGroupModel'] = []
        if self.policy_group_model is not None:
            for k1 in self.policy_group_model:
                result['PolicyGroupModel'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.policy_group_model = []
        if m.get('PolicyGroupModel') is not None:
            for k1 in m.get('PolicyGroupModel'):
                temp_model = main_models.ListPolicyGroupsResponseBodyPolicyGroupModel()
                self.policy_group_model.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPolicyGroupsResponseBodyPolicyGroupModel(DaraModel):
    def __init__(
        self,
        camera_redirect: str = None,
        clipboard: str = None,
        gmt_create: str = None,
        html_5file_transfer: str = None,
        local_drive: str = None,
        lock_resolution: str = None,
        net_redirect_policy: main_models.ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy = None,
        policy_group_id: str = None,
        policy_group_name: str = None,
        policy_related_resources: main_models.ListPolicyGroupsResponseBodyPolicyGroupModelPolicyRelatedResources = None,
        session_resolution_height: int = None,
        session_resolution_width: int = None,
        watermark: main_models.ListPolicyGroupsResponseBodyPolicyGroupModelWatermark = None,
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
        # *   readwrite: read and write.
        # *   off: read/write disabled.
        self.clipboard = clipboard
        # The time when the policy was created.
        self.gmt_create = gmt_create
        # The file transfer policy of the HTML5 client.
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
        # *   off: read/write denied.
        self.local_drive = local_drive
        # Identifies whether the resolution is locked.
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
        self.policy_related_resources = policy_related_resources
        # The height of the resolution.
        self.session_resolution_height = session_resolution_height
        # The width of the resolution.
        self.session_resolution_width = session_resolution_width
        self.watermark = watermark

    def validate(self):
        if self.net_redirect_policy:
            self.net_redirect_policy.validate()
        if self.policy_related_resources:
            self.policy_related_resources.validate()
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

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

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

        if self.policy_related_resources is not None:
            result['PolicyRelatedResources'] = self.policy_related_resources.to_map()

        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height

        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width

        if self.watermark is not None:
            result['Watermark'] = self.watermark.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraRedirect') is not None:
            self.camera_redirect = m.get('CameraRedirect')

        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Html5FileTransfer') is not None:
            self.html_5file_transfer = m.get('Html5FileTransfer')

        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')

        if m.get('LockResolution') is not None:
            self.lock_resolution = m.get('LockResolution')

        if m.get('NetRedirectPolicy') is not None:
            temp_model = main_models.ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy()
            self.net_redirect_policy = temp_model.from_map(m.get('NetRedirectPolicy'))

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')

        if m.get('PolicyRelatedResources') is not None:
            temp_model = main_models.ListPolicyGroupsResponseBodyPolicyGroupModelPolicyRelatedResources()
            self.policy_related_resources = temp_model.from_map(m.get('PolicyRelatedResources'))

        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')

        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')

        if m.get('Watermark') is not None:
            temp_model = main_models.ListPolicyGroupsResponseBodyPolicyGroupModelWatermark()
            self.watermark = temp_model.from_map(m.get('Watermark'))

        return self

class ListPolicyGroupsResponseBodyPolicyGroupModelWatermark(DaraModel):
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

class ListPolicyGroupsResponseBodyPolicyGroupModelPolicyRelatedResources(DaraModel):
    def __init__(
        self,
        android_instance_group_ids: List[str] = None,
        cloud_phone_matrix_ids: List[str] = None,
    ):
        self.android_instance_group_ids = android_instance_group_ids
        self.cloud_phone_matrix_ids = cloud_phone_matrix_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_group_ids is not None:
            result['AndroidInstanceGroupIds'] = self.android_instance_group_ids

        if self.cloud_phone_matrix_ids is not None:
            result['CloudPhoneMatrixIds'] = self.cloud_phone_matrix_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceGroupIds') is not None:
            self.android_instance_group_ids = m.get('AndroidInstanceGroupIds')

        if m.get('CloudPhoneMatrixIds') is not None:
            self.cloud_phone_matrix_ids = m.get('CloudPhoneMatrixIds')

        return self

class ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicy(DaraModel):
    def __init__(
        self,
        custom_proxy: str = None,
        host_addr: str = None,
        net_redirect: str = None,
        port: str = None,
        proxy_password: str = None,
        proxy_type: str = None,
        proxy_user_name: str = None,
        rules: List[main_models.ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicyRules] = None,
    ):
        # Indicates whether a custom proxy is manually configured.
        # 
        # Valid values:
        # 
        # *   off
        # *   on
        self.custom_proxy = custom_proxy
        # The IPv4 address of the custom proxy.
        self.host_addr = host_addr
        # Indicates whether the network redirection feature is enabled. When this feature is enabled, network traffic is automatically redirected to the on-premises network by default.
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
        # The proxy rules.
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
                temp_model = main_models.ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ListPolicyGroupsResponseBodyPolicyGroupModelNetRedirectPolicyRules(DaraModel):
    def __init__(
        self,
        rule_type: str = None,
        target: str = None,
    ):
        # The type of the rule.
        # 
        # Valid values:
        # 
        # *   prc: an application package name.
        # *   domain: a domain name.
        self.rule_type = rule_type
        # The name of the application package or domain name.
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

