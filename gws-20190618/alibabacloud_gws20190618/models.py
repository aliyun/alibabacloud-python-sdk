# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class SetClusterDnatRequest(TeaModel):
    def __init__(self, cluster_id=None, nat_id=None, nat_eip=None):
        self.cluster_id = cluster_id    # type: str
        self.nat_id = nat_id            # type: str
        self.nat_eip = nat_eip          # type: str

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.nat_id, 'nat_id')

    def to_map(self):
        result = {}
        result['ClusterId'] = self.cluster_id
        result['NatId'] = self.nat_id
        result['NatEip'] = self.nat_eip
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.nat_id = map.get('NatId')
        self.nat_eip = map.get('NatEip')
        return self


class SetClusterDnatResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateServiceLinkedRoleRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(self, request_id=None, already_exists=None):
        self.request_id = request_id    # type: str
        self.already_exists = already_exists  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.already_exists, 'already_exists')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AlreadyExists'] = self.already_exists
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.already_exists = map.get('AlreadyExists')
        return self


class DescribeClusterConnectionsRequest(TeaModel):
    def __init__(self, cluster_id=None, start_time=None, end_time=None, task_id=None):
        self.cluster_id = cluster_id    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['ClusterId'] = self.cluster_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.task_id = map.get('TaskId')
        return self


class DescribeClusterConnectionsResponse(TeaModel):
    def __init__(self, request_id=None, task_finished=None, task_id=None, total_count=None, connections=None):
        self.request_id = request_id    # type: str
        self.task_finished = task_finished  # type: bool
        self.task_id = task_id          # type: str
        self.total_count = total_count  # type: int
        self.connections = connections  # type: List[DescribeClusterConnectionsResponseConnections]

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
        result = {}
        result['RequestId'] = self.request_id
        result['TaskFinished'] = self.task_finished
        result['TaskId'] = self.task_id
        result['TotalCount'] = self.total_count
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        else:
            result['Connections'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_finished = map.get('TaskFinished')
        self.task_id = map.get('TaskId')
        self.total_count = map.get('TotalCount')
        self.connections = []
        if map.get('Connections') is not None:
            for k in map.get('Connections'):
                temp_model = DescribeClusterConnectionsResponseConnections()
                self.connections.append(temp_model.from_map(k))
        else:
            self.connections = None
        return self


class DescribeClusterConnectionsResponseConnections(TeaModel):
    def __init__(self, instance_id=None, client_name=None, logon_time=None, logoff_time=None, logoff_status=None):
        self.instance_id = instance_id  # type: str
        self.client_name = client_name  # type: str
        self.logon_time = logon_time    # type: str
        self.logoff_time = logoff_time  # type: str
        self.logoff_status = logoff_status  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.client_name, 'client_name')
        self.validate_required(self.logon_time, 'logon_time')
        self.validate_required(self.logoff_time, 'logoff_time')
        self.validate_required(self.logoff_status, 'logoff_status')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['ClientName'] = self.client_name
        result['LogonTime'] = self.logon_time
        result['LogoffTime'] = self.logoff_time
        result['LogoffStatus'] = self.logoff_status
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.client_name = map.get('ClientName')
        self.logon_time = map.get('LogonTime')
        self.logoff_time = map.get('LogoffTime')
        self.logoff_status = map.get('LogoffStatus')
        return self


class DescribeClusterADDomainRequest(TeaModel):
    def __init__(self, cluster_id=None, task_id=None):
        self.cluster_id = cluster_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        result['ClusterId'] = self.cluster_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.task_id = map.get('TaskId')
        return self


class DescribeClusterADDomainResponse(TeaModel):
    def __init__(self, request_id=None, is_supported=None, task_finished=None, task_id=None, domain_name=None,
                 domain_dns_ip=None):
        self.request_id = request_id    # type: str
        self.is_supported = is_supported  # type: bool
        self.task_finished = task_finished  # type: bool
        self.task_id = task_id          # type: str
        self.domain_name = domain_name  # type: str
        self.domain_dns_ip = domain_dns_ip  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_supported, 'is_supported')
        self.validate_required(self.task_finished, 'task_finished')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_dns_ip, 'domain_dns_ip')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['IsSupported'] = self.is_supported
        result['TaskFinished'] = self.task_finished
        result['TaskId'] = self.task_id
        result['DomainName'] = self.domain_name
        result['DomainDnsIp'] = self.domain_dns_ip
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.is_supported = map.get('IsSupported')
        self.task_finished = map.get('TaskFinished')
        self.task_id = map.get('TaskId')
        self.domain_name = map.get('DomainName')
        self.domain_dns_ip = map.get('DomainDnsIp')
        return self


