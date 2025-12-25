# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateLogicDatabaseRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        database_ids: List[int] = None,
        tid: int = None,
    ):
        # The alias of the logical database.
        # 
        # This parameter is required.
        self.alias = alias
        # The IDs of the physical databases that compose the logical database. You can specify one or more database IDs. You can call the [ListDatabases](https://www.alibabacloud.com/help/en/data-management-service/latest/listdatabases) or [SearchDatabase](https://www.alibabacloud.com/help/en/data-management-service/latest/searchdatabase) operation to query the IDs of the physical databases.
        # 
        # This parameter is required.
        self.database_ids = database_ids
        # The ID of the tenant. 
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://www.alibabacloud.com/help/en/data-management-service/latest/manage-dms-tenants) topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

