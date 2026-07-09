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
        # The pagination token that indicates the position up to which data has been read in the current call. An empty value indicates that all data has been read.
        self.next_token = next_token
        # The policy information.
        self.policy_group_model = policy_group_model
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
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
        access_policies: List[main_models.ListPolicyGroupsResponseBodyPolicyGroupModelAccessPolicies] = None,
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
        self.access_policies = access_policies
        # Indicates whether local camera redirection is enabled.
        self.camera_redirect = camera_redirect
        # The clipboard permission.
        self.clipboard = clipboard
        # The creation time.
        self.gmt_create = gmt_create
        # The file transfer policy for the HTML5 client.
        self.html_5file_transfer = html_5file_transfer
        # The local disk mapping permission.
        self.local_drive = local_drive
        # The locked resolution.
        self.lock_resolution = lock_resolution
        # The network redirection settings.
        self.net_redirect_policy = net_redirect_policy
        # The policy ID.
        self.policy_group_id = policy_group_id
        # The policy name.
        self.policy_group_name = policy_group_name
        # The resources associated with the policy.
        self.policy_related_resources = policy_related_resources
        # The height of the resolution.
        self.session_resolution_height = session_resolution_height
        # The width of the resolution.
        self.session_resolution_width = session_resolution_width
        # The screen watermark settings.
        self.watermark = watermark

    def validate(self):
        if self.access_policies:
            for v1 in self.access_policies:
                 if v1:
                    v1.validate()
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
        result['AccessPolicies'] = []
        if self.access_policies is not None:
            for k1 in self.access_policies:
                result['AccessPolicies'].append(k1.to_map() if k1 else None)

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
        self.access_policies = []
        if m.get('AccessPolicies') is not None:
            for k1 in m.get('AccessPolicies'):
                temp_model = main_models.ListPolicyGroupsResponseBodyPolicyGroupModelAccessPolicies()
                self.access_policies.append(temp_model.from_map(k1))

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
        # The watermark font color. Valid values: 0 to 16777215.
        self.watermark_color = watermark_color
        # The custom watermark content. The value can be up to 10 characters in length and does not support emoji characters.
        self.watermark_custom_text = watermark_custom_text
        # The watermark font size. Valid values: 10 to 20.
        self.watermark_font_size = watermark_font_size
        # The screen watermark switch.
        self.watermark_switch = watermark_switch
        # The watermark opacity. A larger value indicates lower transparency. Valid values: 10 to 100.
        self.watermark_transparency_value = watermark_transparency_value
        # The screen watermark content.
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
        # The list of instance group IDs.
        self.android_instance_group_ids = android_instance_group_ids
        # The list of matrix IDs.
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
        # Indicates whether a transparent proxy is manually configured.
        self.custom_proxy = custom_proxy
        # The proxy IP address of the transparent proxy. The value must be in IPv4 format.
        self.host_addr = host_addr
        # Indicates whether network redirection is enabled. After this feature is enabled, traffic is redirected to the client-side network by default.
        self.net_redirect = net_redirect
        # The port of the transparent proxy. Valid values: 1 to 65535.
        self.port = port
        # The proxy password. The value must be 1 to 256 characters in length and cannot contain Chinese characters or whitespace characters.
        self.proxy_password = proxy_password
        # The proxy protocol type.
        self.proxy_type = proxy_type
        # The proxy username. The value must be 1 to 256 characters in length and cannot contain Chinese characters or whitespace characters.
        self.proxy_user_name = proxy_user_name
        # The list of proxy rules.
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
        # The rule type.
        self.rule_type = rule_type
        # The application package name or domain name.
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

class ListPolicyGroupsResponseBodyPolicyGroupModelAccessPolicies(DaraModel):
    def __init__(
        self,
        access_policy_rule_id: int = None,
        cidr_ip: str = None,
        description: str = None,
        policy: str = None,
        priority: int = None,
    ):
        self.access_policy_rule_id = access_policy_rule_id
        self.cidr_ip = cidr_ip
        self.description = description
        self.policy = policy
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_policy_rule_id is not None:
            result['AccessPolicyRuleId'] = self.access_policy_rule_id

        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip

        if self.description is not None:
            result['Description'] = self.description

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPolicyRuleId') is not None:
            self.access_policy_rule_id = m.get('AccessPolicyRuleId')

        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