class SetClusterADDomainRequest(TeaModel):
    def __init__(self, cluster_id=None, domain_dns_ip=None, domain_name=None, domain_password=None,
                 domain_admin=None, domain_delete=None):
        self.cluster_id = cluster_id    # type: str
        self.domain_dns_ip = domain_dns_ip  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_password = domain_password  # type: str
        self.domain_admin = domain_admin  # type: str
        self.domain_delete = domain_delete  # type: bool

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.domain_dns_ip, 'domain_dns_ip')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_password, 'domain_password')

    def to_map(self):
        result = {}
        result['ClusterId'] = self.cluster_id
        result['DomainDnsIp'] = self.domain_dns_ip
        result['DomainName'] = self.domain_name
        result['DomainPassword'] = self.domain_password
        result['DomainAdmin'] = self.domain_admin
        result['DomainDelete'] = self.domain_delete
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.domain_dns_ip = map.get('DomainDnsIp')
        self.domain_name = map.get('DomainName')
        self.domain_password = map.get('DomainPassword')
        self.domain_admin = map.get('DomainAdmin')
        self.domain_delete = map.get('DomainDelete')
        return self


class SetClusterADDomainResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class DescribeInstancePolicyRequest(TeaModel):
    def __init__(self, instance_id=None, task_id=None, async_mode=None):
        self.instance_id = instance_id  # type: str
        self.task_id = task_id          # type: str
        self.async_mode = async_mode    # type: bool

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['TaskId'] = self.task_id
        result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.task_id = map.get('TaskId')
        self.async_mode = map.get('AsyncMode')
        return self


class DescribeInstancePolicyResponse(TeaModel):
    def __init__(self, request_id=None, visual_lossless=None, optimize_for_3d=None, task_id=None,
                 task_finished=None):
        self.request_id = request_id    # type: str
        self.visual_lossless = visual_lossless  # type: str
        self.optimize_for_3d = optimize_for_3d  # type: str
        self.task_id = task_id          # type: str
        self.task_finished = task_finished  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.visual_lossless, 'visual_lossless')
        self.validate_required(self.optimize_for_3d, 'optimize_for_3d')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.task_finished, 'task_finished')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VisualLossless'] = self.visual_lossless
        result['OptimizeFor3d'] = self.optimize_for_3d
        result['TaskId'] = self.task_id
        result['TaskFinished'] = self.task_finished
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.visual_lossless = map.get('VisualLossless')
        self.optimize_for_3d = map.get('OptimizeFor3d')
        self.task_id = map.get('TaskId')
        self.task_finished = map.get('TaskFinished')
        return self


class SetInstancePolicyRequest(TeaModel):
    def __init__(self, instance_id=None, visual_lossless=None, optimize_for_3d=None, async_mode=None):
        self.instance_id = instance_id  # type: str
        self.visual_lossless = visual_lossless  # type: str
        self.optimize_for_3d = optimize_for_3d  # type: str
        self.async_mode = async_mode    # type: bool

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['VisualLossless'] = self.visual_lossless
        result['OptimizeFor3d'] = self.optimize_for_3d
        result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.visual_lossless = map.get('VisualLossless')
        self.optimize_for_3d = map.get('OptimizeFor3d')
        self.async_mode = map.get('AsyncMode')
        return self


class SetInstancePolicyResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, request_id=None, available_resources=None):
        self.request_id = request_id    # type: str
        self.available_resources = available_resources  # type: List[DescribeAvailableResourceResponseAvailableResources]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_resources, 'available_resources')
        if self.available_resources:
            for k in self.available_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k in self.available_resources:
                result['AvailableResources'].append(k.to_map() if k else None)
        else:
            result['AvailableResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.available_resources = []
        if map.get('AvailableResources') is not None:
            for k in map.get('AvailableResources'):
                temp_model = DescribeAvailableResourceResponseAvailableResources()
                self.available_resources.append(temp_model.from_map(k))
        else:
            self.available_resources = None
        return self


class DescribeAvailableResourceResponseAvailableResources(TeaModel):
    def __init__(self, cluster_type=None, zone=None):
        self.cluster_type = cluster_type  # type: str
        self.zone = zone                # type: str

    def validate(self):
        self.validate_required(self.cluster_type, 'cluster_type')
        self.validate_required(self.zone, 'zone')

    def to_map(self):
        result = {}
        result['ClusterType'] = self.cluster_type
        result['Zone'] = self.zone
        return result

    def from_map(self, map={}):
        self.cluster_type = map.get('ClusterType')
        self.zone = map.get('Zone')
        return self


class SetClusterPolicyRequest(TeaModel):
    def __init__(self, cluster_id=None, usb_redirect=None, watermark=None, local_drive=None, clipboard=None,
                 udp_port=None, domain_list=None, async_mode=None):
        self.cluster_id = cluster_id    # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark      # type: str
        self.local_drive = local_drive  # type: str
        self.clipboard = clipboard      # type: str
        self.udp_port = udp_port        # type: str
        self.domain_list = domain_list  # type: str
        self.async_mode = async_mode    # type: bool

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.usb_redirect, 'usb_redirect')
        self.validate_required(self.watermark, 'watermark')
        self.validate_required(self.local_drive, 'local_drive')
        self.validate_required(self.clipboard, 'clipboard')

    def to_map(self):
        result = {}
        result['ClusterId'] = self.cluster_id
        result['UsbRedirect'] = self.usb_redirect
        result['Watermark'] = self.watermark
        result['LocalDrive'] = self.local_drive
        result['Clipboard'] = self.clipboard
        result['UdpPort'] = self.udp_port
        result['DomainList'] = self.domain_list
        result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.usb_redirect = map.get('UsbRedirect')
        self.watermark = map.get('Watermark')
        self.local_drive = map.get('LocalDrive')
        self.clipboard = map.get('Clipboard')
        self.udp_port = map.get('UdpPort')
        self.domain_list = map.get('DomainList')
        self.async_mode = map.get('AsyncMode')
        return self


class SetClusterPolicyResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class DescribeClusterPolicyRequest(TeaModel):
    def __init__(self, task_id=None, async_mode=None, cluster_id=None):
        self.task_id = task_id          # type: str
        self.async_mode = async_mode    # type: bool
        self.cluster_id = cluster_id    # type: str

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        result['TaskId'] = self.task_id
        result['AsyncMode'] = self.async_mode
        result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        self.task_id = map.get('TaskId')
        self.async_mode = map.get('AsyncMode')
        self.cluster_id = map.get('ClusterId')
        return self


class DescribeClusterPolicyResponse(TeaModel):
    def __init__(self, request_id=None, usb_redirect=None, watermark=None, local_drive=None, clipboard=None,
                 udp_port=None, domain_list=None, task_id=None, task_finished=None):
        self.request_id = request_id    # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark      # type: str
        self.local_drive = local_drive  # type: str
        self.clipboard = clipboard      # type: str
        self.udp_port = udp_port        # type: str
        self.domain_list = domain_list  # type: str
        self.task_id = task_id          # type: str
        self.task_finished = task_finished  # type: bool

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
        result = {}
        result['RequestId'] = self.request_id
        result['UsbRedirect'] = self.usb_redirect
        result['Watermark'] = self.watermark
        result['LocalDrive'] = self.local_drive
        result['Clipboard'] = self.clipboard
        result['UdpPort'] = self.udp_port
        result['DomainList'] = self.domain_list
        result['TaskId'] = self.task_id
        result['TaskFinished'] = self.task_finished
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.usb_redirect = map.get('UsbRedirect')
        self.watermark = map.get('Watermark')
        self.local_drive = map.get('LocalDrive')
        self.clipboard = map.get('Clipboard')
        self.udp_port = map.get('UdpPort')
        self.domain_list = map.get('DomainList')
        self.task_id = map.get('TaskId')
        self.task_finished = map.get('TaskFinished')
        return self


