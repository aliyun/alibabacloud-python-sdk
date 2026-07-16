# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperationDatabasesRequest(DaraModel):
    def __init__(
        self,
        database_address: str = None,
        database_name: str = None,
        database_type: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_state: str = None,
    ):
        # The address of the database.
        self.database_address = database_address
        # The name of the database. This parameter supports only exact matches.
        self.database_name = database_name
        # The database type. Valid values:
        # 
        # - **MySQL**
        # 
        # - **SQLServer**
        # 
        # - **Oracle**
        # 
        # - **PostgreSQL**
        self.database_type = database_type
        # The ID of the Bastionhost instance.
        # 
        # > Call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. The default value is **1**.
        self.page_number = page_number
        # The number of entries to return on each page.<br>The maximum value is 100. The default value is 20. If you do not specify this parameter, 20 entries are returned.<br>
        # 
        # > Specify a value for this parameter.
        self.page_size = page_size
        # The region ID of the Bastionhost instance.
        # 
        # > For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The source of the database. Valid values:
        # 
        # - **Local**: a local database
        # 
        # - **Rds**: an ApsaraDB RDS database
        # 
        # - **PolarDB**: a PolarDB database
        self.source = source
        # The ID of the source instance. This parameter supports only exact matches.
        self.source_instance_id = source_instance_id
        # The status of the source instance. You can use this parameter to filter the results.
        # 
        # - **Normal**: The instance is running.
        # 
        # - **RemoteRelease**: The instance is released.
        self.source_instance_state = source_instance_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_address is not None:
            result['DatabaseAddress'] = self.database_address

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source is not None:
            result['Source'] = self.source

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseAddress') is not None:
            self.database_address = m.get('DatabaseAddress')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')

        return self

