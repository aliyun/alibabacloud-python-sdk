# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeParentInstanceResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeParentInstanceResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # When performing a paginated query, set the current page number. Default value: **1**.
        self.current_page = current_page
        # The assets.
        self.items = items
        # When performing a paginated query, set the maximum number of data asset instances displayed per page. Default value: **10**.
        self.page_size = page_size
        # Request ID of the result.
        self.request_id = request_id
        # Total number of data items in the result.
        self.total_count = total_count

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeParentInstanceResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeParentInstanceResponseBodyItems(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        auth_status: int = None,
        auth_time: int = None,
        cluster_status: str = None,
        connect_node: str = None,
        db_num: str = None,
        engine_type: str = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_size: int = None,
        local_name: str = None,
        member_account: int = None,
        parent_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        support_connect_nodes: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        un_connect_db_count: str = None,
        un_support_one_click_auth_reason: str = None,
    ):
        # Audit authorization status. The values are as follows:
        # - **1**: Authorized
        # - **0**: Unauthorized
        self.audit_status = audit_status
        # Authorization status of the data asset instance.
        # - **0**: Unauthorized
        # - **1**: Authorized
        self.auth_status = auth_status
        # Instance authorization time, in milliseconds.
        self.auth_time = auth_time
        # Instance status.
        self.cluster_status = cluster_status
        # Connection node type, valid only for MongoDB assets.
        self.connect_node = connect_node
        # Number of databases under the instance.
        self.db_num = db_num
        # The engine type. Valid values:
        # - **MySQL**
        # - **MariaDB**
        # - **Oracle**
        # - **PostgreSQL**
        # - **SQLServer**
        self.engine_type = engine_type
        # Description of the instance.
        self.instance_description = instance_description
        # Instance ID.
        self.instance_id = instance_id
        # Instance space size, valid only for OSS assets. Unit: bytes.
        self.instance_size = instance_size
        # Region name. The values are as follows:
        # 
        # - **China (Hangzhou)**
        # - **China (Shanghai)**
        # - **China (Beijing)**
        # - **China (Zhangjiakou)**
        # - **China (Shenzhen)**
        # - **China (Guangzhou)**
        # - **China (Hong Kong)**
        # - **Singapore**
        # - **US (Silicon Valley)**
        self.local_name = local_name
        # Member account ID.
        self.member_account = member_account
        # Identifier for the authorized asset. For structured data, it is identified by `instanceID.databaseName`.
        self.parent_id = parent_id
        # The region in which the asset resides.
        self.region_id = region_id
        # Asset type name. The values are as follows:
        # - **MaxCompute**
        # - **OSS**
        # - **ADB-MYSQL**
        # - **TableStore**
        # - **RDS**
        # - **SelfDB**
        # - **PolarDB-X**
        # - **PolarDB**
        # - **ADB-PG**
        # - **OceanBase**
        # - **MongoDB**
        # - **Redis**
        self.resource_type = resource_type
        # Supported connection nodes, separated by commas.
        self.support_connect_nodes = support_connect_nodes
        # Tenant ID, valid only for OceanBase assets.
        self.tenant_id = tenant_id
        # Tenant name, valid only for OceanBase assets.
        self.tenant_name = tenant_name
        # Number of unconnected databases under the instance.
        self.un_connect_db_count = un_connect_db_count
        # Reason for not supporting one-click authorization.
        self.un_support_one_click_auth_reason = un_support_one_click_auth_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time

        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status

        if self.connect_node is not None:
            result['ConnectNode'] = self.connect_node

        if self.db_num is not None:
            result['DbNum'] = self.db_num

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_size is not None:
            result['InstanceSize'] = self.instance_size

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.support_connect_nodes is not None:
            result['SupportConnectNodes'] = self.support_connect_nodes

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.un_connect_db_count is not None:
            result['UnConnectDbCount'] = self.un_connect_db_count

        if self.un_support_one_click_auth_reason is not None:
            result['UnSupportOneClickAuthReason'] = self.un_support_one_click_auth_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')

        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')

        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')

        if m.get('ConnectNode') is not None:
            self.connect_node = m.get('ConnectNode')

        if m.get('DbNum') is not None:
            self.db_num = m.get('DbNum')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSize') is not None:
            self.instance_size = m.get('InstanceSize')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SupportConnectNodes') is not None:
            self.support_connect_nodes = m.get('SupportConnectNodes')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('UnConnectDbCount') is not None:
            self.un_connect_db_count = m.get('UnConnectDbCount')

        if m.get('UnSupportOneClickAuthReason') is not None:
            self.un_support_one_click_auth_reason = m.get('UnSupportOneClickAuthReason')

        return self

