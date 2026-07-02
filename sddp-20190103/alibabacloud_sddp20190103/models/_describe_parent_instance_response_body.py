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
        # The page number of the returned page. Default value: **1**.
        self.current_page = current_page
        # The list of queried data assets.
        self.items = items
        # The maximum number of data asset instances returned on each page. Default value: **10**.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
        # The audit authorization status. Valid values:
        # 
        # - **1**: Authorized.
        # 
        # - **0**: Unauthorized.
        self.audit_status = audit_status
        # The authorization status of the data asset instance.
        # 
        # - **0**: Unauthorized.
        # 
        # - **1**: Authorized.
        self.auth_status = auth_status
        # The time when the instance was authorized. Unit: milliseconds.
        self.auth_time = auth_time
        # The instance status.
        self.cluster_status = cluster_status
        # The type of the connection node. This parameter is valid only for MongoDB assets.
        self.connect_node = connect_node
        # The number of databases in the instance.
        self.db_num = db_num
        # The type of the database engine. Valid values:
        # 
        # - **MySQL**.
        # 
        # - **MariaDB**.
        # 
        # - **Oracle**.
        # 
        # - **PostgreSQL**.
        # 
        # - **SQLServer**.
        self.engine_type = engine_type
        # The description of the instance.
        self.instance_description = instance_description
        # The instance ID.
        self.instance_id = instance_id
        # The storage space of the instance. This parameter is valid only for OSS assets. Unit: bytes.
        self.instance_size = instance_size
        # The name of the region. The following list describes the valid values:
        # 
        # - **China (Hangzhou)**
        # 
        # - **China (Shanghai)**
        # 
        # - **China (Beijing)**
        # 
        # - **China (Zhangjiakou)**
        # 
        # - **China (Shenzhen)**
        # 
        # - **China (Guangzhou)**
        # 
        # - **China (Hong Kong)**
        # 
        # - **Singapore**
        # 
        # - **US (Silicon Valley)**
        self.local_name = local_name
        # The ID of the member account.
        self.member_account = member_account
        # The identifier of the authorized asset. If the asset is structured data, the identifier is in the format of \\`Instance ID.Database name\\`.
        self.parent_id = parent_id
        # The region where the asset resides.
        self.region_id = region_id
        # The name of the asset type. Valid values:
        # 
        # - **MaxCompute**
        # 
        # - **OSS**
        # 
        # - **ADB-MYSQL**
        # 
        # - **TableStore**
        # 
        # - **RDS**
        # 
        # - **SelfDB**
        # 
        # - **PolarDB-X**
        # 
        # - **PolarDB**
        # 
        # - **ADB-PG**
        # 
        # - **OceanBase**
        # 
        # - **MongoDB**
        # 
        # - **Redis**
        self.resource_type = resource_type
        # The supported connection nodes. Multiple nodes are separated by commas.
        self.support_connect_nodes = support_connect_nodes
        # The tenant ID. This parameter is valid only for OceanBase assets.
        self.tenant_id = tenant_id
        # The tenant name. This parameter is valid only for OceanBase assets.
        self.tenant_name = tenant_name
        # The number of unconnected databases in the instance.
        self.un_connect_db_count = un_connect_db_count
        # The reason why one-click authorization is not supported.
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