class SetInstanceNameRequest(TeaModel):
    def __init__(self, instance_id=None, name=None):
        self.instance_id = instance_id  # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.name = map.get('Name')
        return self


class SetInstanceNameResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SetImageNameRequest(TeaModel):
    def __init__(self, image_id=None, name=None):
        self.image_id = image_id        # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.name = map.get('Name')
        return self


class SetImageNameResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SetClusterNameRequest(TeaModel):
    def __init__(self, cluster_id=None, name=None):
        self.cluster_id = cluster_id    # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['ClusterId'] = self.cluster_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.name = map.get('Name')
        return self


class SetClusterNameResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class StopInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class StartInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SetInstanceUserRequest(TeaModel):
    def __init__(self, instance_id=None, user_uid=None, user_name=None):
        self.instance_id = instance_id  # type: str
        self.user_uid = user_uid        # type: int
        self.user_name = user_name      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.user_uid, 'user_uid')
        self.validate_required(self.user_name, 'user_name')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['UserUid'] = self.user_uid
        result['UserName'] = self.user_name
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.user_uid = map.get('UserUid')
        self.user_name = map.get('UserName')
        return self


class SetInstanceUserResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        return self


class RestartInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class IsUserAdminRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class IsUserAdminResponse(TeaModel):
    def __init__(self, request_id=None, is_admin=None, is_allow=None):
        self.request_id = request_id    # type: str
        self.is_admin = is_admin        # type: bool
        self.is_allow = is_allow        # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_admin, 'is_admin')
        self.validate_required(self.is_allow, 'is_allow')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['IsAdmin'] = self.is_admin
        result['IsAllow'] = self.is_allow
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.is_admin = map.get('IsAdmin')
        self.is_allow = map.get('IsAllow')
        return self


class GetConnectTicketRequest(TeaModel):
    def __init__(self, instance_id=None, app_name=None, user_name=None, password=None, task_id=None, async_mode=None):
        self.instance_id = instance_id  # type: str
        self.app_name = app_name        # type: str
        self.user_name = user_name      # type: str
        self.password = password        # type: str
        self.task_id = task_id          # type: str
        self.async_mode = async_mode    # type: bool

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['AppName'] = self.app_name
        result['UserName'] = self.user_name
        result['Password'] = self.password
        result['TaskId'] = self.task_id
        result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.app_name = map.get('AppName')
        self.user_name = map.get('UserName')
        self.password = map.get('Password')
        self.task_id = map.get('TaskId')
        self.async_mode = map.get('AsyncMode')
        return self


class GetConnectTicketResponse(TeaModel):
    def __init__(self, request_id=None, ticket=None, task_id=None, task_finished=None):
        self.request_id = request_id    # type: str
        self.ticket = ticket            # type: str
        self.task_id = task_id          # type: str
        self.task_finished = task_finished  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ticket, 'ticket')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.task_finished, 'task_finished')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Ticket'] = self.ticket
        result['TaskId'] = self.task_id
        result['TaskFinished'] = self.task_finished
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ticket = map.get('Ticket')
        self.task_id = map.get('TaskId')
        self.task_finished = map.get('TaskFinished')
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, cluster_id=None, instance_id=None, user_uid=None,
                 user_name=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.cluster_id = cluster_id    # type: str
        self.instance_id = instance_id  # type: str
        self.user_uid = user_uid        # type: int
        self.user_name = user_name      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ClusterId'] = self.cluster_id
        result['InstanceId'] = self.instance_id
        result['UserUid'] = self.user_uid
        result['UserName'] = self.user_name
        return result

    def from_map(self, map={}):
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.cluster_id = map.get('ClusterId')
        self.instance_id = map.get('InstanceId')
        self.user_uid = map.get('UserUid')
        self.user_name = map.get('UserName')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, instances=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.instances = instances      # type: List[DescribeInstancesResponseInstances]

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
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        else:
            result['Instances'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.instances = []
        if map.get('Instances') is not None:
            for k in map.get('Instances'):
                temp_model = DescribeInstancesResponseInstances()
                self.instances.append(temp_model.from_map(k))
        else:
            self.instances = None
        return self


class DescribeInstancesResponseInstancesAppList(TeaModel):
    def __init__(self, app_name=None, app_path=None, app_args=None):
        self.app_name = app_name        # type: str
        self.app_path = app_path        # type: str
        self.app_args = app_args        # type: str

    def validate(self):
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.app_path, 'app_path')
        self.validate_required(self.app_args, 'app_args')

    def to_map(self):
        result = {}
        result['AppName'] = self.app_name
        result['AppPath'] = self.app_path
        result['AppArgs'] = self.app_args
        return result

    def from_map(self, map={}):
        self.app_name = map.get('AppName')
        self.app_path = map.get('AppPath')
        self.app_args = map.get('AppArgs')
        return self


