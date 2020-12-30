# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddIpRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        ip_list: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.ip_list = ip_list
        self.instance_id = instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AddIpResponseBody(TeaModel):
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


class AddIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddIpResponseBody = None,
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
            temp_model = AddIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckGrantRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckGrantResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        request_id: str = None,
    ):
        self.status = status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckGrantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckGrantResponseBody = None,
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
            temp_model = CheckGrantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
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
        self.source_ip = source_ip
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
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
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


class ConfigSchedruleOnDemandResponseBody(TeaModel):
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


class ConfigSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigSchedruleOnDemandResponseBody = None,
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
            temp_model = ConfigSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
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
        self.source_ip = source_ip
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
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
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


class CreateSchedruleOnDemandResponseBody(TeaModel):
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


class CreateSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSchedruleOnDemandResponseBody = None,
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
            temp_model = CreateSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBlackholeRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        ip: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.ip = ip
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteBlackholeResponseBody(TeaModel):
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


class DeleteBlackholeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBlackholeResponseBody = None,
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
            temp_model = DeleteBlackholeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIpRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        ip_list: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.ip_list = ip_list
        self.instance_id = instance_id
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIpResponseBody(TeaModel):
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


class DeleteIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIpResponseBody = None,
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
            temp_model = DeleteIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        rule_name: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.rule_name = rule_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteSchedruleOnDemandResponseBody(TeaModel):
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


class DeleteSchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSchedruleOnDemandResponseBody = None,
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
            temp_model = DeleteSchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDdosEventRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        start_time: int = None,
        end_time: int = None,
        page_size: int = None,
        page_no: int = None,
        instance_id: str = None,
        ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_no = page_no
        self.instance_id = instance_id
        self.ip = ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
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


class DescribeDdosEventResponseBodyEvents(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        status: str = None,
        start_time: int = None,
        mbps: int = None,
        ip: str = None,
        pps: int = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.mbps = mbps
        self.ip = ip
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeDdosEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        events: List[DescribeDdosEventResponseBodyEvents] = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.events = events
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeDdosEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeDdosEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDdosEventResponseBody = None,
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
            temp_model = DescribeDdosEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExcpetionCountRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeExcpetionCountResponseBody(TeaModel):
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
        pass

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


class DescribeExcpetionCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeExcpetionCountResponseBody = None,
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
            temp_model = DescribeExcpetionCountResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        source_ip: str = None,
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
        self.source_ip = source_ip
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
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
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


class DescribeInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        status: str = None,
        ip_type: str = None,
        auto_renewal: bool = None,
        remark: str = None,
        expire_time: int = None,
        product: str = None,
        gmt_create: int = None,
        instance_id: str = None,
        instance_type: str = None,
        blackholding_count: str = None,
    ):
        self.status = status
        self.ip_type = ip_type
        self.auto_renewal = auto_renewal
        self.remark = remark
        self.expire_time = expire_time
        self.product = product
        self.gmt_create = gmt_create
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.blackholding_count = blackholding_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.product is not None:
            result['Product'] = self.product
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.blackholding_count is not None:
            result['BlackholdingCount'] = self.blackholding_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('BlackholdingCount') is not None:
            self.blackholding_count = m.get('BlackholdingCount')
        return self


class DescribeInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        instance_list: List[DescribeInstanceListResponseBodyInstanceList] = None,
    ):
        self.request_id = request_id
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
                temp_model = DescribeInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class DescribeInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceListResponseBody = None,
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
            temp_model = DescribeInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id_list: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id_list = instance_id_list
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig(TeaModel):
    def __init__(
        self,
        pack_basic_thre: int = None,
        bind_ip_count: int = None,
        pack_adv_thre: int = None,
        ip_basic_thre: int = None,
        ip_advance_thre: int = None,
        ip_spec: int = None,
    ):
        self.pack_basic_thre = pack_basic_thre
        self.bind_ip_count = bind_ip_count
        self.pack_adv_thre = pack_adv_thre
        self.ip_basic_thre = ip_basic_thre
        self.ip_advance_thre = ip_advance_thre
        self.ip_spec = ip_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pack_basic_thre is not None:
            result['PackBasicThre'] = self.pack_basic_thre
        if self.bind_ip_count is not None:
            result['BindIpCount'] = self.bind_ip_count
        if self.pack_adv_thre is not None:
            result['PackAdvThre'] = self.pack_adv_thre
        if self.ip_basic_thre is not None:
            result['IpBasicThre'] = self.ip_basic_thre
        if self.ip_advance_thre is not None:
            result['IpAdvanceThre'] = self.ip_advance_thre
        if self.ip_spec is not None:
            result['IpSpec'] = self.ip_spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackBasicThre') is not None:
            self.pack_basic_thre = m.get('PackBasicThre')
        if m.get('BindIpCount') is not None:
            self.bind_ip_count = m.get('BindIpCount')
        if m.get('PackAdvThre') is not None:
            self.pack_adv_thre = m.get('PackAdvThre')
        if m.get('IpBasicThre') is not None:
            self.ip_basic_thre = m.get('IpBasicThre')
        if m.get('IpAdvanceThre') is not None:
            self.ip_advance_thre = m.get('IpAdvanceThre')
        if m.get('IpSpec') is not None:
            self.ip_spec = m.get('IpSpec')
        return self


class DescribeInstanceSpecsResponseBodyInstanceSpecs(TeaModel):
    def __init__(
        self,
        pack_config: DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig = None,
        region: str = None,
        available_delete_blackhole_count: str = None,
        instance_id: str = None,
    ):
        self.pack_config = pack_config
        self.region = region
        self.available_delete_blackhole_count = available_delete_blackhole_count
        self.instance_id = instance_id

    def validate(self):
        if self.pack_config:
            self.pack_config.validate()

    def to_map(self):
        result = dict()
        if self.pack_config is not None:
            result['PackConfig'] = self.pack_config.to_map()
        if self.region is not None:
            result['Region'] = self.region
        if self.available_delete_blackhole_count is not None:
            result['AvailableDeleteBlackholeCount'] = self.available_delete_blackhole_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackConfig') is not None:
            temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecsPackConfig()
            self.pack_config = temp_model.from_map(m['PackConfig'])
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AvailableDeleteBlackholeCount') is not None:
            self.available_delete_blackhole_count = m.get('AvailableDeleteBlackholeCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceSpecsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_specs: List[DescribeInstanceSpecsResponseBodyInstanceSpecs] = None,
    ):
        self.request_id = request_id
        self.instance_specs = instance_specs

    def validate(self):
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
                temp_model = DescribeInstanceSpecsResponseBodyInstanceSpecs()
                self.instance_specs.append(temp_model.from_map(k))
        return self


class DescribeInstanceSpecsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceSpecsResponseBody = None,
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
            temp_model = DescribeInstanceSpecsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOnDemandDdosEventRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        start_time: int = None,
        end_time: int = None,
        page_size: int = None,
        page_no: int = None,
        instance_id: str = None,
        ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_no = page_no
        self.instance_id = instance_id
        self.ip = ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
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


