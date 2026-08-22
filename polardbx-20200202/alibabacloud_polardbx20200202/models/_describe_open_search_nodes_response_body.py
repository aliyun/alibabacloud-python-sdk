# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenSearchNodesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeOpenSearchNodesResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeOpenSearchNodesResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The data struct.
        self.data = data
        # Id of the request
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
            temp_model = main_models.DescribeOpenSearchNodesResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeOpenSearchNodesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOpenSearchNodesResponseBodyData(DaraModel):
    def __init__(
        self,
        result: List[main_models.DescribeOpenSearchNodesResponseBodyDataResult] = None,
    ):
        # The query result object.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeOpenSearchNodesResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DescribeOpenSearchNodesResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        cpu_cores: int = None,
        cpu_percent: str = None,
        disk_size_gb: int = None,
        disk_used_percent: str = None,
        health: str = None,
        heap_percent: str = None,
        host: str = None,
        host_name: str = None,
        load_one_m: str = None,
        memory_gb: int = None,
        node_type: str = None,
        port: int = None,
        zone_id: str = None,
    ):
        # The number of CPU cores of the node.
        self.cpu_cores = cpu_cores
        # The CPU usage (%).
        self.cpu_percent = cpu_percent
        # The total disk capacity of the node, in GB.
        self.disk_size_gb = disk_size_gb
        # The disk space usage of the node.
        self.disk_used_percent = disk_used_percent
        # The total number of unresolved baseline check items.
        self.health = health
        # The JVM heap memory usage of the node.
        self.heap_percent = heap_percent
        # The IP address and port of the session host that initiated the session.
        self.host = host
        # The name of the host on which the node instance runs. You can log on to the host and run the `hostname` command to view the hostname.
        self.host_name = host_name
        # The average system load of the node over the last 1 minute.
        self.load_one_m = load_one_m
        # The amount of memory used.
        self.memory_gb = memory_gb
        # The node type to query. Valid values:
        # - all: queries both dn and gms nodes.
        # - gms: queries only gms nodes.
        # - dn: queries only dn nodes.
        self.node_type = node_type
        # The port.
        self.port = port
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores

        if self.cpu_percent is not None:
            result['CpuPercent'] = self.cpu_percent

        if self.disk_size_gb is not None:
            result['DiskSizeGB'] = self.disk_size_gb

        if self.disk_used_percent is not None:
            result['DiskUsedPercent'] = self.disk_used_percent

        if self.health is not None:
            result['Health'] = self.health

        if self.heap_percent is not None:
            result['HeapPercent'] = self.heap_percent

        if self.host is not None:
            result['Host'] = self.host

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.load_one_m is not None:
            result['LoadOneM'] = self.load_one_m

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.port is not None:
            result['Port'] = self.port

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')

        if m.get('CpuPercent') is not None:
            self.cpu_percent = m.get('CpuPercent')

        if m.get('DiskSizeGB') is not None:
            self.disk_size_gb = m.get('DiskSizeGB')

        if m.get('DiskUsedPercent') is not None:
            self.disk_used_percent = m.get('DiskUsedPercent')

        if m.get('Health') is not None:
            self.health = m.get('Health')

        if m.get('HeapPercent') is not None:
            self.heap_percent = m.get('HeapPercent')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('LoadOneM') is not None:
            self.load_one_m = m.get('LoadOneM')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeOpenSearchNodesResponseBodyAccessDeniedDetail(DaraModel):
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
        # The authentication action.
        self.auth_action = auth_action
        # The identity used for authentication in the request.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The type of the authentication principal.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of the permission denial.
        self.no_permission_type = no_permission_type
        # The policy type.
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

