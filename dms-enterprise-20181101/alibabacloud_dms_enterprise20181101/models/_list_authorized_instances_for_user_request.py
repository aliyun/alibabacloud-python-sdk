# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAuthorizedInstancesForUserRequest(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        env_type: str = None,
        page_number: str = None,
        page_size: str = None,
        search_key: str = None,
        tid: int = None,
        user_id: str = None,
    ):
        # The type of databases. Valid values:
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
        # The type of the environment in which the database instance is deployed. Valid values:
        # 
        # *   **product**: production environment.
        # *   **dev**: development environment.
        # *   **pre**: pre-release environment.
        # *   **test**: test environment.
        # *   **sit**: system integration testing (SIT) environment.
        # *   **uat**: user acceptance testing (UAT) environment.
        # *   **pet**: stress testing environment.
        # *   **stag**: staging environment.
        self.env_type = env_type
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The search keyword.
        self.search_key = search_key
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the DMS console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
        # The ID of the user. You can call the [GetUser](https://help.aliyun.com/document_detail/465816.html) operation to query the user ID.
        # 
        # > If IdentityType is set to USER, this parameter is required.
        # 
        # This parameter is required.
        self.user_id = user_id

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

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

