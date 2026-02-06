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
        # The IP addresses that you want to add to the review security group. You can add a maximum of 100 IP addresses to a review security group. Separate multiple IP addresses with commas (,). You can add IP addresses in the following formats to review security groups:
        # 
        # *   IP address: 192.168.0.1
        # *   CIDR block: 192.168.0.1/24. /24 indicates that the prefix of the CIDR block is 24 bits in length. You can replace 24 with a value that ranges `from 1 to 32`.
        # 
        # This parameter is required.
        self.ips = ips
        # The operation type. Valid values:
        # 
        # *   **Append** (default): adds the IP addresses to the original whitelist.
        # *   **Cover**: overwrites the original whitelist.
        # *   **Delete**: removes the IP addresses from the original whitelist.
        # 
        # >  If the value that you specify is invalid, the default value is used.
        self.operate_mode = operate_mode
        # The name of the review security group. Default value: **Default**. You can specify a maximum of 10 review security groups.
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

