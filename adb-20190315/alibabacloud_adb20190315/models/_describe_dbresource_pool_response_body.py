# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeDBResourcePoolResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        pools_info: List[main_models.DescribeDBResourcePoolResponseBodyPoolsInfo] = None,
        request_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # Details of the resource group.
        self.pools_info = pools_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.pools_info:
            for v1 in self.pools_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['PoolsInfo'] = []
        if self.pools_info is not None:
            for k1 in self.pools_info:
                result['PoolsInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.pools_info = []
        if m.get('PoolsInfo') is not None:
            for k1 in m.get('PoolsInfo'):
                temp_model = main_models.DescribeDBResourcePoolResponseBodyPoolsInfo()
                self.pools_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBResourcePoolResponseBodyPoolsInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        node_num: int = None,
        pool_name: str = None,
        pool_users: str = None,
        query_type: str = None,
        update_time: str = None,
    ):
        # The time when the resource group was created.
        self.create_time = create_time
        # The number of nodes.
        # 
        # >  Each node consumes 16 cores and 64 GB memory.
        self.node_num = node_num
        # The name of the resource group.
        self.pool_name = pool_name
        # The database accounts that are associated with the resource group.
        self.pool_users = pool_users
        # The mode in which SQL statements are executed.
        # 
        # *   **batch**
        # *   **interactive**
        # 
        # >  For more information, see [Query execution modes](https://help.aliyun.com/document_detail/189502.html).
        self.query_type = query_type
        # The time when the resource group was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        if self.pool_name is not None:
            result['PoolName'] = self.pool_name

        if self.pool_users is not None:
            result['PoolUsers'] = self.pool_users

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')

        if m.get('PoolUsers') is not None:
            self.pool_users = m.get('PoolUsers')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

