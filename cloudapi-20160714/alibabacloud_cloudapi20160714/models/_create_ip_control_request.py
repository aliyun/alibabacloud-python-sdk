# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class CreateIpControlRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        ip_control_name: str = None,
        ip_control_policys: List[main_models.CreateIpControlRequestIpControlPolicys] = None,
        ip_control_type: str = None,
        security_token: str = None,
    ):
        # The description. The description can be up to 200 characters in length.
        self.description = description
        # The name of the ACL. The name must be 4 to 50 characters in length, and can contain letters, digits, and underscores (_). The name cannot start with an underscore (_).``
        # 
        # This parameter is required.
        self.ip_control_name = ip_control_name
        # The information about the policies. The information is an array of ipcontrolpolicys data.
        self.ip_control_policys = ip_control_policys
        # The type of the ACL. Valid values:
        # 
        # *   **ALLOW**: an IP address whitelist
        # *   **REFUSE**: an IP address blacklist
        # 
        # This parameter is required.
        self.ip_control_type = ip_control_type
        self.security_token = security_token

    def validate(self):
        if self.ip_control_policys:
            for v1 in self.ip_control_policys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name

        result['IpControlPolicys'] = []
        if self.ip_control_policys is not None:
            for k1 in self.ip_control_policys:
                result['IpControlPolicys'].append(k1.to_map() if k1 else None)

        if self.ip_control_type is not None:
            result['IpControlType'] = self.ip_control_type

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')

        self.ip_control_policys = []
        if m.get('IpControlPolicys') is not None:
            for k1 in m.get('IpControlPolicys'):
                temp_model = main_models.CreateIpControlRequestIpControlPolicys()
                self.ip_control_policys.append(temp_model.from_map(k1))

        if m.get('IpControlType') is not None:
            self.ip_control_type = m.get('IpControlType')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

class CreateIpControlRequestIpControlPolicys(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cidr_ip: str = None,
    ):
        # The ID of the application that is restricted by the policy. You can configure the AppId parameter only when the value of the IpControlType parameter is ALLOW.
        # 
        # *   You can add only one application ID at a time.
        # *   If this parameter is empty, no applications are restricted.
        # *   If this parameter is not empty, not only IP addresses but also applications are restricted.
        # *   If this parameter is not empty and no security authentication method is specified for the API, all API calls are restricted.
        # *   If the value of the IpControlType parameter is REFUSE and the AppId parameter is not empty, API Gateway automatically ignores the AppId parameter and restricts only the IP addresses.
        # *   Valid values of N in IpControlPolicys.N: `[1,100]`.
        self.app_id = app_id
        # The IP address or CIDR block involved in a policy.
        # 
        # *   If you want to specify a policy when you create an ACL, this parameter is required.
        # *   The IP address or CIDR block that is defined in each policy. Separate multiple IP addresses or CIDR blocks with semicolons (;). You can add a maximum of 10 IP addresses or CIDR blocks.
        # *   Valid values of N in IpControlPolicys.N: `[1,100]`.
        self.cidr_ip = cidr_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')

        return self

