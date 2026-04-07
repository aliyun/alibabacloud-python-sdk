# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListResourceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListResourceGroupsResponseBodyData] = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The resource groups.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListResourceGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListResourceGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_ext_key: str = None,
        cluster: str = None,
        create_time: str = None,
        enable_kp: bool = None,
        id: int = None,
        identifier: str = None,
        is_default: bool = None,
        mode: str = None,
        name: str = None,
        resource_group_type: str = None,
        resource_manager_resource_group_id: str = None,
        sequence: int = None,
        specs: Dict[str, Any] = None,
        status: int = None,
        tags: List[main_models.ListResourceGroupsResponseBodyDataTags] = None,
        tenant_id: int = None,
        update_time: str = None,
    ):
        # The category of the resource group. Valid values:
        # 
        # *   default: shared resource group
        # *   single: exclusive resource group
        self.biz_ext_key = biz_ext_key
        # The name of the cluster. This parameter is returned only if the type of the resource group is MaxCompute or PAI.
        self.cluster = cluster
        # The time when the cluster was created. Example: Jul 9, 2018 2:43:37 PM.
        self.create_time = create_time
        # Indicates whether the UID of an Alibaba Cloud account is used for access. Valid values:
        # 
        # *   true: The MaxCompute compute engine uses the UID of the Alibaba Cloud account as the display name of the account for access.
        # *   false: The MaxCompute compute engine uses the name of the Alibaba Cloud account as the display name of the account for access. The remaining values are useless. This parameter is returned only if the type of the resource group is MaxCompute.
        self.enable_kp = enable_kp
        # The resource group ID.
        self.id = id
        # The identifier of the resource group.
        self.identifier = identifier
        # Indicates whether the resource group is the default resource group. Valid values:
        # 
        # *   true: The resource group is the default resource group.
        # *   false: The resource group is not the default resource group.
        self.is_default = is_default
        # The mode of the resource group. Valid values:
        # 
        # *   ISOLATE: exclusive resource group that adopts the subscription billing method
        # *   SHARE: shared resource group that adopts the pay-as-you-go billing method
        # *   DEVELOP: resource group for developers
        self.mode = mode
        # The name of the resource group.
        self.name = name
        # The type of the resource group. Valid values:
        # 
        # *   0: DataWorks
        # *   2: MaxCompute
        # *   3: PAI
        # *   4: Data Integration
        # *   7: scheduling
        # *   9: DataService Studio
        self.resource_group_type = resource_group_type
        # The ID of your Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The sequence number of the resource group. Created resource groups are sorted in ascending order by sequence number.
        self.sequence = sequence
        # The details of the resource group. The content enclosed in braces {} is the details of the resource group.
        self.specs = specs
        # The status of the resource group. Valid values:
        # 
        # *   0: NORMAL, which indicates that the resource group is running or in service.
        # *   1: STOP, which indicates that the resource group has expired and is frozen.
        # *   2: DELETED, which indicates that the resource group is released or destroyed.
        # *   3: CREATING, which indicates that the resource group is being created or started.
        # *   4: CREATE_FAILED, which indicates that the resource group fails to be created or started.
        # *   5: UPDATING, which indicates that the resource group is being scaled out or upgraded.
        # *   6: UPDATE_FAILED, which indicates that the resource group fails to be scaled out or upgraded.
        # *   7: DELETING, which indicates that the resource group is being released or destroyed.
        # *   8: DELETE_FAILED, which indicates that the resource group fails to be released or destroyed.
        # *   9: TIMEOUT, which indicates that the operation performed on the resource group times out. All operations may time out. This value is temporarily available only for DataService Studio.
        self.status = status
        # The tags.
        self.tags = tags
        # The tenant ID.
        self.tenant_id = tenant_id
        # The time when the resource group was last updated.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_ext_key is not None:
            result['BizExtKey'] = self.biz_ext_key

        if self.cluster is not None:
            result['Cluster'] = self.cluster

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_kp is not None:
            result['EnableKp'] = self.enable_kp

        if self.id is not None:
            result['Id'] = self.id

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_group_type is not None:
            result['ResourceGroupType'] = self.resource_group_type

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.specs is not None:
            result['Specs'] = self.specs

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizExtKey') is not None:
            self.biz_ext_key = m.get('BizExtKey')

        if m.get('Cluster') is not None:
            self.cluster = m.get('Cluster')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableKp') is not None:
            self.enable_kp = m.get('EnableKp')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceGroupType') is not None:
            self.resource_group_type = m.get('ResourceGroupType')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('Specs') is not None:
            self.specs = m.get('Specs')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListResourceGroupsResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListResourceGroupsResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

