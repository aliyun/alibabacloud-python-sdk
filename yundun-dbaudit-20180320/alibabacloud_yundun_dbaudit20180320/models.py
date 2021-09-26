# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddLogMaskConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mask_name: str = None,
        mask_regex: str = None,
        mask_txt: str = None,
        mask_description: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mask_name = mask_name
        self.mask_regex = mask_regex
        self.mask_txt = mask_txt
        self.mask_description = mask_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_name is not None:
            result['MaskName'] = self.mask_name
        if self.mask_regex is not None:
            result['MaskRegex'] = self.mask_regex
        if self.mask_txt is not None:
            result['MaskTxt'] = self.mask_txt
        if self.mask_description is not None:
            result['MaskDescription'] = self.mask_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskName') is not None:
            self.mask_name = m.get('MaskName')
        if m.get('MaskRegex') is not None:
            self.mask_regex = m.get('MaskRegex')
        if m.get('MaskTxt') is not None:
            self.mask_txt = m.get('MaskTxt')
        if m.get('MaskDescription') is not None:
            self.mask_description = m.get('MaskDescription')
        return self


class AddLogMaskConfigResponseBody(TeaModel):
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


class AddLogMaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddLogMaskConfigResponseBody = None,
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
            temp_model = AddLogMaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateDbToRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        rule_ids: str = None,
        rule_db_relations: str = None,
        oper_type: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.rule_ids = rule_ids
        self.rule_db_relations = rule_db_relations
        self.oper_type = oper_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.rule_db_relations is not None:
            result['RuleDbRelations'] = self.rule_db_relations
        if self.oper_type is not None:
            result['OperType'] = self.oper_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('RuleDbRelations') is not None:
            self.rule_db_relations = m.get('RuleDbRelations')
        if m.get('OperType') is not None:
            self.oper_type = m.get('OperType')
        return self


class AssociateDbToRuleResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateDbToRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateDbToRuleResponseBody = None,
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
            temp_model = AssociateDbToRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateRuleToDbRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        json_param: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.json_param = json_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class AssociateRuleToDbResponseBodyServerData(TeaModel):
    def __init__(
        self,
        json_result: str = None,
    ):
        self.json_result = json_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class AssociateRuleToDbResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: AssociateRuleToDbResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = AssociateRuleToDbResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class AssociateRuleToDbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateRuleToDbResponseBody = None,
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
            temp_model = AssociateRuleToDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeAgentStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        agent_id: str = None,
        agent_status: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.agent_id = agent_id
        self.agent_status = agent_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        return self


class ChangeAgentStatusResponseBody(TeaModel):
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


class ChangeAgentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeAgentStatusResponseBody = None,
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
            temp_model = ChangeAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeLogMaskConfigStateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mask_id: int = None,
        mask_state: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mask_id = mask_id
        self.mask_state = mask_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id is not None:
            result['MaskId'] = self.mask_id
        if self.mask_state is not None:
            result['MaskState'] = self.mask_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskId') is not None:
            self.mask_id = m.get('MaskId')
        if m.get('MaskState') is not None:
            self.mask_state = m.get('MaskState')
        return self


class ChangeLogMaskConfigStateResponseBody(TeaModel):
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


class ChangeLogMaskConfigStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeLogMaskConfigStateResponseBody = None,
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
            temp_model = ChangeLogMaskConfigStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeRulePriorityRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: str = None,
        rule_infos: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.rule_infos = rule_infos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_infos is not None:
            result['RuleInfos'] = self.rule_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleInfos') is not None:
            self.rule_infos = m.get('RuleInfos')
        return self


class ChangeRulePriorityResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeRulePriorityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeRulePriorityResponseBody = None,
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
            temp_model = ChangeRulePriorityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeRuleStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        json_param: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.json_param = json_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class ChangeRuleStatusResponseBody(TeaModel):
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


class ChangeRuleStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeRuleStatusResponseBody = None,
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
            temp_model = ChangeRuleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMailRegisteredRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mail: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mail = mail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mail is not None:
            result['Mail'] = self.mail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        return self


class CheckMailRegisteredResponseBody(TeaModel):
    def __init__(
        self,
        registered: bool = None,
        request_id: str = None,
    ):
        self.registered = registered
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registered is not None:
            result['Registered'] = self.registered
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Registered') is not None:
            self.registered = m.get('Registered')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckMailRegisteredResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckMailRegisteredResponseBody = None,
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
            temp_model = CheckMailRegisteredResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearAgentRecordsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        agent_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.agent_ids = agent_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        return self


class ClearAgentRecordsResponseBody(TeaModel):
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


class ClearAgentRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClearAgentRecordsResponseBody = None,
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
            temp_model = ClearAgentRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceNetworkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        public_access_control: int = None,
        region_id: str = None,
        private_white_list: List[str] = None,
        public_white_list: List[str] = None,
        security_group_ids: List[str] = None,
    ):
        self.instance_id = instance_id
        self.public_access_control = public_access_control
        self.region_id = region_id
        self.private_white_list = private_white_list
        self.public_white_list = public_white_list
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_access_control is not None:
            result['PublicAccessControl'] = self.public_access_control
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list
        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicAccessControl') is not None:
            self.public_access_control = m.get('PublicAccessControl')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')
        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class ConfigInstanceNetworkResponseBody(TeaModel):
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


class ConfigInstanceNetworkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigInstanceNetworkResponseBody = None,
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
            temp_model = ConfigInstanceNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_name: str = None,
        db_instance_id: str = None,
        asset_type: int = None,
        db_type: int = None,
        db_version: int = None,
        db_certificate: str = None,
        db_username: str = None,
        db_password: str = None,
        db_addresses: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_name = db_name
        self.db_instance_id = db_instance_id
        self.asset_type = asset_type
        self.db_type = db_type
        self.db_version = db_version
        self.db_certificate = db_certificate
        self.db_username = db_username
        self.db_password = db_password
        self.db_addresses = db_addresses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.db_certificate is not None:
            result['DbCertificate'] = self.db_certificate
        if self.db_username is not None:
            result['DbUsername'] = self.db_username
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DbCertificate') is not None:
            self.db_certificate = m.get('DbCertificate')
        if m.get('DbUsername') is not None:
            self.db_username = m.get('DbUsername')
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')
        return self


class CreateDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        request_id: str = None,
    ):
        self.db_id = db_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataSourceResponseBody = None,
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
            temp_model = CreateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGradeProtectionReportRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class CreateGradeProtectionReportResponseBodyServerData(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateGradeProtectionReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: CreateGradeProtectionReportResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreateGradeProtectionReportResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreateGradeProtectionReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGradeProtectionReportResponseBody = None,
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
            temp_model = CreateGradeProtectionReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntegratedReportRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class CreateIntegratedReportResponseBodyServerData(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateIntegratedReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: CreateIntegratedReportResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreateIntegratedReportResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreateIntegratedReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIntegratedReportResponseBody = None,
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
            temp_model = CreateIntegratedReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogAlarmTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        task_name: str = None,
        to_mail_list: List[str] = None,
        db_id_list: List[str] = None,
        risk_level_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.task_name = task_name
        self.to_mail_list = to_mail_list
        self.db_id_list = db_id_list
        self.risk_level_list = risk_level_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        if self.db_id_list is not None:
            result['DbIdList'] = self.db_id_list
        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        if m.get('DbIdList') is not None:
            self.db_id_list = m.get('DbIdList')
        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')
        return self


class CreateLogAlarmTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
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


class CreateLogAlarmTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLogAlarmTaskResponseBody = None,
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
            temp_model = CreateLogAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePCIReportRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class CreatePCIReportResponseBodyServerData(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreatePCIReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: CreatePCIReportResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreatePCIReportResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreatePCIReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePCIReportResponseBody = None,
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
            temp_model = CreatePCIReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReportPushTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        schedule_type: str = None,
        schedule_time: str = None,
        job_status: int = None,
        report_type: List[str] = None,
        db_list: List[str] = None,
        email_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.schedule_type = schedule_type
        self.schedule_time = schedule_time
        self.job_status = job_status
        self.report_type = report_type
        self.db_list = db_list
        self.email_list = email_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.email_list is not None:
            result['EmailList'] = self.email_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('EmailList') is not None:
            self.email_list = m.get('EmailList')
        return self


class CreateReportPushTaskResponseBody(TeaModel):
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


class CreateReportPushTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateReportPushTaskResponseBody = None,
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
            temp_model = CreateReportPushTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        rule_info: str = None,
        rule_db_relation: str = None,
        rule_group: str = None,
        effect_current_dbstatus: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.rule_info = rule_info
        self.rule_db_relation = rule_db_relation
        self.rule_group = rule_group
        self.effect_current_dbstatus = effect_current_dbstatus

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_info is not None:
            result['RuleInfo'] = self.rule_info
        if self.rule_db_relation is not None:
            result['RuleDbRelation'] = self.rule_db_relation
        if self.rule_group is not None:
            result['RuleGroup'] = self.rule_group
        if self.effect_current_dbstatus is not None:
            result['EffectCurrentDBStatus'] = self.effect_current_dbstatus
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleInfo') is not None:
            self.rule_info = m.get('RuleInfo')
        if m.get('RuleDbRelation') is not None:
            self.rule_db_relation = m.get('RuleDbRelation')
        if m.get('RuleGroup') is not None:
            self.rule_group = m.get('RuleGroup')
        if m.get('EffectCurrentDBStatus') is not None:
            self.effect_current_dbstatus = m.get('EffectCurrentDBStatus')
        return self


class CreateRuleResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRuleResponseBody = None,
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
            temp_model = CreateRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRuleGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        group_name: str = None,
        group_type: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.group_name = group_name
        self.group_type = group_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        return self


class CreateRuleGroupResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRuleGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRuleGroupResponseBody = None,
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
            temp_model = CreateRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSOXReportRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class CreateSOXReportResponseBodyServerData(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateSOXReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: CreateSOXReportResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreateSOXReportResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreateSOXReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSOXReportResponseBody = None,
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
            temp_model = CreateSOXReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSqlRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        json_param: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.json_param = json_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class CreateSqlRuleResponseBodyServerData(TeaModel):
    def __init__(
        self,
        json_result: str = None,
    ):
        self.json_result = json_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class CreateSqlRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: CreateSqlRuleResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = CreateSqlRuleResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class CreateSqlRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSqlRuleResponseBody = None,
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
            temp_model = CreateSqlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSystemAlarmTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        task_name: str = None,
        to_mail_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.task_name = task_name
        self.to_mail_list = to_mail_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        return self


class CreateSystemAlarmTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
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


class CreateSystemAlarmTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSystemAlarmTaskResponseBody = None,
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
            temp_model = CreateSystemAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        task_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class DeleteAlarmTaskResponseBody(TeaModel):
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


class DeleteAlarmTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlarmTaskResponseBody = None,
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
            temp_model = DeleteAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_ids = db_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_ids is not None:
            result['DbIds'] = self.db_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbIds') is not None:
            self.db_ids = m.get('DbIds')
        return self


class DeleteDataSourceResponseBody(TeaModel):
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


class DeleteDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataSourceResponseBody = None,
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
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReportPushTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        job_id: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteReportPushTaskResponseBody(TeaModel):
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


class DeleteReportPushTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteReportPushTaskResponseBody = None,
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
            temp_model = DeleteReportPushTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        rule_id: str = None,
        rule_type: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.rule_id = rule_id
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class DeleteRuleResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRuleResponseBody = None,
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
            temp_model = DeleteRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRuleGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        group_key_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.group_key_id = group_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_key_id is not None:
            result['GroupKeyId'] = self.group_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupKeyId') is not None:
            self.group_key_id = m.get('GroupKeyId')
        return self


class DeleteRuleGroupResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRuleGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRuleGroupResponseBody = None,
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
            temp_model = DeleteRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeregisterTemplatesFromRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        sentence_param: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.sentence_param = sentence_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sentence_param is not None:
            result['SentenceParam'] = self.sentence_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SentenceParam') is not None:
            self.sentence_param = m.get('SentenceParam')
        return self


class DeregisterTemplatesFromRuleResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeregisterTemplatesFromRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeregisterTemplatesFromRuleResponseBody = None,
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
            temp_model = DeregisterTemplatesFromRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeInstanceAttributeResponseBodyInstanceAttribute(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        vswitch_id: str = None,
        internet_ip: str = None,
        network_type: str = None,
        image_version_name: str = None,
        series_code: str = None,
        description: str = None,
        access_type: int = None,
        ecs_status: str = None,
        operatable: bool = None,
        plan_upgrade_status: int = None,
        expire_time: int = None,
        upgradeable: bool = None,
        instance_id: str = None,
        internet_endpoint: str = None,
        intranet_ip: str = None,
        renewable: bool = None,
        region_id: str = None,
        intranet_endpoint: str = None,
        start_time: int = None,
        upgrade_status: int = None,
        plan_upgradeable: bool = None,
        instance_status: str = None,
        license_code: str = None,
        public_access_control: int = None,
        public_white_list: List[str] = None,
        security_group_ids: List[str] = None,
        private_white_list: List[str] = None,
    ):
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.internet_ip = internet_ip
        self.network_type = network_type
        self.image_version_name = image_version_name
        self.series_code = series_code
        self.description = description
        self.access_type = access_type
        self.ecs_status = ecs_status
        self.operatable = operatable
        self.plan_upgrade_status = plan_upgrade_status
        self.expire_time = expire_time
        self.upgradeable = upgradeable
        self.instance_id = instance_id
        self.internet_endpoint = internet_endpoint
        self.intranet_ip = intranet_ip
        self.renewable = renewable
        self.region_id = region_id
        self.intranet_endpoint = intranet_endpoint
        self.start_time = start_time
        self.upgrade_status = upgrade_status
        self.plan_upgradeable = plan_upgradeable
        self.instance_status = instance_status
        self.license_code = license_code
        self.public_access_control = public_access_control
        self.public_white_list = public_white_list
        self.security_group_ids = security_group_ids
        self.private_white_list = private_white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.image_version_name is not None:
            result['ImageVersionName'] = self.image_version_name
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.ecs_status is not None:
            result['EcsStatus'] = self.ecs_status
        if self.operatable is not None:
            result['Operatable'] = self.operatable
        if self.plan_upgrade_status is not None:
            result['PlanUpgradeStatus'] = self.plan_upgrade_status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.renewable is not None:
            result['Renewable'] = self.renewable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status
        if self.plan_upgradeable is not None:
            result['PlanUpgradeable'] = self.plan_upgradeable
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.public_access_control is not None:
            result['PublicAccessControl'] = self.public_access_control
        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ImageVersionName') is not None:
            self.image_version_name = m.get('ImageVersionName')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('EcsStatus') is not None:
            self.ecs_status = m.get('EcsStatus')
        if m.get('Operatable') is not None:
            self.operatable = m.get('Operatable')
        if m.get('PlanUpgradeStatus') is not None:
            self.plan_upgrade_status = m.get('PlanUpgradeStatus')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Renewable') is not None:
            self.renewable = m.get('Renewable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')
        if m.get('PlanUpgradeable') is not None:
            self.plan_upgradeable = m.get('PlanUpgradeable')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PublicAccessControl') is not None:
            self.public_access_control = m.get('PublicAccessControl')
        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_attribute: DescribeInstanceAttributeResponseBodyInstanceAttribute = None,
    ):
        self.request_id = request_id
        self.instance_attribute = instance_attribute

    def validate(self):
        if self.instance_attribute:
            self.instance_attribute.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_attribute is not None:
            result['InstanceAttribute'] = self.instance_attribute.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceAttribute') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstanceAttribute()
            self.instance_attribute = temp_model.from_map(m['InstanceAttribute'])
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceAttributeResponseBody = None,
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
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
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


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_status: str = None,
        region_id: str = None,
        page_no: int = None,
        current_page: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        instance_id: List[str] = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        self.instance_status = instance_status
        self.region_id = region_id
        self.page_no = page_no
        self.current_page = current_page
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.instance_id = instance_id
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
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        vswitch_id: str = None,
        internet_ip: str = None,
        network_type: str = None,
        image_version_name: str = None,
        series_code: str = None,
        description: str = None,
        ecs_status: str = None,
        operatable: bool = None,
        plan_upgrade_status: int = None,
        expire_time: int = None,
        upgradeable: bool = None,
        legacy: bool = None,
        instance_id: str = None,
        internet_endpoint: str = None,
        intranet_ip: str = None,
        renewable: bool = None,
        region_id: str = None,
        intranet_endpoint: str = None,
        start_time: int = None,
        upgrade_status: int = None,
        plan_upgradeable: bool = None,
        instance_status: str = None,
        license_code: str = None,
    ):
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.internet_ip = internet_ip
        self.network_type = network_type
        self.image_version_name = image_version_name
        self.series_code = series_code
        self.description = description
        self.ecs_status = ecs_status
        self.operatable = operatable
        self.plan_upgrade_status = plan_upgrade_status
        self.expire_time = expire_time
        self.upgradeable = upgradeable
        self.legacy = legacy
        self.instance_id = instance_id
        self.internet_endpoint = internet_endpoint
        self.intranet_ip = intranet_ip
        self.renewable = renewable
        self.region_id = region_id
        self.intranet_endpoint = intranet_endpoint
        self.start_time = start_time
        self.upgrade_status = upgrade_status
        self.plan_upgradeable = plan_upgradeable
        self.instance_status = instance_status
        self.license_code = license_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.image_version_name is not None:
            result['ImageVersionName'] = self.image_version_name
        if self.series_code is not None:
            result['SeriesCode'] = self.series_code
        if self.description is not None:
            result['Description'] = self.description
        if self.ecs_status is not None:
            result['EcsStatus'] = self.ecs_status
        if self.operatable is not None:
            result['Operatable'] = self.operatable
        if self.plan_upgrade_status is not None:
            result['PlanUpgradeStatus'] = self.plan_upgrade_status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.upgradeable is not None:
            result['Upgradeable'] = self.upgradeable
        if self.legacy is not None:
            result['Legacy'] = self.legacy
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.renewable is not None:
            result['Renewable'] = self.renewable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status
        if self.plan_upgradeable is not None:
            result['PlanUpgradeable'] = self.plan_upgradeable
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('ImageVersionName') is not None:
            self.image_version_name = m.get('ImageVersionName')
        if m.get('SeriesCode') is not None:
            self.series_code = m.get('SeriesCode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EcsStatus') is not None:
            self.ecs_status = m.get('EcsStatus')
        if m.get('Operatable') is not None:
            self.operatable = m.get('Operatable')
        if m.get('PlanUpgradeStatus') is not None:
            self.plan_upgrade_status = m.get('PlanUpgradeStatus')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Upgradeable') is not None:
            self.upgradeable = m.get('Upgradeable')
        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('Renewable') is not None:
            self.renewable = m.get('Renewable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')
        if m.get('PlanUpgradeable') is not None:
            self.plan_upgradeable = m.get('PlanUpgradeable')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLoginTicketRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeLoginTicketResponseBodyLoginTicketZones(TeaModel):
    def __init__(
        self,
        zone_id: str = None,
        local_name: str = None,
    ):
        self.zone_id = zone_id
        self.local_name = local_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        return self


class DescribeLoginTicketResponseBodyLoginTicket(TeaModel):
    def __init__(
        self,
        ticket: str = None,
        certificate: str = None,
        zones: List[DescribeLoginTicketResponseBodyLoginTicketZones] = None,
    ):
        self.ticket = ticket
        self.certificate = certificate
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.certificate is not None:
            result['Certificate'] = self.certificate
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeLoginTicketResponseBodyLoginTicketZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeLoginTicketResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        login_ticket: DescribeLoginTicketResponseBodyLoginTicket = None,
    ):
        self.request_id = request_id
        self.login_ticket = login_ticket

    def validate(self):
        if self.login_ticket:
            self.login_ticket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_ticket is not None:
            result['LoginTicket'] = self.login_ticket.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoginTicket') is not None:
            temp_model = DescribeLoginTicketResponseBodyLoginTicket()
            self.login_ticket = temp_model.from_map(m['LoginTicket'])
        return self


class DescribeLoginTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeLoginTicketResponseBody = None,
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
            temp_model = DescribeLoginTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
    ):
        self.region_endpoint = region_endpoint
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DescribeSyncInfoRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeSyncInfoResponseBodyInstanceInfo(TeaModel):
    def __init__(
        self,
        status: int = None,
        vswitch_id: str = None,
        region_no: str = None,
        ecs_instance_id: str = None,
        image_version_name: str = None,
        plan_code: str = None,
        ecs_uuid: str = None,
        access_type: int = None,
        ecs_status: str = None,
        plan_upgrade_status: int = None,
        zone_no: str = None,
        aliuid: int = None,
        product_name: str = None,
        ecs_eip: str = None,
        expire_time: int = None,
        ecs_internet_ip: str = None,
        instance_id: str = None,
        renewable: bool = None,
        ecs_intranet_ip: str = None,
        start_time: int = None,
        region_name: str = None,
        upgrade_status: int = None,
        plan_upgradeable: str = None,
        custom_name: str = None,
        ecs_network_type: str = None,
        public_access_control: int = None,
        vendor_code: str = None,
        plan_name: str = None,
        product_code: str = None,
    ):
        self.status = status
        self.vswitch_id = vswitch_id
        self.region_no = region_no
        self.ecs_instance_id = ecs_instance_id
        self.image_version_name = image_version_name
        self.plan_code = plan_code
        self.ecs_uuid = ecs_uuid
        self.access_type = access_type
        self.ecs_status = ecs_status
        self.plan_upgrade_status = plan_upgrade_status
        self.zone_no = zone_no
        self.aliuid = aliuid
        self.product_name = product_name
        self.ecs_eip = ecs_eip
        self.expire_time = expire_time
        self.ecs_internet_ip = ecs_internet_ip
        self.instance_id = instance_id
        self.renewable = renewable
        self.ecs_intranet_ip = ecs_intranet_ip
        self.start_time = start_time
        self.region_name = region_name
        self.upgrade_status = upgrade_status
        self.plan_upgradeable = plan_upgradeable
        self.custom_name = custom_name
        self.ecs_network_type = ecs_network_type
        self.public_access_control = public_access_control
        self.vendor_code = vendor_code
        self.plan_name = plan_name
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.image_version_name is not None:
            result['ImageVersionName'] = self.image_version_name
        if self.plan_code is not None:
            result['PlanCode'] = self.plan_code
        if self.ecs_uuid is not None:
            result['EcsUuid'] = self.ecs_uuid
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.ecs_status is not None:
            result['EcsStatus'] = self.ecs_status
        if self.plan_upgrade_status is not None:
            result['PlanUpgradeStatus'] = self.plan_upgrade_status
        if self.zone_no is not None:
            result['ZoneNo'] = self.zone_no
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.ecs_eip is not None:
            result['EcsEip'] = self.ecs_eip
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.ecs_internet_ip is not None:
            result['EcsInternetIp'] = self.ecs_internet_ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renewable is not None:
            result['Renewable'] = self.renewable
        if self.ecs_intranet_ip is not None:
            result['EcsIntranetIp'] = self.ecs_intranet_ip
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status
        if self.plan_upgradeable is not None:
            result['PlanUpgradeable'] = self.plan_upgradeable
        if self.custom_name is not None:
            result['CustomName'] = self.custom_name
        if self.ecs_network_type is not None:
            result['EcsNetworkType'] = self.ecs_network_type
        if self.public_access_control is not None:
            result['PublicAccessControl'] = self.public_access_control
        if self.vendor_code is not None:
            result['VendorCode'] = self.vendor_code
        if self.plan_name is not None:
            result['PlanName'] = self.plan_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('ImageVersionName') is not None:
            self.image_version_name = m.get('ImageVersionName')
        if m.get('PlanCode') is not None:
            self.plan_code = m.get('PlanCode')
        if m.get('EcsUuid') is not None:
            self.ecs_uuid = m.get('EcsUuid')
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('EcsStatus') is not None:
            self.ecs_status = m.get('EcsStatus')
        if m.get('PlanUpgradeStatus') is not None:
            self.plan_upgrade_status = m.get('PlanUpgradeStatus')
        if m.get('ZoneNo') is not None:
            self.zone_no = m.get('ZoneNo')
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('EcsEip') is not None:
            self.ecs_eip = m.get('EcsEip')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('EcsInternetIp') is not None:
            self.ecs_internet_ip = m.get('EcsInternetIp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Renewable') is not None:
            self.renewable = m.get('Renewable')
        if m.get('EcsIntranetIp') is not None:
            self.ecs_intranet_ip = m.get('EcsIntranetIp')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')
        if m.get('PlanUpgradeable') is not None:
            self.plan_upgradeable = m.get('PlanUpgradeable')
        if m.get('CustomName') is not None:
            self.custom_name = m.get('CustomName')
        if m.get('EcsNetworkType') is not None:
            self.ecs_network_type = m.get('EcsNetworkType')
        if m.get('PublicAccessControl') is not None:
            self.public_access_control = m.get('PublicAccessControl')
        if m.get('VendorCode') is not None:
            self.vendor_code = m.get('VendorCode')
        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeSyncInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_info: DescribeSyncInfoResponseBodyInstanceInfo = None,
    ):
        self.request_id = request_id
        self.instance_info = instance_info

    def validate(self):
        if self.instance_info:
            self.instance_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceInfo') is not None:
            temp_model = DescribeSyncInfoResponseBodyInstanceInfo()
            self.instance_info = temp_model.from_map(m['InstanceInfo'])
        return self


class DescribeSyncInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSyncInfoResponseBody = None,
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
            temp_model = DescribeSyncInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableLogMaskConfigsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mask_id_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mask_id_list = mask_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id_list is not None:
            result['MaskIdList'] = self.mask_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskIdList') is not None:
            self.mask_id_list = m.get('MaskIdList')
        return self


class DisableLogMaskConfigsResponseBody(TeaModel):
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


class DisableLogMaskConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableLogMaskConfigsResponseBody = None,
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
            temp_model = DisableLogMaskConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateRulesFromDbRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        json_param: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.json_param = json_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class DissociateRulesFromDbResponseBodyServerData(TeaModel):
    def __init__(
        self,
        json_result: str = None,
    ):
        self.json_result = json_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class DissociateRulesFromDbResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: DissociateRulesFromDbResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = DissociateRulesFromDbResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class DissociateRulesFromDbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DissociateRulesFromDbResponseBody = None,
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
            temp_model = DissociateRulesFromDbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateTemplatesFromRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        json_param: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.json_param = json_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.json_param is not None:
            result['JsonParam'] = self.json_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JsonParam') is not None:
            self.json_param = m.get('JsonParam')
        return self


class DissociateTemplatesFromRuleResponseBody(TeaModel):
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


class DissociateTemplatesFromRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DissociateTemplatesFromRuleResponseBody = None,
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
            temp_model = DissociateTemplatesFromRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditLogMaskConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mask_id: int = None,
        mask_name: str = None,
        mask_regex: str = None,
        mask_txt: str = None,
        mask_description: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mask_id = mask_id
        self.mask_name = mask_name
        self.mask_regex = mask_regex
        self.mask_txt = mask_txt
        self.mask_description = mask_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id is not None:
            result['MaskId'] = self.mask_id
        if self.mask_name is not None:
            result['MaskName'] = self.mask_name
        if self.mask_regex is not None:
            result['MaskRegex'] = self.mask_regex
        if self.mask_txt is not None:
            result['MaskTxt'] = self.mask_txt
        if self.mask_description is not None:
            result['MaskDescription'] = self.mask_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskId') is not None:
            self.mask_id = m.get('MaskId')
        if m.get('MaskName') is not None:
            self.mask_name = m.get('MaskName')
        if m.get('MaskRegex') is not None:
            self.mask_regex = m.get('MaskRegex')
        if m.get('MaskTxt') is not None:
            self.mask_txt = m.get('MaskTxt')
        if m.get('MaskDescription') is not None:
            self.mask_description = m.get('MaskDescription')
        return self


class EditLogMaskConfigResponseBody(TeaModel):
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


class EditLogMaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditLogMaskConfigResponseBody = None,
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
            temp_model = EditLogMaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableLogMaskConfigsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mask_id_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mask_id_list = mask_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id_list is not None:
            result['MaskIdList'] = self.mask_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskIdList') is not None:
            self.mask_id_list = m.get('MaskIdList')
        return self


class EnableLogMaskConfigsResponseBody(TeaModel):
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


class EnableLogMaskConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableLogMaskConfigsResponseBody = None,
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
            temp_model = EnableLogMaskConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentFileUrlRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAgentFileUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        linux_file_url: str = None,
        access_token: str = None,
        win_file_url: str = None,
    ):
        self.request_id = request_id
        self.linux_file_url = linux_file_url
        self.access_token = access_token
        self.win_file_url = win_file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.linux_file_url is not None:
            result['LinuxFileUrl'] = self.linux_file_url
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.win_file_url is not None:
            result['WinFileUrl'] = self.win_file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LinuxFileUrl') is not None:
            self.linux_file_url = m.get('LinuxFileUrl')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('WinFileUrl') is not None:
            self.win_file_url = m.get('WinFileUrl')
        return self


class GetAgentFileUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentFileUrlResponseBody = None,
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
            temp_model = GetAgentFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        agent_ip: str = None,
        agent_status: int = None,
        agent_os: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.agent_ip = agent_ip
        self.agent_status = agent_status
        self.agent_os = agent_os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_ip is not None:
            result['AgentIp'] = self.agent_ip
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.agent_os is not None:
            result['AgentOs'] = self.agent_os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentIp') is not None:
            self.agent_ip = m.get('AgentIp')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('AgentOs') is not None:
            self.agent_os = m.get('AgentOs')
        return self


class GetAgentListResponseBodyAgentList(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        private_ip: str = None,
        rmagent_mem: int = None,
        agent_id: str = None,
        rmagent_cpu: int = None,
        first_login_time: str = None,
        agent_os: str = None,
        agent_status: int = None,
        agent_port: str = None,
        agent_version: str = None,
        send_packets: int = None,
        send_bytes: int = None,
        last_active_time: str = None,
        send_packet_count: int = None,
        ecs_id: str = None,
        public_ip: str = None,
        send_byte_count: int = None,
    ):
        self.vpc_id = vpc_id
        self.private_ip = private_ip
        self.rmagent_mem = rmagent_mem
        self.agent_id = agent_id
        self.rmagent_cpu = rmagent_cpu
        self.first_login_time = first_login_time
        self.agent_os = agent_os
        self.agent_status = agent_status
        self.agent_port = agent_port
        self.agent_version = agent_version
        self.send_packets = send_packets
        self.send_bytes = send_bytes
        self.last_active_time = last_active_time
        self.send_packet_count = send_packet_count
        self.ecs_id = ecs_id
        self.public_ip = public_ip
        self.send_byte_count = send_byte_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip
        if self.rmagent_mem is not None:
            result['RmagentMem'] = self.rmagent_mem
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.rmagent_cpu is not None:
            result['RmagentCpu'] = self.rmagent_cpu
        if self.first_login_time is not None:
            result['FirstLoginTime'] = self.first_login_time
        if self.agent_os is not None:
            result['AgentOs'] = self.agent_os
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.agent_port is not None:
            result['AgentPort'] = self.agent_port
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.send_packets is not None:
            result['SendPackets'] = self.send_packets
        if self.send_bytes is not None:
            result['SendBytes'] = self.send_bytes
        if self.last_active_time is not None:
            result['LastActiveTime'] = self.last_active_time
        if self.send_packet_count is not None:
            result['SendPacketCount'] = self.send_packet_count
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        if self.send_byte_count is not None:
            result['SendByteCount'] = self.send_byte_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')
        if m.get('RmagentMem') is not None:
            self.rmagent_mem = m.get('RmagentMem')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('RmagentCpu') is not None:
            self.rmagent_cpu = m.get('RmagentCpu')
        if m.get('FirstLoginTime') is not None:
            self.first_login_time = m.get('FirstLoginTime')
        if m.get('AgentOs') is not None:
            self.agent_os = m.get('AgentOs')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('AgentPort') is not None:
            self.agent_port = m.get('AgentPort')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('SendPackets') is not None:
            self.send_packets = m.get('SendPackets')
        if m.get('SendBytes') is not None:
            self.send_bytes = m.get('SendBytes')
        if m.get('LastActiveTime') is not None:
            self.last_active_time = m.get('LastActiveTime')
        if m.get('SendPacketCount') is not None:
            self.send_packet_count = m.get('SendPacketCount')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        if m.get('SendByteCount') is not None:
            self.send_byte_count = m.get('SendByteCount')
        return self


class GetAgentListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        agent_list: List[GetAgentListResponseBodyAgentList] = None,
    ):
        self.request_id = request_id
        self.agent_list = agent_list

    def validate(self):
        if self.agent_list:
            for k in self.agent_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AgentList'] = []
        if self.agent_list is not None:
            for k in self.agent_list:
                result['AgentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.agent_list = []
        if m.get('AgentList') is not None:
            for k in m.get('AgentList'):
                temp_model = GetAgentListResponseBodyAgentList()
                self.agent_list.append(temp_model.from_map(k))
        return self


class GetAgentListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentListResponseBody = None,
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
            temp_model = GetAgentListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppointOperationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAppointOperationResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppointOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppointOperationResponseBody = None,
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
            temp_model = GetAppointOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditCountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetAuditCountResponseBody(TeaModel):
    def __init__(
        self,
        session_count: int = None,
        sql_count: int = None,
        risk_count: int = None,
        request_id: str = None,
    ):
        self.session_count = session_count
        self.sql_count = sql_count
        self.risk_count = risk_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuditCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuditCountResponseBody = None,
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
            temp_model = GetAuditCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditCountDistributionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetAuditCountDistributionResponseBodyTimeList(TeaModel):
    def __init__(
        self,
        session_count: int = None,
        begin_date: str = None,
        sql_count: int = None,
        end_date: str = None,
        risk_count: int = None,
    ):
        self.session_count = session_count
        self.begin_date = begin_date
        self.sql_count = sql_count
        self.end_date = end_date
        self.risk_count = risk_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        return self


class GetAuditCountDistributionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[GetAuditCountDistributionResponseBodyTimeList] = None,
    ):
        self.request_id = request_id
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetAuditCountDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetAuditCountDistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuditCountDistributionResponseBody = None,
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
            temp_model = GetAuditCountDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBaseTemplateListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetBaseTemplateListResponseBodyTemplateList(TeaModel):
    def __init__(
        self,
        db_type_name: str = None,
        template_content: str = None,
        sql_type_name: str = None,
        template_id: str = None,
        template_state: str = None,
    ):
        self.db_type_name = db_type_name
        self.template_content = template_content
        self.sql_type_name = sql_type_name
        self.template_id = template_id
        self.template_state = template_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.sql_type_name is not None:
            result['SqlTypeName'] = self.sql_type_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_state is not None:
            result['TemplateState'] = self.template_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('SqlTypeName') is not None:
            self.sql_type_name = m.get('SqlTypeName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateState') is not None:
            self.template_state = m.get('TemplateState')
        return self


class GetBaseTemplateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_list: List[GetBaseTemplateListResponseBodyTemplateList] = None,
    ):
        self.request_id = request_id
        self.template_list = template_list

    def validate(self):
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TemplateList'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['TemplateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_list = []
        if m.get('TemplateList') is not None:
            for k in m.get('TemplateList'):
                temp_model = GetBaseTemplateListResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k))
        return self


class GetBaseTemplateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetBaseTemplateListResponseBody = None,
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
            temp_model = GetBaseTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDasUsageRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDasUsageResponseBodyAuditAssetDbTypes(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        db_count: int = None,
    ):
        self.db_type = db_type
        self.db_count = db_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_count is not None:
            result['DbCount'] = self.db_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbCount') is not None:
            self.db_count = m.get('DbCount')
        return self


class GetDasUsageResponseBodyAuditAsset(TeaModel):
    def __init__(
        self,
        db_count: int = None,
        db_types: List[GetDasUsageResponseBodyAuditAssetDbTypes] = None,
    ):
        self.db_count = db_count
        self.db_types = db_types

    def validate(self):
        if self.db_types:
            for k in self.db_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_count is not None:
            result['DbCount'] = self.db_count
        result['DbTypes'] = []
        if self.db_types is not None:
            for k in self.db_types:
                result['DbTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbCount') is not None:
            self.db_count = m.get('DbCount')
        self.db_types = []
        if m.get('DbTypes') is not None:
            for k in m.get('DbTypes'):
                temp_model = GetDasUsageResponseBodyAuditAssetDbTypes()
                self.db_types.append(temp_model.from_map(k))
        return self


class GetDasUsageResponseBodyConsoleAccess(TeaModel):
    def __init__(
        self,
        last_access_time: str = None,
        day_90access_count: int = None,
        day_15access_count: int = None,
        day_30access_count: int = None,
        day_180access_count: int = None,
    ):
        self.last_access_time = last_access_time
        self.day_90access_count = day_90access_count
        self.day_15access_count = day_15access_count
        self.day_30access_count = day_30access_count
        self.day_180access_count = day_180access_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.day_90access_count is not None:
            result['Day90AccessCount'] = self.day_90access_count
        if self.day_15access_count is not None:
            result['Day15AccessCount'] = self.day_15access_count
        if self.day_30access_count is not None:
            result['Day30AccessCount'] = self.day_30access_count
        if self.day_180access_count is not None:
            result['Day180AccessCount'] = self.day_180access_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('Day90AccessCount') is not None:
            self.day_90access_count = m.get('Day90AccessCount')
        if m.get('Day15AccessCount') is not None:
            self.day_15access_count = m.get('Day15AccessCount')
        if m.get('Day30AccessCount') is not None:
            self.day_30access_count = m.get('Day30AccessCount')
        if m.get('Day180AccessCount') is not None:
            self.day_180access_count = m.get('Day180AccessCount')
        return self


class GetDasUsageResponseBodyAgent(TeaModel):
    def __init__(
        self,
        has_flow: bool = None,
        inst_state: str = None,
        active_count: int = None,
    ):
        self.has_flow = has_flow
        self.inst_state = inst_state
        self.active_count = active_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_flow is not None:
            result['HasFlow'] = self.has_flow
        if self.inst_state is not None:
            result['InstState'] = self.inst_state
        if self.active_count is not None:
            result['ActiveCount'] = self.active_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasFlow') is not None:
            self.has_flow = m.get('HasFlow')
        if m.get('InstState') is not None:
            self.inst_state = m.get('InstState')
        if m.get('ActiveCount') is not None:
            self.active_count = m.get('ActiveCount')
        return self


class GetDasUsageResponseBodyNoticeState(TeaModel):
    def __init__(
        self,
        risk_notice: bool = None,
        sys_notice: bool = None,
    ):
        self.risk_notice = risk_notice
        self.sys_notice = sys_notice

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_notice is not None:
            result['RiskNotice'] = self.risk_notice
        if self.sys_notice is not None:
            result['SysNotice'] = self.sys_notice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskNotice') is not None:
            self.risk_notice = m.get('RiskNotice')
        if m.get('SysNotice') is not None:
            self.sys_notice = m.get('SysNotice')
        return self


class GetDasUsageResponseBodyRiskAsset(TeaModel):
    def __init__(
        self,
        risk_dbcount: int = None,
        day_30risk_dbcount: int = None,
    ):
        self.risk_dbcount = risk_dbcount
        self.day_30risk_dbcount = day_30risk_dbcount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_dbcount is not None:
            result['RiskDBCount'] = self.risk_dbcount
        if self.day_30risk_dbcount is not None:
            result['Day30RiskDBCount'] = self.day_30risk_dbcount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskDBCount') is not None:
            self.risk_dbcount = m.get('RiskDBCount')
        if m.get('Day30RiskDBCount') is not None:
            self.day_30risk_dbcount = m.get('Day30RiskDBCount')
        return self


