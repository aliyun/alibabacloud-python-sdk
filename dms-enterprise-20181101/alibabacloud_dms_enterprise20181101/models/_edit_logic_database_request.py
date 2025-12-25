# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EditLogicDatabaseRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        database_ids: List[int] = None,
        logic_db_id: int = None,
        tid: int = None,
    ):
        # - The alias of the logical database. If you want to change the alias, specify a new alias.
        # - If you do not need to change the alias of the logical database, call the [GetLogicDatabase](https://www.alibabacloud.com/help/en/data-management-service/latest/getlogicdatabase) or [GetDBTopology](https://www.alibabacloud.com/help/en/data-management-service/latest/getdbtopology) operation to query the alias of the logical database.
        # 
        # This parameter is required.
        self.alias = alias
        # - The IDs of the physical databases that compose the logical database. If you want to change the physical databases, you can call the [ListDatabases](https://www.alibabacloud.com/help/en/data-management-service/latest/listdatabases) or [SearchDatabase](https://www.alibabacloud.com/help/en/data-management-service/latest/searchdatabase) operation to query the IDs of the new physical databases that you want to specify.
        # - If you do not want to change the physical databases, you can call the [GetDBTopology](https://www.alibabacloud.com/help/en/data-management-service/latest/getdbtopology) operation to query the IDs of the physical databases that compose the logical database.
        # 
        # This parameter is required.
        self.database_ids = database_ids
        # The ID of the logical database. You can call the [ListLogicDatabases](https://www.alibabacloud.com/help/en/data-management-service/latest/listlogicdatabases) operation to query the ID of the logical database.
        # 
        # This parameter is required.
        self.logic_db_id = logic_db_id
        # The ID of the tenant. 
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://www.alibabacloud.com/help/en/data-management-service/latest/manage-dms-tenants) topic.
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

        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')

        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