class DescribeInstancesResponseInstances(TeaModel):
    def __init__(self, instance_id=None, name=None, cluster_id=None, status=None, work_mode=None, stopped_mode=None,
                 image_id=None, instance_charge_type=None, instance_type=None, create_time=None, expire_time=None,
                 user_uid=None, user_name=None, domain_name=None, max_bandwidth_in=None, max_bandwidth_out=None,
                 is_bound_user=None, app_list=None):
        self.instance_id = instance_id  # type: str
        self.name = name                # type: str
        self.cluster_id = cluster_id    # type: str
        self.status = status            # type: str
        self.work_mode = work_mode      # type: str
        self.stopped_mode = stopped_mode  # type: str
        self.image_id = image_id        # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.instance_type = instance_type  # type: str
        self.create_time = create_time  # type: str
        self.expire_time = expire_time  # type: str
        self.user_uid = user_uid        # type: int
        self.user_name = user_name      # type: str
        self.domain_name = domain_name  # type: str
        self.max_bandwidth_in = max_bandwidth_in  # type: int
        self.max_bandwidth_out = max_bandwidth_out  # type: int
        self.is_bound_user = is_bound_user  # type: bool
        self.app_list = app_list        # type: List[DescribeInstancesResponseInstancesAppList]

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
        result = {}
        result['InstanceId'] = self.instance_id
        result['Name'] = self.name
        result['ClusterId'] = self.cluster_id
        result['Status'] = self.status
        result['WorkMode'] = self.work_mode
        result['StoppedMode'] = self.stopped_mode
        result['ImageId'] = self.image_id
        result['InstanceChargeType'] = self.instance_charge_type
        result['InstanceType'] = self.instance_type
        result['CreateTime'] = self.create_time
        result['ExpireTime'] = self.expire_time
        result['UserUid'] = self.user_uid
        result['UserName'] = self.user_name
        result['DomainName'] = self.domain_name
        result['MaxBandwidthIn'] = self.max_bandwidth_in
        result['MaxBandwidthOut'] = self.max_bandwidth_out
        result['IsBoundUser'] = self.is_bound_user
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        else:
            result['AppList'] = None
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.name = map.get('Name')
        self.cluster_id = map.get('ClusterId')
        self.status = map.get('Status')
        self.work_mode = map.get('WorkMode')
        self.stopped_mode = map.get('StoppedMode')
        self.image_id = map.get('ImageId')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.instance_type = map.get('InstanceType')
        self.create_time = map.get('CreateTime')
        self.expire_time = map.get('ExpireTime')
        self.user_uid = map.get('UserUid')
        self.user_name = map.get('UserName')
        self.domain_name = map.get('DomainName')
        self.max_bandwidth_in = map.get('MaxBandwidthIn')
        self.max_bandwidth_out = map.get('MaxBandwidthOut')
        self.is_bound_user = map.get('IsBoundUser')
        self.app_list = []
        if map.get('AppList') is not None:
            for k in map.get('AppList'):
                temp_model = DescribeInstancesResponseInstancesAppList()
                self.app_list.append(temp_model.from_map(k))
        else:
            self.app_list = None
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['InstanceType'] = self.instance_type
        return result

    def from_map(self, map={}):
        self.instance_type = map.get('InstanceType')
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, images=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.images = images            # type: List[DescribeImagesResponseImages]

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
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        else:
            result['Images'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.images = []
        if map.get('Images') is not None:
            for k in map.get('Images'):
                temp_model = DescribeImagesResponseImages()
                self.images.append(temp_model.from_map(k))
        else:
            self.images = None
        return self


class DescribeImagesResponseImages(TeaModel):
    def __init__(self, image_id=None, name=None, size=None, status=None, create_time=None, progress=None,
                 image_type=None, product_code=None):
        self.image_id = image_id        # type: str
        self.name = name                # type: str
        self.size = size                # type: int
        self.status = status            # type: str
        self.create_time = create_time  # type: str
        self.progress = progress        # type: str
        self.image_type = image_type    # type: str
        self.product_code = product_code  # type: str

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
        result = {}
        result['ImageId'] = self.image_id
        result['Name'] = self.name
        result['Size'] = self.size
        result['Status'] = self.status
        result['CreateTime'] = self.create_time
        result['Progress'] = self.progress
        result['ImageType'] = self.image_type
        result['ProductCode'] = self.product_code
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.name = map.get('Name')
        self.size = map.get('Size')
        self.status = map.get('Status')
        self.create_time = map.get('CreateTime')
        self.progress = map.get('Progress')
        self.image_type = map.get('ImageType')
        self.product_code = map.get('ProductCode')
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(self, cluster_id=None, page_number=None, page_size=None):
        self.cluster_id = cluster_id    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ClusterId'] = self.cluster_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, clusters=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.clusters = clusters        # type: List[DescribeClustersResponseClusters]

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
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        else:
            result['Clusters'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.clusters = []
        if map.get('Clusters') is not None:
            for k in map.get('Clusters'):
                temp_model = DescribeClustersResponseClusters()
                self.clusters.append(temp_model.from_map(k))
        else:
            self.clusters = None
        return self


class DescribeClustersResponseClusters(TeaModel):
    def __init__(self, cluster_id=None, name=None, status=None, vpc_id=None, create_time=None, security_group=None,
                 domain_name=None, nat_id=None, nat_eip=None, instance_count=None):
        self.cluster_id = cluster_id    # type: str
        self.name = name                # type: str
        self.status = status            # type: str
        self.vpc_id = vpc_id            # type: str
        self.create_time = create_time  # type: str
        self.security_group = security_group  # type: str
        self.domain_name = domain_name  # type: str
        self.nat_id = nat_id            # type: str
        self.nat_eip = nat_eip          # type: str
        self.instance_count = instance_count  # type: int

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
        result = {}
        result['ClusterId'] = self.cluster_id
        result['Name'] = self.name
        result['Status'] = self.status
        result['VpcId'] = self.vpc_id
        result['CreateTime'] = self.create_time
        result['SecurityGroup'] = self.security_group
        result['DomainName'] = self.domain_name
        result['NatId'] = self.nat_id
        result['NatEip'] = self.nat_eip
        result['InstanceCount'] = self.instance_count
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.name = map.get('Name')
        self.status = map.get('Status')
        self.vpc_id = map.get('VpcId')
        self.create_time = map.get('CreateTime')
        self.security_group = map.get('SecurityGroup')
        self.domain_name = map.get('DomainName')
        self.nat_id = map.get('NatId')
        self.nat_eip = map.get('NatEip')
        self.instance_count = map.get('InstanceCount')
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteImageRequest(TeaModel):
    def __init__(self, image_id=None):
        self.image_id = image_id        # type: str

    def validate(self):
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, cluster_id=None):
        self.cluster_id = cluster_id    # type: str

    def validate(self):
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, cluster_id=None, v_switch_id=None, name=None, image_id=None, system_disk_size=None,
                 system_disk_category=None, allocate_public_address=None, internet_charge_type=None, internet_max_bandwidth_in=None,
                 internet_max_bandwidth_out=None, instance_type=None, instance_charge_type=None, auto_renew=None, period=None,
                 period_unit=None, work_mode=None, app_list=None):
        self.cluster_id = cluster_id    # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.name = name                # type: str
        self.image_id = image_id        # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.system_disk_category = system_disk_category  # type: str
        self.allocate_public_address = allocate_public_address  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.internet_max_bandwidth_in = internet_max_bandwidth_in  # type: int
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.instance_type = instance_type  # type: str
        self.instance_charge_type = instance_charge_type  # type: str
        self.auto_renew = auto_renew    # type: str
        self.period = period            # type: int
        self.period_unit = period_unit  # type: str
        self.work_mode = work_mode      # type: str
        self.app_list = app_list        # type: List[CreateInstanceRequestAppList]

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
        result = {}
        result['ClusterId'] = self.cluster_id
        result['VSwitchId'] = self.v_switch_id
        result['Name'] = self.name
        result['ImageId'] = self.image_id
        result['SystemDiskSize'] = self.system_disk_size
        result['SystemDiskCategory'] = self.system_disk_category
        result['AllocatePublicAddress'] = self.allocate_public_address
        result['InternetChargeType'] = self.internet_charge_type
        result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        result['InstanceType'] = self.instance_type
        result['InstanceChargeType'] = self.instance_charge_type
        result['AutoRenew'] = self.auto_renew
        result['Period'] = self.period
        result['PeriodUnit'] = self.period_unit
        result['WorkMode'] = self.work_mode
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        else:
            result['AppList'] = None
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('ClusterId')
        self.v_switch_id = map.get('VSwitchId')
        self.name = map.get('Name')
        self.image_id = map.get('ImageId')
        self.system_disk_size = map.get('SystemDiskSize')
        self.system_disk_category = map.get('SystemDiskCategory')
        self.allocate_public_address = map.get('AllocatePublicAddress')
        self.internet_charge_type = map.get('InternetChargeType')
        self.internet_max_bandwidth_in = map.get('InternetMaxBandwidthIn')
        self.internet_max_bandwidth_out = map.get('InternetMaxBandwidthOut')
        self.instance_type = map.get('InstanceType')
        self.instance_charge_type = map.get('InstanceChargeType')
        self.auto_renew = map.get('AutoRenew')
        self.period = map.get('Period')
        self.period_unit = map.get('PeriodUnit')
        self.work_mode = map.get('WorkMode')
        self.app_list = []
        if map.get('AppList') is not None:
            for k in map.get('AppList'):
                temp_model = CreateInstanceRequestAppList()
                self.app_list.append(temp_model.from_map(k))
        else:
            self.app_list = None
        return self


