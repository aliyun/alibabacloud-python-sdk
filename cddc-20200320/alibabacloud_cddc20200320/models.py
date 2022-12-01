# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CreateDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        auto_renew: str = None,
        client_token: str = None,
        dedicated_host_group_id: str = None,
        host_class: str = None,
        host_storage: str = None,
        host_storage_type: str = None,
        image_category: str = None,
        os_password: str = None,
        owner_id: int = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        used_time: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.client_token = client_token
        self.dedicated_host_group_id = dedicated_host_group_id
        self.host_class = host_class
        self.host_storage = host_storage
        self.host_storage_type = host_storage_type
        self.image_category = image_category
        self.os_password = os_password
        self.owner_id = owner_id
        self.pay_type = pay_type
        self.period = period
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.used_time = used_time
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_storage_type is not None:
            result['HostStorageType'] = self.host_storage_type
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostStorageType') is not None:
            self.host_storage_type = m.get('HostStorageType')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        dedicate_host_list: CreateDedicatedHostResponseBodyDedicateHostList = None,
        order_id: int = None,
        request_id: str = None,
    ):
        self.dedicate_host_list = dedicate_host_list
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        if self.dedicate_host_list:
            self.dedicate_host_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicate_host_list is not None:
            result['DedicateHostList'] = self.dedicate_host_list.to_map()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicateHostList') is not None:
            temp_model = CreateDedicatedHostResponseBodyDedicateHostList()
            self.dedicate_host_list = temp_model.from_map(m['DedicateHostList'])
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        account_type: str = None,
        bastion_instance_id: str = None,
        client_token: str = None,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.account_name = account_name
        self.account_password = account_password
        self.account_type = account_type
        self.bastion_instance_id = bastion_instance_id
        self.client_token = client_token
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: CreateDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedHostGroupRequest(TeaModel):
    def __init__(
        self,
        allocation_policy: str = None,
        client_token: str = None,
        cpu_allocation_ratio: int = None,
        dedicated_host_group_desc: str = None,
        disk_allocation_ratio: int = None,
        engine: str = None,
        host_replace_policy: str = None,
        mem_allocation_ratio: int = None,
        open_permission: int = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vpcid: str = None,
    ):
        self.allocation_policy = allocation_policy
        self.client_token = client_token
        self.cpu_allocation_ratio = cpu_allocation_ratio
        self.dedicated_host_group_desc = dedicated_host_group_desc
        self.disk_allocation_ratio = disk_allocation_ratio
        self.engine = engine
        self.host_replace_policy = host_replace_policy
        self.mem_allocation_ratio = mem_allocation_ratio
        self.open_permission = open_permission
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.vpcid = vpcid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        return self


class CreateDedicatedHostGroupResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        request_id: str = None,
    ):
        self.dedicated_host_group_id = dedicated_host_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedHostGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDedicatedHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateDedicatedHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMyBaseRequestECSClassList(TeaModel):
    def __init__(
        self,
        data_disk_performance_level: str = None,
        disk_capacity: int = None,
        disk_count: int = None,
        disk_type: str = None,
        instance_type: str = None,
        node_count: int = None,
        sys_disk_capacity: int = None,
        sys_disk_type: str = None,
        system_disk_performance_level: str = None,
    ):
        self.data_disk_performance_level = data_disk_performance_level
        self.disk_capacity = disk_capacity
        self.disk_count = disk_count
        self.disk_type = disk_type
        self.instance_type = instance_type
        self.node_count = node_count
        self.sys_disk_capacity = sys_disk_capacity
        self.sys_disk_type = sys_disk_type
        self.system_disk_performance_level = system_disk_performance_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_disk_performance_level is not None:
            result['dataDiskPerformanceLevel'] = self.data_disk_performance_level
        if self.disk_capacity is not None:
            result['diskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['diskCount'] = self.disk_count
        if self.disk_type is not None:
            result['diskType'] = self.disk_type
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.node_count is not None:
            result['nodeCount'] = self.node_count
        if self.sys_disk_capacity is not None:
            result['sysDiskCapacity'] = self.sys_disk_capacity
        if self.sys_disk_type is not None:
            result['sysDiskType'] = self.sys_disk_type
        if self.system_disk_performance_level is not None:
            result['systemDiskPerformanceLevel'] = self.system_disk_performance_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataDiskPerformanceLevel') is not None:
            self.data_disk_performance_level = m.get('dataDiskPerformanceLevel')
        if m.get('diskCapacity') is not None:
            self.disk_capacity = m.get('diskCapacity')
        if m.get('diskCount') is not None:
            self.disk_count = m.get('diskCount')
        if m.get('diskType') is not None:
            self.disk_type = m.get('diskType')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('nodeCount') is not None:
            self.node_count = m.get('nodeCount')
        if m.get('sysDiskCapacity') is not None:
            self.sys_disk_capacity = m.get('sysDiskCapacity')
        if m.get('sysDiskType') is not None:
            self.sys_disk_type = m.get('sysDiskType')
        if m.get('systemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('systemDiskPerformanceLevel')
        return self


class CreateMyBaseRequest(TeaModel):
    def __init__(
        self,
        auto_renew: str = None,
        client_token: str = None,
        dedicated_host_group_description: str = None,
        dedicated_host_group_id: str = None,
        ecsclass_list: List[CreateMyBaseRequestECSClassList] = None,
        engine: str = None,
        image_id: str = None,
        key_pair_name: str = None,
        os_password: str = None,
        owner_id: int = None,
        password_inherit: str = None,
        pay_type: str = None,
        period: str = None,
        period_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.client_token = client_token
        self.dedicated_host_group_description = dedicated_host_group_description
        self.dedicated_host_group_id = dedicated_host_group_id
        self.ecsclass_list = ecsclass_list
        self.engine = engine
        self.image_id = image_id
        self.key_pair_name = key_pair_name
        self.os_password = os_password
        self.owner_id = owner_id
        self.password_inherit = password_inherit
        self.pay_type = pay_type
        self.period = period
        self.period_type = period_type
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.ecsclass_list:
            for k in self.ecsclass_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_group_description is not None:
            result['DedicatedHostGroupDescription'] = self.dedicated_host_group_description
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        result['ECSClassList'] = []
        if self.ecsclass_list is not None:
            for k in self.ecsclass_list:
                result['ECSClassList'].append(k.to_map() if k else None)
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostGroupDescription') is not None:
            self.dedicated_host_group_description = m.get('DedicatedHostGroupDescription')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        self.ecsclass_list = []
        if m.get('ECSClassList') is not None:
            for k in m.get('ECSClassList'):
                temp_model = CreateMyBaseRequestECSClassList()
                self.ecsclass_list.append(temp_model.from_map(k))
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateMyBaseShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_renew: str = None,
        client_token: str = None,
        dedicated_host_group_description: str = None,
        dedicated_host_group_id: str = None,
        ecsclass_list_shrink: str = None,
        engine: str = None,
        image_id: str = None,
        key_pair_name: str = None,
        os_password: str = None,
        owner_id: int = None,
        password_inherit: str = None,
        pay_type: str = None,
        period: str = None,
        period_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.auto_renew = auto_renew
        self.client_token = client_token
        self.dedicated_host_group_description = dedicated_host_group_description
        self.dedicated_host_group_id = dedicated_host_group_id
        self.ecsclass_list_shrink = ecsclass_list_shrink
        self.engine = engine
        self.image_id = image_id
        self.key_pair_name = key_pair_name
        self.os_password = os_password
        self.owner_id = owner_id
        self.password_inherit = password_inherit
        self.pay_type = pay_type
        self.period = period
        self.period_type = period_type
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_host_group_description is not None:
            result['DedicatedHostGroupDescription'] = self.dedicated_host_group_description
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.ecsclass_list_shrink is not None:
            result['ECSClassList'] = self.ecsclass_list_shrink
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.os_password is not None:
            result['OsPassword'] = self.os_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_type is not None:
            result['PeriodType'] = self.period_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedHostGroupDescription') is not None:
            self.dedicated_host_group_description = m.get('DedicatedHostGroupDescription')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('ECSClassList') is not None:
            self.ecsclass_list_shrink = m.get('ECSClassList')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('OsPassword') is not None:
            self.os_password = m.get('OsPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateMyBaseResponseBodyOrderListOrderList(TeaModel):
    def __init__(
        self,
        create_timestamp: int = None,
        ecsinstance_ids: str = None,
        order_id: str = None,
    ):
        self.create_timestamp = create_timestamp
        self.ecsinstance_ids = ecsinstance_ids
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.ecsinstance_ids is not None:
            result['ECSInstanceIds'] = self.ecsinstance_ids
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('ECSInstanceIds') is not None:
            self.ecsinstance_ids = m.get('ECSInstanceIds')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateMyBaseResponseBodyOrderList(TeaModel):
    def __init__(
        self,
        order_list: List[CreateMyBaseResponseBodyOrderListOrderList] = None,
    ):
        self.order_list = order_list

    def validate(self):
        if self.order_list:
            for k in self.order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OrderList'] = []
        if self.order_list is not None:
            for k in self.order_list:
                result['OrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.order_list = []
        if m.get('OrderList') is not None:
            for k in m.get('OrderList'):
                temp_model = CreateMyBaseResponseBodyOrderListOrderList()
                self.order_list.append(temp_model.from_map(k))
        return self


class CreateMyBaseResponseBody(TeaModel):
    def __init__(
        self,
        order_list: CreateMyBaseResponseBodyOrderList = None,
        request_id: str = None,
    ):
        self.order_list = order_list
        self.request_id = request_id

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderList') is not None:
            temp_model = CreateMyBaseResponseBodyOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMyBaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMyBaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateMyBaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.account_name = account_name
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: DeleteDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDedicatedHostGroupRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dedicated_host_group_id = dedicated_host_group_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: DeleteDedicatedHostGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteDedicatedHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostAttributeRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDedicatedHostAttributeResponseBody(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        allocation_status: str = None,
        auto_renew: str = None,
        cpuallocation_ratio: str = None,
        cpu_used: str = None,
        created_time: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        disk_allocation_ratio: str = None,
        distribution_tag: str = None,
        ecs_class_code: str = None,
        expired_time: str = None,
        host_cpu: int = None,
        host_class: str = None,
        host_mem: int = None,
        host_name: str = None,
        host_status: str = None,
        host_storage: int = None,
        host_type: str = None,
        ipaddress: str = None,
        image_category: str = None,
        instance_number: int = None,
        instance_number_master: int = None,
        instance_number_romaster: int = None,
        instance_number_roslave: int = None,
        instance_number_slave: int = None,
        mem_allocation_ratio: str = None,
        memory_used: str = None,
        open_permission: str = None,
        region_id: str = None,
        request_id: str = None,
        storage_used: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.account_name = account_name
        self.account_type = account_type
        self.allocation_status = allocation_status
        self.auto_renew = auto_renew
        self.cpuallocation_ratio = cpuallocation_ratio
        self.cpu_used = cpu_used
        self.created_time = created_time
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_host_id = dedicated_host_id
        self.disk_allocation_ratio = disk_allocation_ratio
        self.distribution_tag = distribution_tag
        self.ecs_class_code = ecs_class_code
        self.expired_time = expired_time
        self.host_cpu = host_cpu
        self.host_class = host_class
        self.host_mem = host_mem
        self.host_name = host_name
        self.host_status = host_status
        self.host_storage = host_storage
        self.host_type = host_type
        self.ipaddress = ipaddress
        self.image_category = image_category
        self.instance_number = instance_number
        self.instance_number_master = instance_number_master
        self.instance_number_romaster = instance_number_romaster
        self.instance_number_roslave = instance_number_roslave
        self.instance_number_slave = instance_number_slave
        self.mem_allocation_ratio = mem_allocation_ratio
        self.memory_used = memory_used
        self.open_permission = open_permission
        self.region_id = region_id
        self.request_id = request_id
        self.storage_used = storage_used
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio
        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.distribution_tag is not None:
            result['DistributionTag'] = self.distribution_tag
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.instance_number_master is not None:
            result['InstanceNumberMaster'] = self.instance_number_master
        if self.instance_number_romaster is not None:
            result['InstanceNumberROMaster'] = self.instance_number_romaster
        if self.instance_number_roslave is not None:
            result['InstanceNumberROSlave'] = self.instance_number_roslave
        if self.instance_number_slave is not None:
            result['InstanceNumberSlave'] = self.instance_number_slave
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')
        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DistributionTag') is not None:
            self.distribution_tag = m.get('DistributionTag')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('InstanceNumberMaster') is not None:
            self.instance_number_master = m.get('InstanceNumberMaster')
        if m.get('InstanceNumberROMaster') is not None:
            self.instance_number_romaster = m.get('InstanceNumberROMaster')
        if m.get('InstanceNumberROSlave') is not None:
            self.instance_number_roslave = m.get('InstanceNumberROSlave')
        if m.get('InstanceNumberSlave') is not None:
            self.instance_number_slave = m.get('InstanceNumberSlave')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDedicatedHostAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostDisksRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDedicatedHostDisksResponseBodyDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        dbinstance_id: str = None,
        device: str = None,
        disk_id: str = None,
        has_dbinstance: bool = None,
        max_iops: int = None,
        max_throughput: int = None,
        performance_level: str = None,
        size: int = None,
        status: str = None,
        type: str = None,
        zone_id: str = None,
    ):
        self.category = category
        self.dbinstance_id = dbinstance_id
        self.device = device
        self.disk_id = disk_id
        self.has_dbinstance = has_dbinstance
        self.max_iops = max_iops
        self.max_throughput = max_throughput
        self.performance_level = performance_level
        self.size = size
        self.status = status
        self.type = type
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.has_dbinstance is not None:
            result['HasDBInstance'] = self.has_dbinstance
        if self.max_iops is not None:
            result['MaxIOPS'] = self.max_iops
        if self.max_throughput is not None:
            result['MaxThroughput'] = self.max_throughput
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('HasDBInstance') is not None:
            self.has_dbinstance = m.get('HasDBInstance')
        if m.get('MaxIOPS') is not None:
            self.max_iops = m.get('MaxIOPS')
        if m.get('MaxThroughput') is not None:
            self.max_throughput = m.get('MaxThroughput')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostDisksResponseBody(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        disks: List[DescribeDedicatedHostDisksResponseBodyDisks] = None,
        request_id: str = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.disks = disks
        self.request_id = request_id

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
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        self.disks = []
        if m.get('Disks') is not None:
            for k in m.get('Disks'):
                temp_model = DescribeDedicatedHostDisksResponseBodyDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDedicatedHostDisksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDedicatedHostDisksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDedicatedHostDisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostGroupsRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_group_id: str = None,
        engine: str = None,
        image_category: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dedicated_host_group_id = dedicated_host_group_id
        self.engine = engine
        self.image_category = image_category
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        allocation_policy: str = None,
        bastion_instance_id: str = None,
        category: str = None,
        cpu_allocate_ration: float = None,
        cpu_allocated_amount: float = None,
        cpu_allocation_ratio: int = None,
        create_time: str = None,
        dedicated_host_count_group_by_host_type: Dict[str, Any] = None,
        dedicated_host_group_desc: str = None,
        dedicated_host_group_id: str = None,
        deploy_type: str = None,
        disk_allocate_ration: float = None,
        disk_allocated_amount: float = None,
        disk_allocation_ratio: int = None,
        disk_used_amount: float = None,
        disk_utility: float = None,
        engine: str = None,
        host_number: int = None,
        host_replace_policy: str = None,
        instance_number: int = None,
        mem_allocate_ration: float = None,
        mem_allocated_amount: float = None,
        mem_allocation_ratio: int = None,
        mem_used_amount: float = None,
        mem_utility: float = None,
        open_permission: str = None,
        text: str = None,
        vpcid: str = None,
        zone_idlist: DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroupsDedicatedHostGroupsZoneIDList = None,
    ):
        self.allocation_policy = allocation_policy
        self.bastion_instance_id = bastion_instance_id
        self.category = category
        self.cpu_allocate_ration = cpu_allocate_ration
        self.cpu_allocated_amount = cpu_allocated_amount
        self.cpu_allocation_ratio = cpu_allocation_ratio
        self.create_time = create_time
        self.dedicated_host_count_group_by_host_type = dedicated_host_count_group_by_host_type
        self.dedicated_host_group_desc = dedicated_host_group_desc
        self.dedicated_host_group_id = dedicated_host_group_id
        self.deploy_type = deploy_type
        self.disk_allocate_ration = disk_allocate_ration
        self.disk_allocated_amount = disk_allocated_amount
        self.disk_allocation_ratio = disk_allocation_ratio
        self.disk_used_amount = disk_used_amount
        self.disk_utility = disk_utility
        self.engine = engine
        self.host_number = host_number
        self.host_replace_policy = host_replace_policy
        self.instance_number = instance_number
        self.mem_allocate_ration = mem_allocate_ration
        self.mem_allocated_amount = mem_allocated_amount
        self.mem_allocation_ratio = mem_allocation_ratio
        self.mem_used_amount = mem_used_amount
        self.mem_utility = mem_utility
        self.open_permission = open_permission
        self.text = text
        self.vpcid = vpcid
        self.zone_idlist = zone_idlist

    def validate(self):
        if self.zone_idlist:
            self.zone_idlist.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.category is not None:
            result['Category'] = self.category
        if self.cpu_allocate_ration is not None:
            result['CpuAllocateRation'] = self.cpu_allocate_ration
        if self.cpu_allocated_amount is not None:
            result['CpuAllocatedAmount'] = self.cpu_allocated_amount
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dedicated_host_count_group_by_host_type is not None:
            result['DedicatedHostCountGroupByHostType'] = self.dedicated_host_count_group_by_host_type
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_allocate_ration is not None:
            result['DiskAllocateRation'] = self.disk_allocate_ration
        if self.disk_allocated_amount is not None:
            result['DiskAllocatedAmount'] = self.disk_allocated_amount
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.disk_used_amount is not None:
            result['DiskUsedAmount'] = self.disk_used_amount
        if self.disk_utility is not None:
            result['DiskUtility'] = self.disk_utility
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_number is not None:
            result['HostNumber'] = self.host_number
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.mem_allocate_ration is not None:
            result['MemAllocateRation'] = self.mem_allocate_ration
        if self.mem_allocated_amount is not None:
            result['MemAllocatedAmount'] = self.mem_allocated_amount
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.mem_used_amount is not None:
            result['MemUsedAmount'] = self.mem_used_amount
        if self.mem_utility is not None:
            result['MemUtility'] = self.mem_utility
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.text is not None:
            result['Text'] = self.text
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.zone_idlist is not None:
            result['ZoneIDList'] = self.zone_idlist.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CpuAllocateRation') is not None:
            self.cpu_allocate_ration = m.get('CpuAllocateRation')
        if m.get('CpuAllocatedAmount') is not None:
            self.cpu_allocated_amount = m.get('CpuAllocatedAmount')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DedicatedHostCountGroupByHostType') is not None:
            self.dedicated_host_count_group_by_host_type = m.get('DedicatedHostCountGroupByHostType')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskAllocateRation') is not None:
            self.disk_allocate_ration = m.get('DiskAllocateRation')
        if m.get('DiskAllocatedAmount') is not None:
            self.disk_allocated_amount = m.get('DiskAllocatedAmount')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DiskUsedAmount') is not None:
            self.disk_used_amount = m.get('DiskUsedAmount')
        if m.get('DiskUtility') is not None:
            self.disk_utility = m.get('DiskUtility')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostNumber') is not None:
            self.host_number = m.get('HostNumber')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('MemAllocateRation') is not None:
            self.mem_allocate_ration = m.get('MemAllocateRation')
        if m.get('MemAllocatedAmount') is not None:
            self.mem_allocated_amount = m.get('MemAllocatedAmount')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemUsedAmount') is not None:
            self.mem_used_amount = m.get('MemUsedAmount')
        if m.get('MemUtility') is not None:
            self.mem_utility = m.get('MemUtility')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
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
        dedicated_host_groups: DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups = None,
        request_id: str = None,
    ):
        self.dedicated_host_groups = dedicated_host_groups
        self.request_id = request_id

    def validate(self):
        if self.dedicated_host_groups:
            self.dedicated_host_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_groups is not None:
            result['DedicatedHostGroups'] = self.dedicated_host_groups.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroups') is not None:
            temp_model = DescribeDedicatedHostGroupsResponseBodyDedicatedHostGroups()
            self.dedicated_host_groups = temp_model.from_map(m['DedicatedHostGroups'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDedicatedHostGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDedicatedHostGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDedicatedHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedHostsRequest(TeaModel):
    def __init__(
        self,
        allocation_status: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        host_status: str = None,
        host_type: str = None,
        order_id: int = None,
        owner_id: int = None,
        page_numbers: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tags: str = None,
        zone_id: str = None,
    ):
        self.allocation_status = allocation_status
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_host_id = dedicated_host_id
        self.host_status = host_status
        self.host_type = host_type
        self.order_id = order_id
        self.owner_id = owner_id
        self.page_numbers = page_numbers
        self.page_size = page_size
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.tags = tags
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedHostsResponseBodyDedicatedHostsDedicatedHosts(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_type: str = None,
        allocation_status: str = None,
        bastion_instance_id: str = None,
        cpuallocation_ratio: str = None,
        category: str = None,
        charge_type: str = None,
        cpu_used: str = None,
        created_time: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        disk_allocation_ratio: str = None,
        disk_info: str = None,
        distribution_symbol: str = None,
        distribution_tag: str = None,
        ecs_class_code: str = None,
        ecs_id: str = None,
        end_time: str = None,
        engine: str = None,
        host_cpu: str = None,
        host_class: str = None,
        host_mem: str = None,
        host_name: str = None,
        host_status: str = None,
        host_storage: str = None,
        host_type: str = None,
        ipaddress: str = None,
        image_category: str = None,
        instance_number: str = None,
        mem_allocation_ratio: str = None,
        memory_used: str = None,
        mssql_support_version: str = None,
        open_permission: str = None,
        storage_used: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.account_name = account_name
        self.account_type = account_type
        self.allocation_status = allocation_status
        self.bastion_instance_id = bastion_instance_id
        self.cpuallocation_ratio = cpuallocation_ratio
        self.category = category
        self.charge_type = charge_type
        self.cpu_used = cpu_used
        self.created_time = created_time
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_host_id = dedicated_host_id
        self.disk_allocation_ratio = disk_allocation_ratio
        self.disk_info = disk_info
        self.distribution_symbol = distribution_symbol
        self.distribution_tag = distribution_tag
        self.ecs_class_code = ecs_class_code
        self.ecs_id = ecs_id
        self.end_time = end_time
        self.engine = engine
        self.host_cpu = host_cpu
        self.host_class = host_class
        self.host_mem = host_mem
        self.host_name = host_name
        self.host_status = host_status
        self.host_storage = host_storage
        self.host_type = host_type
        self.ipaddress = ipaddress
        self.image_category = image_category
        self.instance_number = instance_number
        self.mem_allocation_ratio = mem_allocation_ratio
        self.memory_used = memory_used
        self.mssql_support_version = mssql_support_version
        self.open_permission = open_permission
        self.storage_used = storage_used
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.bastion_instance_id is not None:
            result['BastionInstanceId'] = self.bastion_instance_id
        if self.cpuallocation_ratio is not None:
            result['CPUAllocationRatio'] = self.cpuallocation_ratio
        if self.category is not None:
            result['Category'] = self.category
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu_used is not None:
            result['CpuUsed'] = self.cpu_used
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info
        if self.distribution_symbol is not None:
            result['DistributionSymbol'] = self.distribution_symbol
        if self.distribution_tag is not None:
            result['DistributionTag'] = self.distribution_tag
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.host_cpu is not None:
            result['HostCPU'] = self.host_cpu
        if self.host_class is not None:
            result['HostClass'] = self.host_class
        if self.host_mem is not None:
            result['HostMem'] = self.host_mem
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_status is not None:
            result['HostStatus'] = self.host_status
        if self.host_storage is not None:
            result['HostStorage'] = self.host_storage
        if self.host_type is not None:
            result['HostType'] = self.host_type
        if self.ipaddress is not None:
            result['IPAddress'] = self.ipaddress
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.instance_number is not None:
            result['InstanceNumber'] = self.instance_number
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.memory_used is not None:
            result['MemoryUsed'] = self.memory_used
        if self.mssql_support_version is not None:
            result['MssqlSupportVersion'] = self.mssql_support_version
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.storage_used is not None:
            result['StorageUsed'] = self.storage_used
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('BastionInstanceId') is not None:
            self.bastion_instance_id = m.get('BastionInstanceId')
        if m.get('CPUAllocationRatio') is not None:
            self.cpuallocation_ratio = m.get('CPUAllocationRatio')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CpuUsed') is not None:
            self.cpu_used = m.get('CpuUsed')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')
        if m.get('DistributionSymbol') is not None:
            self.distribution_symbol = m.get('DistributionSymbol')
        if m.get('DistributionTag') is not None:
            self.distribution_tag = m.get('DistributionTag')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('HostCPU') is not None:
            self.host_cpu = m.get('HostCPU')
        if m.get('HostClass') is not None:
            self.host_class = m.get('HostClass')
        if m.get('HostMem') is not None:
            self.host_mem = m.get('HostMem')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')
        if m.get('HostStorage') is not None:
            self.host_storage = m.get('HostStorage')
        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')
        if m.get('IPAddress') is not None:
            self.ipaddress = m.get('IPAddress')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('InstanceNumber') is not None:
            self.instance_number = m.get('InstanceNumber')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('MemoryUsed') is not None:
            self.memory_used = m.get('MemoryUsed')
        if m.get('MssqlSupportVersion') is not None:
            self.mssql_support_version = m.get('MssqlSupportVersion')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('StorageUsed') is not None:
            self.storage_used = m.get('StorageUsed')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        dedicated_host_group_id: str = None,
        dedicated_hosts: DescribeDedicatedHostsResponseBodyDedicatedHosts = None,
        max_auto_scale_host_storage: int = None,
        page_numbers: int = None,
        page_size: int = None,
        request_id: str = None,
        total_records: int = None,
    ):
        self.dedicated_host_group_id = dedicated_host_group_id
        self.dedicated_hosts = dedicated_hosts
        self.max_auto_scale_host_storage = max_auto_scale_host_storage
        self.page_numbers = page_numbers
        self.page_size = page_size
        self.request_id = request_id
        self.total_records = total_records

    def validate(self):
        if self.dedicated_hosts:
            self.dedicated_hosts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.dedicated_hosts is not None:
            result['DedicatedHosts'] = self.dedicated_hosts.to_map()
        if self.max_auto_scale_host_storage is not None:
            result['MaxAutoScaleHostStorage'] = self.max_auto_scale_host_storage
        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_records is not None:
            result['TotalRecords'] = self.total_records
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DedicatedHosts') is not None:
            temp_model = DescribeDedicatedHostsResponseBodyDedicatedHosts()
            self.dedicated_hosts = temp_model.from_map(m['DedicatedHosts'])
        if m.get('MaxAutoScaleHostStorage') is not None:
            self.max_auto_scale_host_storage = m.get('MaxAutoScaleHostStorage')
        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecords') is not None:
            self.total_records = m.get('TotalRecords')
        return self


class DescribeDedicatedHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDedicatedHostsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeDedicatedHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostEcsLevelInfoRequest(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        image_category: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        storage_type: str = None,
        zone_id: str = None,
    ):
        self.db_type = db_type
        self.image_category = image_category
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.storage_type = storage_type
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.image_category is not None:
            result['ImageCategory'] = self.image_category
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('ImageCategory') is not None:
            self.image_category = m.get('ImageCategory')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfosItems(TeaModel):
    def __init__(
        self,
        cloud_storage_bandwidth: float = None,
        cpu: int = None,
        cpu_frequency: str = None,
        cpu_version: str = None,
        description: str = None,
        ecs_class: str = None,
        ecs_class_code: str = None,
        is_cloud_disk: int = None,
        local_storage: str = None,
        memory: int = None,
        net_band_width: float = None,
        net_package: int = None,
        rds_class_code: str = None,
        storage_iops: int = None,
    ):
        self.cloud_storage_bandwidth = cloud_storage_bandwidth
        self.cpu = cpu
        self.cpu_frequency = cpu_frequency
        self.cpu_version = cpu_version
        self.description = description
        self.ecs_class = ecs_class
        self.ecs_class_code = ecs_class_code
        self.is_cloud_disk = is_cloud_disk
        self.local_storage = local_storage
        self.memory = memory
        self.net_band_width = net_band_width
        self.net_package = net_package
        self.rds_class_code = rds_class_code
        self.storage_iops = storage_iops

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_storage_bandwidth is not None:
            result['CloudStorageBandwidth'] = self.cloud_storage_bandwidth
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.cpu_frequency is not None:
            result['CpuFrequency'] = self.cpu_frequency
        if self.cpu_version is not None:
            result['CpuVersion'] = self.cpu_version
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_class is not None:
            result['EcsClass'] = self.ecs_class
        if self.ecs_class_code is not None:
            result['EcsClassCode'] = self.ecs_class_code
        if self.is_cloud_disk is not None:
            result['IsCloudDisk'] = self.is_cloud_disk
        if self.local_storage is not None:
            result['LocalStorage'] = self.local_storage
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.net_band_width is not None:
            result['NetBandWidth'] = self.net_band_width
        if self.net_package is not None:
            result['NetPackage'] = self.net_package
        if self.rds_class_code is not None:
            result['RdsClassCode'] = self.rds_class_code
        if self.storage_iops is not None:
            result['StorageIops'] = self.storage_iops
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudStorageBandwidth') is not None:
            self.cloud_storage_bandwidth = m.get('CloudStorageBandwidth')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CpuFrequency') is not None:
            self.cpu_frequency = m.get('CpuFrequency')
        if m.get('CpuVersion') is not None:
            self.cpu_version = m.get('CpuVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsClass') is not None:
            self.ecs_class = m.get('EcsClass')
        if m.get('EcsClassCode') is not None:
            self.ecs_class_code = m.get('EcsClassCode')
        if m.get('IsCloudDisk') is not None:
            self.is_cloud_disk = m.get('IsCloudDisk')
        if m.get('LocalStorage') is not None:
            self.local_storage = m.get('LocalStorage')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetBandWidth') is not None:
            self.net_band_width = m.get('NetBandWidth')
        if m.get('NetPackage') is not None:
            self.net_package = m.get('NetPackage')
        if m.get('RdsClassCode') is not None:
            self.rds_class_code = m.get('RdsClassCode')
        if m.get('StorageIops') is not None:
            self.storage_iops = m.get('StorageIops')
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
        host_ecs_level_infos: List[DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos] = None,
        request_id: str = None,
    ):
        self.host_ecs_level_infos = host_ecs_level_infos
        self.request_id = request_id

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
        result['HostEcsLevelInfos'] = []
        if self.host_ecs_level_infos is not None:
            for k in self.host_ecs_level_infos:
                result['HostEcsLevelInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_ecs_level_infos = []
        if m.get('HostEcsLevelInfos') is not None:
            for k in m.get('HostEcsLevelInfos'):
                temp_model = DescribeHostEcsLevelInfoResponseBodyHostEcsLevelInfos()
                self.host_ecs_level_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHostEcsLevelInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHostEcsLevelInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeHostEcsLevelInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHostWebShellRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: DescribeHostWebShellResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeHostWebShellResponseBody()
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
        region_id: str = None,
        zone_id: str = None,
    ):
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
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
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAccountRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.account_name = account_name
        self.account_password = account_password
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: ModifyDedicatedHostAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyDedicatedHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostAttributeRequest(TeaModel):
    def __init__(
        self,
        allocation_status: str = None,
        dedicated_host_id: str = None,
        host_name: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.allocation_status = allocation_status
        self.dedicated_host_id = dedicated_host_id
        self.host_name = host_name
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: ModifyDedicatedHostAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyDedicatedHostAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostClassRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        switch_time: str = None,
        switch_time_mode: str = None,
        target_class_code: str = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.switch_time = switch_time
        self.switch_time_mode = switch_time_mode
        self.target_class_code = target_class_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        if self.target_class_code is not None:
            result['TargetClassCode'] = self.target_class_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        if m.get('TargetClassCode') is not None:
            self.target_class_code = m.get('TargetClassCode')
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
        status_code: int = None,
        body: ModifyDedicatedHostClassResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyDedicatedHostClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostGroupAttributeRequest(TeaModel):
    def __init__(
        self,
        allocation_policy: str = None,
        cpu_allocation_ratio: int = None,
        dedicated_host_group_desc: str = None,
        dedicated_host_group_id: str = None,
        disk_allocation_ratio: int = None,
        host_replace_policy: str = None,
        mem_allocation_ratio: int = None,
        open_permission: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.allocation_policy = allocation_policy
        self.cpu_allocation_ratio = cpu_allocation_ratio
        self.dedicated_host_group_desc = dedicated_host_group_desc
        self.dedicated_host_group_id = dedicated_host_group_id
        self.disk_allocation_ratio = disk_allocation_ratio
        self.host_replace_policy = host_replace_policy
        self.mem_allocation_ratio = mem_allocation_ratio
        self.open_permission = open_permission
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_policy is not None:
            result['AllocationPolicy'] = self.allocation_policy
        if self.cpu_allocation_ratio is not None:
            result['CpuAllocationRatio'] = self.cpu_allocation_ratio
        if self.dedicated_host_group_desc is not None:
            result['DedicatedHostGroupDesc'] = self.dedicated_host_group_desc
        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id
        if self.disk_allocation_ratio is not None:
            result['DiskAllocationRatio'] = self.disk_allocation_ratio
        if self.host_replace_policy is not None:
            result['HostReplacePolicy'] = self.host_replace_policy
        if self.mem_allocation_ratio is not None:
            result['MemAllocationRatio'] = self.mem_allocation_ratio
        if self.open_permission is not None:
            result['OpenPermission'] = self.open_permission
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationPolicy') is not None:
            self.allocation_policy = m.get('AllocationPolicy')
        if m.get('CpuAllocationRatio') is not None:
            self.cpu_allocation_ratio = m.get('CpuAllocationRatio')
        if m.get('DedicatedHostGroupDesc') is not None:
            self.dedicated_host_group_desc = m.get('DedicatedHostGroupDesc')
        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')
        if m.get('DiskAllocationRatio') is not None:
            self.disk_allocation_ratio = m.get('DiskAllocationRatio')
        if m.get('HostReplacePolicy') is not None:
            self.host_replace_policy = m.get('HostReplacePolicy')
        if m.get('MemAllocationRatio') is not None:
            self.mem_allocation_ratio = m.get('MemAllocationRatio')
        if m.get('OpenPermission') is not None:
            self.open_permission = m.get('OpenPermission')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: ModifyDedicatedHostGroupAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyDedicatedHostGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedHostPasswordRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        new_password: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.new_password = new_password
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.new_password is not None:
            result['NewPassword'] = self.new_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: ModifyDedicatedHostPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ModifyDedicatedHostPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHostBaseInfoByInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos(TeaModel):
    def __init__(
        self,
        cluster_name: str = None,
        engine: str = None,
        engine_version: str = None,
        expired_time: str = None,
        host_name: str = None,
        ip: str = None,
        port: str = None,
        role: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.cluster_name = cluster_name
        self.engine = engine
        self.engine_version = engine_version
        self.expired_time = expired_time
        self.host_name = host_name
        self.ip = ip
        self.port = port
        self.role = role
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class QueryHostBaseInfoByInstanceResponseBody(TeaModel):
    def __init__(
        self,
        host_instance_console_infos: List[QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos] = None,
        request_id: str = None,
    ):
        self.host_instance_console_infos = host_instance_console_infos
        self.request_id = request_id

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
        result['HostInstanceConsoleInfos'] = []
        if self.host_instance_console_infos is not None:
            for k in self.host_instance_console_infos:
                result['HostInstanceConsoleInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_instance_console_infos = []
        if m.get('HostInstanceConsoleInfos') is not None:
            for k in m.get('HostInstanceConsoleInfos'):
                temp_model = QueryHostBaseInfoByInstanceResponseBodyHostInstanceConsoleInfos()
                self.host_instance_console_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryHostBaseInfoByInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryHostBaseInfoByInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryHostBaseInfoByInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHostInstanceConsoleInfoRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo(TeaModel):
    def __init__(
        self,
        cpu_ratio: float = None,
        disk_curr: float = None,
        mem_ratio: float = None,
        perf_idb_pio: float = None,
    ):
        self.cpu_ratio = cpu_ratio
        self.disk_curr = disk_curr
        self.mem_ratio = mem_ratio
        self.perf_idb_pio = perf_idb_pio

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_ratio is not None:
            result['CpuRatio'] = self.cpu_ratio
        if self.disk_curr is not None:
            result['DiskCurr'] = self.disk_curr
        if self.mem_ratio is not None:
            result['MemRatio'] = self.mem_ratio
        if self.perf_idb_pio is not None:
            result['PerfIdbPio'] = self.perf_idb_pio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuRatio') is not None:
            self.cpu_ratio = m.get('CpuRatio')
        if m.get('DiskCurr') is not None:
            self.disk_curr = m.get('DiskCurr')
        if m.get('MemRatio') is not None:
            self.mem_ratio = m.get('MemRatio')
        if m.get('PerfIdbPio') is not None:
            self.perf_idb_pio = m.get('PerfIdbPio')
        return self


class QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos(TeaModel):
    def __init__(
        self,
        cpu_cores: int = None,
        cpu_increase_ratio_value: int = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        disk_size: int = None,
        engine: str = None,
        engine_version: str = None,
        ip: str = None,
        level_name: str = None,
        max_conn_increase_ratio_value: int = None,
        mem_size: int = None,
        memory_increase_ratio_value: int = None,
        perf_info: QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo = None,
        port: str = None,
        role: str = None,
        status: str = None,
    ):
        self.cpu_cores = cpu_cores
        self.cpu_increase_ratio_value = cpu_increase_ratio_value
        self.dbinstance_description = dbinstance_description
        self.dbinstance_id = dbinstance_id
        self.disk_size = disk_size
        self.engine = engine
        self.engine_version = engine_version
        self.ip = ip
        self.level_name = level_name
        self.max_conn_increase_ratio_value = max_conn_increase_ratio_value
        self.mem_size = mem_size
        self.memory_increase_ratio_value = memory_increase_ratio_value
        self.perf_info = perf_info
        self.port = port
        self.role = role
        self.status = status

    def validate(self):
        if self.perf_info:
            self.perf_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.cpu_increase_ratio_value is not None:
            result['CpuIncreaseRatioValue'] = self.cpu_increase_ratio_value
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.level_name is not None:
            result['LevelName'] = self.level_name
        if self.max_conn_increase_ratio_value is not None:
            result['MaxConnIncreaseRatioValue'] = self.max_conn_increase_ratio_value
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.memory_increase_ratio_value is not None:
            result['MemoryIncreaseRatioValue'] = self.memory_increase_ratio_value
        if self.perf_info is not None:
            result['PerfInfo'] = self.perf_info.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('CpuIncreaseRatioValue') is not None:
            self.cpu_increase_ratio_value = m.get('CpuIncreaseRatioValue')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('LevelName') is not None:
            self.level_name = m.get('LevelName')
        if m.get('MaxConnIncreaseRatioValue') is not None:
            self.max_conn_increase_ratio_value = m.get('MaxConnIncreaseRatioValue')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('MemoryIncreaseRatioValue') is not None:
            self.memory_increase_ratio_value = m.get('MemoryIncreaseRatioValue')
        if m.get('PerfInfo') is not None:
            temp_model = QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfosPerfInfo()
            self.perf_info = temp_model.from_map(m['PerfInfo'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryHostInstanceConsoleInfoResponseBody(TeaModel):
    def __init__(
        self,
        host_instance_console_infos: List[QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos] = None,
        request_id: str = None,
    ):
        self.host_instance_console_infos = host_instance_console_infos
        self.request_id = request_id

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
        result['HostInstanceConsoleInfos'] = []
        if self.host_instance_console_infos is not None:
            for k in self.host_instance_console_infos:
                result['HostInstanceConsoleInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_instance_console_infos = []
        if m.get('HostInstanceConsoleInfos') is not None:
            for k in m.get('HostInstanceConsoleInfos'):
                temp_model = QueryHostInstanceConsoleInfoResponseBodyHostInstanceConsoleInfos()
                self.host_instance_console_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryHostInstanceConsoleInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryHostInstanceConsoleInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryHostInstanceConsoleInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplaceDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        failover_mode: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.failover_mode = failover_mode
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: ReplaceDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ReplaceDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDedicatedHostRequest(TeaModel):
    def __init__(
        self,
        dedicated_host_id: str = None,
        failover_mode: str = None,
        force_stop: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.dedicated_host_id = dedicated_host_id
        self.failover_mode = failover_mode
        self.force_stop = force_stop
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id
        if self.failover_mode is not None:
            result['FailoverMode'] = self.failover_mode
        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')
        if m.get('FailoverMode') is not None:
            self.failover_mode = m.get('FailoverMode')
        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
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
        status_code: int = None,
        body: RestartDedicatedHostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RestartDedicatedHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


