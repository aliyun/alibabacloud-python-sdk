# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseInstancePublicConnectionRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        current_connection_string: str = None,
        dbinstance_id: str = None,
    ):
        # The type of the endpoint. Default value: primary. Valid values:
        # 
        # *   **primary**: primary endpoint.
        # *   **cluster**: cluster endpoint. This type of endpoints can be created only for instances that have multiple coordinator nodes.
        self.address_type = address_type
        # The public endpoint of the instance.
        # 
        # You can log on to the AnalyticDB for PostgreSQL console and go to the **Basic Information** page of the instance to view the **public endpoint** in the **Database Connection** section.
        # 
        # This parameter is required.
        self.current_connection_string = current_connection_string
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

