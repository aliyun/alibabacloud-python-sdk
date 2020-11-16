# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class ModifyPolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None, name=None, clipboard=None, local_drive=None,
                 usb_redirect=None, watermark=None):
        self.region_id = region_id      # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.name = name                # type: str
        self.clipboard = clipboard      # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PolicyGroupId'] = self.policy_group_id
        result['Name'] = self.name
        result['Clipboard'] = self.clipboard
        result['LocalDrive'] = self.local_drive
        result['UsbRedirect'] = self.usb_redirect
        result['Watermark'] = self.watermark
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.policy_group_id = map.get('PolicyGroupId')
        self.name = map.get('Name')
        self.clipboard = map.get('Clipboard')
        self.local_drive = map.get('LocalDrive')
        self.usb_redirect = map.get('UsbRedirect')
        self.watermark = map.get('Watermark')
        return self


class ModifyPolicyGroupResponse(TeaModel):
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


class PayOrderCallbackRequest(TeaModel):
    def __init__(self, data=None):
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['data'] = self.data
        return result

    def from_map(self, map={}):
        self.data = map.get('data')
        return self


class PayOrderCallbackResponse(TeaModel):
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


class DescribeDesktopTypesRequest(TeaModel):
    def __init__(self, region_id=None, desktop_type_id=None, instance_type_family=None):
        self.region_id = region_id      # type: str
        self.desktop_type_id = desktop_type_id  # type: str
        self.instance_type_family = instance_type_family  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DesktopTypeId'] = self.desktop_type_id
        result['InstanceTypeFamily'] = self.instance_type_family
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.desktop_type_id = map.get('DesktopTypeId')
        self.instance_type_family = map.get('InstanceTypeFamily')
        return self


class DescribeDesktopTypesResponse(TeaModel):
    def __init__(self, request_id=None, desktop_types=None):
        self.request_id = request_id    # type: str
        self.desktop_types = desktop_types  # type: List[DescribeDesktopTypesResponseDesktopTypes]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.desktop_types, 'desktop_types')
        if self.desktop_types:
            for k in self.desktop_types:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DesktopTypes'] = []
        if self.desktop_types is not None:
            for k in self.desktop_types:
                result['DesktopTypes'].append(k.to_map() if k else None)
        else:
            result['DesktopTypes'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.desktop_types = []
        if map.get('DesktopTypes') is not None:
            for k in map.get('DesktopTypes'):
                temp_model = DescribeDesktopTypesResponseDesktopTypes()
                self.desktop_types.append(temp_model.from_map(k))
        else:
            self.desktop_types = None
        return self


class DescribeDesktopTypesResponseDesktopTypes(TeaModel):
    def __init__(self, desktop_type_id=None, instance_type_family=None, cpu_count=None, gpucount=None,
                 memory_size=None, system_disk_size=None, data_disk_size=None):
        self.desktop_type_id = desktop_type_id  # type: str
        self.instance_type_family = instance_type_family  # type: str
        self.cpu_count = cpu_count      # type: str
        self.gpucount = gpucount        # type: str
        self.memory_size = memory_size  # type: str
        self.system_disk_size = system_disk_size  # type: str
        self.data_disk_size = data_disk_size  # type: str

    def validate(self):
        self.validate_required(self.desktop_type_id, 'desktop_type_id')
        self.validate_required(self.instance_type_family, 'instance_type_family')
        self.validate_required(self.cpu_count, 'cpu_count')
        self.validate_required(self.gpucount, 'gpucount')
        self.validate_required(self.memory_size, 'memory_size')
        self.validate_required(self.system_disk_size, 'system_disk_size')
        self.validate_required(self.data_disk_size, 'data_disk_size')

    def to_map(self):
        result = {}
        result['DesktopTypeId'] = self.desktop_type_id
        result['InstanceTypeFamily'] = self.instance_type_family
        result['CpuCount'] = self.cpu_count
        result['GPUCount'] = self.gpucount
        result['MemorySize'] = self.memory_size
        result['SystemDiskSize'] = self.system_disk_size
        result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, map={}):
        self.desktop_type_id = map.get('DesktopTypeId')
        self.instance_type_family = map.get('InstanceTypeFamily')
        self.cpu_count = map.get('CpuCount')
        self.gpucount = map.get('GPUCount')
        self.memory_size = map.get('MemorySize')
        self.system_disk_size = map.get('SystemDiskSize')
        self.data_disk_size = map.get('DataDiskSize')
        return self


class DescribeDirectoriesRequest(TeaModel):
    def __init__(self, region_id=None, directory_type=None, directory_id=None, max_results=None, next_token=None):
        self.region_id = region_id      # type: str
        self.directory_type = directory_type  # type: str
        self.directory_id = directory_id  # type: List[str]
        self.max_results = max_results  # type: int
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DirectoryType'] = self.directory_type
        result['DirectoryId'] = self.directory_id
        result['MaxResults'] = self.max_results
        result['NextToken'] = self.next_token
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
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
    def __init__(self, adconnector_address=None, v_switch_id=None, connector_status=None,
                 network_interface_id=None):
        self.adconnector_address = adconnector_address  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.connector_status = connector_status  # type: str
        self.network_interface_id = network_interface_id  # type: str

    def validate(self):
        self.validate_required(self.adconnector_address, 'adconnector_address')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.connector_status, 'connector_status')
        self.validate_required(self.network_interface_id, 'network_interface_id')

    def to_map(self):
        result = {}
        result['ADConnectorAddress'] = self.adconnector_address
        result['VSwitchId'] = self.v_switch_id
        result['ConnectorStatus'] = self.connector_status
        result['NetworkInterfaceId'] = self.network_interface_id
        return result

    def from_map(self, map={}):
        self.adconnector_address = map.get('ADConnectorAddress')
        self.v_switch_id = map.get('VSwitchId')
        self.connector_status = map.get('ConnectorStatus')
        self.network_interface_id = map.get('NetworkInterfaceId')
        return self


