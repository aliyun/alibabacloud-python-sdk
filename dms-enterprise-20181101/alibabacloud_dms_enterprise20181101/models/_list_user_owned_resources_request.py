# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserOwnedResourcesRequest(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_type: str = None,
        page_number: int = None,
        page_size: int = None,
        tid: int = None,
        user_id: str = None,
    ):
        # The database name.
        self.database_name = database_name
        # The type of the database instance. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
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
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true.**: The database is a logical database
        # *   **false**: The database is a physical database.
        self.logic = logic
        # The type of the owner. Valid values:
        # 
        # *   INSTANCE: an owner of an instance.
        # *   DATABASE: an owner of a physical database.
        # *   TABLE: an owner of a physical table.
        # 
        # This parameter is required.
        self.owner_type = owner_type
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
        # The ID of the user.
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
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

