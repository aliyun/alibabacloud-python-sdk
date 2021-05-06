# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class DescribeOnDemandInstanceRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeOnDemandInstanceResponseInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        remark: str = None,
        defense_status: str = None,
        region_id: str = None,
        ipnet: List[str] = None,
    ):
        self.instance_id = instance_id
        self.remark = remark
        self.defense_status = defense_status
        self.region_id = region_id
        self.ipnet = ipnet

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.defense_status, 'defense_status')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipnet, 'ipnet')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.defense_status is not None:
            result['DefenseStatus'] = self.defense_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ipnet is not None:
            result['Ipnet'] = self.ipnet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('DefenseStatus') is not None:
            self.defense_status = m.get('DefenseStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Ipnet') is not None:
            self.ipnet = m.get('Ipnet')
        return self


class DescribeOnDemandInstanceResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: str = None,
        instances: List[DescribeOnDemandInstanceResponseInstances] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.instances = instances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeOnDemandInstanceResponseInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class ModifyOnDemaondDefenseStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        defense_status: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.defense_status = defense_status
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.defense_status, 'defense_status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.defense_status is not None:
            result['DefenseStatus'] = self.defense_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DefenseStatus') is not None:
            self.defense_status = m.get('DefenseStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyOnDemaondDefenseStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        current_page: int = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.current_page = current_page
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeOpEntitiesResponseOpEntities(TeaModel):
    def __init__(
        self,
        entity_object: str = None,
        entity_type: int = None,
        op_desc: str = None,
        op_account: str = None,
        op_action: int = None,
        gmt_create: int = None,
    ):
        self.entity_object = entity_object
        self.entity_type = entity_type
        self.op_desc = op_desc
        self.op_account = op_account
        self.op_action = op_action
        self.gmt_create = gmt_create

    def validate(self):
        self.validate_required(self.entity_object, 'entity_object')
        self.validate_required(self.entity_type, 'entity_type')
        self.validate_required(self.op_desc, 'op_desc')
        self.validate_required(self.op_account, 'op_account')
        self.validate_required(self.op_action, 'op_action')
        self.validate_required(self.gmt_create, 'gmt_create')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        op_entities: List[DescribeOpEntitiesResponseOpEntities] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.op_entities = op_entities

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.op_entities, 'op_entities')
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k in m.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        return self


class DescribePackPaidTrafficRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        current_page: int = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.current_page = current_page
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribePackPaidTrafficResponsePackPaidTraffics(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_time: int = None,
        base_bandwidth: int = None,
        elastic_bandwidth: int = None,
        paid_capacity: float = None,
        total_capacity: float = None,
        max_attack: float = None,
    ):
        self.instance_id = instance_id
        self.start_time = start_time
        self.base_bandwidth = base_bandwidth
        self.elastic_bandwidth = elastic_bandwidth
        self.paid_capacity = paid_capacity
        self.total_capacity = total_capacity
        self.max_attack = max_attack

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.base_bandwidth, 'base_bandwidth')
        self.validate_required(self.elastic_bandwidth, 'elastic_bandwidth')
        self.validate_required(self.paid_capacity, 'paid_capacity')
        self.validate_required(self.total_capacity, 'total_capacity')
        self.validate_required(self.max_attack, 'max_attack')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.paid_capacity is not None:
            result['PaidCapacity'] = self.paid_capacity
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.max_attack is not None:
            result['MaxAttack'] = self.max_attack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('PaidCapacity') is not None:
            self.paid_capacity = m.get('PaidCapacity')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('MaxAttack') is not None:
            self.max_attack = m.get('MaxAttack')
        return self


class DescribePackPaidTrafficResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        pack_paid_traffics: List[DescribePackPaidTrafficResponsePackPaidTraffics] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.pack_paid_traffics = pack_paid_traffics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.pack_paid_traffics, 'pack_paid_traffics')
        if self.pack_paid_traffics:
            for k in self.pack_paid_traffics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['PackPaidTraffics'] = []
        if self.pack_paid_traffics is not None:
            for k in self.pack_paid_traffics:
                result['PackPaidTraffics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.pack_paid_traffics = []
        if m.get('PackPaidTraffics') is not None:
            for k in m.get('PackPaidTraffics'):
                temp_model = DescribePackPaidTrafficResponsePackPaidTraffics()
                self.pack_paid_traffics.append(temp_model.from_map(k))
        return self


class DescribeResourcePackUsageRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        end_time: int = None,
        start_time: int = None,
    ):
        self.source_ip = source_ip
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeResourcePackUsageResponsePackUsages(TeaModel):
    def __init__(
        self,
        traffic: float = None,
        time: int = None,
    ):
        self.traffic = traffic
        self.time = time

    def validate(self):
        self.validate_required(self.traffic, 'traffic')
        self.validate_required(self.time, 'time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeResourcePackUsageResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        interval: int = None,
        start_time: int = None,
        end_time: int = None,
        pack_usages: List[DescribeResourcePackUsageResponsePackUsages] = None,
    ):
        self.request_id = request_id
        self.interval = interval
        self.start_time = start_time
        self.end_time = end_time
        self.pack_usages = pack_usages

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.pack_usages, 'pack_usages')
        if self.pack_usages:
            for k in self.pack_usages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['PackUsages'] = []
        if self.pack_usages is not None:
            for k in self.pack_usages:
                result['PackUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.pack_usages = []
        if m.get('PackUsages') is not None:
            for k in m.get('PackUsages'):
                temp_model = DescribeResourcePackUsageResponsePackUsages()
                self.pack_usages.append(temp_model.from_map(k))
        return self


class DescribeResourcePackStatisticsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeResourcePackStatisticsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_pack_num: int = None,
        total_curr_capacity: int = None,
        total_used_capacity: int = None,
        total_init_capacity: int = None,
    ):
        self.request_id = request_id
        self.available_pack_num = available_pack_num
        self.total_curr_capacity = total_curr_capacity
        self.total_used_capacity = total_used_capacity
        self.total_init_capacity = total_init_capacity

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_pack_num, 'available_pack_num')
        self.validate_required(self.total_curr_capacity, 'total_curr_capacity')
        self.validate_required(self.total_used_capacity, 'total_used_capacity')
        self.validate_required(self.total_init_capacity, 'total_init_capacity')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_pack_num is not None:
            result['AvailablePackNum'] = self.available_pack_num
        if self.total_curr_capacity is not None:
            result['TotalCurrCapacity'] = self.total_curr_capacity
        if self.total_used_capacity is not None:
            result['TotalUsedCapacity'] = self.total_used_capacity
        if self.total_init_capacity is not None:
            result['TotalInitCapacity'] = self.total_init_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailablePackNum') is not None:
            self.available_pack_num = m.get('AvailablePackNum')
        if m.get('TotalCurrCapacity') is not None:
            self.total_curr_capacity = m.get('TotalCurrCapacity')
        if m.get('TotalUsedCapacity') is not None:
            self.total_used_capacity = m.get('TotalUsedCapacity')
        if m.get('TotalInitCapacity') is not None:
            self.total_init_capacity = m.get('TotalInitCapacity')
        return self


class DescribeResourcePackInstancesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.source_ip = source_ip
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class DescribeResourcePackInstancesResponseResourcePacks(TeaModel):
    def __init__(
        self,
        resource_pack_id: str = None,
        init_capacity: int = None,
        curr_capacity: int = None,
        start_time: int = None,
        end_time: int = None,
        status: str = None,
    ):
        self.resource_pack_id = resource_pack_id
        self.init_capacity = init_capacity
        self.curr_capacity = curr_capacity
        self.start_time = start_time
        self.end_time = end_time
        self.status = status

    def validate(self):
        self.validate_required(self.resource_pack_id, 'resource_pack_id')
        self.validate_required(self.init_capacity, 'init_capacity')
        self.validate_required(self.curr_capacity, 'curr_capacity')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_pack_id is not None:
            result['ResourcePackId'] = self.resource_pack_id
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourcePackId') is not None:
            self.resource_pack_id = m.get('ResourcePackId')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeResourcePackInstancesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        resource_packs: List[DescribeResourcePackInstancesResponseResourcePacks] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.resource_packs = resource_packs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.resource_packs, 'resource_packs')
        if self.resource_packs:
            for k in self.resource_packs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ResourcePacks'] = []
        if self.resource_packs is not None:
            for k in self.resource_packs:
                result['ResourcePacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.resource_packs = []
        if m.get('ResourcePacks') is not None:
            for k in m.get('ResourcePacks'):
                temp_model = DescribeResourcePackInstancesResponseResourcePacks()
                self.resource_packs.append(temp_model.from_map(k))
        return self


class DeleteBlackholeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        pack_id: str = None,
        ip: str = None,
    ):
        self.source_ip = source_ip
        self.pack_id = pack_id
        self.ip = ip

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DeleteBlackholeResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class CheckGrantRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CheckGrantResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: int = None,
    ):
        self.request_id = request_id
        self.status = status

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteProductRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        pack_id: str = None,
    ):
        self.source_ip = source_ip
        self.pack_id = pack_id

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class AddProductRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        pack_id: str = None,
        product: str = None,
    ):
        self.source_ip = source_ip
        self.pack_id = pack_id
        self.product = product

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.product, 'product')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        return self


class AddProductResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class AddIpRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        pack_id: str = None,
        ip_list: str = None,
    ):
        self.source_ip = source_ip
        self.pack_id = pack_id
        self.ip_list = ip_list

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.ip_list, 'ip_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class AddIpResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DescribeInstanceListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        pack_id_list: str = None,
        instance_id_list: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.source_ip = source_ip
        self.pack_id_list = pack_id_list
        self.instance_id_list = instance_id_list
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id_list is not None:
            result['PackIdList'] = self.pack_id_list
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PackIdList') is not None:
            self.pack_id_list = m.get('PackIdList')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceListResponseInstanceList(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        instance_id: str = None,
        product: str = None,
        remark: str = None,
        status: str = None,
        pack_id: str = None,
        gmt_create: int = None,
    ):
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.product = product
        self.remark = remark
        self.status = status
        self.pack_id = pack_id
        self.gmt_create = gmt_create

    def validate(self):
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.product, 'product')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.status, 'status')
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.gmt_create, 'gmt_create')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.product is not None:
            result['Product'] = self.product
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class DescribeInstanceListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        instance_list: List[DescribeInstanceListResponseInstanceList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.instance_list = instance_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.instance_list, 'instance_list')
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeInstanceListResponseInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class DescribeTopTrafficRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ipnet: str = None,
        start_time: str = None,
        end_time: str = None,
        rn: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.ipnet = ipnet
        self.start_time = start_time
        self.end_time = end_time
        self.rn = rn
        self.page_no = page_no
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ipnet is not None:
            result['Ipnet'] = self.ipnet
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.rn is not None:
            result['Rn'] = self.rn
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ipnet') is not None:
            self.ipnet = m.get('Ipnet')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Rn') is not None:
            self.rn = m.get('Rn')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTopTrafficResponseTrafficList(TeaModel):
    def __init__(
        self,
        pps: int = None,
        bps: int = None,
        attack_bps: int = None,
        attack_pps: int = None,
        ip: str = None,
    ):
        self.pps = pps
        self.bps = bps
        self.attack_bps = attack_bps
        self.attack_pps = attack_pps
        self.ip = ip

    def validate(self):
        self.validate_required(self.pps, 'pps')
        self.validate_required(self.bps, 'bps')
        self.validate_required(self.attack_bps, 'attack_bps')
        self.validate_required(self.attack_pps, 'attack_pps')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.bps is not None:
            result['Bps'] = self.bps
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps
        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')
        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeTopTrafficResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        traffic_list: List[DescribeTopTrafficResponseTrafficList] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.traffic_list = traffic_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.traffic_list, 'traffic_list')
        if self.traffic_list:
            for k in self.traffic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['TrafficList'] = []
        if self.traffic_list is not None:
            for k in self.traffic_list:
                result['TrafficList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.traffic_list = []
        if m.get('TrafficList') is not None:
            for k in m.get('TrafficList'):
                temp_model = DescribeTopTrafficResponseTrafficList()
                self.traffic_list.append(temp_model.from_map(k))
        return self


class DescribeDdosEventRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        pack_id: str = None,
        start_time: int = None,
        end_time: int = None,
        page_size: int = None,
        page_no: int = None,
    ):
        self.source_ip = source_ip
        self.pack_id = pack_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_no = page_no

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_no, 'page_no')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class DescribeDdosEventResponseEvents(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        pps: int = None,
        ip: str = None,
        mbps: int = None,
        status: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.pps = pps
        self.ip = ip
        self.mbps = mbps
        self.status = status

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.pps, 'pps')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.mbps, 'mbps')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDdosEventResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        events: List[DescribeDdosEventResponseEvents] = None,
    ):
        self.request_id = request_id
        self.total = total
        self.events = events

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDdosEventResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DescribeTrafficRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        name: str = None,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
    ):
        self.source_ip = source_ip
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.interval, 'interval')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.name is not None:
            result['Name'] = self.name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeTrafficResponseFlowList(TeaModel):
    def __init__(
        self,
        pps: int = None,
        flow_type: str = None,
        kbps: int = None,
        name: str = None,
        time: int = None,
    ):
        self.pps = pps
        self.flow_type = flow_type
        self.kbps = kbps
        self.name = name
        self.time = time

    def validate(self):
        self.validate_required(self.pps, 'pps')
        self.validate_required(self.flow_type, 'flow_type')
        self.validate_required(self.kbps, 'kbps')
        self.validate_required(self.name, 'name')
        self.validate_required(self.time, 'time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.kbps is not None:
            result['Kbps'] = self.kbps
        if self.name is not None:
            result['Name'] = self.name
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('Kbps') is not None:
            self.kbps = m.get('Kbps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class DescribeTrafficResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        flow_list: List[DescribeTrafficResponseFlowList] = None,
    ):
        self.request_id = request_id
        self.flow_list = flow_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.flow_list, 'flow_list')
        if self.flow_list:
            for k in self.flow_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FlowList'] = []
        if self.flow_list is not None:
            for k in self.flow_list:
                result['FlowList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.flow_list = []
        if m.get('FlowList') is not None:
            for k in m.get('FlowList'):
                temp_model = DescribeTrafficResponseFlowList()
                self.flow_list.append(temp_model.from_map(k))
        return self


class DeleteIpRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        pack_id: str = None,
        ip_list: str = None,
    ):
        self.source_ip = source_ip
        self.pack_id = pack_id
        self.ip_list = ip_list

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.ip_list, 'ip_list')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        return self


class DeleteIpResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DescribePackRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        pack_id: str = None,
    ):
        self.source_ip = source_ip
        self.pack_id = pack_id

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        return self


class DescribePackResponsePackInfoIpList(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        self.ip = ip

    def validate(self):
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribePackResponsePackInfoPackConfig(TeaModel):
    def __init__(
        self,
        pack_adv_thre: int = None,
        ip_advance_thre: int = None,
        ip_basic_thre: int = None,
        pack_basic_thre: int = None,
        ip_spec: int = None,
    ):
        self.pack_adv_thre = pack_adv_thre
        self.ip_advance_thre = ip_advance_thre
        self.ip_basic_thre = ip_basic_thre
        self.pack_basic_thre = pack_basic_thre
        self.ip_spec = ip_spec

    def validate(self):
        self.validate_required(self.pack_adv_thre, 'pack_adv_thre')
        self.validate_required(self.ip_advance_thre, 'ip_advance_thre')
        self.validate_required(self.ip_basic_thre, 'ip_basic_thre')
        self.validate_required(self.pack_basic_thre, 'pack_basic_thre')
        self.validate_required(self.ip_spec, 'ip_spec')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pack_adv_thre is not None:
            result['PackAdvThre'] = self.pack_adv_thre
        if self.ip_advance_thre is not None:
            result['IpAdvanceThre'] = self.ip_advance_thre
        if self.ip_basic_thre is not None:
            result['IpBasicThre'] = self.ip_basic_thre
        if self.pack_basic_thre is not None:
            result['PackBasicThre'] = self.pack_basic_thre
        if self.ip_spec is not None:
            result['IpSpec'] = self.ip_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackAdvThre') is not None:
            self.pack_adv_thre = m.get('PackAdvThre')
        if m.get('IpAdvanceThre') is not None:
            self.ip_advance_thre = m.get('IpAdvanceThre')
        if m.get('IpBasicThre') is not None:
            self.ip_basic_thre = m.get('IpBasicThre')
        if m.get('PackBasicThre') is not None:
            self.pack_basic_thre = m.get('PackBasicThre')
        if m.get('IpSpec') is not None:
            self.ip_spec = m.get('IpSpec')
        return self


class DescribePackResponsePackInfo(TeaModel):
    def __init__(
        self,
        region: str = None,
        available_delete_blackhole_count: int = None,
        ip_list: List[DescribePackResponsePackInfoIpList] = None,
        pack_config: DescribePackResponsePackInfoPackConfig = None,
    ):
        self.region = region
        self.available_delete_blackhole_count = available_delete_blackhole_count
        self.ip_list = ip_list
        self.pack_config = pack_config

    def validate(self):
        self.validate_required(self.region, 'region')
        self.validate_required(self.available_delete_blackhole_count, 'available_delete_blackhole_count')
        self.validate_required(self.ip_list, 'ip_list')
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()
        self.validate_required(self.pack_config, 'pack_config')
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.available_delete_blackhole_count is not None:
            result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = m.get('AvailableDeleteBlackholeCount')
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = DescribePackResponsePackInfoIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('PackConfig') is not None:
            temp_model = DescribePackResponsePackInfoPackConfig()
            self.pack_config = temp_model.from_map(m['PackConfig'])
        return self


class DescribePackResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        pack_info: DescribePackResponsePackInfo = None,
    ):
        self.request_id = request_id
        self.pack_info = pack_info

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.pack_info, 'pack_info')
        if self.pack_info:
            self.pack_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pack_info is not None:
            result['PackInfo'] = self.pack_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PackInfo') is not None:
            temp_model = DescribePackResponsePackInfo()
            self.pack_info = temp_model.from_map(m['PackInfo'])
        return self


class DescribePackListRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribePackListResponsePackListPackConfig(TeaModel):
    def __init__(
        self,
        pack_adv_thre: int = None,
        ip_advance_thre: int = None,
        ip_basic_thre: int = None,
        pack_basic_thre: int = None,
        ip_spec: int = None,
    ):
        self.pack_adv_thre = pack_adv_thre
        self.ip_advance_thre = ip_advance_thre
        self.ip_basic_thre = ip_basic_thre
        self.pack_basic_thre = pack_basic_thre
        self.ip_spec = ip_spec

    def validate(self):
        self.validate_required(self.pack_adv_thre, 'pack_adv_thre')
        self.validate_required(self.ip_advance_thre, 'ip_advance_thre')
        self.validate_required(self.ip_basic_thre, 'ip_basic_thre')
        self.validate_required(self.pack_basic_thre, 'pack_basic_thre')
        self.validate_required(self.ip_spec, 'ip_spec')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pack_adv_thre is not None:
            result['PackAdvThre'] = self.pack_adv_thre
        if self.ip_advance_thre is not None:
            result['IpAdvanceThre'] = self.ip_advance_thre
        if self.ip_basic_thre is not None:
            result['IpBasicThre'] = self.ip_basic_thre
        if self.pack_basic_thre is not None:
            result['PackBasicThre'] = self.pack_basic_thre
        if self.ip_spec is not None:
            result['IpSpec'] = self.ip_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackAdvThre') is not None:
            self.pack_adv_thre = m.get('PackAdvThre')
        if m.get('IpAdvanceThre') is not None:
            self.ip_advance_thre = m.get('IpAdvanceThre')
        if m.get('IpBasicThre') is not None:
            self.ip_basic_thre = m.get('IpBasicThre')
        if m.get('PackBasicThre') is not None:
            self.pack_basic_thre = m.get('PackBasicThre')
        if m.get('IpSpec') is not None:
            self.ip_spec = m.get('IpSpec')
        return self


class DescribePackListResponsePackList(TeaModel):
    def __init__(
        self,
        available_delete_blackhole_count: int = None,
        region: str = None,
        pack_id: str = None,
        pack_config: DescribePackListResponsePackListPackConfig = None,
    ):
        self.available_delete_blackhole_count = available_delete_blackhole_count
        self.region = region
        self.pack_id = pack_id
        self.pack_config = pack_config

    def validate(self):
        self.validate_required(self.available_delete_blackhole_count, 'available_delete_blackhole_count')
        self.validate_required(self.region, 'region')
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.pack_config, 'pack_config')
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_delete_blackhole_count is not None:
            result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count
        if self.region is not None:
            result['Region'] = self.region
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = m.get('AvailableDeleteBlackholeCount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PackId') is not None:
            self.pack_id = m.get('PackId')
        if m.get('PackConfig') is not None:
            temp_model = DescribePackListResponsePackListPackConfig()
            self.pack_config = temp_model.from_map(m['PackConfig'])
        return self


class DescribePackListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        pack_list: List[DescribePackListResponsePackList] = None,
    ):
        self.request_id = request_id
        self.pack_list = pack_list

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.pack_list, 'pack_list')
        if self.pack_list:
            for k in self.pack_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PackList'] = []
        if self.pack_list is not None:
            for k in self.pack_list:
                result['PackList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.pack_list = []
        if m.get('PackList') is not None:
            for k in m.get('PackList'):
                temp_model = DescribePackListResponsePackList()
                self.pack_list.append(temp_model.from_map(k))
        return self


