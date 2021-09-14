# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ModifyDBInstanceSwitchWeightRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dbinstance_name: str = None,
        switch_weight: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dbinstance_name = dbinstance_name
        self.switch_weight = switch_weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.switch_weight is not None:
            result['SwitchWeight'] = self.switch_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('SwitchWeight') is not None:
            self.switch_weight = m.get('SwitchWeight')
        return self


class ModifyDBInstanceSwitchWeightResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBInstanceSwitchWeightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceSwitchWeightResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDBInstanceSwitchWeightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableDedicatedHostZonesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        db_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.db_type = db_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        return self


class DescribeAvailableDedicatedHostZonesResponseBodyZonesDedicatedHostZones(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        description: str = None,
    ):
        self.zone_id = zone_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class DescribeAvailableDedicatedHostZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        dedicated_host_zones: List[DescribeAvailableDedicatedHostZonesResponseBodyZonesDedicatedHostZones] = None,
    ):
        self.dedicated_host_zones = dedicated_host_zones

    def validate(self):
        if self.dedicated_host_zones:
            for k in self.dedicated_host_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedHostZones'] = []
        if self.dedicated_host_zones is not None:
            for k in self.dedicated_host_zones:
                result['DedicatedHostZones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_host_zones = []
        if m.get('DedicatedHostZones') is not None:
            for k in m.get('DedicatedHostZones'):
                temp_model = DescribeAvailableDedicatedHostZonesResponseBodyZonesDedicatedHostZones()
                self.dedicated_host_zones.append(temp_model.from_map(k))
        return self


class DescribeAvailableDedicatedHostZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: DescribeAvailableDedicatedHostZonesResponseBodyZones = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeAvailableDedicatedHostZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeAvailableDedicatedHostZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableDedicatedHostZonesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAvailableDedicatedHostZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostGroupsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        image_category: str = None,
        engine: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.image_category = image_category
        self.engine = engine

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList(TeaModel):
    def __init__(
        self,
        zone_idlist: List[str] = None,
    ):
        self.zone_idlist = zone_idlist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneIDList') is not None:
            self.zone_idlist = m.get('ZoneIDList')
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups(TeaModel):
    def __init__(
        self,
        disk_allocate_ration: float = None,
        deploy_type: str = None,
        create_time: str = None,
        dedicated_host_count_group_by_host_type: Dict[str, Any] = None,
        text: str = None,
        dedicated_host_group_id: str = None,
        disk_utility: float = None,
        mem_used_amount: float = None,
        mem_allocated_amount: float = None,
        cpu_allocation_ratio: int = None,
        mem_allocation_ratio: int = None,
        mem_allocate_ration: float = None,
        mem_utility: float = None,
        cpu_allocated_amount: float = None,
        dedicated_host_group_desc: str = None,
        cpu_allocate_ration: float = None,
        instance_number: int = None,
        open_permission: str = None,
        vpcid: str = None,
        disk_allocated_amount: float = None,
        host_number: int = None,
        disk_used_amount: float = None,
        allocation_policy: str = None,
        engine: str = None,
        disk_allocation_ratio: int = None,
        bastion_instance_id: str = None,
        host_replace_policy: str = None,
        zone_idlist: DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList = None,
    ):
        self.disk_allocate_ration = disk_allocate_ration
        self.deploy_type = deploy_type
        self.create_time = create_time
        self.dedicated_host_count_group_by_host_type = dedicated_host_count_group_by_host_type
        self.text = text
        self.dedicated_host_group_id = dedicated_host_group_id
        self.disk_utility = disk_utility
        self.mem_used_amount = mem_used_amount
        self.mem_allocated_amount = mem_allocated_amount
        self.cpu_allocation_ratio = cpu_allocation_ratio
        self.mem_allocation_ratio = mem_allocation_ratio
        self.mem_allocate_ration = mem_allocate_ration
        self.mem_utility = mem_utility
        self.cpu_allocated_amount = cpu_allocated_amount
        self.dedicated_host_group_desc = dedicated_host_group_desc
        self.cpu_allocate_ration = cpu_allocate_ration
        self.instance_number = instance_number
        self.open_permission = open_permission
        self.vpcid = vpcid
        self.disk_allocated_amount = disk_allocated_amount
        self.host_number = host_number
        self.disk_used_amount = disk_used_amount
        self.allocation_policy = allocation_policy
        self.engine = engine
        self.disk_allocation_ratio = disk_allocation_ratio
        self.bastion_instance_id = bastion_instance_id
        self.host_replace_policy = host_replace_policy
        self.zone_idlist = zone_idlist

    def validate(self):
        if self.zone_idlist:
            self.zone_idlist.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_allocate_ration is not None:
            result['DiskAllocateRation'] = self.disk_allocate_ration
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dedicated_host_count_group_by_host_type is not None:
            result['DedicatedHostCountGroupByHostType'] = self.dedicated_host_count_group_by_host_type
        if self.text is not None:
            result['Text'] = self.text
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.disk_utility is not None:
            result['DiskUtility'] = self.disk_utility
        if self.mem_used_amount is not None:
            result['MemUsedAmount'] = self.mem_used_amount
        if self.mem_allocated_amount is not None:
            result['MemAllocatedAmount'] = self.mem_allocated_amount
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.mem_allocate_ration is not None:
            result['MemAllocateRation'] = self.mem_allocate_ration
        if self.mem_utility is not None:
            result['MemUtility'] = self.mem_utility
        if self.cpu_allocated_amount is not None:
            result['CpuAllocatedAmount'] = self.cpu_allocated_amount
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.cpu_allocate_ration is not None:
            result['CpuAllocateRation'] = self.cpu_allocate_ration
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.disk_allocated_amount is not None:
            result['DiskAllocatedAmount'] = self.disk_allocated_amount
        if self.host_number is not None:
            result['HostNumber'] = self.host_number
        if self.disk_used_amount is not None:
            result['DiskUsedAmount'] = self.disk_used_amount
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskAllocateRation') is not None:
            self.disk_allocate_ration = m.get('DiskAllocateRation')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DedicatedHostCountGroupByHostType') is not None:
            self.dedicated_host_count_group_by_host_type = m.get('DedicatedHostCountGroupByHostType')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DiskUtility') is not None:
            self.disk_utility = m.get('DiskUtility')
        if m.get('MemUsedAmount') is not None:
            self.mem_used_amount = m.get('MemUsedAmount')
        if m.get('MemAllocatedAmount') is not None:
            self.mem_allocated_amount = m.get('MemAllocatedAmount')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemAllocateRation') is not None:
            self.mem_allocate_ration = m.get('MemAllocateRation')
        if m.get('MemUtility') is not None:
            self.mem_utility = m.get('MemUtility')
        if m.get('CpuAllocatedAmount') is not None:
            self.cpu_allocated_amount = m.get('CpuAllocatedAmount')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('CpuAllocateRation') is not None:
            self.cpu_allocate_ration = m.get('CpuAllocateRation')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('DiskAllocatedAmount') is not None:
            self.disk_allocated_amount = m.get('DiskAllocatedAmount')
        if m.get('HostNumber') is not None:
            self.host_number = m.get('HostNumber')
        if m.get('DiskUsedAmount') is not None:
            self.disk_used_amount = m.get('DiskUsedAmount')
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('ZoneIDList') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList()
            self.zone_idlist = temp_model.from_map(m['ZoneIDList'])
        return self


class DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups(TeaModel):
    def __init__(
        self,
        dedicated_host_groups: List[DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups] = None,
    ):
        self.dedicated_host_groups = dedicated_host_groups

    def validate(self):
        if self.dedicated_host_groups:
            for k in self.dedicated_host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedHostGroups'] = []
        if self.dedicated_host_groups is not None:
            for k in self.dedicated_host_groups:
                result['DedicatedHostGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_host_groups = []
        if m.get('DedicatedHostGroups') is not None:
            for k in m.get('DedicatedHostGroups'):
                temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroups()
                self.dedicated_host_groups.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dedicated_host_groups: DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups = None,
    ):
        self.request_id = request_id
        self.dedicated_host_groups = dedicated_host_groups

    def validate(self):
        if self.dedicated_host_groups:
            self.dedicated_host_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dedicated_host_groups is not None:
            result['DedicatedHostGroups'] = self.dedicated_host_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DedicatedHostGroups') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups()
            self.dedicated_host_groups = temp_model.from_map(m['DedicatedHostGroups'])
        return self


class DescribeDedicatedHostGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedHostGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMyBaseHostOverViewRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        region: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeMyBaseHostOverViewResponseBodyRegionsRegionModelTypeModelsTypeModel(TeaModel):
    def __init__(
        self,
        host_engine_count: str = None,
        host_date_type: str = None,
        count: int = None,
    ):
        self.host_engine_count = host_engine_count
        self.host_date_type = host_date_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_engine_count is not None:
            result['HostEngineCount'] = self.host_engine_count
        if self.host_date_type is not None:
            result['HostDateType'] = self.host_date_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostEngineCount') is not None:
            self.host_engine_count = m.get('HostEngineCount')
        if m.get('HostDateType') is not None:
            self.host_date_type = m.get('HostDateType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class DescribeMyBaseHostOverViewResponseBodyRegionsRegionModelTypeModels(TeaModel):
    def __init__(
        self,
        type_model: List[DescribeMyBaseHostOverViewResponseBodyRegionsRegionModelTypeModelsTypeModel] = None,
    ):
        self.type_model = type_model

    def validate(self):
        if self.type_model:
            for k in self.type_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TypeModel'] = []
        if self.type_model is not None:
            for k in self.type_model:
                result['TypeModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.type_model = []
        if m.get('TypeModel') is not None:
            for k in m.get('TypeModel'):
                temp_model = DescribeMyBaseHostOverViewResponseBodyRegionsRegionModelTypeModelsTypeModel()
                self.type_model.append(temp_model.from_map(k))
        return self


class DescribeMyBaseHostOverViewResponseBodyRegionsRegionModel(TeaModel):
    def __init__(
        self,
        engine_count: str = None,
        total_count: int = None,
        host_group_count: int = None,
        region: str = None,
        type_models: DescribeMyBaseHostOverViewResponseBodyRegionsRegionModelTypeModels = None,
    ):
        self.engine_count = engine_count
        self.total_count = total_count
        self.host_group_count = host_group_count
        self.region = region
        self.type_models = type_models

    def validate(self):
        if self.type_models:
            self.type_models.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_count is not None:
            result['EngineCount'] = self.engine_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.host_group_count is not None:
            result['HostGroupCount'] = self.host_group_count
        if self.region is not None:
            result['Region'] = self.region
        if self.type_models is not None:
            result['TypeModels'] = self.type_models.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineCount') is not None:
            self.engine_count = m.get('EngineCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('HostGroupCount') is not None:
            self.host_group_count = m.get('HostGroupCount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TypeModels') is not None:
            temp_model = DescribeMyBaseHostOverViewResponseBodyRegionsRegionModelTypeModels()
            self.type_models = temp_model.from_map(m['TypeModels'])
        return self


class DescribeMyBaseHostOverViewResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_model: List[DescribeMyBaseHostOverViewResponseBodyRegionsRegionModel] = None,
    ):
        self.region_model = region_model

    def validate(self):
        if self.region_model:
            for k in self.region_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionModel'] = []
        if self.region_model is not None:
            for k in self.region_model:
                result['RegionModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_model = []
        if m.get('RegionModel') is not None:
            for k in m.get('RegionModel'):
                temp_model = DescribeMyBaseHostOverViewResponseBodyRegionsRegionModel()
                self.region_model.append(temp_model.from_map(k))
        return self


class DescribeMyBaseHostOverViewResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeMyBaseHostOverViewResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeMyBaseHostOverViewResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeMyBaseHostOverViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMyBaseHostOverViewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMyBaseHostOverViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBriefDedicatedHostsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        zone_id: str = None,
        page_numbers: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.zone_id = zone_id
        self.page_numbers = page_numbers
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeBriefDedicatedHostsResponseBodyDedicatedHosts(TeaModel):
    def __init__(
        self,
        allocation_status: str = None,
        region: str = None,
        host_status: str = None,
        zone_id: str = None,
        host_cpu: int = None,
        dedicated_host_id: str = None,
        engine: str = None,
        host_mem: int = None,
        created_time: str = None,
    ):
        self.allocation_status = allocation_status
        self.region = region
        self.host_status = host_status
        self.zone_id = zone_id
        self.host_cpu = host_cpu
        self.dedicated_host_id = dedicated_host_id
        self.engine = engine
        self.host_mem = host_mem
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.region is not None:
            result['Region'] = self.region
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeBriefDedicatedHostsResponseBody(TeaModel):
    def __init__(
        self,
        total_records: int = None,
        page_size: int = None,
        request_id: str = None,
        page_numbers: int = None,
        dedicated_host_group_id: str = None,
        dedicated_hosts: List[DescribeBriefDedicatedHostsResponseBodyDedicatedHosts] = None,
    ):
        self.total_records = total_records
        self.page_size = page_size
        self.request_id = request_id
        self.page_numbers = page_numbers
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_hosts = dedicated_hosts

    def validate(self):
        if self.dedicated_hosts:
            for k in self.dedicated_hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_records is not None:
            result['TotalRecords'] = self.total_records
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DedicatedHosts'] = []
        if self.dedicated_hosts is not None:
            for k in self.dedicated_hosts:
                result['DedicatedHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.dedicated_hosts = []
        if m.get('DedicatedHosts') is not None:
            for k in m.get('DedicatedHosts'):
                temp_model = DescribeBriefDedicatedHostsResponseBodyDedicatedHosts()
                self.dedicated_hosts.append(temp_model.from_map(k))
        return self


class DescribeBriefDedicatedHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBriefDedicatedHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBriefDedicatedHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedResourceAdvisorRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_group_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDedicatedResourceAdvisorResponseBodyResourceAdvisorsResourceAdvisors(TeaModel):
    def __init__(
        self,
        cpu_usage_after_action: float = None,
        action: str = None,
        destination_dedicated_host_id: str = None,
        source_dedicated_instance_id: str = None,
        action_description: str = None,
        source_dedicated_instance_role: str = None,
        source_dedicated_host_id: str = None,
        cpu_usage_before_action: float = None,
    ):
        self.cpu_usage_after_action = cpu_usage_after_action
        self.action = action
        self.destination_dedicated_host_id = destination_dedicated_host_id
        self.source_dedicated_instance_id = source_dedicated_instance_id
        self.action_description = action_description
        self.source_dedicated_instance_role = source_dedicated_instance_role
        self.source_dedicated_host_id = source_dedicated_host_id
        self.cpu_usage_before_action = cpu_usage_before_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_usage_after_action is not None:
            result['CpuUsageAfterAction'] = self.cpu_usage_after_action
        if self.action is not None:
            result['Action'] = self.action
        if self.destination_dedicated_host_id is not None:
            result['DestinationDedicatedHostId'] = self.destination_dedicated_host_id
        if self.source_dedicated_instance_id is not None:
            result['SourceDedicatedInstanceId'] = self.source_dedicated_instance_id
        if self.action_description is not None:
            result['ActionDescription'] = self.action_description
        if self.source_dedicated_instance_role is not None:
            result['SourceDedicatedInstanceRole'] = self.source_dedicated_instance_role
        if self.source_dedicated_host_id is not None:
            result['SourceDedicatedHostId'] = self.source_dedicated_host_id
        if self.cpu_usage_before_action is not None:
            result['CpuUsageBeforeAction'] = self.cpu_usage_before_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuUsageAfterAction') is not None:
            self.cpu_usage_after_action = m.get('CpuUsageAfterAction')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('DestinationDedicatedHostId') is not None:
            self.destination_dedicated_host_id = m.get('DestinationDedicatedHostId')
        if m.get('SourceDedicatedInstanceId') is not None:
            self.source_dedicated_instance_id = m.get('SourceDedicatedInstanceId')
        if m.get('ActionDescription') is not None:
            self.action_description = m.get('ActionDescription')
        if m.get('SourceDedicatedInstanceRole') is not None:
            self.source_dedicated_instance_role = m.get('SourceDedicatedInstanceRole')
        if m.get('SourceDedicatedHostId') is not None:
            self.source_dedicated_host_id = m.get('SourceDedicatedHostId')
        if m.get('CpuUsageBeforeAction') is not None:
            self.cpu_usage_before_action = m.get('CpuUsageBeforeAction')
        return self


class DescribeDedicatedResourceAdvisorResponseBodyResourceAdvisors(TeaModel):
    def __init__(
        self,
        resource_advisors: List[DescribeDedicatedResourceAdvisorResponseBodyResourceAdvisorsResourceAdvisors] = None,
    ):
        self.resource_advisors = resource_advisors

    def validate(self):
        if self.resource_advisors:
            for k in self.resource_advisors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceAdvisors'] = []
        if self.resource_advisors is not None:
            for k in self.resource_advisors:
                result['ResourceAdvisors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_advisors = []
        if m.get('ResourceAdvisors') is not None:
            for k in m.get('ResourceAdvisors'):
                temp_model = DescribeDedicatedResourceAdvisorResponseBodyResourceAdvisorsResourceAdvisors()
                self.resource_advisors.append(temp_model.from_map(k))
        return self


class DescribeDedicatedResourceAdvisorResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        request_id: str = None,
        resource_advisors: DescribeDedicatedResourceAdvisorResponseBodyResourceAdvisors = None,
    ):
        self.dedicated_host_group_id = dedicated_host_group_id
        self.request_id = request_id
        self.resource_advisors = resource_advisors

    def validate(self):
        if self.resource_advisors:
            self.resource_advisors.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_advisors is not None:
            result['ResourceAdvisors'] = self.resource_advisors.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceAdvisors') is not None:
            temp_model = DescribeDedicatedResourceAdvisorResponseBodyResourceAdvisors()
            self.resource_advisors = temp_model.from_map(m['ResourceAdvisors'])
        return self


class DescribeDedicatedResourceAdvisorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedResourceAdvisorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedResourceAdvisorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeListUserBackupFileRecordRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        status: str = None,
        engine: str = None,
        ops_service_version: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.status = status
        self.engine = engine
        self.ops_service_version = ops_service_version
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.ops_service_version is not None:
            result['OpsServiceVersion'] = self.ops_service_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('OpsServiceVersion') is not None:
            self.ops_service_version = m.get('OpsServiceVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeListUserBackupFileRecordResponseBodyRecords(TeaModel):
    def __init__(
        self,
        status: str = None,
        oss_file_path: str = None,
        oss_bucket: str = None,
        gmt_modified: str = None,
        bid: str = None,
        engine_version: str = None,
        oss_file_name: str = None,
        oss_file_size: int = None,
        gmt_created: str = None,
        backup_set_id: str = None,
        instance_name: str = None,
        db_instance_name: str = None,
        engine: str = None,
        binlog_info: str = None,
        custins_id: str = None,
        oss_file_meta_data: str = None,
        oss_url: str = None,
        task_id: str = None,
        id: int = None,
        reason: str = None,
        uid: str = None,
    ):
        self.status = status
        self.oss_file_path = oss_file_path
        self.oss_bucket = oss_bucket
        self.gmt_modified = gmt_modified
        self.bid = bid
        self.engine_version = engine_version
        self.oss_file_name = oss_file_name
        self.oss_file_size = oss_file_size
        self.gmt_created = gmt_created
        self.backup_set_id = backup_set_id
        self.instance_name = instance_name
        self.db_instance_name = db_instance_name
        self.engine = engine
        self.binlog_info = binlog_info
        self.custins_id = custins_id
        self.oss_file_meta_data = oss_file_meta_data
        self.oss_url = oss_url
        self.task_id = task_id
        self.id = id
        self.reason = reason
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.oss_file_path is not None:
            result['OssFilePath'] = self.oss_file_path
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.oss_file_name is not None:
            result['OssFileName'] = self.oss_file_name
        if self.oss_file_size is not None:
            result['OssFileSize'] = self.oss_file_size
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.binlog_info is not None:
            result['BinlogInfo'] = self.binlog_info
        if self.custins_id is not None:
            result['CustinsId'] = self.custins_id
        if self.oss_file_meta_data is not None:
            result['OssFileMetaData'] = self.oss_file_meta_data
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.id is not None:
            result['Id'] = self.id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OssFilePath') is not None:
            self.oss_file_path = m.get('OssFilePath')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('OssFileName') is not None:
            self.oss_file_name = m.get('OssFileName')
        if m.get('OssFileSize') is not None:
            self.oss_file_size = m.get('OssFileSize')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('BinlogInfo') is not None:
            self.binlog_info = m.get('BinlogInfo')
        if m.get('CustinsId') is not None:
            self.custins_id = m.get('CustinsId')
        if m.get('OssFileMetaData') is not None:
            self.oss_file_meta_data = m.get('OssFileMetaData')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeListUserBackupFileRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        records: List[DescribeListUserBackupFileRecordResponseBodyRecords] = None,
    ):
        self.request_id = request_id
        self.records = records

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = DescribeListUserBackupFileRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        return self


class DescribeListUserBackupFileRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeListUserBackupFileRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeListUserBackupFileRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_id: str = None,
        account_name: str = None,
        account_password: str = None,
        region_id: str = None,
        bastion_instance_id: str = None,
        account_type: str = None,
        client_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_id = dedicated_host_id
        self.account_name = account_name
        self.account_password = account_password
        self.region_id = region_id
        self.bastion_instance_id = bastion_instance_id
        self.account_type = account_type
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDedicatedHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_id: str = None,
        account_name: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_id = dedicated_host_id
        self.account_name = account_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDedicatedHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDedicatedHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedHostGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_group_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDedicatedHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDedicatedHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDedicatedHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDedicatedHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserIfAuthoriseMyBaseSystemRoleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        region: str = None,
        zone_id: str = None,
        ram_role_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.region = region
        self.zone_id = zone_id
        self.ram_role_name = ram_role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region is not None:
            result['Region'] = self.region
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')
        return self


class CheckUserIfAuthoriseMyBaseSystemRoleResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        request_id: str = None,
        role_name: str = None,
    ):
        self.ali_uid = ali_uid
        self.request_id = request_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CheckUserIfAuthoriseMyBaseSystemRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckUserIfAuthoriseMyBaseSystemRoleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckUserIfAuthoriseMyBaseSystemRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduleInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        schedule_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.schedule_id = schedule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        return self


class DescribeScheduleInstanceResponseBodyInstanceScheduleStatusList(TeaModel):
    def __init__(
        self,
        schedule_status: str = None,
        instance_node_target_host_id: str = None,
        instance_node_role: str = None,
        engine: str = None,
        instance_id: str = None,
        instance_node_source_host_id: str = None,
    ):
        self.schedule_status = schedule_status
        self.instance_node_target_host_id = instance_node_target_host_id
        self.instance_node_role = instance_node_role
        self.engine = engine
        self.instance_id = instance_id
        self.instance_node_source_host_id = instance_node_source_host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_status is not None:
            result['ScheduleStatus'] = self.schedule_status
        if self.instance_node_target_host_id is not None:
            result['InstanceNodeTargetHostId'] = self.instance_node_target_host_id
        if self.instance_node_role is not None:
            result['InstanceNodeRole'] = self.instance_node_role
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_node_source_host_id is not None:
            result['InstanceNodeSourceHostId'] = self.instance_node_source_host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleStatus') is not None:
            self.schedule_status = m.get('ScheduleStatus')
        if m.get('InstanceNodeTargetHostId') is not None:
            self.instance_node_target_host_id = m.get('InstanceNodeTargetHostId')
        if m.get('InstanceNodeRole') is not None:
            self.instance_node_role = m.get('InstanceNodeRole')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceNodeSourceHostId') is not None:
            self.instance_node_source_host_id = m.get('InstanceNodeSourceHostId')
        return self


class DescribeScheduleInstanceResponseBody(TeaModel):
    def __init__(
        self,
        schedule_id: str = None,
        request_id: str = None,
        instance_schedule_status_list: List[DescribeScheduleInstanceResponseBodyInstanceScheduleStatusList] = None,
    ):
        self.schedule_id = schedule_id
        self.request_id = request_id
        self.instance_schedule_status_list = instance_schedule_status_list

    def validate(self):
        if self.instance_schedule_status_list:
            for k in self.instance_schedule_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceScheduleStatusList'] = []
        if self.instance_schedule_status_list is not None:
            for k in self.instance_schedule_status_list:
                result['InstanceScheduleStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_schedule_status_list = []
        if m.get('InstanceScheduleStatusList') is not None:
            for k in m.get('InstanceScheduleStatusList'):
                temp_model = DescribeScheduleInstanceResponseBodyInstanceScheduleStatusList()
                self.instance_schedule_status_list.append(temp_model.from_map(k))
        return self


class DescribeScheduleInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScheduleInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScheduleInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExcuteScheduleRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        action_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.action_type = action_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        return self


class ExcuteScheduleResponseBody(TeaModel):
    def __init__(
        self,
        schedule_id: str = None,
        request_id: str = None,
    ):
        self.schedule_id = schedule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExcuteScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExcuteScheduleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExcuteScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_id: str = None,
        failover_mode: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id
        self.failover_mode = failover_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        return self


class ReplaceDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ReplaceDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReplaceDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReplaceDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_id: str = None,
        account_name: str = None,
        account_password: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_id = dedicated_host_id
        self.account_name = account_name
        self.account_password = account_password
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDedicatedHostAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostEcsLevelInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        db_type: str = None,
        region_id: str = None,
        zone_id: str = None,
        storage_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.db_type = db_type
        self.region_id = region_id
        self.zone_id = zone_id
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems(TeaModel):
    def __init__(
        self,
        net_band_width: float = None,
        ecs_class: str = None,
        rds_class_code: str = None,
        cpu: int = None,
        cpu_frequency: str = None,
        storage_iops: int = None,
        cloud_storage_bandwidth: float = None,
        ecs_class_code: str = None,
        is_cloud_disk: int = None,
        memory: int = None,
        net_package: int = None,
        cpu_version: str = None,
        local_storage: str = None,
        description: str = None,
    ):
        self.net_band_width = net_band_width
        self.ecs_class = ecs_class
        self.rds_class_code = rds_class_code
        self.cpu = cpu
        self.cpu_frequency = cpu_frequency
        self.storage_iops = storage_iops
        self.cloud_storage_bandwidth = cloud_storage_bandwidth
        self.ecs_class_code = ecs_class_code
        self.is_cloud_disk = is_cloud_disk
        self.memory = memory
        self.net_package = net_package
        self.cpu_version = cpu_version
        self.local_storage = local_storage
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.net_band_width is not None:
            result['NetBandWidth'] = self.net_band_width
        if self.ecs_class is not None:
            result['EcsClass'] = self.ecs_class
        if self.rds_class_code is not None:
            result['RdsClassCode'] = self.rds_class_code
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_frequency is not None:
            result['CpuFrequency'] = self.cpu_frequency
        if self.storage_iops is not None:
            result['StorageIops'] = self.storage_iops
        if self.cloud_storage_bandwidth is not None:
            result['CloudStorageBandwidth'] = self.cloud_storage_bandwidth
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.is_cloud_disk is not None:
            result['IsCloudDisk'] = self.is_cloud_disk
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.net_package is not None:
            result['NetPackage'] = self.net_package
        if self.cpu_version is not None:
            result['CpuVersion'] = self.cpu_version
        if self.local_storage is not None:
            result['LocalStorage'] = self.local_storage
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetBandWidth') is not None:
            self.net_band_width = m.get('NetBandWidth')
        if m.get('EcsClass') is not None:
            self.ecs_class = m.get('EcsClass')
        if m.get('RdsClassCode') is not None:
            self.rds_class_code = m.get('RdsClassCode')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuFrequency') is not None:
            self.cpu_frequency = m.get('CpuFrequency')
        if m.get('StorageIops') is not None:
            self.storage_iops = m.get('StorageIops')
        if m.get('CloudStorageBandwidth') is not None:
            self.cloud_storage_bandwidth = m.get('CloudStorageBandwidth')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('IsCloudDisk') is not None:
            self.is_cloud_disk = m.get('IsCloudDisk')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetPackage') is not None:
            self.net_package = m.get('NetPackage')
        if m.get('CpuVersion') is not None:
            self.cpu_version = m.get('CpuVersion')
        if m.get('LocalStorage') is not None:
            self.local_storage = m.get('LocalStorage')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos(TeaModel):
    def __init__(
        self,
        cddc_host_type: str = None,
        items: List[DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems] = None,
    ):
        self.cddc_host_type = cddc_host_type
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cddc_host_type is not None:
            result['CddcHostType'] = self.cddc_host_type
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CddcHostType') is not None:
            self.cddc_host_type = m.get('CddcHostType')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeHostEcsLevelInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_ecs_level_infos: List[DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos] = None,
    ):
        self.request_id = request_id
        self.host_ecs_level_infos = host_ecs_level_infos

    def validate(self):
        if self.host_ecs_level_infos:
            for k in self.host_ecs_level_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostEcsLevelInfos'] = []
        if self.host_ecs_level_infos is not None:
            for k in self.host_ecs_level_infos:
                result['HostEcsLevelInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_ecs_level_infos = []
        if m.get('HostEcsLevelInfos') is not None:
            for k in m.get('HostEcsLevelInfos'):
                temp_model = DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos()
                self.host_ecs_level_infos.append(temp_model.from_map(k))
        return self


class DescribeHostEcsLevelInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHostEcsLevelInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHostEcsLevelInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocateHostInstanceCrossVpcVipRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        connection_string: str = None,
        port: str = None,
        dbinstance_id: str = None,
        bind_vpc_id: str = None,
        bind_vswitch_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.connection_string = connection_string
        self.port = port
        self.dbinstance_id = dbinstance_id
        self.bind_vpc_id = bind_vpc_id
        self.bind_vswitch_id = bind_vswitch_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.port is not None:
            result['Port'] = self.port
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.bind_vpc_id is not None:
            result['BindVpcId'] = self.bind_vpc_id
        if self.bind_vswitch_id is not None:
            result['BindVSwitchId'] = self.bind_vswitch_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('BindVpcId') is not None:
            self.bind_vpc_id = m.get('BindVpcId')
        if m.get('BindVSwitchId') is not None:
            self.bind_vswitch_id = m.get('BindVSwitchId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AllocateHostInstanceCrossVpcVipResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AllocateHostInstanceCrossVpcVipResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AllocateHostInstanceCrossVpcVipResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AllocateHostInstanceCrossVpcVipResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        order_id: int = None,
        host_type: str = None,
        host_status: str = None,
        allocation_status: str = None,
        zone_id: str = None,
        dedicated_host_id: str = None,
        page_numbers: int = None,
        page_size: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.order_id = order_id
        self.host_type = host_type
        self.host_status = host_status
        self.allocation_status = allocation_status
        self.zone_id = zone_id
        self.dedicated_host_id = dedicated_host_id
        self.page_numbers = page_numbers
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts(TeaModel):
    def __init__(
        self,
        deploy_type: str = None,
        host_type: str = None,
        host_storage: str = None,
        memory_used: str = None,
        dedicated_host_group_id: str = None,
        allocation_status: str = None,
        storage_used: str = None,
        ecs_class_code: str = None,
        dedicated_host_id: str = None,
        mem_allocation_ratio: str = None,
        created_time: str = None,
        ipaddress: str = None,
        host_status: str = None,
        host_name: str = None,
        host_cpu: str = None,
        cpu_used: str = None,
        instance_number: str = None,
        open_permission: str = None,
        distribution_symbol: str = None,
        vpcid: str = None,
        host_class: str = None,
        end_time: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
        cpuallocation_ratio: str = None,
        image_category: str = None,
        engine: str = None,
        disk_allocation_ratio: str = None,
        host_mem: str = None,
        bastion_instance_id: str = None,
        account_name: str = None,
    ):
        self.deploy_type = deploy_type
        self.host_type = host_type
        self.host_storage = host_storage
        self.memory_used = memory_used
        self.dedicated_host_group_id = dedicated_host_group_id
        self.allocation_status = allocation_status
        self.storage_used = storage_used
        self.ecs_class_code = ecs_class_code
        self.dedicated_host_id = dedicated_host_id
        self.mem_allocation_ratio = mem_allocation_ratio
        self.created_time = created_time
        self.ipaddress = ipaddress
        self.host_status = host_status
        self.host_name = host_name
        self.host_cpu = host_cpu
        self.cpu_used = cpu_used
        self.instance_number = instance_number
        self.open_permission = open_permission
        self.distribution_symbol = distribution_symbol
        self.vpcid = vpcid
        self.host_class = host_class
        self.end_time = end_time
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id
        self.cpuallocation_ratio = cpuallocation_ratio
        self.image_category = image_category
        self.engine = engine
        self.disk_allocation_ratio = disk_allocation_ratio
        self.host_mem = host_mem
        self.bastion_instance_id = bastion_instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.distribution_symbol is not None:
            result['DistributionSymbol'] = self.distribution_symbol
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('DistributionSymbol') is not None:
            self.distribution_symbol = m.get('DistributionSymbol')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeDedicatedHostsResponseBodyDedicatedHosts(TeaModel):
    def __init__(
        self,
        dedicated_hosts: List[DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts] = None,
    ):
        self.dedicated_hosts = dedicated_hosts

    def validate(self):
        if self.dedicated_hosts:
            for k in self.dedicated_hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedHosts'] = []
        if self.dedicated_hosts is not None:
            for k in self.dedicated_hosts:
                result['DedicatedHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicated_hosts = []
        if m.get('DedicatedHosts') is not None:
            for k in m.get('DedicatedHosts'):
                temp_model = DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts()
                self.dedicated_hosts.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostsResponseBody(TeaModel):
    def __init__(
        self,
        total_records: int = None,
        page_size: int = None,
        request_id: str = None,
        page_numbers: int = None,
        dedicated_host_group_id: str = None,
        dedicated_hosts: DescribeDedicatedHostsResponseBodyDedicatedHosts = None,
    ):
        self.total_records = total_records
        self.page_size = page_size
        self.request_id = request_id
        self.page_numbers = page_numbers
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_hosts = dedicated_hosts

    def validate(self):
        if self.dedicated_hosts:
            self.dedicated_hosts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_records is not None:
            result['TotalRecords'] = self.total_records
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_hosts is not None:
            result['DedicatedHosts'] = self.dedicated_hosts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHosts') is not None:
            temp_model = DescribeDedicatedHostsResponseBodyDedicatedHosts()
            self.dedicated_hosts = temp_model.from_map(m['DedicatedHosts'])
        return self


class DescribeDedicatedHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostDisksRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_id = dedicated_host_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDedicatedHostDisksResponseBodyDisks(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        performance_level: str = None,
        disk_id: str = None,
        max_throughput: int = None,
        max_iops: int = None,
        has_dbinstance: bool = None,
        device: str = None,
        size: int = None,
        zone_id: str = None,
        category: str = None,
        dbinstance_id: str = None,
    ):
        self.type = type
        self.status = status
        self.performance_level = performance_level
        self.disk_id = disk_id
        self.max_throughput = max_throughput
        self.max_iops = max_iops
        self.has_dbinstance = has_dbinstance
        self.device = device
        self.size = size
        self.zone_id = zone_id
        self.category = category
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.status is not None:
            result['Status'] = self.status
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.max_throughput is not None:
            result['MaxThroughput'] = self.max_throughput
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.has_dbinstance is not None:
            result['HasDBInstance'] = self.has_dbinstance
        if self.device is not None:
            result['Device'] = self.device
        if self.size is not None:
            result['Size'] = self.size
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.category is not None:
            result['Category'] = self.category
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('MaxThroughput') is not None:
            self.max_throughput = m.get('MaxThroughput')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('HasDBInstance') is not None:
            self.has_dbinstance = m.get('HasDBInstance')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeDedicatedHostDisksResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        disks: List[DescribeDedicatedHostDisksResponseBodyDisks] = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.request_id = request_id
        self.disks = disks

    def validate(self):
        if self.disks:
            for k in self.disks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDedicatedHostDisksResponseBodyDisks()
                self.disks.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostDisksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedHostDisksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostDisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMyBaseInstanceOverViewRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        region: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModelInstanceModelsInstanceModel(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        pay_type: str = None,
        zone_id: str = None,
        dbinstance_id: str = None,
        dbinstance_status: str = None,
        created_time: str = None,
    ):
        self.expire_time = expire_time
        self.pay_type = pay_type
        self.zone_id = zone_id
        self.dbinstance_id = dbinstance_id
        self.dbinstance_status = dbinstance_status
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModelInstanceModels(TeaModel):
    def __init__(
        self,
        instance_model: List[DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModelInstanceModelsInstanceModel] = None,
    ):
        self.instance_model = instance_model

    def validate(self):
        if self.instance_model:
            for k in self.instance_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceModel'] = []
        if self.instance_model is not None:
            for k in self.instance_model:
                result['InstanceModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_model = []
        if m.get('InstanceModel') is not None:
            for k in m.get('InstanceModel'):
                temp_model = DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModelInstanceModelsInstanceModel()
                self.instance_model.append(temp_model.from_map(k))
        return self


class DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModel(TeaModel):
    def __init__(
        self,
        count: int = None,
        instance_date_type: str = None,
        instance_engine_count: str = None,
        instance_models: DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModelInstanceModels = None,
    ):
        self.count = count
        self.instance_date_type = instance_date_type
        self.instance_engine_count = instance_engine_count
        self.instance_models = instance_models

    def validate(self):
        if self.instance_models:
            self.instance_models.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_date_type is not None:
            result['InstanceDateType'] = self.instance_date_type
        if self.instance_engine_count is not None:
            result['InstanceEngineCount'] = self.instance_engine_count
        if self.instance_models is not None:
            result['InstanceModels'] = self.instance_models.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceDateType') is not None:
            self.instance_date_type = m.get('InstanceDateType')
        if m.get('InstanceEngineCount') is not None:
            self.instance_engine_count = m.get('InstanceEngineCount')
        if m.get('InstanceModels') is not None:
            temp_model = DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModelInstanceModels()
            self.instance_models = temp_model.from_map(m['InstanceModels'])
        return self


class DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModels(TeaModel):
    def __init__(
        self,
        type_model: List[DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModel] = None,
    ):
        self.type_model = type_model

    def validate(self):
        if self.type_model:
            for k in self.type_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TypeModel'] = []
        if self.type_model is not None:
            for k in self.type_model:
                result['TypeModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.type_model = []
        if m.get('TypeModel') is not None:
            for k in m.get('TypeModel'):
                temp_model = DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModelsTypeModel()
                self.type_model.append(temp_model.from_map(k))
        return self


class DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModel(TeaModel):
    def __init__(
        self,
        engine_count: str = None,
        total_count: int = None,
        region: str = None,
        type_models: DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModels = None,
    ):
        self.engine_count = engine_count
        self.total_count = total_count
        self.region = region
        self.type_models = type_models

    def validate(self):
        if self.type_models:
            self.type_models.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_count is not None:
            result['EngineCount'] = self.engine_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.region is not None:
            result['Region'] = self.region
        if self.type_models is not None:
            result['TypeModels'] = self.type_models.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineCount') is not None:
            self.engine_count = m.get('EngineCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TypeModels') is not None:
            temp_model = DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModelTypeModels()
            self.type_models = temp_model.from_map(m['TypeModels'])
        return self


class DescribeMyBaseInstanceOverViewResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_model: List[DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModel] = None,
    ):
        self.region_model = region_model

    def validate(self):
        if self.region_model:
            for k in self.region_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionModel'] = []
        if self.region_model is not None:
            for k in self.region_model:
                result['RegionModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_model = []
        if m.get('RegionModel') is not None:
            for k in m.get('RegionModel'):
                temp_model = DescribeMyBaseInstanceOverViewResponseBodyRegionsRegionModel()
                self.region_model.append(temp_model.from_map(k))
        return self


class DescribeMyBaseInstanceOverViewResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeMyBaseInstanceOverViewResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeMyBaseInstanceOverViewResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeMyBaseInstanceOverViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMyBaseInstanceOverViewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeMyBaseInstanceOverViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScheduleMethodRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_group_id: str = None,
        engine: str = None,
        instance_distribution: str = None,
        zone_distribution: str = None,
        cpu_utility_threshold: str = None,
        memory_utility_threshold: str = None,
        local_disk_utility_threshold: str = None,
        zones_order: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.engine = engine
        self.instance_distribution = instance_distribution
        self.zone_distribution = zone_distribution
        self.cpu_utility_threshold = cpu_utility_threshold
        self.memory_utility_threshold = memory_utility_threshold
        self.local_disk_utility_threshold = local_disk_utility_threshold
        self.zones_order = zones_order
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_distribution is not None:
            result['InstanceDistribution'] = self.instance_distribution
        if self.zone_distribution is not None:
            result['ZoneDistribution'] = self.zone_distribution
        if self.cpu_utility_threshold is not None:
            result['CpuUtilityThreshold'] = self.cpu_utility_threshold
        if self.memory_utility_threshold is not None:
            result['MemoryUtilityThreshold'] = self.memory_utility_threshold
        if self.local_disk_utility_threshold is not None:
            result['LocalDiskUtilityThreshold'] = self.local_disk_utility_threshold
        if self.zones_order is not None:
            result['ZonesOrder'] = self.zones_order
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceDistribution') is not None:
            self.instance_distribution = m.get('InstanceDistribution')
        if m.get('ZoneDistribution') is not None:
            self.zone_distribution = m.get('ZoneDistribution')
        if m.get('CpuUtilityThreshold') is not None:
            self.cpu_utility_threshold = m.get('CpuUtilityThreshold')
        if m.get('MemoryUtilityThreshold') is not None:
            self.memory_utility_threshold = m.get('MemoryUtilityThreshold')
        if m.get('LocalDiskUtilityThreshold') is not None:
            self.local_disk_utility_threshold = m.get('LocalDiskUtilityThreshold')
        if m.get('ZonesOrder') is not None:
            self.zones_order = m.get('ZonesOrder')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyScheduleMethodResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyScheduleMethodResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyScheduleMethodResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyScheduleMethodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableDedicatedHostClassesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        zone_id: str = None,
        storage_type: str = None,
        db_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.zone_id = zone_id
        self.storage_type = storage_type
        self.db_type = db_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.db_type is not None:
            result['DbType'] = self.db_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        return self


class DescribeAvailableDedicatedHostClassesResponseBodyHostClassesHostClasses(TeaModel):
    def __init__(
        self,
        description: str = None,
        host_class_name: str = None,
    ):
        self.description = description
        self.host_class_name = host_class_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.host_class_name is not None:
            result['HostClassName'] = self.host_class_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HostClassName') is not None:
            self.host_class_name = m.get('HostClassName')
        return self


class DescribeAvailableDedicatedHostClassesResponseBodyHostClasses(TeaModel):
    def __init__(
        self,
        host_classes: List[DescribeAvailableDedicatedHostClassesResponseBodyHostClassesHostClasses] = None,
    ):
        self.host_classes = host_classes

    def validate(self):
        if self.host_classes:
            for k in self.host_classes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostClasses'] = []
        if self.host_classes is not None:
            for k in self.host_classes:
                result['HostClasses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_classes = []
        if m.get('HostClasses') is not None:
            for k in m.get('HostClasses'):
                temp_model = DescribeAvailableDedicatedHostClassesResponseBodyHostClassesHostClasses()
                self.host_classes.append(temp_model.from_map(k))
        return self


class DescribeAvailableDedicatedHostClassesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_classes: DescribeAvailableDedicatedHostClassesResponseBodyHostClasses = None,
    ):
        self.request_id = request_id
        self.host_classes = host_classes

    def validate(self):
        if self.host_classes:
            self.host_classes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.host_classes is not None:
            result['HostClasses'] = self.host_classes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HostClasses') is not None:
            temp_model = DescribeAvailableDedicatedHostClassesResponseBodyHostClasses()
            self.host_classes = temp_model.from_map(m['HostClasses'])
        return self


class DescribeAvailableDedicatedHostClassesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableDedicatedHostClassesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAvailableDedicatedHostClassesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCheckUserBackupFileRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        engine_version: str = None,
        bucket_region: str = None,
        backup_file: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.engine_version = engine_version
        self.bucket_region = bucket_region
        self.backup_file = backup_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.bucket_region is not None:
            result['BucketRegion'] = self.bucket_region
        if self.backup_file is not None:
            result['BackupFile'] = self.backup_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('BucketRegion') is not None:
            self.bucket_region = m.get('BucketRegion')
        if m.get('BackupFile') is not None:
            self.backup_file = m.get('BackupFile')
        return self


class DescribeCheckUserBackupFileResponseBody(TeaModel):
    def __init__(
        self,
        status: bool = None,
        dbinstance_name: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        self.status = status
        self.dbinstance_name = dbinstance_name
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeCheckUserBackupFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCheckUserBackupFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCheckUserBackupFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostPasswordRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        new_password: str = None,
        dedicated_host_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.new_password = new_password
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        return self


class ModifyDedicatedHostPasswordResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_name: str = None,
        request_id: str = None,
    ):
        self.dedicated_host_name = dedicated_host_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostPasswordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduleMethodsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        return self


class DescribeScheduleMethodsResponseBodyScheduleMethodList(TeaModel):
    def __init__(
        self,
        zones_order: str = None,
        zone_distribution: str = None,
        cpuutility_threshold: int = None,
        dedicated_host_group_desc: str = None,
        memory_utility_threshold: int = None,
        engine: str = None,
        instance_distribution: str = None,
        local_disk_utility_threshold: int = None,
        dedicated_host_group_id: str = None,
    ):
        self.zones_order = zones_order
        self.zone_distribution = zone_distribution
        self.cpuutility_threshold = cpuutility_threshold
        self.dedicated_host_group_desc = dedicated_host_group_desc
        self.memory_utility_threshold = memory_utility_threshold
        self.engine = engine
        self.instance_distribution = instance_distribution
        self.local_disk_utility_threshold = local_disk_utility_threshold
        self.dedicated_host_group_id = dedicated_host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zones_order is not None:
            result['ZonesOrder'] = self.zones_order
        if self.zone_distribution is not None:
            result['ZoneDistribution'] = self.zone_distribution
        if self.cpuutility_threshold is not None:
            result['CPUUtilityThreshold'] = self.cpuutility_threshold
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.memory_utility_threshold is not None:
            result['MemoryUtilityThreshold'] = self.memory_utility_threshold
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_distribution is not None:
            result['InstanceDistribution'] = self.instance_distribution
        if self.local_disk_utility_threshold is not None:
            result['LocalDiskUtilityThreshold'] = self.local_disk_utility_threshold
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZonesOrder') is not None:
            self.zones_order = m.get('ZonesOrder')
        if m.get('ZoneDistribution') is not None:
            self.zone_distribution = m.get('ZoneDistribution')
        if m.get('CPUUtilityThreshold') is not None:
            self.cpuutility_threshold = m.get('CPUUtilityThreshold')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('MemoryUtilityThreshold') is not None:
            self.memory_utility_threshold = m.get('MemoryUtilityThreshold')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceDistribution') is not None:
            self.instance_distribution = m.get('InstanceDistribution')
        if m.get('LocalDiskUtilityThreshold') is not None:
            self.local_disk_utility_threshold = m.get('LocalDiskUtilityThreshold')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        return self


class DescribeScheduleMethodsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        schedule_method_list: List[DescribeScheduleMethodsResponseBodyScheduleMethodList] = None,
    ):
        self.request_id = request_id
        self.schedule_method_list = schedule_method_list

    def validate(self):
        if self.schedule_method_list:
            for k in self.schedule_method_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScheduleMethodList'] = []
        if self.schedule_method_list is not None:
            for k in self.schedule_method_list:
                result['ScheduleMethodList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.schedule_method_list = []
        if m.get('ScheduleMethodList') is not None:
            for k in m.get('ScheduleMethodList'):
                temp_model = DescribeScheduleMethodsResponseBodyScheduleMethodList()
                self.schedule_method_list.append(temp_model.from_map(k))
        return self


class DescribeScheduleMethodsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScheduleMethodsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScheduleMethodsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_id: str = None,
        failover_mode: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id
        self.failover_mode = failover_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        return self


class ClearDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ClearDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClearDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ClearDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserBackupFileRecordRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        engine: str = None,
        ops_service_version: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.engine = engine
        self.ops_service_version = ops_service_version
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.ops_service_version is not None:
            result['OpsServiceVersion'] = self.ops_service_version
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('OpsServiceVersion') is not None:
            self.ops_service_version = m.get('OpsServiceVersion')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteUserBackupFileRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: str = None,
        id: str = None,
        instance_name: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.id = id
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class DeleteUserBackupFileRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserBackupFileRecordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserBackupFileRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEvaluateDedicatedHostsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        class_code: str = None,
        engine: str = None,
        engine_version: str = None,
        zone_id: str = None,
        dedicated_host_id: str = None,
        storage_type: str = None,
        storage_size: int = None,
        node_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.class_code = class_code
        self.engine = engine
        self.engine_version = engine_version
        self.zone_id = zone_id
        self.dedicated_host_id = dedicated_host_id
        self.storage_type = storage_type
        self.storage_size = storage_size
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.class_code is not None:
            result['ClassCode'] = self.class_code
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeEvaluateDedicatedHostsResponseBodyDedicatedHosts(TeaModel):
    def __init__(
        self,
        host_allocation_status: bool = None,
        comment: str = None,
        host_free_mem: int = None,
        host_status: str = None,
        host_free_cpu: int = None,
        host_storage: int = None,
        host_cpu: int = None,
        region_id: str = None,
        host_free_storage: int = None,
        v_switch_id: str = None,
        dedicated_host_name: str = None,
        zone_id: str = None,
        image_category: str = None,
        dedicated_host_id: str = None,
        engine: str = None,
        is_could_ssd: bool = None,
        is_available_for_instance: bool = None,
        host_mem: int = None,
        created_time: int = None,
        ipaddress: str = None,
    ):
        self.host_allocation_status = host_allocation_status
        self.comment = comment
        self.host_free_mem = host_free_mem
        self.host_status = host_status
        self.host_free_cpu = host_free_cpu
        self.host_storage = host_storage
        self.host_cpu = host_cpu
        self.region_id = region_id
        self.host_free_storage = host_free_storage
        self.v_switch_id = v_switch_id
        self.dedicated_host_name = dedicated_host_name
        self.zone_id = zone_id
        self.image_category = image_category
        self.dedicated_host_id = dedicated_host_id
        self.engine = engine
        self.is_could_ssd = is_could_ssd
        self.is_available_for_instance = is_available_for_instance
        self.host_mem = host_mem
        self.created_time = created_time
        self.ipaddress = ipaddress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_allocation_status is not None:
            result['HostAllocationStatus'] = self.host_allocation_status
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_free_mem is not None:
            result['HostFreeMem'] = self.host_free_mem
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_free_cpu is not None:
            result['HostFreeCPU'] = self.host_free_cpu
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_free_storage is not None:
            result['HostFreeStorage'] = self.host_free_storage
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_could_ssd is not None:
            result['IsCouldSSD'] = self.is_could_ssd
        if self.is_available_for_instance is not None:
            result['IsAvailableForInstance'] = self.is_available_for_instance
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAllocationStatus') is not None:
            self.host_allocation_status = m.get('HostAllocationStatus')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostFreeMem') is not None:
            self.host_free_mem = m.get('HostFreeMem')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostFreeCPU') is not None:
            self.host_free_cpu = m.get('HostFreeCPU')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostFreeStorage') is not None:
            self.host_free_storage = m.get('HostFreeStorage')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsCouldSSD') is not None:
            self.is_could_ssd = m.get('IsCouldSSD')
        if m.get('IsAvailableForInstance') is not None:
            self.is_available_for_instance = m.get('IsAvailableForInstance')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        return self


class DescribeEvaluateDedicatedHostsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_required_cpu: int = None,
        cpu_over_allocation_ratio: int = None,
        memory_over_allocation_ratio: int = None,
        instance_required_memory: int = None,
        instance_class_code: str = None,
        instance_required_storage: int = None,
        disk_over_allocation_ratio: int = None,
        dedicated_host_group_id: str = None,
        dedicated_hosts: List[DescribeEvaluateDedicatedHostsResponseBodyDedicatedHosts] = None,
    ):
        self.request_id = request_id
        self.instance_required_cpu = instance_required_cpu
        self.cpu_over_allocation_ratio = cpu_over_allocation_ratio
        self.memory_over_allocation_ratio = memory_over_allocation_ratio
        self.instance_required_memory = instance_required_memory
        self.instance_class_code = instance_class_code
        self.instance_required_storage = instance_required_storage
        self.disk_over_allocation_ratio = disk_over_allocation_ratio
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_hosts = dedicated_hosts

    def validate(self):
        if self.dedicated_hosts:
            for k in self.dedicated_hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_required_cpu is not None:
            result['InstanceRequiredCPU'] = self.instance_required_cpu
        if self.cpu_over_allocation_ratio is not None:
            result['CpuOverAllocationRatio'] = self.cpu_over_allocation_ratio
        if self.memory_over_allocation_ratio is not None:
            result['MemoryOverAllocationRatio'] = self.memory_over_allocation_ratio
        if self.instance_required_memory is not None:
            result['InstanceRequiredMemory'] = self.instance_required_memory
        if self.instance_class_code is not None:
            result['InstanceClassCode'] = self.instance_class_code
        if self.instance_required_storage is not None:
            result['InstanceRequiredStorage'] = self.instance_required_storage
        if self.disk_over_allocation_ratio is not None:
            result['DiskOverAllocationRatio'] = self.disk_over_allocation_ratio
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DedicatedHosts'] = []
        if self.dedicated_hosts is not None:
            for k in self.dedicated_hosts:
                result['DedicatedHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceRequiredCPU') is not None:
            self.instance_required_cpu = m.get('InstanceRequiredCPU')
        if m.get('CpuOverAllocationRatio') is not None:
            self.cpu_over_allocation_ratio = m.get('CpuOverAllocationRatio')
        if m.get('MemoryOverAllocationRatio') is not None:
            self.memory_over_allocation_ratio = m.get('MemoryOverAllocationRatio')
        if m.get('InstanceRequiredMemory') is not None:
            self.instance_required_memory = m.get('InstanceRequiredMemory')
        if m.get('InstanceClassCode') is not None:
            self.instance_class_code = m.get('InstanceClassCode')
        if m.get('InstanceRequiredStorage') is not None:
            self.instance_required_storage = m.get('InstanceRequiredStorage')
        if m.get('DiskOverAllocationRatio') is not None:
            self.disk_over_allocation_ratio = m.get('DiskOverAllocationRatio')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.dedicated_hosts = []
        if m.get('DedicatedHosts') is not None:
            for k in m.get('DedicatedHosts'):
                temp_model = DescribeEvaluateDedicatedHostsResponseBodyDedicatedHosts()
                self.dedicated_hosts.append(temp_model.from_map(k))
        return self


class DescribeEvaluateDedicatedHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEvaluateDedicatedHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEvaluateDedicatedHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostInstanceMonitorInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_id: str = None,
        region_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_id = dedicated_host_id
        self.region_id = region_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeHostInstanceMonitorInfoResponseBodyItemsAuroraSwitchInstanceLog(TeaModel):
    def __init__(
        self,
        switch_from: float = None,
        switch_type: float = None,
        switch_time: int = None,
    ):
        self.switch_from = switch_from
        self.switch_type = switch_type
        self.switch_time = switch_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.switch_from is not None:
            result['SwitchFrom'] = self.switch_from
        if self.switch_type is not None:
            result['SwitchType'] = self.switch_type
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchFrom') is not None:
            self.switch_from = m.get('SwitchFrom')
        if m.get('SwitchType') is not None:
            self.switch_type = m.get('SwitchType')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        return self


class DescribeHostInstanceMonitorInfoResponseBodyItems(TeaModel):
    def __init__(
        self,
        status: str = None,
        mem_size: int = None,
        disk_size: int = None,
        ip: str = None,
        dbinstance_id: str = None,
        level_name: str = None,
        engine: str = None,
        role: str = None,
        port: str = None,
        cpu_cores: int = None,
        engine_version: str = None,
        aurora_switch_instance_log: DescribeHostInstanceMonitorInfoResponseBodyItemsAuroraSwitchInstanceLog = None,
    ):
        self.status = status
        self.mem_size = mem_size
        self.disk_size = disk_size
        self.ip = ip
        self.dbinstance_id = dbinstance_id
        self.level_name = level_name
        self.engine = engine
        self.role = role
        self.port = port
        self.cpu_cores = cpu_cores
        self.engine_version = engine_version
        self.aurora_switch_instance_log = aurora_switch_instance_log

    def validate(self):
        if self.aurora_switch_instance_log:
            self.aurora_switch_instance_log.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.level_name is not None:
            result['LevelName'] = self.level_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.role is not None:
            result['Role'] = self.role
        if self.port is not None:
            result['Port'] = self.port
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.aurora_switch_instance_log is not None:
            result['AuroraSwitchInstanceLog'] = self.aurora_switch_instance_log.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('AuroraSwitchInstanceLog') is not None:
            temp_model = DescribeHostInstanceMonitorInfoResponseBodyItemsAuroraSwitchInstanceLog()
            self.aurora_switch_instance_log = temp_model.from_map(m['AuroraSwitchInstanceLog'])
        return self


class DescribeHostInstanceMonitorInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        items: List[DescribeHostInstanceMonitorInfoResponseBodyItems] = None,
    ):
        self.request_id = request_id
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeHostInstanceMonitorInfoResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeHostInstanceMonitorInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHostInstanceMonitorInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHostInstanceMonitorInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostMetricRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_group_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDedicatedHostMetricResponseBodyMetricsMetricsRisks(TeaModel):
    def __init__(
        self,
        risks: List[str] = None,
    ):
        self.risks = risks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risks is not None:
            result['Risks'] = self.risks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Risks') is not None:
            self.risks = m.get('Risks')
        return self


class DescribeDedicatedHostMetricResponseBodyMetricsMetrics(TeaModel):
    def __init__(
        self,
        avg_mem_usage: float = None,
        end_date: str = None,
        avg_iops: int = None,
        max_mem_usage: float = None,
        start_date: str = None,
        dedicated_host_id: str = None,
        max_iops: int = None,
        avg_cpu_usage: float = None,
        disk_usage: float = None,
        max_cpu_usage: float = None,
        risks: DescribeDedicatedHostMetricResponseBodyMetricsMetricsRisks = None,
    ):
        self.avg_mem_usage = avg_mem_usage
        self.end_date = end_date
        self.avg_iops = avg_iops
        self.max_mem_usage = max_mem_usage
        self.start_date = start_date
        self.dedicated_host_id = dedicated_host_id
        self.max_iops = max_iops
        self.avg_cpu_usage = avg_cpu_usage
        self.disk_usage = disk_usage
        self.max_cpu_usage = max_cpu_usage
        self.risks = risks

    def validate(self):
        if self.risks:
            self.risks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_mem_usage is not None:
            result['AvgMemUsage'] = self.avg_mem_usage
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.avg_iops is not None:
            result['AvgIops'] = self.avg_iops
        if self.max_mem_usage is not None:
            result['MaxMemUsage'] = self.max_mem_usage
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.max_iops is not None:
            result['MaxIops'] = self.max_iops
        if self.avg_cpu_usage is not None:
            result['AvgCpuUsage'] = self.avg_cpu_usage
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage
        if self.max_cpu_usage is not None:
            result['MaxCpuUsage'] = self.max_cpu_usage
        if self.risks is not None:
            result['Risks'] = self.risks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgMemUsage') is not None:
            self.avg_mem_usage = m.get('AvgMemUsage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('AvgIops') is not None:
            self.avg_iops = m.get('AvgIops')
        if m.get('MaxMemUsage') is not None:
            self.max_mem_usage = m.get('MaxMemUsage')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('MaxIops') is not None:
            self.max_iops = m.get('MaxIops')
        if m.get('AvgCpuUsage') is not None:
            self.avg_cpu_usage = m.get('AvgCpuUsage')
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')
        if m.get('MaxCpuUsage') is not None:
            self.max_cpu_usage = m.get('MaxCpuUsage')
        if m.get('Risks') is not None:
            temp_model = DescribeDedicatedHostMetricResponseBodyMetricsMetricsRisks()
            self.risks = temp_model.from_map(m['Risks'])
        return self


class DescribeDedicatedHostMetricResponseBodyMetrics(TeaModel):
    def __init__(
        self,
        metrics: List[DescribeDedicatedHostMetricResponseBodyMetricsMetrics] = None,
    ):
        self.metrics = metrics

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeDedicatedHostMetricResponseBodyMetricsMetrics()
                self.metrics.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostMetricResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        request_id: str = None,
        metrics: DescribeDedicatedHostMetricResponseBodyMetrics = None,
    ):
        self.dedicated_host_group_id = dedicated_host_group_id
        self.request_id = request_id
        self.metrics = metrics

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Metrics') is not None:
            temp_model = DescribeDedicatedHostMetricResponseBodyMetrics()
            self.metrics = temp_model.from_map(m['Metrics'])
        return self


class DescribeDedicatedHostMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedHostMetricResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        host_name: str = None,
        zone_id: str = None,
        v_switch_id: str = None,
        host_class: str = None,
        pay_type: str = None,
        period: str = None,
        used_time: str = None,
        client_token: str = None,
        auto_renew: str = None,
        image_category: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.host_name = host_name
        self.zone_id = zone_id
        self.v_switch_id = v_switch_id
        self.host_class = host_class
        self.pay_type = pay_type
        self.period = period
        self.used_time = used_time
        self.client_token = client_token
        self.auto_renew = auto_renew
        self.image_category = image_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        return self


class CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
    ):
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        return self


class CreateDedicatedHostResponseBodyDedicateHostList(TeaModel):
    def __init__(
        self,
        dedicate_host_list: List[CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList] = None,
    ):
        self.dedicate_host_list = dedicate_host_list

    def validate(self):
        if self.dedicate_host_list:
            for k in self.dedicate_host_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicateHostList'] = []
        if self.dedicate_host_list is not None:
            for k in self.dedicate_host_list:
                result['DedicateHostList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dedicate_host_list = []
        if m.get('DedicateHostList') is not None:
            for k in m.get('DedicateHostList'):
                temp_model = CreateDedicatedHostResponseBodyDedicateHostListDedicateHostList()
                self.dedicate_host_list.append(temp_model.from_map(k))
        return self


class CreateDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
        dedicate_host_list: CreateDedicatedHostResponseBodyDedicateHostList = None,
    ):
        self.order_id = order_id
        self.request_id = request_id
        self.dedicate_host_list = dedicate_host_list

    def validate(self):
        if self.dedicate_host_list:
            self.dedicate_host_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dedicate_host_list is not None:
            result['DedicateHostList'] = self.dedicate_host_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DedicateHostList') is not None:
            temp_model = CreateDedicatedHostResponseBodyDedicateHostList()
            self.dedicate_host_list = temp_model.from_map(m['DedicateHostList'])
        return self


class CreateDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedInstanceMetricRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_id = dedicated_host_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDedicatedInstanceMetricResponseBodyMetricsMetricsRisks(TeaModel):
    def __init__(
        self,
        risks: List[str] = None,
    ):
        self.risks = risks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risks is not None:
            result['Risks'] = self.risks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Risks') is not None:
            self.risks = m.get('Risks')
        return self


class DescribeDedicatedInstanceMetricResponseBodyMetricsMetrics(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        max_mem_usage: float = None,
        dedicated_instance_id: str = None,
        start_date: str = None,
        disk_usage: float = None,
        avg_mem_usage: float = None,
        max_iops: int = None,
        memory: float = None,
        avg_cpu_usage: float = None,
        avg_iops: int = None,
        role: str = None,
        max_cpu_usage: float = None,
        risks: DescribeDedicatedInstanceMetricResponseBodyMetricsMetricsRisks = None,
    ):
        self.end_date = end_date
        self.max_mem_usage = max_mem_usage
        self.dedicated_instance_id = dedicated_instance_id
        self.start_date = start_date
        self.disk_usage = disk_usage
        self.avg_mem_usage = avg_mem_usage
        self.max_iops = max_iops
        self.memory = memory
        self.avg_cpu_usage = avg_cpu_usage
        self.avg_iops = avg_iops
        self.role = role
        self.max_cpu_usage = max_cpu_usage
        self.risks = risks

    def validate(self):
        if self.risks:
            self.risks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.max_mem_usage is not None:
            result['MaxMemUsage'] = self.max_mem_usage
        if self.dedicated_instance_id is not None:
            result['DedicatedInstanceId'] = self.dedicated_instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage
        if self.avg_mem_usage is not None:
            result['AvgMemUsage'] = self.avg_mem_usage
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.avg_cpu_usage is not None:
            result['AvgCpuUsage'] = self.avg_cpu_usage
        if self.avg_iops is not None:
            result['AvgIOPS'] = self.avg_iops
        if self.role is not None:
            result['Role'] = self.role
        if self.max_cpu_usage is not None:
            result['MaxCpuUsage'] = self.max_cpu_usage
        if self.risks is not None:
            result['Risks'] = self.risks.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('MaxMemUsage') is not None:
            self.max_mem_usage = m.get('MaxMemUsage')
        if m.get('DedicatedInstanceId') is not None:
            self.dedicated_instance_id = m.get('DedicatedInstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')
        if m.get('AvgMemUsage') is not None:
            self.avg_mem_usage = m.get('AvgMemUsage')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('AvgCpuUsage') is not None:
            self.avg_cpu_usage = m.get('AvgCpuUsage')
        if m.get('AvgIOPS') is not None:
            self.avg_iops = m.get('AvgIOPS')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('MaxCpuUsage') is not None:
            self.max_cpu_usage = m.get('MaxCpuUsage')
        if m.get('Risks') is not None:
            temp_model = DescribeDedicatedInstanceMetricResponseBodyMetricsMetricsRisks()
            self.risks = temp_model.from_map(m['Risks'])
        return self


class DescribeDedicatedInstanceMetricResponseBodyMetrics(TeaModel):
    def __init__(
        self,
        metrics: List[DescribeDedicatedInstanceMetricResponseBodyMetricsMetrics] = None,
    ):
        self.metrics = metrics

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeDedicatedInstanceMetricResponseBodyMetricsMetrics()
                self.metrics.append(temp_model.from_map(k))
        return self


class DescribeDedicatedInstanceMetricResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        metrics: DescribeDedicatedInstanceMetricResponseBodyMetrics = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.request_id = request_id
        self.metrics = metrics

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Metrics') is not None:
            temp_model = DescribeDedicatedInstanceMetricResponseBodyMetrics()
            self.metrics = temp_model.from_map(m['Metrics'])
        return self


class DescribeDedicatedInstanceMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedInstanceMetricResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedInstanceMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCrossVpcInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dbinstance_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class DescribeCrossVpcInstanceResponseBodyItems(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
    ):
        self.connection_string = connection_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        return self


class DescribeCrossVpcInstanceResponseBody(TeaModel):
    def __init__(
        self,
        has_del_in_process_task: bool = None,
        request_id: str = None,
        has_create_in_process_task: bool = None,
        items: List[DescribeCrossVpcInstanceResponseBodyItems] = None,
    ):
        self.has_del_in_process_task = has_del_in_process_task
        self.request_id = request_id
        self.has_create_in_process_task = has_create_in_process_task
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_del_in_process_task is not None:
            result['HasDelInProcessTask'] = self.has_del_in_process_task
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.has_create_in_process_task is not None:
            result['HasCreateInProcessTask'] = self.has_create_in_process_task
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasDelInProcessTask') is not None:
            self.has_del_in_process_task = m.get('HasDelInProcessTask')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HasCreateInProcessTask') is not None:
            self.has_create_in_process_task = m.get('HasCreateInProcessTask')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeCrossVpcInstanceResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class DescribeCrossVpcInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCrossVpcInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeCrossVpcInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostClassRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_id: str = None,
        target_class_code: str = None,
        switch_time: str = None,
        switch_time_mode: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id
        self.target_class_code = target_class_code
        self.switch_time = switch_time
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.target_class_code is not None:
            result['TargetClassCode'] = self.target_class_code
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('TargetClassCode') is not None:
            self.target_class_code = m.get('TargetClassCode')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class ModifyDedicatedHostClassResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyDedicatedHostClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostClassResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostsCheckInBastionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        bastion_instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.bastion_instance_id = bastion_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        return self


class DescribeDedicatedHostsCheckInBastionResponseBodyHosts(TeaModel):
    def __init__(
        self,
        status: str = None,
        dedicated_host_name: str = None,
        allocation_status: bool = None,
        in_bastion: bool = None,
        host_name: str = None,
        ip: str = None,
    ):
        self.status = status
        self.dedicated_host_name = dedicated_host_name
        self.allocation_status = allocation_status
        self.in_bastion = in_bastion
        self.host_name = host_name
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.in_bastion is not None:
            result['InBastion'] = self.in_bastion
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('InBastion') is not None:
            self.in_bastion = m.get('InBastion')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeDedicatedHostsCheckInBastionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bastion_instance_id: str = None,
        dedicated_host_group_id: str = None,
        hosts: List[DescribeDedicatedHostsCheckInBastionResponseBodyHosts] = None,
    ):
        self.request_id = request_id
        self.bastion_instance_id = bastion_instance_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.hosts = hosts

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = DescribeDedicatedHostsCheckInBastionResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostsCheckInBastionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedHostsCheckInBastionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostsCheckInBastionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropDedicatedHostUserRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_name: str = None,
        user_name: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_name = dedicated_host_name
        self.user_name = user_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DropDedicatedHostUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DropDedicatedHostUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DropDedicatedHostUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DropDedicatedHostUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostsInBastionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        bastion_instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.bastion_instance_id = bastion_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        return self


class DescribeDedicatedHostsInBastionResponseBodyHosts(TeaModel):
    def __init__(
        self,
        host_description: str = None,
        comment: str = None,
        bastion_host_id: str = None,
        os_name: str = None,
        host_account_count: str = None,
        dedicated_host_id: str = None,
        host_private_ip: str = None,
        account_creating: bool = None,
        account_name: str = None,
    ):
        self.host_description = host_description
        self.comment = comment
        self.bastion_host_id = bastion_host_id
        self.os_name = os_name
        self.host_account_count = host_account_count
        self.dedicated_host_id = dedicated_host_id
        self.host_private_ip = host_private_ip
        self.account_creating = account_creating
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_description is not None:
            result['HostDescription'] = self.host_description
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.bastion_host_id is not None:
            result['BastionHostId'] = self.bastion_host_id
        if self.os_name is not None:
            result['OsName'] = self.os_name
        if self.host_account_count is not None:
            result['HostAccountCount'] = self.host_account_count
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.host_private_ip is not None:
            result['HostPrivateIp'] = self.host_private_ip
        if self.account_creating is not None:
            result['AccountCreating'] = self.account_creating
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostDescription') is not None:
            self.host_description = m.get('HostDescription')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('BastionHostId') is not None:
            self.bastion_host_id = m.get('BastionHostId')
        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')
        if m.get('HostAccountCount') is not None:
            self.host_account_count = m.get('HostAccountCount')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('HostPrivateIp') is not None:
            self.host_private_ip = m.get('HostPrivateIp')
        if m.get('AccountCreating') is not None:
            self.account_creating = m.get('AccountCreating')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeDedicatedHostsInBastionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bastion_instance_id: str = None,
        dedicated_host_group_id: str = None,
        hosts: List[DescribeDedicatedHostsInBastionResponseBodyHosts] = None,
    ):
        self.request_id = request_id
        self.bastion_instance_id = bastion_instance_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.hosts = hosts

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = DescribeDedicatedHostsInBastionResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostsInBastionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedHostsInBastionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostsInBastionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_group_desc: str = None,
        cpu_allocation_ratio: int = None,
        mem_allocation_ratio: int = None,
        disk_allocation_ratio: int = None,
        allocation_policy: str = None,
        host_replace_policy: str = None,
        open_permission: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_host_group_desc = dedicated_host_group_desc
        self.cpu_allocation_ratio = cpu_allocation_ratio
        self.mem_allocation_ratio = mem_allocation_ratio
        self.disk_allocation_ratio = disk_allocation_ratio
        self.allocation_policy = allocation_policy
        self.host_replace_policy = host_replace_policy
        self.open_permission = open_permission

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        return self


class ModifyDedicatedHostGroupAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostGroupAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHostInstanceConsoleInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        return self


class QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo(TeaModel):
    def __init__(
        self,
        perf_idb_pio: float = None,
        disk_curr: float = None,
        mem_ratio: float = None,
        cpu_ratio: float = None,
    ):
        self.perf_idb_pio = perf_idb_pio
        self.disk_curr = disk_curr
        self.mem_ratio = mem_ratio
        self.cpu_ratio = cpu_ratio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.perf_idb_pio is not None:
            result['PerfIdbPio'] = self.perf_idb_pio
        if self.disk_curr is not None:
            result['DiskCurr'] = self.disk_curr
        if self.mem_ratio is not None:
            result['MemRatio'] = self.mem_ratio
        if self.cpu_ratio is not None:
            result['CpuRatio'] = self.cpu_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerfIdbPio') is not None:
            self.perf_idb_pio = m.get('PerfIdbPio')
        if m.get('DiskCurr') is not None:
            self.disk_curr = m.get('DiskCurr')
        if m.get('MemRatio') is not None:
            self.mem_ratio = m.get('MemRatio')
        if m.get('CpuRatio') is not None:
            self.cpu_ratio = m.get('CpuRatio')
        return self


class QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos(TeaModel):
    def __init__(
        self,
        status: str = None,
        max_conn_increase_ratio_value: int = None,
        mem_size: int = None,
        disk_size: int = None,
        ip: str = None,
        port: str = None,
        engine_version: str = None,
        memory_increase_ratio_value: int = None,
        cpu_increase_ratio_value: int = None,
        dbinstance_id: str = None,
        engine: str = None,
        level_name: str = None,
        role: str = None,
        dbinstance_description: str = None,
        cpu_cores: int = None,
        perf_info: QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo = None,
    ):
        self.status = status
        self.max_conn_increase_ratio_value = max_conn_increase_ratio_value
        self.mem_size = mem_size
        self.disk_size = disk_size
        self.ip = ip
        self.port = port
        self.engine_version = engine_version
        self.memory_increase_ratio_value = memory_increase_ratio_value
        self.cpu_increase_ratio_value = cpu_increase_ratio_value
        self.dbinstance_id = dbinstance_id
        self.engine = engine
        self.level_name = level_name
        self.role = role
        self.dbinstance_description = dbinstance_description
        self.cpu_cores = cpu_cores
        self.perf_info = perf_info

    def validate(self):
        if self.perf_info:
            self.perf_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.max_conn_increase_ratio_value is not None:
            result['MaxConnIncreaseRatioValue'] = self.max_conn_increase_ratio_value
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.memory_increase_ratio_value is not None:
            result['MemoryIncreaseRatioValue'] = self.memory_increase_ratio_value
        if self.cpu_increase_ratio_value is not None:
            result['CpuIncreaseRatioValue'] = self.cpu_increase_ratio_value
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.level_name is not None:
            result['LevelName'] = self.level_name
        if self.role is not None:
            result['Role'] = self.role
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.perf_info is not None:
            result['PerfInfo'] = self.perf_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MaxConnIncreaseRatioValue') is not None:
            self.max_conn_increase_ratio_value = m.get('MaxConnIncreaseRatioValue')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('MemoryIncreaseRatioValue') is not None:
            self.memory_increase_ratio_value = m.get('MemoryIncreaseRatioValue')
        if m.get('CpuIncreaseRatioValue') is not None:
            self.cpu_increase_ratio_value = m.get('CpuIncreaseRatioValue')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('PerfInfo') is not None:
            temp_model = QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo()
            self.perf_info = temp_model.from_map(m['PerfInfo'])
        return self


class QueryHostInstanceConsoleInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_instance_console_infos: List[QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos] = None,
    ):
        self.request_id = request_id
        self.host_instance_console_infos = host_instance_console_infos

    def validate(self):
        if self.host_instance_console_infos:
            for k in self.host_instance_console_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostInstanceConsoleInfos'] = []
        if self.host_instance_console_infos is not None:
            for k in self.host_instance_console_infos:
                result['HostInstanceConsoleInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_instance_console_infos = []
        if m.get('HostInstanceConsoleInfos') is not None:
            for k in m.get('HostInstanceConsoleInfos'):
                temp_model = QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos()
                self.host_instance_console_infos.append(temp_model.from_map(k))
        return self


class QueryHostInstanceConsoleInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryHostInstanceConsoleInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryHostInstanceConsoleInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        resource_owner_id: int = None,
    ):
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeRegionsResponseBodyRegionsRDSRegion(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        region_id: str = None,
    ):
        self.zone_id = zone_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        rdsregion: List[DescribeRegionsResponseBodyRegionsRDSRegion] = None,
    ):
        self.rdsregion = rdsregion

    def validate(self):
        if self.rdsregion:
            for k in self.rdsregion:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RDSRegion'] = []
        if self.rdsregion is not None:
            for k in self.rdsregion:
                result['RDSRegion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rdsregion = []
        if m.get('RDSRegion') is not None:
            for k in m.get('RDSRegion'):
                temp_model = DescribeRegionsResponseBodyRegionsRDSRegion()
                self.rdsregion.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHostBaseInfoByInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dbinstance_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        status: str = None,
        expired_time: str = None,
        cluster_name: str = None,
        ip: str = None,
        host_name: str = None,
        engine: str = None,
        role: str = None,
        port: str = None,
        engine_version: str = None,
    ):
        self.vpc_id = vpc_id
        self.status = status
        self.expired_time = expired_time
        self.cluster_name = cluster_name
        self.ip = ip
        self.host_name = host_name
        self.engine = engine
        self.role = role
        self.port = port
        self.engine_version = engine_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.role is not None:
            result['Role'] = self.role
        if self.port is not None:
            result['Port'] = self.port
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        return self


class QueryHostBaseInfoByInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        host_instance_console_infos: List[QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos] = None,
    ):
        self.request_id = request_id
        self.host_instance_console_infos = host_instance_console_infos

    def validate(self):
        if self.host_instance_console_infos:
            for k in self.host_instance_console_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostInstanceConsoleInfos'] = []
        if self.host_instance_console_infos is not None:
            for k in self.host_instance_console_infos:
                result['HostInstanceConsoleInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_instance_console_infos = []
        if m.get('HostInstanceConsoleInfos') is not None:
            for k in m.get('HostInstanceConsoleInfos'):
                temp_model = QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos()
                self.host_instance_console_infos.append(temp_model.from_map(k))
        return self


class QueryHostBaseInfoByInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryHostBaseInfoByInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryHostBaseInfoByInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedInstanceDistributionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_group_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDedicatedInstanceDistributionResponseBody(TeaModel):
    def __init__(
        self,
        dbclass: Dict[str, Any] = None,
        dbversion: Dict[str, Any] = None,
        request_id: str = None,
        instance_count: int = None,
        dbtype: Dict[str, Any] = None,
        dedicated_host_group_id: str = None,
    ):
        self.dbclass = dbclass
        self.dbversion = dbversion
        self.request_id = request_id
        self.instance_count = instance_count
        self.dbtype = dbtype
        self.dedicated_host_group_id = dedicated_host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbclass is not None:
            result['DBClass'] = self.dbclass
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClass') is not None:
            self.dbclass = m.get('DBClass')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        return self


class DescribeDedicatedInstanceDistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedInstanceDistributionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedInstanceDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScheduleHostRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        schedule_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.schedule_id = schedule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        return self


class DescribeScheduleHostResponseBodyHostScheduleStatusList(TeaModel):
    def __init__(
        self,
        schedule_status: str = None,
        dedicated_host_id: str = None,
        instance_out_id: str = None,
        instance_in_id: str = None,
    ):
        self.schedule_status = schedule_status
        self.dedicated_host_id = dedicated_host_id
        self.instance_out_id = instance_out_id
        self.instance_in_id = instance_in_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_status is not None:
            result['ScheduleStatus'] = self.schedule_status
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.instance_out_id is not None:
            result['InstanceOutId'] = self.instance_out_id
        if self.instance_in_id is not None:
            result['InstanceInId'] = self.instance_in_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleStatus') is not None:
            self.schedule_status = m.get('ScheduleStatus')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('InstanceOutId') is not None:
            self.instance_out_id = m.get('InstanceOutId')
        if m.get('InstanceInId') is not None:
            self.instance_in_id = m.get('InstanceInId')
        return self


class DescribeScheduleHostResponseBody(TeaModel):
    def __init__(
        self,
        schedule_id: str = None,
        request_id: str = None,
        host_schedule_status_list: List[DescribeScheduleHostResponseBodyHostScheduleStatusList] = None,
    ):
        self.schedule_id = schedule_id
        self.request_id = request_id
        self.host_schedule_status_list = host_schedule_status_list

    def validate(self):
        if self.host_schedule_status_list:
            for k in self.host_schedule_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['HostScheduleStatusList'] = []
        if self.host_schedule_status_list is not None:
            for k in self.host_schedule_status_list:
                result['HostScheduleStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.host_schedule_status_list = []
        if m.get('HostScheduleStatusList') is not None:
            for k in m.get('HostScheduleStatusList'):
                temp_model = DescribeScheduleHostResponseBodyHostScheduleStatusList()
                self.host_schedule_status_list.append(temp_model.from_map(k))
        return self


class DescribeScheduleHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScheduleHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScheduleHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_id: str = None,
        host_name: str = None,
        allocation_status: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id
        self.host_name = host_name
        self.allocation_status = allocation_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        return self


class ModifyDedicatedHostAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDedicatedHostAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDedicatedHostAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        engine: str = None,
        cpu_allocation_ratio: int = None,
        mem_allocation_ratio: int = None,
        disk_allocation_ratio: int = None,
        allocation_policy: str = None,
        vpcid: str = None,
        host_replace_policy: str = None,
        client_token: str = None,
        open_permission: int = None,
        dedicated_host_group_desc: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.engine = engine
        self.cpu_allocation_ratio = cpu_allocation_ratio
        self.mem_allocation_ratio = mem_allocation_ratio
        self.disk_allocation_ratio = disk_allocation_ratio
        self.allocation_policy = allocation_policy
        self.vpcid = vpcid
        self.host_replace_policy = host_replace_policy
        self.client_token = client_token
        self.open_permission = open_permission
        self.dedicated_host_group_desc = dedicated_host_group_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        return self


class CreateDedicatedHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dedicated_host_group_id: str = None,
    ):
        self.request_id = request_id
        self.dedicated_host_group_id = dedicated_host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        return self


class CreateDedicatedHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDedicatedHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDedicatedHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddHostsToBastionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        bastion_instance_id: str = None,
        hosts: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.bastion_instance_id = bastion_instance_id
        self.hosts = hosts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        return self


class AddHostsToBastionResponseBodyHosts(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_name: str = None,
        message: str = None,
        host_private_ip: str = None,
    ):
        self.code = code
        self.host_name = host_name
        self.message = message
        self.host_private_ip = host_private_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.message is not None:
            result['Message'] = self.message
        if self.host_private_ip is not None:
            result['HostPrivateIp'] = self.host_private_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HostPrivateIp') is not None:
            self.host_private_ip = m.get('HostPrivateIp')
        return self


class AddHostsToBastionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bastion_instance_id: str = None,
        dedicated_host_group_id: str = None,
        hosts: List[AddHostsToBastionResponseBodyHosts] = None,
    ):
        self.request_id = request_id
        self.bastion_instance_id = bastion_instance_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.hosts = hosts

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = AddHostsToBastionResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        return self


class AddHostsToBastionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddHostsToBastionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddHostsToBastionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostsToBastionUserRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        bastion_user: str = None,
        bastion_instance_id: str = None,
        hosts: str = None,
        dedicated_host_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.bastion_user = bastion_user
        self.bastion_instance_id = bastion_instance_id
        self.hosts = hosts
        self.dedicated_host_group_id = dedicated_host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.bastion_user is not None:
            result['BastionUser'] = self.bastion_user
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BastionUser') is not None:
            self.bastion_user = m.get('BastionUser')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        return self


class AttachHostsToBastionUserResponseBodyHosts(TeaModel):
    def __init__(
        self,
        code: str = None,
        host_name: str = None,
        message: str = None,
    ):
        self.code = code
        self.host_name = host_name
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostsToBastionUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bastion_instance_id: str = None,
        bastion_user: str = None,
        hosts: List[AttachHostsToBastionUserResponseBodyHosts] = None,
    ):
        self.request_id = request_id
        self.bastion_instance_id = bastion_instance_id
        self.bastion_user = bastion_user
        self.hosts = hosts

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.bastion_user is not None:
            result['BastionUser'] = self.bastion_user
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('BastionUser') is not None:
            self.bastion_user = m.get('BastionUser')
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = AttachHostsToBastionUserResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        return self


class AttachHostsToBastionUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachHostsToBastionUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostsToBastionUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEvaluateDedicatedHostsForInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_group_id: str = None,
        dbinstance_id: str = None,
        exclude_type: str = None,
        zone_id: str = None,
        dedicated_host_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dbinstance_id = dbinstance_id
        self.exclude_type = exclude_type
        self.zone_id = zone_id
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.exclude_type is not None:
            result['ExcludeType'] = self.exclude_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('ExcludeType') is not None:
            self.exclude_type = m.get('ExcludeType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        return self


class DescribeEvaluateDedicatedHostsForInstanceResponseBodyDedicatedHosts(TeaModel):
    def __init__(
        self,
        is_contain_read_only_instance: bool = None,
        host_allocation_status: bool = None,
        comment: str = None,
        host_free_mem: int = None,
        host_status: str = None,
        host_free_cpu: int = None,
        host_storage: int = None,
        host_cpu: int = None,
        region_id: str = None,
        host_free_storage: int = None,
        v_switch_id: str = None,
        dedicated_host_name: str = None,
        zone_id: str = None,
        dedicated_host_id: str = None,
        engine: str = None,
        is_could_ssd: bool = None,
        is_available_for_instance: bool = None,
        host_mem: int = None,
        created_time: int = None,
        ipaddress: str = None,
    ):
        self.is_contain_read_only_instance = is_contain_read_only_instance
        self.host_allocation_status = host_allocation_status
        self.comment = comment
        self.host_free_mem = host_free_mem
        self.host_status = host_status
        self.host_free_cpu = host_free_cpu
        self.host_storage = host_storage
        self.host_cpu = host_cpu
        self.region_id = region_id
        self.host_free_storage = host_free_storage
        self.v_switch_id = v_switch_id
        self.dedicated_host_name = dedicated_host_name
        self.zone_id = zone_id
        self.dedicated_host_id = dedicated_host_id
        self.engine = engine
        self.is_could_ssd = is_could_ssd
        self.is_available_for_instance = is_available_for_instance
        self.host_mem = host_mem
        self.created_time = created_time
        self.ipaddress = ipaddress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_contain_read_only_instance is not None:
            result['IsContainReadOnlyInstance'] = self.is_contain_read_only_instance
        if self.host_allocation_status is not None:
            result['HostAllocationStatus'] = self.host_allocation_status
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_free_mem is not None:
            result['HostFreeMem'] = self.host_free_mem
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_free_cpu is not None:
            result['HostFreeCPU'] = self.host_free_cpu
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.host_free_storage is not None:
            result['HostFreeStorage'] = self.host_free_storage
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_could_ssd is not None:
            result['IsCouldSSD'] = self.is_could_ssd
        if self.is_available_for_instance is not None:
            result['IsAvailableForInstance'] = self.is_available_for_instance
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsContainReadOnlyInstance') is not None:
            self.is_contain_read_only_instance = m.get('IsContainReadOnlyInstance')
        if m.get('HostAllocationStatus') is not None:
            self.host_allocation_status = m.get('HostAllocationStatus')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostFreeMem') is not None:
            self.host_free_mem = m.get('HostFreeMem')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostFreeCPU') is not None:
            self.host_free_cpu = m.get('HostFreeCPU')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('HostFreeStorage') is not None:
            self.host_free_storage = m.get('HostFreeStorage')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsCouldSSD') is not None:
            self.is_could_ssd = m.get('IsCouldSSD')
        if m.get('IsAvailableForInstance') is not None:
            self.is_available_for_instance = m.get('IsAvailableForInstance')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        return self


class DescribeEvaluateDedicatedHostsForInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_required_cpu: int = None,
        cpu_over_allocation_ratio: int = None,
        memory_over_allocation_ratio: int = None,
        instance_required_memory: int = None,
        instance_class_code: str = None,
        available_host_num: int = None,
        instance_required_storage: int = None,
        disk_over_allocation_ratio: int = None,
        dedicated_host_group_id: str = None,
        dedicated_hosts: List[DescribeEvaluateDedicatedHostsForInstanceResponseBodyDedicatedHosts] = None,
    ):
        self.request_id = request_id
        self.instance_required_cpu = instance_required_cpu
        self.cpu_over_allocation_ratio = cpu_over_allocation_ratio
        self.memory_over_allocation_ratio = memory_over_allocation_ratio
        self.instance_required_memory = instance_required_memory
        self.instance_class_code = instance_class_code
        self.available_host_num = available_host_num
        self.instance_required_storage = instance_required_storage
        self.disk_over_allocation_ratio = disk_over_allocation_ratio
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_hosts = dedicated_hosts

    def validate(self):
        if self.dedicated_hosts:
            for k in self.dedicated_hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_required_cpu is not None:
            result['InstanceRequiredCPU'] = self.instance_required_cpu
        if self.cpu_over_allocation_ratio is not None:
            result['CpuOverAllocationRatio'] = self.cpu_over_allocation_ratio
        if self.memory_over_allocation_ratio is not None:
            result['MemoryOverAllocationRatio'] = self.memory_over_allocation_ratio
        if self.instance_required_memory is not None:
            result['InstanceRequiredMemory'] = self.instance_required_memory
        if self.instance_class_code is not None:
            result['InstanceClassCode'] = self.instance_class_code
        if self.available_host_num is not None:
            result['AvailableHostNum'] = self.available_host_num
        if self.instance_required_storage is not None:
            result['InstanceRequiredStorage'] = self.instance_required_storage
        if self.disk_over_allocation_ratio is not None:
            result['DiskOverAllocationRatio'] = self.disk_over_allocation_ratio
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['DedicatedHosts'] = []
        if self.dedicated_hosts is not None:
            for k in self.dedicated_hosts:
                result['DedicatedHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceRequiredCPU') is not None:
            self.instance_required_cpu = m.get('InstanceRequiredCPU')
        if m.get('CpuOverAllocationRatio') is not None:
            self.cpu_over_allocation_ratio = m.get('CpuOverAllocationRatio')
        if m.get('MemoryOverAllocationRatio') is not None:
            self.memory_over_allocation_ratio = m.get('MemoryOverAllocationRatio')
        if m.get('InstanceRequiredMemory') is not None:
            self.instance_required_memory = m.get('InstanceRequiredMemory')
        if m.get('InstanceClassCode') is not None:
            self.instance_class_code = m.get('InstanceClassCode')
        if m.get('AvailableHostNum') is not None:
            self.available_host_num = m.get('AvailableHostNum')
        if m.get('InstanceRequiredStorage') is not None:
            self.instance_required_storage = m.get('InstanceRequiredStorage')
        if m.get('DiskOverAllocationRatio') is not None:
            self.disk_over_allocation_ratio = m.get('DiskOverAllocationRatio')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.dedicated_hosts = []
        if m.get('DedicatedHosts') is not None:
            for k in m.get('DedicatedHosts'):
                temp_model = DescribeEvaluateDedicatedHostsForInstanceResponseBodyDedicatedHosts()
                self.dedicated_hosts.append(temp_model.from_map(k))
        return self


class DescribeEvaluateDedicatedHostsForInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEvaluateDedicatedHostsForInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEvaluateDedicatedHostsForInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_id: str = None,
        failover_mode: str = None,
        force_stop: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id
        self.failover_mode = failover_mode
        self.force_stop = force_stop

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        return self


class RestartDedicatedHostResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RestartDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RestartDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostHealthRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_id = dedicated_host_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDedicatedHostHealthResponseBodyHostEventsHostEvents(TeaModel):
    def __init__(
        self,
        event_name: str = None,
        event_time: str = None,
        event_type: str = None,
        event_description: str = None,
    ):
        self.event_name = event_name
        self.event_time = event_time
        self.event_type = event_type
        self.event_description = event_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.event_description is not None:
            result['EventDescription'] = self.event_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('EventDescription') is not None:
            self.event_description = m.get('EventDescription')
        return self


class DescribeDedicatedHostHealthResponseBodyHostEvents(TeaModel):
    def __init__(
        self,
        host_events: List[DescribeDedicatedHostHealthResponseBodyHostEventsHostEvents] = None,
    ):
        self.host_events = host_events

    def validate(self):
        if self.host_events:
            for k in self.host_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostEvents'] = []
        if self.host_events is not None:
            for k in self.host_events:
                result['HostEvents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_events = []
        if m.get('HostEvents') is not None:
            for k in m.get('HostEvents'):
                temp_model = DescribeDedicatedHostHealthResponseBodyHostEventsHostEvents()
                self.host_events.append(temp_model.from_map(k))
        return self


class DescribeDedicatedHostHealthResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        resource_event: Dict[str, Any] = None,
        request_id: str = None,
        health_status: Dict[str, Any] = None,
        host_events: DescribeDedicatedHostHealthResponseBodyHostEvents = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.resource_event = resource_event
        self.request_id = request_id
        self.health_status = health_status
        self.host_events = host_events

    def validate(self):
        if self.host_events:
            self.host_events.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.resource_event is not None:
            result['ResourceEvent'] = self.resource_event
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.health_status is not None:
            result['HealthStatus'] = self.health_status
        if self.host_events is not None:
            result['HostEvents'] = self.host_events.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('ResourceEvent') is not None:
            self.resource_event = m.get('ResourceEvent')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')
        if m.get('HostEvents') is not None:
            temp_model = DescribeDedicatedHostHealthResponseBodyHostEvents()
            self.host_events = temp_model.from_map(m['HostEvents'])
        return self


class DescribeDedicatedHostHealthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedHostHealthResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostWebShellRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        dedicated_host_id: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.dedicated_host_id = dedicated_host_id
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHostWebShellResponseBody(TeaModel):
    def __init__(
        self,
        login_url: str = None,
        request_id: str = None,
    ):
        self.login_url = login_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_url is not None:
            result['LoginUrl'] = self.login_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHostWebShellResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHostWebShellResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHostWebShellResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostAttributeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        region_id: str = None,
        dedicated_host_id: str = None,
        dedicated_host_group_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.region_id = region_id
        self.dedicated_host_id = dedicated_host_id
        self.dedicated_host_group_id = dedicated_host_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        return self


class DescribeDedicatedHostAttributeResponseBody(TeaModel):
    def __init__(
        self,
        host_type: str = None,
        host_storage: int = None,
        instance_number_roslave: int = None,
        account_type: str = None,
        memory_used: str = None,
        dedicated_host_group_id: str = None,
        request_id: str = None,
        instance_number_romaster: int = None,
        allocation_status: str = None,
        storage_used: str = None,
        ecs_class_code: str = None,
        dedicated_host_id: str = None,
        mem_allocation_ratio: str = None,
        created_time: str = None,
        ipaddress: str = None,
        auto_renew: str = None,
        host_status: str = None,
        host_name: str = None,
        host_cpu: int = None,
        open_permission: str = None,
        instance_number: int = None,
        cpu_used: str = None,
        vpcid: str = None,
        host_class: str = None,
        region_id: str = None,
        instance_number_master: int = None,
        v_switch_id: str = None,
        instance_number_slave: int = None,
        expired_time: str = None,
        zone_id: str = None,
        cpuallocation_ratio: str = None,
        image_category: str = None,
        disk_allocation_ratio: str = None,
        host_mem: int = None,
        account_name: str = None,
    ):
        self.host_type = host_type
        self.host_storage = host_storage
        self.instance_number_roslave = instance_number_roslave
        self.account_type = account_type
        self.memory_used = memory_used
        self.dedicated_host_group_id = dedicated_host_group_id
        self.request_id = request_id
        self.instance_number_romaster = instance_number_romaster
        self.allocation_status = allocation_status
        self.storage_used = storage_used
        self.ecs_class_code = ecs_class_code
        self.dedicated_host_id = dedicated_host_id
        self.mem_allocation_ratio = mem_allocation_ratio
        self.created_time = created_time
        self.ipaddress = ipaddress
        self.auto_renew = auto_renew
        self.host_status = host_status
        self.host_name = host_name
        self.host_cpu = host_cpu
        self.open_permission = open_permission
        self.instance_number = instance_number
        self.cpu_used = cpu_used
        self.vpcid = vpcid
        self.host_class = host_class
        self.region_id = region_id
        self.instance_number_master = instance_number_master
        self.v_switch_id = v_switch_id
        self.instance_number_slave = instance_number_slave
        self.expired_time = expired_time
        self.zone_id = zone_id
        self.cpuallocation_ratio = cpuallocation_ratio
        self.image_category = image_category
        self.disk_allocation_ratio = disk_allocation_ratio
        self.host_mem = host_mem
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.instance_number_roslave is not None:
            result['InstanceNumberROSlave'] = self.instance_number_roslave
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_number_romaster is not None:
            result['InstanceNumberROMaster'] = self.instance_number_romaster
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_number_master is not None:
            result['InstanceNumberMaster'] = self.instance_number_master
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.instance_number_slave is not None:
            result['InstanceNumberSlave'] = self.instance_number_slave
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('InstanceNumberROSlave') is not None:
            self.instance_number_roslave = m.get('InstanceNumberROSlave')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceNumberROMaster') is not None:
            self.instance_number_romaster = m.get('InstanceNumberROMaster')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceNumberMaster') is not None:
            self.instance_number_master = m.get('InstanceNumberMaster')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('InstanceNumberSlave') is not None:
            self.instance_number_slave = m.get('InstanceNumberSlave')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeDedicatedHostAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDedicatedHostAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


