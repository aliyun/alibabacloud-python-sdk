# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class DescribeOnDemandInstanceStatusRequest(TeaModel):
    def __init__(self, instance_id_list=None, region_id=None):
        self.instance_id_list = instance_id_list  # type: List[str]
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id_list, 'instance_id_list')

    def to_map(self):
        result = {}
        result['InstanceIdList'] = self.instance_id_list
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id_list = map.get('InstanceIdList')
        self.region_id = map.get('RegionId')
        return self


class DescribeOnDemandInstanceStatusResponse(TeaModel):
    def __init__(self, request_id=None, instances=None):
        self.request_id = request_id    # type: str
        self.instances = instances      # type: List[DescribeOnDemandInstanceStatusResponseInstances]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        else:
            result['Instances'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.instances = []
        if map.get('Instances') is not None:
            for k in map.get('Instances'):
                temp_model = DescribeOnDemandInstanceStatusResponseInstances()
                self.instances.append(temp_model.from_map(k))
        else:
            self.instances = None
        return self


class DescribeOnDemandInstanceStatusResponseInstances(TeaModel):
    def __init__(self, user_id=None, net=None, instance_id=None, registed_as=None, desc=None, declared=None,
                 mode=None):
        self.user_id = user_id          # type: str
        self.net = net                  # type: str
        self.instance_id = instance_id  # type: str
        self.registed_as = registed_as  # type: str
        self.desc = desc                # type: str
        self.declared = declared        # type: str
        self.mode = mode                # type: str

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.net, 'net')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.registed_as, 'registed_as')
        self.validate_required(self.desc, 'desc')
        self.validate_required(self.declared, 'declared')
        self.validate_required(self.mode, 'mode')

    def to_map(self):
        result = {}
        result['UserId'] = self.user_id
        result['Net'] = self.net
        result['InstanceId'] = self.instance_id
        result['RegistedAs'] = self.registed_as
        result['Desc'] = self.desc
        result['Declared'] = self.declared
        result['Mode'] = self.mode
        return result

    def from_map(self, map={}):
        self.user_id = map.get('UserId')
        self.net = map.get('Net')
        self.instance_id = map.get('InstanceId')
        self.registed_as = map.get('RegistedAs')
        self.desc = map.get('Desc')
        self.declared = map.get('Declared')
        self.mode = map.get('Mode')
        return self


class SetInstanceModeOnDemandRequest(TeaModel):
    def __init__(self, instance_id_list=None, mode=None, region_id=None):
        self.instance_id_list = instance_id_list  # type: List[str]
        self.mode = mode                # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id_list, 'instance_id_list')
        self.validate_required(self.mode, 'mode')

    def to_map(self):
        result = {}
        result['InstanceIdList'] = self.instance_id_list
        result['Mode'] = self.mode
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id_list = map.get('InstanceIdList')
        self.mode = map.get('Mode')
        self.region_id = map.get('RegionId')
        return self


class SetInstanceModeOnDemandResponse(TeaModel):
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


class QuerySchedruleOnDemandRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.region_id = map.get('RegionId')
        return self


