# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class DescribeDirectoriesRequest(TeaModel):
    def __init__(self, directory_type=None, directory_id=None, max_results=None, next_token=None):
        self.directory_type = directory_type  # type: str
        self.directory_id = directory_id  # type: List[str]
        self.max_results = max_results  # type: int
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.directory_type, 'directory_type')

    def to_map(self):
        result = {}
        result['DirectoryType'] = self.directory_type
        result['DirectoryId'] = self.directory_id
        result['MaxResults'] = self.max_results
        result['NextToken'] = self.next_token
        return result

    def from_map(self, map={}):
        self.directory_type = map.get('DirectoryType')
        self.directory_id = map.get('DirectoryId')
        self.max_results = map.get('MaxResults')
        self.next_token = map.get('NextToken')
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(self, next_token=None, request_id=None, directories=None):
        self.next_token = next_token    # type: str
        self.request_id = request_id    # type: str
        self.directories = directories  # type: List[DescribeDirectoriesResponseDirectories]

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.directories, 'directories')
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextToken'] = self.next_token
        result['RequestId'] = self.request_id
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        else:
            result['Directories'] = None
        return result

    def from_map(self, map={}):
        self.next_token = map.get('NextToken')
        self.request_id = map.get('RequestId')
        self.directories = []
        if map.get('Directories') is not None:
            for k in map.get('Directories'):
                temp_model = DescribeDirectoriesResponseDirectories()
                self.directories.append(temp_model.from_map(k))
        else:
            self.directories = None
        return self


class DescribeDirectoriesResponseDirectoriesADConnectors(TeaModel):
    def __init__(self, adconnector_address=None, v_switch_id=None, connector_status=None):
        self.adconnector_address = adconnector_address  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.connector_status = connector_status  # type: str

    def validate(self):
        self.validate_required(self.adconnector_address, 'adconnector_address')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.connector_status, 'connector_status')

    def to_map(self):
        result = {}
        result['ADConnectorAddress'] = self.adconnector_address
        result['VSwitchId'] = self.v_switch_id
        result['ConnectorStatus'] = self.connector_status
        return result

    def from_map(self, map={}):
        self.adconnector_address = map.get('ADConnectorAddress')
        self.v_switch_id = map.get('VSwitchId')
        self.connector_status = map.get('ConnectorStatus')
        return self


class DescribeDirectoriesResponseDirectories(TeaModel):
    def __init__(self, directory_id=None, status=None, directory_type=None, creation_time=None, name=None,
                 custom_security_group_id=None, dns_user_name=None, enable_internet_access=None, trust_password=None, domain_name=None,
                 domain_user_name=None, domain_password=None, adconnectors=None, dns_address=None):
        self.directory_id = directory_id  # type: str
        self.status = status            # type: str
        self.directory_type = directory_type  # type: str
        self.creation_time = creation_time  # type: str
        self.name = name                # type: str
        self.custom_security_group_id = custom_security_group_id  # type: str
        self.dns_user_name = dns_user_name  # type: str
        self.enable_internet_access = enable_internet_access  # type: bool
        self.trust_password = trust_password  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.domain_password = domain_password  # type: str
        self.adconnectors = adconnectors  # type: List[DescribeDirectoriesResponseDirectoriesADConnectors]
        self.dns_address = dns_address  # type: List[str]

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.name, 'name')
        self.validate_required(self.custom_security_group_id, 'custom_security_group_id')
        self.validate_required(self.dns_user_name, 'dns_user_name')
        self.validate_required(self.enable_internet_access, 'enable_internet_access')
        self.validate_required(self.trust_password, 'trust_password')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_user_name, 'domain_user_name')
        self.validate_required(self.domain_password, 'domain_password')
        self.validate_required(self.adconnectors, 'adconnectors')
        if self.adconnectors:
            for k in self.adconnectors:
                if k:
                    k.validate()
        self.validate_required(self.dns_address, 'dns_address')

    def to_map(self):
        result = {}
        result['DirectoryId'] = self.directory_id
        result['Status'] = self.status
        result['DirectoryType'] = self.directory_type
        result['CreationTime'] = self.creation_time
        result['Name'] = self.name
        result['CustomSecurityGroupId'] = self.custom_security_group_id
        result['DnsUserName'] = self.dns_user_name
        result['EnableInternetAccess'] = self.enable_internet_access
        result['TrustPassword'] = self.trust_password
        result['DomainName'] = self.domain_name
        result['DomainUserName'] = self.domain_user_name
        result['DomainPassword'] = self.domain_password
        result['ADConnectors'] = []
        if self.adconnectors is not None:
            for k in self.adconnectors:
                result['ADConnectors'].append(k.to_map() if k else None)
        else:
            result['ADConnectors'] = None
        result['DnsAddress'] = self.dns_address
        return result

    def from_map(self, map={}):
        self.directory_id = map.get('DirectoryId')
        self.status = map.get('Status')
        self.directory_type = map.get('DirectoryType')
        self.creation_time = map.get('CreationTime')
        self.name = map.get('Name')
        self.custom_security_group_id = map.get('CustomSecurityGroupId')
        self.dns_user_name = map.get('DnsUserName')
        self.enable_internet_access = map.get('EnableInternetAccess')
        self.trust_password = map.get('TrustPassword')
        self.domain_name = map.get('DomainName')
        self.domain_user_name = map.get('DomainUserName')
        self.domain_password = map.get('DomainPassword')
        self.adconnectors = []
        if map.get('ADConnectors') is not None:
            for k in map.get('ADConnectors'):
                temp_model = DescribeDirectoriesResponseDirectoriesADConnectors()
                self.adconnectors.append(temp_model.from_map(k))
        else:
            self.adconnectors = None
        self.dns_address = map.get('DnsAddress')
        return self


