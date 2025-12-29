# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeReplicaSetRoleResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        replica_sets: main_models.DescribeReplicaSetRoleResponseBodyReplicaSets = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The details of the roles of the replica set instance.
        self.replica_sets = replica_sets
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.replica_sets:
            self.replica_sets.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.replica_sets is not None:
            result['ReplicaSets'] = self.replica_sets.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ReplicaSets') is not None:
            temp_model = main_models.DescribeReplicaSetRoleResponseBodyReplicaSets()
            self.replica_sets = temp_model.from_map(m.get('ReplicaSets'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeReplicaSetRoleResponseBodyReplicaSets(DaraModel):
    def __init__(
        self,
        replica_set: List[main_models.DescribeReplicaSetRoleResponseBodyReplicaSetsReplicaSet] = None,
    ):
        self.replica_set = replica_set

    def validate(self):
        if self.replica_set:
            for v1 in self.replica_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReplicaSet'] = []
        if self.replica_set is not None:
            for k1 in self.replica_set:
                result['ReplicaSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.replica_set = []
        if m.get('ReplicaSet') is not None:
            for k1 in m.get('ReplicaSet'):
                temp_model = main_models.DescribeReplicaSetRoleResponseBodyReplicaSetsReplicaSet()
                self.replica_set.append(temp_model.from_map(k1))

        return self

class DescribeReplicaSetRoleResponseBodyReplicaSetsReplicaSet(DaraModel):
    def __init__(
        self,
        connection_domain: str = None,
        connection_port: str = None,
        connection_type: str = None,
        expired_time: str = None,
        network_type: str = None,
        replica_set_role: str = None,
        role_id: str = None,
    ):
        # The endpoint of the node.
        self.connection_domain = connection_domain
        # The port number that is used to connect to the node.
        self.connection_port = connection_port
        # The connection type of the node.
        self.connection_type = connection_type
        # The remaining duration of the classic network endpoint. Unit: seconds.
        self.expired_time = expired_time
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**: the virtual private cloud (VPC)
        # *   **Classic**: the classic network
        # *   **Public**: the Internet
        self.network_type = network_type
        # The role of the node in the replica set instance. Valid values:
        # 
        # *   **Primary**
        # *   **Secondary**
        self.replica_set_role = replica_set_role
        # The role ID of the node.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain

        if self.connection_port is not None:
            result['ConnectionPort'] = self.connection_port

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.replica_set_role is not None:
            result['ReplicaSetRole'] = self.replica_set_role

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')

        if m.get('ConnectionPort') is not None:
            self.connection_port = m.get('ConnectionPort')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('ReplicaSetRole') is not None:
            self.replica_set_role = m.get('ReplicaSetRole')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self

