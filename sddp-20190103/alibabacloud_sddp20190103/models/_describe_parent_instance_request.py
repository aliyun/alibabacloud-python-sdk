# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeParentInstanceRequest(DaraModel):
    def __init__(
        self,
        auth_status: int = None,
        check_status: int = None,
        cluster_status: str = None,
        current_page: int = None,
        db_name: str = None,
        engine_type: str = None,
        instance_id: str = None,
        lang: str = None,
        member_account: int = None,
        page_size: int = None,
        resource_type: int = None,
        service_region_id: str = None,
    ):
        # Authorization status of the data asset instance.
        # - **0**: Unauthorized
        # - **1**: Authorized
        self.auth_status = auth_status
        # Connection status of the instance or the database under the instance. Values:
        # - **-3**: Database not created
        # - **-2**: Released
        # - **-1**: Not connected
        # - **2**: Connectivity test in progress
        # - **3**: Connected
        # - **4**: Connection failed
        self.check_status = check_status
        # Instance status.
        # - **Running**: Running
        # - **Released**: Released
        # - **DatabaseNotCreated**: Database not created
        self.cluster_status = cluster_status
        # When performing a paginated query, set the current page number. Default value: **1**.
        self.current_page = current_page
        # Database name.
        self.db_name = db_name
        # Engine type. Values:
        # - **MySQL**
        # - **MariaDB**
        # - **Oracle**
        # - **PostgreSQL**
        # - **SQLServer**
        self.engine_type = engine_type
        # The instance ID to which the data in the data asset table belongs.
        self.instance_id = instance_id
        # Language type for request and response messages. Values:
        # - **zh_cn**: Default, Simplified Chinese
        # - **en_us**: English (US)
        self.lang = lang
        # Member account ID.
        self.member_account = member_account
        # When performing a paginated query, set the number of rows per page. Default value: 10.
        self.page_size = page_size
        # The product type. Valid values:
        # - **1**: MaxCompute
        # - **2**: OSS
        # - **3**: ADB-MYSQL
        # - **4**: TableStore
        # - **5**: RDS
        # - **6**: SelfDB
        # - **7**: PolarDB-X
        # - **8**: PolarDB
        # - **9**: ADB-PG
        # - **10**: OceanBase
        # - **11**: MongoDB
        # - **25**: Redis
        self.resource_type = resource_type
        # The region where the asset is located. Values:
        # - **cn-beijing**: China (Beijing)
        # - **cn-zhangjiakou**: China (Zhangjiakou)
        # - **cn-huhehaote**: China (Hohhot)
        # - **cn-hangzhou**: China (Hangzhou)
        # - **cn-shanghai**: China (Shanghai)
        # - **cn-shenzhen**: China (Shenzhen)
        # - **cn-hongkong**:  China (Hong Kong)
        self.service_region_id = service_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_status is not None:
            result['AuthStatus'] = self.auth_status

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthStatus') is not None:
            self.auth_status = m.get('AuthStatus')

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        return self