class DeleteDirectoriesRequest(TeaModel):
    def __init__(self, directory_id=None):
        self.directory_id = directory_id  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, map={}):
        self.directory_id = map.get('DirectoryId')
        return self


class DeleteDirectoriesResponse(TeaModel):
    def __init__(self, next_token=None, request_id=None):
        self.next_token = next_token    # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['NextToken'] = self.next_token
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.next_token = map.get('NextToken')
        self.request_id = map.get('RequestId')
        return self


class DescribeDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None, group_id=None, desktop_status=None, max_results=None,
                 next_token=None, user_name=None, desktop_name=None, desktop_id=None):
        self.region_id = region_id      # type: str
        self.directory_id = directory_id  # type: str
        self.group_id = group_id        # type: str
        self.desktop_status = desktop_status  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token    # type: str
        self.user_name = user_name      # type: str
        self.desktop_name = desktop_name  # type: str
        self.desktop_id = desktop_id    # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DirectoryId'] = self.directory_id
        result['GroupId'] = self.group_id
        result['DesktopStatus'] = self.desktop_status
        result['MaxResults'] = self.max_results
        result['NextToken'] = self.next_token
        result['UserName'] = self.user_name
        result['DesktopName'] = self.desktop_name
        result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.directory_id = map.get('DirectoryId')
        self.group_id = map.get('GroupId')
        self.desktop_status = map.get('DesktopStatus')
        self.max_results = map.get('MaxResults')
        self.next_token = map.get('NextToken')
        self.user_name = map.get('UserName')
        self.desktop_name = map.get('DesktopName')
        self.desktop_id = map.get('DesktopId')
        return self


class DescribeDesktopsResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, desktops=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.desktops = desktops        # type: List[DescribeDesktopsResponseDesktops]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.desktops, 'desktops')
        if self.desktops:
            for k in self.desktops:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        result['Desktops'] = []
        if self.desktops is not None:
            for k in self.desktops:
                result['Desktops'].append(k.to_map() if k else None)
        else:
            result['Desktops'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        self.desktops = []
        if map.get('Desktops') is not None:
            for k in map.get('Desktops'):
                temp_model = DescribeDesktopsResponseDesktops()
                self.desktops.append(temp_model.from_map(k))
        else:
            self.desktops = None
        return self


class DescribeDesktopsResponseDesktopsDisks(TeaModel):
    def __init__(self, disk_id=None, disk_size=None, disk_type=None):
        self.disk_id = disk_id          # type: str
        self.disk_size = disk_size      # type: int
        self.disk_type = disk_type      # type: str

    def validate(self):
        self.validate_required(self.disk_id, 'disk_id')
        self.validate_required(self.disk_size, 'disk_size')
        self.validate_required(self.disk_type, 'disk_type')

    def to_map(self):
        result = {}
        result['DiskId'] = self.disk_id
        result['DiskSize'] = self.disk_size
        result['DiskType'] = self.disk_type
        return result

    def from_map(self, map={}):
        self.disk_id = map.get('DiskId')
        self.disk_size = map.get('DiskSize')
        self.disk_type = map.get('DiskType')
        return self


class DescribeDesktopsResponseDesktops(TeaModel):
    def __init__(self, directory_id=None, creation_time=None, desktop_id=None, desktop_status=None,
                 desktop_name=None, image_id=None, desktop_type=None, system_disk_category=None, system_disk_size=None,
                 data_disk_category=None, data_disk_size=None, connection_status=None, policy_group_id=None, cpu=None, memory=None,
                 network_interface_id=None, disks=None, end_user_ids=None):
        self.directory_id = directory_id  # type: str
        self.creation_time = creation_time  # type: str
        self.desktop_id = desktop_id    # type: str
        self.desktop_status = desktop_status  # type: str
        self.desktop_name = desktop_name  # type: str
        self.image_id = image_id        # type: str
        self.desktop_type = desktop_type  # type: str
        self.system_disk_category = system_disk_category  # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.data_disk_category = data_disk_category  # type: str
        self.data_disk_size = data_disk_size  # type: str
        self.connection_status = connection_status  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.cpu = cpu                  # type: int
        self.memory = memory            # type: int
        self.network_interface_id = network_interface_id  # type: int
        self.disks = disks              # type: List[DescribeDesktopsResponseDesktopsDisks]
        self.end_user_ids = end_user_ids  # type: List[str]

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.desktop_status, 'desktop_status')
        self.validate_required(self.desktop_name, 'desktop_name')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.desktop_type, 'desktop_type')
        self.validate_required(self.system_disk_category, 'system_disk_category')
        self.validate_required(self.system_disk_size, 'system_disk_size')
        self.validate_required(self.data_disk_category, 'data_disk_category')
        self.validate_required(self.data_disk_size, 'data_disk_size')
        self.validate_required(self.connection_status, 'connection_status')
        self.validate_required(self.policy_group_id, 'policy_group_id')
        self.validate_required(self.cpu, 'cpu')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.network_interface_id, 'network_interface_id')
        self.validate_required(self.disks, 'disks')
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()
        self.validate_required(self.end_user_ids, 'end_user_ids')

    def to_map(self):
        result = {}
        result['DirectoryId'] = self.directory_id
        result['CreationTime'] = self.creation_time
        result['DesktopId'] = self.desktop_id
        result['DesktopStatus'] = self.desktop_status
        result['DesktopName'] = self.desktop_name
        result['ImageId'] = self.image_id
        result['DesktopType'] = self.desktop_type
        result['SystemDiskCategory'] = self.system_disk_category
        result['SystemDiskSize'] = self.system_disk_size
        result['DataDiskCategory'] = self.data_disk_category
        result['DataDiskSize'] = self.data_disk_size
        result['ConnectionStatus'] = self.connection_status
        result['PolicyGroupId'] = self.policy_group_id
        result['Cpu'] = self.cpu
        result['Memory'] = self.memory
        result['NetworkInterfaceId'] = self.network_interface_id
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        else:
            result['Disks'] = None
        result['EndUserIds'] = self.end_user_ids
        return result

    def from_map(self, map={}):
        self.directory_id = map.get('DirectoryId')
        self.creation_time = map.get('CreationTime')
        self.desktop_id = map.get('DesktopId')
        self.desktop_status = map.get('DesktopStatus')
        self.desktop_name = map.get('DesktopName')
        self.image_id = map.get('ImageId')
        self.desktop_type = map.get('DesktopType')
        self.system_disk_category = map.get('SystemDiskCategory')
        self.system_disk_size = map.get('SystemDiskSize')
        self.data_disk_category = map.get('DataDiskCategory')
        self.data_disk_size = map.get('DataDiskSize')
        self.connection_status = map.get('ConnectionStatus')
        self.policy_group_id = map.get('PolicyGroupId')
        self.cpu = map.get('Cpu')
        self.memory = map.get('Memory')
        self.network_interface_id = map.get('NetworkInterfaceId')
        self.disks = []
        if map.get('Disks') is not None:
            for k in map.get('Disks'):
                temp_model = DescribeDesktopsResponseDesktopsDisks()
                self.disks.append(temp_model.from_map(k))
        else:
            self.disks = None
        self.end_user_ids = map.get('EndUserIds')
        return self


class RebootDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None):
        self.region_id = region_id      # type: str
        self.desktop_id = desktop_id    # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.desktop_id = map.get('DesktopId')
        return self


class RebootDesktopsResponse(TeaModel):
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


class GetConnectionTicketRequest(TeaModel):
    def __init__(self, region_id=None, instance_id=None, user_name=None, password=None, task_id=None,
                 desktop_id=None):
        self.region_id = region_id      # type: str
        self.instance_id = instance_id  # type: str
        self.user_name = user_name      # type: str
        self.password = password        # type: str
        self.task_id = task_id          # type: str
        self.desktop_id = desktop_id    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['InstanceId'] = self.instance_id
        result['UserName'] = self.user_name
        result['Password'] = self.password
        result['TaskId'] = self.task_id
        result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.instance_id = map.get('InstanceId')
        self.user_name = map.get('UserName')
        self.password = map.get('Password')
        self.task_id = map.get('TaskId')
        self.desktop_id = map.get('DesktopId')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None, task_status=None, ticket=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str
        self.task_status = task_status  # type: str
        self.ticket = ticket            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.task_status, 'task_status')
        self.validate_required(self.ticket, 'ticket')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        result['TaskStatus'] = self.task_status
        result['Ticket'] = self.ticket
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        self.task_status = map.get('TaskStatus')
        self.ticket = map.get('Ticket')
        return self
