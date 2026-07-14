# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAIServiceSecurityIpsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        security_iplist: str = None,
        service_id: str = None,
        type: str = None,
    ):
        # The instance ID.
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to query the details of all instances in a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The list of IP addresses in the IP address whitelist group. You can add up to 1,000 IP addresses, separated by commas (,). The value 127.0.0.1 indicates that no external IP addresses are allowed to access the instance. The following formats are supported:
        # - 10.23.12.24 (IP address)
        # - 10.23.12.24/24 (CIDR pattern, Classless Inter-Domain Routing. /24 specifies the prefix length, which ranges from 1 to 32.)
        # 
        # This parameter is required.
        self.security_iplist = security_iplist
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service type. Currently, only drama is supported.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

