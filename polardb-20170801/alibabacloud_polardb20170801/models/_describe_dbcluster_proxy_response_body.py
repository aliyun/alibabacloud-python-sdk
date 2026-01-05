# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterProxyResponseBody(DaraModel):
    def __init__(
        self,
        child_instances: List[main_models.DescribeDBClusterProxyResponseBodyChildInstances] = None,
        dbproxy_cluster_id: str = None,
        dbproxy_cluster_num: int = None,
        dbproxy_cluster_status: str = None,
        request_id: str = None,
    ):
        self.child_instances = child_instances
        self.dbproxy_cluster_id = dbproxy_cluster_id
        self.dbproxy_cluster_num = dbproxy_cluster_num
        self.dbproxy_cluster_status = dbproxy_cluster_status
        self.request_id = request_id

    def validate(self):
        if self.child_instances:
            for v1 in self.child_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChildInstances'] = []
        if self.child_instances is not None:
            for k1 in self.child_instances:
                result['ChildInstances'].append(k1.to_map() if k1 else None)

        if self.dbproxy_cluster_id is not None:
            result['DBProxyClusterId'] = self.dbproxy_cluster_id

        if self.dbproxy_cluster_num is not None:
            result['DBProxyClusterNum'] = self.dbproxy_cluster_num

        if self.dbproxy_cluster_status is not None:
            result['DBProxyClusterStatus'] = self.dbproxy_cluster_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_instances = []
        if m.get('ChildInstances') is not None:
            for k1 in m.get('ChildInstances'):
                temp_model = main_models.DescribeDBClusterProxyResponseBodyChildInstances()
                self.child_instances.append(temp_model.from_map(k1))

        if m.get('DBProxyClusterId') is not None:
            self.dbproxy_cluster_id = m.get('DBProxyClusterId')

        if m.get('DBProxyClusterNum') is not None:
            self.dbproxy_cluster_num = m.get('DBProxyClusterNum')

        if m.get('DBProxyClusterStatus') is not None:
            self.dbproxy_cluster_status = m.get('DBProxyClusterStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterProxyResponseBodyChildInstances(DaraModel):
    def __init__(
        self,
        dbnode_class: str = None,
        dbnode_ip: str = None,
        dbnode_id: str = None,
        dbnode_port: str = None,
        dbnode_status: str = None,
        host_name: str = None,
    ):
        self.dbnode_class = dbnode_class
        self.dbnode_ip = dbnode_ip
        self.dbnode_id = dbnode_id
        self.dbnode_port = dbnode_port
        self.dbnode_status = dbnode_status
        self.host_name = host_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        if self.dbnode_ip is not None:
            result['DBNodeIP'] = self.dbnode_ip

        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        if self.dbnode_port is not None:
            result['DBNodePort'] = self.dbnode_port

        if self.dbnode_status is not None:
            result['DBNodeStatus'] = self.dbnode_status

        if self.host_name is not None:
            result['HostName'] = self.host_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        if m.get('DBNodeIP') is not None:
            self.dbnode_ip = m.get('DBNodeIP')

        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        if m.get('DBNodePort') is not None:
            self.dbnode_port = m.get('DBNodePort')

        if m.get('DBNodeStatus') is not None:
            self.dbnode_status = m.get('DBNodeStatus')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        return self

