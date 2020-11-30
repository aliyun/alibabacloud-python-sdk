# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class DescribeOnDemandInstanceRequest(TeaModel):
    def __init__(self, page_no=None, page_size=None, region_id=None):
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        return self


class DescribeOnDemandInstanceResponse(TeaModel):
    def __init__(self, request_id=None, total=None, instances=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: str
        self.instances = instances      # type: List[DescribeOnDemandInstanceResponseInstances]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.instances = []
        if map.get('Instances') is not None:
            for k in map.get('Instances'):
                temp_model = DescribeOnDemandInstanceResponseInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeOnDemandInstanceResponseInstances(TeaModel):
    def __init__(self, instance_id=None, remark=None, defense_status=None, region_id=None, ipnet=None):
        self.instance_id = instance_id  # type: str
        self.remark = remark            # type: str
        self.defense_status = defense_status  # type: str
        self.region_id = region_id      # type: str
        self.ipnet = ipnet              # type: List[str]

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.defense_status, 'defense_status')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.ipnet, 'ipnet')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Remark') is not None:
            self.remark = map.get('Remark')
        if map.get('DefenseStatus') is not None:
            self.defense_status = map.get('DefenseStatus')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('Ipnet') is not None:
            self.ipnet = map.get('Ipnet')
        return self


class ModifyOnDemaondDefenseStatusRequest(TeaModel):
    def __init__(self, instance_id=None, defense_status=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.defense_status = defense_status  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.defense_status, 'defense_status')

    def to_map(self):
        result = {}
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.defense_status is not None:
            result['DefenseStatus'] = self.defense_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('DefenseStatus') is not None:
            self.defense_status = map.get('DefenseStatus')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        return self


class ModifyOnDemaondDefenseStatusResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(self, source_ip=None, lang=None, current_page=None, page_size=None, start_time=None, end_time=None):
        self.source_ip = source_ip      # type: str
        self.lang = lang                # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Lang') is not None:
            self.lang = map.get('Lang')
        if map.get('CurrentPage') is not None:
            self.current_page = map.get('CurrentPage')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, op_entities=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.op_entities = op_entities  # type: List[DescribeOpEntitiesResponseOpEntities]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.op_entities, 'op_entities')
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.op_entities = []
        if map.get('OpEntities') is not None:
            for k in map.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        return self


class DescribeOpEntitiesResponseOpEntities(TeaModel):
    def __init__(self, entity_object=None, entity_type=None, op_desc=None, op_account=None, op_action=None,
                 gmt_create=None):
        self.entity_object = entity_object  # type: str
        self.entity_type = entity_type  # type: int
        self.op_desc = op_desc          # type: str
        self.op_account = op_account    # type: str
        self.op_action = op_action      # type: int
        self.gmt_create = gmt_create    # type: int

    def validate(self):
        self.validate_required(self.entity_object, 'entity_object')
        self.validate_required(self.entity_type, 'entity_type')
        self.validate_required(self.op_desc, 'op_desc')
        self.validate_required(self.op_account, 'op_account')
        self.validate_required(self.op_action, 'op_action')
        self.validate_required(self.gmt_create, 'gmt_create')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('EntityObject') is not None:
            self.entity_object = map.get('EntityObject')
        if map.get('EntityType') is not None:
            self.entity_type = map.get('EntityType')
        if map.get('OpDesc') is not None:
            self.op_desc = map.get('OpDesc')
        if map.get('OpAccount') is not None:
            self.op_account = map.get('OpAccount')
        if map.get('OpAction') is not None:
            self.op_action = map.get('OpAction')
        if map.get('GmtCreate') is not None:
            self.gmt_create = map.get('GmtCreate')
        return self


class DescribePackPaidTrafficRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, current_page=None, page_size=None, start_time=None,
                 end_time=None):
        self.source_ip = source_ip      # type: str
        self.instance_id = instance_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('CurrentPage') is not None:
            self.current_page = map.get('CurrentPage')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        return self


class DescribePackPaidTrafficResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, pack_paid_traffics=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.pack_paid_traffics = pack_paid_traffics  # type: List[DescribePackPaidTrafficResponsePackPaidTraffics]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.pack_paid_traffics, 'pack_paid_traffics')
        if self.pack_paid_traffics:
            for k in self.pack_paid_traffics:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['PackPaidTraffics'] = []
        if self.pack_paid_traffics is not None:
            for k in self.pack_paid_traffics:
                result['PackPaidTraffics'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.pack_paid_traffics = []
        if map.get('PackPaidTraffics') is not None:
            for k in map.get('PackPaidTraffics'):
                temp_model = DescribePackPaidTrafficResponsePackPaidTraffics()
                self.pack_paid_traffics.append(temp_model.from_map(k))
        return self


class DescribePackPaidTrafficResponsePackPaidTraffics(TeaModel):
    def __init__(self, instance_id=None, start_time=None, base_bandwidth=None, elastic_bandwidth=None,
                 paid_capacity=None, total_capacity=None, max_attack=None):
        self.instance_id = instance_id  # type: str
        self.start_time = start_time    # type: int
        self.base_bandwidth = base_bandwidth  # type: int
        self.elastic_bandwidth = elastic_bandwidth  # type: int
        self.paid_capacity = paid_capacity  # type: float
        self.total_capacity = total_capacity  # type: float
        self.max_attack = max_attack    # type: float

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.base_bandwidth, 'base_bandwidth')
        self.validate_required(self.elastic_bandwidth, 'elastic_bandwidth')
        self.validate_required(self.paid_capacity, 'paid_capacity')
        self.validate_required(self.total_capacity, 'total_capacity')
        self.validate_required(self.max_attack, 'max_attack')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('BaseBandwidth') is not None:
            self.base_bandwidth = map.get('BaseBandwidth')
        if map.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = map.get('ElasticBandwidth')
        if map.get('PaidCapacity') is not None:
            self.paid_capacity = map.get('PaidCapacity')
        if map.get('TotalCapacity') is not None:
            self.total_capacity = map.get('TotalCapacity')
        if map.get('MaxAttack') is not None:
            self.max_attack = map.get('MaxAttack')
        return self


class DescribeResourcePackUsageRequest(TeaModel):
    def __init__(self, source_ip=None, end_time=None, start_time=None):
        self.source_ip = source_ip      # type: str
        self.end_time = end_time        # type: int
        self.start_time = start_time    # type: int

    def validate(self):
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        return self


class DescribeResourcePackUsageResponse(TeaModel):
    def __init__(self, request_id=None, interval=None, start_time=None, end_time=None, pack_usages=None):
        self.request_id = request_id    # type: str
        self.interval = interval        # type: int
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.pack_usages = pack_usages  # type: List[DescribeResourcePackUsageResponsePackUsages]

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        self.pack_usages = []
        if map.get('PackUsages') is not None:
            for k in map.get('PackUsages'):
                temp_model = DescribeResourcePackUsageResponsePackUsages()
                self.pack_usages.append(temp_model.from_map(k))
        return self


class DescribeResourcePackUsageResponsePackUsages(TeaModel):
    def __init__(self, traffic=None, time=None):
        self.traffic = traffic          # type: float
        self.time = time                # type: int

    def validate(self):
        self.validate_required(self.traffic, 'traffic')
        self.validate_required(self.time, 'time')

    def to_map(self):
        result = {}
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, map={}):
        if map.get('Traffic') is not None:
            self.traffic = map.get('Traffic')
        if map.get('Time') is not None:
            self.time = map.get('Time')
        return self


class DescribeResourcePackStatisticsRequest(TeaModel):
    def __init__(self, source_ip=None):
        self.source_ip = source_ip      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        return self


