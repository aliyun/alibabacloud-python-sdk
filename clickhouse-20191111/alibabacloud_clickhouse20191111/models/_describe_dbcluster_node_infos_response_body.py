# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterNodeInfosResponseBody(DaraModel):
    def __init__(
        self,
        node_infos: List[main_models.DescribeDBClusterNodeInfosResponseBodyNodeInfos] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_node_count: int = None,
        zk_node_infos: List[main_models.DescribeDBClusterNodeInfosResponseBodyZkNodeInfos] = None,
    ):
        self.node_infos = node_infos
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_node_count = total_node_count
        self.zk_node_infos = zk_node_infos

    def validate(self):
        if self.node_infos:
            for v1 in self.node_infos:
                 if v1:
                    v1.validate()
        if self.zk_node_infos:
            for v1 in self.zk_node_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeInfos'] = []
        if self.node_infos is not None:
            for k1 in self.node_infos:
                result['NodeInfos'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_node_count is not None:
            result['TotalNodeCount'] = self.total_node_count

        result['ZkNodeInfos'] = []
        if self.zk_node_infos is not None:
            for k1 in self.zk_node_infos:
                result['ZkNodeInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_infos = []
        if m.get('NodeInfos') is not None:
            for k1 in m.get('NodeInfos'):
                temp_model = main_models.DescribeDBClusterNodeInfosResponseBodyNodeInfos()
                self.node_infos.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNodeCount') is not None:
            self.total_node_count = m.get('TotalNodeCount')

        self.zk_node_infos = []
        if m.get('ZkNodeInfos') is not None:
            for k1 in m.get('ZkNodeInfos'):
                temp_model = main_models.DescribeDBClusterNodeInfosResponseBodyZkNodeInfos()
                self.zk_node_infos.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterNodeInfosResponseBodyZkNodeInfos(DaraModel):
    def __init__(
        self,
        failover_testing: bool = None,
        node_name: str = None,
        replica_id: str = None,
    ):
        self.failover_testing = failover_testing
        self.node_name = node_name
        self.replica_id = replica_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failover_testing is not None:
            result['FailoverTesting'] = self.failover_testing

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.replica_id is not None:
            result['ReplicaId'] = self.replica_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailoverTesting') is not None:
            self.failover_testing = m.get('FailoverTesting')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('ReplicaId') is not None:
            self.replica_id = m.get('ReplicaId')

        return self

class DescribeDBClusterNodeInfosResponseBodyNodeInfos(DaraModel):
    def __init__(
        self,
        failover_testing: bool = None,
        node_ip: str = None,
        node_name: str = None,
        replica_id: str = None,
        shard_id: str = None,
    ):
        self.failover_testing = failover_testing
        self.node_ip = node_ip
        self.node_name = node_name
        self.replica_id = replica_id
        self.shard_id = shard_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failover_testing is not None:
            result['FailoverTesting'] = self.failover_testing

        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.replica_id is not None:
            result['ReplicaId'] = self.replica_id

        if self.shard_id is not None:
            result['ShardId'] = self.shard_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailoverTesting') is not None:
            self.failover_testing = m.get('FailoverTesting')

        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('ReplicaId') is not None:
            self.replica_id = m.get('ReplicaId')

        if m.get('ShardId') is not None:
            self.shard_id = m.get('ShardId')

        return self

