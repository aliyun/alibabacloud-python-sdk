# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class ContainerInfo(TeaModel):
    def __init__(
        self,
        current_reaon: str = None,
        current_status: str = None,
        current_timestamp: str = None,
        image: str = None,
        last_reason: str = None,
        last_status: str = None,
        last_timestamp: str = None,
        name: str = None,
        port: int = None,
        ready: bool = None,
        restart_count: int = None,
    ):
        self.current_reaon = current_reaon
        self.current_status = current_status
        self.current_timestamp = current_timestamp
        self.image = image
        self.last_reason = last_reason
        self.last_status = last_status
        self.last_timestamp = last_timestamp
        self.name = name
        self.port = port
        self.ready = ready
        self.restart_count = restart_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_reaon is not None:
            result['CurrentReaon'] = self.current_reaon
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status
        if self.current_timestamp is not None:
            result['CurrentTimestamp'] = self.current_timestamp
        if self.image is not None:
            result['Image'] = self.image
        if self.last_reason is not None:
            result['LastReason'] = self.last_reason
        if self.last_status is not None:
            result['LastStatus'] = self.last_status
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.name is not None:
            result['Name'] = self.name
        if self.port is not None:
            result['Port'] = self.port
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentReaon') is not None:
            self.current_reaon = m.get('CurrentReaon')
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')
        if m.get('CurrentTimestamp') is not None:
            self.current_timestamp = m.get('CurrentTimestamp')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('LastReason') is not None:
            self.last_reason = m.get('LastReason')
        if m.get('LastStatus') is not None:
            self.last_status = m.get('LastStatus')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        return self