class DescribeResourcePackStatisticsResponse(TeaModel):
    def __init__(self, request_id=None, available_pack_num=None, total_curr_capacity=None,
                 total_used_capacity=None, total_init_capacity=None):
        self.request_id = request_id    # type: str
        self.available_pack_num = available_pack_num  # type: int
        self.total_curr_capacity = total_curr_capacity  # type: int
        self.total_used_capacity = total_used_capacity  # type: int
        self.total_init_capacity = total_init_capacity  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.available_pack_num, 'available_pack_num')
        self.validate_required(self.total_curr_capacity, 'total_curr_capacity')
        self.validate_required(self.total_used_capacity, 'total_used_capacity')
        self.validate_required(self.total_init_capacity, 'total_init_capacity')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('AvailablePackNum') is not None:
            self.available_pack_num = map.get('AvailablePackNum')
        if map.get('TotalCurrCapacity') is not None:
            self.total_curr_capacity = map.get('TotalCurrCapacity')
        if map.get('TotalUsedCapacity') is not None:
            self.total_used_capacity = map.get('TotalUsedCapacity')
        if map.get('TotalInitCapacity') is not None:
            self.total_init_capacity = map.get('TotalInitCapacity')
        return self


class DescribeResourcePackInstancesRequest(TeaModel):
    def __init__(self, source_ip=None, page_size=None, current_page=None):
        self.source_ip = source_ip      # type: str
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('CurrentPage') is not None:
            self.current_page = map.get('CurrentPage')
        return self


class DescribeResourcePackInstancesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, resource_packs=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.resource_packs = resource_packs  # type: List[DescribeResourcePackInstancesResponseResourcePacks]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.resource_packs, 'resource_packs')
        if self.resource_packs:
            for k in self.resource_packs:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ResourcePacks'] = []
        if self.resource_packs is not None:
            for k in self.resource_packs:
                result['ResourcePacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('TotalCount') is not None:
            self.total_count = map.get('TotalCount')
        self.resource_packs = []
        if map.get('ResourcePacks') is not None:
            for k in map.get('ResourcePacks'):
                temp_model = DescribeResourcePackInstancesResponseResourcePacks()
                self.resource_packs.append(temp_model.from_map(k))
        return self


class DescribeResourcePackInstancesResponseResourcePacks(TeaModel):
    def __init__(self, resource_pack_id=None, init_capacity=None, curr_capacity=None, start_time=None,
                 end_time=None, status=None):
        self.resource_pack_id = resource_pack_id  # type: str
        self.init_capacity = init_capacity  # type: int
        self.curr_capacity = curr_capacity  # type: int
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.resource_pack_id, 'resource_pack_id')
        self.validate_required(self.init_capacity, 'init_capacity')
        self.validate_required(self.curr_capacity, 'curr_capacity')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ResourcePackId') is not None:
            self.resource_pack_id = map.get('ResourcePackId')
        if map.get('InitCapacity') is not None:
            self.init_capacity = map.get('InitCapacity')
        if map.get('CurrCapacity') is not None:
            self.curr_capacity = map.get('CurrCapacity')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class DeleteBlackholeRequest(TeaModel):
    def __init__(self, source_ip=None, pack_id=None, ip=None):
        self.source_ip = source_ip      # type: str
        self.pack_id = pack_id          # type: str
        self.ip = ip                    # type: str

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        if map.get('Ip') is not None:
            self.ip = map.get('Ip')
        return self


class DeleteBlackholeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CheckGrantRequest(TeaModel):
    def __init__(self, source_ip=None):
        self.source_ip = source_ip      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        return self


class CheckGrantResponse(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id    # type: str
        self.status = status            # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class DeleteProductRequest(TeaModel):
    def __init__(self, source_ip=None, pack_id=None):
        self.source_ip = source_ip      # type: str
        self.pack_id = pack_id          # type: str

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class AddProductRequest(TeaModel):
    def __init__(self, source_ip=None, pack_id=None, product=None):
        self.source_ip = source_ip      # type: str
        self.pack_id = pack_id          # type: str
        self.product = product          # type: str

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.product, 'product')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.product is not None:
            result['Product'] = self.product
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        if map.get('Product') is not None:
            self.product = map.get('Product')
        return self


class AddProductResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class AddIpRequest(TeaModel):
    def __init__(self, source_ip=None, pack_id=None, ip_list=None):
        self.source_ip = source_ip      # type: str
        self.pack_id = pack_id          # type: str
        self.ip_list = ip_list          # type: str

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.ip_list, 'ip_list')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        if map.get('IpList') is not None:
            self.ip_list = map.get('IpList')
        return self


class AddIpResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribeInstanceListRequest(TeaModel):
    def __init__(self, source_ip=None, pack_id_list=None, instance_id_list=None, page_no=None, page_size=None):
        self.source_ip = source_ip      # type: str
        self.pack_id_list = pack_id_list  # type: str
        self.instance_id_list = instance_id_list  # type: str
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PackIdList') is not None:
            self.pack_id_list = map.get('PackIdList')
        if map.get('InstanceIdList') is not None:
            self.instance_id_list = map.get('InstanceIdList')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        return self


class DescribeInstanceListResponse(TeaModel):
    def __init__(self, request_id=None, total=None, instance_list=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.instance_list = instance_list  # type: List[DescribeInstanceListResponseInstanceList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.instance_list, 'instance_list')
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.instance_list = []
        if map.get('InstanceList') is not None:
            for k in map.get('InstanceList'):
                temp_model = DescribeInstanceListResponseInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class DescribeInstanceListResponseInstanceList(TeaModel):
    def __init__(self, expire_time=None, instance_id=None, product=None, remark=None, status=None, pack_id=None,
                 gmt_create=None):
        self.expire_time = expire_time  # type: int
        self.instance_id = instance_id  # type: str
        self.product = product          # type: str
        self.remark = remark            # type: str
        self.status = status            # type: str
        self.pack_id = pack_id          # type: str
        self.gmt_create = gmt_create    # type: int

    def validate(self):
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.product, 'product')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.status, 'status')
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.gmt_create, 'gmt_create')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ExpireTime') is not None:
            self.expire_time = map.get('ExpireTime')
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Product') is not None:
            self.product = map.get('Product')
        if map.get('Remark') is not None:
            self.remark = map.get('Remark')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        if map.get('GmtCreate') is not None:
            self.gmt_create = map.get('GmtCreate')
        return self


