# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class SetClusterDnatRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        nat_id: str = None,
        nat_eip: str = None,
    ):
        self.cluster_id = cluster_id
        self.nat_id = nat_id
        self.nat_eip = nat_eip

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.nat_id, 'nat_id')

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.nat_id is not None:
            result['NatId'] = self.nat_id
        if self.nat_eip is not None:
            result['NatEip'] = self.nat_eip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NatId') is not None:
            self.nat_id = m.get('NatId')
        if m.get('NatEip') is not None:
            self.nat_eip = m.get('NatEip')
        return self


class SetClusterDnatResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        already_exists: bool = None,
    ):
        self.request_id = request_id
        self.already_exists = already_exists

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.already_exists, 'already_exists')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.already_exists is not None:
            result['AlreadyExists'] = self.already_exists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AlreadyExists') is not None:
            self.already_exists = m.get('AlreadyExists')
        return self


class DescribeClusterConnectionsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        start_time: str = None,
        end_time: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.start_time = start_time
        self.end_time = end_time
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeClusterConnectionsResponseConnections(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        host_name: str = None,
        client_name: str = None,
        logon_time: str = None,
        logoff_time: str = None,
        logoff_status: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.host_name = host_name
        self.client_name = client_name
        self.logon_time = logon_time
        self.logoff_time = logoff_time
        self.logoff_status = logoff_status

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.host_name, 'host_name')
        self.validate_required(self.client_name, 'client_name')
        self.validate_required(self.logon_time, 'logon_time')
        self.validate_required(self.logoff_time, 'logoff_time')
        self.validate_required(self.logoff_status, 'logoff_status')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.client_name is not None:
            result['ClientName'] = self.client_name
        if self.logon_time is not None:
            result['LogonTime'] = self.logon_time
        if self.logoff_time is not None:
            result['LogoffTime'] = self.logoff_time
        if self.logoff_status is not None:
            result['LogoffStatus'] = self.logoff_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')
        if m.get('LogonTime') is not None:
            self.logon_time = m.get('LogonTime')
        if m.get('LogoffTime') is not None:
            self.logoff_time = m.get('LogoffTime')
        if m.get('LogoffStatus') is not None:
            self.logoff_status = m.get('LogoffStatus')
        return self


class DescribeClusterConnectionsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_finished: bool = None,
        task_id: str = None,
        total_count: int = None,
        connections: List[DescribeClusterConnectionsResponseConnections] = None,
    ):
        self.request_id = request_id
        self.task_finished = task_finished
        self.task_id = task_id
        self.total_count = total_count
        self.connections = connections

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_finished, 'task_finished')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.connections, 'connections')
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = DescribeClusterConnectionsResponseConnections()
                self.connections.append(temp_model.from_map(k))
        return self


class DescribeClusterADDomainRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeClusterADDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_supported: bool = None,
        task_finished: bool = None,
        task_id: str = None,
        domain_name: str = None,
        domain_dns_ip: str = None,
    ):
        self.request_id = request_id
        self.is_supported = is_supported
        self.task_finished = task_finished
        self.task_id = task_id
        self.domain_name = domain_name
        self.domain_dns_ip = domain_dns_ip

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_supported, 'is_supported')
        self.validate_required(self.task_finished, 'task_finished')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_dns_ip, 'domain_dns_ip')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_supported is not None:
            result['IsSupported'] = self.is_supported
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_dns_ip is not None:
            result['DomainDnsIp'] = self.domain_dns_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsSupported') is not None:
            self.is_supported = m.get('IsSupported')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainDnsIp') is not None:
            self.domain_dns_ip = m.get('DomainDnsIp')
        return self


class SetClusterADDomainRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        domain_dns_ip: str = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_admin: str = None,
        domain_delete: bool = None,
    ):
        self.cluster_id = cluster_id
        self.domain_dns_ip = domain_dns_ip
        self.domain_name = domain_name
        self.domain_password = domain_password
        self.domain_admin = domain_admin
        self.domain_delete = domain_delete

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.domain_dns_ip, 'domain_dns_ip')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_password, 'domain_password')

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.domain_dns_ip is not None:
            result['DomainDnsIp'] = self.domain_dns_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_admin is not None:
            result['DomainAdmin'] = self.domain_admin
        if self.domain_delete is not None:
            result['DomainDelete'] = self.domain_delete
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DomainDnsIp') is not None:
            self.domain_dns_ip = m.get('DomainDnsIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainAdmin') is not None:
            self.domain_admin = m.get('DomainAdmin')
        if m.get('DomainDelete') is not None:
            self.domain_delete = m.get('DomainDelete')
        return self


class SetClusterADDomainResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeInstancePolicyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
        async_mode: bool = None,
    ):
        self.instance_id = instance_id
        self.task_id = task_id
        self.async_mode = async_mode

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class DescribeInstancePolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        visual_lossless: str = None,
        optimize_for_3d: str = None,
        task_id: str = None,
        task_finished: bool = None,
    ):
        self.request_id = request_id
        self.visual_lossless = visual_lossless
        self.optimize_for_3d = optimize_for_3d
        self.task_id = task_id
        self.task_finished = task_finished

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.visual_lossless, 'visual_lossless')
        self.validate_required(self.optimize_for_3d, 'optimize_for_3d')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.task_finished, 'task_finished')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.visual_lossless is not None:
            result['VisualLossless'] = self.visual_lossless
        if self.optimize_for_3d is not None:
            result['OptimizeFor3d'] = self.optimize_for_3d
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VisualLossless') is not None:
            self.visual_lossless = m.get('VisualLossless')
        if m.get('OptimizeFor3d') is not None:
            self.optimize_for_3d = m.get('OptimizeFor3d')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        return self


class SetInstancePolicyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        visual_lossless: str = None,
        optimize_for_3d: str = None,
        async_mode: bool = None,
    ):
        self.instance_id = instance_id
        self.visual_lossless = visual_lossless
        self.optimize_for_3d = optimize_for_3d
        self.async_mode = async_mode

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.visual_lossless is not None:
            result['VisualLossless'] = self.visual_lossless
        if self.optimize_for_3d is not None:
            result['OptimizeFor3d'] = self.optimize_for_3d
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VisualLossless') is not None:
            self.visual_lossless = m.get('VisualLossless')
        if m.get('OptimizeFor3d') is not None:
            self.optimize_for_3d = m.get('OptimizeFor3d')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class SetInstancePolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DescribeAvailableResourceResponseAvailableResources(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        zone: str = None,
    ):
        self.cluster_type = cluster_type
        self.zone = zone

    def validate(self):
        self.validate_required(self.cluster_type, 'cluster_type')
        self.validate_required(self.zone, 'zone')

    def to_map(self):
        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_resources: List[DescribeAvailableResourceResponseAvailableResources] = None,
    ):
        self.request_id = request_id
        self.available_resources = available_resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_resources, 'available_resources')
        if self.available_resources:
            for k in self.available_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k in self.available_resources:
                result['AvailableResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.available_resources = []
        if m.get('AvailableResources') is not None:
            for k in m.get('AvailableResources'):
                temp_model = DescribeAvailableResourceResponseAvailableResources()
                self.available_resources.append(temp_model.from_map(k))
        return self


class SetClusterPolicyRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        usb_redirect: str = None,
        watermark: str = None,
        local_drive: str = None,
        clipboard: str = None,
        udp_port: str = None,
        domain_list: str = None,
        async_mode: bool = None,
    ):
        self.cluster_id = cluster_id
        self.usb_redirect = usb_redirect
        self.watermark = watermark
        self.local_drive = local_drive
        self.clipboard = clipboard
        self.udp_port = udp_port
        self.domain_list = domain_list
        self.async_mode = async_mode

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.usb_redirect, 'usb_redirect')
        self.validate_required(self.watermark, 'watermark')
        self.validate_required(self.local_drive, 'local_drive')
        self.validate_required(self.clipboard, 'clipboard')

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.udp_port is not None:
            result['UdpPort'] = self.udp_port
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('UdpPort') is not None:
            self.udp_port = m.get('UdpPort')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class SetClusterPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeClusterPolicyRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        async_mode: bool = None,
        cluster_id: str = None,
    ):
        self.task_id = task_id
        self.async_mode = async_mode
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterPolicyResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        usb_redirect: str = None,
        watermark: str = None,
        local_drive: str = None,
        clipboard: str = None,
        udp_port: str = None,
        domain_list: str = None,
        task_id: str = None,
        task_finished: bool = None,
    ):
        self.request_id = request_id
        self.usb_redirect = usb_redirect
        self.watermark = watermark
        self.local_drive = local_drive
        self.clipboard = clipboard
        self.udp_port = udp_port
        self.domain_list = domain_list
        self.task_id = task_id
        self.task_finished = task_finished

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.usb_redirect, 'usb_redirect')
        self.validate_required(self.watermark, 'watermark')
        self.validate_required(self.local_drive, 'local_drive')
        self.validate_required(self.clipboard, 'clipboard')
        self.validate_required(self.udp_port, 'udp_port')
        self.validate_required(self.domain_list, 'domain_list')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.task_finished, 'task_finished')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.udp_port is not None:
            result['UdpPort'] = self.udp_port
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('UdpPort') is not None:
            self.udp_port = m.get('UdpPort')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        return self


class SetInstanceNameRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetInstanceNameResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetImageNameRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        name: str = None,
    ):
        self.image_id = image_id
        self.name = name

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetImageNameResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetClusterNameRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        name: str = None,
    ):
        self.cluster_id = cluster_id
        self.name = name

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetClusterNameResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetInstanceUserRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        user_uid: int = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.user_uid = user_uid
        self.user_name = user_name

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.user_uid, 'user_uid')
        self.validate_required(self.user_name, 'user_name')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class SetInstanceUserResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RestartInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IsUserAdminRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class IsUserAdminResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_admin: bool = None,
        is_allow: bool = None,
    ):
        self.request_id = request_id
        self.is_admin = is_admin
        self.is_allow = is_allow

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_admin, 'is_admin')
        self.validate_required(self.is_allow, 'is_allow')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.is_allow is not None:
            result['IsAllow'] = self.is_allow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('IsAllow') is not None:
            self.is_allow = m.get('IsAllow')
        return self


class GetConnectTicketRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        app_name: str = None,
        user_name: str = None,
        password: str = None,
        task_id: str = None,
        async_mode: bool = None,
    ):
        self.instance_id = instance_id
        self.app_name = app_name
        self.user_name = user_name
        self.password = password
        self.task_id = task_id
        self.async_mode = async_mode

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class GetConnectTicketResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ticket: str = None,
        task_id: str = None,
        task_finished: bool = None,
    ):
        self.request_id = request_id
        self.ticket = ticket
        self.task_id = task_id
        self.task_finished = task_finished

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ticket, 'ticket')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.task_finished, 'task_finished')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        cluster_id: str = None,
        instance_id: str = None,
        user_uid: int = None,
        user_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.user_uid = user_uid
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeInstancesResponseInstancesAppList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_path: str = None,
        app_args: str = None,
    ):
        self.app_name = app_name
        self.app_path = app_path
        self.app_args = app_args

    def validate(self):
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.app_path, 'app_path')
        self.validate_required(self.app_args, 'app_args')

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_path is not None:
            result['AppPath'] = self.app_path
        if self.app_args is not None:
            result['AppArgs'] = self.app_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppPath') is not None:
            self.app_path = m.get('AppPath')
        if m.get('AppArgs') is not None:
            self.app_args = m.get('AppArgs')
        return self


class DescribeInstancesResponseInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        cluster_id: str = None,
        status: str = None,
        work_mode: str = None,
        stopped_mode: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_type: str = None,
        create_time: str = None,
        expire_time: str = None,
        user_uid: int = None,
        user_name: str = None,
        domain_name: str = None,
        max_bandwidth_in: int = None,
        max_bandwidth_out: int = None,
        is_bound_user: bool = None,
        app_list: List[DescribeInstancesResponseInstancesAppList] = None,
    ):
        self.instance_id = instance_id
        self.name = name
        self.cluster_id = cluster_id
        self.status = status
        self.work_mode = work_mode
        self.stopped_mode = stopped_mode
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_type = instance_type
        self.create_time = create_time
        self.expire_time = expire_time
        self.user_uid = user_uid
        self.user_name = user_name
        self.domain_name = domain_name
        self.max_bandwidth_in = max_bandwidth_in
        self.max_bandwidth_out = max_bandwidth_out
        self.is_bound_user = is_bound_user
        self.app_list = app_list

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.work_mode, 'work_mode')
        self.validate_required(self.stopped_mode, 'stopped_mode')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.instance_charge_type, 'instance_charge_type')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.user_uid, 'user_uid')
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.max_bandwidth_in, 'max_bandwidth_in')
        self.validate_required(self.max_bandwidth_out, 'max_bandwidth_out')
        self.validate_required(self.is_bound_user, 'is_bound_user')
        self.validate_required(self.app_list, 'app_list')
        if self.app_list:
            for k in self.app_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.status is not None:
            result['Status'] = self.status
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.max_bandwidth_in is not None:
            result['MaxBandwidthIn'] = self.max_bandwidth_in
        if self.max_bandwidth_out is not None:
            result['MaxBandwidthOut'] = self.max_bandwidth_out
        if self.is_bound_user is not None:
            result['IsBoundUser'] = self.is_bound_user
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('MaxBandwidthIn') is not None:
            self.max_bandwidth_in = m.get('MaxBandwidthIn')
        if m.get('MaxBandwidthOut') is not None:
            self.max_bandwidth_out = m.get('MaxBandwidthOut')
        if m.get('IsBoundUser') is not None:
            self.is_bound_user = m.get('IsBoundUser')
        self.app_list = []
        if m.get('AppList') is not None:
            for k in m.get('AppList'):
                temp_model = DescribeInstancesResponseInstancesAppList()
                self.app_list.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        instances: List[DescribeInstancesResponseInstances] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.instances = instances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeImagesResponseImages(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        name: str = None,
        size: int = None,
        status: str = None,
        create_time: str = None,
        progress: str = None,
        image_type: str = None,
        product_code: str = None,
    ):
        self.image_id = image_id
        self.name = name
        self.size = size
        self.status = status
        self.create_time = create_time
        self.progress = progress
        self.image_type = image_type
        self.product_code = product_code

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.size, 'size')
        self.validate_required(self.status, 'status')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.progress, 'progress')
        self.validate_required(self.image_type, 'image_type')
        self.validate_required(self.product_code, 'product_code')

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.name is not None:
            result['Name'] = self.name
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        images: List[DescribeImagesResponseImages] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.images = images

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.images, 'images')
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = DescribeImagesResponseImages()
                self.images.append(temp_model.from_map(k))
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeClustersResponseClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        name: str = None,
        status: str = None,
        vpc_id: str = None,
        create_time: str = None,
        security_group: str = None,
        domain_name: str = None,
        nat_id: str = None,
        nat_eip: str = None,
        instance_count: int = None,
    ):
        self.cluster_id = cluster_id
        self.name = name
        self.status = status
        self.vpc_id = vpc_id
        self.create_time = create_time
        self.security_group = security_group
        self.domain_name = domain_name
        self.nat_id = nat_id
        self.nat_eip = nat_eip
        self.instance_count = instance_count

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.security_group, 'security_group')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.nat_id, 'nat_id')
        self.validate_required(self.nat_eip, 'nat_eip')
        self.validate_required(self.instance_count, 'instance_count')

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.nat_id is not None:
            result['NatId'] = self.nat_id
        if self.nat_eip is not None:
            result['NatEip'] = self.nat_eip
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('NatId') is not None:
            self.nat_id = m.get('NatId')
        if m.get('NatEip') is not None:
            self.nat_eip = m.get('NatEip')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        page_number: int = None,
        page_size: int = None,
        clusters: List[DescribeClustersResponseClusters] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.page_number = page_number
        self.page_size = page_size
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeClustersResponseClusters()
                self.clusters.append(temp_model.from_map(k))
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
    ):
        self.image_id = image_id

    def validate(self):
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceRequestAppList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_path: str = None,
        app_args: str = None,
    ):
        self.app_name = app_name
        self.app_path = app_path
        self.app_args = app_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_path is not None:
            result['AppPath'] = self.app_path
        if self.app_args is not None:
            result['AppArgs'] = self.app_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppPath') is not None:
            self.app_path = m.get('AppPath')
        if m.get('AppArgs') is not None:
            self.app_args = m.get('AppArgs')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        v_switch_id: str = None,
        name: str = None,
        image_id: str = None,
        system_disk_size: int = None,
        system_disk_category: str = None,
        allocate_public_address: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        instance_type: str = None,
        instance_charge_type: str = None,
        auto_renew: str = None,
        period: int = None,
        period_unit: str = None,
        work_mode: str = None,
        app_list: List[CreateInstanceRequestAppList] = None,
    ):
        self.cluster_id = cluster_id
        self.v_switch_id = v_switch_id
        self.name = name
        self.image_id = image_id
        self.system_disk_size = system_disk_size
        self.system_disk_category = system_disk_category
        self.allocate_public_address = allocate_public_address
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.instance_type = instance_type
        self.instance_charge_type = instance_charge_type
        self.auto_renew = auto_renew
        self.period = period
        self.period_unit = period_unit
        self.work_mode = work_mode
        self.app_list = app_list

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.system_disk_size, 'system_disk_size')
        self.validate_required(self.system_disk_category, 'system_disk_category')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.work_mode, 'work_mode')
        if self.app_list:
            for k in self.app_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.allocate_public_address is not None:
            result['AllocatePublicAddress'] = self.allocate_public_address
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('AllocatePublicAddress') is not None:
            self.allocate_public_address = m.get('AllocatePublicAddress')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        self.app_list = []
        if m.get('AppList') is not None:
            for k in m.get('AppList'):
                temp_model = CreateInstanceRequestAppList()
                self.app_list.append(temp_model.from_map(k))
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateImageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateImageResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        image_id: str = None,
    ):
        self.request_id = request_id
        self.image_id = image_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        cluster_type: str = None,
        v_switch_id: str = None,
    ):
        self.vpc_id = vpc_id
        self.cluster_type = cluster_type
        self.v_switch_id = v_switch_id

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.cluster_type, 'cluster_type')

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_id: str = None,
    ):
        self.request_id = request_id
        self.cluster_id = cluster_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


