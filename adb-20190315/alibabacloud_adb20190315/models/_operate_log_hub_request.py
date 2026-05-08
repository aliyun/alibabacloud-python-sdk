# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class OperateLogHubRequest(DaraModel):
    def __init__(
        self,
        create: bool = None,
        dbcluster_id: str = None,
        deliver_name: str = None,
        deliver_time: str = None,
        description: str = None,
        filter_dirty_data: bool = None,
        log_hub_stores: List[main_models.OperateLogHubRequestLogHubStores] = None,
        log_store_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        project_name: str = None,
        provider: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        schema_name: str = None,
        table_name: str = None,
        user_name: str = None,
    ):
        # Specifies whether to create the log shipping job.
        # 
        # This parameter is required.
        self.create = create
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the log shipping job.
        # 
        # This parameter is required.
        self.deliver_name = deliver_name
        # The shipping time.
        # 
        # This parameter is required.
        self.deliver_time = deliver_time
        # The description of the log shipping job.
        # 
        # This parameter is required.
        self.description = description
        # Specifies whether to filter dirty data.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.filter_dirty_data = filter_dirty_data
        # The log keywords.
        # 
        # This parameter is required.
        self.log_hub_stores = log_hub_stores
        # The name of the Logstore.
        # 
        # This parameter is required.
        self.log_store_name = log_store_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the database account.
        # 
        # This parameter is required.
        self.password = password
        # The name of the Simple Log Service project.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The channel of the log shipping job.
        self.provider = provider
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the database.
        # 
        # This parameter is required.
        self.schema_name = schema_name
        # The name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The name of the database account.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        if self.log_hub_stores:
            for v1 in self.log_hub_stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create is not None:
            result['Create'] = self.create

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.deliver_name is not None:
            result['DeliverName'] = self.deliver_name

        if self.deliver_time is not None:
            result['DeliverTime'] = self.deliver_time

        if self.description is not None:
            result['Description'] = self.description

        if self.filter_dirty_data is not None:
            result['FilterDirtyData'] = self.filter_dirty_data

        result['LogHubStores'] = []
        if self.log_hub_stores is not None:
            for k1 in self.log_hub_stores:
                result['LogHubStores'].append(k1.to_map() if k1 else None)

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Create') is not None:
            self.create = m.get('Create')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DeliverName') is not None:
            self.deliver_name = m.get('DeliverName')

        if m.get('DeliverTime') is not None:
            self.deliver_time = m.get('DeliverTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FilterDirtyData') is not None:
            self.filter_dirty_data = m.get('FilterDirtyData')

        self.log_hub_stores = []
        if m.get('LogHubStores') is not None:
            for k1 in m.get('LogHubStores'):
                temp_model = main_models.OperateLogHubRequestLogHubStores()
                self.log_hub_stores.append(temp_model.from_map(k1))

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class OperateLogHubRequestLogHubStores(DaraModel):
    def __init__(
        self,
        field_key: str = None,
        log_key: str = None,
    ):
        # The value of the log keyword.
        # 
        # This parameter is required.
        self.field_key = field_key
        # The log keyword.
        # 
        # This parameter is required.
        self.log_key = log_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_key is not None:
            result['FieldKey'] = self.field_key

        if self.log_key is not None:
            result['LogKey'] = self.log_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldKey') is not None:
            self.field_key = m.get('FieldKey')

        if m.get('LogKey') is not None:
            self.log_key = m.get('LogKey')

        return self

