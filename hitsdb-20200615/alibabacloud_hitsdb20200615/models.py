# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        accept_language: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
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


class GetInstanceIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        instance_id: str = None,
        group_name: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.instance_id = instance_id
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetInstanceIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        ip_list: List[str] = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class GetInstanceIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceIpWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetInstanceIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLindormInstanceResponseBodyEngineList(TeaModel):
    def __init__(
        self,
        version: str = None,
        cpu_count: str = None,
        core_count: str = None,
        engine: str = None,
        memory_size: str = None,
        is_last_version: bool = None,
    ):
        self.version = version
        self.cpu_count = cpu_count
        self.core_count = core_count
        self.engine = engine
        self.memory_size = memory_size
        self.is_last_version = is_last_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.core_count is not None:
            result['CoreCount'] = self.core_count
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.is_last_version is not None:
            result['IsLastVersion'] = self.is_last_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('CoreCount') is not None:
            self.core_count = m.get('CoreCount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('IsLastVersion') is not None:
            self.is_last_version = m.get('IsLastVersion')
        return self


class GetLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        engine_list: List[GetLindormInstanceResponseBodyEngineList] = None,
        auto_renew: bool = None,
        disk_usage: str = None,
        network_type: str = None,
        service_type: str = None,
        instance_alias: str = None,
        instance_status: str = None,
        engine_type: int = None,
        instance_storage: str = None,
        request_id: str = None,
        zone_id: str = None,
        instance_id: str = None,
        create_time: str = None,
        cold_storage: int = None,
        disk_category: str = None,
        pay_type: str = None,
        deletion_protection: str = None,
        vswitch_id: str = None,
        vpc_id: str = None,
        region_id: str = None,
        expire_time: str = None,
        ali_uid: int = None,
    ):
        self.engine_list = engine_list
        self.auto_renew = auto_renew
        self.disk_usage = disk_usage
        self.network_type = network_type
        self.service_type = service_type
        self.instance_alias = instance_alias
        self.instance_status = instance_status
        self.engine_type = engine_type
        self.instance_storage = instance_storage
        self.request_id = request_id
        self.zone_id = zone_id
        self.instance_id = instance_id
        self.create_time = create_time
        self.cold_storage = cold_storage
        self.disk_category = disk_category
        self.pay_type = pay_type
        self.deletion_protection = deletion_protection
        self.vswitch_id = vswitch_id
        self.vpc_id = vpc_id
        self.region_id = region_id
        self.expire_time = expire_time
        self.ali_uid = ali_uid

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = GetLindormInstanceResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        return self


class GetLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLindormInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceEngineListRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLindormInstanceEngineListResponseBodyEngineListNetInfoList(TeaModel):
    def __init__(
        self,
        access_type: int = None,
        connection_string: str = None,
        net_type: str = None,
        port: int = None,
    ):
        self.access_type = access_type
        self.connection_string = connection_string
        self.net_type = net_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class GetLindormInstanceEngineListResponseBodyEngineList(TeaModel):
    def __init__(
        self,
        engine_type: str = None,
        net_info_list: List[GetLindormInstanceEngineListResponseBodyEngineListNetInfoList] = None,
    ):
        self.engine_type = engine_type
        self.net_info_list = net_info_list

    def validate(self):
        if self.net_info_list:
            for k in self.net_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        result['NetInfoList'] = []
        if self.net_info_list is not None:
            for k in self.net_info_list:
                result['NetInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        self.net_info_list = []
        if m.get('NetInfoList') is not None:
            for k in m.get('NetInfoList'):
                temp_model = GetLindormInstanceEngineListResponseBodyEngineListNetInfoList()
                self.net_info_list.append(temp_model.from_map(k))
        return self


class GetLindormInstanceEngineListResponseBody(TeaModel):
    def __init__(
        self,
        engine_list: List[GetLindormInstanceEngineListResponseBodyEngineList] = None,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.engine_list = engine_list
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = GetLindormInstanceEngineListResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLindormInstanceEngineListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLindormInstanceEngineListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetLindormInstanceEngineListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceListRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        query_str: str = None,
        page_number: int = None,
        page_size: int = None,
        service_type: str = None,
        support_engine: int = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.query_str = query_str
        self.page_number = page_number
        self.page_size = page_size
        self.service_type = service_type
        self.support_engine = support_engine

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.support_engine is not None:
            result['SupportEngine'] = self.support_engine
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupportEngine') is not None:
            self.support_engine = m.get('SupportEngine')
        return self


class GetLindormInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        engine_type: str = None,
        expire_time: str = None,
        create_time: str = None,
        pay_type: str = None,
        instance_storage: str = None,
        ali_uid: int = None,
        service_type: str = None,
        network_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        instance_alias: str = None,
        zone_id: str = None,
        instance_status: str = None,
    ):
        self.vpc_id = vpc_id
        self.engine_type = engine_type
        self.expire_time = expire_time
        self.create_time = create_time
        self.pay_type = pay_type
        self.instance_storage = instance_storage
        self.ali_uid = ali_uid
        self.service_type = service_type
        self.network_type = network_type
        self.instance_id = instance_id
        self.region_id = region_id
        self.instance_alias = instance_alias
        self.zone_id = zone_id
        self.instance_status = instance_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        return self


class GetLindormInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        total: int = None,
        instance_list: List[GetLindormInstanceListResponseBodyInstanceList] = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.total = total
        self.instance_list = instance_list

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = GetLindormInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class GetLindormInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLindormInstanceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = GetLindormInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        instance_id: str = None,
        security_ip_list: str = None,
        group_name: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.instance_id = instance_id
        self.security_ip_list = security_ip_list
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class UpdateInstanceIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

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


class UpdateInstanceIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceIpWhiteListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
            temp_model = UpdateInstanceIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