class GetDasUsageResponseBodyRiskRuleMaxHitRule(TeaModel):
    def __init__(
        self,
        count: int = None,
        rule_name: str = None,
    ):
        self.count = count
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetDasUsageResponseBodyRiskRuleDay30MaxHitRule(TeaModel):
    def __init__(
        self,
        count: int = None,
        rule_name: str = None,
    ):
        self.count = count
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetDasUsageResponseBodyRiskRule(TeaModel):
    def __init__(
        self,
        day_30risk_count: int = None,
        risk_count: int = None,
        max_hit_rule: GetDasUsageResponseBodyRiskRuleMaxHitRule = None,
        day_30max_hit_rule: GetDasUsageResponseBodyRiskRuleDay30MaxHitRule = None,
    ):
        self.day_30risk_count = day_30risk_count
        self.risk_count = risk_count
        self.max_hit_rule = max_hit_rule
        self.day_30max_hit_rule = day_30max_hit_rule

    def validate(self):
        if self.max_hit_rule:
            self.max_hit_rule.validate()
        if self.day_30max_hit_rule:
            self.day_30max_hit_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_30risk_count is not None:
            result['Day30RiskCount'] = self.day_30risk_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.max_hit_rule is not None:
            result['MaxHitRule'] = self.max_hit_rule.to_map()
        if self.day_30max_hit_rule is not None:
            result['Day30MaxHitRule'] = self.day_30max_hit_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day30RiskCount') is not None:
            self.day_30risk_count = m.get('Day30RiskCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('MaxHitRule') is not None:
            temp_model = GetDasUsageResponseBodyRiskRuleMaxHitRule()
            self.max_hit_rule = temp_model.from_map(m['MaxHitRule'])
        if m.get('Day30MaxHitRule') is not None:
            temp_model = GetDasUsageResponseBodyRiskRuleDay30MaxHitRule()
            self.day_30max_hit_rule = temp_model.from_map(m['Day30MaxHitRule'])
        return self


class GetDasUsageResponseBodyWpAsset(TeaModel):
    def __init__(
        self,
        avg_time: int = None,
        db_name: str = None,
    ):
        self.avg_time = avg_time
        self.db_name = db_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_time is not None:
            result['AvgTime'] = self.avg_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgTime') is not None:
            self.avg_time = m.get('AvgTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        return self


class GetDasUsageResponseBody(TeaModel):
    def __init__(
        self,
        over_1s_sql_count: int = None,
        request_id: str = None,
        session_total_count: int = None,
        create_time: str = None,
        sql_total_count: int = None,
        audit_asset: GetDasUsageResponseBodyAuditAsset = None,
        console_access: GetDasUsageResponseBodyConsoleAccess = None,
        agent: GetDasUsageResponseBodyAgent = None,
        notice_state: GetDasUsageResponseBodyNoticeState = None,
        risk_asset: GetDasUsageResponseBodyRiskAsset = None,
        risk_rule: GetDasUsageResponseBodyRiskRule = None,
        wp_asset: GetDasUsageResponseBodyWpAsset = None,
    ):
        self.over_1s_sql_count = over_1s_sql_count
        self.request_id = request_id
        self.session_total_count = session_total_count
        self.create_time = create_time
        self.sql_total_count = sql_total_count
        self.audit_asset = audit_asset
        self.console_access = console_access
        self.agent = agent
        self.notice_state = notice_state
        self.risk_asset = risk_asset
        self.risk_rule = risk_rule
        self.wp_asset = wp_asset

    def validate(self):
        if self.audit_asset:
            self.audit_asset.validate()
        if self.console_access:
            self.console_access.validate()
        if self.agent:
            self.agent.validate()
        if self.notice_state:
            self.notice_state.validate()
        if self.risk_asset:
            self.risk_asset.validate()
        if self.risk_rule:
            self.risk_rule.validate()
        if self.wp_asset:
            self.wp_asset.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.over_1s_sql_count is not None:
            result['Over1sSqlCount'] = self.over_1s_sql_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_total_count is not None:
            result['SessionTotalCount'] = self.session_total_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sql_total_count is not None:
            result['SqlTotalCount'] = self.sql_total_count
        if self.audit_asset is not None:
            result['AuditAsset'] = self.audit_asset.to_map()
        if self.console_access is not None:
            result['ConsoleAccess'] = self.console_access.to_map()
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()
        if self.notice_state is not None:
            result['NoticeState'] = self.notice_state.to_map()
        if self.risk_asset is not None:
            result['RiskAsset'] = self.risk_asset.to_map()
        if self.risk_rule is not None:
            result['RiskRule'] = self.risk_rule.to_map()
        if self.wp_asset is not None:
            result['WpAsset'] = self.wp_asset.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Over1sSqlCount') is not None:
            self.over_1s_sql_count = m.get('Over1sSqlCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionTotalCount') is not None:
            self.session_total_count = m.get('SessionTotalCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SqlTotalCount') is not None:
            self.sql_total_count = m.get('SqlTotalCount')
        if m.get('AuditAsset') is not None:
            temp_model = GetDasUsageResponseBodyAuditAsset()
            self.audit_asset = temp_model.from_map(m['AuditAsset'])
        if m.get('ConsoleAccess') is not None:
            temp_model = GetDasUsageResponseBodyConsoleAccess()
            self.console_access = temp_model.from_map(m['ConsoleAccess'])
        if m.get('Agent') is not None:
            temp_model = GetDasUsageResponseBodyAgent()
            self.agent = temp_model.from_map(m['Agent'])
        if m.get('NoticeState') is not None:
            temp_model = GetDasUsageResponseBodyNoticeState()
            self.notice_state = temp_model.from_map(m['NoticeState'])
        if m.get('RiskAsset') is not None:
            temp_model = GetDasUsageResponseBodyRiskAsset()
            self.risk_asset = temp_model.from_map(m['RiskAsset'])
        if m.get('RiskRule') is not None:
            temp_model = GetDasUsageResponseBodyRiskRule()
            self.risk_rule = temp_model.from_map(m['RiskRule'])
        if m.get('WpAsset') is not None:
            temp_model = GetDasUsageResponseBodyWpAsset()
            self.wp_asset = temp_model.from_map(m['WpAsset'])
        return self


class GetDasUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDasUsageResponseBody = None,
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
            temp_model = GetDasUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDBAuditCountListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetDBAuditCountListResponseBodyDbList(TeaModel):
    def __init__(
        self,
        session_count: int = None,
        db_id: int = None,
        db_name: str = None,
        db_type: int = None,
        sql_count: int = None,
        db_type_name: str = None,
        risk_count: int = None,
        db_version_name: str = None,
        asset_type: int = None,
        db_version: int = None,
        db_addresses: List[str] = None,
    ):
        self.session_count = session_count
        self.db_id = db_id
        self.db_name = db_name
        self.db_type = db_type
        self.sql_count = sql_count
        self.db_type_name = db_type_name
        self.risk_count = risk_count
        self.db_version_name = db_version_name
        self.asset_type = asset_type
        self.db_version = db_version
        self.db_addresses = db_addresses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_count is not None:
            result['SessionCount'] = self.session_count
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.db_version_name is not None:
            result['DbVersionName'] = self.db_version_name
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('DbVersionName') is not None:
            self.db_version_name = m.get('DbVersionName')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')
        return self


class GetDBAuditCountListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        db_list: List[GetDBAuditCountListResponseBodyDbList] = None,
    ):
        self.request_id = request_id
        self.db_list = db_list

    def validate(self):
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.db_list = []
        if m.get('DbList') is not None:
            for k in m.get('DbList'):
                temp_model = GetDBAuditCountListResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k))
        return self


class GetDBAuditCountListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDBAuditCountListResponseBody = None,
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
            temp_model = GetDBAuditCountListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupDetailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        group_key_id: str = None,
        group_type: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.group_key_id = group_key_id
        self.group_type = group_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_key_id is not None:
            result['GroupKeyId'] = self.group_key_id
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupKeyId') is not None:
            self.group_key_id = m.get('GroupKeyId')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        return self


class GetGroupDetailResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGroupDetailResponseBody = None,
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
            temp_model = GetGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLicenseRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLicenseResponseBody(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        request_id: str = None,
        asset_limit: int = None,
        asset_limit_used: int = None,
    ):
        self.start_time = start_time
        self.request_id = request_id
        self.asset_limit = asset_limit
        self.asset_limit_used = asset_limit_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.asset_limit is not None:
            result['AssetLimit'] = self.asset_limit
        if self.asset_limit_used is not None:
            result['AssetLimitUsed'] = self.asset_limit_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AssetLimit') is not None:
            self.asset_limit = m.get('AssetLimit')
        if m.get('AssetLimitUsed') is not None:
            self.asset_limit_used = m.get('AssetLimitUsed')
        return self


class GetLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLicenseResponseBody = None,
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
            temp_model = GetLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogDetailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        begin_date: str = None,
        end_date: str = None,
        sql_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.sql_id = sql_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        return self


class GetLogDetailResponseBody(TeaModel):
    def __init__(
        self,
        client_port: int = None,
        app_client_ip: str = None,
        exec_cost_us: int = None,
        session_logout_time: str = None,
        client_os_user: str = None,
        rule_id: int = None,
        request_id: str = None,
        sql_id: str = None,
        session_id: str = None,
        sql_type: str = None,
        app_username: str = None,
        risk_level: int = None,
        db_id: int = None,
        rule_type: int = None,
        rule_key_id: int = None,
        sql_result: str = None,
        affect_rows: int = None,
        sql_type_name: str = None,
        schema: str = None,
        session_login_time: str = None,
        db_user: str = None,
        server_mac: str = None,
        db_server: str = None,
        rule_name: str = None,
        response_code: str = None,
        sql_content: str = None,
        inst_name: str = None,
        template_content: str = None,
        client_program: str = None,
        capture_time: str = None,
        client_ip: str = None,
        client_mac: str = None,
        template_id: str = None,
        response_text: str = None,
        fetch_cost_us: int = None,
        template_rules: List[str] = None,
    ):
        self.client_port = client_port
        self.app_client_ip = app_client_ip
        self.exec_cost_us = exec_cost_us
        self.session_logout_time = session_logout_time
        self.client_os_user = client_os_user
        self.rule_id = rule_id
        self.request_id = request_id
        self.sql_id = sql_id
        self.session_id = session_id
        self.sql_type = sql_type
        self.app_username = app_username
        self.risk_level = risk_level
        self.db_id = db_id
        self.rule_type = rule_type
        self.rule_key_id = rule_key_id
        self.sql_result = sql_result
        self.affect_rows = affect_rows
        self.sql_type_name = sql_type_name
        self.schema = schema
        self.session_login_time = session_login_time
        self.db_user = db_user
        self.server_mac = server_mac
        self.db_server = db_server
        self.rule_name = rule_name
        self.response_code = response_code
        self.sql_content = sql_content
        self.inst_name = inst_name
        self.template_content = template_content
        self.client_program = client_program
        self.capture_time = capture_time
        self.client_ip = client_ip
        self.client_mac = client_mac
        self.template_id = template_id
        self.response_text = response_text
        self.fetch_cost_us = fetch_cost_us
        self.template_rules = template_rules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.app_client_ip is not None:
            result['AppClientIp'] = self.app_client_ip
        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us
        if self.session_logout_time is not None:
            result['SessionLogoutTime'] = self.session_logout_time
        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.app_username is not None:
            result['AppUsername'] = self.app_username
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_key_id is not None:
            result['RuleKeyId'] = self.rule_key_id
        if self.sql_result is not None:
            result['SqlResult'] = self.sql_result
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.sql_type_name is not None:
            result['SqlTypeName'] = self.sql_type_name
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.session_login_time is not None:
            result['SessionLoginTime'] = self.session_login_time
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac
        if self.db_server is not None:
            result['DbServer'] = self.db_server
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.sql_content is not None:
            result['SqlContent'] = self.sql_content
        if self.inst_name is not None:
            result['InstName'] = self.inst_name
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.response_text is not None:
            result['ResponseText'] = self.response_text
        if self.fetch_cost_us is not None:
            result['FetchCostUS'] = self.fetch_cost_us
        if self.template_rules is not None:
            result['TemplateRules'] = self.template_rules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('AppClientIp') is not None:
            self.app_client_ip = m.get('AppClientIp')
        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')
        if m.get('SessionLogoutTime') is not None:
            self.session_logout_time = m.get('SessionLogoutTime')
        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('AppUsername') is not None:
            self.app_username = m.get('AppUsername')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleKeyId') is not None:
            self.rule_key_id = m.get('RuleKeyId')
        if m.get('SqlResult') is not None:
            self.sql_result = m.get('SqlResult')
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('SqlTypeName') is not None:
            self.sql_type_name = m.get('SqlTypeName')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('SessionLoginTime') is not None:
            self.session_login_time = m.get('SessionLoginTime')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')
        if m.get('DbServer') is not None:
            self.db_server = m.get('DbServer')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('SqlContent') is not None:
            self.sql_content = m.get('SqlContent')
        if m.get('InstName') is not None:
            self.inst_name = m.get('InstName')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('ResponseText') is not None:
            self.response_text = m.get('ResponseText')
        if m.get('FetchCostUS') is not None:
            self.fetch_cost_us = m.get('FetchCostUS')
        if m.get('TemplateRules') is not None:
            self.template_rules = m.get('TemplateRules')
        return self


class GetLogDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogDetailResponseBody = None,
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
            temp_model = GetLogDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        sql_id: str = None,
        sql_key: str = None,
        session_id: str = None,
        template_id: str = None,
        is_success: str = None,
        min_affect_rows: int = None,
        max_affect_rows: int = None,
        min_exec_cost_us: int = None,
        max_exec_cost_us: int = None,
        rule_name: str = None,
        client_ip_list: List[str] = None,
        db_user_list: List[str] = None,
        db_host_list: List[str] = None,
        risk_level_list: List[str] = None,
        rule_type_list: List[str] = None,
        sql_type_list: List[str] = None,
        client_program_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.page_number = page_number
        self.page_size = page_size
        self.sql_id = sql_id
        self.sql_key = sql_key
        self.session_id = session_id
        self.template_id = template_id
        self.is_success = is_success
        self.min_affect_rows = min_affect_rows
        self.max_affect_rows = max_affect_rows
        self.min_exec_cost_us = min_exec_cost_us
        self.max_exec_cost_us = max_exec_cost_us
        self.rule_name = rule_name
        self.client_ip_list = client_ip_list
        self.db_user_list = db_user_list
        self.db_host_list = db_host_list
        self.risk_level_list = risk_level_list
        self.rule_type_list = rule_type_list
        self.sql_type_list = sql_type_list
        self.client_program_list = client_program_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_key is not None:
            result['SqlKey'] = self.sql_key
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.min_affect_rows is not None:
            result['MinAffectRows'] = self.min_affect_rows
        if self.max_affect_rows is not None:
            result['MaxAffectRows'] = self.max_affect_rows
        if self.min_exec_cost_us is not None:
            result['MinExecCostUS'] = self.min_exec_cost_us
        if self.max_exec_cost_us is not None:
            result['MaxExecCostUS'] = self.max_exec_cost_us
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list
        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list
        if self.db_host_list is not None:
            result['DbHostList'] = self.db_host_list
        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list
        if self.rule_type_list is not None:
            result['RuleTypeList'] = self.rule_type_list
        if self.sql_type_list is not None:
            result['SqlTypeList'] = self.sql_type_list
        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlKey') is not None:
            self.sql_key = m.get('SqlKey')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('MinAffectRows') is not None:
            self.min_affect_rows = m.get('MinAffectRows')
        if m.get('MaxAffectRows') is not None:
            self.max_affect_rows = m.get('MaxAffectRows')
        if m.get('MinExecCostUS') is not None:
            self.min_exec_cost_us = m.get('MinExecCostUS')
        if m.get('MaxExecCostUS') is not None:
            self.max_exec_cost_us = m.get('MaxExecCostUS')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')
        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')
        if m.get('DbHostList') is not None:
            self.db_host_list = m.get('DbHostList')
        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')
        if m.get('RuleTypeList') is not None:
            self.rule_type_list = m.get('RuleTypeList')
        if m.get('SqlTypeList') is not None:
            self.sql_type_list = m.get('SqlTypeList')
        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')
        return self