class QuerySchedruleOnDemandResponse(TeaModel):
    def __init__(self, request_id=None, user_id=None, instance_id=None, rule_config=None, rule_status=None):
        self.request_id = request_id    # type: str
        self.user_id = user_id          # type: str
        self.instance_id = instance_id  # type: str
        self.rule_config = rule_config  # type: List[QuerySchedruleOnDemandResponseRuleConfig]
        self.rule_status = rule_status  # type: List[QuerySchedruleOnDemandResponseRuleStatus]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.rule_config, 'rule_config')
        if self.rule_config:
            for k in self.rule_config:
                if k:
                    k.validate()
        self.validate_required(self.rule_status, 'rule_status')
        if self.rule_status:
            for k in self.rule_status:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['UserId'] = self.user_id
        result['InstanceId'] = self.instance_id
        result['RuleConfig'] = []
        if self.rule_config is not None:
            for k in self.rule_config:
                result['RuleConfig'].append(k.to_map() if k else None)
        else:
            result['RuleConfig'] = None
        result['RuleStatus'] = []
        if self.rule_status is not None:
            for k in self.rule_status:
                result['RuleStatus'].append(k.to_map() if k else None)
        else:
            result['RuleStatus'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.user_id = map.get('UserId')
        self.instance_id = map.get('InstanceId')
        self.rule_config = []
        if map.get('RuleConfig') is not None:
            for k in map.get('RuleConfig'):
                temp_model = QuerySchedruleOnDemandResponseRuleConfig()
                self.rule_config.append(temp_model.from_map(k))
        else:
            self.rule_config = None
        self.rule_status = []
        if map.get('RuleStatus') is not None:
            for k in map.get('RuleStatus'):
                temp_model = QuerySchedruleOnDemandResponseRuleStatus()
                self.rule_status.append(temp_model.from_map(k))
        else:
            self.rule_status = None
        return self


class QuerySchedruleOnDemandResponseRuleConfig(TeaModel):
    def __init__(self, rule_name=None, rule_condition_cnt=None, rule_undo_begin_time=None, rule_undo_mode=None,
                 rule_undo_end_time=None, rule_condition_mbps=None, rule_condition_kpps=None, rule_switch=None, rule_action=None,
                 time_zone=None):
        self.rule_name = rule_name      # type: str
        self.rule_condition_cnt = rule_condition_cnt  # type: str
        self.rule_undo_begin_time = rule_undo_begin_time  # type: str
        self.rule_undo_mode = rule_undo_mode  # type: str
        self.rule_undo_end_time = rule_undo_end_time  # type: str
        self.rule_condition_mbps = rule_condition_mbps  # type: str
        self.rule_condition_kpps = rule_condition_kpps  # type: str
        self.rule_switch = rule_switch  # type: str
        self.rule_action = rule_action  # type: str
        self.time_zone = time_zone      # type: str

    def validate(self):
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.rule_condition_cnt, 'rule_condition_cnt')
        self.validate_required(self.rule_undo_begin_time, 'rule_undo_begin_time')
        self.validate_required(self.rule_undo_mode, 'rule_undo_mode')
        self.validate_required(self.rule_undo_end_time, 'rule_undo_end_time')
        self.validate_required(self.rule_condition_mbps, 'rule_condition_mbps')
        self.validate_required(self.rule_condition_kpps, 'rule_condition_kpps')
        self.validate_required(self.rule_switch, 'rule_switch')
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.time_zone, 'time_zone')

    def to_map(self):
        result = {}
        result['RuleName'] = self.rule_name
        result['RuleConditionCnt'] = self.rule_condition_cnt
        result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        result['RuleUndoMode'] = self.rule_undo_mode
        result['RuleUndoEndTime'] = self.rule_undo_end_time
        result['RuleConditionMbps'] = self.rule_condition_mbps
        result['RuleConditionKpps'] = self.rule_condition_kpps
        result['RuleSwitch'] = self.rule_switch
        result['RuleAction'] = self.rule_action
        result['TimeZone'] = self.time_zone
        return result

    def from_map(self, map={}):
        self.rule_name = map.get('RuleName')
        self.rule_condition_cnt = map.get('RuleConditionCnt')
        self.rule_undo_begin_time = map.get('RuleUndoBeginTime')
        self.rule_undo_mode = map.get('RuleUndoMode')
        self.rule_undo_end_time = map.get('RuleUndoEndTime')
        self.rule_condition_mbps = map.get('RuleConditionMbps')
        self.rule_condition_kpps = map.get('RuleConditionKpps')
        self.rule_switch = map.get('RuleSwitch')
        self.rule_action = map.get('RuleAction')
        self.time_zone = map.get('TimeZone')
        return self


class QuerySchedruleOnDemandResponseRuleStatus(TeaModel):
    def __init__(self, net=None, rule_sched_status=None):
        self.net = net                  # type: str
        self.rule_sched_status = rule_sched_status  # type: str

    def validate(self):
        self.validate_required(self.net, 'net')
        self.validate_required(self.rule_sched_status, 'rule_sched_status')

    def to_map(self):
        result = {}
        result['Net'] = self.net
        result['RuleSchedStatus'] = self.rule_sched_status
        return result

    def from_map(self, map={}):
        self.net = map.get('Net')
        self.rule_sched_status = map.get('RuleSchedStatus')
        return self


