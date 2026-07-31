# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeManagedInstancesRequest(DaraModel):
    def __init__(
        self,
        activation_id: str = None,
        connected: str = None,
        instance_id: List[str] = None,
        instance_ip: str = None,
        instance_name: str = None,
        machine_id: str = None,
        max_results: int = None,
        next_token: str = None,
        os_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeManagedInstancesRequestTag] = None,
    ):
        # The activation code ID.
        self.activation_id = activation_id
        # Specifies whether the managed instance is connected.
        # 
        # true: The managed instance is connected. You can manage the managed instance by using Cloud Assistant.
        # 
        # false: The managed instance is not connected. The server may be shut down or Cloud Assistant Agent may not be properly installed.
        self.connected = connected
        # The ID of the managed instance. Valid values of N: 1 to 50.
        self.instance_id = instance_id
        # The internal IP address or public IP address of the managed instance.
        self.instance_ip = instance_ip
        # The name of the managed instance.
        self.instance_name = instance_name
        # The value of the MachineId parameter specified when registering the managed instance. A maximum of 36 characters are allowed.
        # Example registration script:
        # ```
        # aliyun-service --register \\
        #   --RegionId=ap-southeast-1 \\
        #   --ActivationId=xxxxxxxxxxx \\
        #   --ActivationCode=xxxxxxxxx \\
        #   --MachineId=xxxxxx \\ # Optional parameter that specifies the unique identifier of the machine
        #   --ForceResue                 
        # ```
        # 
        # - If MachineId and ForceResult are specified during registration, Cloud Assistant generates a fixed managed instance ID for this MachineId.
        # - If MachineId is not explicitly specified, Cloud Assistant automatically generates a MachineId value based on the hardware information of the machine.
        # - Recommendation: Explicitly specify MachineId and ForceResult to mark the mapping between managed instances and on-premises machines.
        self.machine_id = machine_id
        # The maximum number of entries per page for a paging query.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The operating system type of the managed instance. Valid values:
        # 
        # - windows
        # - linux
        # - FreeBSD
        self.os_type = os_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is about to be deprecated. Use NextToken and MaxResults to complete paging query operations.
        self.page_number = page_number
        # > This parameter is about to be deprecated. Use NextToken and MaxResults to complete paging query operations.
        self.page_size = page_size
        # The region ID. Currently supported regions: China (Qingdao), China (Beijing), China (Zhangjiakou), China (Hohhot), China (Ulanqab), China (Hangzhou), China (Shanghai), China (Shenzhen), China (Heyuan), China (Guangzhou), China (Chengdu), Hong Kong (China), Singapore, Japan (Tokyo), US (Silicon Valley), and US (Virginia).
        # 
        # You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query region IDs and other information.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the managed instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activation_id is not None:
            result['ActivationId'] = self.activation_id

        if self.connected is not None:
            result['Connected'] = self.connected

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ip is not None:
            result['InstanceIp'] = self.instance_ip

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.machine_id is not None:
            result['MachineId'] = self.machine_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationId') is not None:
            self.activation_id = m.get('ActivationId')

        if m.get('Connected') is not None:
            self.connected = m.get('Connected')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIp') is not None:
            self.instance_ip = m.get('InstanceIp')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MachineId') is not None:
            self.machine_id = m.get('MachineId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeManagedInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeManagedInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the managed instance. Valid values of N: 1 to 20. The tag key cannot be an empty string.
        # 
        # If you use a single tag to filter resources, the resource count with this tag cannot exceed 1,000. If you use multiple tags to filter resources, the resource count of resources that have all specified tags attached cannot exceed 1,000. If the resource count exceeds 1,000, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation to query resources.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the managed instance. Valid values of N: 1 to 20. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