class DescribeTopTrafficRequest(TeaModel):
    def __init__(self, instance_id=None, ipnet=None, start_time=None, end_time=None, rn=None, page_no=None,
                 page_size=None, resource_group_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.ipnet = ipnet              # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.rn = rn                    # type: int
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('InstanceId') is not None:
            self.instance_id = map.get('InstanceId')
        if map.get('Ipnet') is not None:
            self.ipnet = map.get('Ipnet')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Rn') is not None:
            self.rn = map.get('Rn')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        return self


class DescribeTopTrafficResponse(TeaModel):
    def __init__(self, request_id=None, total=None, traffic_list=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.traffic_list = traffic_list  # type: List[DescribeTopTrafficResponseTrafficList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.traffic_list, 'traffic_list')
        if self.traffic_list:
            for k in self.traffic_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['TrafficList'] = []
        if self.traffic_list is not None:
            for k in self.traffic_list:
                result['TrafficList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.traffic_list = []
        if map.get('TrafficList') is not None:
            for k in map.get('TrafficList'):
                temp_model = DescribeTopTrafficResponseTrafficList()
                self.traffic_list.append(temp_model.from_map(k))
        return self


class DescribeTopTrafficResponseTrafficList(TeaModel):
    def __init__(self, pps=None, bps=None, attack_bps=None, attack_pps=None, ip=None):
        self.pps = pps                  # type: int
        self.bps = bps                  # type: int
        self.attack_bps = attack_bps    # type: int
        self.attack_pps = attack_pps    # type: int
        self.ip = ip                    # type: str

    def validate(self):
        self.validate_required(self.pps, 'pps')
        self.validate_required(self.bps, 'bps')
        self.validate_required(self.attack_bps, 'attack_bps')
        self.validate_required(self.attack_pps, 'attack_pps')
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('Pps') is not None:
            self.pps = map.get('Pps')
        if map.get('Bps') is not None:
            self.bps = map.get('Bps')
        if map.get('AttackBps') is not None:
            self.attack_bps = map.get('AttackBps')
        if map.get('AttackPps') is not None:
            self.attack_pps = map.get('AttackPps')
        if map.get('Ip') is not None:
            self.ip = map.get('Ip')
        return self


class DescribeDdosEventRequest(TeaModel):
    def __init__(self, source_ip=None, pack_id=None, start_time=None, end_time=None, page_size=None, page_no=None):
        self.source_ip = source_ip      # type: str
        self.pack_id = pack_id          # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.page_size = page_size      # type: int
        self.page_no = page_no          # type: int

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_no, 'page_no')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('PageSize') is not None:
            self.page_size = map.get('PageSize')
        if map.get('PageNo') is not None:
            self.page_no = map.get('PageNo')
        return self


class DescribeDdosEventResponse(TeaModel):
    def __init__(self, request_id=None, total=None, events=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.events = events            # type: List[DescribeDdosEventResponseEvents]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Total') is not None:
            self.total = map.get('Total')
        self.events = []
        if map.get('Events') is not None:
            for k in map.get('Events'):
                temp_model = DescribeDdosEventResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class DescribeDdosEventResponseEvents(TeaModel):
    def __init__(self, start_time=None, end_time=None, pps=None, ip=None, mbps=None, status=None):
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.pps = pps                  # type: int
        self.ip = ip                    # type: str
        self.mbps = mbps                # type: int
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.pps, 'pps')
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.mbps, 'mbps')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Pps') is not None:
            self.pps = map.get('Pps')
        if map.get('Ip') is not None:
            self.ip = map.get('Ip')
        if map.get('Mbps') is not None:
            self.mbps = map.get('Mbps')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        return self


class DescribeTrafficRequest(TeaModel):
    def __init__(self, source_ip=None, name=None, start_time=None, end_time=None, interval=None):
        self.source_ip = source_ip      # type: str
        self.name = name                # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.interval = interval        # type: int

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.interval, 'interval')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('StartTime') is not None:
            self.start_time = map.get('StartTime')
        if map.get('EndTime') is not None:
            self.end_time = map.get('EndTime')
        if map.get('Interval') is not None:
            self.interval = map.get('Interval')
        return self


class DescribeTrafficResponse(TeaModel):
    def __init__(self, request_id=None, flow_list=None):
        self.request_id = request_id    # type: str
        self.flow_list = flow_list      # type: List[DescribeTrafficResponseFlowList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.flow_list, 'flow_list')
        if self.flow_list:
            for k in self.flow_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FlowList'] = []
        if self.flow_list is not None:
            for k in self.flow_list:
                result['FlowList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.flow_list = []
        if map.get('FlowList') is not None:
            for k in map.get('FlowList'):
                temp_model = DescribeTrafficResponseFlowList()
                self.flow_list.append(temp_model.from_map(k))
        return self


class DescribeTrafficResponseFlowList(TeaModel):
    def __init__(self, pps=None, flow_type=None, kbps=None, name=None, time=None):
        self.pps = pps                  # type: int
        self.flow_type = flow_type      # type: str
        self.kbps = kbps                # type: int
        self.name = name                # type: str
        self.time = time                # type: int

    def validate(self):
        self.validate_required(self.pps, 'pps')
        self.validate_required(self.flow_type, 'flow_type')
        self.validate_required(self.kbps, 'kbps')
        self.validate_required(self.name, 'name')
        self.validate_required(self.time, 'time')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('Pps') is not None:
            self.pps = map.get('Pps')
        if map.get('FlowType') is not None:
            self.flow_type = map.get('FlowType')
        if map.get('Kbps') is not None:
            self.kbps = map.get('Kbps')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Time') is not None:
            self.time = map.get('Time')
        return self


class DeleteIpRequest(TeaModel):
    def __init__(self, source_ip=None, pack_id=None, ip_list=None):
        self.source_ip = source_ip      # type: str
        self.pack_id = pack_id          # type: str
        self.ip_list = ip_list          # type: str

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.ip_list, 'ip_list')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        if map.get('IpList') is not None:
            self.ip_list = map.get('IpList')
        return self


class DeleteIpResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class DescribePackRequest(TeaModel):
    def __init__(self, source_ip=None, pack_id=None):
        self.source_ip = source_ip      # type: str
        self.pack_id = pack_id          # type: str

    def validate(self):
        self.validate_required(self.pack_id, 'pack_id')

    def to_map(self):
        result = {}
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        return result

    def from_map(self, map={}):
        if map.get('SourceIp') is not None:
            self.source_ip = map.get('SourceIp')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        return self


class DescribePackResponse(TeaModel):
    def __init__(self, request_id=None, pack_info=None):
        self.request_id = request_id    # type: str
        self.pack_info = pack_info      # type: DescribePackResponsePackInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.pack_info, 'pack_info')
        if self.pack_info:
            self.pack_info.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.pack_info is not None:
            result['PackInfo'] = self.pack_info.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('PackInfo') is not None:
            temp_model = DescribePackResponsePackInfo()
            self.pack_info = temp_model.from_map(map['PackInfo'])
        return self


class DescribePackResponsePackInfoIpList(TeaModel):
    def __init__(self, ip=None):
        self.ip = ip                    # type: str

    def validate(self):
        self.validate_required(self.ip, 'ip')

    def to_map(self):
        result = {}
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, map={}):
        if map.get('Ip') is not None:
            self.ip = map.get('Ip')
        return self


class DescribePackResponsePackInfoPackConfig(TeaModel):
    def __init__(self, pack_adv_thre=None, ip_advance_thre=None, ip_basic_thre=None, pack_basic_thre=None,
                 ip_spec=None):
        self.pack_adv_thre = pack_adv_thre  # type: int
        self.ip_advance_thre = ip_advance_thre  # type: int
        self.ip_basic_thre = ip_basic_thre  # type: int
        self.pack_basic_thre = pack_basic_thre  # type: int
        self.ip_spec = ip_spec          # type: int

    def validate(self):
        self.validate_required(self.pack_adv_thre, 'pack_adv_thre')
        self.validate_required(self.ip_advance_thre, 'ip_advance_thre')
        self.validate_required(self.ip_basic_thre, 'ip_basic_thre')
        self.validate_required(self.pack_basic_thre, 'pack_basic_thre')
        self.validate_required(self.ip_spec, 'ip_spec')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('PackAdvThre') is not None:
            self.pack_adv_thre = map.get('PackAdvThre')
        if map.get('IpAdvanceThre') is not None:
            self.ip_advance_thre = map.get('IpAdvanceThre')
        if map.get('IpBasicThre') is not None:
            self.ip_basic_thre = map.get('IpBasicThre')
        if map.get('PackBasicThre') is not None:
            self.pack_basic_thre = map.get('PackBasicThre')
        if map.get('IpSpec') is not None:
            self.ip_spec = map.get('IpSpec')
        return self


class DescribePackResponsePackInfo(TeaModel):
    def __init__(self, region=None, available_delete_blackhole_count=None, ip_list=None, pack_config=None):
        self.region = region            # type: str
        self.available_delete_blackhole_count = available_delete_blackhole_count  # type: int
        self.ip_list = ip_list          # type: List[DescribePackResponsePackInfoIpList]
        self.pack_config = pack_config  # type: DescribePackResponsePackInfoPackConfig

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
        result = {}
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

    def from_map(self, map={}):
        if map.get('Region') is not None:
            self.region = map.get('Region')
        if map.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = map.get('AvailableDeleteBlackholeCount')
        self.ip_list = []
        if map.get('IpList') is not None:
            for k in map.get('IpList'):
                temp_model = DescribePackResponsePackInfoIpList()
                self.ip_list.append(temp_model.from_map(k))
        if map.get('PackConfig') is not None:
            temp_model = DescribePackResponsePackInfoPackConfig()
            self.pack_config = temp_model.from_map(map['PackConfig'])
        return self


