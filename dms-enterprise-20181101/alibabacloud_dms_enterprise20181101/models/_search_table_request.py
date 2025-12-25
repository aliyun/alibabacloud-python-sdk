# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchTableRequest(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        page_number: int = None,
        page_size: int = None,
        return_guid: bool = None,
        search_key: str = None,
        search_range: str = None,
        search_target: str = None,
        tid: int = None,
    ):
        # The type of database. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        # *   **PostgreSQL**
        # *   **Oracle**
        # *   **DRDS**
        # *   **OceanBase**
        # *   **Mongo**
        # *   **Redis**
        self.db_type = db_type
        # The type of the environment to which databases belong. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # Specifies whether to return the GUID of each table.
        self.return_guid = return_guid
        # The keyword that is used to query tables.
        self.search_key = search_key
        # The scope of tables that you want to query. Valid values:
        # 
        # *   **HAS_PERMSSION**: the tables on which the current account has permissions.
        # *   **OWNER**: the tables owned by the current account.
        # *   **MY_FOCUS**: the tables that the current account follows.
        # *   **UNKNOWN**: all tables.
        self.search_range = search_range
        # The type of table that you want to query. Valid values:
        # 
        # *   **TABLE**: physical and logical tables
        # *   **SINGLE_TABLE**: physical tables
        # *   **LOGIC_TABLE**: logical tables
        self.search_target = search_target
        # The ID of the tenant.
        # 
        # > To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.return_guid is not None:
            result['ReturnGuid'] = self.return_guid

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.search_range is not None:
            result['SearchRange'] = self.search_range

        if self.search_target is not None:
            result['SearchTarget'] = self.search_target

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReturnGuid') is not None:
            self.return_guid = m.get('ReturnGuid')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SearchRange') is not None:
            self.search_range = m.get('SearchRange')

        if m.get('SearchTarget') is not None:
            self.search_target = m.get('SearchTarget')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