class GetLogListResponseBodyResults(TeaModel):
    def __init__(
        self,
        client_port: int = None,
        exec_cost_us: int = None,
        app_client_ip: str = None,
        session_logout_time: str = None,
        client_os_user: str = None,
        rule_id: int = None,
        sql_id: str = None,
        session_id: str = None,
        sql_type: str = None,
        risk_level: int = None,
        app_username: str = None,
        db_id: int = None,
        rule_type: int = None,
        rule_key_id: int = None,
        affect_rows: int = None,
        schema: str = None,
        session_login_time: str = None,
        db_user: str = None,
        server_mac: str = None,
        db_server: str = None,
        rule_name: str = None,
        sql_content: str = None,
        response_code: str = None,
        inst_name: str = None,
        client_program: str = None,
        capture_time: str = None,
        client_ip: str = None,
        client_mac: str = None,
        template_id: str = None,
        fetch_cost_us: int = None,
        response_text: str = None,
    ):
        self.client_port = client_port
        self.exec_cost_us = exec_cost_us
        self.app_client_ip = app_client_ip
        self.session_logout_time = session_logout_time
        self.client_os_user = client_os_user
        self.rule_id = rule_id
        self.sql_id = sql_id
        self.session_id = session_id
        self.sql_type = sql_type
        self.risk_level = risk_level
        self.app_username = app_username
        self.db_id = db_id
        self.rule_type = rule_type
        self.rule_key_id = rule_key_id
        self.affect_rows = affect_rows
        self.schema = schema
        self.session_login_time = session_login_time
        self.db_user = db_user
        self.server_mac = server_mac
        self.db_server = db_server
        self.rule_name = rule_name
        self.sql_content = sql_content
        self.response_code = response_code
        self.inst_name = inst_name
        self.client_program = client_program
        self.capture_time = capture_time
        self.client_ip = client_ip
        self.client_mac = client_mac
        self.template_id = template_id
        self.fetch_cost_us = fetch_cost_us
        self.response_text = response_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us
        if self.app_client_ip is not None:
            result['AppClientIp'] = self.app_client_ip
        if self.session_logout_time is not None:
            result['SessionLogoutTime'] = self.session_logout_time
        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.app_username is not None:
            result['AppUsername'] = self.app_username
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_key_id is not None:
            result['RuleKeyId'] = self.rule_key_id
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.session_login_time is not None:
            result['SessionLoginTime'] = self.session_login_time
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac
        if self.db_server is not None:
            result['DbServer'] = self.db_server
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.sql_content is not None:
            result['SqlContent'] = self.sql_content
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.inst_name is not None:
            result['InstName'] = self.inst_name
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.fetch_cost_us is not None:
            result['FetchCostUS'] = self.fetch_cost_us
        if self.response_text is not None:
            result['ResponseText'] = self.response_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')
        if m.get('AppClientIp') is not None:
            self.app_client_ip = m.get('AppClientIp')
        if m.get('SessionLogoutTime') is not None:
            self.session_logout_time = m.get('SessionLogoutTime')
        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('AppUsername') is not None:
            self.app_username = m.get('AppUsername')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleKeyId') is not None:
            self.rule_key_id = m.get('RuleKeyId')
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('SessionLoginTime') is not None:
            self.session_login_time = m.get('SessionLoginTime')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')
        if m.get('DbServer') is not None:
            self.db_server = m.get('DbServer')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SqlContent') is not None:
            self.sql_content = m.get('SqlContent')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('InstName') is not None:
            self.inst_name = m.get('InstName')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FetchCostUS') is not None:
            self.fetch_cost_us = m.get('FetchCostUS')
        if m.get('ResponseText') is not None:
            self.response_text = m.get('ResponseText')
        return self


class GetLogListResponseBody(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        request_id: str = None,
        begin_date: str = None,
        incomplete: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        results: List[GetLogListResponseBodyResults] = None,
    ):
        self.end_date = end_date
        self.request_id = request_id
        self.begin_date = begin_date
        self.incomplete = incomplete
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.incomplete is not None:
            result['Incomplete'] = self.incomplete
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('Incomplete') is not None:
            self.incomplete = m.get('Incomplete')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetLogListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetLogListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogListResponseBody = None,
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
            temp_model = GetLogListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogMaskConfigsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mask_name: str = None,
        mask_type: int = None,
        mask_state: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mask_name = mask_name
        self.mask_type = mask_type
        self.mask_state = mask_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_name is not None:
            result['MaskName'] = self.mask_name
        if self.mask_type is not None:
            result['MaskType'] = self.mask_type
        if self.mask_state is not None:
            result['MaskState'] = self.mask_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskName') is not None:
            self.mask_name = m.get('MaskName')
        if m.get('MaskType') is not None:
            self.mask_type = m.get('MaskType')
        if m.get('MaskState') is not None:
            self.mask_state = m.get('MaskState')
        return self


class GetLogMaskConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        mask_description: str = None,
        mask_state: int = None,
        mask_name: str = None,
        mask_regex: str = None,
        mask_txt: str = None,
        mask_id: int = None,
        mask_type: int = None,
    ):
        self.mask_description = mask_description
        self.mask_state = mask_state
        self.mask_name = mask_name
        self.mask_regex = mask_regex
        self.mask_txt = mask_txt
        self.mask_id = mask_id
        self.mask_type = mask_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mask_description is not None:
            result['MaskDescription'] = self.mask_description
        if self.mask_state is not None:
            result['MaskState'] = self.mask_state
        if self.mask_name is not None:
            result['MaskName'] = self.mask_name
        if self.mask_regex is not None:
            result['MaskRegex'] = self.mask_regex
        if self.mask_txt is not None:
            result['MaskTxt'] = self.mask_txt
        if self.mask_id is not None:
            result['MaskId'] = self.mask_id
        if self.mask_type is not None:
            result['MaskType'] = self.mask_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaskDescription') is not None:
            self.mask_description = m.get('MaskDescription')
        if m.get('MaskState') is not None:
            self.mask_state = m.get('MaskState')
        if m.get('MaskName') is not None:
            self.mask_name = m.get('MaskName')
        if m.get('MaskRegex') is not None:
            self.mask_regex = m.get('MaskRegex')
        if m.get('MaskTxt') is not None:
            self.mask_txt = m.get('MaskTxt')
        if m.get('MaskId') is not None:
            self.mask_id = m.get('MaskId')
        if m.get('MaskType') is not None:
            self.mask_type = m.get('MaskType')
        return self


class GetLogMaskConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        configs: List[GetLogMaskConfigsResponseBodyConfigs] = None,
    ):
        self.request_id = request_id
        self.configs = configs

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = GetLogMaskConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        return self


class GetLogMaskConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogMaskConfigsResponseBody = None,
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
            temp_model = GetLogMaskConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogQueryConditionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
        is_risk: str = None,
        is_success: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.is_risk = is_risk
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.is_risk is not None:
            result['IsRisk'] = self.is_risk
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('IsRisk') is not None:
            self.is_risk = m.get('IsRisk')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetLogQueryConditionResponseBodySqlTypeList(TeaModel):
    def __init__(
        self,
        sql_keyword: str = None,
        sql_type: str = None,
    ):
        self.sql_keyword = sql_keyword
        self.sql_type = sql_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sql_keyword is not None:
            result['SqlKeyword'] = self.sql_keyword
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SqlKeyword') is not None:
            self.sql_keyword = m.get('SqlKeyword')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class GetLogQueryConditionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        db_user_list: List[str] = None,
        client_ip_list: List[str] = None,
        client_program_list: List[str] = None,
        db_server_list: List[str] = None,
        sql_type_list: List[GetLogQueryConditionResponseBodySqlTypeList] = None,
    ):
        self.request_id = request_id
        self.db_user_list = db_user_list
        self.client_ip_list = client_ip_list
        self.client_program_list = client_program_list
        self.db_server_list = db_server_list
        self.sql_type_list = sql_type_list

    def validate(self):
        if self.sql_type_list:
            for k in self.sql_type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list
        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list
        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list
        if self.db_server_list is not None:
            result['DbServerList'] = self.db_server_list
        result['SqlTypeList'] = []
        if self.sql_type_list is not None:
            for k in self.sql_type_list:
                result['SqlTypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')
        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')
        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')
        if m.get('DbServerList') is not None:
            self.db_server_list = m.get('DbServerList')
        self.sql_type_list = []
        if m.get('SqlTypeList') is not None:
            for k in m.get('SqlTypeList'):
                temp_model = GetLogQueryConditionResponseBodySqlTypeList()
                self.sql_type_list.append(temp_model.from_map(k))
        return self


class GetLogQueryConditionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogQueryConditionResponseBody = None,
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
            temp_model = GetLogQueryConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogStatisticsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
        by_db_id: int = None,
        by_client_ip: int = None,
        by_db_user: int = None,
        by_db_server: int = None,
        by_client_program: int = None,
        by_sql_type: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.by_db_id = by_db_id
        self.by_client_ip = by_client_ip
        self.by_db_user = by_db_user
        self.by_db_server = by_db_server
        self.by_client_program = by_client_program
        self.by_sql_type = by_sql_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.by_db_id is not None:
            result['ByDbId'] = self.by_db_id
        if self.by_client_ip is not None:
            result['ByClientIp'] = self.by_client_ip
        if self.by_db_user is not None:
            result['ByDbUser'] = self.by_db_user
        if self.by_db_server is not None:
            result['ByDbServer'] = self.by_db_server
        if self.by_client_program is not None:
            result['ByClientProgram'] = self.by_client_program
        if self.by_sql_type is not None:
            result['BySqlType'] = self.by_sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ByDbId') is not None:
            self.by_db_id = m.get('ByDbId')
        if m.get('ByClientIp') is not None:
            self.by_client_ip = m.get('ByClientIp')
        if m.get('ByDbUser') is not None:
            self.by_db_user = m.get('ByDbUser')
        if m.get('ByDbServer') is not None:
            self.by_db_server = m.get('ByDbServer')
        if m.get('ByClientProgram') is not None:
            self.by_client_program = m.get('ByClientProgram')
        if m.get('BySqlType') is not None:
            self.by_sql_type = m.get('BySqlType')
        return self


class GetLogStatisticsResponseBodyCountList(TeaModel):
    def __init__(
        self,
        sql_keyword: str = None,
        db_id: int = None,
        db_name: str = None,
        client_program: str = None,
        db_user: str = None,
        client_ip: str = None,
        sql_count: int = None,
        risk_count: int = None,
        db_server: str = None,
        sql_type: str = None,
    ):
        self.sql_keyword = sql_keyword
        self.db_id = db_id
        self.db_name = db_name
        self.client_program = client_program
        self.db_user = db_user
        self.client_ip = client_ip
        self.sql_count = sql_count
        self.risk_count = risk_count
        self.db_server = db_server
        self.sql_type = sql_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sql_keyword is not None:
            result['SqlKeyword'] = self.sql_keyword
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.db_server is not None:
            result['DbServer'] = self.db_server
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SqlKeyword') is not None:
            self.sql_keyword = m.get('SqlKeyword')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('DbServer') is not None:
            self.db_server = m.get('DbServer')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class GetLogStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        count_list: List[GetLogStatisticsResponseBodyCountList] = None,
    ):
        self.request_id = request_id
        self.count_list = count_list

    def validate(self):
        if self.count_list:
            for k in self.count_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CountList'] = []
        if self.count_list is not None:
            for k in self.count_list:
                result['CountList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.count_list = []
        if m.get('CountList') is not None:
            for k in m.get('CountList'):
                temp_model = GetLogStatisticsResponseBodyCountList()
                self.count_list.append(temp_model.from_map(k))
        return self


class GetLogStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogStatisticsResponseBody = None,
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
            temp_model = GetLogStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogTopDistributionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetLogTopDistributionResponseBodyTimeList(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        sql_count: int = None,
        end_date: str = None,
        top_time: str = None,
    ):
        self.begin_date = begin_date
        self.sql_count = sql_count
        self.end_date = end_date
        self.top_time = top_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.top_time is not None:
            result['TopTime'] = self.top_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('TopTime') is not None:
            self.top_time = m.get('TopTime')
        return self


class GetLogTopDistributionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[GetLogTopDistributionResponseBodyTimeList] = None,
    ):
        self.request_id = request_id
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetLogTopDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetLogTopDistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogTopDistributionResponseBody = None,
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
            temp_model = GetLogTopDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogTopStatisticsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        top_time: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.top_time = top_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.top_time is not None:
            result['TopTime'] = self.top_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('TopTime') is not None:
            self.top_time = m.get('TopTime')
        return self


class GetLogTopStatisticsResponseBodyCountList(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        db_user: str = None,
        sql_count: int = None,
        client_program: str = None,
    ):
        self.client_ip = client_ip
        self.db_user = db_user
        self.sql_count = sql_count
        self.client_program = client_program

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        return self


class GetLogTopStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        count_list: List[GetLogTopStatisticsResponseBodyCountList] = None,
    ):
        self.request_id = request_id
        self.count_list = count_list

    def validate(self):
        if self.count_list:
            for k in self.count_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CountList'] = []
        if self.count_list is not None:
            for k in self.count_list:
                result['CountList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.count_list = []
        if m.get('CountList') is not None:
            for k in m.get('CountList'):
                temp_model = GetLogTopStatisticsResponseBodyCountList()
                self.count_list.append(temp_model.from_map(k))
        return self


class GetLogTopStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogTopStatisticsResponseBody = None,
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
            temp_model = GetLogTopStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLogTypeDistributionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetLogTypeDistributionResponseBodyTimeList(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        exec_cost_us: str = None,
        insert_sql_count: int = None,
        select_sql_count: int = None,
        delete_sql_count: int = None,
        begin_date: str = None,
        other_sql_count: int = None,
        sql_count: int = None,
        update_sql_count: int = None,
    ):
        self.end_date = end_date
        self.exec_cost_us = exec_cost_us
        self.insert_sql_count = insert_sql_count
        self.select_sql_count = select_sql_count
        self.delete_sql_count = delete_sql_count
        self.begin_date = begin_date
        self.other_sql_count = other_sql_count
        self.sql_count = sql_count
        self.update_sql_count = update_sql_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us
        if self.insert_sql_count is not None:
            result['InsertSqlCount'] = self.insert_sql_count
        if self.select_sql_count is not None:
            result['SelectSqlCount'] = self.select_sql_count
        if self.delete_sql_count is not None:
            result['DeleteSqlCount'] = self.delete_sql_count
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.other_sql_count is not None:
            result['OtherSqlCount'] = self.other_sql_count
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.update_sql_count is not None:
            result['UpdateSqlCount'] = self.update_sql_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')
        if m.get('InsertSqlCount') is not None:
            self.insert_sql_count = m.get('InsertSqlCount')
        if m.get('SelectSqlCount') is not None:
            self.select_sql_count = m.get('SelectSqlCount')
        if m.get('DeleteSqlCount') is not None:
            self.delete_sql_count = m.get('DeleteSqlCount')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('OtherSqlCount') is not None:
            self.other_sql_count = m.get('OtherSqlCount')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('UpdateSqlCount') is not None:
            self.update_sql_count = m.get('UpdateSqlCount')
        return self


class GetLogTypeDistributionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[GetLogTypeDistributionResponseBodyTimeList] = None,
    ):
        self.request_id = request_id
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetLogTypeDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetLogTypeDistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLogTypeDistributionResponseBody = None,
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
            temp_model = GetLogTypeDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNewSqlTemplateListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        template_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.page_number = page_number
        self.page_size = page_size
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetNewSqlTemplateListResponseBodyResults(TeaModel):
    def __init__(
        self,
        template_content: str = None,
        template_id: str = None,
        first_capture_time: str = None,
    ):
        self.template_content = template_content
        self.template_id = template_id
        self.first_capture_time = first_capture_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.first_capture_time is not None:
            result['FirstCaptureTime'] = self.first_capture_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('FirstCaptureTime') is not None:
            self.first_capture_time = m.get('FirstCaptureTime')
        return self


class GetNewSqlTemplateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        results: List[GetNewSqlTemplateListResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetNewSqlTemplateListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetNewSqlTemplateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNewSqlTemplateListResponseBody = None,
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
            temp_model = GetNewSqlTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReportFileUrlRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        file_name: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GetReportFileUrlResponseBodyServerData(TeaModel):
    def __init__(
        self,
        file_url: str = None,
    ):
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetReportFileUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: GetReportFileUrlResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = GetReportFileUrlResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class GetReportFileUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetReportFileUrlResponseBody = None,
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
            temp_model = GetReportFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRiskLevelDistributionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetRiskLevelDistributionResponseBodyTimeList(TeaModel):
    def __init__(
        self,
        middle_risk_count: int = None,
        high_risk_count: int = None,
        end_date: str = None,
        begin_date: str = None,
        risk_count: int = None,
        low_risk_count: int = None,
    ):
        self.middle_risk_count = middle_risk_count
        self.high_risk_count = high_risk_count
        self.end_date = end_date
        self.begin_date = begin_date
        self.risk_count = risk_count
        self.low_risk_count = low_risk_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.middle_risk_count is not None:
            result['MiddleRiskCount'] = self.middle_risk_count
        if self.high_risk_count is not None:
            result['HighRiskCount'] = self.high_risk_count
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.low_risk_count is not None:
            result['LowRiskCount'] = self.low_risk_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MiddleRiskCount') is not None:
            self.middle_risk_count = m.get('MiddleRiskCount')
        if m.get('HighRiskCount') is not None:
            self.high_risk_count = m.get('HighRiskCount')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('LowRiskCount') is not None:
            self.low_risk_count = m.get('LowRiskCount')
        return self


class GetRiskLevelDistributionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[GetRiskLevelDistributionResponseBodyTimeList] = None,
    ):
        self.request_id = request_id
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetRiskLevelDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetRiskLevelDistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRiskLevelDistributionResponseBody = None,
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
            temp_model = GetRiskLevelDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRiskStatisticsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
        by_db_id: int = None,
        by_risk_level: int = None,
        by_rule_type: int = None,
        by_rule_id: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.by_db_id = by_db_id
        self.by_risk_level = by_risk_level
        self.by_rule_type = by_rule_type
        self.by_rule_id = by_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.by_db_id is not None:
            result['ByDbId'] = self.by_db_id
        if self.by_risk_level is not None:
            result['ByRiskLevel'] = self.by_risk_level
        if self.by_rule_type is not None:
            result['ByRuleType'] = self.by_rule_type
        if self.by_rule_id is not None:
            result['ByRuleId'] = self.by_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ByDbId') is not None:
            self.by_db_id = m.get('ByDbId')
        if m.get('ByRiskLevel') is not None:
            self.by_risk_level = m.get('ByRiskLevel')
        if m.get('ByRuleType') is not None:
            self.by_rule_type = m.get('ByRuleType')
        if m.get('ByRuleId') is not None:
            self.by_rule_id = m.get('ByRuleId')
        return self


class GetRiskStatisticsResponseBodyTimeList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        db_id: int = None,
        db_name: str = None,
        rule_type: int = None,
        last_capture_time: str = None,
        risk_count: int = None,
        rule_name: str = None,
        rule_id: str = None,
    ):
        self.risk_level = risk_level
        self.db_id = db_id
        self.db_name = db_name
        self.rule_type = rule_type
        self.last_capture_time = last_capture_time
        self.risk_count = risk_count
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.last_capture_time is not None:
            result['LastCaptureTime'] = self.last_capture_time
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('LastCaptureTime') is not None:
            self.last_capture_time = m.get('LastCaptureTime')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetRiskStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[GetRiskStatisticsResponseBodyTimeList] = None,
    ):
        self.request_id = request_id
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetRiskStatisticsResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetRiskStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRiskStatisticsResponseBody = None,
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
            temp_model = GetRiskStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleDetailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        rule_id: int = None,
        rule_key_id: int = None,
        db_id: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.rule_id = rule_id
        self.rule_key_id = rule_key_id
        self.db_id = db_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_key_id is not None:
            result['RuleKeyId'] = self.rule_key_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleKeyId') is not None:
            self.rule_key_id = m.get('RuleKeyId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        return self


class GetRuleDetailResponseBodyServerData(TeaModel):
    def __init__(
        self,
        json_result: str = None,
    ):
        self.json_result = json_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class GetRuleDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: GetRuleDetailResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = GetRuleDetailResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class GetRuleDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRuleDetailResponseBody = None,
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
            temp_model = GetRuleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRuleGroupNameRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        group_name: str = None,
        group_type: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.group_name = group_name
        self.group_type = group_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        return self


class GetRuleGroupNameResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRuleGroupNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRuleGroupNameResponseBody = None,
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
            temp_model = GetRuleGroupNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionDetailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        session_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GetSessionDetailResponseBody(TeaModel):
    def __init__(
        self,
        login_time: str = None,
        db_id: int = None,
        login_code: int = None,
        client_port: int = None,
        login_message: str = None,
        db_user: str = None,
        logout_time: str = None,
        server_port: int = None,
        client_os_user: str = None,
        server_mac: str = None,
        request_id: str = None,
        client_program: str = None,
        client_ip: str = None,
        server_ip: str = None,
        session_id: str = None,
        client_mac: str = None,
    ):
        self.login_time = login_time
        self.db_id = db_id
        self.login_code = login_code
        self.client_port = client_port
        self.login_message = login_message
        self.db_user = db_user
        self.logout_time = logout_time
        self.server_port = server_port
        self.client_os_user = client_os_user
        self.server_mac = server_mac
        self.request_id = request_id
        self.client_program = client_program
        self.client_ip = client_ip
        self.server_ip = server_ip
        self.session_id = session_id
        self.client_mac = client_mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_time is not None:
            result['LoginTime'] = self.login_time
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.login_code is not None:
            result['LoginCode'] = self.login_code
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.login_message is not None:
            result['LoginMessage'] = self.login_message
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.logout_time is not None:
            result['LogoutTime'] = self.logout_time
        if self.server_port is not None:
            result['ServerPort'] = self.server_port
        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user
        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginTime') is not None:
            self.login_time = m.get('LoginTime')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('LoginCode') is not None:
            self.login_code = m.get('LoginCode')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('LoginMessage') is not None:
            self.login_message = m.get('LoginMessage')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('LogoutTime') is not None:
            self.logout_time = m.get('LogoutTime')
        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')
        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')
        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')
        return self


class GetSessionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSessionDetailResponseBody = None,
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
            temp_model = GetSessionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionDistributionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetSessionDistributionResponseBodyTimeList(TeaModel):
    def __init__(
        self,
        begin_date: str = None,
        login_session_count: int = None,
        active_session_count: int = None,
        end_date: str = None,
        error_session_count: int = None,
    ):
        self.begin_date = begin_date
        self.login_session_count = login_session_count
        self.active_session_count = active_session_count
        self.end_date = end_date
        self.error_session_count = error_session_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.login_session_count is not None:
            result['LoginSessionCount'] = self.login_session_count
        if self.active_session_count is not None:
            result['ActiveSessionCount'] = self.active_session_count
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.error_session_count is not None:
            result['ErrorSessionCount'] = self.error_session_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('LoginSessionCount') is not None:
            self.login_session_count = m.get('LoginSessionCount')
        if m.get('ActiveSessionCount') is not None:
            self.active_session_count = m.get('ActiveSessionCount')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ErrorSessionCount') is not None:
            self.error_session_count = m.get('ErrorSessionCount')
        return self


class GetSessionDistributionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_list: List[GetSessionDistributionResponseBodyTimeList] = None,
    ):
        self.request_id = request_id
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = GetSessionDistributionResponseBodyTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class GetSessionDistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSessionDistributionResponseBody = None,
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
            temp_model = GetSessionDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        session_id: str = None,
        action_list: List[str] = None,
        client_ip_list: List[str] = None,
        db_user_list: List[str] = None,
        db_host_list: List[str] = None,
        client_program_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.page_number = page_number
        self.page_size = page_size
        self.session_id = session_id
        self.action_list = action_list
        self.client_ip_list = client_ip_list
        self.db_user_list = db_user_list
        self.db_host_list = db_host_list
        self.client_program_list = client_program_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.action_list is not None:
            result['ActionList'] = self.action_list
        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list
        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list
        if self.db_host_list is not None:
            result['DbHostList'] = self.db_host_list
        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('ActionList') is not None:
            self.action_list = m.get('ActionList')
        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')
        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')
        if m.get('DbHostList') is not None:
            self.db_host_list = m.get('DbHostList')
        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')
        return self


class GetSessionListResponseBodyResults(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        login_code: int = None,
        action: str = None,
        client_port: int = None,
        login_message: str = None,
        db_user: str = None,
        server_port: int = None,
        client_os_user: str = None,
        server_mac: str = None,
        client_program: str = None,
        capture_time: str = None,
        client_ip: str = None,
        server_ip: str = None,
        session_id: str = None,
        client_mac: str = None,
    ):
        self.db_id = db_id
        self.login_code = login_code
        self.action = action
        self.client_port = client_port
        self.login_message = login_message
        self.db_user = db_user
        self.server_port = server_port
        self.client_os_user = client_os_user
        self.server_mac = server_mac
        self.client_program = client_program
        self.capture_time = capture_time
        self.client_ip = client_ip
        self.server_ip = server_ip
        self.session_id = session_id
        self.client_mac = client_mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.login_code is not None:
            result['LoginCode'] = self.login_code
        if self.action is not None:
            result['Action'] = self.action
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.login_message is not None:
            result['LoginMessage'] = self.login_message
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.server_port is not None:
            result['ServerPort'] = self.server_port
        if self.client_os_user is not None:
            result['ClientOsUser'] = self.client_os_user
        if self.server_mac is not None:
            result['ServerMac'] = self.server_mac
        if self.client_program is not None:
            result['ClientProgram'] = self.client_program
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.client_mac is not None:
            result['ClientMac'] = self.client_mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('LoginCode') is not None:
            self.login_code = m.get('LoginCode')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('LoginMessage') is not None:
            self.login_message = m.get('LoginMessage')
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')
        if m.get('ClientOsUser') is not None:
            self.client_os_user = m.get('ClientOsUser')
        if m.get('ServerMac') is not None:
            self.server_mac = m.get('ServerMac')
        if m.get('ClientProgram') is not None:
            self.client_program = m.get('ClientProgram')
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('ClientMac') is not None:
            self.client_mac = m.get('ClientMac')
        return self


class GetSessionListResponseBody(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        request_id: str = None,
        begin_date: str = None,
        incomplete: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        results: List[GetSessionListResponseBodyResults] = None,
    ):
        self.end_date = end_date
        self.request_id = request_id
        self.begin_date = begin_date
        self.incomplete = incomplete
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.incomplete is not None:
            result['Incomplete'] = self.incomplete
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('Incomplete') is not None:
            self.incomplete = m.get('Incomplete')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetSessionListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetSessionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSessionListResponseBody = None,
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
            temp_model = GetSessionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionQueryConditionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GetSessionQueryConditionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        db_user_list: List[str] = None,
        client_ip_list: List[str] = None,
        client_program_list: List[str] = None,
        db_server_list: List[str] = None,
    ):
        self.request_id = request_id
        self.db_user_list = db_user_list
        self.client_ip_list = client_ip_list
        self.client_program_list = client_program_list
        self.db_server_list = db_server_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.db_user_list is not None:
            result['DbUserList'] = self.db_user_list
        if self.client_ip_list is not None:
            result['ClientIpList'] = self.client_ip_list
        if self.client_program_list is not None:
            result['ClientProgramList'] = self.client_program_list
        if self.db_server_list is not None:
            result['DbServerList'] = self.db_server_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DbUserList') is not None:
            self.db_user_list = m.get('DbUserList')
        if m.get('ClientIpList') is not None:
            self.client_ip_list = m.get('ClientIpList')
        if m.get('ClientProgramList') is not None:
            self.client_program_list = m.get('ClientProgramList')
        if m.get('DbServerList') is not None:
            self.db_server_list = m.get('DbServerList')
        return self


class GetSessionQueryConditionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSessionQueryConditionResponseBody = None,
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
            temp_model = GetSessionQueryConditionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlTemplateListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        sql_id: str = None,
        template_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.page_number = page_number
        self.page_size = page_size
        self.sql_id = sql_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetSqlTemplateListResponseBodyResultsRuleList(TeaModel):
    def __init__(
        self,
        risk_level: int = None,
        rule_state: int = None,
        db_id: int = None,
        rule_name: str = None,
        rule_id: str = None,
    ):
        self.risk_level = risk_level
        self.rule_state = rule_state
        self.db_id = db_id
        self.rule_name = rule_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rule_state is not None:
            result['RuleState'] = self.rule_state
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RuleState') is not None:
            self.rule_state = m.get('RuleState')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetSqlTemplateListResponseBodyResults(TeaModel):
    def __init__(
        self,
        template_content: str = None,
        last_capture_time: str = None,
        capture_count: int = None,
        template_id: str = None,
        sql_type: int = None,
        rule_list: List[GetSqlTemplateListResponseBodyResultsRuleList] = None,
    ):
        self.template_content = template_content
        self.last_capture_time = last_capture_time
        self.capture_count = capture_count
        self.template_id = template_id
        self.sql_type = sql_type
        self.rule_list = rule_list

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.last_capture_time is not None:
            result['LastCaptureTime'] = self.last_capture_time
        if self.capture_count is not None:
            result['CaptureCount'] = self.capture_count
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('LastCaptureTime') is not None:
            self.last_capture_time = m.get('LastCaptureTime')
        if m.get('CaptureCount') is not None:
            self.capture_count = m.get('CaptureCount')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = GetSqlTemplateListResponseBodyResultsRuleList()
                self.rule_list.append(temp_model.from_map(k))
        return self


class GetSqlTemplateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        results: List[GetSqlTemplateListResponseBodyResults] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.results = results

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = GetSqlTemplateListResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class GetSqlTemplateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSqlTemplateListResponseBody = None,
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
            temp_model = GetSqlTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopSqlTemplateListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
        order_type: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class GetTopSqlTemplateListResponseBodyTemplateList(TeaModel):
    def __init__(
        self,
        template_content: str = None,
        exec_cost_us: str = None,
        affect_rows: str = None,
        exec_cost_usmean: str = None,
        last_capture_time: str = None,
        template_id: str = None,
        capture_count: str = None,
    ):
        self.template_content = template_content
        self.exec_cost_us = exec_cost_us
        self.affect_rows = affect_rows
        self.exec_cost_usmean = exec_cost_usmean
        self.last_capture_time = last_capture_time
        self.template_id = template_id
        self.capture_count = capture_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.exec_cost_us is not None:
            result['ExecCostUS'] = self.exec_cost_us
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows
        if self.exec_cost_usmean is not None:
            result['ExecCostUSMean'] = self.exec_cost_usmean
        if self.last_capture_time is not None:
            result['LastCaptureTime'] = self.last_capture_time
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.capture_count is not None:
            result['CaptureCount'] = self.capture_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('ExecCostUS') is not None:
            self.exec_cost_us = m.get('ExecCostUS')
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')
        if m.get('ExecCostUSMean') is not None:
            self.exec_cost_usmean = m.get('ExecCostUSMean')
        if m.get('LastCaptureTime') is not None:
            self.last_capture_time = m.get('LastCaptureTime')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CaptureCount') is not None:
            self.capture_count = m.get('CaptureCount')
        return self


class GetTopSqlTemplateListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_list: List[GetTopSqlTemplateListResponseBodyTemplateList] = None,
    ):
        self.request_id = request_id
        self.template_list = template_list

    def validate(self):
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TemplateList'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['TemplateList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_list = []
        if m.get('TemplateList') is not None:
            for k in m.get('TemplateList'):
                temp_model = GetTopSqlTemplateListResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k))
        return self


class GetTopSqlTemplateListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTopSqlTemplateListResponseBody = None,
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
            temp_model = GetTopSqlTemplateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GradeProtectionReportRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class GradeProtectionReportResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GradeProtectionReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GradeProtectionReportResponseBody = None,
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
            temp_model = GradeProtectionReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportDataSourceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        data_json: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.data_json = data_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.data_json is not None:
            result['DataJson'] = self.data_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataJson') is not None:
            self.data_json = m.get('DataJson')
        return self


class ImportDataSourceResponseBody(TeaModel):
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


class ImportDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportDataSourceResponseBody = None,
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
            temp_model = ImportDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IntegratedReportRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class IntegratedReportResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IntegratedReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IntegratedReportResponseBody = None,
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
            temp_model = IntegratedReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAssociatedRulesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        rule_name: str = None,
        rule_type: str = None,
        rule_defn: str = None,
        db_id: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.rule_defn = rule_defn
        self.db_id = db_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_defn is not None:
            result['RuleDefn'] = self.rule_defn
        if self.db_id is not None:
            result['DbId'] = self.db_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleDefn') is not None:
            self.rule_defn = m.get('RuleDefn')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        return self


class ListAssociatedRulesResponseBodyServerData(TeaModel):
    def __init__(
        self,
        json_result: str = None,
    ):
        self.json_result = json_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class ListAssociatedRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: ListAssociatedRulesResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = ListAssociatedRulesResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class ListAssociatedRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAssociatedRulesResponseBody = None,
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
            temp_model = ListAssociatedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_ids = db_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_ids is not None:
            result['DbIds'] = self.db_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbIds') is not None:
            self.db_ids = m.get('DbIds')
        return self


class ListDataSourceAttributeResponseBodyDbList(TeaModel):
    def __init__(
        self,
        result_audit_mode: str = None,
        db_id: int = None,
        result_audit_max_size: int = None,
        audit_mode: str = None,
        result_audit_max_line: int = None,
    ):
        self.result_audit_mode = result_audit_mode
        self.db_id = db_id
        self.result_audit_max_size = result_audit_max_size
        self.audit_mode = audit_mode
        self.result_audit_max_line = result_audit_max_line

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_audit_mode is not None:
            result['ResultAuditMode'] = self.result_audit_mode
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.result_audit_max_size is not None:
            result['ResultAuditMaxSize'] = self.result_audit_max_size
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode
        if self.result_audit_max_line is not None:
            result['ResultAuditMaxLine'] = self.result_audit_max_line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultAuditMode') is not None:
            self.result_audit_mode = m.get('ResultAuditMode')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('ResultAuditMaxSize') is not None:
            self.result_audit_max_size = m.get('ResultAuditMaxSize')
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')
        if m.get('ResultAuditMaxLine') is not None:
            self.result_audit_max_line = m.get('ResultAuditMaxLine')
        return self


class ListDataSourceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        db_list: List[ListDataSourceAttributeResponseBodyDbList] = None,
    ):
        self.request_id = request_id
        self.db_list = db_list

    def validate(self):
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.db_list = []
        if m.get('DbList') is not None:
            for k in m.get('DbList'):
                temp_model = ListDataSourceAttributeResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k))
        return self


class ListDataSourceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataSourceAttributeResponseBody = None,
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
            temp_model = ListDataSourceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        return self


class ListDataSourcesResponseBodyDbList(TeaModel):
    def __init__(
        self,
        db_id: int = None,
        create_time: str = None,
        db_username: str = None,
        db_certificate: str = None,
        db_instance_id: str = None,
        asset_type: int = None,
        db_version: int = None,
        db_name: str = None,
        db_type: int = None,
        audit_switch: int = None,
        db_type_name: str = None,
        db_version_name: str = None,
        db_addresses: List[str] = None,
    ):
        self.db_id = db_id
        self.create_time = create_time
        self.db_username = db_username
        self.db_certificate = db_certificate
        self.db_instance_id = db_instance_id
        self.asset_type = asset_type
        self.db_version = db_version
        self.db_name = db_name
        self.db_type = db_type
        self.audit_switch = audit_switch
        self.db_type_name = db_type_name
        self.db_version_name = db_version_name
        self.db_addresses = db_addresses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_username is not None:
            result['DbUsername'] = self.db_username
        if self.db_certificate is not None:
            result['DbCertificate'] = self.db_certificate
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.audit_switch is not None:
            result['AuditSwitch'] = self.audit_switch
        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name
        if self.db_version_name is not None:
            result['DbVersionName'] = self.db_version_name
        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbUsername') is not None:
            self.db_username = m.get('DbUsername')
        if m.get('DbCertificate') is not None:
            self.db_certificate = m.get('DbCertificate')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('AuditSwitch') is not None:
            self.audit_switch = m.get('AuditSwitch')
        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')
        if m.get('DbVersionName') is not None:
            self.db_version_name = m.get('DbVersionName')
        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        db_list: List[ListDataSourcesResponseBodyDbList] = None,
    ):
        self.request_id = request_id
        self.db_list = db_list

    def validate(self):
        if self.db_list:
            for k in self.db_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['DbList'] = []
        if self.db_list is not None:
            for k in self.db_list:
                result['DbList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.db_list = []
        if m.get('DbList') is not None:
            for k in m.get('DbList'):
                temp_model = ListDataSourcesResponseBodyDbList()
                self.db_list.append(temp_model.from_map(k))
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDataSourcesResponseBody = None,
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
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogAlarmTasksRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListLogAlarmTasksResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        task_status: int = None,
        task_id: int = None,
        create_time: str = None,
        task_name: str = None,
        to_mail_list: List[str] = None,
        risk_level_list: List[str] = None,
        db_id_list: List[str] = None,
    ):
        self.task_status = task_status
        self.task_id = task_id
        self.create_time = create_time
        self.task_name = task_name
        self.to_mail_list = to_mail_list
        self.risk_level_list = risk_level_list
        self.db_id_list = db_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list
        if self.db_id_list is not None:
            result['DbIdList'] = self.db_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')
        if m.get('DbIdList') is not None:
            self.db_id_list = m.get('DbIdList')
        return self


class ListLogAlarmTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[ListLogAlarmTasksResponseBodyTaskList] = None,
    ):
        self.request_id = request_id
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListLogAlarmTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListLogAlarmTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListLogAlarmTasksResponseBody = None,
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
            temp_model = ListLogAlarmTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReportPushTasksRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListReportPushTasksResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        schedule_time: str = None,
        job_status: int = None,
        job_id: int = None,
        schedule_type: str = None,
        db_list: List[str] = None,
        report_type: List[str] = None,
        email_list: List[str] = None,
    ):
        self.schedule_time = schedule_time
        self.job_status = job_status
        self.job_id = job_id
        self.schedule_type = schedule_type
        self.db_list = db_list
        self.report_type = report_type
        self.email_list = email_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.email_list is not None:
            result['EmailList'] = self.email_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('EmailList') is not None:
            self.email_list = m.get('EmailList')
        return self


class ListReportPushTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[ListReportPushTasksResponseBodyTaskList] = None,
    ):
        self.request_id = request_id
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListReportPushTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListReportPushTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListReportPushTasksResponseBody = None,
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
            temp_model = ListReportPushTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRuleGroupsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        rule_name: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListRuleGroupsResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRuleGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRuleGroupsResponseBody = None,
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
            temp_model = ListRuleGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRulesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: str = None,
        foreground_type: str = None,
        rule_name: str = None,
        rule_type: str = None,
        rule_group_id: str = None,
        risk_level: str = None,
        rule_quote: int = None,
        rule_state: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.foreground_type = foreground_type
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.rule_group_id = rule_group_id
        self.risk_level = risk_level
        self.rule_quote = rule_quote
        self.rule_state = rule_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.foreground_type is not None:
            result['ForegroundType'] = self.foreground_type
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.rule_group_id is not None:
            result['RuleGroupId'] = self.rule_group_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.rule_quote is not None:
            result['RuleQuote'] = self.rule_quote
        if self.rule_state is not None:
            result['RuleState'] = self.rule_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('ForegroundType') is not None:
            self.foreground_type = m.get('ForegroundType')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('RuleGroupId') is not None:
            self.rule_group_id = m.get('RuleGroupId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RuleQuote') is not None:
            self.rule_quote = m.get('RuleQuote')
        if m.get('RuleState') is not None:
            self.rule_state = m.get('RuleState')
        return self


class ListRulesResponseBodyServerData(TeaModel):
    def __init__(
        self,
        json_result: str = None,
    ):
        self.json_result = json_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.json_result is not None:
            result['JsonResult'] = self.json_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JsonResult') is not None:
            self.json_result = m.get('JsonResult')
        return self


class ListRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: ListRulesResponseBodyServerData = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            self.server_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_data is not None:
            result['ServerData'] = self.server_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerData') is not None:
            temp_model = ListRulesResponseBodyServerData()
            self.server_data = temp_model.from_map(m['ServerData'])
        return self


class ListRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRulesResponseBody = None,
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
            temp_model = ListRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSqlTypeKeysForRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListSqlTypeKeysForRuleResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSqlTypeKeysForRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSqlTypeKeysForRuleResponseBody = None,
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
            temp_model = ListSqlTypeKeysForRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSqlTypesForRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        type_id: str = None,
        sqltype_1: str = None,
        key_world: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.type_id = type_id
        self.sqltype_1 = sqltype_1
        self.key_world = key_world

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.type_id is not None:
            result['TypeId'] = self.type_id
        if self.sqltype_1 is not None:
            result['Sqltype1'] = self.sqltype_1
        if self.key_world is not None:
            result['KeyWorld'] = self.key_world
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')
        if m.get('Sqltype1') is not None:
            self.sqltype_1 = m.get('Sqltype1')
        if m.get('KeyWorld') is not None:
            self.key_world = m.get('KeyWorld')
        return self


class ListSqlTypesForRuleResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSqlTypesForRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSqlTypesForRuleResponseBody = None,
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
            temp_model = ListSqlTypesForRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSupportDbTypesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListSupportDbTypesResponseBodyTypeListDbVersions(TeaModel):
    def __init__(
        self,
        db_version_name: str = None,
        db_version: int = None,
    ):
        self.db_version_name = db_version_name
        self.db_version = db_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_version_name is not None:
            result['DbVersionName'] = self.db_version_name
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbVersionName') is not None:
            self.db_version_name = m.get('DbVersionName')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        return self


class ListSupportDbTypesResponseBodyTypeList(TeaModel):
    def __init__(
        self,
        db_type: int = None,
        db_type_name: str = None,
        db_versions: List[ListSupportDbTypesResponseBodyTypeListDbVersions] = None,
    ):
        self.db_type = db_type
        self.db_type_name = db_type_name
        self.db_versions = db_versions

    def validate(self):
        if self.db_versions:
            for k in self.db_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_type_name is not None:
            result['DbTypeName'] = self.db_type_name
        result['DbVersions'] = []
        if self.db_versions is not None:
            for k in self.db_versions:
                result['DbVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbTypeName') is not None:
            self.db_type_name = m.get('DbTypeName')
        self.db_versions = []
        if m.get('DbVersions') is not None:
            for k in m.get('DbVersions'):
                temp_model = ListSupportDbTypesResponseBodyTypeListDbVersions()
                self.db_versions.append(temp_model.from_map(k))
        return self


class ListSupportDbTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        type_list: List[ListSupportDbTypesResponseBodyTypeList] = None,
    ):
        self.request_id = request_id
        self.type_list = type_list

    def validate(self):
        if self.type_list:
            for k in self.type_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TypeList'] = []
        if self.type_list is not None:
            for k in self.type_list:
                result['TypeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.type_list = []
        if m.get('TypeList') is not None:
            for k in m.get('TypeList'):
                temp_model = ListSupportDbTypesResponseBodyTypeList()
                self.type_list.append(temp_model.from_map(k))
        return self


class ListSupportDbTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSupportDbTypesResponseBody = None,
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
            temp_model = ListSupportDbTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemAlarmsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        alarm_type: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.alarm_type = alarm_type
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class ListSystemAlarmsResponseBodyAlarms(TeaModel):
    def __init__(
        self,
        read_mark: int = None,
        alarm_detail: str = None,
        alarm_type: str = None,
        alarm_id: int = None,
        create_time: str = None,
    ):
        self.read_mark = read_mark
        self.alarm_detail = alarm_detail
        self.alarm_type = alarm_type
        self.alarm_id = alarm_id
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.read_mark is not None:
            result['ReadMark'] = self.read_mark
        if self.alarm_detail is not None:
            result['AlarmDetail'] = self.alarm_detail
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadMark') is not None:
            self.read_mark = m.get('ReadMark')
        if m.get('AlarmDetail') is not None:
            self.alarm_detail = m.get('AlarmDetail')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListSystemAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        alarms: List[ListSystemAlarmsResponseBodyAlarms] = None,
    ):
        self.request_id = request_id
        self.alarms = alarms

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = ListSystemAlarmsResponseBodyAlarms()
                self.alarms.append(temp_model.from_map(k))
        return self


class ListSystemAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSystemAlarmsResponseBody = None,
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
            temp_model = ListSystemAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemAlarmTasksRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListSystemAlarmTasksResponseBodyTaskList(TeaModel):
    def __init__(
        self,
        task_status: int = None,
        task_id: int = None,
        create_time: str = None,
        task_name: str = None,
        to_mail_list: List[str] = None,
    ):
        self.task_status = task_status
        self.task_id = task_id
        self.create_time = create_time
        self.task_name = task_name
        self.to_mail_list = to_mail_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        return self


class ListSystemAlarmTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_list: List[ListSystemAlarmTasksResponseBodyTaskList] = None,
    ):
        self.request_id = request_id
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListSystemAlarmTasksResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class ListSystemAlarmTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSystemAlarmTasksResponseBody = None,
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
            temp_model = ListSystemAlarmTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        current_page: int = None,
        request_id: str = None,
        page_size: int = None,
        total_count: int = None,
        tag_keys: List[ListTagKeysResponseBodyTagKeys] = None,
    ):
        self.current_page = current_page
        self.request_id = request_id
        self.page_size = page_size
        self.total_count = total_count
        self.tag_keys = tag_keys

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
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
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        region_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        resource_type: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesForSqlRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        sql_type_1: str = None,
        chose_condition: str = None,
        db_id: int = None,
        rule_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.sql_type_1 = sql_type_1
        self.chose_condition = chose_condition
        self.db_id = db_id
        self.rule_id = rule_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_type_1 is not None:
            result['SqlType1'] = self.sql_type_1
        if self.chose_condition is not None:
            result['ChoseCondition'] = self.chose_condition
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlType1') is not None:
            self.sql_type_1 = m.get('SqlType1')
        if m.get('ChoseCondition') is not None:
            self.chose_condition = m.get('ChoseCondition')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTemplatesForSqlRuleResponseBodyServerData(TeaModel):
    def __init__(
        self,
        count_timely: str = None,
        black_or_white: int = None,
        sql_text: str = None,
        sqltype_1: str = None,
        sql_id: str = None,
    ):
        self.count_timely = count_timely
        self.black_or_white = black_or_white
        self.sql_text = sql_text
        self.sqltype_1 = sqltype_1
        self.sql_id = sql_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_timely is not None:
            result['CountTimely'] = self.count_timely
        if self.black_or_white is not None:
            result['BlackOrWhite'] = self.black_or_white
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        if self.sqltype_1 is not None:
            result['Sqltype1'] = self.sqltype_1
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountTimely') is not None:
            self.count_timely = m.get('CountTimely')
        if m.get('BlackOrWhite') is not None:
            self.black_or_white = m.get('BlackOrWhite')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        if m.get('Sqltype1') is not None:
            self.sqltype_1 = m.get('Sqltype1')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        return self


class ListTemplatesForSqlRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_data: List[ListTemplatesForSqlRuleResponseBodyServerData] = None,
    ):
        self.request_id = request_id
        self.server_data = server_data

    def validate(self):
        if self.server_data:
            for k in self.server_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServerData'] = []
        if self.server_data is not None:
            for k in self.server_data:
                result['ServerData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.server_data = []
        if m.get('ServerData') is not None:
            for k in m.get('ServerData'):
                temp_model = ListTemplatesForSqlRuleResponseBodyServerData()
                self.server_data.append(temp_model.from_map(k))
        return self


class ListTemplatesForSqlRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTemplatesForSqlRuleResponseBody = None,
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
            temp_model = ListTemplatesForSqlRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsedSqlTypesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        rule_id: str = None,
        rule_type: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.rule_id = rule_id
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        return self


class ListUsedSqlTypesResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUsedSqlTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListUsedSqlTypesResponseBody = None,
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
            temp_model = ListUsedSqlTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBaseTemplateStateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        template_state: int = None,
        template_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.template_state = template_state
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.template_state is not None:
            result['TemplateState'] = self.template_state
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateState') is not None:
            self.template_state = m.get('TemplateState')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class ModifyBaseTemplateStateResponseBody(TeaModel):
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


class ModifyBaseTemplateStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBaseTemplateStateResponseBody = None,
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
            temp_model = ModifyBaseTemplateStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCustomNameRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
        commodity_code: str = None,
        instance_id: str = None,
        custom_name: str = None,
    ):
        self.source_ip = source_ip
        self.commodity_code = commodity_code
        self.instance_id = instance_id
        self.custom_name = custom_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.custom_name is not None:
            result['CustomName'] = self.custom_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CustomName') is not None:
            self.custom_name = m.get('CustomName')
        return self


class ModifyCustomNameResponseBody(TeaModel):
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


class ModifyCustomNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyCustomNameResponseBody = None,
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
            temp_model = ModifyCustomNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        db_name: str = None,
        db_version: int = None,
        db_certificate: str = None,
        db_username: str = None,
        db_password: str = None,
        db_instance_id: str = None,
        db_addresses: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.db_name = db_name
        self.db_version = db_version
        self.db_certificate = db_certificate
        self.db_username = db_username
        self.db_password = db_password
        self.db_instance_id = db_instance_id
        self.db_addresses = db_addresses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_version is not None:
            result['DbVersion'] = self.db_version
        if self.db_certificate is not None:
            result['DbCertificate'] = self.db_certificate
        if self.db_username is not None:
            result['DbUsername'] = self.db_username
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.db_addresses is not None:
            result['DbAddresses'] = self.db_addresses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')
        if m.get('DbCertificate') is not None:
            self.db_certificate = m.get('DbCertificate')
        if m.get('DbUsername') is not None:
            self.db_username = m.get('DbUsername')
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('DbAddresses') is not None:
            self.db_addresses = m.get('DbAddresses')
        return self


class ModifyDataSourceResponseBody(TeaModel):
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


class ModifyDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDataSourceResponseBody = None,
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
            temp_model = ModifyDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataSourceAttributeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        audit_mode: str = None,
        result_audit_mode: str = None,
        result_audit_max_line: int = None,
        result_audit_max_size: int = None,
        db_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.audit_mode = audit_mode
        self.result_audit_mode = result_audit_mode
        self.result_audit_max_line = result_audit_max_line
        self.result_audit_max_size = result_audit_max_size
        self.db_ids = db_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode
        if self.result_audit_mode is not None:
            result['ResultAuditMode'] = self.result_audit_mode
        if self.result_audit_max_line is not None:
            result['ResultAuditMaxLine'] = self.result_audit_max_line
        if self.result_audit_max_size is not None:
            result['ResultAuditMaxSize'] = self.result_audit_max_size
        if self.db_ids is not None:
            result['DbIds'] = self.db_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')
        if m.get('ResultAuditMode') is not None:
            self.result_audit_mode = m.get('ResultAuditMode')
        if m.get('ResultAuditMaxLine') is not None:
            self.result_audit_max_line = m.get('ResultAuditMaxLine')
        if m.get('ResultAuditMaxSize') is not None:
            self.result_audit_max_size = m.get('ResultAuditMaxSize')
        if m.get('DbIds') is not None:
            self.db_ids = m.get('DbIds')
        return self


class ModifyDataSourceAttributeResponseBody(TeaModel):
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


class ModifyDataSourceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDataSourceAttributeResponseBody = None,
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
            temp_model = ModifyDataSourceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        description: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.description = description
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
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


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceAttributeResponseBody = None,
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
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyLogAlarmTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        task_name: str = None,
        task_id: int = None,
        to_mail_list: List[str] = None,
        db_id_list: List[str] = None,
        risk_level_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.task_name = task_name
        self.task_id = task_id
        self.to_mail_list = to_mail_list
        self.db_id_list = db_id_list
        self.risk_level_list = risk_level_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        if self.db_id_list is not None:
            result['DbIdList'] = self.db_id_list
        if self.risk_level_list is not None:
            result['RiskLevelList'] = self.risk_level_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        if m.get('DbIdList') is not None:
            self.db_id_list = m.get('DbIdList')
        if m.get('RiskLevelList') is not None:
            self.risk_level_list = m.get('RiskLevelList')
        return self


class ModifyLogAlarmTaskResponseBody(TeaModel):
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


class ModifyLogAlarmTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyLogAlarmTaskResponseBody = None,
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
            temp_model = ModifyLogAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPlanRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.commodity_code = commodity_code
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyPlanResponseBody(TeaModel):
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


class ModifyPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPlanResponseBody = None,
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
            temp_model = ModifyPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyReportPushTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        job_id: int = None,
        schedule_type: str = None,
        schedule_time: str = None,
        job_status: int = None,
        report_type: List[str] = None,
        db_list: List[str] = None,
        email_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.job_id = job_id
        self.schedule_type = schedule_type
        self.schedule_time = schedule_time
        self.job_status = job_status
        self.report_type = report_type
        self.db_list = db_list
        self.email_list = email_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.email_list is not None:
            result['EmailList'] = self.email_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('EmailList') is not None:
            self.email_list = m.get('EmailList')
        return self


class ModifyReportPushTaskResponseBody(TeaModel):
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


class ModifyReportPushTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyReportPushTaskResponseBody = None,
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
            temp_model = ModifyReportPushTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyRuleGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        group_id: str = None,
        group_name: str = None,
        group_type: str = None,
        group_key_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.group_id = group_id
        self.group_name = group_name
        self.group_type = group_type
        self.group_key_id = group_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_key_id is not None:
            result['GroupKeyId'] = self.group_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupKeyId') is not None:
            self.group_key_id = m.get('GroupKeyId')
        return self


class ModifyRuleGroupResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyRuleGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyRuleGroupResponseBody = None,
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
            temp_model = ModifyRuleGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySystemAlarmTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        task_name: str = None,
        task_id: int = None,
        to_mail_list: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.task_name = task_name
        self.task_id = task_id
        self.to_mail_list = to_mail_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.to_mail_list is not None:
            result['ToMailList'] = self.to_mail_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ToMailList') is not None:
            self.to_mail_list = m.get('ToMailList')
        return self


class ModifySystemAlarmTaskResponseBody(TeaModel):
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


class ModifySystemAlarmTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySystemAlarmTaskResponseBody = None,
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
            temp_model = ModifySystemAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        region_id: str = None,
    ):
        self.resource_id = resource_id
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveResourceGroupResponseBody = None,
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PciReportRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class PciReportResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PciReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PciReportResponseBody = None,
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
            temp_model = PciReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutLoginCountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class PutLoginCountResponseBody(TeaModel):
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


class PutLoginCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutLoginCountResponseBody = None,
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
            temp_model = PutLoginCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadMarkSystemAlarmsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        alarm_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.alarm_ids = alarm_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.alarm_ids is not None:
            result['AlarmIds'] = self.alarm_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AlarmIds') is not None:
            self.alarm_ids = m.get('AlarmIds')
        return self


class ReadMarkSystemAlarmsResponseBody(TeaModel):
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


class ReadMarkSystemAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReadMarkSystemAlarmsResponseBody = None,
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
            temp_model = ReadMarkSystemAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        service_code: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.service_code = service_code
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RefundInstanceResponseBody(TeaModel):
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


class RefundInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefundInstanceResponseBody = None,
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
            temp_model = RefundInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterNoticeMailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mail: str = None,
        vcode: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mail = mail
        self.vcode = vcode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mail is not None:
            result['Mail'] = self.mail
        if self.vcode is not None:
            result['Vcode'] = self.vcode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        if m.get('Vcode') is not None:
            self.vcode = m.get('Vcode')
        return self


class RegisterNoticeMailResponseBody(TeaModel):
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


class RegisterNoticeMailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterNoticeMailResponseBody = None,
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
            temp_model = RegisterNoticeMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveLogMaskConfigRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mask_id: int = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mask_id = mask_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mask_id is not None:
            result['MaskId'] = self.mask_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaskId') is not None:
            self.mask_id = m.get('MaskId')
        return self


class RemoveLogMaskConfigResponseBody(TeaModel):
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


class RemoveLogMaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveLogMaskConfigResponseBody = None,
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
            temp_model = RemoveLogMaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerifyCodeMailRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        mail: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.mail = mail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mail is not None:
            result['Mail'] = self.mail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mail') is not None:
            self.mail = m.get('Mail')
        return self


class SendVerifyCodeMailResponseBody(TeaModel):
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


class SendVerifyCodeMailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendVerifyCodeMailResponseBody = None,
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
            temp_model = SendVerifyCodeMailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SoxReportRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        db_id: int = None,
        begin_date: str = None,
        end_date: str = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.db_id = db_id
        self.begin_date = begin_date
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.db_id is not None:
            result['DbId'] = self.db_id
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        return self


class SoxReportResponseBody(TeaModel):
    def __init__(
        self,
        server_data: str = None,
        request_id: str = None,
    ):
        self.server_data = server_data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_data is not None:
            result['ServerData'] = self.server_data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerData') is not None:
            self.server_data = m.get('ServerData')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SoxReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SoxReportResponseBody = None,
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
            temp_model = SoxReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAlarmTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        task_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class StartAlarmTaskResponseBody(TeaModel):
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


class StartAlarmTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartAlarmTaskResponseBody = None,
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
            temp_model = StartAlarmTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        vswitch_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.vswitch_id = vswitch_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartInstanceResponseBody(TeaModel):
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


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAlarmTaskRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        instance_id: str = None,
        task_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.instance_id = instance_id
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_ids is not None:
            result['TaskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskIds') is not None:
            self.task_ids = m.get('TaskIds')
        return self


class StopAlarmTaskResponseBody(TeaModel):
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


class StopAlarmTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopAlarmTaskResponseBody = None,
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
            temp_model = StopAlarmTaskResponseBody()
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
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceVersionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpgradeInstanceVersionResponseBody(TeaModel):
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


class UpgradeInstanceVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeInstanceVersionResponseBody = None,
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
            temp_model = UpgradeInstanceVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


