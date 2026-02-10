# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUniBackupDatabaseRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        database_type: str = None,
        instance_name: str = None,
        page_size: int = None,
        query_type: str = None,
        uni_region_id: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The type of the database. Valid values:
        # 
        # *   **MYSQL**
        # *   **MSSQL**
        # *   **Oracle**
        self.database_type = database_type
        # The name of the Elastic Compute Service (ECS) instance.
        self.instance_name = instance_name
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The condition that is used to query the database. Valid values:
        # 
        # *   **create**: newly created
        # *   **restore**: restored
        self.query_type = query_type
        # The region ID of the server that hosts the database.
        self.uni_region_id = uni_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.uni_region_id is not None:
            result['UniRegionId'] = self.uni_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('UniRegionId') is not None:
            self.uni_region_id = m.get('UniRegionId')

        return self