class DeleteSchedruleOnDemandRequest(TeaModel):
    def __init__(self, instance_id=None, rule_name=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.rule_name = rule_name      # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.rule_name, 'rule_name')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['RuleName'] = self.rule_name
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.rule_name = map.get('RuleName')
        self.region_id = map.get('RegionId')
        return self


class DeleteSchedruleOnDemandResponse(TeaModel):
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


class ConfigSchedruleOnDemandRequest(TeaModel):
    def __init__(self, instance_id=None, rule_name=None, rule_condition_mbps=None, rule_condition_kpps=None,
                 rule_condition_cnt=None, rule_action=None, rule_switch=None, rule_undo_mode=None, rule_undo_begin_time=None,
                 rule_undo_end_time=None, time_zone=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.rule_name = rule_name      # type: str
        self.rule_condition_mbps = rule_condition_mbps  # type: str
        self.rule_condition_kpps = rule_condition_kpps  # type: str
        self.rule_condition_cnt = rule_condition_cnt  # type: str
        self.rule_action = rule_action  # type: str
        self.rule_switch = rule_switch  # type: str
        self.rule_undo_mode = rule_undo_mode  # type: str
        self.rule_undo_begin_time = rule_undo_begin_time  # type: str
        self.rule_undo_end_time = rule_undo_end_time  # type: str
        self.time_zone = time_zone      # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.rule_condition_mbps, 'rule_condition_mbps')
        self.validate_required(self.rule_condition_kpps, 'rule_condition_kpps')
        self.validate_required(self.rule_condition_cnt, 'rule_condition_cnt')
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.rule_switch, 'rule_switch')
        self.validate_required(self.rule_undo_mode, 'rule_undo_mode')
        self.validate_required(self.rule_undo_begin_time, 'rule_undo_begin_time')
        self.validate_required(self.time_zone, 'time_zone')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['RuleName'] = self.rule_name
        result['RuleConditionMbps'] = self.rule_condition_mbps
        result['RuleConditionKpps'] = self.rule_condition_kpps
        result['RuleConditionCnt'] = self.rule_condition_cnt
        result['RuleAction'] = self.rule_action
        result['RuleSwitch'] = self.rule_switch
        result['RuleUndoMode'] = self.rule_undo_mode
        result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        result['RuleUndoEndTime'] = self.rule_undo_end_time
        result['TimeZone'] = self.time_zone
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.rule_name = map.get('RuleName')
        self.rule_condition_mbps = map.get('RuleConditionMbps')
        self.rule_condition_kpps = map.get('RuleConditionKpps')
        self.rule_condition_cnt = map.get('RuleConditionCnt')
        self.rule_action = map.get('RuleAction')
        self.rule_switch = map.get('RuleSwitch')
        self.rule_undo_mode = map.get('RuleUndoMode')
        self.rule_undo_begin_time = map.get('RuleUndoBeginTime')
        self.rule_undo_end_time = map.get('RuleUndoEndTime')
        self.time_zone = map.get('TimeZone')
        self.region_id = map.get('RegionId')
        return self


class ConfigSchedruleOnDemandResponse(TeaModel):
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


class CreateSchedruleOnDemandRequest(TeaModel):
    def __init__(self, instance_id=None, rule_name=None, rule_condition_mbps=None, rule_condition_kpps=None,
                 rule_condition_cnt=None, rule_action=None, rule_switch=None, rule_undo_mode=None, rule_undo_begin_time=None,
                 rule_undo_end_time=None, time_zone=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.rule_name = rule_name      # type: str
        self.rule_condition_mbps = rule_condition_mbps  # type: str
        self.rule_condition_kpps = rule_condition_kpps  # type: str
        self.rule_condition_cnt = rule_condition_cnt  # type: str
        self.rule_action = rule_action  # type: str
        self.rule_switch = rule_switch  # type: str
        self.rule_undo_mode = rule_undo_mode  # type: str
        self.rule_undo_begin_time = rule_undo_begin_time  # type: str
        self.rule_undo_end_time = rule_undo_end_time  # type: str
        self.time_zone = time_zone      # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.rule_condition_mbps, 'rule_condition_mbps')
        self.validate_required(self.rule_condition_kpps, 'rule_condition_kpps')
        self.validate_required(self.rule_condition_cnt, 'rule_condition_cnt')
        self.validate_required(self.rule_action, 'rule_action')
        self.validate_required(self.rule_switch, 'rule_switch')
        self.validate_required(self.rule_undo_mode, 'rule_undo_mode')
        self.validate_required(self.rule_undo_begin_time, 'rule_undo_begin_time')
        self.validate_required(self.time_zone, 'time_zone')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['RuleName'] = self.rule_name
        result['RuleConditionMbps'] = self.rule_condition_mbps
        result['RuleConditionKpps'] = self.rule_condition_kpps
        result['RuleConditionCnt'] = self.rule_condition_cnt
        result['RuleAction'] = self.rule_action
        result['RuleSwitch'] = self.rule_switch
        result['RuleUndoMode'] = self.rule_undo_mode
        result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        result['RuleUndoEndTime'] = self.rule_undo_end_time
        result['TimeZone'] = self.time_zone
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.rule_name = map.get('RuleName')
        self.rule_condition_mbps = map.get('RuleConditionMbps')
        self.rule_condition_kpps = map.get('RuleConditionKpps')
        self.rule_condition_cnt = map.get('RuleConditionCnt')
        self.rule_action = map.get('RuleAction')
        self.rule_switch = map.get('RuleSwitch')
        self.rule_undo_mode = map.get('RuleUndoMode')
        self.rule_undo_begin_time = map.get('RuleUndoBeginTime')
        self.rule_undo_end_time = map.get('RuleUndoEndTime')
        self.time_zone = map.get('TimeZone')
        self.region_id = map.get('RegionId')
        return self


class CreateSchedruleOnDemandResponse(TeaModel):
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


class DescribeOnDemandDdosEventRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, page_size=None, page_no=None, instance_id=None, ip=None,
                 resource_group_id=None, region_id=None):
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.page_size = page_size      # type: int
        self.page_no = page_no          # type: int
        self.instance_id = instance_id  # type: str
        self.ip = ip                    # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNo'] = self.page_no
        result['InstanceId'] = self.instance_id
        result['Ip'] = self.ip
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_no = map.get('PageNo')
        self.instance_id = map.get('InstanceId')
        self.ip = map.get('Ip')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class DescribeOnDemandDdosEventResponse(TeaModel):
    def __init__(self, request_id=None, total=None, events=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.events = events            # type: List[DescribeOnDemandDdosEventResponseEvents]

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
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        else:
            result['Events'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        self.events = []
        if map.get('Events') is not None:
            for k in map.get('Events'):
                temp_model = DescribeOnDemandDdosEventResponseEvents()
                self.events.append(temp_model.from_map(k))
        else:
            self.events = None
        return self


class DescribeOnDemandDdosEventResponseEvents(TeaModel):
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
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Pps'] = self.pps
        result['Ip'] = self.ip
        result['Mbps'] = self.mbps
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.pps = map.get('Pps')
        self.ip = map.get('Ip')
        self.mbps = map.get('Mbps')
        self.status = map.get('Status')
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, region_id=None, resource_type=None, page_size=None, current_page=None,
                 resource_group_id=None):
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ResourceType'] = self.resource_type
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.resource_type = map.get('ResourceType')
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, request_id=None, current_page=None, page_size=None, total_count=None, tag_keys=None):
        self.request_id = request_id    # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.tag_keys = tag_keys        # type: List[ListTagKeysResponseTagKeys]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.tag_keys, 'tag_keys')
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        else:
            result['TagKeys'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.tag_keys = []
        if map.get('TagKeys') is not None:
            for k in map.get('TagKeys'):
                temp_model = ListTagKeysResponseTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        else:
            self.tag_keys = None
        return self


class ListTagKeysResponseTagKeys(TeaModel):
    def __init__(self, tag_key=None, tag_count=None):
        self.tag_key = tag_key          # type: str
        self.tag_count = tag_count      # type: int

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_count, 'tag_count')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagCount'] = self.tag_count
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_count = map.get('TagCount')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, resource_group_id=None, region_id=None, resource_type=None, resource_id=None, tag=None,
                 next_token=None):
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag = tag                  # type: List[ListTagResourcesRequestTag]
        self.next_token = next_token    # type: str

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        result['NextToken'] = self.next_token
        return result

    def from_map(self, map={}):
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        self.next_token = map.get('NextToken')
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, next_token=None, tag_resources=None):
        self.request_id = request_id    # type: str
        self.next_token = next_token    # type: str
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseTagResources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextToken'] = self.next_token
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        else:
            result['TagResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_token = map.get('NextToken')
        if map.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseTagResources()
            self.tag_resources = temp_model.from_map(map['TagResources'])
        else:
            self.tag_resources = None
        return self


class ListTagResourcesResponseTagResourcesTagResource(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag_key=None, tag_value=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: str
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = {}
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        return result

    def from_map(self, map={}):
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        self.tag_resource = tag_resource  # type: List[ListTagResourcesResponseTagResourcesTagResource]

    def validate(self):
        self.validate_required(self.tag_resource, 'tag_resource')
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        else:
            result['TagResource'] = None
        return result

    def from_map(self, map={}):
        self.tag_resource = []
        if map.get('TagResource') is not None:
            for k in map.get('TagResource'):
                temp_model = ListTagResourcesResponseTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        else:
            self.tag_resource = None
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, resource_group_id=None, region_id=None, resource_type=None, resource_id=None, tag_key=None,
                 all=None):
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag_key = tag_key          # type: List[str]
        self.all = all                  # type: bool

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['TagKey'] = self.tag_key
        result['All'] = self.all
        return result

    def from_map(self, map={}):
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag_key = map.get('TagKey')
        self.all = map.get('All')
        return self


class UntagResourcesResponse(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(self, resource_group_id=None, region_id=None, resource_type=None, resource_id=None, tag=None):
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: List[str]
        self.tag = tag                  # type: List[TagResourcesRequestTag]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        result['ResourceType'] = self.resource_type
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        self.resource_type = map.get('ResourceType')
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class TagResourcesResponse(TeaModel):
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


class DescribeExcpetionCountRequest(TeaModel):
    def __init__(self, resource_group_id=None, region_id=None):
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class DescribeExcpetionCountResponse(TeaModel):
    def __init__(self, request_id=None, exception_ip_count=None, expire_time_count=None):
        self.request_id = request_id    # type: str
        self.exception_ip_count = exception_ip_count  # type: int
        self.expire_time_count = expire_time_count  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.exception_ip_count, 'exception_ip_count')
        self.validate_required(self.expire_time_count, 'expire_time_count')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ExceptionIpCount'] = self.exception_ip_count
        result['ExpireTimeCount'] = self.expire_time_count
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.exception_ip_count = map.get('ExceptionIpCount')
        self.expire_time_count = map.get('ExpireTimeCount')
        return self


class DescribePackIpListRequest(TeaModel):
    def __init__(self, page_no=None, page_size=None, instance_id=None, ip=None, product_name=None,
                 resource_group_id=None, region_id=None):
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.instance_id = instance_id  # type: str
        self.ip = ip                    # type: str
        self.product_name = product_name  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['InstanceId'] = self.instance_id
        result['Ip'] = self.ip
        result['ProductName'] = self.product_name
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.instance_id = map.get('InstanceId')
        self.ip = map.get('Ip')
        self.product_name = map.get('ProductName')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class DescribePackIpListResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, total=None, ip_list=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.total = total              # type: int
        self.ip_list = ip_list          # type: List[DescribePackIpListResponseIpList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.total, 'total')
        self.validate_required(self.ip_list, 'ip_list')
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Total'] = self.total
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        else:
            result['IpList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.total = map.get('Total')
        self.ip_list = []
        if map.get('IpList') is not None:
            for k in map.get('IpList'):
                temp_model = DescribePackIpListResponseIpList()
                self.ip_list.append(temp_model.from_map(k))
        else:
            self.ip_list = None
        return self


class DescribePackIpListResponseIpList(TeaModel):
    def __init__(self, ip=None, product=None, status=None, remark=None):
        self.ip = ip                    # type: str
        self.product = product          # type: str
        self.status = status            # type: str
        self.remark = remark            # type: str

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.product, 'product')
        self.validate_required(self.status, 'status')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = {}
        result['Ip'] = self.ip
        result['Product'] = self.product
        result['Status'] = self.status
        result['Remark'] = self.remark
        return result

    def from_map(self, map={}):
        self.ip = map.get('Ip')
        self.product = map.get('Product')
        self.status = map.get('Status')
        self.remark = map.get('Remark')
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, resource_group_id=None, region_id=None):
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, regions=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.regions = regions          # type: List[DescribeRegionsResponseRegions]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.regions, 'regions')
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        else:
            result['Regions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.regions = []
        if map.get('Regions') is not None:
            for k in map.get('Regions'):
                temp_model = DescribeRegionsResponseRegions()
                self.regions.append(temp_model.from_map(k))
        else:
            self.regions = None
        return self


class DescribeRegionsResponseRegions(TeaModel):
    def __init__(self, region_en_name=None, region_name=None, region_id=None):
        self.region_en_name = region_en_name  # type: str
        self.region_name = region_name  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.region_en_name, 'region_en_name')
        self.validate_required(self.region_name, 'region_name')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = {}
        result['RegionEnName'] = self.region_en_name
        result['RegionName'] = self.region_name
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.region_en_name = map.get('RegionEnName')
        self.region_name = map.get('RegionName')
        self.region_id = map.get('RegionId')
        return self