class DescribeDirectoriesResponseDirectories(TeaModel):
    def __init__(self, directory_id=None, status=None, directory_type=None, creation_time=None, name=None,
                 vpc_id=None, custom_security_group_id=None, dns_user_name=None, enable_internet_access=None,
                 trust_password=None, domain_name=None, domain_user_name=None, domain_password=None, adconnectors=None,
                 dns_address=None, v_switch_ids=None):
        self.directory_id = directory_id  # type: str
        self.status = status            # type: str
        self.directory_type = directory_type  # type: str
        self.creation_time = creation_time  # type: str
        self.name = name                # type: str
        self.vpc_id = vpc_id            # type: str
        self.custom_security_group_id = custom_security_group_id  # type: str
        self.dns_user_name = dns_user_name  # type: str
        self.enable_internet_access = enable_internet_access  # type: bool
        self.trust_password = trust_password  # type: str
        self.domain_name = domain_name  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.domain_password = domain_password  # type: str
        self.adconnectors = adconnectors  # type: List[DescribeDirectoriesResponseDirectoriesADConnectors]
        self.dns_address = dns_address  # type: List[str]
        self.v_switch_ids = v_switch_ids  # type: List[str]

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.directory_type, 'directory_type')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.name, 'name')
        self.validate_required(self.vpc_id, 'vpc_id')
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
        self.validate_required(self.v_switch_ids, 'v_switch_ids')

    def to_map(self):
        result = {}
        result['DirectoryId'] = self.directory_id
        result['Status'] = self.status
        result['DirectoryType'] = self.directory_type
        result['CreationTime'] = self.creation_time
        result['Name'] = self.name
        result['VpcId'] = self.vpc_id
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
        result['VSwitchIds'] = self.v_switch_ids
        return result

    def from_map(self, map={}):
        self.directory_id = map.get('DirectoryId')
        self.status = map.get('Status')
        self.directory_type = map.get('DirectoryType')
        self.creation_time = map.get('CreationTime')
        self.name = map.get('Name')
        self.vpc_id = map.get('VpcId')
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
        self.v_switch_ids = map.get('VSwitchIds')
        return self


class DeleteDirectoriesRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None):
        self.region_id = region_id      # type: str
        self.directory_id = directory_id  # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
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


class ListDirectoryUsersRequest(TeaModel):
    def __init__(self, region_id=None, directory_id=None, next_token=None, max_results=None):
        self.region_id = region_id      # type: str
        self.directory_id = directory_id  # type: str
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DirectoryId'] = self.directory_id
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.directory_id = map.get('DirectoryId')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        return self


class ListDirectoryUsersResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, users=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.users = users              # type: List[ListDirectoryUsersResponseUsers]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.users, 'users')
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        else:
            result['Users'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        self.users = []
        if map.get('Users') is not None:
            for k in map.get('Users'):
                temp_model = ListDirectoryUsersResponseUsers()
                self.users.append(temp_model.from_map(k))
        else:
            self.users = None
        return self


class ListDirectoryUsersResponseUsers(TeaModel):
    def __init__(self, end_user=None):
        self.end_user = end_user        # type: str

    def validate(self):
        self.validate_required(self.end_user, 'end_user')

    def to_map(self):
        result = {}
        result['EndUser'] = self.end_user
        return result

    def from_map(self, map={}):
        self.end_user = map.get('EndUser')
        return self


class CreateImageRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, image_name=None, description=None):
        self.region_id = region_id      # type: str
        self.desktop_id = desktop_id    # type: str
        self.image_name = image_name    # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DesktopId'] = self.desktop_id
        result['ImageName'] = self.image_name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.desktop_id = map.get('DesktopId')
        self.image_name = map.get('ImageName')
        self.description = map.get('Description')
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


class CreateRAMDirectoryRequest(TeaModel):
    def __init__(self, region_id=None, directory_name=None, enable_internet_access=None, v_switch_id=None):
        self.region_id = region_id      # type: str
        self.directory_name = directory_name  # type: str
        self.enable_internet_access = enable_internet_access  # type: bool
        self.v_switch_id = v_switch_id  # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DirectoryName'] = self.directory_name
        result['EnableInternetAccess'] = self.enable_internet_access
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.directory_name = map.get('DirectoryName')
        self.enable_internet_access = map.get('EnableInternetAccess')
        self.v_switch_id = map.get('VSwitchId')
        return self


class CreateRAMDirectoryResponse(TeaModel):
    def __init__(self, request_id=None, directory_id=None):
        self.request_id = request_id    # type: str
        self.directory_id = directory_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.directory_id, 'directory_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DirectoryId'] = self.directory_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.directory_id = map.get('DirectoryId')
        return self


class DeletePolicyGroupsRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None):
        self.region_id = region_id      # type: str
        self.policy_group_id = policy_group_id  # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.policy_group_id, 'policy_group_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.policy_group_id = map.get('PolicyGroupId')
        return self


class DeletePolicyGroupsResponse(TeaModel):
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


class DescribePolicyGroupsRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, policy_group_id=None):
        self.region_id = region_id      # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token    # type: str
        self.policy_group_id = policy_group_id  # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['MaxResults'] = self.max_results
        result['NextToken'] = self.next_token
        result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.max_results = map.get('MaxResults')
        self.next_token = map.get('NextToken')
        self.policy_group_id = map.get('PolicyGroupId')
        return self


class DescribePolicyGroupsResponse(TeaModel):
    def __init__(self, next_token=None, request_id=None, describe_policy_groups=None):
        self.next_token = next_token    # type: str
        self.request_id = request_id    # type: str
        self.describe_policy_groups = describe_policy_groups  # type: List[DescribePolicyGroupsResponseDescribePolicyGroups]

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.describe_policy_groups, 'describe_policy_groups')
        if self.describe_policy_groups:
            for k in self.describe_policy_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextToken'] = self.next_token
        result['RequestId'] = self.request_id
        result['DescribePolicyGroups'] = []
        if self.describe_policy_groups is not None:
            for k in self.describe_policy_groups:
                result['DescribePolicyGroups'].append(k.to_map() if k else None)
        else:
            result['DescribePolicyGroups'] = None
        return result

    def from_map(self, map={}):
        self.next_token = map.get('NextToken')
        self.request_id = map.get('RequestId')
        self.describe_policy_groups = []
        if map.get('DescribePolicyGroups') is not None:
            for k in map.get('DescribePolicyGroups'):
                temp_model = DescribePolicyGroupsResponseDescribePolicyGroups()
                self.describe_policy_groups.append(temp_model.from_map(k))
        else:
            self.describe_policy_groups = None
        return self


