# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIpControlPolicyItemRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cidr_ip: str = None,
        ip_control_id: str = None,
        policy_item_id: str = None,
        security_token: str = None,
    ):
        # The ID of the application that is restricted by the policy. You can configure the AppId parameter only when the value of the IpControlType parameter is ALLOW.
        # 
        # *   You can add only one application ID at a time.
        # *   If this parameter is empty, no applications are restricted.
        # *   If this parameter is not empty, not only IP addresses but also applications are restricted.
        # *   If this parameter is not empty and no security authentication method is specified for the API, all API calls are restricted.
        # *   If the value of the IpControlType parameter is REFUSE and the AppId parameter is not empty, API Gateway automatically ignores the AppId parameter and restricts only the IP addresses.
        self.app_id = app_id
        # The IP address or CIDR block that is defined in a policy. Separate multiple IP addresses or CIDR blocks with semicolons (;). You can add a maximum of 10 IP addresses or CIDR blocks.
        # 
        # This parameter is required.
        self.cidr_ip = cidr_ip
        # The ID of the ACL. The ID is unique.
        # 
        # This parameter is required.
        self.ip_control_id = ip_control_id
        # The ID of the policy.
        # 
        # This parameter is required.
        self.policy_item_id = policy_item_id
        self.security_token = security_token

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

        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id

        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')

        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')

        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

