# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBInstanceIPArrayShrinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        iparray_attribute: str = None,
        iparray_name: str = None,
        security_iplist_shrink: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The attribute of the IP whitelist group.
        self.iparray_attribute = iparray_attribute
        # The name of the IP whitelist group.
        # 
        # This parameter is required.
        self.iparray_name = iparray_name
        # The IP addresses in the IP whitelist group. A maximum of 1,000 IP addresses or CIDR blocks are allowed.
        # 
        # This parameter is required.
        self.security_iplist_shrink = security_iplist_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.iparray_attribute is not None:
            result['IPArrayAttribute'] = self.iparray_attribute

        if self.iparray_name is not None:
            result['IPArrayName'] = self.iparray_name

        if self.security_iplist_shrink is not None:
            result['SecurityIPList'] = self.security_iplist_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IPArrayAttribute') is not None:
            self.iparray_attribute = m.get('IPArrayAttribute')

        if m.get('IPArrayName') is not None:
            self.iparray_name = m.get('IPArrayName')

        if m.get('SecurityIPList') is not None:
            self.security_iplist_shrink = m.get('SecurityIPList')

        return self