class DescribePolicyGroupsResponseDescribePolicyGroups(TeaModel):
    def __init__(self, policy_group_id=None, policy_group_type=None, clipboard=None, local_drive=None,
                 usb_redirect=None, watermark=None, name=None):
        self.policy_group_id = policy_group_id  # type: str
        self.policy_group_type = policy_group_type  # type: str
        self.clipboard = clipboard      # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark      # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.policy_group_id, 'policy_group_id')
        self.validate_required(self.policy_group_type, 'policy_group_type')
        self.validate_required(self.clipboard, 'clipboard')
        self.validate_required(self.local_drive, 'local_drive')
        self.validate_required(self.usb_redirect, 'usb_redirect')
        self.validate_required(self.watermark, 'watermark')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['PolicyGroupId'] = self.policy_group_id
        result['PolicyGroupType'] = self.policy_group_type
        result['Clipboard'] = self.clipboard
        result['LocalDrive'] = self.local_drive
        result['UsbRedirect'] = self.usb_redirect
        result['Watermark'] = self.watermark
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.policy_group_id = map.get('PolicyGroupId')
        self.policy_group_type = map.get('PolicyGroupType')
        self.clipboard = map.get('Clipboard')
        self.local_drive = map.get('LocalDrive')
        self.usb_redirect = map.get('UsbRedirect')
        self.watermark = map.get('Watermark')
        self.name = map.get('Name')
        return self


class DeleteDesktopsRequest(TeaModel):
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


class DeleteDesktopsResponse(TeaModel):
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


class ModifyImageAttributeRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None, name=None, description=None):
        self.region_id = region_id      # type: str
        self.image_id = image_id        # type: str
        self.name = name                # type: str
        self.description = description  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ImageId'] = self.image_id
        result['Name'] = self.name
        result['Description'] = self.description
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.image_id = map.get('ImageId')
        self.name = map.get('Name')
        self.description = map.get('Description')
        return self


class ModifyImageAttributeResponse(TeaModel):
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


class DoLogicalDeleteResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = invoker          # type: str
        self.pk = pk                    # type: str
        self.bid = bid                  # type: str
        self.hid = hid                  # type: int
        self.country = country          # type: str
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup    # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['Invoker'] = self.invoker
        result['Pk'] = self.pk
        result['Bid'] = self.bid
        result['Hid'] = self.hid
        result['Country'] = self.country
        result['TaskIdentifier'] = self.task_identifier
        result['TaskExtraData'] = self.task_extra_data
        result['GmtWakeup'] = self.gmt_wakeup
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.invoker = map.get('Invoker')
        self.pk = map.get('Pk')
        self.bid = map.get('Bid')
        self.hid = map.get('Hid')
        self.country = map.get('Country')
        self.task_identifier = map.get('TaskIdentifier')
        self.task_extra_data = map.get('TaskExtraData')
        self.gmt_wakeup = map.get('GmtWakeup')
        self.region_id = map.get('RegionId')
        return self


class DoLogicalDeleteResourceResponse(TeaModel):
    def __init__(self, bid=None, country=None, hid=None, interrupt=None, invoker=None, message=None, pk=None,
                 success=None, task_extra_data=None, task_identifier=None, gmt_wakeup=None, request_id=None):
        self.bid = bid                  # type: str
        self.country = country          # type: str
        self.hid = hid                  # type: int
        self.interrupt = interrupt      # type: bool
        self.invoker = invoker          # type: str
        self.message = message          # type: str
        self.pk = pk                    # type: str
        self.success = success          # type: bool
        self.task_extra_data = task_extra_data  # type: str
        self.task_identifier = task_identifier  # type: str
        self.gmt_wakeup = gmt_wakeup    # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.bid, 'bid')
        self.validate_required(self.country, 'country')
        self.validate_required(self.hid, 'hid')
        self.validate_required(self.interrupt, 'interrupt')
        self.validate_required(self.invoker, 'invoker')
        self.validate_required(self.message, 'message')
        self.validate_required(self.pk, 'pk')
        self.validate_required(self.success, 'success')
        self.validate_required(self.task_extra_data, 'task_extra_data')
        self.validate_required(self.task_identifier, 'task_identifier')
        self.validate_required(self.gmt_wakeup, 'gmt_wakeup')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['Bid'] = self.bid
        result['Country'] = self.country
        result['Hid'] = self.hid
        result['Interrupt'] = self.interrupt
        result['Invoker'] = self.invoker
        result['Message'] = self.message
        result['Pk'] = self.pk
        result['Success'] = self.success
        result['TaskExtraData'] = self.task_extra_data
        result['TaskIdentifier'] = self.task_identifier
        result['GmtWakeup'] = self.gmt_wakeup
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.bid = map.get('Bid')
        self.country = map.get('Country')
        self.hid = map.get('Hid')
        self.interrupt = map.get('Interrupt')
        self.invoker = map.get('Invoker')
        self.message = map.get('Message')
        self.pk = map.get('Pk')
        self.success = map.get('Success')
        self.task_extra_data = map.get('TaskExtraData')
        self.task_identifier = map.get('TaskIdentifier')
        self.gmt_wakeup = map.get('GmtWakeup')
        self.request_id = map.get('RequestId')
        return self


class ModifyEntitlementRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, end_user_id=None):
        self.region_id = region_id      # type: str
        self.desktop_id = desktop_id    # type: str
        self.end_user_id = end_user_id  # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DesktopId'] = self.desktop_id
        result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.desktop_id = map.get('DesktopId')
        self.end_user_id = map.get('EndUserId')
        return self


class ModifyEntitlementResponse(TeaModel):
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


class DeleteBundlesRequest(TeaModel):
    def __init__(self, region_id=None, bundle_id=None):
        self.region_id = region_id      # type: str
        self.bundle_id = bundle_id      # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bundle_id, 'bundle_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['BundleId'] = self.bundle_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.bundle_id = map.get('BundleId')
        return self


class DeleteBundlesResponse(TeaModel):
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


class DescribeDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, group_id=None, desktop_status=None, max_results=None, next_token=None,
                 user_name=None, desktop_name=None, directory_id=None, policy_group_id=None, desktop_id=None,
                 end_user_id=None):
        self.region_id = region_id      # type: str
        self.group_id = group_id        # type: str
        self.desktop_status = desktop_status  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token    # type: str
        self.user_name = user_name      # type: str
        self.desktop_name = desktop_name  # type: str
        self.directory_id = directory_id  # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.desktop_id = desktop_id    # type: List[str]
        self.end_user_id = end_user_id  # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GroupId'] = self.group_id
        result['DesktopStatus'] = self.desktop_status
        result['MaxResults'] = self.max_results
        result['NextToken'] = self.next_token
        result['UserName'] = self.user_name
        result['DesktopName'] = self.desktop_name
        result['DirectoryId'] = self.directory_id
        result['PolicyGroupId'] = self.policy_group_id
        result['DesktopId'] = self.desktop_id
        result['EndUserId'] = self.end_user_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.group_id = map.get('GroupId')
        self.desktop_status = map.get('DesktopStatus')
        self.max_results = map.get('MaxResults')
        self.next_token = map.get('NextToken')
        self.user_name = map.get('UserName')
        self.desktop_name = map.get('DesktopName')
        self.directory_id = map.get('DirectoryId')
        self.policy_group_id = map.get('PolicyGroupId')
        self.desktop_id = map.get('DesktopId')
        self.end_user_id = map.get('EndUserId')
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
                 network_interface_id=None, expired_time=None, charge_type=None, disks=None, end_user_ids=None):
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
        self.expired_time = expired_time  # type: str
        self.charge_type = charge_type  # type: str
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
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.charge_type, 'charge_type')
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
        result['ExpiredTime'] = self.expired_time
        result['ChargeType'] = self.charge_type
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
        self.expired_time = map.get('ExpiredTime')
        self.charge_type = map.get('ChargeType')
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


class CreateBundleRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None, desktop_type=None, root_disk_size_gib=None, bundle_name=None,
                 description=None, user_disk_size_gib=None):
        self.region_id = region_id      # type: str
        self.image_id = image_id        # type: str
        self.desktop_type = desktop_type  # type: str
        self.root_disk_size_gib = root_disk_size_gib  # type: int
        self.bundle_name = bundle_name  # type: str
        self.description = description  # type: str
        self.user_disk_size_gib = user_disk_size_gib  # type: List[int]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.desktop_type, 'desktop_type')
        self.validate_required(self.root_disk_size_gib, 'root_disk_size_gib')
        self.validate_required(self.user_disk_size_gib, 'user_disk_size_gib')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ImageId'] = self.image_id
        result['DesktopType'] = self.desktop_type
        result['RootDiskSizeGib'] = self.root_disk_size_gib
        result['BundleName'] = self.bundle_name
        result['Description'] = self.description
        result['UserDiskSizeGib'] = self.user_disk_size_gib
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.image_id = map.get('ImageId')
        self.desktop_type = map.get('DesktopType')
        self.root_disk_size_gib = map.get('RootDiskSizeGib')
        self.bundle_name = map.get('BundleName')
        self.description = map.get('Description')
        self.user_disk_size_gib = map.get('UserDiskSizeGib')
        return self


class CreateBundleResponse(TeaModel):
    def __init__(self, request_id=None, bundle_id=None):
        self.request_id = request_id    # type: str
        self.bundle_id = bundle_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bundle_id, 'bundle_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BundleId'] = self.bundle_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.bundle_id = map.get('BundleId')
        return self


class ModifyDesktopsPolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, policy_group_id=None, desktop_id=None):
        self.region_id = region_id      # type: str
        self.policy_group_id = policy_group_id  # type: str
        self.desktop_id = desktop_id    # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['PolicyGroupId'] = self.policy_group_id
        result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.policy_group_id = map.get('PolicyGroupId')
        self.desktop_id = map.get('DesktopId')
        return self


