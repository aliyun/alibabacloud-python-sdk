# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAuditSecurityIpRequest(DaraModel):
    def __init__(
        self,
        ips: str = None,
        operate_mode: str = None,
        security_group_name: str = None,
    ):
        # The list of security IP addresses for review. Each group supports a maximum of 100 IP addresses. Separate multiple IP addresses with commas (,). The following formats are supported:
        # 
        # - Exact IP address: 192.168.0.1
        # - CIDR block: 192.168.0.1/24 (Classless Inter-Domain Routing. /24 specifies the length of the prefix in the address. Valid values: `[1,32]`.)
        # 
        # This parameter is required.
        self.ips = ips
        # The operation mode. Valid values:
        # 
        # - **Append**: default value. Appends IP addresses to the IP address whitelist.
        # - **Cover**: overwrites the existing IP address whitelist.
        # - **Delete**: deletes IP addresses from the IP address whitelist.
        # > If the specified value is not within the valid values, the default value (Append) is used.
        self.operate_mode = operate_mode
        # The name of the security group for review. Default value: **Default**. A maximum of 10 security groups are supported.
        self.security_group_name = security_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ips is not None:
            result['Ips'] = self.ips

        if self.operate_mode is not None:
            result['OperateMode'] = self.operate_mode

        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        if m.get('OperateMode') is not None:
            self.operate_mode = m.get('OperateMode')

        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')

        return self

