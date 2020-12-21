# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List


class DescribeOnDemandInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id_list: List[str] = None,
        region_id: str = None,
    ):
        self.instance_id_list = instance_id_list
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.instance_id_list, 'instance_id_list')

    def to_map(self):
        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeOnDemandInstanceStatusResponseInstances(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        net: str = None,
        instance_id: str = None,
        registed_as: str = None,
        desc: str = None,
        declared: str = None,
        mode: str = None,
    ):
        self.user_id = user_id
        self.net = net
        self.instance_id = instance_id
        self.registed_as = registed_as
        self.desc = desc
        self.declared = declared
        self.mode = mode

    def validate(self):
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.net, 'net')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.registed_as, 'registed_as')
        self.validate_required(self.desc, 'desc')
        self.validate_required(self.declared, 'declared')
        self.validate_required(self.mode, 'mode')

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.net is not None:
            result['Net'] = self.net
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.registed_as is not None:
            result['RegistedAs'] = self.registed_as
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.declared is not None:
            result['Declared'] = self.declared
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegistedAs') is not None:
            self.registed_as = m.get('RegistedAs')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Declared') is not None:
            self.declared = m.get('Declared')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class DescribeOnDemandInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instances: List[DescribeOnDemandInstanceStatusResponseInstances] = None,
    ):
        self.request_id = request_id
        self.instances = instances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeOnDemandInstanceStatusResponseInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class SetInstanceModeOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id_list: List[str] = None,
        mode: str = None,
        region_id: str = None,
    ):
        self.instance_id_list = instance_id_list
        self.mode = mode
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.instance_id_list, 'instance_id_list')
        self.validate_required(self.mode, 'mode')

    def to_map(self):
        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetInstanceModeOnDemandResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class QuerySchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QuerySchedruleOnDemandResponseRuleConfig(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
        rule_condition_cnt: str = None,
        rule_undo_begin_time: str = None,
        rule_undo_mode: str = None,
        rule_undo_end_time: str = None,
        rule_condition_mbps: str = None,
        rule_condition_kpps: str = None,
        rule_switch: str = None,
        rule_action: str = None,
        time_zone: str = None,
    ):
        self.rule_name = rule_name
        self.rule_condition_cnt = rule_condition_cnt
        self.rule_undo_begin_time = rule_undo_begin_time
        self.rule_undo_mode = rule_undo_mode
        self.rule_undo_end_time = rule_undo_end_time
        self.rule_condition_mbps = rule_condition_mbps
        self.rule_condition_kpps = rule_condition_kpps
        self.rule_switch = rule_switch
        self.rule_action = rule_action
        self.time_zone = time_zone

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
        result = dict()
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class QuerySchedruleOnDemandResponseRuleStatus(TeaModel):
    def __init__(
        self,
        net: str = None,
        rule_sched_status: str = None,
    ):
        self.net = net
        self.rule_sched_status = rule_sched_status

    def validate(self):
        self.validate_required(self.net, 'net')
        self.validate_required(self.rule_sched_status, 'rule_sched_status')

    def to_map(self):
        result = dict()
        if self.net is not None:
            result['Net'] = self.net
        if self.rule_sched_status is not None:
            result['RuleSchedStatus'] = self.rule_sched_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('RuleSchedStatus') is not None:
            self.rule_sched_status = m.get('RuleSchedStatus')
        return self


class QuerySchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        user_id: str = None,
        instance_id: str = None,
        rule_config: List[QuerySchedruleOnDemandResponseRuleConfig] = None,
        rule_status: List[QuerySchedruleOnDemandResponseRuleStatus] = None,
    ):
        self.request_id = request_id
        self.user_id = user_id
        self.instance_id = instance_id
        self.rule_config = rule_config
        self.rule_status = rule_status

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
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['RuleConfig'] = []
        if self.rule_config is not None:
            for k in self.rule_config:
                result['RuleConfig'].append(k.to_map() if k else None)
        result['RuleStatus'] = []
        if self.rule_status is not None:
            for k in self.rule_status:
                result['RuleStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.rule_config = []
        if m.get('RuleConfig') is not None:
            for k in m.get('RuleConfig'):
                temp_model = QuerySchedruleOnDemandResponseRuleConfig()
                self.rule_config.append(temp_model.from_map(k))
        self.rule_status = []
        if m.get('RuleStatus') is not None:
            for k in m.get('RuleStatus'):
                temp_model = QuerySchedruleOnDemandResponseRuleStatus()
                self.rule_status.append(temp_model.from_map(k))
        return self


class DeleteSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_name: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.rule_name = rule_name
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.rule_name, 'rule_name')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class ConfigSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_name: str = None,
        rule_condition_mbps: str = None,
        rule_condition_kpps: str = None,
        rule_condition_cnt: str = None,
        rule_action: str = None,
        rule_switch: str = None,
        rule_undo_mode: str = None,
        rule_undo_begin_time: str = None,
        rule_undo_end_time: str = None,
        time_zone: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.rule_name = rule_name
        self.rule_condition_mbps = rule_condition_mbps
        self.rule_condition_kpps = rule_condition_kpps
        self.rule_condition_cnt = rule_condition_cnt
        self.rule_action = rule_action
        self.rule_switch = rule_switch
        self.rule_undo_mode = rule_undo_mode
        self.rule_undo_begin_time = rule_undo_begin_time
        self.rule_undo_end_time = rule_undo_end_time
        self.time_zone = time_zone
        self.region_id = region_id

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
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class CreateSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_name: str = None,
        rule_condition_mbps: str = None,
        rule_condition_kpps: str = None,
        rule_condition_cnt: str = None,
        rule_action: str = None,
        rule_switch: str = None,
        rule_undo_mode: str = None,
        rule_undo_begin_time: str = None,
        rule_undo_end_time: str = None,
        time_zone: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.rule_name = rule_name
        self.rule_condition_mbps = rule_condition_mbps
        self.rule_condition_kpps = rule_condition_kpps
        self.rule_condition_cnt = rule_condition_cnt
        self.rule_action = rule_action
        self.rule_switch = rule_switch
        self.rule_undo_mode = rule_undo_mode
        self.rule_undo_begin_time = rule_undo_begin_time
        self.rule_undo_end_time = rule_undo_end_time
        self.time_zone = time_zone
        self.region_id = region_id

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
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DescribeOnDemandDdosEventRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        page_size: int = None,
        page_no: int = None,
        instance_id: str = None,
        ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_no = page_no
        self.instance_id = instance_id
        self.ip = ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeOnDemandDdosEventResponseEvents(TeaModel):
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


class DescribeOnDemandDdosEventResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        events: List[DescribeOnDemandDdosEventResponseEvents] = None,
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
                temp_model = DescribeOnDemandDdosEventResponseEvents()
                self.events.append(temp_model.from_map(k))
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        page_size: int = None,
        current_page: int = None,
        resource_group_id: str = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.page_size = page_size
        self.current_page = current_page
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListTagKeysResponseTagKeys(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_count: int = None,
    ):
        self.tag_key = tag_key
        self.tag_count = tag_count

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_count, 'tag_count')

    def to_map(self):
        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        tag_keys: List[ListTagKeysResponseTagKeys] = None,
    ):
        self.request_id = request_id
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.tag_keys = tag_keys

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
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
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
        resource_group_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
        next_token: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag
        self.next_token = next_token

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTagResourcesResponseTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        self.validate_required(self.tag_resource, 'tag_resource')
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        tag_resources: ListTagResourcesResponseTagResources = None,
    ):
        self.request_id = request_id
        self.next_token = next_token
        self.tag_resources = tag_resources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_token, 'next_token')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
        all: bool = None,
    ):
        self.resource_group_id = resource_group_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key
        self.all = all

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.all is not None:
            result['All'] = self.all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('All') is not None:
            self.all = m.get('All')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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
        resource_group_id: str = None,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.resource_group_id = resource_group_id
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.resource_id, 'resource_id')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DescribeExcpetionCountRequest(TeaModel):
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


class DescribeExcpetionCountResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        exception_ip_count: int = None,
        expire_time_count: int = None,
    ):
        self.request_id = request_id
        self.exception_ip_count = exception_ip_count
        self.expire_time_count = expire_time_count

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.exception_ip_count, 'exception_ip_count')
        self.validate_required(self.expire_time_count, 'expire_time_count')

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.exception_ip_count is not None:
            result['ExceptionIpCount'] = self.exception_ip_count
        if self.expire_time_count is not None:
            result['ExpireTimeCount'] = self.expire_time_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExceptionIpCount') is not None:
            self.exception_ip_count = m.get('ExceptionIpCount')
        if m.get('ExpireTimeCount') is not None:
            self.expire_time_count = m.get('ExpireTimeCount')
        return self


class DescribePackIpListRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        instance_id: str = None,
        ip: str = None,
        product_name: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.instance_id = instance_id
        self.ip = ip
        self.product_name = product_name
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribePackIpListResponseIpList(TeaModel):
    def __init__(
        self,
        ip: str = None,
        product: str = None,
        status: str = None,
        remark: str = None,
    ):
        self.ip = ip
        self.product = product
        self.status = status
        self.remark = remark

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.product, 'product')
        self.validate_required(self.status, 'status')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.product is not None:
            result['Product'] = self.product
        if self.status is not None:
            result['Status'] = self.status
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DescribePackIpListResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        total: int = None,
        ip_list: List[DescribePackIpListResponseIpList] = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.total = total
        self.ip_list = ip_list

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
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.total is not None:
            result['Total'] = self.total
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = DescribePackIpListResponseIpList()
                self.ip_list.append(temp_model.from_map(k))
        return self


class DescribeRegionsRequest(TeaModel):
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


class DescribeRegionsResponseRegions(TeaModel):
    def __init__(
        self,
        region_en_name: str = None,
        region_name: str = None,
        region_id: str = None,
    ):
        self.region_en_name = region_en_name
        self.region_name = region_name
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.region_en_name, 'region_en_name')
        self.validate_required(self.region_name, 'region_name')
        self.validate_required(self.region_id, 'region_id')

    def to_map(self):
        result = dict()
        if self.region_en_name is not None:
            result['RegionEnName'] = self.region_en_name
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEnName') is not None:
            self.region_en_name = m.get('RegionEnName')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        regions: List[DescribeRegionsResponseRegions] = None,
    ):
        self.request_id = request_id
        self.success = success
        self.code = code
        self.regions = regions

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
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class ModifyRemarkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.remark, 'remark')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyRemarkResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

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


class DescribeTrafficRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ipnet: str = None,
        ip: str = None,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.ipnet = ipnet
        self.ip = ip
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ipnet is not None:
            result['Ipnet'] = self.ipnet
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.interval is not None:
            result['Interval'] = self.interval
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
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTrafficResponseFlowList(TeaModel):
    def __init__(
        self,
        pps: int = None,
        flow_type: str = None,
        kbps: int = None,
        name: str = None,
        attack_bps: int = None,
        attack_pps: int = None,
        time: int = None,
    ):
        self.pps = pps
        self.flow_type = flow_type
        self.kbps = kbps
        self.name = name
        self.attack_bps = attack_bps
        self.attack_pps = attack_pps
        self.time = time

    def validate(self):
        self.validate_required(self.pps, 'pps')
        self.validate_required(self.flow_type, 'flow_type')
        self.validate_required(self.kbps, 'kbps')
        self.validate_required(self.name, 'name')
        self.validate_required(self.attack_bps, 'attack_bps')
        self.validate_required(self.attack_pps, 'attack_pps')
        self.validate_required(self.time, 'time')

    def to_map(self):
        result = dict()
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.kbps is not None:
            result['Kbps'] = self.kbps
        if self.name is not None:
            result['Name'] = self.name
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps
        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps
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
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')
        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')
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


class DescribeResourcePackUsageRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        end_time: int = None,
        start_time: int = None,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.end_time = end_time
        self.start_time = start_time
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        ddos_region_id: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.ddos_region_id = ddos_region_id
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.page_size = page_size
        self.current_page = current_page
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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


class DescribePackPaidTrafficRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        current_page: int = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.current_page = current_page
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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


class DescribeOpEntitiesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
        order_by: str = None,
        order_dir: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time
        self.order_by = order_by
        self.order_dir = order_dir
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_dir is not None:
            result['OrderDir'] = self.order_dir
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderDir') is not None:
            self.order_dir = m.get('OrderDir')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(
        self,
        instance_id_list: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.instance_id_list = instance_id_list
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.instance_id_list, 'instance_id_list')

    def to_map(self):
        result = dict()
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceSpecsResponseInstanceSpecsPackConfig(TeaModel):
    def __init__(
        self,
        pack_adv_thre: int = None,
        ip_advance_thre: int = None,
        ip_basic_thre: int = None,
        pack_basic_thre: int = None,
        ip_spec: int = None,
        bind_ip_count: int = None,
    ):
        self.pack_adv_thre = pack_adv_thre
        self.ip_advance_thre = ip_advance_thre
        self.ip_basic_thre = ip_basic_thre
        self.pack_basic_thre = pack_basic_thre
        self.ip_spec = ip_spec
        self.bind_ip_count = bind_ip_count

    def validate(self):
        self.validate_required(self.pack_adv_thre, 'pack_adv_thre')
        self.validate_required(self.ip_advance_thre, 'ip_advance_thre')
        self.validate_required(self.ip_basic_thre, 'ip_basic_thre')
        self.validate_required(self.pack_basic_thre, 'pack_basic_thre')
        self.validate_required(self.ip_spec, 'ip_spec')
        self.validate_required(self.bind_ip_count, 'bind_ip_count')

    def to_map(self):
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
        if self.bind_ip_count is not None:
            result['BindIpCount'] = self.bind_ip_count
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
        if m.get('BindIpCount') is not None:
            self.bind_ip_count = m.get('BindIpCount')
        return self