class ModifyDesktopsPolicyGroupResponse(TeaModel):
    def __init__(self, request_id=None, modify_results=None):
        self.request_id = request_id    # type: str
        self.modify_results = modify_results  # type: List[ModifyDesktopsPolicyGroupResponseModifyResults]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.modify_results, 'modify_results')
        if self.modify_results:
            for k in self.modify_results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ModifyResults'] = []
        if self.modify_results is not None:
            for k in self.modify_results:
                result['ModifyResults'].append(k.to_map() if k else None)
        else:
            result['ModifyResults'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.modify_results = []
        if map.get('ModifyResults') is not None:
            for k in map.get('ModifyResults'):
                temp_model = ModifyDesktopsPolicyGroupResponseModifyResults()
                self.modify_results.append(temp_model.from_map(k))
        else:
            self.modify_results = None
        return self


class ModifyDesktopsPolicyGroupResponseModifyResults(TeaModel):
    def __init__(self, desktop_id=None, code=None, message=None):
        self.desktop_id = desktop_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: int

    def validate(self):
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['DesktopId'] = self.desktop_id
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.desktop_id = map.get('DesktopId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class CreatePolicyGroupRequest(TeaModel):
    def __init__(self, region_id=None, clipboard=None, local_drive=None, usb_redirect=None, watermark=None,
                 name=None):
        self.region_id = region_id      # type: str
        self.clipboard = clipboard      # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark      # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['Clipboard'] = self.clipboard
        result['LocalDrive'] = self.local_drive
        result['UsbRedirect'] = self.usb_redirect
        result['Watermark'] = self.watermark
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.clipboard = map.get('Clipboard')
        self.local_drive = map.get('LocalDrive')
        self.usb_redirect = map.get('UsbRedirect')
        self.watermark = map.get('Watermark')
        self.name = map.get('Name')
        return self


class CreatePolicyGroupResponse(TeaModel):
    def __init__(self, request_id=None, policy_group_id=None):
        self.request_id = request_id    # type: str
        self.policy_group_id = policy_group_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.policy_group_id, 'policy_group_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PolicyGroupId'] = self.policy_group_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.policy_group_id = map.get('PolicyGroupId')
        return self


class DoPhysicalDeleteResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = invoker          # type: str
        self.pk = pk                    # type: str
        self.bid = bid                  # type: str
        self.hid = hid                  # type: int
        self.country = country          # type: str
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup    # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['Invoker'] = self.invoker
        result['Pk'] = self.pk
        result['Bid'] = self.bid
        result['Hid'] = self.hid
        result['Country'] = self.country
        result['TaskIdentifier'] = self.task_identifier
        result['TaskExtraData'] = self.task_extra_data
        result['GmtWakeup'] = self.gmt_wakeup
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.invoker = map.get('Invoker')
        self.pk = map.get('Pk')
        self.bid = map.get('Bid')
        self.hid = map.get('Hid')
        self.country = map.get('Country')
        self.task_identifier = map.get('TaskIdentifier')
        self.task_extra_data = map.get('TaskExtraData')
        self.gmt_wakeup = map.get('GmtWakeup')
        self.region_id = map.get('RegionId')
        return self


class DoPhysicalDeleteResourceResponse(TeaModel):
    def __init__(self, bid=None, country=None, hid=None, interrupt=None, invoker=None, message=None, request_id=None,
                 pk=None, success=None, task_extra_data=None, task_identifier=None, gmt_wakeup=None):
        self.bid = bid                  # type: str
        self.country = country          # type: str
        self.hid = hid                  # type: int
        self.interrupt = interrupt      # type: bool
        self.invoker = invoker          # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.pk = pk                    # type: str
        self.success = success          # type: bool
        self.task_extra_data = task_extra_data  # type: str
        self.task_identifier = task_identifier  # type: str
        self.gmt_wakeup = gmt_wakeup    # type: str

    def validate(self):
        self.validate_required(self.bid, 'bid')
        self.validate_required(self.country, 'country')
        self.validate_required(self.hid, 'hid')
        self.validate_required(self.interrupt, 'interrupt')
        self.validate_required(self.invoker, 'invoker')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.pk, 'pk')
        self.validate_required(self.success, 'success')
        self.validate_required(self.task_extra_data, 'task_extra_data')
        self.validate_required(self.task_identifier, 'task_identifier')
        self.validate_required(self.gmt_wakeup, 'gmt_wakeup')

    def to_map(self):
        result = {}
        result['Bid'] = self.bid
        result['Country'] = self.country
        result['Hid'] = self.hid
        result['Interrupt'] = self.interrupt
        result['Invoker'] = self.invoker
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Pk'] = self.pk
        result['Success'] = self.success
        result['TaskExtraData'] = self.task_extra_data
        result['TaskIdentifier'] = self.task_identifier
        result['GmtWakeup'] = self.gmt_wakeup
        return result

    def from_map(self, map={}):
        self.bid = map.get('Bid')
        self.country = map.get('Country')
        self.hid = map.get('Hid')
        self.interrupt = map.get('Interrupt')
        self.invoker = map.get('Invoker')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.pk = map.get('Pk')
        self.success = map.get('Success')
        self.task_extra_data = map.get('TaskExtraData')
        self.task_identifier = map.get('TaskIdentifier')
        self.gmt_wakeup = map.get('GmtWakeup')
        return self


class CreateADConnectorDirectoryRequest(TeaModel):
    def __init__(self, region_id=None, domain_name=None, domain_user_name=None, domain_password=None,
                 dns_address=None, v_switch_id=None, directory_name=None):
        self.region_id = region_id      # type: str
        self.domain_name = domain_name  # type: str
        self.domain_user_name = domain_user_name  # type: str
        self.domain_password = domain_password  # type: str
        self.dns_address = dns_address  # type: List[str]
        self.v_switch_id = v_switch_id  # type: List[str]
        self.directory_name = directory_name  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.domain_user_name, 'domain_user_name')
        self.validate_required(self.domain_password, 'domain_password')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DomainName'] = self.domain_name
        result['DomainUserName'] = self.domain_user_name
        result['DomainPassword'] = self.domain_password
        result['DnsAddress'] = self.dns_address
        result['VSwitchId'] = self.v_switch_id
        result['DirectoryName'] = self.directory_name
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.domain_name = map.get('DomainName')
        self.domain_user_name = map.get('DomainUserName')
        self.domain_password = map.get('DomainPassword')
        self.dns_address = map.get('DnsAddress')
        self.v_switch_id = map.get('VSwitchId')
        self.directory_name = map.get('DirectoryName')
        return self


class CreateADConnectorDirectoryResponse(TeaModel):
    def __init__(self, directory_id=None, request_id=None, trust_password=None, ad_connectors=None):
        self.directory_id = directory_id  # type: str
        self.request_id = request_id    # type: str
        self.trust_password = trust_password  # type: str
        self.ad_connectors = ad_connectors  # type: List[CreateADConnectorDirectoryResponseAdConnectors]

    def validate(self):
        self.validate_required(self.directory_id, 'directory_id')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.trust_password, 'trust_password')
        self.validate_required(self.ad_connectors, 'ad_connectors')
        if self.ad_connectors:
            for k in self.ad_connectors:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DirectoryId'] = self.directory_id
        result['RequestId'] = self.request_id
        result['TrustPassword'] = self.trust_password
        result['AdConnectors'] = []
        if self.ad_connectors is not None:
            for k in self.ad_connectors:
                result['AdConnectors'].append(k.to_map() if k else None)
        else:
            result['AdConnectors'] = None
        return result

    def from_map(self, map={}):
        self.directory_id = map.get('DirectoryId')
        self.request_id = map.get('RequestId')
        self.trust_password = map.get('TrustPassword')
        self.ad_connectors = []
        if map.get('AdConnectors') is not None:
            for k in map.get('AdConnectors'):
                temp_model = CreateADConnectorDirectoryResponseAdConnectors()
                self.ad_connectors.append(temp_model.from_map(k))
        else:
            self.ad_connectors = None
        return self


class CreateADConnectorDirectoryResponseAdConnectors(TeaModel):
    def __init__(self, address=None):
        self.address = address          # type: str

    def validate(self):
        self.validate_required(self.address, 'address')

    def to_map(self):
        result = {}
        result['Address'] = self.address
        return result

    def from_map(self, map={}):
        self.address = map.get('Address')
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
    def __init__(self, request_id=None, ticket=None, task_id=None, task_status=None):
        self.request_id = request_id    # type: str
        self.ticket = ticket            # type: str
        self.task_id = task_id          # type: str
        self.task_status = task_status  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.ticket, 'ticket')
        self.validate_required(self.task_id, 'task_id')
        self.validate_required(self.task_status, 'task_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Ticket'] = self.ticket
        result['TaskId'] = self.task_id
        result['TaskStatus'] = self.task_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.ticket = map.get('Ticket')
        self.task_id = map.get('TaskId')
        self.task_status = map.get('TaskStatus')
        return self


class ModifyDesktopPolicysRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, clipboard=None, local_drive=None, usb_redirect=None,
                 watermark=None):
        self.region_id = region_id      # type: str
        self.desktop_id = desktop_id    # type: List[str]
        self.clipboard = clipboard      # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DesktopId'] = self.desktop_id
        result['Clipboard'] = self.clipboard
        result['LocalDrive'] = self.local_drive
        result['UsbRedirect'] = self.usb_redirect
        result['Watermark'] = self.watermark
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.desktop_id = map.get('DesktopId')
        self.clipboard = map.get('Clipboard')
        self.local_drive = map.get('LocalDrive')
        self.usb_redirect = map.get('UsbRedirect')
        self.watermark = map.get('Watermark')
        return self


class ModifyDesktopPolicysResponse(TeaModel):
    def __init__(self, request_id=None, results=None):
        self.request_id = request_id    # type: str
        self.results = results          # type: List[ModifyDesktopPolicysResponseResults]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.results, 'results')
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        else:
            result['Results'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.results = []
        if map.get('Results') is not None:
            for k in map.get('Results'):
                temp_model = ModifyDesktopPolicysResponseResults()
                self.results.append(temp_model.from_map(k))
        else:
            self.results = None
        return self


class ModifyDesktopPolicysResponseResults(TeaModel):
    def __init__(self, desktop_id=None, success=None, code=None, message=None):
        self.desktop_id = desktop_id    # type: str
        self.success = success          # type: str
        self.code = code                # type: str
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.desktop_id, 'desktop_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['DesktopId'] = self.desktop_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.desktop_id = map.get('DesktopId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        return self


class DescribeBundlesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, user_name=None, category=None,
                 bundle_id=None, bundle_type=None):
        self.region_id = region_id      # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token    # type: str
        self.user_name = user_name      # type: str
        self.category = category        # type: str
        self.bundle_id = bundle_id      # type: List[str]
        self.bundle_type = bundle_type  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['MaxResults'] = self.max_results
        result['NextToken'] = self.next_token
        result['UserName'] = self.user_name
        result['Category'] = self.category
        result['BundleId'] = self.bundle_id
        result['BundleType'] = self.bundle_type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.max_results = map.get('MaxResults')
        self.next_token = map.get('NextToken')
        self.user_name = map.get('UserName')
        self.category = map.get('Category')
        self.bundle_id = map.get('BundleId')
        self.bundle_type = map.get('BundleType')
        return self


class DescribeBundlesResponse(TeaModel):
    def __init__(self, next_token=None, request_id=None, bundles=None):
        self.next_token = next_token    # type: str
        self.request_id = request_id    # type: str
        self.bundles = bundles          # type: List[DescribeBundlesResponseBundles]

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bundles, 'bundles')
        if self.bundles:
            for k in self.bundles:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextToken'] = self.next_token
        result['RequestId'] = self.request_id
        result['Bundles'] = []
        if self.bundles is not None:
            for k in self.bundles:
                result['Bundles'].append(k.to_map() if k else None)
        else:
            result['Bundles'] = None
        return result

    def from_map(self, map={}):
        self.next_token = map.get('NextToken')
        self.request_id = map.get('RequestId')
        self.bundles = []
        if map.get('Bundles') is not None:
            for k in map.get('Bundles'):
                temp_model = DescribeBundlesResponseBundles()
                self.bundles.append(temp_model.from_map(k))
        else:
            self.bundles = None
        return self


class DescribeBundlesResponseBundlesDisks(TeaModel):
    def __init__(self, disk_size=None, disk_type=None):
        self.disk_size = disk_size      # type: int
        self.disk_type = disk_type      # type: str

    def validate(self):
        self.validate_required(self.disk_size, 'disk_size')
        self.validate_required(self.disk_type, 'disk_type')

    def to_map(self):
        result = {}
        result['DiskSize'] = self.disk_size
        result['DiskType'] = self.disk_type
        return result

    def from_map(self, map={}):
        self.disk_size = map.get('DiskSize')
        self.disk_type = map.get('DiskType')
        return self