class DescribePackListRequest(TeaModel):
    def __init__(self, resource_group_id=None, region_id=None):
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        if map.get('ResourceGroupId') is not None:
            self.resource_group_id = map.get('ResourceGroupId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        return self


class DescribePackListResponse(TeaModel):
    def __init__(self, request_id=None, pack_list=None):
        self.request_id = request_id    # type: str
        self.pack_list = pack_list      # type: List[DescribePackListResponsePackList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.pack_list, 'pack_list')
        if self.pack_list:
            for k in self.pack_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PackList'] = []
        if self.pack_list is not None:
            for k in self.pack_list:
                result['PackList'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        self.pack_list = []
        if map.get('PackList') is not None:
            for k in map.get('PackList'):
                temp_model = DescribePackListResponsePackList()
                self.pack_list.append(temp_model.from_map(k))
        return self


class DescribePackListResponsePackListPackConfig(TeaModel):
    def __init__(self, pack_adv_thre=None, ip_advance_thre=None, ip_basic_thre=None, pack_basic_thre=None,
                 ip_spec=None):
        self.pack_adv_thre = pack_adv_thre  # type: int
        self.ip_advance_thre = ip_advance_thre  # type: int
        self.ip_basic_thre = ip_basic_thre  # type: int
        self.pack_basic_thre = pack_basic_thre  # type: int
        self.ip_spec = ip_spec          # type: int

    def validate(self):
        self.validate_required(self.pack_adv_thre, 'pack_adv_thre')
        self.validate_required(self.ip_advance_thre, 'ip_advance_thre')
        self.validate_required(self.ip_basic_thre, 'ip_basic_thre')
        self.validate_required(self.pack_basic_thre, 'pack_basic_thre')
        self.validate_required(self.ip_spec, 'ip_spec')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('PackAdvThre') is not None:
            self.pack_adv_thre = map.get('PackAdvThre')
        if map.get('IpAdvanceThre') is not None:
            self.ip_advance_thre = map.get('IpAdvanceThre')
        if map.get('IpBasicThre') is not None:
            self.ip_basic_thre = map.get('IpBasicThre')
        if map.get('PackBasicThre') is not None:
            self.pack_basic_thre = map.get('PackBasicThre')
        if map.get('IpSpec') is not None:
            self.ip_spec = map.get('IpSpec')
        return self


class DescribePackListResponsePackList(TeaModel):
    def __init__(self, available_delete_blackhole_count=None, region=None, pack_id=None, pack_config=None):
        self.available_delete_blackhole_count = available_delete_blackhole_count  # type: int
        self.region = region            # type: str
        self.pack_id = pack_id          # type: str
        self.pack_config = pack_config  # type: DescribePackListResponsePackListPackConfig

    def validate(self):
        self.validate_required(self.available_delete_blackhole_count, 'available_delete_blackhole_count')
        self.validate_required(self.region, 'region')
        self.validate_required(self.pack_id, 'pack_id')
        self.validate_required(self.pack_config, 'pack_config')
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        result = {}
        if self.available_delete_blackhole_count is not None:
            result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count
        if self.region is not None:
            result['Region'] = self.region
        if self.pack_id is not None:
            result['PackId'] = self.pack_id
        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()
        return result

    def from_map(self, map={}):
        if map.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = map.get('AvailableDeleteBlackholeCount')
        if map.get('Region') is not None:
            self.region = map.get('Region')
        if map.get('PackId') is not None:
            self.pack_id = map.get('PackId')
        if map.get('PackConfig') is not None:
            temp_model = DescribePackListResponsePackListPackConfig()
            self.pack_config = temp_model.from_map(map['PackConfig'])
        return self


