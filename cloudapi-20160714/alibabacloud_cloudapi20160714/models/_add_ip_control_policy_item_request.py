# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddIpControlPolicyItemRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cidr_ip: str = None,
        ip_control_id: str = None,
        security_token: str = None,
    ):
        # The restriction policy on app IDs for a specific policy. You can restrict app IDs only for whitelists. The IpControlType values of whitelists are ALLOW.
        # 
        # *   You can add only one app ID restriction policy at a time.
        # *   If this parameter is empty, no restriction is imposed on the app IDs.
        # *   If this parameter is not empty, there is restriction not only on IP addresses, but also on apps.
        # *   Please note that if this parameter is not empty and the security authentication method of the API is No Authentication, all API calls are restricted.
        # *   If this parameter is not empty for a blacklist, API Gateway automatically skips this parameter and sets only restriction on IP addresses. The IpControlType value of a blacklist is REFUSE.
        self.app_id = app_id
        # The IP addresses or CIDR blocks involved in the policy. Separate multiple IP addresses or CIDR blocks with semicolons (;). You can specify a maximum of 10 IP addresses or CIDR blocks.
        # 
        # This parameter is required.
        self.cidr_ip = cidr_ip
        # The ID of the ACL. The ID is unique.
        # 
        # This parameter is required.
        self.ip_control_id = ip_control_id
        # The security token included in the WebSocket request header. The system uses this token to authenticate the request.
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

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