class DescribeBundlesResponseBundles(TeaModel):
    def __init__(self, image_id=None, bundle_id=None, bundle_type=None, bundle_name=None, description=None,
                 desktop_type=None, disks=None):
        self.image_id = image_id        # type: str
        self.bundle_id = bundle_id      # type: str
        self.bundle_type = bundle_type  # type: str
        self.bundle_name = bundle_name  # type: str
        self.description = description  # type: str
        self.desktop_type = desktop_type  # type: str
        self.disks = disks              # type: List[DescribeBundlesResponseBundlesDisks]

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.bundle_id, 'bundle_id')
        self.validate_required(self.bundle_type, 'bundle_type')
        self.validate_required(self.bundle_name, 'bundle_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.desktop_type, 'desktop_type')
        self.validate_required(self.disks, 'disks')
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['BundleId'] = self.bundle_id
        result['BundleType'] = self.bundle_type
        result['BundleName'] = self.bundle_name
        result['Description'] = self.description
        result['DesktopType'] = self.desktop_type
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        else:
            result['Disks'] = None
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.bundle_id = map.get('BundleId')
        self.bundle_type = map.get('BundleType')
        self.bundle_name = map.get('BundleName')
        self.description = map.get('Description')
        self.desktop_type = map.get('DesktopType')
        self.disks = []
        if map.get('Disks') is not None:
            for k in map.get('Disks'):
                temp_model = DescribeBundlesResponseBundlesDisks()
                self.disks.append(temp_model.from_map(k))
        else:
            self.disks = None
        return self


class DeleteImagesRequest(TeaModel):
    def __init__(self, region_id=None, image_id=None):
        self.region_id = region_id      # type: str
        self.image_id = image_id        # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ImageId'] = self.image_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.image_id = map.get('ImageId')
        return self


class DeleteImagesResponse(TeaModel):
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


class DoCheckResourceRequest(TeaModel):
    def __init__(self, invoker=None, pk=None, bid=None, hid=None, country=None, task_identifier=None,
                 task_extra_data=None, gmt_wakeup=None, region_id=None):
        self.invoker = invoker          # type: str
        self.pk = pk                    # type: str
        self.bid = bid                  # type: str
        self.hid = hid                  # type: int
        self.country = country          # type: str
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup    # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['Invoker'] = self.invoker
        result['Pk'] = self.pk
        result['Bid'] = self.bid
        result['Hid'] = self.hid
        result['Country'] = self.country
        result['TaskIdentifier'] = self.task_identifier
        result['TaskExtraData'] = self.task_extra_data
        result['GmtWakeup'] = self.gmt_wakeup
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.invoker = map.get('Invoker')
        self.pk = map.get('Pk')
        self.bid = map.get('Bid')
        self.hid = map.get('Hid')
        self.country = map.get('Country')
        self.task_identifier = map.get('TaskIdentifier')
        self.task_extra_data = map.get('TaskExtraData')
        self.gmt_wakeup = map.get('GmtWakeup')
        self.region_id = map.get('RegionId')
        return self


class DoCheckResourceResponse(TeaModel):
    def __init__(self, request_id=None, interrupt=None, invoker=None, pk=None, bid=None, hid=None, country=None,
                 task_identifier=None, task_extra_data=None, gmt_wakeup=None, success=None, message=None, level=None, url=None,
                 prompt=None):
        self.request_id = request_id    # type: str
        self.interrupt = interrupt      # type: bool
        self.invoker = invoker          # type: str
        self.pk = pk                    # type: str
        self.bid = bid                  # type: str
        self.hid = hid                  # type: int
        self.country = country          # type: str
        self.task_identifier = task_identifier  # type: str
        self.task_extra_data = task_extra_data  # type: str
        self.gmt_wakeup = gmt_wakeup    # type: str
        self.success = success          # type: bool
        self.message = message          # type: str
        self.level = level              # type: int
        self.url = url                  # type: str
        self.prompt = prompt            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.interrupt, 'interrupt')
        self.validate_required(self.invoker, 'invoker')
        self.validate_required(self.pk, 'pk')
        self.validate_required(self.bid, 'bid')
        self.validate_required(self.hid, 'hid')
        self.validate_required(self.country, 'country')
        self.validate_required(self.task_identifier, 'task_identifier')
        self.validate_required(self.task_extra_data, 'task_extra_data')
        self.validate_required(self.gmt_wakeup, 'gmt_wakeup')
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.level, 'level')
        self.validate_required(self.url, 'url')
        self.validate_required(self.prompt, 'prompt')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Interrupt'] = self.interrupt
        result['Invoker'] = self.invoker
        result['Pk'] = self.pk
        result['Bid'] = self.bid
        result['Hid'] = self.hid
        result['Country'] = self.country
        result['TaskIdentifier'] = self.task_identifier
        result['TaskExtraData'] = self.task_extra_data
        result['GmtWakeup'] = self.gmt_wakeup
        result['Success'] = self.success
        result['Message'] = self.message
        result['Level'] = self.level
        result['Url'] = self.url
        result['Prompt'] = self.prompt
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.interrupt = map.get('Interrupt')
        self.invoker = map.get('Invoker')
        self.pk = map.get('Pk')
        self.bid = map.get('Bid')
        self.hid = map.get('Hid')
        self.country = map.get('Country')
        self.task_identifier = map.get('TaskIdentifier')
        self.task_extra_data = map.get('TaskExtraData')
        self.gmt_wakeup = map.get('GmtWakeup')
        self.success = map.get('Success')
        self.message = map.get('Message')
        self.level = map.get('Level')
        self.url = map.get('Url')
        self.prompt = map.get('Prompt')
        return self


class DescribeDesktopPolicysRequest(TeaModel):
    def __init__(self, region_id=None, desktop_id=None, next_token=None, max_results=None):
        self.region_id = region_id      # type: str
        self.desktop_id = desktop_id    # type: List[str]
        self.next_token = next_token    # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['DesktopId'] = self.desktop_id
        result['NextToken'] = self.next_token
        result['MaxResults'] = self.max_results
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.desktop_id = map.get('DesktopId')
        self.next_token = map.get('NextToken')
        self.max_results = map.get('MaxResults')
        return self


class DescribeDesktopPolicysResponse(TeaModel):
    def __init__(self, next_token=None, request_id=None, describe_desktop_policys=None):
        self.next_token = next_token    # type: str
        self.request_id = request_id    # type: str
        self.describe_desktop_policys = describe_desktop_policys  # type: List[DescribeDesktopPolicysResponseDescribeDesktopPolicys]

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.describe_desktop_policys, 'describe_desktop_policys')
        if self.describe_desktop_policys:
            for k in self.describe_desktop_policys:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextToken'] = self.next_token
        result['RequestId'] = self.request_id
        result['DescribeDesktopPolicys'] = []
        if self.describe_desktop_policys is not None:
            for k in self.describe_desktop_policys:
                result['DescribeDesktopPolicys'].append(k.to_map() if k else None)
        else:
            result['DescribeDesktopPolicys'] = None
        return result

    def from_map(self, map={}):
        self.next_token = map.get('NextToken')
        self.request_id = map.get('RequestId')
        self.describe_desktop_policys = []
        if map.get('DescribeDesktopPolicys') is not None:
            for k in map.get('DescribeDesktopPolicys'):
                temp_model = DescribeDesktopPolicysResponseDescribeDesktopPolicys()
                self.describe_desktop_policys.append(temp_model.from_map(k))
        else:
            self.describe_desktop_policys = None
        return self


class DescribeDesktopPolicysResponseDescribeDesktopPolicys(TeaModel):
    def __init__(self, clipboard=None, local_drive=None, usb_redirect=None, watermark=None, desktop_id=None):
        self.clipboard = clipboard      # type: str
        self.local_drive = local_drive  # type: str
        self.usb_redirect = usb_redirect  # type: str
        self.watermark = watermark      # type: str
        self.desktop_id = desktop_id    # type: str

    def validate(self):
        self.validate_required(self.clipboard, 'clipboard')
        self.validate_required(self.local_drive, 'local_drive')
        self.validate_required(self.usb_redirect, 'usb_redirect')
        self.validate_required(self.watermark, 'watermark')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = {}
        result['Clipboard'] = self.clipboard
        result['LocalDrive'] = self.local_drive
        result['UsbRedirect'] = self.usb_redirect
        result['Watermark'] = self.watermark
        result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, map={}):
        self.clipboard = map.get('Clipboard')
        self.local_drive = map.get('LocalDrive')
        self.usb_redirect = map.get('UsbRedirect')
        self.watermark = map.get('Watermark')
        self.desktop_id = map.get('DesktopId')
        return self