class CreateInstanceRequestAppList(TeaModel):
    def __init__(self, app_name=None, app_path=None, app_args=None):
        self.app_name = app_name        # type: str
        self.app_path = app_path        # type: str
        self.app_args = app_args        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['AppName'] = self.app_name
        result['AppPath'] = self.app_path
        result['AppArgs'] = self.app_args
        return result

    def from_map(self, map={}):
        self.app_name = map.get('AppName')
        self.app_path = map.get('AppPath')
        self.app_args = map.get('AppArgs')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, request_id=None, instance_id=None):
        self.request_id = request_id    # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.instance_id = map.get('InstanceId')
        return self


class CreateImageRequest(TeaModel):
    def __init__(self, instance_id=None, name=None):
        self.instance_id = instance_id  # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.name = map.get('Name')
        return self


class CreateImageResponse(TeaModel):
    def __init__(self, request_id=None, image_id=None):
        self.request_id = request_id    # type: str
        self.image_id = image_id        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ImageId'] = self.image_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.image_id = map.get('ImageId')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, vpc_id=None, cluster_type=None, v_switch_id=None):
        self.vpc_id = vpc_id            # type: str
        self.cluster_type = cluster_type  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        self.validate_required(self.vpc_id, 'vpc_id')
        self.validate_required(self.cluster_type, 'cluster_type')

    def to_map(self):
        result = {}
        result['VpcId'] = self.vpc_id
        result['ClusterType'] = self.cluster_type
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.vpc_id = map.get('VpcId')
        self.cluster_type = map.get('ClusterType')
        self.v_switch_id = map.get('VSwitchId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, request_id=None, cluster_id=None):
        self.request_id = request_id    # type: str
        self.cluster_id = cluster_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.cluster_id, 'cluster_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.cluster_id = map.get('ClusterId')
        return self
