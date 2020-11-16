# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class RefreshLoginTokenRequest(TeaModel):
    def __init__(self, region_id=None, client_id=None, directory_id=None, end_user_id=None, login_token=None):
        self.region_id = region_id      # type: str
        self.client_id = client_id      # type: str
        self.directory_id = directory_id  # type: str
        self.end_user_id = end_user_id  # type: str
        self.login_token = login_token  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.end_user_id, 'end_user_id')
        self.validate_required(self.login_token, 'login_token')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientId'] = self.client_id
        result['DirectoryId'] = self.directory_id
        result['EndUserId'] = self.end_user_id
        result['LoginToken'] = self.login_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_id = map.get('ClientId')
        self.directory_id = map.get('DirectoryId')
        self.end_user_id = map.get('EndUserId')
        self.login_token = map.get('LoginToken')
        return self


class RefreshLoginTokenResponse(TeaModel):
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


class DescribeDirectoriesRequest(TeaModel):
    def __init__(self, region_id=None, client_id=None, directory_id=None):
        self.region_id = region_id      # type: str
        self.client_id = client_id      # type: str
        self.directory_id = directory_id  # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.client_id, 'client_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientId'] = self.client_id
        result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_id = map.get('ClientId')
        self.directory_id = map.get('DirectoryId')
        return self


class DescribeDirectoriesResponse(TeaModel):
    def __init__(self, request_id=None, directories=None):
        self.request_id = request_id    # type: str
        self.directories = directories  # type: List[DescribeDirectoriesResponseDirectories]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.directories, 'directories')
        if self.directories:
            for k in self.directories:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Directories'] = []
        if self.directories is not None:
            for k in self.directories:
                result['Directories'].append(k.to_map() if k else None)
        else:
            result['Directories'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.directories = []
        if map.get('Directories') is not None:
            for k in map.get('Directories'):
                temp_model = DescribeDirectoriesResponseDirectories()
                self.directories.append(temp_model.from_map(k))
        else:
            self.directories = None
        return self


class DescribeDirectoriesResponseDirectories(TeaModel):
    def __init__(self, directory_id=None, directory_type=None):
        self.directory_id = directory_id  # type: str
        self.directory_type = directory_type  # type: str

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.directory_type, 'directory_type')

    def to_map(self):
        result = {}
        result['DirectoryId'] = self.directory_id
        result['DirectoryType'] = self.directory_type
        return result

    def from_map(self, map={}):
        self.directory_id = map.get('DirectoryId')
        self.directory_type = map.get('DirectoryType')
        return self


class DescribeDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None, client_id=None, login_token=None, group_id=None,
                 desktop_status=None, max_results=None, next_token=None, user_name=None, desktop_name=None, desktop_id=None):
        self.region_id = region_id      # type: str
        self.directory_id = directory_id  # type: str
        self.client_id = client_id      # type: str
        self.login_token = login_token  # type: str
        self.group_id = group_id        # type: str
        self.desktop_status = desktop_status  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token    # type: str
        self.user_name = user_name      # type: str
        self.desktop_name = desktop_name  # type: str
        self.desktop_id = desktop_id    # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.login_token, 'login_token')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DirectoryId'] = self.directory_id
        result['ClientId'] = self.client_id
        result['LoginToken'] = self.login_token
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
        self.client_id = map.get('ClientId')
        self.login_token = map.get('LoginToken')
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
    def __init__(self, region_id=None, client_id=None, login_token=None, desktop_id=None):
        self.region_id = region_id      # type: str
        self.client_id = client_id      # type: str
        self.login_token = login_token  # type: str
        self.desktop_id = desktop_id    # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.login_token, 'login_token')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientId'] = self.client_id
        result['LoginToken'] = self.login_token
        result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_id = map.get('ClientId')
        self.login_token = map.get('LoginToken')
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
    def __init__(self, region_id=None, client_id=None, login_token=None, task_id=None, desktop_id=None):
        self.region_id = region_id      # type: str
        self.client_id = client_id      # type: str
        self.login_token = login_token  # type: str
        self.task_id = task_id          # type: str
        self.desktop_id = desktop_id    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.login_token, 'login_token')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientId'] = self.client_id
        result['LoginToken'] = self.login_token
        result['TaskId'] = self.task_id
        result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_id = map.get('ClientId')
        self.login_token = map.get('LoginToken')
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


class GetLoginTokenRequest(TeaModel):
    def __init__(self, region_id=None, client_id=None, directory_id=None, end_user_id=None, password=None):
        self.region_id = region_id      # type: str
        self.client_id = client_id      # type: str
        self.directory_id = directory_id  # type: str
        self.end_user_id = end_user_id  # type: str
        self.password = password        # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.client_id, 'client_id')
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.end_user_id, 'end_user_id')
        self.validate_required(self.password, 'password')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClientId'] = self.client_id
        result['DirectoryId'] = self.directory_id
        result['EndUserId'] = self.end_user_id
        result['Password'] = self.password
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.client_id = map.get('ClientId')
        self.directory_id = map.get('DirectoryId')
        self.end_user_id = map.get('EndUserId')
        self.password = map.get('Password')
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(self, login_token=None, request_id=None):
        self.login_token = login_token  # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.login_token, 'login_token')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['LoginToken'] = self.login_token
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.login_token = map.get('LoginToken')
        self.request_id = map.get('RequestId')
        return self