class ModifyRemarkRequest(TeaModel):
    def __init__(self, instance_id=None, remark=None, resource_group_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.remark = remark            # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Remark'] = self.remark
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.remark = map.get('Remark')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class ModifyRemarkResponse(TeaModel):
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


class DescribeTrafficRequest(TeaModel):
    def __init__(self, instance_id=None, ipnet=None, ip=None, start_time=None, end_time=None, interval=None,
                 resource_group_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.ipnet = ipnet              # type: str
        self.ip = ip                    # type: str
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.interval = interval        # type: int
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Ipnet'] = self.ipnet
        result['Ip'] = self.ip
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Interval'] = self.interval
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.ipnet = map.get('Ipnet')
        self.ip = map.get('Ip')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.interval = map.get('Interval')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
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
        result['RequestId'] = self.request_id
        result['FlowList'] = []
        if self.flow_list is not None:
            for k in self.flow_list:
                result['FlowList'].append(k.to_map() if k else None)
        else:
            result['FlowList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.flow_list = []
        if map.get('FlowList') is not None:
            for k in map.get('FlowList'):
                temp_model = DescribeTrafficResponseFlowList()
                self.flow_list.append(temp_model.from_map(k))
        else:
            self.flow_list = None
        return self


class DescribeTrafficResponseFlowList(TeaModel):
    def __init__(self, pps=None, flow_type=None, kbps=None, name=None, attack_bps=None, attack_pps=None, time=None):
        self.pps = pps                  # type: int
        self.flow_type = flow_type      # type: str
        self.kbps = kbps                # type: int
        self.name = name                # type: str
        self.attack_bps = attack_bps    # type: int
        self.attack_pps = attack_pps    # type: int
        self.time = time                # type: int

    def validate(self):
        self.validate_required(self.pps, 'pps')
        self.validate_required(self.flow_type, 'flow_type')
        self.validate_required(self.kbps, 'kbps')
        self.validate_required(self.name, 'name')
        self.validate_required(self.attack_bps, 'attack_bps')
        self.validate_required(self.attack_pps, 'attack_pps')
        self.validate_required(self.time, 'time')

    def to_map(self):
        result = {}
        result['Pps'] = self.pps
        result['FlowType'] = self.flow_type
        result['Kbps'] = self.kbps
        result['Name'] = self.name
        result['AttackBps'] = self.attack_bps
        result['AttackPps'] = self.attack_pps
        result['Time'] = self.time
        return result

    def from_map(self, map={}):
        self.pps = map.get('Pps')
        self.flow_type = map.get('FlowType')
        self.kbps = map.get('Kbps')
        self.name = map.get('Name')
        self.attack_bps = map.get('AttackBps')
        self.attack_pps = map.get('AttackPps')
        self.time = map.get('Time')
        return self


class DescribeResourcePackUsageRequest(TeaModel):
    def __init__(self, source_ip=None, end_time=None, start_time=None, instance_id=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.end_time = end_time        # type: int
        self.start_time = start_time    # type: int
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['EndTime'] = self.end_time
        result['StartTime'] = self.start_time
        result['InstanceId'] = self.instance_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.end_time = map.get('EndTime')
        self.start_time = map.get('StartTime')
        self.instance_id = map.get('InstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
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
        result['RequestId'] = self.request_id
        result['Interval'] = self.interval
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PackUsages'] = []
        if self.pack_usages is not None:
            for k in self.pack_usages:
                result['PackUsages'].append(k.to_map() if k else None)
        else:
            result['PackUsages'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.interval = map.get('Interval')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.pack_usages = []
        if map.get('PackUsages') is not None:
            for k in map.get('PackUsages'):
                temp_model = DescribeResourcePackUsageResponsePackUsages()
                self.pack_usages.append(temp_model.from_map(k))
        else:
            self.pack_usages = None
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
        result['Traffic'] = self.traffic
        result['Time'] = self.time
        return result

    def from_map(self, map={}):
        self.traffic = map.get('Traffic')
        self.time = map.get('Time')
        return self


class DescribeResourcePackStatisticsRequest(TeaModel):
    def __init__(self, source_ip=None, ddos_region_id=None, instance_id=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.ddos_region_id = ddos_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['DdosRegionId'] = self.ddos_region_id
        result['InstanceId'] = self.instance_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.ddos_region_id = map.get('DdosRegionId')
        self.instance_id = map.get('InstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
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
        result['RequestId'] = self.request_id
        result['AvailablePackNum'] = self.available_pack_num
        result['TotalCurrCapacity'] = self.total_curr_capacity
        result['TotalUsedCapacity'] = self.total_used_capacity
        result['TotalInitCapacity'] = self.total_init_capacity
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.available_pack_num = map.get('AvailablePackNum')
        self.total_curr_capacity = map.get('TotalCurrCapacity')
        self.total_used_capacity = map.get('TotalUsedCapacity')
        self.total_init_capacity = map.get('TotalInitCapacity')
        return self


class DescribeResourcePackInstancesRequest(TeaModel):
    def __init__(self, source_ip=None, page_size=None, current_page=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.resource_group_id = map.get('ResourceGroupId')
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
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['ResourcePacks'] = []
        if self.resource_packs is not None:
            for k in self.resource_packs:
                result['ResourcePacks'].append(k.to_map() if k else None)
        else:
            result['ResourcePacks'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.resource_packs = []
        if map.get('ResourcePacks') is not None:
            for k in map.get('ResourcePacks'):
                temp_model = DescribeResourcePackInstancesResponseResourcePacks()
                self.resource_packs.append(temp_model.from_map(k))
        else:
            self.resource_packs = None
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
        result['ResourcePackId'] = self.resource_pack_id
        result['InitCapacity'] = self.init_capacity
        result['CurrCapacity'] = self.curr_capacity
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.resource_pack_id = map.get('ResourcePackId')
        self.init_capacity = map.get('InitCapacity')
        self.curr_capacity = map.get('CurrCapacity')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.status = map.get('Status')
        return self


class DescribePackPaidTrafficRequest(TeaModel):
    def __init__(self, source_ip=None, instance_id=None, current_page=None, page_size=None, start_time=None,
                 end_time=None, resource_group_id=None):
        self.source_ip = source_ip      # type: str
        self.instance_id = instance_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['SourceIp'] = self.source_ip
        result['InstanceId'] = self.instance_id
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.source_ip = map.get('SourceIp')
        self.instance_id = map.get('InstanceId')
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.resource_group_id = map.get('ResourceGroupId')
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
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PackPaidTraffics'] = []
        if self.pack_paid_traffics is not None:
            for k in self.pack_paid_traffics:
                result['PackPaidTraffics'].append(k.to_map() if k else None)
        else:
            result['PackPaidTraffics'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.pack_paid_traffics = []
        if map.get('PackPaidTraffics') is not None:
            for k in map.get('PackPaidTraffics'):
                temp_model = DescribePackPaidTrafficResponsePackPaidTraffics()
                self.pack_paid_traffics.append(temp_model.from_map(k))
        else:
            self.pack_paid_traffics = None
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
        result['InstanceId'] = self.instance_id
        result['StartTime'] = self.start_time
        result['BaseBandwidth'] = self.base_bandwidth
        result['ElasticBandwidth'] = self.elastic_bandwidth
        result['PaidCapacity'] = self.paid_capacity
        result['TotalCapacity'] = self.total_capacity
        result['MaxAttack'] = self.max_attack
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.start_time = map.get('StartTime')
        self.base_bandwidth = map.get('BaseBandwidth')
        self.elastic_bandwidth = map.get('ElasticBandwidth')
        self.paid_capacity = map.get('PaidCapacity')
        self.total_capacity = map.get('TotalCapacity')
        self.max_attack = map.get('MaxAttack')
        return self


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, start_time=None, end_time=None, order_by=None,
                 order_dir=None, instance_id=None, resource_group_id=None, region_id=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.order_by = order_by        # type: str
        self.order_dir = order_dir      # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['OrderBy'] = self.order_by
        result['OrderDir'] = self.order_dir
        result['InstanceId'] = self.instance_id
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.order_by = map.get('OrderBy')
        self.order_dir = map.get('OrderDir')
        self.instance_id = map.get('InstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
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
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        else:
            result['OpEntities'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.op_entities = []
        if map.get('OpEntities') is not None:
            for k in map.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        else:
            self.op_entities = None
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
        result['EntityObject'] = self.entity_object
        result['EntityType'] = self.entity_type
        result['OpDesc'] = self.op_desc
        result['OpAccount'] = self.op_account
        result['OpAction'] = self.op_action
        result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, map={}):
        self.entity_object = map.get('EntityObject')
        self.entity_type = map.get('EntityType')
        self.op_desc = map.get('OpDesc')
        self.op_account = map.get('OpAccount')
        self.op_action = map.get('OpAction')
        self.gmt_create = map.get('GmtCreate')
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(self, instance_id_list=None, region_id=None, resource_group_id=None):
        self.instance_id_list = instance_id_list  # type: str
        self.region_id = region_id      # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.instance_id_list, 'instance_id_list')

    def to_map(self):
        result = {}
        result['InstanceIdList'] = self.instance_id_list
        result['RegionId'] = self.region_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.instance_id_list = map.get('InstanceIdList')
        self.region_id = map.get('RegionId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(self, request_id=None, instance_specs=None):
        self.request_id = request_id    # type: str
        self.instance_specs = instance_specs  # type: List[DescribeInstanceSpecsResponseInstanceSpecs]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_specs, 'instance_specs')
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        else:
            result['InstanceSpecs'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.instance_specs = []
        if map.get('InstanceSpecs') is not None:
            for k in map.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        else:
            self.instance_specs = None
        return self


class DescribeInstanceSpecsResponseInstanceSpecsPackConfig(TeaModel):
    def __init__(self, pack_adv_thre=None, ip_advance_thre=None, ip_basic_thre=None, pack_basic_thre=None,
                 ip_spec=None, bind_ip_count=None):
        self.pack_adv_thre = pack_adv_thre  # type: int
        self.ip_advance_thre = ip_advance_thre  # type: int
        self.ip_basic_thre = ip_basic_thre  # type: int
        self.pack_basic_thre = pack_basic_thre  # type: int
        self.ip_spec = ip_spec          # type: int
        self.bind_ip_count = bind_ip_count  # type: int

    def validate(self):
        self.validate_required(self.pack_adv_thre, 'pack_adv_thre')
        self.validate_required(self.ip_advance_thre, 'ip_advance_thre')
        self.validate_required(self.ip_basic_thre, 'ip_basic_thre')
        self.validate_required(self.pack_basic_thre, 'pack_basic_thre')
        self.validate_required(self.ip_spec, 'ip_spec')
        self.validate_required(self.bind_ip_count, 'bind_ip_count')

    def to_map(self):
        result = {}
        result['PackAdvThre'] = self.pack_adv_thre
        result['IpAdvanceThre'] = self.ip_advance_thre
        result['IpBasicThre'] = self.ip_basic_thre
        result['PackBasicThre'] = self.pack_basic_thre
        result['IpSpec'] = self.ip_spec
        result['BindIpCount'] = self.bind_ip_count
        return result

    def from_map(self, map={}):
        self.pack_adv_thre = map.get('PackAdvThre')
        self.ip_advance_thre = map.get('IpAdvanceThre')
        self.ip_basic_thre = map.get('IpBasicThre')
        self.pack_basic_thre = map.get('PackBasicThre')
        self.ip_spec = map.get('IpSpec')
        self.bind_ip_count = map.get('BindIpCount')
        return self


class DescribeInstanceSpecsResponseInstanceSpecs(TeaModel):
    def __init__(self, region=None, available_delete_blackhole_count=None, instance_id=None, pack_config=None):
        self.region = region            # type: str
        self.available_delete_blackhole_count = available_delete_blackhole_count  # type: str
        self.instance_id = instance_id  # type: str
        self.pack_config = pack_config  # type: DescribeInstanceSpecsResponseInstanceSpecsPackConfig

    def validate(self):
        self.validate_required(self.region, 'region')
        self.validate_required(self.available_delete_blackhole_count, 'available_delete_blackhole_count')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.pack_config, 'pack_config')
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        result = {}
        result['Region'] = self.region
        result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count
        result['InstanceId'] = self.instance_id
        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()
        else:
            result['PackConfig'] = None
        return result

    def from_map(self, map={}):
        self.region = map.get('Region')
        self.available_delete_blackhole_count = map.get('AvailableDeleteBlackholeCount')
        self.instance_id = map.get('InstanceId')
        if map.get('PackConfig') is not None:
            temp_model = DescribeInstanceSpecsResponseInstanceSpecsPackConfig()
            self.pack_config = temp_model.from_map(map['PackConfig'])
        else:
            self.pack_config = None
        return self


class DescribeInstanceListRequest(TeaModel):
    def __init__(self, resource_group_id=None, instance_id_list=None, remark=None, page_no=None, page_size=None,
                 ip_version=None, instance_type=None, ip=None, orderby=None, orderdire=None, region_id=None, tag=None):
        self.resource_group_id = resource_group_id  # type: str
        self.instance_id_list = instance_id_list  # type: str
        self.remark = remark            # type: str
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int
        self.ip_version = ip_version    # type: str
        self.instance_type = instance_type  # type: str
        self.ip = ip                    # type: str
        self.orderby = orderby          # type: str
        self.orderdire = orderdire      # type: str
        self.region_id = region_id      # type: str
        self.tag = tag                  # type: List[DescribeInstanceListRequestTag]

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceGroupId'] = self.resource_group_id
        result['InstanceIdList'] = self.instance_id_list
        result['Remark'] = self.remark
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        result['IpVersion'] = self.ip_version
        result['InstanceType'] = self.instance_type
        result['Ip'] = self.ip
        result['Orderby'] = self.orderby
        result['Orderdire'] = self.orderdire
        result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.resource_group_id = map.get('ResourceGroupId')
        self.instance_id_list = map.get('InstanceIdList')
        self.remark = map.get('Remark')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        self.ip_version = map.get('IpVersion')
        self.instance_type = map.get('InstanceType')
        self.ip = map.get('Ip')
        self.orderby = map.get('Orderby')
        self.orderdire = map.get('Orderdire')
        self.region_id = map.get('RegionId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeInstanceListRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
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
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        else:
            result['InstanceList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        self.instance_list = []
        if map.get('InstanceList') is not None:
            for k in map.get('InstanceList'):
                temp_model = DescribeInstanceListResponseInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        else:
            self.instance_list = None
        return self


class DescribeInstanceListResponseInstanceList(TeaModel):
    def __init__(self, expire_time=None, instance_id=None, product=None, remark=None, status=None, ip_type=None,
                 auto_renewal=None, blackholding_count=None, gmt_create=None, instance_type=None):
        self.expire_time = expire_time  # type: int
        self.instance_id = instance_id  # type: str
        self.product = product          # type: str
        self.remark = remark            # type: str
        self.status = status            # type: str
        self.ip_type = ip_type          # type: str
        self.auto_renewal = auto_renewal  # type: bool
        self.blackholding_count = blackholding_count  # type: str
        self.gmt_create = gmt_create    # type: int
        self.instance_type = instance_type  # type: str

    def validate(self):
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.product, 'product')
        self.validate_required(self.remark, 'remark')
        self.validate_required(self.status, 'status')
        self.validate_required(self.ip_type, 'ip_type')
        self.validate_required(self.auto_renewal, 'auto_renewal')
        self.validate_required(self.blackholding_count, 'blackholding_count')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.instance_type, 'instance_type')

    def to_map(self):
        result = {}
        result['ExpireTime'] = self.expire_time
        result['InstanceId'] = self.instance_id
        result['Product'] = self.product
        result['Remark'] = self.remark
        result['Status'] = self.status
        result['IpType'] = self.ip_type
        result['AutoRenewal'] = self.auto_renewal
        result['BlackholdingCount'] = self.blackholding_count
        result['GmtCreate'] = self.gmt_create
        result['InstanceType'] = self.instance_type
        return result

    def from_map(self, map={}):
        self.expire_time = map.get('ExpireTime')
        self.instance_id = map.get('InstanceId')
        self.product = map.get('Product')
        self.remark = map.get('Remark')
        self.status = map.get('Status')
        self.ip_type = map.get('IpType')
        self.auto_renewal = map.get('AutoRenewal')
        self.blackholding_count = map.get('BlackholdingCount')
        self.gmt_create = map.get('GmtCreate')
        self.instance_type = map.get('InstanceType')
        return self


class DescribeDdosEventRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, page_size=None, page_no=None, instance_id=None, ip=None,
                 resource_group_id=None, region_id=None):
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.page_size = page_size      # type: int
        self.page_no = page_no          # type: int
        self.instance_id = instance_id  # type: str
        self.ip = ip                    # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNo'] = self.page_no
        result['InstanceId'] = self.instance_id
        result['Ip'] = self.ip
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_no = map.get('PageNo')
        self.instance_id = map.get('InstanceId')
        self.ip = map.get('Ip')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
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
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        else:
            result['Events'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        self.events = []
        if map.get('Events') is not None:
            for k in map.get('Events'):
                temp_model = DescribeDdosEventResponseEvents()
                self.events.append(temp_model.from_map(k))
        else:
            self.events = None
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
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Pps'] = self.pps
        result['Ip'] = self.ip
        result['Mbps'] = self.mbps
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.pps = map.get('Pps')
        self.ip = map.get('Ip')
        self.mbps = map.get('Mbps')
        self.status = map.get('Status')
        return self


class DeleteIpRequest(TeaModel):
    def __init__(self, ip_list=None, instance_id=None, resource_group_id=None, region_id=None):
        self.ip_list = ip_list          # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.ip_list, 'ip_list')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['IpList'] = self.ip_list
        result['InstanceId'] = self.instance_id
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.ip_list = map.get('IpList')
        self.instance_id = map.get('InstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class DeleteIpResponse(TeaModel):
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


class DeleteBlackholeRequest(TeaModel):
    def __init__(self, ip=None, instance_id=None, resource_group_id=None, region_id=None):
        self.ip = ip                    # type: str
        self.instance_id = instance_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Ip'] = self.ip
        result['InstanceId'] = self.instance_id
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.ip = map.get('Ip')
        self.instance_id = map.get('InstanceId')
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
        return self


class DeleteBlackholeResponse(TeaModel):
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


class CheckGrantRequest(TeaModel):
    def __init__(self, resource_group_id=None, region_id=None):
        self.resource_group_id = resource_group_id  # type: str
        self.region_id = region_id      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ResourceGroupId'] = self.resource_group_id
        result['RegionId'] = self.region_id
        return result

    def from_map(self, map={}):
        self.resource_group_id = map.get('ResourceGroupId')
        self.region_id = map.get('RegionId')
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
        result['RequestId'] = self.request_id
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.status = map.get('Status')
        return self


class AddIpRequest(TeaModel):
    def __init__(self, ip_list=None, instance_id=None, region_id=None, resource_group_id=None):
        self.ip_list = ip_list          # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id      # type: str
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        self.validate_required(self.ip_list, 'ip_list')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['IpList'] = self.ip_list
        result['InstanceId'] = self.instance_id
        result['RegionId'] = self.region_id
        result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        self.ip_list = map.get('IpList')
        self.instance_id = map.get('InstanceId')
        self.region_id = map.get('RegionId')
        self.resource_group_id = map.get('ResourceGroupId')
        return self


class AddIpResponse(TeaModel):
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
