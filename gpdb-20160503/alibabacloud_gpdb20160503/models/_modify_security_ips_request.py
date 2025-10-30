# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySecurityIpsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_iparray_attribute: str = None,
        dbinstance_iparray_name: str = None,
        dbinstance_id: str = None,
        modify_mode: str = None,
        resource_group_id: str = None,
        security_iplist: str = None,
    ):
        # The attribute of the IP address whitelist. By default, this parameter is empty. A whitelist with the `hidden` attribute does not appear in the console.
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute
        # The name of the whitelist. If you do not enter a name, IP addresses are added to the default whitelist.
        # 
        # >  You can create up to 50 whitelists for an instance.
        self.dbinstance_iparray_name = dbinstance_iparray_name
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The method of modification. Valid values:
        # 
        # *   **Cover**: overwrites the whitelist.
        # *   **Append**: appends data to the whitelist.
        # *   **Delete**: deletes the whitelist.
        self.modify_mode = modify_mode
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The IP addresses listed in the whitelist. You can add up to 1,000 IP addresses to the whitelist. Separate multiple IP addresses with commas (,). The IP addresses must use one of the following formats:
        # 
        # *   0.0.0.0/0
        # *   10.23.12.24. This is a standard IP address.
        # *   10.23.12.24/24. This is a CIDR block. The value `/24` indicates that the prefix of the CIDR block is 24-bit long. You can replace 24 with a value in the range of `1 to 32`.
        # 
        # This parameter is required.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute

        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')

        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