class CreateDesktopsRequest(TeaModel):
    def __init__(self, region_id=None, group_id=None, bundle_id=None, system_disk_size=None, data_disk_size=None,
                 desktop_name=None, user_name=None, vpc_id=None, amount=None, directory_id=None, end_user_id=None,
                 policy_group_id=None, charge_type=None, period=None, period_unit=None, auto_pay=None):
        self.region_id = region_id      # type: str
        self.group_id = group_id        # type: str
        self.bundle_id = bundle_id      # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.data_disk_size = data_disk_size  # type: int
        self.desktop_name = desktop_name  # type: str
        self.user_name = user_name      # type: str
        self.vpc_id = vpc_id            # type: str
        self.amount = amount            # type: int
        self.directory_id = directory_id  # type: str
        self.end_user_id = end_user_id  # type: List[str]
        self.policy_group_id = policy_group_id  # type: str
        self.charge_type = charge_type  # type: str
        self.period = period            # type: int
        self.period_unit = period_unit  # type: str
        self.auto_pay = auto_pay        # type: bool

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.bundle_id, 'bundle_id')
        self.validate_required(self.end_user_id, 'end_user_id')
        self.validate_required(self.policy_group_id, 'policy_group_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['GroupId'] = self.group_id
        result['BundleId'] = self.bundle_id
        result['SystemDiskSize'] = self.system_disk_size
        result['DataDiskSize'] = self.data_disk_size
        result['DesktopName'] = self.desktop_name
        result['UserName'] = self.user_name
        result['VpcId'] = self.vpc_id
        result['Amount'] = self.amount
        result['DirectoryId'] = self.directory_id
        result['EndUserId'] = self.end_user_id
        result['PolicyGroupId'] = self.policy_group_id
        result['ChargeType'] = self.charge_type
        result['Period'] = self.period
        result['PeriodUnit'] = self.period_unit
        result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.group_id = map.get('GroupId')
        self.bundle_id = map.get('BundleId')
        self.system_disk_size = map.get('SystemDiskSize')
        self.data_disk_size = map.get('DataDiskSize')
        self.desktop_name = map.get('DesktopName')
        self.user_name = map.get('UserName')
        self.vpc_id = map.get('VpcId')
        self.amount = map.get('Amount')
        self.directory_id = map.get('DirectoryId')
        self.end_user_id = map.get('EndUserId')
        self.policy_group_id = map.get('PolicyGroupId')
        self.charge_type = map.get('ChargeType')
        self.period = map.get('Period')
        self.period_unit = map.get('PeriodUnit')
        self.auto_pay = map.get('AutoPay')
        return self


class CreateDesktopsResponse(TeaModel):
    def __init__(self, request_id=None, order_id=None, desktop_id=None):
        self.request_id = request_id    # type: str
        self.order_id = order_id        # type: str
        self.desktop_id = desktop_id    # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.desktop_id, 'desktop_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrderId'] = self.order_id
        result['DesktopId'] = self.desktop_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.order_id = map.get('OrderId')
        self.desktop_id = map.get('DesktopId')
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(self, region_id=None, max_results=None, next_token=None, image_type=None, image_status=None,
                 image_id=None):
        self.region_id = region_id      # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token    # type: str
        self.image_type = image_type    # type: str
        self.image_status = image_status  # type: str
        self.image_id = image_id        # type: List[str]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['MaxResults'] = self.max_results
        result['NextToken'] = self.next_token
        result['ImageType'] = self.image_type
        result['ImageStatus'] = self.image_status
        result['ImageId'] = self.image_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.max_results = map.get('MaxResults')
        self.next_token = map.get('NextToken')
        self.image_type = map.get('ImageType')
        self.image_status = map.get('ImageStatus')
        self.image_id = map.get('ImageId')
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(self, next_token=None, request_id=None, images=None):
        self.next_token = next_token    # type: str
        self.request_id = request_id    # type: str
        self.images = images            # type: List[DescribeImagesResponseImages]

    def validate(self):
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.images, 'images')
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NextToken'] = self.next_token
        result['RequestId'] = self.request_id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        else:
            result['Images'] = None
        return result

    def from_map(self, map={}):
        self.next_token = map.get('NextToken')
        self.request_id = map.get('RequestId')
        self.images = []
        if map.get('Images') is not None:
            for k in map.get('Images'):
                temp_model = DescribeImagesResponseImages()
                self.images.append(temp_model.from_map(k))
        else:
            self.images = None
        return self


class DescribeImagesResponseImages(TeaModel):
    def __init__(self, creation_time=None, image_id=None, image_type=None, name=None, progress=None, size=None,
                 status=None, description=None, os_type=None):
        self.creation_time = creation_time  # type: str
        self.image_id = image_id        # type: str
        self.image_type = image_type    # type: str
        self.name = name                # type: str
        self.progress = progress        # type: int
        self.size = size                # type: int
        self.status = status            # type: str
        self.description = description  # type: str
        self.os_type = os_type          # type: str

    def validate(self):
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.image_type, 'image_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.progress, 'progress')
        self.validate_required(self.size, 'size')
        self.validate_required(self.status, 'status')
        self.validate_required(self.description, 'description')
        self.validate_required(self.os_type, 'os_type')

    def to_map(self):
        result = {}
        result['CreationTime'] = self.creation_time
        result['ImageId'] = self.image_id
        result['ImageType'] = self.image_type
        result['Name'] = self.name
        result['Progress'] = self.progress
        result['Size'] = self.size
        result['Status'] = self.status
        result['Description'] = self.description
        result['OsType'] = self.os_type
        return result

    def from_map(self, map={}):
        self.creation_time = map.get('CreationTime')
        self.image_id = map.get('ImageId')
        self.image_type = map.get('ImageType')
        self.name = map.get('Name')
        self.progress = map.get('Progress')
        self.size = map.get('Size')
        self.status = map.get('Status')
        self.description = map.get('Description')
        self.os_type = map.get('OsType')
        return self


