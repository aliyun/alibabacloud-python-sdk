# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenSearchTopologyResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeOpenSearchTopologyResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeOpenSearchTopologyResponseBodyData = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeOpenSearchTopologyResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeOpenSearchTopologyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOpenSearchTopologyResponseBodyData(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeOpenSearchTopologyResponseBodyDataNodes] = None,
        storage: main_models.DescribeOpenSearchTopologyResponseBodyDataStorage = None,
    ):
        self.nodes = nodes
        self.storage = storage

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()
        if self.storage:
            self.storage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.storage is not None:
            result['Storage'] = self.storage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeOpenSearchTopologyResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Storage') is not None:
            temp_model = main_models.DescribeOpenSearchTopologyResponseBodyDataStorage()
            self.storage = temp_model.from_map(m.get('Storage'))

        return self

class DescribeOpenSearchTopologyResponseBodyDataStorage(DaraModel):
    def __init__(
        self,
        replica_count: int = None,
        storage_total_gb: int = None,
        storage_type: str = None,
    ):
        self.replica_count = replica_count
        self.storage_total_gb = storage_total_gb
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.replica_count is not None:
            result['ReplicaCount'] = self.replica_count

        if self.storage_total_gb is not None:
            result['StorageTotalGB'] = self.storage_total_gb

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReplicaCount') is not None:
            self.replica_count = m.get('ReplicaCount')

        if m.get('StorageTotalGB') is not None:
            self.storage_total_gb = m.get('StorageTotalGB')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeOpenSearchTopologyResponseBodyDataNodes(DaraModel):
    def __init__(
        self,
        availability_zone: str = None,
        cpu: int = None,
        host: str = None,
        is_leader: bool = None,
        memory_gb: int = None,
        node_id: str = None,
        role: str = None,
        status: str = None,
    ):
        self.availability_zone = availability_zone
        self.cpu = cpu
        self.host = host
        self.is_leader = is_leader
        self.memory_gb = memory_gb
        self.node_id = node_id
        self.role = role
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.host is not None:
            result['Host'] = self.host

        if self.is_leader is not None:
            result['IsLeader'] = self.is_leader

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.role is not None:
            result['Role'] = self.role

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('IsLeader') is not None:
            self.is_leader = m.get('IsLeader')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeOpenSearchTopologyResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