class DescribeOnDemandDdosEventResponseBodyEvents(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        status: str = None,
        start_time: int = None,
        mbps: int = None,
        ip: str = None,
        pps: int = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.mbps = mbps
        self.ip = ip
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.mbps is not None:
            result['Mbps'] = self.mbps
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.pps is not None:
            result['Pps'] = self.pps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Mbps') is not None:
            self.mbps = m.get('Mbps')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        return self


class DescribeOnDemandDdosEventResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        events: List[DescribeOnDemandDdosEventResponseBodyEvents] = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.events = events
        self.total = total

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.events = []
        if m.get('Events') is not None:
            for k in m.get('Events'):
                temp_model = DescribeOnDemandDdosEventResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeOnDemandDdosEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOnDemandDdosEventResponseBody = None,
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
            temp_model = DescribeOnDemandDdosEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOnDemandInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        region_id: str = None,
        instance_id_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.region_id = region_id
        self.instance_id_list = instance_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        return self


class DescribeOnDemandInstanceStatusResponseBodyInstances(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        mode: str = None,
        instance_id: str = None,
        declared: str = None,
        registed_as: str = None,
        net: str = None,
        desc: str = None,
    ):
        self.user_id = user_id
        self.mode = mode
        self.instance_id = instance_id
        self.declared = declared
        self.registed_as = registed_as
        self.net = net
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.declared is not None:
            result['Declared'] = self.declared
        if self.registed_as is not None:
            result['RegistedAs'] = self.registed_as
        if self.net is not None:
            result['Net'] = self.net
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Declared') is not None:
            self.declared = m.get('Declared')
        if m.get('RegistedAs') is not None:
            self.registed_as = m.get('RegistedAs')
        if m.get('Net') is not None:
            self.net = m.get('Net')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class DescribeOnDemandInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeOnDemandInstanceStatusResponseBodyInstances] = None,
        request_id: str = None,
    ):
        self.instances = instances
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeOnDemandInstanceStatusResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOnDemandInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOnDemandInstanceStatusResponseBody = None,
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
            temp_model = DescribeOnDemandInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        order_by: str = None,
        order_dir: str = None,
        instance_id: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
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
        pass

    def to_map(self):
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


class DescribeOpEntitiesResponseBodyOpEntities(TeaModel):
    def __init__(
        self,
        entity_type: int = None,
        entity_object: str = None,
        op_action: int = None,
        gmt_create: int = None,
        op_account: str = None,
        op_desc: str = None,
    ):
        self.entity_type = entity_type
        self.entity_object = entity_object
        self.op_action = op_action
        self.gmt_create = gmt_create
        self.op_account = op_account
        self.op_desc = op_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object
        if self.op_action is not None:
            result['OpAction'] = self.op_action
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.op_account is not None:
            result['OpAccount'] = self.op_account
        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')
        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')
        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')
        return self


class DescribeOpEntitiesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        op_entities: List[DescribeOpEntitiesResponseBodyOpEntities] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.op_entities = op_entities

    def validate(self):
        if self.op_entities:
            for k in self.op_entities:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k in self.op_entities:
                result['OpEntities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k in m.get('OpEntities'):
                temp_model = DescribeOpEntitiesResponseBodyOpEntities()
                self.op_entities.append(temp_model.from_map(k))
        return self


class DescribeOpEntitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeOpEntitiesResponseBody = None,
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
            temp_model = DescribeOpEntitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePackIpListRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        page_no: int = None,
        page_size: int = None,
        instance_id: str = None,
        ip: str = None,
        product_name: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.page_no = page_no
        self.page_size = page_size
        self.instance_id = instance_id
        self.ip = ip
        self.product_name = product_name
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
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


class DescribePackIpListResponseBodyIpList(TeaModel):
    def __init__(
        self,
        status: str = None,
        remark: str = None,
        product: str = None,
        ip: str = None,
    ):
        self.status = status
        self.remark = remark
        self.product = product
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.product is not None:
            result['Product'] = self.product
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribePackIpListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ip_list: List[DescribePackIpListResponseBodyIpList] = None,
        total: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.ip_list = ip_list
        self.total = total
        self.code = code
        self.success = success

    def validate(self):
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = DescribePackIpListResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePackIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePackIpListResponseBody = None,
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
            temp_model = DescribePackIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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


class DescribePackPaidTrafficResponseBodyPackPaidTraffics(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        base_bandwidth: int = None,
        elastic_bandwidth: int = None,
        total_capacity: float = None,
        max_attack: float = None,
        instance_id: str = None,
        paid_capacity: float = None,
    ):
        self.start_time = start_time
        self.base_bandwidth = base_bandwidth
        self.elastic_bandwidth = elastic_bandwidth
        self.total_capacity = total_capacity
        self.max_attack = max_attack
        self.instance_id = instance_id
        self.paid_capacity = paid_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.max_attack is not None:
            result['MaxAttack'] = self.max_attack
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.paid_capacity is not None:
            result['PaidCapacity'] = self.paid_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('MaxAttack') is not None:
            self.max_attack = m.get('MaxAttack')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PaidCapacity') is not None:
            self.paid_capacity = m.get('PaidCapacity')
        return self


class DescribePackPaidTrafficResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        pack_paid_traffics: List[DescribePackPaidTrafficResponseBodyPackPaidTraffics] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.pack_paid_traffics = pack_paid_traffics

    def validate(self):
        if self.pack_paid_traffics:
            for k in self.pack_paid_traffics:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PackPaidTraffics'] = []
        if self.pack_paid_traffics is not None:
            for k in self.pack_paid_traffics:
                result['PackPaidTraffics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.pack_paid_traffics = []
        if m.get('PackPaidTraffics') is not None:
            for k in m.get('PackPaidTraffics'):
                temp_model = DescribePackPaidTrafficResponseBodyPackPaidTraffics()
                self.pack_paid_traffics.append(temp_model.from_map(k))
        return self


class DescribePackPaidTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePackPaidTrafficResponseBody = None,
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
            temp_model = DescribePackPaidTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
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
        pass

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


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.regions = regions
        self.code = code
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
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
        pass

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


class DescribeResourcePackInstancesResponseBodyResourcePacks(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        status: str = None,
        start_time: int = None,
        resource_pack_id: str = None,
        curr_capacity: int = None,
        init_capacity: int = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.resource_pack_id = resource_pack_id
        self.curr_capacity = curr_capacity
        self.init_capacity = init_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.resource_pack_id is not None:
            result['ResourcePackId'] = self.resource_pack_id
        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity
        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ResourcePackId') is not None:
            self.resource_pack_id = m.get('ResourcePackId')
        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')
        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')
        return self


class DescribeResourcePackInstancesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        resource_packs: List[DescribeResourcePackInstancesResponseBodyResourcePacks] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.resource_packs = resource_packs

    def validate(self):
        if self.resource_packs:
            for k in self.resource_packs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourcePacks'] = []
        if self.resource_packs is not None:
            for k in self.resource_packs:
                result['ResourcePacks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_packs = []
        if m.get('ResourcePacks') is not None:
            for k in m.get('ResourcePacks'):
                temp_model = DescribeResourcePackInstancesResponseBodyResourcePacks()
                self.resource_packs.append(temp_model.from_map(k))
        return self


class DescribeResourcePackInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeResourcePackInstancesResponseBody = None,
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
            temp_model = DescribeResourcePackInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class DescribeResourcePackStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_init_capacity: int = None,
        total_curr_capacity: int = None,
        available_pack_num: int = None,
        total_used_capacity: int = None,
    ):
        self.request_id = request_id
        self.total_init_capacity = total_init_capacity
        self.total_curr_capacity = total_curr_capacity
        self.available_pack_num = available_pack_num
        self.total_used_capacity = total_used_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_init_capacity is not None:
            result['TotalInitCapacity'] = self.total_init_capacity
        if self.total_curr_capacity is not None:
            result['TotalCurrCapacity'] = self.total_curr_capacity
        if self.available_pack_num is not None:
            result['AvailablePackNum'] = self.available_pack_num
        if self.total_used_capacity is not None:
            result['TotalUsedCapacity'] = self.total_used_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalInitCapacity') is not None:
            self.total_init_capacity = m.get('TotalInitCapacity')
        if m.get('TotalCurrCapacity') is not None:
            self.total_curr_capacity = m.get('TotalCurrCapacity')
        if m.get('AvailablePackNum') is not None:
            self.available_pack_num = m.get('AvailablePackNum')
        if m.get('TotalUsedCapacity') is not None:
            self.total_used_capacity = m.get('TotalUsedCapacity')
        return self


class DescribeResourcePackStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeResourcePackStatisticsResponseBody = None,
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
            temp_model = DescribeResourcePackStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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


class DescribeResourcePackUsageResponseBodyPackUsages(TeaModel):
    def __init__(
        self,
        time: int = None,
        traffic: float = None,
    ):
        self.time = time
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.traffic is not None:
            result['Traffic'] = self.traffic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')
        return self


class DescribeResourcePackUsageResponseBody(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        request_id: str = None,
        pack_usages: List[DescribeResourcePackUsageResponseBodyPackUsages] = None,
        start_time: int = None,
        interval: int = None,
    ):
        self.end_time = end_time
        self.request_id = request_id
        self.pack_usages = pack_usages
        self.start_time = start_time
        self.interval = interval

    def validate(self):
        if self.pack_usages:
            for k in self.pack_usages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PackUsages'] = []
        if self.pack_usages is not None:
            for k in self.pack_usages:
                result['PackUsages'].append(k.to_map() if k else None)
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.interval is not None:
            result['Interval'] = self.interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.pack_usages = []
        if m.get('PackUsages') is not None:
            for k in m.get('PackUsages'):
                temp_model = DescribeResourcePackUsageResponseBodyPackUsages()
                self.pack_usages.append(temp_model.from_map(k))
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        return self


class DescribeResourcePackUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeResourcePackUsageResponseBody = None,
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
            temp_model = DescribeResourcePackUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTrafficRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        ipnet: str = None,
        ip: str = None,
        start_time: int = None,
        end_time: int = None,
        interval: int = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.ipnet = ipnet
        self.ip = ip
        self.start_time = start_time
        self.end_time = end_time
        self.interval = interval
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
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


class DescribeTrafficResponseBodyFlowList(TeaModel):
    def __init__(
        self,
        time: int = None,
        flow_type: str = None,
        attack_pps: int = None,
        name: str = None,
        pps: int = None,
        kbps: int = None,
        attack_bps: int = None,
    ):
        self.time = time
        self.flow_type = flow_type
        self.attack_pps = attack_pps
        self.name = name
        self.pps = pps
        self.kbps = kbps
        self.attack_bps = attack_bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.flow_type is not None:
            result['FlowType'] = self.flow_type
        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps
        if self.name is not None:
            result['Name'] = self.name
        if self.pps is not None:
            result['Pps'] = self.pps
        if self.kbps is not None:
            result['Kbps'] = self.kbps
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')
        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pps') is not None:
            self.pps = m.get('Pps')
        if m.get('Kbps') is not None:
            self.kbps = m.get('Kbps')
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')
        return self


class DescribeTrafficResponseBody(TeaModel):
    def __init__(
        self,
        flow_list: List[DescribeTrafficResponseBodyFlowList] = None,
        request_id: str = None,
    ):
        self.flow_list = flow_list
        self.request_id = request_id

    def validate(self):
        if self.flow_list:
            for k in self.flow_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FlowList'] = []
        if self.flow_list is not None:
            for k in self.flow_list:
                result['FlowList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_list = []
        if m.get('FlowList') is not None:
            for k in m.get('FlowList'):
                temp_model = DescribeTrafficResponseBodyFlowList()
                self.flow_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTrafficResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTrafficResponseBody = None,
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
            temp_model = DescribeTrafficResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        region_id: str = None,
        tag_owner_uid: str = None,
        tag_owner_bid: str = None,
        resource_type: str = None,
        scope: str = None,
        page_size: int = None,
        current_page: int = None,
        resource_group_id: str = None,
    ):
        self.source_ip = source_ip
        self.region_id = region_id
        self.tag_owner_uid = tag_owner_uid
        self.tag_owner_bid = tag_owner_bid
        self.resource_type = resource_type
        self.scope = scope
        self.page_size = page_size
        self.current_page = current_page
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid
        if self.tag_owner_bid is not None:
            result['TagOwnerBid'] = self.tag_owner_bid
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')
        if m.get('TagOwnerBid') is not None:
            self.tag_owner_bid = m.get('TagOwnerBid')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(
        self,
        tag_count: int = None,
        tag_key: str = None,
    ):
        self.tag_count = tag_count
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        current_page: int = None,
        tag_keys: List[ListTagKeysResponseBodyTagKeys] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.current_page = current_page
        self.tag_keys = tag_keys

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagKeysResponseBody = None,
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
            temp_model = ListTagKeysResponseBody()
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
        source_ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
        tag_owner_uid: str = None,
        tag_owner_bid: str = None,
        resource_type: str = None,
        scope: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id
        self.tag_owner_uid = tag_owner_uid
        self.tag_owner_bid = tag_owner_bid
        self.resource_type = resource_type
        self.scope = scope
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid
        if self.tag_owner_bid is not None:
            result['TagOwnerBid'] = self.tag_owner_bid
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')
        if m.get('TagOwnerBid') is not None:
            self.tag_owner_bid = m.get('TagOwnerBid')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
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
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRemarkRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        lang: str = None,
        instance_id: str = None,
        remark: str = None,
        resource_group_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.lang = lang
        self.instance_id = instance_id
        self.remark = remark
        self.resource_group_id = resource_group_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.lang is not None:
            result['Lang'] = self.lang
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
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyRemarkResponseBody(TeaModel):
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


class ModifyRemarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRemarkResponseBody = None,
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
            temp_model = ModifyRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySchedruleOnDemandRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.source_ip = source_ip
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QuerySchedruleOnDemandResponseBodyRuleStatus(TeaModel):
    def __init__(
        self,
        rule_sched_status: str = None,
        net: str = None,
    ):
        self.rule_sched_status = rule_sched_status
        self.net = net

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_sched_status is not None:
            result['RuleSchedStatus'] = self.rule_sched_status
        if self.net is not None:
            result['Net'] = self.net
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleSchedStatus') is not None:
            self.rule_sched_status = m.get('RuleSchedStatus')
        if m.get('Net') is not None:
            self.net = m.get('Net')
        return self


class QuerySchedruleOnDemandResponseBodyRuleConfig(TeaModel):
    def __init__(
        self,
        rule_switch: str = None,
        rule_condition_mbps: str = None,
        time_zone: str = None,
        rule_action: str = None,
        rule_condition_kpps: str = None,
        rule_undo_mode: str = None,
        rule_undo_begin_time: str = None,
        rule_condition_cnt: str = None,
        rule_undo_end_time: str = None,
        rule_name: str = None,
    ):
        self.rule_switch = rule_switch
        self.rule_condition_mbps = rule_condition_mbps
        self.time_zone = time_zone
        self.rule_action = rule_action
        self.rule_condition_kpps = rule_condition_kpps
        self.rule_undo_mode = rule_undo_mode
        self.rule_undo_begin_time = rule_undo_begin_time
        self.rule_condition_cnt = rule_condition_cnt
        self.rule_undo_end_time = rule_undo_end_time
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch
        if self.rule_condition_mbps is not None:
            result['RuleConditionMbps'] = self.rule_condition_mbps
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action
        if self.rule_condition_kpps is not None:
            result['RuleConditionKpps'] = self.rule_condition_kpps
        if self.rule_undo_mode is not None:
            result['RuleUndoMode'] = self.rule_undo_mode
        if self.rule_undo_begin_time is not None:
            result['RuleUndoBeginTime'] = self.rule_undo_begin_time
        if self.rule_condition_cnt is not None:
            result['RuleConditionCnt'] = self.rule_condition_cnt
        if self.rule_undo_end_time is not None:
            result['RuleUndoEndTime'] = self.rule_undo_end_time
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')
        if m.get('RuleConditionMbps') is not None:
            self.rule_condition_mbps = m.get('RuleConditionMbps')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')
        if m.get('RuleConditionKpps') is not None:
            self.rule_condition_kpps = m.get('RuleConditionKpps')
        if m.get('RuleUndoMode') is not None:
            self.rule_undo_mode = m.get('RuleUndoMode')
        if m.get('RuleUndoBeginTime') is not None:
            self.rule_undo_begin_time = m.get('RuleUndoBeginTime')
        if m.get('RuleConditionCnt') is not None:
            self.rule_condition_cnt = m.get('RuleConditionCnt')
        if m.get('RuleUndoEndTime') is not None:
            self.rule_undo_end_time = m.get('RuleUndoEndTime')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class QuerySchedruleOnDemandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        user_id: str = None,
        rule_status: List[QuerySchedruleOnDemandResponseBodyRuleStatus] = None,
        rule_config: List[QuerySchedruleOnDemandResponseBodyRuleConfig] = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.user_id = user_id
        self.rule_status = rule_status
        self.rule_config = rule_config

    def validate(self):
        if self.rule_status:
            for k in self.rule_status:
                if k:
                    k.validate()
        if self.rule_config:
            for k in self.rule_config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        result['RuleStatus'] = []
        if self.rule_status is not None:
            for k in self.rule_status:
                result['RuleStatus'].append(k.to_map() if k else None)
        result['RuleConfig'] = []
        if self.rule_config is not None:
            for k in self.rule_config:
                result['RuleConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        self.rule_status = []
        if m.get('RuleStatus') is not None:
            for k in m.get('RuleStatus'):
                temp_model = QuerySchedruleOnDemandResponseBodyRuleStatus()
                self.rule_status.append(temp_model.from_map(k))
        self.rule_config = []
        if m.get('RuleConfig') is not None:
            for k in m.get('RuleConfig'):
                temp_model = QuerySchedruleOnDemandResponseBodyRuleConfig()
                self.rule_config.append(temp_model.from_map(k))
        return self


class QuerySchedruleOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySchedruleOnDemandResponseBody = None,
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
            temp_model = QuerySchedruleOnDemandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstanceModeOnDemandRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        mode: str = None,
        region_id: str = None,
        instance_id_list: List[str] = None,
    ):
        self.source_ip = source_ip
        self.mode = mode
        self.region_id = region_id
        self.instance_id_list = instance_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')
        return self


class SetInstanceModeOnDemandResponseBody(TeaModel):
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


class SetInstanceModeOnDemandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetInstanceModeOnDemandResponseBody = None,
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
            temp_model = SetInstanceModeOnDemandResponseBody()
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
        source_ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
        tag_owner_uid: str = None,
        tag_owner_bid: str = None,
        resource_type: str = None,
        scope: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id
        self.tag_owner_uid = tag_owner_uid
        self.tag_owner_bid = tag_owner_bid
        self.resource_type = resource_type
        self.scope = scope
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid
        if self.tag_owner_bid is not None:
            result['TagOwnerBid'] = self.tag_owner_bid
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')
        if m.get('TagOwnerBid') is not None:
            self.tag_owner_bid = m.get('TagOwnerBid')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        resource_group_id: str = None,
        region_id: str = None,
        tag_owner_uid: str = None,
        tag_owner_bid: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.source_ip = source_ip
        self.resource_group_id = resource_group_id
        self.region_id = region_id
        self.tag_owner_uid = tag_owner_uid
        self.tag_owner_bid = tag_owner_bid
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tag_owner_uid is not None:
            result['TagOwnerUid'] = self.tag_owner_uid
        if self.tag_owner_bid is not None:
            result['TagOwnerBid'] = self.tag_owner_bid
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TagOwnerUid') is not None:
            self.tag_owner_uid = m.get('TagOwnerUid')
        if m.get('TagOwnerBid') is not None:
            self.tag_owner_bid = m.get('TagOwnerBid')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
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
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


