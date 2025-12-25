# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class AddAuthorityTemplateItemsRequest(DaraModel):
    def __init__(
        self,
        items: List[main_models.AddAuthorityTemplateItemsRequestItems] = None,
        template_id: int = None,
        tid: int = None,
    ):
        # The resources that you want to add to the permission template.
        # 
        # This parameter is required.
        self.items = items
        # The ID of the permission template. You can call the [CreateAuthorityTemplate](https://help.aliyun.com/document_detail/600705.html) operation to obtain the value of this parameter.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The ID of the tenant.
        # 
        # > To view the tenant ID, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.AddAuthorityTemplateItemsRequestItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self



class AddAuthorityTemplateItemsRequestItems(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        instance_id: int = None,
        permission_types: List[str] = None,
        resource_type: str = None,
        table_name: str = None,
    ):
        # The database ID. Databases are divided into physical databases and logical databases.
        # 
        # *   To query the ID of a physical database, call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        # *   To query the ID of a logical database, call the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        # 
        # > This parameter is required if the ResourceType parameter is set to META_DB, LOGIC_DB, META_TABLE, or LOGIC_TABLE.
        self.db_id = db_id
        # The instance ID. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the instance ID.
        # 
        # > This parameter is required if the ResourceType parameter is set to INSTANCE.
        self.instance_id = instance_id
        # The permission types.
        self.permission_types = permission_types
        # The type of the resource from which you want to remove tags. Valid values:
        # 
        # *   **INSTANCE**: instance
        # *   **LOGIC_DB**: logical database
        # *   **META_DB**: physical database
        # *   **LOGIC_TABLE**: logical table
        # *   **LOGIC_TABLE**: physical table
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The table name. You can call the [ListTables](https://help.aliyun.com/document_detail/141878.html) operation to query the name of the table.
        # 
        # > This parameter is required if the ResourceType parameter is set to META_TABLE or LOGIC_TABLE.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.permission_types is not None:
            result['PermissionTypes'] = self.permission_types

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PermissionTypes') is not None:
            self.permission_types = m.get('PermissionTypes')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

