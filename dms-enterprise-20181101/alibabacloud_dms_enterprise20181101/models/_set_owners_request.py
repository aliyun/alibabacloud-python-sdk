# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetOwnersRequest(DaraModel):
    def __init__(
        self,
        owner_ids: str = None,
        owner_type: str = None,
        resource_id: str = None,
        tid: int = None,
    ):
        # The ID of the user whom you want to specify as an owner. Separate multiple IDs with commas (,). You can call the [GetUser](https://help.aliyun.com/document_detail/147098.html) or [ListUsers](https://help.aliyun.com/document_detail/141938.html) operation to query the ID of the user.
        # 
        # >  The value of the OwnerIds parameter is that of the UserId parameter.
        # 
        # This parameter is required.
        self.owner_ids = owner_ids
        # The type of the owner. Valid values:
        # 
        # *   INSTANCE: an owner of an instance.
        # *   DATABASE: an owner of a physical database.
        # *   LOGIC_DATABASE: an owner of a logical database.
        # *   TABLE: an owner of a physical table.
        # *   LOGIC_TABLE: an owner of a logical table.
        # 
        # This parameter is required.
        self.owner_type = owner_type
        # The ID of the resource. The ID of the resource varies with the owner type. The owner types and resource IDs have the following mappings:
        # 
        # *   INSTANCE: the ID of an instance. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) operation to query the ID of the instance.
        # *   DATABASE: the ID of a physical database. You can call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) operation to query the ID of the physical database.
        # *   LOGIC_DATABASE: the ID of a logical database. You can call the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) operation to query the ID of the logical database.
        # *   TABLE: the ID of a physical table. You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the ID of the physical table.
        # *   LOGIC_DATABASE: the ID of a logical table. You can call the [ListLogicTables](https://help.aliyun.com/document_detail/141875.html) operation to query the ID of the logical table.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