class DescribeInstanceSpecsResponseInstanceSpecs(TeaModel):
    def __init__(
        self,
        region: str = None,
        available_delete_blackhole_count: str = None,
        instance_id: str = None,
        pack_config: DescribeInstanceSpecsResponseInstanceSpecsPackConfig = None,
    ):
        self.region = region
        self.available_delete_blackhole_count = available_delete_blackhole_count
        self.instance_id = instance_id
        self.pack_config = pack_config

    def validate(self):
        self.validate_required(self.region, 'region')
        self.validate_required(self.available_delete_blackhole_count, 'available_delete_blackhole_count')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.pack_config, 'pack_config')
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.available_delete_blackhole_count is not None:
            result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = m.get('AvailableDeleteBlackholeCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PackConfig') is not None:
            temp_model = DescribeInstanceSpecsResponseInstanceSpecsPackConfig()
            self.pack_config = temp_model.from_map(m['PackConfig'])
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_specs: List[DescribeInstanceSpecsResponseInstanceSpecs] = None,
    ):
        self.request_id = request_id
        self.instance_specs = instance_specs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_specs, 'instance_specs')
        if self.instance_specs:
            for k in self.instance_specs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['InstanceSpecs'] = []
        if self.instance_specs is not None:
            for k in self.instance_specs:
                result['InstanceSpecs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instance_specs = []
        if m.get('InstanceSpecs') is not None:
            for k in m.get('InstanceSpecs'):
                temp_model = DescribeInstanceSpecsResponseInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        return self


class DescribeInstanceListRequestTag(TeaModel):
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


class DescribeInstanceListRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        instance_id_list: str = None,
        remark: str = None,
        page_no: int = None,
        page_size: int = None,
        ip_version: str = None,
        instance_type: str = None,
        ip: str = None,
        orderby: str = None,
        orderdire: str = None,
        region_id: str = None,
        tag: List[DescribeInstanceListRequestTag] = None,
    ):
        self.resource_group_id = resource_group_id
        self.instance_id_list = instance_id_list
        self.remark = remark
        self.page_no = page_no
        self.page_size = page_size
        self.ip_version = ip_version
        self.instance_type = instance_type
        self.ip = ip
        self.orderby = orderby
        self.orderdire = orderdire
        self.region_id = region_id
        self.tag = tag

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.orderby is not None:
            result['Orderby'] = self.orderby
        if self.orderdire is not None:
            result['Orderdire'] = self.orderdire
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Orderby') is not None:
            self.orderby = m.get('Orderby')
        if m.get('Orderdire') is not None:
            self.orderdire = m.get('Orderdire')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstanceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstanceListResponseInstanceList(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        instance_id: str = None,
        product: str = None,
        remark: str = None,
        status: str = None,
        ip_type: str = None,
        auto_renewal: bool = None,
        blackholding_count: str = None,
        gmt_create: int = None,
        instance_type: str = None,
    ):
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.product = product
        self.remark = remark
        self.status = status
        self.ip_type = ip_type
        self.auto_renewal = auto_renewal
        self.blackholding_count = blackholding_count
        self.gmt_create = gmt_create
        self.instance_type = instance_type

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
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.blackholding_count is not None:
            result['BlackholdingCount'] = self.blackholding_count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
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
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('BlackholdingCount') is not None:
            self.blackholding_count = m.get('BlackholdingCount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
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


class DescribeDdosEventRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        page_size: int = None,
        page_no: int = None,
        instance_id: str = None,
        ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_no = page_no
        self.instance_id = instance_id
        self.ip = ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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


class DeleteIpRequest(TeaModel):
    def __init__(
        self,
        ip_list: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.ip_list = ip_list
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.ip_list, 'ip_list')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBlackholeRequest(TeaModel):
    def __init__(
        self,
        ip: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.ip = ip
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
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


class AddIpRequest(TeaModel):
    def __init__(
        self,
        ip_list: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.ip_list = ip_list
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        self.validate_required(self.ip_list, 'ip_list')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = dict()
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
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
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


