# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arch_version: str = None,
        cold_storage: int = None,
        core_single_storage: int = None,
        core_spec: str = None,
        disk_category: str = None,
        duration: str = None,
        filestore_num: int = None,
        filestore_spec: str = None,
        instance_alias: str = None,
        instance_storage: str = None,
        lindorm_num: int = None,
        lindorm_spec: str = None,
        log_disk_category: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        multi_zone_combination: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        solr_num: int = None,
        solr_spec: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        tsdb_num: int = None,
        tsdb_spec: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.arbiter_vswitch_id = arbiter_vswitch_id
        self.arbiter_zone_id = arbiter_zone_id
        self.arch_version = arch_version
        self.cold_storage = cold_storage
        self.core_single_storage = core_single_storage
        self.core_spec = core_spec
        self.disk_category = disk_category
        self.duration = duration
        self.filestore_num = filestore_num
        self.filestore_spec = filestore_spec
        self.instance_alias = instance_alias
        self.instance_storage = instance_storage
        self.lindorm_num = lindorm_num
        self.lindorm_spec = lindorm_spec
        self.log_disk_category = log_disk_category
        self.log_num = log_num
        self.log_single_storage = log_single_storage
        self.log_spec = log_spec
        self.multi_zone_combination = multi_zone_combination
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.primary_vswitch_id = primary_vswitch_id
        self.primary_zone_id = primary_zone_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.solr_num = solr_num
        self.solr_spec = solr_spec
        self.standby_vswitch_id = standby_vswitch_id
        self.standby_zone_id = standby_zone_id
        self.tsdb_num = tsdb_num
        self.tsdb_spec = tsdb_spec
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
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage
        if self.core_spec is not None:
            result['CoreSpec'] = self.core_spec
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.filestore_num is not None:
            result['FilestoreNum'] = self.filestore_num
        if self.filestore_spec is not None:
            result['FilestoreSpec'] = self.filestore_spec
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.lindorm_num is not None:
            result['LindormNum'] = self.lindorm_num
        if self.lindorm_spec is not None:
            result['LindormSpec'] = self.lindorm_spec
        if self.log_disk_category is not None:
            result['LogDiskCategory'] = self.log_disk_category
        if self.log_num is not None:
            result['LogNum'] = self.log_num
        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage
        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.solr_num is not None:
            result['SolrNum'] = self.solr_num
        if self.solr_spec is not None:
            result['SolrSpec'] = self.solr_spec
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.tsdb_num is not None:
            result['TsdbNum'] = self.tsdb_num
        if self.tsdb_spec is not None:
            result['TsdbSpec'] = self.tsdb_spec
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')
        if m.get('CoreSpec') is not None:
            self.core_spec = m.get('CoreSpec')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FilestoreNum') is not None:
            self.filestore_num = m.get('FilestoreNum')
        if m.get('FilestoreSpec') is not None:
            self.filestore_spec = m.get('FilestoreSpec')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('LindormNum') is not None:
            self.lindorm_num = m.get('LindormNum')
        if m.get('LindormSpec') is not None:
            self.lindorm_spec = m.get('LindormSpec')
        if m.get('LogDiskCategory') is not None:
            self.log_disk_category = m.get('LogDiskCategory')
        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')
        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')
        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SolrNum') is not None:
            self.solr_num = m.get('SolrNum')
        if m.get('SolrSpec') is not None:
            self.solr_spec = m.get('SolrSpec')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('TsdbNum') is not None:
            self.tsdb_num = m.get('TsdbNum')
        if m.get('TsdbSpec') is not None:
            self.tsdb_spec = m.get('TsdbSpec')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLindormInstanceResponseBody = None,
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
            temp_model = CreateLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.accept_language = accept_language
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
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


class GetInstanceIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.group_name = group_name
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetInstanceIpWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip_list: List[str] = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.ip_list = ip_list
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceIpWhiteListResponseBody = None,
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
            temp_model = GetInstanceIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetLindormInstanceResponseBodyEngineList(TeaModel):
    def __init__(
        self,
        core_count: str = None,
        cpu_count: str = None,
        engine: str = None,
        is_last_version: bool = None,
        latest_version: str = None,
        memory_size: str = None,
        version: str = None,
    ):
        self.core_count = core_count
        self.cpu_count = cpu_count
        self.engine = engine
        self.is_last_version = is_last_version
        self.latest_version = latest_version
        self.memory_size = memory_size
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.core_count is not None:
            result['CoreCount'] = self.core_count
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.is_last_version is not None:
            result['IsLastVersion'] = self.is_last_version
        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version
        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreCount') is not None:
            self.core_count = m.get('CoreCount')
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('IsLastVersion') is not None:
            self.is_last_version = m.get('IsLastVersion')
        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')
        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        arbiter_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        auto_renew: bool = None,
        cold_storage: int = None,
        core_disk_category: str = None,
        core_num: int = None,
        core_single_storage: int = None,
        core_spec: str = None,
        create_milliseconds: int = None,
        create_time: str = None,
        deletion_protection: str = None,
        disk_category: str = None,
        disk_threshold: str = None,
        disk_usage: str = None,
        enable_cdc: bool = None,
        enable_compute: bool = None,
        enable_kms: bool = None,
        enable_ssl: bool = None,
        enable_shs: bool = None,
        enable_stream: bool = None,
        engine_list: List[GetLindormInstanceResponseBodyEngineList] = None,
        engine_type: int = None,
        expire_time: str = None,
        expired_milliseconds: int = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_storage: str = None,
        log_disk_category: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        multi_zone_combination: str = None,
        network_type: str = None,
        pay_type: str = None,
        primary_vswitch_id: str = None,
        primary_zone_id: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        service_type: str = None,
        standby_vswitch_id: str = None,
        standby_zone_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.arbiter_vswitch_id = arbiter_vswitch_id
        self.arbiter_zone_id = arbiter_zone_id
        self.auto_renew = auto_renew
        self.cold_storage = cold_storage
        self.core_disk_category = core_disk_category
        self.core_num = core_num
        self.core_single_storage = core_single_storage
        self.core_spec = core_spec
        self.create_milliseconds = create_milliseconds
        self.create_time = create_time
        self.deletion_protection = deletion_protection
        self.disk_category = disk_category
        self.disk_threshold = disk_threshold
        self.disk_usage = disk_usage
        self.enable_cdc = enable_cdc
        self.enable_compute = enable_compute
        self.enable_kms = enable_kms
        self.enable_ssl = enable_ssl
        self.enable_shs = enable_shs
        self.enable_stream = enable_stream
        self.engine_list = engine_list
        self.engine_type = engine_type
        self.expire_time = expire_time
        self.expired_milliseconds = expired_milliseconds
        self.instance_alias = instance_alias
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.instance_storage = instance_storage
        self.log_disk_category = log_disk_category
        self.log_num = log_num
        self.log_single_storage = log_single_storage
        self.log_spec = log_spec
        self.maintain_end_time = maintain_end_time
        self.maintain_start_time = maintain_start_time
        self.multi_zone_combination = multi_zone_combination
        self.network_type = network_type
        self.pay_type = pay_type
        self.primary_vswitch_id = primary_vswitch_id
        self.primary_zone_id = primary_zone_id
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.service_type = service_type
        self.standby_vswitch_id = standby_vswitch_id
        self.standby_zone_id = standby_zone_id
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.zone_id = zone_id

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.core_disk_category is not None:
            result['CoreDiskCategory'] = self.core_disk_category
        if self.core_num is not None:
            result['CoreNum'] = self.core_num
        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage
        if self.core_spec is not None:
            result['CoreSpec'] = self.core_spec
        if self.create_milliseconds is not None:
            result['CreateMilliseconds'] = self.create_milliseconds
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.disk_threshold is not None:
            result['DiskThreshold'] = self.disk_threshold
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage
        if self.enable_cdc is not None:
            result['EnableCdc'] = self.enable_cdc
        if self.enable_compute is not None:
            result['EnableCompute'] = self.enable_compute
        if self.enable_kms is not None:
            result['EnableKms'] = self.enable_kms
        if self.enable_ssl is not None:
            result['EnableSSL'] = self.enable_ssl
        if self.enable_shs is not None:
            result['EnableShs'] = self.enable_shs
        if self.enable_stream is not None:
            result['EnableStream'] = self.enable_stream
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired_milliseconds is not None:
            result['ExpiredMilliseconds'] = self.expired_milliseconds
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.log_disk_category is not None:
            result['LogDiskCategory'] = self.log_disk_category
        if self.log_num is not None:
            result['LogNum'] = self.log_num
        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage
        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CoreDiskCategory') is not None:
            self.core_disk_category = m.get('CoreDiskCategory')
        if m.get('CoreNum') is not None:
            self.core_num = m.get('CoreNum')
        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')
        if m.get('CoreSpec') is not None:
            self.core_spec = m.get('CoreSpec')
        if m.get('CreateMilliseconds') is not None:
            self.create_milliseconds = m.get('CreateMilliseconds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('DiskThreshold') is not None:
            self.disk_threshold = m.get('DiskThreshold')
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')
        if m.get('EnableCdc') is not None:
            self.enable_cdc = m.get('EnableCdc')
        if m.get('EnableCompute') is not None:
            self.enable_compute = m.get('EnableCompute')
        if m.get('EnableKms') is not None:
            self.enable_kms = m.get('EnableKms')
        if m.get('EnableSSL') is not None:
            self.enable_ssl = m.get('EnableSSL')
        if m.get('EnableShs') is not None:
            self.enable_shs = m.get('EnableShs')
        if m.get('EnableStream') is not None:
            self.enable_stream = m.get('EnableStream')
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = GetLindormInstanceResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpiredMilliseconds') is not None:
            self.expired_milliseconds = m.get('ExpiredMilliseconds')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('LogDiskCategory') is not None:
            self.log_disk_category = m.get('LogDiskCategory')
        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')
        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')
        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormInstanceResponseBody = None,
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
            temp_model = GetLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceEngineListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        instance_id: str = None,
        request_id: str = None,
    ):
        self.engine_list = engine_list
        self.instance_id = instance_id
        self.request_id = request_id

    def validate(self):
        if self.engine_list:
            for k in self.engine_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EngineList'] = []
        if self.engine_list is not None:
            for k in self.engine_list:
                result['EngineList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.engine_list = []
        if m.get('EngineList') is not None:
            for k in m.get('EngineList'):
                temp_model = GetLindormInstanceEngineListResponseBodyEngineList()
                self.engine_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetLindormInstanceEngineListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormInstanceEngineListResponseBody = None,
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
            temp_model = GetLindormInstanceEngineListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLindormInstanceListRequestTag(TeaModel):
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


class GetLindormInstanceListRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_str: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        service_type: str = None,
        support_engine: int = None,
        tag: List[GetLindormInstanceListRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        self.query_str = query_str
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.service_type = service_type
        self.support_engine = support_engine
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.support_engine is not None:
            result['SupportEngine'] = self.support_engine
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupportEngine') is not None:
            self.support_engine = m.get('SupportEngine')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = GetLindormInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class GetLindormInstanceListResponseBodyInstanceListTags(TeaModel):
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


class GetLindormInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        create_milliseconds: int = None,
        create_time: str = None,
        enable_compute: bool = None,
        enable_stream: bool = None,
        engine_type: str = None,
        expire_time: str = None,
        expired_milliseconds: int = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_storage: str = None,
        network_type: str = None,
        pay_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        service_type: str = None,
        tags: List[GetLindormInstanceListResponseBodyInstanceListTags] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.ali_uid = ali_uid
        self.create_milliseconds = create_milliseconds
        self.create_time = create_time
        self.enable_compute = enable_compute
        self.enable_stream = enable_stream
        self.engine_type = engine_type
        self.expire_time = expire_time
        self.expired_milliseconds = expired_milliseconds
        self.instance_alias = instance_alias
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.instance_storage = instance_storage
        self.network_type = network_type
        self.pay_type = pay_type
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.service_type = service_type
        self.tags = tags
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.create_milliseconds is not None:
            result['CreateMilliseconds'] = self.create_milliseconds
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_compute is not None:
            result['EnableCompute'] = self.enable_compute
        if self.enable_stream is not None:
            result['EnableStream'] = self.enable_stream
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.expired_milliseconds is not None:
            result['ExpiredMilliseconds'] = self.expired_milliseconds
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CreateMilliseconds') is not None:
            self.create_milliseconds = m.get('CreateMilliseconds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableCompute') is not None:
            self.enable_compute = m.get('EnableCompute')
        if m.get('EnableStream') is not None:
            self.enable_stream = m.get('EnableStream')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ExpiredMilliseconds') is not None:
            self.expired_milliseconds = m.get('ExpiredMilliseconds')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetLindormInstanceListResponseBodyInstanceListTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetLindormInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        instance_list: List[GetLindormInstanceListResponseBodyInstanceList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.instance_list = instance_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = GetLindormInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetLindormInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLindormInstanceListResponseBody = None,
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
            temp_model = GetLindormInstanceListResponseBody()
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
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        security_token: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.security_token = security_token
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
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


class ModifyInstancePayTypeRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.pay_type = pay_type
        self.pricing_cycle = pricing_cycle
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyInstancePayTypeResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstancePayTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstancePayTypeResponseBody = None,
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
            temp_model = ModifyInstancePayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ReleaseLindormInstanceResponseBody(TeaModel):
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


class ReleaseLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseLindormInstanceResponseBody = None,
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
            temp_model = ReleaseLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        self.duration = duration
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.pricing_cycle = pricing_cycle
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RenewLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewLindormInstanceResponseBody = None,
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
            temp_model = RenewLindormInstanceResponseBody()
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
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        security_token: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.security_token = security_token
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
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
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
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
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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
        owner_account: str = None,
        owner_id: int = None,
        resource_id: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        security_token: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.security_token = security_token
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
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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


class UpdateInstanceIpWhiteListRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_ip_list: str = None,
        security_token: str = None,
    ):
        self.group_name = group_name
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_ip_list = security_ip_list
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
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


class UpdateInstanceIpWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceIpWhiteListResponseBody = None,
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
            temp_model = UpdateInstanceIpWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeLindormInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_storage: int = None,
        cold_storage: int = None,
        core_single_storage: int = None,
        filestore_num: int = None,
        filestore_spec: str = None,
        instance_id: str = None,
        lindorm_num: int = None,
        lindorm_spec: str = None,
        log_num: int = None,
        log_single_storage: int = None,
        log_spec: str = None,
        lts_core_num: int = None,
        lts_core_spec: str = None,
        owner_account: str = None,
        owner_id: int = None,
        phoenix_core_num: int = None,
        phoenix_core_spec: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        solr_num: int = None,
        solr_spec: str = None,
        tsdb_num: int = None,
        tsdb_spec: str = None,
        upgrade_type: str = None,
        zone_id: str = None,
    ):
        self.cluster_storage = cluster_storage
        self.cold_storage = cold_storage
        self.core_single_storage = core_single_storage
        self.filestore_num = filestore_num
        self.filestore_spec = filestore_spec
        self.instance_id = instance_id
        self.lindorm_num = lindorm_num
        self.lindorm_spec = lindorm_spec
        self.log_num = log_num
        self.log_single_storage = log_single_storage
        self.log_spec = log_spec
        self.lts_core_num = lts_core_num
        self.lts_core_spec = lts_core_spec
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.phoenix_core_num = phoenix_core_num
        self.phoenix_core_spec = phoenix_core_spec
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        self.solr_num = solr_num
        self.solr_spec = solr_spec
        self.tsdb_num = tsdb_num
        self.tsdb_spec = tsdb_spec
        self.upgrade_type = upgrade_type
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_storage is not None:
            result['ClusterStorage'] = self.cluster_storage
        if self.cold_storage is not None:
            result['ColdStorage'] = self.cold_storage
        if self.core_single_storage is not None:
            result['CoreSingleStorage'] = self.core_single_storage
        if self.filestore_num is not None:
            result['FilestoreNum'] = self.filestore_num
        if self.filestore_spec is not None:
            result['FilestoreSpec'] = self.filestore_spec
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lindorm_num is not None:
            result['LindormNum'] = self.lindorm_num
        if self.lindorm_spec is not None:
            result['LindormSpec'] = self.lindorm_spec
        if self.log_num is not None:
            result['LogNum'] = self.log_num
        if self.log_single_storage is not None:
            result['LogSingleStorage'] = self.log_single_storage
        if self.log_spec is not None:
            result['LogSpec'] = self.log_spec
        if self.lts_core_num is not None:
            result['LtsCoreNum'] = self.lts_core_num
        if self.lts_core_spec is not None:
            result['LtsCoreSpec'] = self.lts_core_spec
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phoenix_core_num is not None:
            result['PhoenixCoreNum'] = self.phoenix_core_num
        if self.phoenix_core_spec is not None:
            result['PhoenixCoreSpec'] = self.phoenix_core_spec
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.solr_num is not None:
            result['SolrNum'] = self.solr_num
        if self.solr_spec is not None:
            result['SolrSpec'] = self.solr_spec
        if self.tsdb_num is not None:
            result['TsdbNum'] = self.tsdb_num
        if self.tsdb_spec is not None:
            result['TsdbSpec'] = self.tsdb_spec
        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterStorage') is not None:
            self.cluster_storage = m.get('ClusterStorage')
        if m.get('ColdStorage') is not None:
            self.cold_storage = m.get('ColdStorage')
        if m.get('CoreSingleStorage') is not None:
            self.core_single_storage = m.get('CoreSingleStorage')
        if m.get('FilestoreNum') is not None:
            self.filestore_num = m.get('FilestoreNum')
        if m.get('FilestoreSpec') is not None:
            self.filestore_spec = m.get('FilestoreSpec')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LindormNum') is not None:
            self.lindorm_num = m.get('LindormNum')
        if m.get('LindormSpec') is not None:
            self.lindorm_spec = m.get('LindormSpec')
        if m.get('LogNum') is not None:
            self.log_num = m.get('LogNum')
        if m.get('LogSingleStorage') is not None:
            self.log_single_storage = m.get('LogSingleStorage')
        if m.get('LogSpec') is not None:
            self.log_spec = m.get('LogSpec')
        if m.get('LtsCoreNum') is not None:
            self.lts_core_num = m.get('LtsCoreNum')
        if m.get('LtsCoreSpec') is not None:
            self.lts_core_spec = m.get('LtsCoreSpec')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoenixCoreNum') is not None:
            self.phoenix_core_num = m.get('PhoenixCoreNum')
        if m.get('PhoenixCoreSpec') is not None:
            self.phoenix_core_spec = m.get('PhoenixCoreSpec')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SolrNum') is not None:
            self.solr_num = m.get('SolrNum')
        if m.get('SolrSpec') is not None:
            self.solr_spec = m.get('SolrSpec')
        if m.get('TsdbNum') is not None:
            self.tsdb_num = m.get('TsdbNum')
        if m.get('TsdbSpec') is not None:
            self.tsdb_spec = m.get('TsdbSpec')
        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpgradeLindormInstanceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeLindormInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeLindormInstanceResponseBody = None,
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
            temp_model = UpgradeLindormInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


