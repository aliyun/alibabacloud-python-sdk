# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class Instance(DaraModel):
    def __init__(
        self,
        current_amount: float = None,
        detached: bool = None,
        external_ip: str = None,
        external_instance_port: int = None,
        host_ip: str = None,
        host_name: str = None,
        inner_ip: str = None,
        instance_name: str = None,
        instance_port: int = None,
        instance_type: str = None,
        is_latest: bool = None,
        is_replica: bool = None,
        is_spot: bool = None,
        isolated: bool = None,
        last_state: List[Dict[str, Any]] = None,
        namespace: str = None,
        original_amount: float = None,
        ready_processes: int = None,
        reason: str = None,
        replica_name: str = None,
        resource_type: str = None,
        restart_count: int = None,
        role: str = None,
        start_at: str = None,
        start_time: str = None,
        status: str = None,
        tenant_host_ip: str = None,
        tenant_instance_ip: str = None,
        total_processes: int = None,
        zone: str = None,
    ):
        self.current_amount = current_amount
        self.detached = detached
        self.external_ip = external_ip
        self.external_instance_port = external_instance_port
        self.host_ip = host_ip
        self.host_name = host_name
        self.inner_ip = inner_ip
        self.instance_name = instance_name
        self.instance_port = instance_port
        self.instance_type = instance_type
        self.is_latest = is_latest
        self.is_replica = is_replica
        self.is_spot = is_spot
        self.isolated = isolated
        self.last_state = last_state
        self.namespace = namespace
        self.original_amount = original_amount
        self.ready_processes = ready_processes
        self.reason = reason
        self.replica_name = replica_name
        self.resource_type = resource_type
        self.restart_count = restart_count
        self.role = role
        self.start_at = start_at
        self.start_time = start_time
        self.status = status
        self.tenant_host_ip = tenant_host_ip
        self.tenant_instance_ip = tenant_instance_ip
        self.total_processes = total_processes
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_amount is not None:
            result['CurrentAmount'] = self.current_amount

        if self.detached is not None:
            result['Detached'] = self.detached

        if self.external_ip is not None:
            result['ExternalIP'] = self.external_ip

        if self.external_instance_port is not None:
            result['ExternalInstancePort'] = self.external_instance_port

        if self.host_ip is not None:
            result['HostIP'] = self.host_ip

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.inner_ip is not None:
            result['InnerIP'] = self.inner_ip

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_port is not None:
            result['InstancePort'] = self.instance_port

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_latest is not None:
            result['IsLatest'] = self.is_latest

        if self.is_replica is not None:
            result['IsReplica'] = self.is_replica

        if self.is_spot is not None:
            result['IsSpot'] = self.is_spot

        if self.isolated is not None:
            result['Isolated'] = self.isolated

        if self.last_state is not None:
            result['LastState'] = self.last_state

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount

        if self.ready_processes is not None:
            result['ReadyProcesses'] = self.ready_processes

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.replica_name is not None:
            result['ReplicaName'] = self.replica_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count

        if self.role is not None:
            result['Role'] = self.role

        if self.start_at is not None:
            result['StartAt'] = self.start_at

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_host_ip is not None:
            result['TenantHostIP'] = self.tenant_host_ip

        if self.tenant_instance_ip is not None:
            result['TenantInstanceIP'] = self.tenant_instance_ip

        if self.total_processes is not None:
            result['TotalProcesses'] = self.total_processes

        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentAmount') is not None:
            self.current_amount = m.get('CurrentAmount')

        if m.get('Detached') is not None:
            self.detached = m.get('Detached')

        if m.get('ExternalIP') is not None:
            self.external_ip = m.get('ExternalIP')

        if m.get('ExternalInstancePort') is not None:
            self.external_instance_port = m.get('ExternalInstancePort')

        if m.get('HostIP') is not None:
            self.host_ip = m.get('HostIP')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InnerIP') is not None:
            self.inner_ip = m.get('InnerIP')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstancePort') is not None:
            self.instance_port = m.get('InstancePort')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsLatest') is not None:
            self.is_latest = m.get('IsLatest')

        if m.get('IsReplica') is not None:
            self.is_replica = m.get('IsReplica')

        if m.get('IsSpot') is not None:
            self.is_spot = m.get('IsSpot')

        if m.get('Isolated') is not None:
            self.isolated = m.get('Isolated')

        if m.get('LastState') is not None:
            self.last_state = m.get('LastState')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')

        if m.get('ReadyProcesses') is not None:
            self.ready_processes = m.get('ReadyProcesses')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ReplicaName') is not None:
            self.replica_name = m.get('ReplicaName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('StartAt') is not None:
            self.start_at = m.get('StartAt')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantHostIP') is not None:
            self.tenant_host_ip = m.get('TenantHostIP')

        if m.get('TenantInstanceIP') is not None:
            self.tenant_instance_ip = m.get('TenantInstanceIP')

        if m.get('TotalProcesses') is not None:
            self.total_processes = m.get('TotalProcesses')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

