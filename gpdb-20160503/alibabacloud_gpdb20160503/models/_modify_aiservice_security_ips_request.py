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
        # The ID of the instance.
        # 
        # > To view details of all instances in a destination region, including their IDs, call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # A comma-separated list of IP addresses or CIDR blocks in the IP address whitelist group. You can specify up to 1000 entries. To block all external IP addresses, set this parameter to 127.0.0.1. Valid formats include the following:
        # 
        # - 10.23.12.24 (an IPv4 address)
        # 
        # - 10.23.12.24/24 (a CIDR block. The number after the slash indicates the prefix length and must be between 1 and 32.)
        # 
        # This parameter is required.
        self.security_iplist = security_iplist
        # The ID of the service.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service type. Only drama is supported.
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