class Group(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        cluster_id: str = None,
        create_time: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        name: str = None,
        queue_service: str = None,
        update_time: str = None,
    ):
        self.access_token = access_token
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.internet_endpoint = internet_endpoint
        self.intranet_endpoint = intranet_endpoint
        self.name = name
        self.queue_service = queue_service
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.name is not None:
            result['Name'] = self.name
        if self.queue_service is not None:
            result['QueueService'] = self.queue_service
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QueueService') is not None:
            self.queue_service = m.get('QueueService')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class Instance(TeaModel):
    def __init__(
        self,
        current_amount: float = None,
        external_ip: str = None,
        external_instance_port: int = None,
        host_ip: str = None,
        host_name: str = None,
        inner_ip: str = None,
        instance_name: str = None,
        instance_port: int = None,
        is_spot: bool = None,
        isolated: bool = None,
        last_state: List[Dict[str, Any]] = None,
        namespace: str = None,
        original_amount: float = None,
        ready_processes: int = None,
        reason: str = None,
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
        self.external_ip = external_ip
        self.external_instance_port = external_instance_port
        self.host_ip = host_ip
        self.host_name = host_name
        self.inner_ip = inner_ip
        self.instance_name = instance_name
        self.instance_port = instance_port
        self.is_spot = is_spot
        self.isolated = isolated
        self.last_state = last_state
        self.namespace = namespace
        self.original_amount = original_amount
        self.ready_processes = ready_processes
        self.reason = reason
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_amount is not None:
            result['CurrentAmount'] = self.current_amount
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


class Resource(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cpu_count: int = None,
        create_time: str = None,
        extra_data: Dict[str, Any] = None,
        gpu_count: int = None,
        instance_count: int = None,
        message: str = None,
        post_paid_instance_count: int = None,
        pre_paid_instance_count: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        status: str = None,
        update_time: str = None,
        vendor: str = None,
    ):
        self.cluster_id = cluster_id
        self.cpu_count = cpu_count
        self.create_time = create_time
        self.extra_data = extra_data
        self.gpu_count = gpu_count
        self.instance_count = instance_count
        self.message = message
        self.post_paid_instance_count = post_paid_instance_count
        self.pre_paid_instance_count = pre_paid_instance_count
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.status = status
        self.update_time = update_time
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.message is not None:
            result['Message'] = self.message
        if self.post_paid_instance_count is not None:
            result['PostPaidInstanceCount'] = self.post_paid_instance_count
        if self.pre_paid_instance_count is not None:
            result['PrePaidInstanceCount'] = self.pre_paid_instance_count
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PostPaidInstanceCount') is not None:
            self.post_paid_instance_count = m.get('PostPaidInstanceCount')
        if m.get('PrePaidInstanceCount') is not None:
            self.pre_paid_instance_count = m.get('PrePaidInstanceCount')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class ResourceInstance(TeaModel):
    def __init__(
        self,
        arch: str = None,
        auto_renewal: bool = None,
        charge_type: str = None,
        create_time: str = None,
        expired_time: str = None,
        instance_cpu_count: int = None,
        instance_gpu_count: int = None,
        instance_gpu_memory: str = None,
        instance_id: str = None,
        instance_ip: str = None,
        instance_memory: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_system_disk_size: int = None,
        instance_tenant_ip: str = None,
        instance_type: str = None,
        instance_used_cpu: float = None,
        instance_used_gpu: float = None,
        instance_used_gpu_memory: str = None,
        instance_used_memory: str = None,
        region: str = None,
        resource_id: str = None,
        zone: str = None,
    ):
        self.arch = arch
        self.auto_renewal = auto_renewal
        self.charge_type = charge_type
        self.create_time = create_time
        self.expired_time = expired_time
        self.instance_cpu_count = instance_cpu_count
        self.instance_gpu_count = instance_gpu_count
        self.instance_gpu_memory = instance_gpu_memory
        self.instance_id = instance_id
        self.instance_ip = instance_ip
        self.instance_memory = instance_memory
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.instance_system_disk_size = instance_system_disk_size
        self.instance_tenant_ip = instance_tenant_ip
        self.instance_type = instance_type
        self.instance_used_cpu = instance_used_cpu
        self.instance_used_gpu = instance_used_gpu
        self.instance_used_gpu_memory = instance_used_gpu_memory
        self.instance_used_memory = instance_used_memory
        self.region = region
        self.resource_id = resource_id
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arch is not None:
            result['Arch'] = self.arch
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_cpu_count is not None:
            result['InstanceCpuCount'] = self.instance_cpu_count
        if self.instance_gpu_count is not None:
            result['InstanceGpuCount'] = self.instance_gpu_count
        if self.instance_gpu_memory is not None:
            result['InstanceGpuMemory'] = self.instance_gpu_memory
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip
        if self.instance_memory is not None:
            result['InstanceMemory'] = self.instance_memory
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_system_disk_size is not None:
            result['InstanceSystemDiskSize'] = self.instance_system_disk_size
        if self.instance_tenant_ip is not None:
            result['InstanceTenantIp'] = self.instance_tenant_ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_used_cpu is not None:
            result['InstanceUsedCpu'] = self.instance_used_cpu
        if self.instance_used_gpu is not None:
            result['InstanceUsedGpu'] = self.instance_used_gpu
        if self.instance_used_gpu_memory is not None:
            result['InstanceUsedGpuMemory'] = self.instance_used_gpu_memory
        if self.instance_used_memory is not None:
            result['InstanceUsedMemory'] = self.instance_used_memory
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arch') is not None:
            self.arch = m.get('Arch')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceCpuCount') is not None:
            self.instance_cpu_count = m.get('InstanceCpuCount')
        if m.get('InstanceGpuCount') is not None:
            self.instance_gpu_count = m.get('InstanceGpuCount')
        if m.get('InstanceGpuMemory') is not None:
            self.instance_gpu_memory = m.get('InstanceGpuMemory')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')
        if m.get('InstanceMemory') is not None:
            self.instance_memory = m.get('InstanceMemory')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceSystemDiskSize') is not None:
            self.instance_system_disk_size = m.get('InstanceSystemDiskSize')
        if m.get('InstanceTenantIp') is not None:
            self.instance_tenant_ip = m.get('InstanceTenantIp')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceUsedCpu') is not None:
            self.instance_used_cpu = m.get('InstanceUsedCpu')
        if m.get('InstanceUsedGpu') is not None:
            self.instance_used_gpu = m.get('InstanceUsedGpu')
        if m.get('InstanceUsedGpuMemory') is not None:
            self.instance_used_gpu_memory = m.get('InstanceUsedGpuMemory')
        if m.get('InstanceUsedMemory') is not None:
            self.instance_used_memory = m.get('InstanceUsedMemory')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class ResourceInstanceWorker(TeaModel):
    def __init__(
        self,
        cpu_limit: int = None,
        cpu_request: int = None,
        gpu_limit: int = None,
        gpu_request: int = None,
        memory_limit: int = None,
        memory_rquest: int = None,
        name: str = None,
        ready: bool = None,
        restart_count: int = None,
        service_name: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.cpu_limit = cpu_limit
        self.cpu_request = cpu_request
        self.gpu_limit = gpu_limit
        self.gpu_request = gpu_request
        self.memory_limit = memory_limit
        self.memory_rquest = memory_rquest
        self.name = name
        self.ready = ready
        self.restart_count = restart_count
        self.service_name = service_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit
        if self.cpu_request is not None:
            result['CpuRequest'] = self.cpu_request
        if self.gpu_limit is not None:
            result['GpuLimit'] = self.gpu_limit
        if self.gpu_request is not None:
            result['GpuRequest'] = self.gpu_request
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.memory_rquest is not None:
            result['MemoryRquest'] = self.memory_rquest
        if self.name is not None:
            result['Name'] = self.name
        if self.ready is not None:
            result['Ready'] = self.ready
        if self.restart_count is not None:
            result['RestartCount'] = self.restart_count
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')
        if m.get('CpuRequest') is not None:
            self.cpu_request = m.get('CpuRequest')
        if m.get('GpuLimit') is not None:
            self.gpu_limit = m.get('GpuLimit')
        if m.get('GpuRequest') is not None:
            self.gpu_request = m.get('GpuRequest')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('MemoryRquest') is not None:
            self.memory_rquest = m.get('MemoryRquest')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')
        if m.get('RestartCount') is not None:
            self.restart_count = m.get('RestartCount')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ServiceLabels(TeaModel):
    def __init__(
        self,
        label_key: str = None,
        label_value: str = None,
    ):
        self.label_key = label_key
        self.label_value = label_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_key is not None:
            result['LabelKey'] = self.label_key
        if self.label_value is not None:
            result['LabelValue'] = self.label_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')
        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')
        return self


class Service(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        app_config: str = None,
        app_spec_name: str = None,
        app_type: str = None,
        app_version: str = None,
        caller_uid: str = None,
        cpu: int = None,
        create_time: str = None,
        current_version: int = None,
        extra_data: str = None,
        gpu: int = None,
        image: str = None,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        labels: List[ServiceLabels] = None,
        latest_version: int = None,
        memory: int = None,
        message: str = None,
        namespace: str = None,
        parent_uid: str = None,
        pending_instance: int = None,
        reason: str = None,
        region: str = None,
        request_id: str = None,
        resource: str = None,
        resource_alias: str = None,
        role: str = None,
        role_attrs: str = None,
        running_instance: int = None,
        safety_lock: str = None,
        secondary_internet_endpoint: str = None,
        secondary_intranet_endpoint: str = None,
        service_config: str = None,
        service_group: str = None,
        service_id: str = None,
        service_name: str = None,
        service_uid: str = None,
        source: str = None,
        status: str = None,
        total_instance: int = None,
        update_time: str = None,
        weight: int = None,
        workspace_id: str = None,
    ):
        self.access_token = access_token
        self.app_config = app_config
        self.app_spec_name = app_spec_name
        self.app_type = app_type
        self.app_version = app_version
        self.caller_uid = caller_uid
        self.cpu = cpu
        self.create_time = create_time
        self.current_version = current_version
        self.extra_data = extra_data
        self.gpu = gpu
        self.image = image
        self.internet_endpoint = internet_endpoint
        self.intranet_endpoint = intranet_endpoint
        self.labels = labels
        self.latest_version = latest_version
        self.memory = memory
        self.message = message
        self.namespace = namespace
        self.parent_uid = parent_uid
        self.pending_instance = pending_instance
        self.reason = reason
        self.region = region
        self.request_id = request_id
        self.resource = resource
        self.resource_alias = resource_alias
        self.role = role
        self.role_attrs = role_attrs
        self.running_instance = running_instance
        self.safety_lock = safety_lock
        self.secondary_internet_endpoint = secondary_internet_endpoint
        self.secondary_intranet_endpoint = secondary_intranet_endpoint
        self.service_config = service_config
        self.service_group = service_group
        self.service_id = service_id
        self.service_name = service_name
        self.service_uid = service_uid
        self.source = source
        self.status = status
        self.total_instance = total_instance
        self.update_time = update_time
        self.weight = weight
        self.workspace_id = workspace_id

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.app_config is not None:
            result['AppConfig'] = self.app_config
        if self.app_spec_name is not None:
            result['AppSpecName'] = self.app_spec_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.image is not None:
            result['Image'] = self.image
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid
        if self.pending_instance is not None:
            result['PendingInstance'] = self.pending_instance
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.resource_alias is not None:
            result['ResourceAlias'] = self.resource_alias
        if self.role is not None:
            result['Role'] = self.role
        if self.role_attrs is not None:
            result['RoleAttrs'] = self.role_attrs
        if self.running_instance is not None:
            result['RunningInstance'] = self.running_instance
        if self.safety_lock is not None:
            result['SafetyLock'] = self.safety_lock
        if self.secondary_internet_endpoint is not None:
            result['SecondaryInternetEndpoint'] = self.secondary_internet_endpoint
        if self.secondary_intranet_endpoint is not None:
            result['SecondaryIntranetEndpoint'] = self.secondary_intranet_endpoint
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_uid is not None:
            result['ServiceUid'] = self.service_uid
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.total_instance is not None:
            result['TotalInstance'] = self.total_instance
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AppConfig') is not None:
            self.app_config = m.get('AppConfig')
        if m.get('AppSpecName') is not None:
            self.app_spec_name = m.get('AppSpecName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = ServiceLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')
        if m.get('PendingInstance') is not None:
            self.pending_instance = m.get('PendingInstance')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ResourceAlias') is not None:
            self.resource_alias = m.get('ResourceAlias')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('RoleAttrs') is not None:
            self.role_attrs = m.get('RoleAttrs')
        if m.get('RunningInstance') is not None:
            self.running_instance = m.get('RunningInstance')
        if m.get('SafetyLock') is not None:
            self.safety_lock = m.get('SafetyLock')
        if m.get('SecondaryInternetEndpoint') is not None:
            self.secondary_internet_endpoint = m.get('SecondaryInternetEndpoint')
        if m.get('SecondaryIntranetEndpoint') is not None:
            self.secondary_intranet_endpoint = m.get('SecondaryIntranetEndpoint')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceUid') is not None:
            self.service_uid = m.get('ServiceUid')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalInstance') is not None:
            self.total_instance = m.get('TotalInstance')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CloneServiceRequest(TeaModel):
    def __init__(
        self,
        labels: Dict[str, str] = None,
        body: str = None,
    ):
        self.labels = labels
        # The request body. For more information, see [CreateService](https://help.aliyun.com/document_detail/412086.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CloneServiceShrinkRequest(TeaModel):
    def __init__(
        self,
        labels_shrink: str = None,
        body: str = None,
    ):
        self.labels_shrink = labels_shrink
        # The request body. For more information, see [CreateService](https://help.aliyun.com/document_detail/412086.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels_shrink is not None:
            result['Labels'] = self.labels_shrink
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels_shrink = m.get('Labels')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CloneServiceResponseBody(TeaModel):
    def __init__(
        self,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        request_id: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
    ):
        # The public endpoint of the service.
        self.internet_endpoint = internet_endpoint
        # The private endpoint of the service.
        self.intranet_endpoint = intranet_endpoint
        # Id of the request
        self.request_id = request_id
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The service status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CloneServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommitServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CommitServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CommitServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CommitServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAclPolicyRequestAclPolicyList(TeaModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        self.comment = comment
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class CreateAclPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_policy_list: List[CreateAclPolicyRequestAclPolicyList] = None,
        vpc_id: str = None,
    ):
        self.acl_policy_list = acl_policy_list
        self.vpc_id = vpc_id

    def validate(self):
        if self.acl_policy_list:
            for k in self.acl_policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclPolicyList'] = []
        if self.acl_policy_list is not None:
            for k in self.acl_policy_list:
                result['AclPolicyList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_policy_list = []
        if m.get('AclPolicyList') is not None:
            for k in m.get('AclPolicyList'):
                temp_model = CreateAclPolicyRequestAclPolicyList()
                self.acl_policy_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateAclPolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        acl_policy_list_shrink: str = None,
        vpc_id: str = None,
    ):
        self.acl_policy_list_shrink = acl_policy_list_shrink
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_policy_list_shrink is not None:
            result['AclPolicyList'] = self.acl_policy_list_shrink
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclPolicyList') is not None:
            self.acl_policy_list_shrink = m.get('AclPolicyList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateAclPolicyResponseBody(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.gateway_id = gateway_id
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAclPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAclPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppServiceRequest(TeaModel):
    def __init__(
        self,
        quota_id: str = None,
        workspace_id: str = None,
        app_type: str = None,
        app_version: str = None,
        config: Dict[str, Any] = None,
        replicas: int = None,
        service_name: str = None,
        service_spec: str = None,
    ):
        # The quota ID.
        self.quota_id = quota_id
        # The workspace ID.
        self.workspace_id = workspace_id
        # The application service type.
        # 
        # Valid values:
        # 
        # *   LLM
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.app_type = app_type
        # The application version.
        self.app_version = app_version
        # The additional configurations that are required for service deployment.
        self.config = config
        # The number of instances.
        # 
        # This parameter is required.
        self.replicas = replicas
        # The service name.
        # 
        # This parameter is required.
        self.service_name = service_name
        # The service specifications. Valid values:
        # 
        # *   llama_7b_fp16
        # *   llama_7b_int8
        # *   llama_13b_fp16
        # *   llama_7b_int8
        # *   chatglm_6b_fp16
        # *   chatglm_6b_int8
        # *   chatglm2_6b_fp16
        # *   baichuan_7b_int8
        # *   baichuan_13b_fp16
        # *   baichuan_7b_fp16
        # 
        # This parameter is required.
        self.service_spec = service_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.config is not None:
            result['Config'] = self.config
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')
        return self


class CreateAppServiceResponseBody(TeaModel):
    def __init__(
        self,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        region: str = None,
        request_id: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
    ):
        # The public endpoint of the service.
        self.internet_endpoint = internet_endpoint
        # The internal endpoint of the service.
        self.intranet_endpoint = intranet_endpoint
        # The region ID of the service.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The service state.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateAppServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAppServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBenchmarkTaskRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body. The body includes the parameters that are set to create a stress testing task.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateBenchmarkTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        region: str = None,
        request_id: str = None,
        task_name: str = None,
    ):
        # The returned message.
        self.message = message
        # The ID of the region where the stress testing task is performed.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The name of the stress testing task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class CreateBenchmarkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBenchmarkTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayRequest(TeaModel):
    def __init__(
        self,
        resource_name: str = None,
        enable_internet: bool = None,
        enable_intranet: bool = None,
        instance_type: str = None,
        name: str = None,
        replicas: int = None,
    ):
        # The name of the resource group.
        self.resource_name = resource_name
        # Specifies whether to enable Internet access. Default value: false.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_internet = enable_internet
        # Specifies whether to enable internal network access. Default value: true.
        self.enable_intranet = enable_intranet
        # The instance type used for the private gateway.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The private gateway alias.
        self.name = name
        self.replicas = replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.enable_internet is not None:
            result['EnableInternet'] = self.enable_internet
        if self.enable_intranet is not None:
            result['EnableIntranet'] = self.enable_intranet
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.name is not None:
            result['Name'] = self.name
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('EnableInternet') is not None:
            self.enable_internet = m.get('EnableInternet')
        if m.get('EnableIntranet') is not None:
            self.enable_intranet = m.get('EnableIntranet')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        return self


class CreateGatewayResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The region ID of the private gateway.
        self.cluster_id = cluster_id
        # The private gateway ID.
        self.gateway_id = gateway_id
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayIntranetLinkedVpcRequest(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateGatewayIntranetLinkedVpcResponseBody(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The private gateway ID.
        self.gateway_id = gateway_id
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGatewayIntranetLinkedVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayIntranetLinkedVpcResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGatewayIntranetLinkedVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRequestSelfManagedResourceOptionsNodeTolerations(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The result.
        # 
        # Valid values:
        # 
        # *   PreferNoSchedule
        # *   NoSchedule
        # *   NoExecute
        self.effect = effect
        # The key name.
        self.key = key
        # The relationship between key names and key values.
        # 
        # Valid values:
        # 
        # *   Equal
        # *   Exists
        self.operator = operator
        # The key value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateResourceRequestSelfManagedResourceOptions(TeaModel):
    def __init__(
        self,
        external_cluster_id: str = None,
        node_match_labels: Dict[str, str] = None,
        node_tolerations: List[CreateResourceRequestSelfManagedResourceOptionsNodeTolerations] = None,
        role_name: str = None,
    ):
        # The ID of the self-managed cluster.
        self.external_cluster_id = external_cluster_id
        # The tag key-value pairs for nodes.
        self.node_match_labels = node_match_labels
        # Tolerations for nodes.
        self.node_tolerations = node_tolerations
        # The name of the RAM user to which the permissions on Elastic Algorithm Service of Platform for AI (PAI-EAS) are granted.
        self.role_name = role_name

    def validate(self):
        if self.node_tolerations:
            for k in self.node_tolerations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_cluster_id is not None:
            result['ExternalClusterId'] = self.external_cluster_id
        if self.node_match_labels is not None:
            result['NodeMatchLabels'] = self.node_match_labels
        result['NodeTolerations'] = []
        if self.node_tolerations is not None:
            for k in self.node_tolerations:
                result['NodeTolerations'].append(k.to_map() if k else None)
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalClusterId') is not None:
            self.external_cluster_id = m.get('ExternalClusterId')
        if m.get('NodeMatchLabels') is not None:
            self.node_match_labels = m.get('NodeMatchLabels')
        self.node_tolerations = []
        if m.get('NodeTolerations') is not None:
            for k in m.get('NodeTolerations'):
                temp_model = CreateResourceRequestSelfManagedResourceOptionsNodeTolerations()
                self.node_tolerations.append(temp_model.from_map(k))
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CreateResourceRequest(TeaModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        charge_type: str = None,
        ecs_instance_count: int = None,
        ecs_instance_type: str = None,
        resource_type: str = None,
        self_managed_resource_options: CreateResourceRequestSelfManagedResourceOptions = None,
        system_disk_size: int = None,
        zone: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   false (default)
        # *   true
        self.auto_renewal = auto_renewal
        # The billing method. Valid values:
        # 
        # *   PrePaid: the subscription billing method.
        # *   PostPaid: the pay-as-you-go billing method.
        # 
        # >  This parameter is required when the ResourceType parameter is set to Dedicated.
        self.charge_type = charge_type
        # The number of ECS instances.
        # 
        # >  This parameter is required when the ResourceType parameter is set to Dedicated.
        self.ecs_instance_count = ecs_instance_count
        # The type of the Elastic Compute Service (ECS) instance.
        # 
        # >  This parameter is required when the ResourceType parameter is set to Dedicated.
        self.ecs_instance_type = ecs_instance_type
        # The type of the resource group. Valid values:
        # 
        # *   Dedicated: the dedicated resource group.
        # *   SelfManaged: the self-managed resource group.
        # 
        # >  If you use a self-managed resource group, you must configure a whitelist.
        self.resource_type = resource_type
        # The configurations of the self-managed resource group.
        self.self_managed_resource_options = self_managed_resource_options
        # The size of the system disk. Unit: GiB. Valid values: 200 to 2000. Default value: 200.
        self.system_disk_size = system_disk_size
        # The ID of the zone in which the instance resides.
        self.zone = zone

    def validate(self):
        if self.self_managed_resource_options:
            self.self_managed_resource_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.ecs_instance_count is not None:
            result['EcsInstanceCount'] = self.ecs_instance_count
        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.self_managed_resource_options is not None:
            result['SelfManagedResourceOptions'] = self.self_managed_resource_options.to_map()
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EcsInstanceCount') is not None:
            self.ecs_instance_count = m.get('EcsInstanceCount')
        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SelfManagedResourceOptions') is not None:
            temp_model = CreateResourceRequestSelfManagedResourceOptions()
            self.self_managed_resource_options = temp_model.from_map(m['SelfManagedResourceOptions'])
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_ids: List[str] = None,
        owner_uid: str = None,
        request_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        # The ID of the cluster to which the resource group belongs.
        self.cluster_id = cluster_id
        # The instance IDs.
        self.instance_ids = instance_ids
        # The user ID (UID) of the resource group owner.
        self.owner_uid = owner_uid
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_id = resource_id
        # The name of the resource group.
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceInstancesRequest(TeaModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        charge_type: str = None,
        ecs_instance_count: int = None,
        ecs_instance_type: str = None,
        system_disk_size: int = None,
        user_data: str = None,
        zone: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # *   false (default)
        # *   true
        self.auto_renewal = auto_renewal
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription.
        # *   PostPaid: pay-as-you-go.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The number of instances that you want to create. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.ecs_instance_count = ecs_instance_count
        # The type of the Elastic Compute Service (ECS) instance.
        # 
        # This parameter is required.
        self.ecs_instance_type = ecs_instance_type
        # The size of the system disk. Unit: GiB. Valid values: 200 to 2000. Default value: 200.
        self.system_disk_size = system_disk_size
        # The user-defined information. This parameter is not in use.
        self.user_data = user_data
        # The zone to which the instance belongs.
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.ecs_instance_count is not None:
            result['EcsInstanceCount'] = self.ecs_instance_count
        if self.ecs_instance_type is not None:
            result['EcsInstanceType'] = self.ecs_instance_type
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('EcsInstanceCount') is not None:
            self.ecs_instance_count = m.get('EcsInstanceCount')
        if m.get('EcsInstanceType') is not None:
            self.ecs_instance_type = m.get('EcsInstanceType')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class CreateResourceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The instance IDs.
        self.instance_ids = instance_ids
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceLogRequest(TeaModel):
    def __init__(
        self,
        log_store: str = None,
        project_name: str = None,
    ):
        # The Logstore of Log Service. For more information about how to query a Logstore, see [ListLogStores](https://help.aliyun.com/document_detail/426970.html).
        # 
        # This parameter is required.
        self.log_store = log_store
        # The Log Service project that is associated with the resource group. For more information about how to query the project, see [ListProject](https://help.aliyun.com/document_detail/74955.html).
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class CreateResourceLogResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        develop: str = None,
        labels: Dict[str, str] = None,
        workspace_id: str = None,
        body: str = None,
    ):
        # Specifies whether to enter development mode.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.develop = develop
        # The custom label.
        self.labels = labels
        # The workspace ID.
        self.workspace_id = workspace_id
        # The request body. For more information about the key request parameters, see **Table 1. Request body parameters** and **Table 2. Metadata parameters**. For more information about all related parameters, see [Parameters of model services](https://help.aliyun.com/document_detail/450525.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.develop is not None:
            result['Develop'] = self.develop
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Develop') is not None:
            self.develop = m.get('Develop')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateServiceShrinkRequest(TeaModel):
    def __init__(
        self,
        develop: str = None,
        labels_shrink: str = None,
        workspace_id: str = None,
        body: str = None,
    ):
        # Specifies whether to enter development mode.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.develop = develop
        # The custom label.
        self.labels_shrink = labels_shrink
        # The workspace ID.
        self.workspace_id = workspace_id
        # The request body. For more information about the key request parameters, see **Table 1. Request body parameters** and **Table 2. Metadata parameters**. For more information about all related parameters, see [Parameters of model services](https://help.aliyun.com/document_detail/450525.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.develop is not None:
            result['Develop'] = self.develop
        if self.labels_shrink is not None:
            result['Labels'] = self.labels_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Develop') is not None:
            self.develop = m.get('Develop')
        if m.get('Labels') is not None:
            self.labels_shrink = m.get('Labels')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        internet_endpoint: str = None,
        intranet_endpoint: str = None,
        region: str = None,
        request_id: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
    ):
        # The public endpoint of the created service.
        self.internet_endpoint = internet_endpoint
        # The internal endpoint of the created service.
        self.intranet_endpoint = intranet_endpoint
        # The region ID of the created service.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The ID of the created service.
        self.service_id = service_id
        # The name of the created service.
        self.service_name = service_name
        # The service state.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.region is not None:
            result['Region'] = self.region
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceAutoScalerRequestBehaviorOnZero(TeaModel):
    def __init__(
        self,
        scale_down_grace_period_seconds: int = None,
        scale_up_activation_replicas: int = None,
    ):
        # The time window that is required before the number of instances is reduced to 0. The number of instances can be reduced to 0 only if no request is available or no traffic exists in the specified time window. Default value: 600.
        self.scale_down_grace_period_seconds = scale_down_grace_period_seconds
        # The number of instances that you want to create at a time if the number of instances is 0. Default value: 1.
        self.scale_up_activation_replicas = scale_up_activation_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_down_grace_period_seconds is not None:
            result['scaleDownGracePeriodSeconds'] = self.scale_down_grace_period_seconds
        if self.scale_up_activation_replicas is not None:
            result['scaleUpActivationReplicas'] = self.scale_up_activation_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleDownGracePeriodSeconds') is not None:
            self.scale_down_grace_period_seconds = m.get('scaleDownGracePeriodSeconds')
        if m.get('scaleUpActivationReplicas') is not None:
            self.scale_up_activation_replicas = m.get('scaleUpActivationReplicas')
        return self


class CreateServiceAutoScalerRequestBehaviorScaleDown(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
    ):
        # The time window that is required before the scale-in operation is performed. The scale-in operation can be performed only if the specified metric drops below the specified threshold in the specified time window. Default value: 300.
        self.stabilization_window_seconds = stabilization_window_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        return self


class CreateServiceAutoScalerRequestBehaviorScaleUp(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
    ):
        # The time window that is required before the scale-out operation is performed. The scale-out operation can be performed only if the specified metric exceeds the specified threshold in the specified time window. Default value: 0.
        self.stabilization_window_seconds = stabilization_window_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        return self


class CreateServiceAutoScalerRequestBehavior(TeaModel):
    def __init__(
        self,
        on_zero: CreateServiceAutoScalerRequestBehaviorOnZero = None,
        scale_down: CreateServiceAutoScalerRequestBehaviorScaleDown = None,
        scale_up: CreateServiceAutoScalerRequestBehaviorScaleUp = None,
    ):
        # The operation that reduces the number of instances to 0.
        self.on_zero = on_zero
        # The scale-in operation.
        self.scale_down = scale_down
        # The scale-out operation.
        self.scale_up = scale_up

    def validate(self):
        if self.on_zero:
            self.on_zero.validate()
        if self.scale_down:
            self.scale_down.validate()
        if self.scale_up:
            self.scale_up.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_zero is not None:
            result['onZero'] = self.on_zero.to_map()
        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down.to_map()
        if self.scale_up is not None:
            result['scaleUp'] = self.scale_up.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onZero') is not None:
            temp_model = CreateServiceAutoScalerRequestBehaviorOnZero()
            self.on_zero = temp_model.from_map(m['onZero'])
        if m.get('scaleDown') is not None:
            temp_model = CreateServiceAutoScalerRequestBehaviorScaleDown()
            self.scale_down = temp_model.from_map(m['scaleDown'])
        if m.get('scaleUp') is not None:
            temp_model = CreateServiceAutoScalerRequestBehaviorScaleUp()
            self.scale_up = temp_model.from_map(m['scaleUp'])
        return self


class CreateServiceAutoScalerRequestScaleStrategies(TeaModel):
    def __init__(
        self,
        metric_name: str = None,
        service: str = None,
        threshold: float = None,
    ):
        # The name of the metric for triggering auto scaling. Valid values:
        # 
        # *   qps: the queries per second (qps) for an individual instance.
        # *   cpu: the cpu utilization.
        # * gpu[util]: gpu utilization.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The service for which the metric is specified. If you do not set this parameter, the current service is specified by default.
        self.service = service
        # The threshold of the metric that triggers auto scaling.
        # 
        # *   If you set metricName to qps, scale-out is triggered when the average qps for a single instance is greater than this threshold.
        # *   If you set metricName to cpu, scale-out is triggered when the average cpu utilization for a single instance is greater than this threshold.
        # *   If you set metricName to gpu, scale-out is triggered when the average cpu utilization for a single instance is greater than this threshold.
        # 
        # This parameter is required.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.service is not None:
            result['service'] = self.service
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class CreateServiceAutoScalerRequest(TeaModel):
    def __init__(
        self,
        behavior: CreateServiceAutoScalerRequestBehavior = None,
        max: int = None,
        min: int = None,
        scale_strategies: List[CreateServiceAutoScalerRequestScaleStrategies] = None,
    ):
        # The Autoscaler operation.
        self.behavior = behavior
        # The maximum number of instances in the service. The value of max must be greater than the value of min.
        # 
        # This parameter is required.
        self.max = max
        # The minimum number of instances in the service.
        # 
        # This parameter is required.
        self.min = min
        # The service for which the metric is specified. If you do not set this parameter, the current service is specified by default.
        # 
        # This parameter is required.
        self.scale_strategies = scale_strategies

    def validate(self):
        if self.behavior:
            self.behavior.validate()
        if self.scale_strategies:
            for k in self.scale_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behavior is not None:
            result['behavior'] = self.behavior.to_map()
        if self.max is not None:
            result['max'] = self.max
        if self.min is not None:
            result['min'] = self.min
        result['scaleStrategies'] = []
        if self.scale_strategies is not None:
            for k in self.scale_strategies:
                result['scaleStrategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('behavior') is not None:
            temp_model = CreateServiceAutoScalerRequestBehavior()
            self.behavior = temp_model.from_map(m['behavior'])
        if m.get('max') is not None:
            self.max = m.get('max')
        if m.get('min') is not None:
            self.min = m.get('min')
        self.scale_strategies = []
        if m.get('scaleStrategies') is not None:
            for k in m.get('scaleStrategies'):
                temp_model = CreateServiceAutoScalerRequestScaleStrategies()
                self.scale_strategies.append(temp_model.from_map(k))
        return self


class CreateServiceAutoScalerResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceAutoScalerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceAutoScalerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceCronScalerRequestScaleJobs(TeaModel):
    def __init__(
        self,
        name: str = None,
        schedule: str = None,
        target_size: int = None,
    ):
        # The name of the CronHPA job.
        self.name = name
        # The cron expression that is used to configure the execution time of the CronHPA job. For more information about how to configure cron expressions, see **Description of special characters** in this topic.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The number of instances that you want to configure for the CronHPA job.
        # 
        # This parameter is required.
        self.target_size = target_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.target_size is not None:
            result['TargetSize'] = self.target_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')
        return self


class CreateServiceCronScalerRequest(TeaModel):
    def __init__(
        self,
        exclude_dates: List[str] = None,
        scale_jobs: List[CreateServiceCronScalerRequestScaleJobs] = None,
    ):
        # The points in time that are excluded when you schedule a CronHPA job. The points in time must be specified by using a cron expression.
        self.exclude_dates = exclude_dates
        # The description of the CronHPA job.
        # 
        # This parameter is required.
        self.scale_jobs = scale_jobs

    def validate(self):
        if self.scale_jobs:
            for k in self.scale_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_dates is not None:
            result['ExcludeDates'] = self.exclude_dates
        result['ScaleJobs'] = []
        if self.scale_jobs is not None:
            for k in self.scale_jobs:
                result['ScaleJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeDates') is not None:
            self.exclude_dates = m.get('ExcludeDates')
        self.scale_jobs = []
        if m.get('ScaleJobs') is not None:
            for k in m.get('ScaleJobs'):
                temp_model = CreateServiceCronScalerRequestScaleJobs()
                self.scale_jobs.append(temp_model.from_map(k))
        return self


class CreateServiceCronScalerResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceCronScalerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceCronScalerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceMirrorRequest(TeaModel):
    def __init__(
        self,
        ratio: int = None,
        target: List[str] = None,
    ):
        # The percentage of the traffic that is mirrored to the destination service. Valid values: 0 to 100.
        self.ratio = ratio
        # The instances.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class CreateServiceMirrorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceMirrorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceMirrorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclPolicyRequestAclPolicyList(TeaModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        self.comment = comment
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class DeleteAclPolicyRequest(TeaModel):
    def __init__(
        self,
        acl_policy_list: List[DeleteAclPolicyRequestAclPolicyList] = None,
        vpc_id: str = None,
    ):
        self.acl_policy_list = acl_policy_list
        self.vpc_id = vpc_id

    def validate(self):
        if self.acl_policy_list:
            for k in self.acl_policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AclPolicyList'] = []
        if self.acl_policy_list is not None:
            for k in self.acl_policy_list:
                result['AclPolicyList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_policy_list = []
        if m.get('AclPolicyList') is not None:
            for k in m.get('AclPolicyList'):
                temp_model = DeleteAclPolicyRequestAclPolicyList()
                self.acl_policy_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DeleteAclPolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        acl_policy_list_shrink: str = None,
        vpc_id: str = None,
    ):
        self.acl_policy_list_shrink = acl_policy_list_shrink
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_policy_list_shrink is not None:
            result['AclPolicyList'] = self.acl_policy_list_shrink
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclPolicyList') is not None:
            self.acl_policy_list_shrink = m.get('AclPolicyList')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DeleteAclPolicyResponseBody(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.gateway_id = gateway_id
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAclPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAclPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBenchmarkTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBenchmarkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBenchmarkTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The private gateway ID.
        self.gateway_id = gateway_id
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayIntranetLinkedVpcRequest(TeaModel):
    def __init__(
        self,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DeleteGatewayIntranetLinkedVpcResponseBody(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The private gateway ID.
        self.gateway_id = gateway_id
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteGatewayIntranetLinkedVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayIntranetLinkedVpcResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGatewayIntranetLinkedVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceDLinkResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceDLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceDLinkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceDLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceInstancesRequest(TeaModel):
    def __init__(
        self,
        all_failed: bool = None,
        instance_list: str = None,
    ):
        # Specifies whether to delete all the instances that fail to be created. Valid values:
        # 
        # *   true
        # *   false
        self.all_failed = all_failed
        # The instances. Separate multiple instances with commas (,), such as `instanceId1,instanceId2`. For more information about how to query the instances, see [ListResourceInstances](https://help.aliyun.com/document_detail/412129.html).
        self.instance_list = instance_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_failed is not None:
            result['AllFailed'] = self.all_failed
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllFailed') is not None:
            self.all_failed = m.get('AllFailed')
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        return self


class DeleteResourceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceLogResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceAutoScalerResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceAutoScalerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceAutoScalerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceCronScalerResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceCronScalerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceCronScalerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        container: str = None,
        instance_list: str = None,
        soft_restart: bool = None,
    ):
        # The name of the container whose process needs to be restarted. This parameter takes effect only if the SoftRestart parameter is set to true.
        self.container = container
        # The instances that you want to restart. Separate multiple instance names with commas (,). For more information about how to query the instance name, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        # 
        # This parameter is required.
        self.instance_list = instance_list
        # Specifies whether to restart only the container process without recreating the instance. Default value: false. Valid values: true and false.
        self.soft_restart = soft_restart

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container is not None:
            result['Container'] = self.container
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        if self.soft_restart is not None:
            result['SoftRestart'] = self.soft_restart
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Container') is not None:
            self.container = m.get('Container')
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        if m.get('SoftRestart') is not None:
            self.soft_restart = m.get('SoftRestart')
        return self


class DeleteServiceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceLabelRequest(TeaModel):
    def __init__(
        self,
        keys: List[str] = None,
    ):
        # The service tags that you want to delete.
        # 
        # This parameter is required.
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class DeleteServiceLabelShrinkRequest(TeaModel):
    def __init__(
        self,
        keys_shrink: str = None,
    ):
        # The service tags that you want to delete.
        # 
        # This parameter is required.
        self.keys_shrink = keys_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')
        return self


class DeleteServiceLabelResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceLabelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceMirrorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServiceMirrorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceMirrorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBenchmarkTaskResponseBody(TeaModel):
    def __init__(
        self,
        available_agent: int = None,
        caller_uid: str = None,
        desired_agent: int = None,
        endpoint: str = None,
        message: str = None,
        parent_uid: str = None,
        reason: str = None,
        request_id: str = None,
        service_name: str = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        token: str = None,
    ):
        # The number of instances that you can test.
        self.available_agent = available_agent
        # The ID of the operation caller.
        self.caller_uid = caller_uid
        # The number of instances that you want to test.
        self.desired_agent = desired_agent
        # The endpoint of the service gateway.
        self.endpoint = endpoint
        # The returned message.
        self.message = message
        # The ID of the Alibaba Cloud account that is used to call the operation.
        self.parent_uid = parent_uid
        # The event or reason that causes the current state of the stress testing task.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The name of the service that you want to test.
        self.service_name = service_name
        # The state of the stress testing task.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Starting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DeleteFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopping
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Error
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Updating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CreateFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The ID of the stress testing task.
        self.task_id = task_id
        # The name of the stress testing task.
        self.task_name = task_name
        # The token for authentication when a stress testing task is created.
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_agent is not None:
            result['AvailableAgent'] = self.available_agent
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.desired_agent is not None:
            result['DesiredAgent'] = self.desired_agent
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.message is not None:
            result['Message'] = self.message
        if self.parent_uid is not None:
            result['ParentUid'] = self.parent_uid
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAgent') is not None:
            self.available_agent = m.get('AvailableAgent')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('DesiredAgent') is not None:
            self.desired_agent = m.get('DesiredAgent')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ParentUid') is not None:
            self.parent_uid = m.get('ParentUid')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DescribeBenchmarkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBenchmarkTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBenchmarkTaskReportRequest(TeaModel):
    def __init__(
        self,
        report_type: str = None,
    ):
        # The report type of the stress testing task. Valid values: RAW and Report.
        self.report_type = report_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        return self


class DescribeBenchmarkTaskReportResponseBody(TeaModel):
    def __init__(
        self,
        data: Any = None,
        report_url: str = None,
        request_id: str = None,
    ):
        # If the value of ReportType is set to RAW, the details about the stress testing report are returned.
        self.data = data
        # If the value of ReportType is set to Report, the URL of the stress testing report is returned.
        self.report_url = report_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeBenchmarkTaskReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBenchmarkTaskReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeBenchmarkTaskReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGatewayResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        external_cluster_id: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        instance_type: str = None,
        internet_domain: str = None,
        internet_enabled: bool = None,
        internet_status: str = None,
        intranet_domain: str = None,
        is_default: bool = None,
        replicas: int = None,
        request_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The time when the private gateway was created. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the self-managed cluster.
        self.external_cluster_id = external_cluster_id
        # The ID of the private gateway.
        self.gateway_id = gateway_id
        # The private gateway alias.
        self.gateway_name = gateway_name
        # The instance type used for the private gateway.
        self.instance_type = instance_type
        # The public endpoint.
        self.internet_domain = internet_domain
        # Indicates whether Internet access is enabled.
        self.internet_enabled = internet_enabled
        self.internet_status = internet_status
        # The internal endpoint.
        self.intranet_domain = intranet_domain
        self.is_default = is_default
        self.replicas = replicas
        # The request ID.
        self.request_id = request_id
        # The state of the private gateway.
        self.status = status
        # The time when the private gateway was updated. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_cluster_id is not None:
            result['ExternalClusterId'] = self.external_cluster_id
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.internet_enabled is not None:
            result['InternetEnabled'] = self.internet_enabled
        if self.internet_status is not None:
            result['InternetStatus'] = self.internet_status
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalClusterId') is not None:
            self.external_cluster_id = m.get('ExternalClusterId')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('InternetEnabled') is not None:
            self.internet_enabled = m.get('InternetEnabled')
        if m.get('InternetStatus') is not None:
            self.internet_status = m.get('InternetStatus')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Group = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Group()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cpu_count: int = None,
        create_time: str = None,
        extra_data: str = None,
        gpu_count: int = None,
        instance_count: int = None,
        message: str = None,
        owner_uid: str = None,
        post_paid_instance_count: int = None,
        pre_paid_instance_count: int = None,
        request_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The ID of the cluster to which the resource group belongs.
        self.cluster_id = cluster_id
        # The total number of CPU cores.
        self.cpu_count = cpu_count
        # The time when the resource group was created.
        self.create_time = create_time
        # The additional information, such as the connection status of a virtual private cloud (VPC) and the log status of Log Service.
        self.extra_data = extra_data
        # The total number of GPUs.
        self.gpu_count = gpu_count
        # The total number of instances in the resource group.
        self.instance_count = instance_count
        # The returned message.
        self.message = message
        # The ID of the resource group owner.
        self.owner_uid = owner_uid
        # The total number of pay-as-you-go instances in the resource group.
        self.post_paid_instance_count = post_paid_instance_count
        # The total number of subscription instances in the resource group.
        self.pre_paid_instance_count = pre_paid_instance_count
        # The request ID.
        self.request_id = request_id
        # The ID of the Elastic Algorithm Service (EAS) resource.
        self.resource_id = resource_id
        # The name of the EAS resource.
        self.resource_name = resource_name
        # The type of the resource group. Valid values:
        # 
        # *   Dedicated: the dedicated resource group.
        # *   SelfManaged: the self-managed resource group.
        self.resource_type = resource_type
        # The state of the resource group.
        self.status = status
        # The time when the resource group was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.message is not None:
            result['Message'] = self.message
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.post_paid_instance_count is not None:
            result['PostPaidInstanceCount'] = self.post_paid_instance_count
        if self.pre_paid_instance_count is not None:
            result['PrePaidInstanceCount'] = self.pre_paid_instance_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('PostPaidInstanceCount') is not None:
            self.post_paid_instance_count = m.get('PostPaidInstanceCount')
        if m.get('PrePaidInstanceCount') is not None:
            self.pre_paid_instance_count = m.get('PrePaidInstanceCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceDLinkResponseBody(TeaModel):
    def __init__(
        self,
        aux_vswitch_list: List[str] = None,
        destination_cidrs: str = None,
        request_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The IDs of the secondary vSwitches that are directly connected.
        self.aux_vswitch_list = aux_vswitch_list
        # The CIDR blocks of the clients that you want to connect to. After this parameter is specified, the CIDR blocks are added to the back-to-origin route of the server. Either this parameter or the VSwitchIdList parameter can be used to determine CIDR blocks.
        self.destination_cidrs = destination_cidrs
        # The request ID.
        self.request_id = request_id
        # The ID of the security group that is directly connected.
        self.security_group_id = security_group_id
        # The ID of the primary vSwitch that is directly connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC that is directly connected.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aux_vswitch_list is not None:
            result['AuxVSwitchList'] = self.aux_vswitch_list
        if self.destination_cidrs is not None:
            result['DestinationCIDRs'] = self.destination_cidrs
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuxVSwitchList') is not None:
            self.aux_vswitch_list = m.get('AuxVSwitchList')
        if m.get('DestinationCIDRs') is not None:
            self.destination_cidrs = m.get('DestinationCIDRs')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeResourceDLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceDLinkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResourceDLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceLogResponseBody(TeaModel):
    def __init__(
        self,
        log_store: str = None,
        message: str = None,
        project_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The Logstore of Log Service.
        self.log_store = log_store
        # The returned message.
        self.message = message
        # The Log Service project that is associated with the resource group.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The state of the resource group.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_store is not None:
            result['LogStore'] = self.log_store
        if self.message is not None:
            result['Message'] = self.message
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeResourceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResourceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Service = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = Service()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceAutoScalerResponseBodyCurrentMetrics(TeaModel):
    def __init__(
        self,
        metric_name: str = None,
        service: str = None,
        value: float = None,
    ):
        # The metric name. Valid values:
        # 
        # *   QPS
        # *   CPU
        self.metric_name = metric_name
        # The service for which the metric is specified.
        self.service = service
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.service is not None:
            result['service'] = self.service
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeServiceAutoScalerResponseBodyScaleStrategies(TeaModel):
    def __init__(
        self,
        metric_name: str = None,
        service: str = None,
        threshold: float = None,
    ):
        # The metric name. Valid values:
        # 
        # *   QPS: the queries per second (QPS) for an individual instance.
        # *   CPU: the CPU utilization.
        self.metric_name = metric_name
        # The service for which the metric is specified. If you do not set this parameter, the current service is specified by default.
        self.service = service
        # The threshold of the metric that triggers auto scaling.
        # 
        # *   If you set metricName to QPS, scale-out is triggered when the average QPS for a single instance is greater than this threshold.
        # *   If you set metricName to CPU, scale-out is triggered when the average CPU utilization for a single instance is greater than this threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.service is not None:
            result['service'] = self.service
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class DescribeServiceAutoScalerResponseBody(TeaModel):
    def __init__(
        self,
        behavior: Dict[str, Any] = None,
        current_metrics: List[DescribeServiceAutoScalerResponseBodyCurrentMetrics] = None,
        max_replica: int = None,
        min_replica: int = None,
        request_id: str = None,
        scale_strategies: List[DescribeServiceAutoScalerResponseBodyScaleStrategies] = None,
        service_name: str = None,
    ):
        # The additional information about the Autoscaler policy, such as the interval of triggering Autoscaler.
        self.behavior = behavior
        # The metrics.
        self.current_metrics = current_metrics
        # The maximum number of instances in the service.
        self.max_replica = max_replica
        # The minimum number of instances in the service.
        self.min_replica = min_replica
        # The request ID.
        self.request_id = request_id
        # The auto scaling policies.
        self.scale_strategies = scale_strategies
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.current_metrics:
            for k in self.current_metrics:
                if k:
                    k.validate()
        if self.scale_strategies:
            for k in self.scale_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behavior is not None:
            result['Behavior'] = self.behavior
        result['CurrentMetrics'] = []
        if self.current_metrics is not None:
            for k in self.current_metrics:
                result['CurrentMetrics'].append(k.to_map() if k else None)
        if self.max_replica is not None:
            result['MaxReplica'] = self.max_replica
        if self.min_replica is not None:
            result['MinReplica'] = self.min_replica
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScaleStrategies'] = []
        if self.scale_strategies is not None:
            for k in self.scale_strategies:
                result['ScaleStrategies'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')
        self.current_metrics = []
        if m.get('CurrentMetrics') is not None:
            for k in m.get('CurrentMetrics'):
                temp_model = DescribeServiceAutoScalerResponseBodyCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k))
        if m.get('MaxReplica') is not None:
            self.max_replica = m.get('MaxReplica')
        if m.get('MinReplica') is not None:
            self.min_replica = m.get('MinReplica')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scale_strategies = []
        if m.get('ScaleStrategies') is not None:
            for k in m.get('ScaleStrategies'):
                temp_model = DescribeServiceAutoScalerResponseBodyScaleStrategies()
                self.scale_strategies.append(temp_model.from_map(k))
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeServiceAutoScalerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceAutoScalerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceCronScalerResponseBodyScaleJobs(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        last_probe_time: str = None,
        message: str = None,
        name: str = None,
        schedule: str = None,
        state: str = None,
        target_size: int = None,
    ):
        # The time when the most recent CronHPA job was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the most recent CronHPA job ran. The time is displayed in UTC.
        self.last_probe_time = last_probe_time
        # The returned message.
        self.message = message
        # The name of the CronHPA job.
        self.name = name
        # The cron expression that is used to configure the execution time of the CronHPA job.
        self.schedule = schedule
        # The status of the most recent CronHPA job.
        self.state = state
        # The number of instances that you expect to configure for the CronHPA job.
        self.target_size = target_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_probe_time is not None:
            result['LastProbeTime'] = self.last_probe_time
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.state is not None:
            result['State'] = self.state
        if self.target_size is not None:
            result['TargetSize'] = self.target_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastProbeTime') is not None:
            self.last_probe_time = m.get('LastProbeTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')
        return self


class DescribeServiceCronScalerResponseBody(TeaModel):
    def __init__(
        self,
        exclude_dates: List[str] = None,
        request_id: str = None,
        scale_jobs: List[DescribeServiceCronScalerResponseBodyScaleJobs] = None,
        service_name: str = None,
    ):
        # The points in time that are excluded when you schedule a CronHPA job. The points in time must be specified by using a cron expression.
        self.exclude_dates = exclude_dates
        # The request ID.
        self.request_id = request_id
        # The CronHPA jobs.
        self.scale_jobs = scale_jobs
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.scale_jobs:
            for k in self.scale_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_dates is not None:
            result['ExcludeDates'] = self.exclude_dates
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScaleJobs'] = []
        if self.scale_jobs is not None:
            for k in self.scale_jobs:
                result['ScaleJobs'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeDates') is not None:
            self.exclude_dates = m.get('ExcludeDates')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scale_jobs = []
        if m.get('ScaleJobs') is not None:
            for k in m.get('ScaleJobs'):
                temp_model = DescribeServiceCronScalerResponseBodyScaleJobs()
                self.scale_jobs.append(temp_model.from_map(k))
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class DescribeServiceCronScalerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceCronScalerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceDiagnosisResponseBodyDiagnosisList(TeaModel):
    def __init__(
        self,
        advices: List[str] = None,
        causes: List[str] = None,
        error: str = None,
    ):
        # The suggestions about how to handle the errors.
        self.advices = advices
        # The causes of the errors.
        self.causes = causes
        # The error message.
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advices is not None:
            result['Advices'] = self.advices
        if self.causes is not None:
            result['Causes'] = self.causes
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advices') is not None:
            self.advices = m.get('Advices')
        if m.get('Causes') is not None:
            self.causes = m.get('Causes')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        return self


class DescribeServiceDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        diagnosis_list: List[DescribeServiceDiagnosisResponseBodyDiagnosisList] = None,
        request_id: str = None,
    ):
        # The diagnostics list.
        self.diagnosis_list = diagnosis_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.diagnosis_list:
            for k in self.diagnosis_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiagnosisList'] = []
        if self.diagnosis_list is not None:
            for k in self.diagnosis_list:
                result['DiagnosisList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.diagnosis_list = []
        if m.get('DiagnosisList') is not None:
            for k in m.get('DiagnosisList'):
                temp_model = DescribeServiceDiagnosisResponseBodyDiagnosisList()
                self.diagnosis_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceDiagnosisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceEventRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event_type: str = None,
        instance_name: str = None,
        page_num: str = None,
        page_size: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. By default, the current point in time is the end of the time range to query.
        self.end_time = end_time
        # The event type. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.event_type = event_type
        # The instance name. For more information about how to obtain the instance name, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        self.instance_name = instance_name
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The beginning of the time range to query. The time must be in UTC. The default value is seven days ago.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeServiceEventResponseBodyEvents(TeaModel):
    def __init__(
        self,
        message: str = None,
        reason: str = None,
        time: str = None,
        type: str = None,
    ):
        # The returned message. The message is formatted and returned in the JSON format.
        self.message = message
        # The cause of the event. The information about the change in the service status is returned.
        self.reason = reason
        # The time when the event occurred. The time must be in UTC.
        self.time = time
        # The event type. Valid values:
        # 
        # *   Normal
        # *   Warning
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeServiceEventResponseBody(TeaModel):
    def __init__(
        self,
        events: List[DescribeServiceEventResponseBodyEvents] = None,
        page_num: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page_num: int = None,
    ):
        # The events.
        self.events = events
        # The page number.
        self.page_num = page_num
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The total number of pages returned.
        self.total_page_num = total_page_num

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeServiceEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class DescribeServiceEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceEventResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceInstanceDiagnosisResponseBodyDiagnosis(TeaModel):
    def __init__(
        self,
        advices: List[str] = None,
        causes: List[str] = None,
        error: str = None,
    ):
        # The solutions to the errors.
        self.advices = advices
        # The causes of the errors.
        self.causes = causes
        # The error message.
        self.error = error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advices is not None:
            result['Advices'] = self.advices
        if self.causes is not None:
            result['Causes'] = self.causes
        if self.error is not None:
            result['Error'] = self.error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advices') is not None:
            self.advices = m.get('Advices')
        if m.get('Causes') is not None:
            self.causes = m.get('Causes')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        return self


class DescribeServiceInstanceDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        diagnosis: DescribeServiceInstanceDiagnosisResponseBodyDiagnosis = None,
        request_id: str = None,
    ):
        # The diagnostics information.
        self.diagnosis = diagnosis
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.diagnosis:
            self.diagnosis.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnosis is not None:
            result['Diagnosis'] = self.diagnosis.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Diagnosis') is not None:
            temp_model = DescribeServiceInstanceDiagnosisResponseBodyDiagnosis()
            self.diagnosis = temp_model.from_map(m['Diagnosis'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeServiceInstanceDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceInstanceDiagnosisResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceInstanceDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceLogRequest(TeaModel):
    def __init__(
        self,
        container_name: str = None,
        end_time: str = None,
        instance_name: str = None,
        ip: str = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
        previous: bool = None,
        start_time: str = None,
    ):
        # The name of the container that runs the service.
        self.container_name = container_name
        # The end of the time range to query. The time must be in UTC.
        self.end_time = end_time
        # The name of the instance that runs the service. For more information about how to query the instance name, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        self.instance_name = instance_name
        # The IP address of the instance whose logs you want to query. For more information about how to query the IP address of an instance, see [ListServiceInstances](https://help.aliyun.com/document_detail/412108.html).
        self.ip = ip
        # The keyword that you use to query the logs of the service.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 500.
        self.page_size = page_size
        # Specifies whether to query the logs that are generated before the instance last restarts. This parameter is available only if the instance restarts.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.previous = previous
        # The beginning of the time range to query. The time must be in Coordinated Universal Time (UTC).
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.previous is not None:
            result['Previous'] = self.previous
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Previous') is not None:
            self.previous = m.get('Previous')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeServiceLogResponseBody(TeaModel):
    def __init__(
        self,
        logs: List[str] = None,
        page_num: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page_num: int = None,
    ):
        # The returned logs.
        self.logs = logs
        # The page number.
        self.page_num = page_num
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The total number of pages returned.
        self.total_page_num = total_page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['Logs'] = self.logs
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')
        return self


class DescribeServiceLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMirrorResponseBody(TeaModel):
    def __init__(
        self,
        ratio: str = None,
        request_id: str = None,
        service_name: str = None,
        target: str = None,
    ):
        # The percentage of traffic that you want to mirror. Valid values: 0 to 100.
        self.ratio = ratio
        # The request ID.
        self.request_id = request_id
        # The service name.
        self.service_name = service_name
        # The destination services to which you want to mirror traffic.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class DescribeServiceMirrorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceMirrorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpotDiscountHistoryRequest(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        is_protect: bool = None,
    ):
        # The type of the Elastic Algorithm Service (EAS) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Specifies whether the preemptible instance has a protection period. During the 1-hour protection period of the preemptible instance, the preemptible instance will not be released.
        self.is_protect = is_protect

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_protect is not None:
            result['IsProtect'] = self.is_protect
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsProtect') is not None:
            self.is_protect = m.get('IsProtect')
        return self


class DescribeSpotDiscountHistoryResponseBodySpotDiscounts(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_discount: str = None,
        timestamp: str = None,
        zone_id: str = None,
    ):
        # The type of the ECS instance.
        self.instance_type = instance_type
        # The discount for the preemptible instance. For example, 0.1 represents a 90% discount.
        self.spot_discount = spot_discount
        # The time when the discount is available. The time must be in UTC.
        self.timestamp = timestamp
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.spot_discount is not None:
            result['SpotDiscount'] = self.spot_discount
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('SpotDiscount') is not None:
            self.spot_discount = m.get('SpotDiscount')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeSpotDiscountHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spot_discounts: List[DescribeSpotDiscountHistoryResponseBodySpotDiscounts] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The discount for the preemptible instance.
        self.spot_discounts = spot_discounts

    def validate(self):
        if self.spot_discounts:
            for k in self.spot_discounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SpotDiscounts'] = []
        if self.spot_discounts is not None:
            for k in self.spot_discounts:
                result['SpotDiscounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spot_discounts = []
        if m.get('SpotDiscounts') is not None:
            for k in m.get('SpotDiscounts'):
                temp_model = DescribeSpotDiscountHistoryResponseBodySpotDiscounts()
                self.spot_discounts.append(temp_model.from_map(k))
        return self


class DescribeSpotDiscountHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSpotDiscountHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSpotDiscountHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DevelopServiceRequest(TeaModel):
    def __init__(
        self,
        exit: str = None,
    ):
        # Specifies whether to exit development mode. Valid values:
        # 
        # *   true: exits development mode.
        # *   false (default): enters development mode.
        self.exit = exit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exit is not None:
            result['Exit'] = self.exit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exit') is not None:
            self.exit = m.get('Exit')
        return self


class DevelopServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DevelopServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DevelopServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DevelopServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclPolicyRequest(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListAclPolicyResponseBodyInternetAclPolicyList(TeaModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        self.comment = comment
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class ListAclPolicyResponseBodyIntranetVpcAclPolicyListIntranetAclPolicyList(TeaModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        self.comment = comment
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class ListAclPolicyResponseBodyIntranetVpcAclPolicyList(TeaModel):
    def __init__(
        self,
        intranet_acl_policy_list: List[ListAclPolicyResponseBodyIntranetVpcAclPolicyListIntranetAclPolicyList] = None,
        vpc_id: str = None,
    ):
        self.intranet_acl_policy_list = intranet_acl_policy_list
        self.vpc_id = vpc_id

    def validate(self):
        if self.intranet_acl_policy_list:
            for k in self.intranet_acl_policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IntranetAclPolicyList'] = []
        if self.intranet_acl_policy_list is not None:
            for k in self.intranet_acl_policy_list:
                result['IntranetAclPolicyList'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.intranet_acl_policy_list = []
        if m.get('IntranetAclPolicyList') is not None:
            for k in m.get('IntranetAclPolicyList'):
                temp_model = ListAclPolicyResponseBodyIntranetVpcAclPolicyListIntranetAclPolicyList()
                self.intranet_acl_policy_list.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListAclPolicyResponseBody(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        internet_acl_policy_list: List[ListAclPolicyResponseBodyInternetAclPolicyList] = None,
        intranet_vpc_acl_policy_list: List[ListAclPolicyResponseBodyIntranetVpcAclPolicyList] = None,
        request_id: str = None,
    ):
        self.gateway_id = gateway_id
        self.internet_acl_policy_list = internet_acl_policy_list
        self.intranet_vpc_acl_policy_list = intranet_vpc_acl_policy_list
        self.request_id = request_id

    def validate(self):
        if self.internet_acl_policy_list:
            for k in self.internet_acl_policy_list:
                if k:
                    k.validate()
        if self.intranet_vpc_acl_policy_list:
            for k in self.intranet_vpc_acl_policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        result['InternetAclPolicyList'] = []
        if self.internet_acl_policy_list is not None:
            for k in self.internet_acl_policy_list:
                result['InternetAclPolicyList'].append(k.to_map() if k else None)
        result['IntranetVpcAclPolicyList'] = []
        if self.intranet_vpc_acl_policy_list is not None:
            for k in self.intranet_vpc_acl_policy_list:
                result['IntranetVpcAclPolicyList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        self.internet_acl_policy_list = []
        if m.get('InternetAclPolicyList') is not None:
            for k in m.get('InternetAclPolicyList'):
                temp_model = ListAclPolicyResponseBodyInternetAclPolicyList()
                self.internet_acl_policy_list.append(temp_model.from_map(k))
        self.intranet_vpc_acl_policy_list = []
        if m.get('IntranetVpcAclPolicyList') is not None:
            for k in m.get('IntranetVpcAclPolicyList'):
                temp_model = ListAclPolicyResponseBodyIntranetVpcAclPolicyList()
                self.intranet_vpc_acl_policy_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAclPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAclPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBenchmarkTaskRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: str = None,
        page_size: str = None,
        service_name: str = None,
    ):
        # The keyword used to query required stress testing tasks. If this parameter is specified, the system returns stress testing tasks based on the names of the stress testing tasks in the matched Elastic Algorithm Service (EAS).
        self.filter = filter
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The name of the EAS service that corresponds to the stress testing task. For more information about how to query the service name, see [ListServices](https://help.aliyun.com/document_detail/412109.html).
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListBenchmarkTaskResponseBodyTasks(TeaModel):
    def __init__(
        self,
        available_agent: int = None,
        create_time: str = None,
        message: str = None,
        region: str = None,
        service_name: str = None,
        status: str = None,
        task_id: str = None,
        task_name: str = None,
        update_time: str = None,
    ):
        # The number of instances that are available for stress testing.
        self.available_agent = available_agent
        # The time when the stress testing task was created.
        self.create_time = create_time
        # The returned message.
        self.message = message
        # The region ID of the stress testing task.
        self.region = region
        # The name of the service on which you want to perform a stress testing.
        self.service_name = service_name
        # The state of the stress testing task.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Starting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DeleteFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopping
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Error
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Updating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CreateFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status
        # The ID of the stress testing task.
        self.task_id = task_id
        # The name of the stress testing task.
        self.task_name = task_name
        # The time when the stress testing task was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_agent is not None:
            result['AvailableAgent'] = self.available_agent
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.message is not None:
            result['Message'] = self.message
        if self.region is not None:
            result['Region'] = self.region
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableAgent') is not None:
            self.available_agent = m.get('AvailableAgent')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListBenchmarkTaskResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[ListBenchmarkTaskResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The stress testing tasks.
        self.tasks = tasks
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListBenchmarkTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListBenchmarkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBenchmarkTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_name = gateway_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGatewayResponseBodyGateways(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        instance_type: str = None,
        internet_domain: str = None,
        internet_enabled: bool = None,
        intranet_domain: str = None,
        is_default: bool = None,
        replicas: int = None,
        status: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.gateway_id = gateway_id
        self.gateway_name = gateway_name
        self.instance_type = instance_type
        self.internet_domain = internet_domain
        self.internet_enabled = internet_enabled
        self.intranet_domain = intranet_domain
        self.is_default = is_default
        self.replicas = replicas
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain
        if self.internet_enabled is not None:
            result['InternetEnabled'] = self.internet_enabled
        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')
        if m.get('InternetEnabled') is not None:
            self.internet_enabled = m.get('InternetEnabled')
        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListGatewayResponseBody(TeaModel):
    def __init__(
        self,
        gateways: List[ListGatewayResponseBodyGateways] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.gateways = gateways
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.gateways:
            for k in self.gateways:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Gateways'] = []
        if self.gateways is not None:
            for k in self.gateways:
                result['Gateways'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateways = []
        if m.get('Gateways') is not None:
            for k in m.get('Gateways'):
                temp_model = ListGatewayResponseBodyGateways()
                self.gateways.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGatewayIntranetLinkedVpcResponseBodyIntranetLinkedVpcList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        security_group_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The IP address.
        self.ip = ip
        # The security group ID.
        self.security_group_id = security_group_id
        # The state of the private gateway.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The private gateway is being created.
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The private gateway is running.
        # 
        #     <!-- -->
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListGatewayIntranetLinkedVpcResponseBody(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        intranet_linked_vpc_list: List[ListGatewayIntranetLinkedVpcResponseBodyIntranetLinkedVpcList] = None,
        request_id: str = None,
    ):
        # The private gateway ID.
        self.gateway_id = gateway_id
        # The internal endpoints.
        self.intranet_linked_vpc_list = intranet_linked_vpc_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.intranet_linked_vpc_list:
            for k in self.intranet_linked_vpc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        result['IntranetLinkedVpcList'] = []
        if self.intranet_linked_vpc_list is not None:
            for k in self.intranet_linked_vpc_list:
                result['IntranetLinkedVpcList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        self.intranet_linked_vpc_list = []
        if m.get('IntranetLinkedVpcList') is not None:
            for k in m.get('IntranetLinkedVpcList'):
                temp_model = ListGatewayIntranetLinkedVpcResponseBodyIntranetLinkedVpcList()
                self.intranet_linked_vpc_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGatewayIntranetLinkedVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGatewayIntranetLinkedVpcResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGatewayIntranetLinkedVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupsRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        page_number: str = None,
        page_size: str = None,
        workspace_id: str = None,
    ):
        # The name of the filter that is used to filter out unwanted service groups. Fuzzy match is supported.
        self.filter = filter
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListGroupsResponseBody(TeaModel):
    def __init__(
        self,
        groups: List[Group] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The service groups.
        self.groups = groups
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = Group()
                self.groups.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceInstanceWorkerRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListResourceInstanceWorkerResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        pods: List[ResourceInstanceWorker] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The workers.
        self.pods = pods
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.pods:
            for k in self.pods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Pods'] = []
        if self.pods is not None:
            for k in self.pods:
                result['Pods'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.pods = []
        if m.get('Pods') is not None:
            for k in m.get('Pods'):
                temp_model = ResourceInstanceWorker()
                self.pods.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceInstanceWorkerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceInstanceWorkerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceInstanceWorkerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceInstancesRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        filter: str = None,
        instance_ip: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort: str = None,
    ):
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription.
        # *   PostPaid: pay-as-you-go.
        self.charge_type = charge_type
        # The keyword used to query instances. Instances can be queried by instance ID or instance IP address.
        self.filter = filter
        # The IP address of the instance.
        self.instance_ip = instance_ip
        # The instance ID. For more information about how to query the instance ID, see [ListResourceInstances](https://help.aliyun.com/document_detail/412129.html).
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The instance state.
        # 
        # Valid values:
        # 
        # *   Ready-SchedulingDisabled
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance is available but unschedulable
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Ready
        # 
        #     <!-- -->
        # 
        #     : The instance
        # 
        #     <!-- -->
        # 
        #     is running
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   NotReady
        # 
        #     <!-- -->
        # 
        #     : The instance is unready.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopped
        # 
        #     <!-- -->
        # 
        #     : The instance has stopped.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   NotReady-SchedulingDisabled
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instance is unavailable and unschedulable
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Attaching
        # 
        #     <!-- -->
        # 
        #     : The instance
        # 
        #     <!-- -->
        # 
        #     is starting
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     : The instance is being deleted.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CreateFailed: The instance failed to be created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.instance_status = instance_status
        # The sorting order.
        # 
        # Valid values:
        # 
        # *   asc: The instances are sorted in ascending order.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   desc
        # 
        #     <!-- -->
        # 
        #     : The instances are sorted in descending order.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.order = order
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The field that you use to sort the query results.
        # 
        # Valid values:
        # 
        # *   CreateTime
        # 
        #     <!-- -->
        # 
        #     : The instances are sorted based on the time when the instances were created.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MemoryUsed
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instances are sorted based on the memory usage of the instances
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   GpuUsed
        # 
        #     <!-- -->
        # 
        #     : The instances are sorted based on the
        # 
        #     <!-- -->
        # 
        #     GPU usage of the instances.
        # 
        #     <!-- -->
        # 
        # *   ExpireTime: The instances are sorted based on the time when the instances expired.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CpuUsed
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     The instances are sorted based on the CPU utilization of the instances.
        # 
        #     <!-- -->
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_ip is not None:
            result['InstanceIP'] = self.instance_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceIP') is not None:
            self.instance_ip = m.get('InstanceIP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListResourceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ResourceInstance] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The instances.
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ResourceInstance()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceServicesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListResourceServicesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        services: List[Service] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The services.
        self.services = services
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = Service()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourceServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The ID of the resource group. You can call the [CreateResource](https://help.aliyun.com/document_detail/412111.html) operation to query the ID of the resource group.
        self.resource_id = resource_id
        # The name of the resource group. You can call the [CreateResource](https://help.aliyun.com/document_detail/412111.html) operation to query the name of the resource group.
        self.resource_name = resource_name
        # The type of the resource group. Valid values:
        # 
        # *   Dedicated: the dedicated resource group.
        # *   SelfManaged: the self-managed resource group.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resources: List[Resource] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The resource groups.
        self.resources = resources
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = Resource()
                self.resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceContainersResponseBody(TeaModel):
    def __init__(
        self,
        containers: List[ContainerInfo] = None,
        request_id: str = None,
        service_name: str = None,
    ):
        # The containers of the service.
        self.containers = containers
        # The request ID.
        self.request_id = request_id
        # The service name.
        self.service_name = service_name

    def validate(self):
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = ContainerInfo()
                self.containers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListServiceContainersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceContainersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceContainersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        host_ip: str = None,
        instance_ip: str = None,
        instance_name: str = None,
        instance_status: str = None,
        instance_type: str = None,
        is_spot: bool = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_type: str = None,
        role: str = None,
        sort: str = None,
    ):
        # The keyword used to query instances. Instances can be queried based on instance name, instance IP address, IP address of the server where the instance resides, and instance type.
        self.filter = filter
        # The IP address of the server where the instance resides.
        self.host_ip = host_ip
        # The IP address of the instance.
        self.instance_ip = instance_ip
        # The instance name.
        self.instance_name = instance_name
        # The instance state.
        self.instance_status = instance_status
        # The instance type.
        self.instance_type = instance_type
        # Specifies whether the instance is a preemptible instance.
        self.is_spot = is_spot
        # The sorting order.
        # 
        # Valid values:
        # 
        # *   asc
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     The instances are sorted in ascending order.
        # 
        # *   desc
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     The instances are sorted in descending order.
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The type of the resource group to which the instance belongs.
        # 
        # Valid values:
        # 
        # *   PublicResource
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DedicatedResource
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.resource_type = resource_type
        # The service role.
        # 
        # Valid values:
        # 
        # *   DataSet
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     dataset service
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   SDProxy
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Stable-Diffusion proxy service
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     standard service
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   Queue
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     queue service
        # 
        #     <!-- -->
        # 
        #     .
        self.role = role
        # The field that you use to sort the query results.
        # 
        # *   Set the value to StartTime.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     The value specifies that the query results are sorted based on the time when the instances were created
        # 
        #     <!-- -->
        # 
        #     .
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.host_ip is not None:
            result['HostIP'] = self.host_ip
        if self.instance_ip is not None:
            result['InstanceIP'] = self.instance_ip
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_spot is not None:
            result['IsSpot'] = self.is_spot
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.role is not None:
            result['Role'] = self.role
        if self.sort is not None:
            result['Sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('HostIP') is not None:
            self.host_ip = m.get('HostIP')
        if m.get('InstanceIP') is not None:
            self.instance_ip = m.get('InstanceIP')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsSpot') is not None:
            self.is_spot = m.get('IsSpot')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        return self


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[Instance] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The instances.
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = Instance()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceVersionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListServiceVersionsResponseBodyVersions(TeaModel):
    def __init__(
        self,
        build_time: str = None,
        image_available: str = None,
        image_id: int = None,
        message: str = None,
        service_config: str = None,
        service_runnable: str = None,
    ):
        # The time when the service version was created. The time is displayed in UTC.
        self.build_time = build_time
        # Indicates whether the image is available. Valid values:
        # 
        # *   true: The image is available.
        # *   false: The image is unavailable.
        # *   unknown: The availability of the image is unknown.
        self.image_available = image_available
        # The image ID.
        self.image_id = image_id
        # The returned message.
        self.message = message
        # The service deployment configurations. This parameter is returned only if the service is deployed by using a custom image.
        self.service_config = service_config
        # Indicates whether Elastic Algorithm service (EAS) is activated. Valid values:
        # 
        # *   true: EAS is activated.
        # *   false: EAS is not activated.
        # *   unknown: The activation of EAS is unknown.
        self.service_runnable = service_runnable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_time is not None:
            result['BuildTime'] = self.build_time
        if self.image_available is not None:
            result['ImageAvailable'] = self.image_available
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.message is not None:
            result['Message'] = self.message
        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config
        if self.service_runnable is not None:
            result['ServiceRunnable'] = self.service_runnable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTime') is not None:
            self.build_time = m.get('BuildTime')
        if m.get('ImageAvailable') is not None:
            self.image_available = m.get('ImageAvailable')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')
        if m.get('ServiceRunnable') is not None:
            self.service_runnable = m.get('ServiceRunnable')
        return self


class ListServiceVersionsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        versions: List[ListServiceVersionsResponseBodyVersions] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The historical versions of the service.
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListServiceVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListServiceVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServiceVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        gateway: str = None,
        group_name: str = None,
        label: Dict[str, str] = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_service_uid: str = None,
        quota_id: str = None,
        resource_name: str = None,
        service_name: str = None,
        service_status: str = None,
        service_type: str = None,
        service_uid: str = None,
        sort: str = None,
        workspace_id: str = None,
    ):
        # The field that is used for fuzzy matches. The system performs fuzzy matches only by service name.
        self.filter = filter
        # The ID of the private gateway.
        self.gateway = gateway
        # The name of the service group. For more information about how to query the name of a service group, see [ListServices](https://help.aliyun.com/document_detail/412109.html).
        self.group_name = group_name
        # The tag that is used to filter services.
        self.label = label
        # The sorting order. Valid values:
        # 
        # *   desc (default): The query results are sorted in descending order.
        # *   asc: The query results are sorted in ascending order.
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The ID of the primary service that corresponds to the Band member service.
        self.parent_service_uid = parent_service_uid
        # The quota ID.
        self.quota_id = quota_id
        # The name or ID of the resource group to which the service belongs.
        self.resource_name = resource_name
        # The service name.
        self.service_name = service_name
        # The service state.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopped
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Failed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Complete
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Cloning
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopping
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Updating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Waiting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   HotUpdate
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Committing
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Starting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DeleteFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Developing
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Scaling
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleted
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Pending
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.service_status = service_status
        # The service type. Valid values:
        # 
        # *   Async
        # *   Standard
        # *   Offline Task
        # *   Proxima
        # 
        # Valid values:
        # 
        # *   Async
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   OfflineTask
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Proxima
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.service_type = service_type
        # The user ID (UID) of the service.
        self.service_uid = service_uid
        # The sort field. By default, the query results are sorted by the timestamp type in descending order.
        self.sort = sort
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.gateway is not None:
            result['Gateway'] = self.gateway
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.label is not None:
            result['Label'] = self.label
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_service_uid is not None:
            result['ParentServiceUid'] = self.parent_service_uid
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.service_uid is not None:
            result['ServiceUid'] = self.service_uid
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentServiceUid') is not None:
            self.parent_service_uid = m.get('ParentServiceUid')
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ServiceUid') is not None:
            self.service_uid = m.get('ServiceUid')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListServicesShrinkRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        gateway: str = None,
        group_name: str = None,
        label_shrink: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_service_uid: str = None,
        quota_id: str = None,
        resource_name: str = None,
        service_name: str = None,
        service_status: str = None,
        service_type: str = None,
        service_uid: str = None,
        sort: str = None,
        workspace_id: str = None,
    ):
        # The field that is used for fuzzy matches. The system performs fuzzy matches only by service name.
        self.filter = filter
        # The ID of the private gateway.
        self.gateway = gateway
        # The name of the service group. For more information about how to query the name of a service group, see [ListServices](https://help.aliyun.com/document_detail/412109.html).
        self.group_name = group_name
        # The tag that is used to filter services.
        self.label_shrink = label_shrink
        # The sorting order. Valid values:
        # 
        # *   desc (default): The query results are sorted in descending order.
        # *   asc: The query results are sorted in ascending order.
        self.order = order
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The ID of the primary service that corresponds to the Band member service.
        self.parent_service_uid = parent_service_uid
        # The quota ID.
        self.quota_id = quota_id
        # The name or ID of the resource group to which the service belongs.
        self.resource_name = resource_name
        # The service name.
        self.service_name = service_name
        # The service state.
        # 
        # Valid values:
        # 
        # *   Creating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopped
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Failed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Complete
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Cloning
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Stopping
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Updating
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Waiting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   HotUpdate
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Committing
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Starting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DeleteFailed
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Running
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Developing
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Scaling
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleted
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Pending
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Deleting
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.service_status = service_status
        # The service type. Valid values:
        # 
        # *   Async
        # *   Standard
        # *   Offline Task
        # *   Proxima
        # 
        # Valid values:
        # 
        # *   Async
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Standard
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   OfflineTask
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Proxima
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.service_type = service_type
        # The user ID (UID) of the service.
        self.service_uid = service_uid
        # The sort field. By default, the query results are sorted by the timestamp type in descending order.
        self.sort = sort
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.gateway is not None:
            result['Gateway'] = self.gateway
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.label_shrink is not None:
            result['Label'] = self.label_shrink
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_service_uid is not None:
            result['ParentServiceUid'] = self.parent_service_uid
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.service_uid is not None:
            result['ServiceUid'] = self.service_uid
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Label') is not None:
            self.label_shrink = m.get('Label')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentServiceUid') is not None:
            self.parent_service_uid = m.get('ParentServiceUid')
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ServiceUid') is not None:
            self.service_uid = m.get('ServiceUid')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        services: List[Service] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The services.
        self.services = services
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = Service()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantAddonsResponseBodyAddons(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        name: str = None,
    ):
        self.attributes = attributes
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListTenantAddonsResponseBody(TeaModel):
    def __init__(
        self,
        addons: List[ListTenantAddonsResponseBodyAddons] = None,
        request_id: str = None,
    ):
        self.addons = addons
        self.request_id = request_id

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['Addons'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addons = []
        if m.get('Addons') is not None:
            for k in m.get('Addons'):
                temp_model = ListTenantAddonsResponseBodyAddons()
                self.addons.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTenantAddonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTenantAddonsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTenantAddonsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReinstallTenantAddonResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReinstallTenantAddonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReinstallTenantAddonResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReinstallTenantAddonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseServiceRequest(TeaModel):
    def __init__(
        self,
        traffic_state: str = None,
        weight: int = None,
    ):
        # The traffic state. Valid values:
        # 
        # *   standalone: independent traffic.
        # *   grouping: grouped traffic.
        self.traffic_state = traffic_state
        # The weight of the canary release. Valid values: 0 to 100.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.traffic_state is not None:
            result['TrafficState'] = self.traffic_state
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficState') is not None:
            self.traffic_state = m.get('TrafficState')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class ReleaseServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RestartServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBenchmarkTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartBenchmarkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartBenchmarkTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBenchmarkTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopBenchmarkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopBenchmarkTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppServiceRequest(TeaModel):
    def __init__(
        self,
        quota_id: str = None,
        workspace_id: str = None,
        app_type: str = None,
        app_version: str = None,
        config: Dict[str, Any] = None,
        replicas: int = None,
        service_spec: str = None,
    ):
        # The quota ID.
        self.quota_id = quota_id
        # The workspace ID.
        self.workspace_id = workspace_id
        # The application type.
        # 
        # Valid values:
        # 
        # *   LLM: the large language model (LLM) application
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.app_type = app_type
        # The application version.
        self.app_version = app_version
        # The additional configurations that are required for service deployment.
        self.config = config
        # The number of instances. This value must be greater than 0.
        self.replicas = replicas
        # The service specifications. Valid values:
        # 
        # *   llama_7b_fp16
        # *   llama_7b_int8
        # *   llama_13b_fp16
        # *   llama_7b_int8
        # *   chatglm_6b_fp16
        # *   chatglm_6b_int8
        # *   chatglm2_6b_fp16
        # *   baichuan_7b_int8
        # *   baichuan_13b_fp16
        # *   baichuan_7b_fp16
        self.service_spec = service_spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.config is not None:
            result['Config'] = self.config
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('ServiceSpec') is not None:
            self.service_spec = m.get('ServiceSpec')
        return self


class UpdateAppServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateAppServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBenchmarkTaskRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
    ):
        # The request body. The body includes the parameters that are set to create a stress testing task. For more information, see **Table 1. Fields in the base parameter**.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateBenchmarkTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBenchmarkTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBenchmarkTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateBenchmarkTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGatewayRequest(TeaModel):
    def __init__(
        self,
        enable_internet: bool = None,
        enable_intranet: bool = None,
        instance_type: str = None,
        is_default: bool = None,
        name: str = None,
        replicas: int = None,
    ):
        # Specifies whether to enable Internet access. Default value: false.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_internet = enable_internet
        # Specifies whether to enable internal network access. Default value: true.
        self.enable_intranet = enable_intranet
        # The instance type used for the private gateway.
        self.instance_type = instance_type
        self.is_default = is_default
        # The private gateway alias.
        self.name = name
        self.replicas = replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_internet is not None:
            result['EnableInternet'] = self.enable_internet
        if self.enable_intranet is not None:
            result['EnableIntranet'] = self.enable_intranet
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInternet') is not None:
            self.enable_internet = m.get('EnableInternet')
        if m.get('EnableIntranet') is not None:
            self.enable_intranet = m.get('EnableIntranet')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        return self


class UpdateGatewayResponseBody(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGatewayResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequestSelfManagedResourceOptionsNodeTolerations(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The effect.
        # Valid values:
        # - PreferNoSchedule
        # - NoSchedule
        # - NoExecute
        self.effect = effect
        # The key name.
        self.key = key
        # Relationship between key names and key values.
        # Valid values:
        # - Equal
        # - Exists
        self.operator = operator
        # The key value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateResourceRequestSelfManagedResourceOptions(TeaModel):
    def __init__(
        self,
        node_match_labels: Dict[str, str] = None,
        node_tolerations: List[UpdateResourceRequestSelfManagedResourceOptionsNodeTolerations] = None,
    ):
        # Tag tag key-value pairs for nodes.
        self.node_match_labels = node_match_labels
        # Tolerations for nodes.
        self.node_tolerations = node_tolerations

    def validate(self):
        if self.node_tolerations:
            for k in self.node_tolerations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_match_labels is not None:
            result['NodeMatchLabels'] = self.node_match_labels
        result['NodeTolerations'] = []
        if self.node_tolerations is not None:
            for k in self.node_tolerations:
                result['NodeTolerations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeMatchLabels') is not None:
            self.node_match_labels = m.get('NodeMatchLabels')
        self.node_tolerations = []
        if m.get('NodeTolerations') is not None:
            for k in m.get('NodeTolerations'):
                temp_model = UpdateResourceRequestSelfManagedResourceOptionsNodeTolerations()
                self.node_tolerations.append(temp_model.from_map(k))
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(
        self,
        resource_name: str = None,
        self_managed_resource_options: UpdateResourceRequestSelfManagedResourceOptions = None,
    ):
        # The new name of the resource group after the update. The name can be up to 27 characters in length.
        self.resource_name = resource_name
        # The configuration items of the self-managed resource group.
        self.self_managed_resource_options = self_managed_resource_options

    def validate(self):
        if self.self_managed_resource_options:
            self.self_managed_resource_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.self_managed_resource_options is not None:
            result['SelfManagedResourceOptions'] = self.self_managed_resource_options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('SelfManagedResourceOptions') is not None:
            temp_model = UpdateResourceRequestSelfManagedResourceOptions()
            self.self_managed_resource_options = temp_model.from_map(m['SelfManagedResourceOptions'])
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_id = resource_id
        # The name of the resource group.
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceDLinkRequest(TeaModel):
    def __init__(
        self,
        destination_cidrs: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        v_switch_id_list: List[str] = None,
    ):
        # The CIDR blocks of the clients that you want to connect to. After this parameter is specified, the CIDR blocks are added to the back-to-origin route of the server. Either this parameter or the VSwitchIdList parameter can be used to determine CIDR blocks.
        self.destination_cidrs = destination_cidrs
        # The ID of the security group to which the Elastic Compute Service (ECS) instance belongs.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The ID of the peer primary vSwitch. After this parameter is specified, an elastic network interface (ENI) is created in the VSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The vSwitches of the clients that you want to connect to. After this parameter is specified, the CIDR blocks of these vSwitches are added to the back-to-origin route of the server.
        self.v_switch_id_list = v_switch_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidrs is not None:
            result['DestinationCIDRs'] = self.destination_cidrs
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_id_list is not None:
            result['VSwitchIdList'] = self.v_switch_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCIDRs') is not None:
            self.destination_cidrs = m.get('DestinationCIDRs')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')
        return self


class UpdateResourceDLinkResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateResourceDLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceDLinkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceDLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceInstanceRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
    ):
        # The operation that updates the scheduling state of the instance in a dedicated resource group. Valid values:
        # 
        # *   Uncordon: allows scheduling the service to this instance.
        # *   Cordon: prohibits scheduling the service to this instance.
        # *   Drain: evicts the service that has been scheduled to this instance.
        # 
        # This parameter is required.
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        return self


class UpdateResourceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        request_id: str = None,
        resource_id: str = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class UpdateResourceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        update_type: str = None,
        body: str = None,
    ):
        # The type of the service update. Valid values: merge and replace. By default, merge is used if you do not specify this parameter.
        # 
        # *   merge: If the JSON string configured for the existing service is `{"a":"b"}` and the JSON string specified in the body parameter is `{"c":"d"}`, the JSON string is `{"a":"b","c":"d"}` after the service update.
        # *   replace: If the JSON string configured for the existing service is `{"a":"b"}` and the JSON string specified in the body parameter is `{"c":"d"}`, the JSON string is `{"c":"d"}` after the service update.
        self.update_type = update_type
        # The request body. The body includes the request parameters that you want to update. For more information about the request parameters, see [CreateService](https://help.aliyun.com/document_detail/412086.html).
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_type is not None:
            result['UpdateType'] = self.update_type
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceAutoScalerRequestBehaviorOnZero(TeaModel):
    def __init__(
        self,
        scale_down_grace_period_seconds: int = None,
        scale_up_activation_replicas: int = None,
    ):
        # The time window that is required before the number of instances is reduced to 0. Default value: 600. The number of instances can be reduced to 0 only if no request is available or no traffic exists in the specified time window.
        self.scale_down_grace_period_seconds = scale_down_grace_period_seconds
        # The number of instances that you want to create at a time if the number of instances is scaled out from 0. Default value: 1.
        self.scale_up_activation_replicas = scale_up_activation_replicas

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_down_grace_period_seconds is not None:
            result['scaleDownGracePeriodSeconds'] = self.scale_down_grace_period_seconds
        if self.scale_up_activation_replicas is not None:
            result['scaleUpActivationReplicas'] = self.scale_up_activation_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleDownGracePeriodSeconds') is not None:
            self.scale_down_grace_period_seconds = m.get('scaleDownGracePeriodSeconds')
        if m.get('scaleUpActivationReplicas') is not None:
            self.scale_up_activation_replicas = m.get('scaleUpActivationReplicas')
        return self


class UpdateServiceAutoScalerRequestBehaviorScaleDown(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
    ):
        # The time window that is required before the scale-in operation is performed. Default value: 300. The scale-in operation can be performed only if the specified metric drops below the threshold in the specified time window.
        self.stabilization_window_seconds = stabilization_window_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        return self


class UpdateServiceAutoScalerRequestBehaviorScaleUp(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
    ):
        # The time window that is required before the scale-out operation is performed. Default value: 0. The scale-out operation can be performed only if the specified metric exceeds the specified threshold in the specified time window.
        self.stabilization_window_seconds = stabilization_window_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        return self


class UpdateServiceAutoScalerRequestBehavior(TeaModel):
    def __init__(
        self,
        on_zero: UpdateServiceAutoScalerRequestBehaviorOnZero = None,
        scale_down: UpdateServiceAutoScalerRequestBehaviorScaleDown = None,
        scale_up: UpdateServiceAutoScalerRequestBehaviorScaleUp = None,
    ):
        # The operation that reduces the number of instances to 0.
        self.on_zero = on_zero
        # The scale-in operation.
        self.scale_down = scale_down
        # The scale-out operation.
        self.scale_up = scale_up

    def validate(self):
        if self.on_zero:
            self.on_zero.validate()
        if self.scale_down:
            self.scale_down.validate()
        if self.scale_up:
            self.scale_up.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.on_zero is not None:
            result['onZero'] = self.on_zero.to_map()
        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down.to_map()
        if self.scale_up is not None:
            result['scaleUp'] = self.scale_up.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('onZero') is not None:
            temp_model = UpdateServiceAutoScalerRequestBehaviorOnZero()
            self.on_zero = temp_model.from_map(m['onZero'])
        if m.get('scaleDown') is not None:
            temp_model = UpdateServiceAutoScalerRequestBehaviorScaleDown()
            self.scale_down = temp_model.from_map(m['scaleDown'])
        if m.get('scaleUp') is not None:
            temp_model = UpdateServiceAutoScalerRequestBehaviorScaleUp()
            self.scale_up = temp_model.from_map(m['scaleUp'])
        return self


class UpdateServiceAutoScalerRequestScaleStrategies(TeaModel):
    def __init__(
        self,
        metric_name: str = None,
        service: str = None,
        threshold: float = None,
    ):
        # The name of the metric for triggering auto scaling. Valid values:
        # 
        # *   qps: the queries per second (QPS) for an individual instance.
        # *   cpu: the CPU utilization.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The service for which the metric is specified. If you do not set this parameter, the current service is specified by default.
        self.service = service
        # The threshold of the metric that triggers auto scaling.
        # 
        # *   If you set metricName to QPS, scale-out is triggered when the average QPS for a single instance is greater than this threshold.
        # *   If you set metricName to CPU, scale-out is triggered when the average CPU utilization for a single instance is greater than this threshold.
        # 
        # This parameter is required.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.service is not None:
            result['service'] = self.service
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class UpdateServiceAutoScalerRequest(TeaModel):
    def __init__(
        self,
        behavior: UpdateServiceAutoScalerRequestBehavior = None,
        max: int = None,
        min: int = None,
        scale_strategies: List[UpdateServiceAutoScalerRequestScaleStrategies] = None,
    ):
        # The Autoscaler operation.
        self.behavior = behavior
        # The maximum number of instances. The value must be greater than that of the min parameter.
        # 
        # This parameter is required.
        self.max = max
        # The minimum number of instances. The value must be greater than 0.
        # 
        # This parameter is required.
        self.min = min
        # The auto scaling policies.
        # 
        # This parameter is required.
        self.scale_strategies = scale_strategies

    def validate(self):
        if self.behavior:
            self.behavior.validate()
        if self.scale_strategies:
            for k in self.scale_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.behavior is not None:
            result['behavior'] = self.behavior.to_map()
        if self.max is not None:
            result['max'] = self.max
        if self.min is not None:
            result['min'] = self.min
        result['scaleStrategies'] = []
        if self.scale_strategies is not None:
            for k in self.scale_strategies:
                result['scaleStrategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('behavior') is not None:
            temp_model = UpdateServiceAutoScalerRequestBehavior()
            self.behavior = temp_model.from_map(m['behavior'])
        if m.get('max') is not None:
            self.max = m.get('max')
        if m.get('min') is not None:
            self.min = m.get('min')
        self.scale_strategies = []
        if m.get('scaleStrategies') is not None:
            for k in m.get('scaleStrategies'):
                temp_model = UpdateServiceAutoScalerRequestScaleStrategies()
                self.scale_strategies.append(temp_model.from_map(k))
        return self


class UpdateServiceAutoScalerResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceAutoScalerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceAutoScalerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceAutoScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceCronScalerRequestScaleJobs(TeaModel):
    def __init__(
        self,
        name: str = None,
        schedule: str = None,
        target_size: int = None,
    ):
        # The name of the CronHPA job.
        self.name = name
        # The cron expression that is used to configure the execution time of the CronHPA job. For more information about how to configure cron expressions, see **Description of special characters** in this topic.
        # 
        # This parameter is required.
        self.schedule = schedule
        # The number of instances that you want to configure for the CronHPA job.
        # 
        # This parameter is required.
        self.target_size = target_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.schedule is not None:
            result['Schedule'] = self.schedule
        if self.target_size is not None:
            result['TargetSize'] = self.target_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')
        if m.get('TargetSize') is not None:
            self.target_size = m.get('TargetSize')
        return self


class UpdateServiceCronScalerRequest(TeaModel):
    def __init__(
        self,
        exclude_dates: List[str] = None,
        scale_jobs: List[UpdateServiceCronScalerRequestScaleJobs] = None,
    ):
        # The points in time that are excluded when you schedule a CronHPA job. The points in time must be specified by using a cron expression.
        self.exclude_dates = exclude_dates
        # The description of the CronHPA job.
        # 
        # This parameter is required.
        self.scale_jobs = scale_jobs

    def validate(self):
        if self.scale_jobs:
            for k in self.scale_jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_dates is not None:
            result['ExcludeDates'] = self.exclude_dates
        result['ScaleJobs'] = []
        if self.scale_jobs is not None:
            for k in self.scale_jobs:
                result['ScaleJobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeDates') is not None:
            self.exclude_dates = m.get('ExcludeDates')
        self.scale_jobs = []
        if m.get('ScaleJobs') is not None:
            for k in m.get('ScaleJobs'):
                temp_model = UpdateServiceCronScalerRequestScaleJobs()
                self.scale_jobs.append(temp_model.from_map(k))
        return self


class UpdateServiceCronScalerResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceCronScalerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceCronScalerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceCronScalerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        isolate: bool = None,
    ):
        # Specifies whether to isolate the service instance. Valid values:
        # 
        # *   true
        # *   false
        self.isolate = isolate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolate is not None:
            result['Isolate'] = self.isolate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Isolate') is not None:
            self.isolate = m.get('Isolate')
        return self


class UpdateServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceLabelRequest(TeaModel):
    def __init__(
        self,
        labels: Dict[str, str] = None,
    ):
        # The custom service tags.
        # 
        # This parameter is required.
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class UpdateServiceLabelResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceLabelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceMirrorRequest(TeaModel):
    def __init__(
        self,
        ratio: int = None,
        target: List[str] = None,
    ):
        # The percentage of traffic that you want to mirror. Valid values: 0 to 100.
        self.ratio = ratio
        # The service instances.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class UpdateServiceMirrorResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceMirrorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceMirrorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceMirrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceSafetyLockRequest(TeaModel):
    def __init__(
        self,
        lock: str = None,
    ):
        # The lock scope. Valid values:
        # 
        # *   all: locks all operations.
        # *   dangerous: locks dangerous operations such as delete and stop operations.
        # *   none: locks no operations.
        # 
        # This parameter is required.
        self.lock = lock

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock is not None:
            result['Lock'] = self.lock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lock') is not None:
            self.lock = m.get('Lock')
        return self


class UpdateServiceSafetyLockResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceSafetyLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceSafetyLockResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceSafetyLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceVersionRequest(TeaModel):
    def __init__(
        self,
        version: int = None,
    ):
        # The destination version of the service. The value must be of the INT type. The value must be greater than 0 and smaller than the current version of the service.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class UpdateServiceVersionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateServiceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


