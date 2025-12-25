# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDBTopologyRequest(DaraModel):
    def __init__(
        self,
        logic_db_id: int = None,
        tid: int = None,
    ):
        # The ID of the logical database. You can call the [ListLogicDatabases](https://www.alibabacloud.com/help/en/data-management-service/latest/listlogicdatabases) or [SearchDatabase](https://www.alibabacloud.com/help/en/data-management-service/latest/searchdatabase) operation to query the ID of the logical database.
        # 
        # This parameter is required.
        self.logic_db_id = logic_db_id
        # The ID of the tenant.
        # 
        # > To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

