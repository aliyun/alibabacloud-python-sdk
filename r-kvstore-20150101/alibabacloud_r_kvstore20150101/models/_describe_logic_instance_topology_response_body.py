# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeLogicInstanceTopologyResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        redis_proxy_list: main_models.DescribeLogicInstanceTopologyResponseBodyRedisProxyList = None,
        redis_shard_list: main_models.DescribeLogicInstanceTopologyResponseBodyRedisShardList = None,
        request_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        self.redis_proxy_list = redis_proxy_list
        self.redis_shard_list = redis_shard_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.redis_proxy_list:
            self.redis_proxy_list.validate()
        if self.redis_shard_list:
            self.redis_shard_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.redis_proxy_list is not None:
            result['RedisProxyList'] = self.redis_proxy_list.to_map()

        if self.redis_shard_list is not None:
            result['RedisShardList'] = self.redis_shard_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RedisProxyList') is not None:
            temp_model = main_models.DescribeLogicInstanceTopologyResponseBodyRedisProxyList()
            self.redis_proxy_list = temp_model.from_map(m.get('RedisProxyList'))

        if m.get('RedisShardList') is not None:
            temp_model = main_models.DescribeLogicInstanceTopologyResponseBodyRedisShardList()
            self.redis_shard_list = temp_model.from_map(m.get('RedisShardList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLogicInstanceTopologyResponseBodyRedisShardList(DaraModel):
    def __init__(
        self,
        node_info: List[main_models.DescribeLogicInstanceTopologyResponseBodyRedisShardListNodeInfo] = None,
    ):
        self.node_info = node_info

    def validate(self):
        if self.node_info:
            for v1 in self.node_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k1 in self.node_info:
                result['NodeInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k1 in m.get('NodeInfo'):
                temp_model = main_models.DescribeLogicInstanceTopologyResponseBodyRedisShardListNodeInfo()
                self.node_info.append(temp_model.from_map(k1))

        return self

class DescribeLogicInstanceTopologyResponseBodyRedisShardListNodeInfo(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        capacity: str = None,
        connection: str = None,
        node_id: str = None,
        node_type: str = None,
        sub_instance_type: str = None,
    ):
        self.bandwidth = bandwidth
        self.capacity = capacity
        self.connection = connection
        self.node_id = node_id
        self.node_type = node_type
        self.sub_instance_type = sub_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.connection is not None:
            result['Connection'] = self.connection

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.sub_instance_type is not None:
            result['SubInstanceType'] = self.sub_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Connection') is not None:
            self.connection = m.get('Connection')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('SubInstanceType') is not None:
            self.sub_instance_type = m.get('SubInstanceType')

        return self

class DescribeLogicInstanceTopologyResponseBodyRedisProxyList(DaraModel):
    def __init__(
        self,
        node_info: List[main_models.DescribeLogicInstanceTopologyResponseBodyRedisProxyListNodeInfo] = None,
    ):
        self.node_info = node_info

    def validate(self):
        if self.node_info:
            for v1 in self.node_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeInfo'] = []
        if self.node_info is not None:
            for k1 in self.node_info:
                result['NodeInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_info = []
        if m.get('NodeInfo') is not None:
            for k1 in m.get('NodeInfo'):
                temp_model = main_models.DescribeLogicInstanceTopologyResponseBodyRedisProxyListNodeInfo()
                self.node_info.append(temp_model.from_map(k1))

        return self

class DescribeLogicInstanceTopologyResponseBodyRedisProxyListNodeInfo(DaraModel):
    def __init__(
        self,
        bandwidth: str = None,
        capacity: str = None,
        connection: str = None,
        node_id: str = None,
        node_type: str = None,
    ):
        self.bandwidth = bandwidth
        self.capacity = capacity
        self.connection = connection
        self.node_id = node_id
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.connection is not None:
            result['Connection'] = self.connection

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Connection') is not None:
            self.connection = m.get('Connection')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        return self

