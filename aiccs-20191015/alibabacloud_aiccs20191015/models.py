# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class SendHotlineHeartBeatRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        token: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class SendHotlineHeartBeatResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendHotlineHeartBeatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendHotlineHeartBeatResponseBody = None,
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
            temp_model = SendHotlineHeartBeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartChatWorkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        account_name: str = None,
    ):
        # instanceId
        self.instance_id = instance_id
        # accountName
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class StartChatWorkResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # httpStatusCode
        self.http_status_code = http_status_code
        # data
        self.data = data
        # code
        self.code = code
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartChatWorkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartChatWorkResponseBody = None,
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
            temp_model = StartChatWorkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HangUpDoubleCallRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        acid: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 会话ID
        self.acid = acid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class HangUpDoubleCallResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 是否调用成功
        self.success = success
        # 错误码
        self.code = code
        # 错误信息
        self.message = message

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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class HangUpDoubleCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HangUpDoubleCallResponseBody = None,
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
            temp_model = HangUpDoubleCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAgentRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        display_name: str = None,
        skill_group_id: List[int] = None,
        skill_group_id_list: List[int] = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.display_name = display_name
        self.skill_group_id = skill_group_id
        self.skill_group_id_list = skill_group_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')
        return self


class UpdateAgentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAgentResponseBody = None,
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
            temp_model = UpdateAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditQualityRuleTagRequestAnalysisTypes(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: int = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class EditQualityRuleTagRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        analysis_types: List[EditQualityRuleTagRequestAnalysisTypes] = None,
    ):
        self.instance_id = instance_id
        self.analysis_types = analysis_types

    def validate(self):
        if self.analysis_types:
            for k in self.analysis_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['AnalysisTypes'] = []
        if self.analysis_types is not None:
            for k in self.analysis_types:
                result['AnalysisTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.analysis_types = []
        if m.get('AnalysisTypes') is not None:
            for k in m.get('AnalysisTypes'):
                temp_model = EditQualityRuleTagRequestAnalysisTypes()
                self.analysis_types.append(temp_model.from_map(k))
        return self


class EditQualityRuleTagResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditQualityRuleTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditQualityRuleTagResponseBody = None,
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
            temp_model = EditQualityRuleTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOnlineServiceVolumeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetOnlineServiceVolumeShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetOnlineServiceVolumeResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetOnlineServiceVolumeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetOnlineServiceVolumeResponseBodyData = None,
        request_id: str = None,
    ):
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetOnlineServiceVolumeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOnlineServiceVolumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOnlineServiceVolumeResponseBody = None,
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
            temp_model = GetOnlineServiceVolumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOutboundTaskRequest(TeaModel):
    def __init__(
        self,
        outbound_task_id: int = None,
        instance_id: str = None,
    ):
        self.outbound_task_id = outbound_task_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteOutboundTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteOutboundTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOutboundTaskResponseBody = None,
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
            temp_model = DeleteOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddOuterAccountRequest(TeaModel):
    def __init__(
        self,
        outer_account_id: str = None,
        outer_account_type: str = None,
        outer_account_name: str = None,
        avatar: str = None,
        real_name: str = None,
        outer_department_id: str = None,
        outer_group_ids: str = None,
        ext: str = None,
        outer_department_type: str = None,
        outer_group_type: str = None,
    ):
        self.outer_account_id = outer_account_id
        self.outer_account_type = outer_account_type
        self.outer_account_name = outer_account_name
        self.avatar = avatar
        self.real_name = real_name
        self.outer_department_id = outer_department_id
        self.outer_group_ids = outer_group_ids
        self.ext = ext
        self.outer_department_type = outer_department_type
        self.outer_group_type = outer_group_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id
        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type
        if self.outer_account_name is not None:
            result['OuterAccountName'] = self.outer_account_name
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.outer_department_id is not None:
            result['OuterDepartmentId'] = self.outer_department_id
        if self.outer_group_ids is not None:
            result['OuterGroupIds'] = self.outer_group_ids
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.outer_department_type is not None:
            result['OuterDepartmentType'] = self.outer_department_type
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')
        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')
        if m.get('OuterAccountName') is not None:
            self.outer_account_name = m.get('OuterAccountName')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('OuterDepartmentId') is not None:
            self.outer_department_id = m.get('OuterDepartmentId')
        if m.get('OuterGroupIds') is not None:
            self.outer_group_ids = m.get('OuterGroupIds')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('OuterDepartmentType') is not None:
            self.outer_department_type = m.get('OuterDepartmentType')
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        return self


class AddOuterAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddOuterAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddOuterAccountResponseBody = None,
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
            temp_model = AddOuterAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentByIdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        agent_id: int = None,
    ):
        self.instance_id = instance_id
        self.agent_id = agent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        return self


class GetAgentByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        show_name: str = None,
        foreign_key: str = None,
        servicer_type: int = None,
        real_name: str = None,
        create_user_name: str = None,
        agent_id: int = None,
        foreign_nick: str = None,
    ):
        self.show_name = show_name
        self.foreign_key = foreign_key
        self.servicer_type = servicer_type
        self.real_name = real_name
        self.create_user_name = create_user_name
        self.agent_id = agent_id
        self.foreign_nick = foreign_nick

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.foreign_key is not None:
            result['ForeignKey'] = self.foreign_key
        if self.servicer_type is not None:
            result['ServicerType'] = self.servicer_type
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.foreign_nick is not None:
            result['ForeignNick'] = self.foreign_nick
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('ForeignKey') is not None:
            self.foreign_key = m.get('ForeignKey')
        if m.get('ServicerType') is not None:
            self.servicer_type = m.get('ServicerType')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('ForeignNick') is not None:
            self.foreign_nick = m.get('ForeignNick')
        return self


class GetAgentByIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAgentByIdResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAgentByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgentByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentByIdResponseBody = None,
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
            temp_model = GetAgentByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityRuleDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        quality_rule_id: int = None,
    ):
        self.instance_id = instance_id
        self.quality_rule_id = quality_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.quality_rule_id is not None:
            result['QualityRuleId'] = self.quality_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QualityRuleId') is not None:
            self.quality_rule_id = m.get('QualityRuleId')
        return self


class GetQualityRuleDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_tag: int = None,
        key_words: List[str] = None,
        match_type: int = None,
        name: str = None,
        rule_create_time: str = None,
        rule_id: int = None,
    ):
        self.rule_tag = rule_tag
        self.key_words = key_words
        self.match_type = match_type
        self.name = name
        self.rule_create_time = rule_create_time
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_create_time is not None:
            result['RuleCreateTime'] = self.rule_create_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleCreateTime') is not None:
            self.rule_create_time = m.get('RuleCreateTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetQualityRuleDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetQualityRuleDetailResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityRuleDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityRuleDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQualityRuleDetailResponseBody = None,
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
            temp_model = GetQualityRuleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityProjectLogRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        project_id: int = None,
    ):
        self.instance_id = instance_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetQualityProjectLogResponseBodyData(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        action_data: str = None,
        project_id: int = None,
        project_create_time: str = None,
        action_time: str = None,
    ):
        self.action_type = action_type
        self.action_data = action_data
        self.project_id = project_id
        self.project_create_time = project_create_time
        self.action_time = action_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.action_data is not None:
            result['ActionData'] = self.action_data
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_create_time is not None:
            result['ProjectCreateTime'] = self.project_create_time
        if self.action_time is not None:
            result['ActionTime'] = self.action_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('ActionData') is not None:
            self.action_data = m.get('ActionData')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectCreateTime') is not None:
            self.project_create_time = m.get('ProjectCreateTime')
        if m.get('ActionTime') is not None:
            self.action_time = m.get('ActionTime')
        return self


class GetQualityProjectLogResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetQualityProjectLogResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetQualityProjectLogResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityProjectLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQualityProjectLogResponseBody = None,
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
            temp_model = GetQualityProjectLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotlineRecordDetailRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        close_time_end: int = None,
        current_page: int = None,
        page_size: int = None,
        close_time_start: int = None,
    ):
        # clientToken
        self.client_token = client_token
        # 实例id
        self.instance_id = instance_id
        # 热线挂断的时间范围
        self.close_time_end = close_time_end
        # 当前页
        self.current_page = current_page
        # 每页数据量
        self.page_size = page_size
        # 热线挂断的时间范围
        self.close_time_start = close_time_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.close_time_end is not None:
            result['CloseTimeEnd'] = self.close_time_end
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.close_time_start is not None:
            result['CloseTimeStart'] = self.close_time_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CloseTimeEnd') is not None:
            self.close_time_end = m.get('CloseTimeEnd')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CloseTimeStart') is not None:
            self.close_time_start = m.get('CloseTimeStart')
        return self


class ListHotlineRecordDetailResponseBodyResultDataData(TeaModel):
    def __init__(
        self,
        servicer_name: str = None,
        start_time: int = None,
        end_time: int = None,
        oss_url: str = None,
    ):
        self.servicer_name = servicer_name
        # 热线开始时间
        self.start_time = start_time
        # 热线结束时间
        self.end_time = end_time
        # 热线通话录音地址
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        return self


class ListHotlineRecordDetailResponseBodyResultData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        total_results: int = None,
        total_page: int = None,
        one_page_size: int = None,
        data: List[ListHotlineRecordDetailResponseBodyResultDataData] = None,
    ):
        self.current_page = current_page
        self.total_results = total_results
        self.total_page = total_page
        self.one_page_size = one_page_size
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListHotlineRecordDetailResponseBodyResultDataData()
                self.data.append(temp_model.from_map(k))
        return self


class ListHotlineRecordDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        result_data: ListHotlineRecordDetailResponseBodyResultData = None,
        code: str = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # httpStatusCode
        self.http_status_code = http_status_code
        # data
        self.result_data = result_data
        # code
        self.code = code
        # success
        self.success = success

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ResultData') is not None:
            temp_model = ListHotlineRecordDetailResponseBodyResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotlineRecordDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHotlineRecordDetailResponseBody = None,
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
            temp_model = ListHotlineRecordDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineMessageLogRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        acid: str = None,
    ):
        # 实例id
        self.instance_id = instance_id
        # 会话id
        self.acid = acid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class GetHotlineMessageLogResponseBodyData(TeaModel):
    def __init__(
        self,
        acid: str = None,
        sender_type: int = None,
        start_time: int = None,
        end_time: int = None,
        mid: str = None,
        content: str = None,
    ):
        # 会话ID
        self.acid = acid
        # 发送方类型（1：会员，2：坐席）
        self.sender_type = sender_type
        # 开始时间
        self.start_time = start_time
        # 结束时间
        self.end_time = end_time
        # 记录id
        self.mid = mid
        # 会话内容
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.sender_type is not None:
            result['SenderType'] = self.sender_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.mid is not None:
            result['Mid'] = self.mid
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('SenderType') is not None:
            self.sender_type = m.get('SenderType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Mid') is not None:
            self.mid = m.get('Mid')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetHotlineMessageLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: List[GetHotlineMessageLogResponseBodyData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 调用是否成功
        self.success = success
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetHotlineMessageLogResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetHotlineMessageLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineMessageLogResponseBody = None,
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
            temp_model = GetHotlineMessageLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityProjectListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        project_id: int = None,
        project_name: str = None,
        status: int = None,
        page_no: int = None,
        page_size: int = None,
        check_freq_type: int = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 质检项ID
        self.project_id = project_id
        # 质检项名称
        self.project_name = project_name
        # 质检项状态
        self.status = status
        # PageNo
        self.page_no = page_no
        # PageSize
        self.page_size = page_size
        # 质检频率
        self.check_freq_type = check_freq_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.status is not None:
            result['Status'] = self.status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.check_freq_type is not None:
            result['checkFreqType'] = self.check_freq_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('checkFreqType') is not None:
            self.check_freq_type = m.get('checkFreqType')
        return self


class GetQualityProjectListResponseBodyDataQualityProjectList(TeaModel):
    def __init__(
        self,
        status: int = None,
        quality_type: int = None,
        quality_rule_ids: List[int] = None,
        create_time: str = None,
        project_name: str = None,
        check_freq_type: int = None,
        dep_list: List[int] = None,
        servicer_list: List[int] = None,
        version: int = None,
        group_list: List[int] = None,
        id: int = None,
        modify_time: str = None,
    ):
        # 质检任务状态
        self.status = status
        # 质检任务类型
        self.quality_type = quality_type
        # 质检规则列表
        self.quality_rule_ids = quality_rule_ids
        # CreateTime
        self.create_time = create_time
        # 质检任务名称
        self.project_name = project_name
        # 质检任务频率
        self.check_freq_type = check_freq_type
        # 技能组分组列表
        self.dep_list = dep_list
        # 坐席列表
        self.servicer_list = servicer_list
        # 版本
        self.version = version
        # 技能组列表
        self.group_list = group_list
        # 质检任务Id
        self.id = id
        # 修改时间
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.quality_type is not None:
            result['QualityType'] = self.quality_type
        if self.quality_rule_ids is not None:
            result['QualityRuleIds'] = self.quality_rule_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.dep_list is not None:
            result['DepList'] = self.dep_list
        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list
        if self.version is not None:
            result['Version'] = self.version
        if self.group_list is not None:
            result['GroupList'] = self.group_list
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QualityType') is not None:
            self.quality_type = m.get('QualityType')
        if m.get('QualityRuleIds') is not None:
            self.quality_rule_ids = m.get('QualityRuleIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')
        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetQualityProjectListResponseBodyData(TeaModel):
    def __init__(
        self,
        quality_project_list: List[GetQualityProjectListResponseBodyDataQualityProjectList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # 质检项列表
        self.quality_project_list = quality_project_list
        # PageNo
        self.page_no = page_no
        # PageSize
        self.page_size = page_size
        # Total
        self.total = total

    def validate(self):
        if self.quality_project_list:
            for k in self.quality_project_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QualityProjectList'] = []
        if self.quality_project_list is not None:
            for k in self.quality_project_list:
                result['QualityProjectList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_project_list = []
        if m.get('QualityProjectList') is not None:
            for k in m.get('QualityProjectList'):
                temp_model = GetQualityProjectListResponseBodyDataQualityProjectList()
                self.quality_project_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQualityProjectListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetQualityProjectListResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Data
        self.data = data
        # Code
        self.code = code
        # Success
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityProjectListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityProjectListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQualityProjectListResponseBody = None,
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
            temp_model = GetQualityProjectListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOutboundTaskRequest(TeaModel):
    def __init__(
        self,
        task_type: int = None,
        task_name: str = None,
        description: str = None,
        start_date: str = None,
        end_date: str = None,
        start_time: str = None,
        end_time: str = None,
        retry_time: int = None,
        retry_interval: int = None,
        skill_group: int = None,
        ani: str = None,
        group_name: str = None,
        model: int = None,
        department_id: int = None,
        ext_attrs: str = None,
        call_infos: str = None,
        instance_id: str = None,
    ):
        self.task_type = task_type
        self.task_name = task_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.retry_time = retry_time
        self.retry_interval = retry_interval
        self.skill_group = skill_group
        self.ani = ani
        self.group_name = group_name
        self.model = model
        self.department_id = department_id
        self.ext_attrs = ext_attrs
        self.call_infos = call_infos
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.description is not None:
            result['Description'] = self.description
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.ani is not None:
            result['Ani'] = self.ani
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.model is not None:
            result['Model'] = self.model
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs
        if self.call_infos is not None:
            result['CallInfos'] = self.call_infos
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')
        if m.get('CallInfos') is not None:
            self.call_infos = m.get('CallInfos')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateOutboundTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateOutboundTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOutboundTaskResponseBody = None,
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
            temp_model = CreateOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineRuntimeInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        account_name: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 账号名
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetHotlineRuntimeInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: Dict[str, Any] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 接口调用是否成功
        self.success = success
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # 数据结果
        self.data = data

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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetHotlineRuntimeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineRuntimeInfoResponseBody = None,
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
            temp_model = GetHotlineRuntimeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeDoubleCallRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        account_name: str = None,
        servicer_phone: str = None,
        member_phone: str = None,
        outbound_call_number: str = None,
        biz_data: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 账号名称
        self.account_name = account_name
        # 坐席手机号（需要通过坐席手机呼叫才需要填写）
        self.servicer_phone = servicer_phone
        # 用户手机号
        self.member_phone = member_phone
        # 外呼主叫号码
        self.outbound_call_number = outbound_call_number
        # 业务携带数据（JsonString）
        self.biz_data = biz_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.servicer_phone is not None:
            result['ServicerPhone'] = self.servicer_phone
        if self.member_phone is not None:
            result['MemberPhone'] = self.member_phone
        if self.outbound_call_number is not None:
            result['OutboundCallNumber'] = self.outbound_call_number
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('ServicerPhone') is not None:
            self.servicer_phone = m.get('ServicerPhone')
        if m.get('MemberPhone') is not None:
            self.member_phone = m.get('MemberPhone')
        if m.get('OutboundCallNumber') is not None:
            self.outbound_call_number = m.get('OutboundCallNumber')
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        return self


class MakeDoubleCallResponseBodyData(TeaModel):
    def __init__(
        self,
        acid: str = None,
    ):
        # 会话id
        self.acid = acid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class MakeDoubleCallResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: MakeDoubleCallResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 调用是否成功
        self.success = success
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # 返回数据
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = MakeDoubleCallResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class MakeDoubleCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MakeDoubleCallResponseBody = None,
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
            temp_model = MakeDoubleCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupAgentStatusDetailsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupAgentStatusDetailsShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupAgentStatusDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 每页的数量
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupAgentStatusDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetSkillGroupAgentStatusDetailsResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 接口调用是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupAgentStatusDetailsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupAgentStatusDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSkillGroupAgentStatusDetailsResponseBody = None,
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
            temp_model = GetSkillGroupAgentStatusDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentServiceStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
        time_latitude_type: str = None,
        exist_department_grouping: bool = None,
        exist_agent_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        return self


class GetAgentServiceStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
        time_latitude_type: str = None,
        exist_department_grouping: bool = None,
        exist_agent_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        return self


class GetAgentServiceStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetAgentServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAgentServiceStatusResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        # 错误描述
        self.message = message
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # data
        self.data = data
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAgentServiceStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgentServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentServiceStatusResponseBody = None,
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
            temp_model = GetAgentServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNumLocationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        phone_num: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.phone_num = phone_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        return self


class GetNumLocationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNumLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNumLocationResponseBody = None,
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
            temp_model = GetNumLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityRuleListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetQualityRuleListResponseBodyDataQualityRuleList(TeaModel):
    def __init__(
        self,
        rule_tag: int = None,
        key_words: List[str] = None,
        match_type: int = None,
        name: str = None,
        rule_create_time: str = None,
        rule_id: int = None,
    ):
        self.rule_tag = rule_tag
        self.key_words = key_words
        self.match_type = match_type
        self.name = name
        self.rule_create_time = rule_create_time
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_create_time is not None:
            result['RuleCreateTime'] = self.rule_create_time
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleCreateTime') is not None:
            self.rule_create_time = m.get('RuleCreateTime')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetQualityRuleListResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
        quality_rule_list: List[GetQualityRuleListResponseBodyDataQualityRuleList] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.total = total
        self.quality_rule_list = quality_rule_list

    def validate(self):
        if self.quality_rule_list:
            for k in self.quality_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['QualityRuleList'] = []
        if self.quality_rule_list is not None:
            for k in self.quality_rule_list:
                result['QualityRuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.quality_rule_list = []
        if m.get('QualityRuleList') is not None:
            for k in m.get('QualityRuleList'):
                temp_model = GetQualityRuleListResponseBodyDataQualityRuleList()
                self.quality_rule_list.append(temp_model.from_map(k))
        return self


class GetQualityRuleListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetQualityRuleListResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityRuleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQualityRuleListResponseBody = None,
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
            temp_model = GetQualityRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOutboundPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class ListOutboundPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[str] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOutboundPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOutboundPhoneNumberResponseBody = None,
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
            temp_model = ListOutboundPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentBySkillGroupIdRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        skill_group_id: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        return self


class ListAgentBySkillGroupIdResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        display_name: str = None,
        agent_id: int = None,
        account_name: str = None,
        tenant_id: int = None,
    ):
        self.status = status
        self.display_name = display_name
        self.agent_id = agent_id
        self.account_name = account_name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ListAgentBySkillGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListAgentBySkillGroupIdResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAgentBySkillGroupIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAgentBySkillGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAgentBySkillGroupIdResponseBody = None,
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
            temp_model = ListAgentBySkillGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HangupThirdCallRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.call_id = call_id
        self.job_id = job_id
        self.connection_id = connection_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        return self


class HangupThirdCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HangupThirdCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HangupThirdCallResponseBody = None,
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
            temp_model = HangupThirdCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartHotlineServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        # js sdk中自动生成的鉴权token
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class StartHotlineServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class StartHotlineServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartHotlineServiceResponseBody = None,
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
            temp_model = StartHotlineServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        # js sdk中自动生成的鉴权token
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetAgentResponseBodyDataGroupList(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        description: str = None,
        channel_type: int = None,
        skill_group_id: int = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.description = description
        self.channel_type = channel_type
        self.skill_group_id = skill_group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetAgentResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        display_name: str = None,
        agent_id: int = None,
        group_list: List[GetAgentResponseBodyDataGroupList] = None,
        account_name: str = None,
        tenant_id: int = None,
    ):
        self.status = status
        self.display_name = display_name
        self.agent_id = agent_id
        self.group_list = group_list
        self.account_name = account_name
        self.tenant_id = tenant_id

    def validate(self):
        if self.group_list:
            for k in self.group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        result['GroupList'] = []
        if self.group_list is not None:
            for k in self.group_list:
                result['GroupList'].append(k.to_map() if k else None)
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        self.group_list = []
        if m.get('GroupList') is not None:
            for k in m.get('GroupList'):
                temp_model = GetAgentResponseBodyDataGroupList()
                self.group_list.append(temp_model.from_map(k))
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetAgentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAgentResponseBodyData = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAgentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentResponseBody = None,
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
            temp_model = GetAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentIndexRealTimeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
    ):
        self.instance_id = instance_id
        self.page_size = page_size
        self.current_page = current_page
        self.dep_ids = dep_ids
        self.group_ids = group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        return self


class GetAgentIndexRealTimeResponseBodyDataColumns(TeaModel):
    def __init__(
        self,
        key: str = None,
        title: str = None,
    ):
        self.key = key
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetAgentIndexRealTimeResponseBodyData(TeaModel):
    def __init__(
        self,
        rows: List[Dict[str, Any]] = None,
        page_size: int = None,
        total: int = None,
        columns: List[GetAgentIndexRealTimeResponseBodyDataColumns] = None,
        page: int = None,
    ):
        self.rows = rows
        self.page_size = page_size
        self.total = total
        self.columns = columns
        self.page = page

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetAgentIndexRealTimeResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetAgentIndexRealTimeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAgentIndexRealTimeResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAgentIndexRealTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgentIndexRealTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentIndexRealTimeResponseBody = None,
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
            temp_model = GetAgentIndexRealTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineGroupDetailReportRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        start_date: int = None,
        end_date: int = None,
        instance_id: str = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date
        self.instance_id = instance_id
        self.dep_ids = dep_ids
        self.group_ids = group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        return self


class GetHotlineGroupDetailReportResponseBodyDataColumns(TeaModel):
    def __init__(
        self,
        key: str = None,
        title: str = None,
    ):
        self.key = key
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetHotlineGroupDetailReportResponseBodyData(TeaModel):
    def __init__(
        self,
        rows: List[Dict[str, Any]] = None,
        page_size: int = None,
        total: int = None,
        columns: List[GetHotlineGroupDetailReportResponseBodyDataColumns] = None,
        page: int = None,
    ):
        self.rows = rows
        self.page_size = page_size
        self.total = total
        self.columns = columns
        self.page = page

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetHotlineGroupDetailReportResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetHotlineGroupDetailReportResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetHotlineGroupDetailReportResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineGroupDetailReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotlineGroupDetailReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineGroupDetailReportResponseBody = None,
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
            temp_model = GetHotlineGroupDetailReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptPhoneNumRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        phone_num: str = None,
    ):
        # 实例Id
        self.instance_id = instance_id
        # 号码明文
        self.phone_num = phone_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        return self


class EncryptPhoneNumResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 接口调用是否成功
        self.success = success
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # 加密后密文
        self.data = data

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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class EncryptPhoneNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EncryptPhoneNumResponseBody = None,
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
            temp_model = EncryptPhoneNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceListRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetInstanceListResponseBodyCommodityInstances(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        http_status_code: int = None,
        commodity_instances: List[GetInstanceListResponseBodyCommodityInstances] = None,
        code: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.http_status_code = http_status_code
        self.commodity_instances = commodity_instances
        self.code = code
        self.success = success

    def validate(self):
        if self.commodity_instances:
            for k in self.commodity_instances:
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
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['CommodityInstances'] = []
        if self.commodity_instances is not None:
            for k in self.commodity_instances:
                result['CommodityInstances'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.commodity_instances = []
        if m.get('CommodityInstances') is not None:
            for k in m.get('CommodityInstances'):
                temp_model = GetInstanceListResponseBodyCommodityInstances()
                self.commodity_instances.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceListResponseBody = None,
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
            temp_model = GetInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityProjectDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        project_id: int = None,
    ):
        # 租户实例ID
        self.instance_id = instance_id
        # 质检任务ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetQualityProjectDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        quality_type: int = None,
        quality_rule_ids: List[int] = None,
        create_time: str = None,
        project_name: str = None,
        check_freq_type: int = None,
        dep_list: List[int] = None,
        servicer_list: List[int] = None,
        version: int = None,
        group_list: List[int] = None,
        id: int = None,
        modify_time: str = None,
    ):
        # 质检任务状态
        self.status = status
        # 质检类型
        self.quality_type = quality_type
        # 质检规则ID
        self.quality_rule_ids = quality_rule_ids
        # 创建时间
        self.create_time = create_time
        # 质检任务名称
        self.project_name = project_name
        # 质检周期
        self.check_freq_type = check_freq_type
        # 技能组分组
        self.dep_list = dep_list
        # 坐席列表
        self.servicer_list = servicer_list
        # Version
        self.version = version
        # 技能组列表
        self.group_list = group_list
        # 质检任务ID
        self.id = id
        # 修改时间
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.quality_type is not None:
            result['QualityType'] = self.quality_type
        if self.quality_rule_ids is not None:
            result['QualityRuleIds'] = self.quality_rule_ids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.dep_list is not None:
            result['DepList'] = self.dep_list
        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list
        if self.version is not None:
            result['Version'] = self.version
        if self.group_list is not None:
            result['GroupList'] = self.group_list
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QualityType') is not None:
            self.quality_type = m.get('QualityType')
        if m.get('QualityRuleIds') is not None:
            self.quality_rule_ids = m.get('QualityRuleIds')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')
        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetQualityProjectDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetQualityProjectDetailResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        # Message
        self.message = message
        # RequestId
        self.request_id = request_id
        # Data
        self.data = data
        # Code
        self.code = code
        # Success
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityProjectDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityProjectDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQualityProjectDetailResponseBody = None,
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
            temp_model = GetQualityProjectDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCcoSmartCallOperateRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        call_id: str = None,
        command: str = None,
        param: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.call_id = call_id
        self.command = command
        self.param = param

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
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.command is not None:
            result['Command'] = self.command
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class SendCcoSmartCallOperateResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SendCcoSmartCallOperateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendCcoSmartCallOperateResponseBody = None,
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
            temp_model = SendCcoSmartCallOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AnswerCallRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.call_id = call_id
        self.job_id = job_id
        self.connection_id = connection_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        return self


class AnswerCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AnswerCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AnswerCallResponseBody = None,
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
            temp_model = AnswerCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMicroOutboundRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        account_type: str = None,
        account_id: str = None,
        command_code: str = None,
        calling_number: str = None,
        called_number: str = None,
        ext_info: str = None,
        app_name: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.account_type = account_type
        self.account_id = account_id
        self.command_code = command_code
        self.calling_number = calling_number
        self.called_number = called_number
        self.ext_info = ext_info
        self.app_name = app_name

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
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.command_code is not None:
            result['CommandCode'] = self.command_code
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CommandCode') is not None:
            self.command_code = m.get('CommandCode')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class StartMicroOutboundResponseBody(TeaModel):
    def __init__(
        self,
        invoke_create_time: str = None,
        request_id: str = None,
        message: str = None,
        invoke_cmd_id: str = None,
        customer_info: str = None,
        code: str = None,
    ):
        self.invoke_create_time = invoke_create_time
        self.request_id = request_id
        self.message = message
        self.invoke_cmd_id = invoke_cmd_id
        self.customer_info = customer_info
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_create_time is not None:
            result['InvokeCreateTime'] = self.invoke_create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.invoke_cmd_id is not None:
            result['InvokeCmdId'] = self.invoke_cmd_id
        if self.customer_info is not None:
            result['CustomerInfo'] = self.customer_info
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeCreateTime') is not None:
            self.invoke_create_time = m.get('InvokeCreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InvokeCmdId') is not None:
            self.invoke_cmd_id = m.get('InvokeCmdId')
        if m.get('CustomerInfo') is not None:
            self.customer_info = m.get('CustomerInfo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class StartMicroOutboundResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartMicroOutboundResponseBody = None,
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
            temp_model = StartMicroOutboundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendHotlineServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        type: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SuspendHotlineServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendHotlineServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendHotlineServiceResponseBody = None,
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
            temp_model = SuspendHotlineServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentStatisticsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
        time_latitude_type: str = None,
        exist_department_grouping: bool = None,
        exist_agent_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        return self


class GetAgentStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
        time_latitude_type: str = None,
        exist_department_grouping: bool = None,
        exist_agent_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        return self


class GetAgentStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetAgentStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetAgentStatisticsResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetAgentStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAgentStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentStatisticsResponseBody = None,
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
            temp_model = GetAgentStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOuterAccountRequest(TeaModel):
    def __init__(
        self,
        outer_account_id: str = None,
        outer_account_type: str = None,
        outer_account_name: str = None,
        avatar: str = None,
        real_name: str = None,
        outer_department_id: str = None,
        outer_group_ids: str = None,
        ext: str = None,
        outer_group_type: str = None,
        outer_department_type: str = None,
    ):
        self.outer_account_id = outer_account_id
        self.outer_account_type = outer_account_type
        self.outer_account_name = outer_account_name
        self.avatar = avatar
        self.real_name = real_name
        self.outer_department_id = outer_department_id
        self.outer_group_ids = outer_group_ids
        self.ext = ext
        self.outer_group_type = outer_group_type
        self.outer_department_type = outer_department_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id
        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type
        if self.outer_account_name is not None:
            result['OuterAccountName'] = self.outer_account_name
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.outer_department_id is not None:
            result['OuterDepartmentId'] = self.outer_department_id
        if self.outer_group_ids is not None:
            result['OuterGroupIds'] = self.outer_group_ids
        if self.ext is not None:
            result['Ext'] = self.ext
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        if self.outer_department_type is not None:
            result['OuterDepartmentType'] = self.outer_department_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')
        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')
        if m.get('OuterAccountName') is not None:
            self.outer_account_name = m.get('OuterAccountName')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('OuterDepartmentId') is not None:
            self.outer_department_id = m.get('OuterDepartmentId')
        if m.get('OuterGroupIds') is not None:
            self.outer_group_ids = m.get('OuterGroupIds')
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        if m.get('OuterDepartmentType') is not None:
            self.outer_department_type = m.get('OuterDepartmentType')
        return self


class UpdateOuterAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateOuterAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateOuterAccountResponseBody = None,
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
            temp_model = UpdateOuterAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineWaitingNumberRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetHotlineWaitingNumberResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: int = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotlineWaitingNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineWaitingNumberResponseBody = None,
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
            temp_model = GetHotlineWaitingNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HoldCallRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.call_id = call_id
        self.job_id = job_id
        self.connection_id = connection_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        return self


class HoldCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HoldCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HoldCallResponseBody = None,
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
            temp_model = HoldCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSeatInformationRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        exist_department_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids = dep_ids
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.dep_ids is not None:
            result['depIds'] = self.dep_ids
        if self.exist_department_grouping is not None:
            result['existDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('depIds') is not None:
            self.dep_ids = m.get('depIds')
        if m.get('existDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('existDepartmentGrouping')
        return self


class GetSeatInformationShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids_shrink: str = None,
        exist_department_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['depIds'] = self.dep_ids_shrink
        if self.exist_department_grouping is not None:
            result['existDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        if m.get('depIds') is not None:
            self.dep_ids_shrink = m.get('depIds')
        if m.get('existDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('existDepartmentGrouping')
        return self


class GetSeatInformationResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rowr: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rowr = rowr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rowr is not None:
            result['Rowr'] = self.rowr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rowr') is not None:
            self.rowr = m.get('Rowr')
        return self


class GetSeatInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetSeatInformationResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSeatInformationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSeatInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSeatInformationResponseBody = None,
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
            temp_model = GetSeatInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRtcTokenRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        account_name: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 账号名称
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetRtcTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        token: str = None,
        rtc_id: str = None,
        account_name: str = None,
    ):
        # token信息
        self.token = token
        # rtcId
        self.rtc_id = rtc_id
        # 账号名
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.rtc_id is not None:
            result['RtcId'] = self.rtc_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('RtcId') is not None:
            self.rtc_id = m.get('RtcId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetRtcTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: GetRtcTokenResponseBodyData = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 是否成功
        self.success = success
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            temp_model = GetRtcTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetRtcTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRtcTokenResponseBody = None,
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
            temp_model = GetRtcTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupAndAgentStatusSummaryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupAndAgentStatusSummaryShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupAndAgentStatusSummaryResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 每页的数量
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupAndAgentStatusSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetSkillGroupAndAgentStatusSummaryResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 接口调用是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupAndAgentStatusSummaryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupAndAgentStatusSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSkillGroupAndAgentStatusSummaryResponseBody = None,
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
            temp_model = GetSkillGroupAndAgentStatusSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRecordDataRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        acid: str = None,
    ):
        self.instance_id = instance_id
        self.acid = acid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class GetRecordDataResponseBodyData(TeaModel):
    def __init__(
        self,
        oss_link: str = None,
        acid: str = None,
    ):
        self.oss_link = oss_link
        self.acid = acid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_link is not None:
            result['OssLink'] = self.oss_link
        if self.acid is not None:
            result['Acid'] = self.acid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssLink') is not None:
            self.oss_link = m.get('OssLink')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        return self


class GetRecordDataResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetRecordDataResponseBodyData = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetRecordDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetRecordDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRecordDataResponseBody = None,
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
            temp_model = GetRecordDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupLatitudeStateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupLatitudeStateShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupLatitudeStateResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 每页的数量
        self.page_size = page_size
        # 总共记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupLatitudeStateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetSkillGroupLatitudeStateResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 接口调用是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupLatitudeStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupLatitudeStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSkillGroupLatitudeStateResponseBody = None,
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
            temp_model = GetSkillGroupLatitudeStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQualityRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        id: int = None,
    ):
        self.instance_id = instance_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteQualityRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQualityRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteQualityRuleResponseBody = None,
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
            temp_model = DeleteQualityRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendOutboundTaskRequest(TeaModel):
    def __init__(
        self,
        outbound_task_id: int = None,
        instance_id: str = None,
    ):
        self.outbound_task_id = outbound_task_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SuspendOutboundTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendOutboundTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendOutboundTaskResponseBody = None,
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
            temp_model = SuspendOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineServiceStatisticsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetHotlineServiceStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetHotlineServiceStatisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetHotlineServiceStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetHotlineServiceStatisticsResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetHotlineServiceStatisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetHotlineServiceStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineServiceStatisticsResponseBody = None,
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
            temp_model = GetHotlineServiceStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditQualityProjectRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        project_id: int = None,
        project_name: str = None,
        check_freq_type: int = None,
        project_version: int = None,
        scope_type: int = None,
        time_range_start: str = None,
        time_range_end: str = None,
        analysis_ids: List[int] = None,
        dep_list: List[int] = None,
        group_list: List[int] = None,
        servicer_list: List[str] = None,
        channel_touch_type: List[int] = None,
    ):
        self.instance_id = instance_id
        self.project_id = project_id
        self.project_name = project_name
        self.check_freq_type = check_freq_type
        self.project_version = project_version
        self.scope_type = scope_type
        self.time_range_start = time_range_start
        self.time_range_end = time_range_end
        self.analysis_ids = analysis_ids
        self.dep_list = dep_list
        self.group_list = group_list
        self.servicer_list = servicer_list
        self.channel_touch_type = channel_touch_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.project_version is not None:
            result['ProjectVersion'] = self.project_version
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start
        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end
        if self.analysis_ids is not None:
            result['AnalysisIds'] = self.analysis_ids
        if self.dep_list is not None:
            result['DepList'] = self.dep_list
        if self.group_list is not None:
            result['GroupList'] = self.group_list
        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list
        if self.channel_touch_type is not None:
            result['ChannelTouchType'] = self.channel_touch_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('ProjectVersion') is not None:
            self.project_version = m.get('ProjectVersion')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')
        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')
        if m.get('AnalysisIds') is not None:
            self.analysis_ids = m.get('AnalysisIds')
        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')
        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')
        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')
        if m.get('ChannelTouchType') is not None:
            self.channel_touch_type = m.get('ChannelTouchType')
        return self


class EditQualityProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        version: int = None,
        project_id: int = None,
        instance_id: str = None,
    ):
        self.version = version
        self.project_id = project_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class EditQualityProjectResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[EditQualityProjectResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = EditQualityProjectResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditQualityProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditQualityProjectResponseBody = None,
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
            temp_model = EditQualityProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOuterOrderedNumbersRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code

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
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        return self


class ListOuterOrderedNumbersResponseBody(TeaModel):
    def __init__(
        self,
        numbers: List[str] = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.numbers = numbers
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListOuterOrderedNumbersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOuterOrderedNumbersResponseBody = None,
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
            temp_model = ListOuterOrderedNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentBasisStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        return self


class GetAgentBasisStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        return self


class GetAgentBasisStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetAgentBasisStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetAgentBasisStatusResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetAgentBasisStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAgentBasisStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentBasisStatusResponseBody = None,
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
            temp_model = GetAgentBasisStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        touch_start_time: str = None,
        touch_end_time: str = None,
        channel_type: str = None,
        hit_status: int = None,
        group_ids: List[int] = None,
        quality_rule_ids: List[int] = None,
        project_ids: List[int] = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.touch_start_time = touch_start_time
        self.touch_end_time = touch_end_time
        self.channel_type = channel_type
        self.hit_status = hit_status
        self.group_ids = group_ids
        self.quality_rule_ids = quality_rule_ids
        self.project_ids = project_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.touch_start_time is not None:
            result['TouchStartTime'] = self.touch_start_time
        if self.touch_end_time is not None:
            result['TouchEndTime'] = self.touch_end_time
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.hit_status is not None:
            result['HitStatus'] = self.hit_status
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.quality_rule_ids is not None:
            result['QualityRuleIds'] = self.quality_rule_ids
        if self.project_ids is not None:
            result['ProjectIds'] = self.project_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TouchStartTime') is not None:
            self.touch_start_time = m.get('TouchStartTime')
        if m.get('TouchEndTime') is not None:
            self.touch_end_time = m.get('TouchEndTime')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('HitStatus') is not None:
            self.hit_status = m.get('HitStatus')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('QualityRuleIds') is not None:
            self.quality_rule_ids = m.get('QualityRuleIds')
        if m.get('ProjectIds') is not None:
            self.project_ids = m.get('ProjectIds')
        return self


class GetQualityResultResponseBodyDataQualityResultResponseList(TeaModel):
    def __init__(
        self,
        touch_id: str = None,
        servicer_name: str = None,
        member_name: str = None,
        project_name: str = None,
        project_id: str = None,
        channel_type: str = None,
        channel_type_name: str = None,
        touch_start_time: str = None,
        servicer_id: str = None,
        rule_name: str = None,
        rule_id: str = None,
        group_name: str = None,
        group_id: str = None,
        instance_name: str = None,
        hit_status: bool = None,
        hit_detail: str = None,
    ):
        self.touch_id = touch_id
        self.servicer_name = servicer_name
        self.member_name = member_name
        self.project_name = project_name
        self.project_id = project_id
        self.channel_type = channel_type
        self.channel_type_name = channel_type_name
        self.touch_start_time = touch_start_time
        self.servicer_id = servicer_id
        self.rule_name = rule_name
        self.rule_id = rule_id
        self.group_name = group_name
        self.group_id = group_id
        self.instance_name = instance_name
        self.hit_status = hit_status
        self.hit_detail = hit_detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.channel_type_name is not None:
            result['ChannelTypeName'] = self.channel_type_name
        if self.touch_start_time is not None:
            result['TouchStartTime'] = self.touch_start_time
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.hit_status is not None:
            result['HitStatus'] = self.hit_status
        if self.hit_detail is not None:
            result['HitDetail'] = self.hit_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ChannelTypeName') is not None:
            self.channel_type_name = m.get('ChannelTypeName')
        if m.get('TouchStartTime') is not None:
            self.touch_start_time = m.get('TouchStartTime')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('HitStatus') is not None:
            self.hit_status = m.get('HitStatus')
        if m.get('HitDetail') is not None:
            self.hit_detail = m.get('HitDetail')
        return self


class GetQualityResultResponseBodyData(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        quality_result_response_list: List[GetQualityResultResponseBodyDataQualityResultResponseList] = None,
        page_size: int = None,
        total_num: int = None,
    ):
        self.page_no = page_no
        self.quality_result_response_list = quality_result_response_list
        self.page_size = page_size
        self.total_num = total_num

    def validate(self):
        if self.quality_result_response_list:
            for k in self.quality_result_response_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        result['QualityResultResponseList'] = []
        if self.quality_result_response_list is not None:
            for k in self.quality_result_response_list:
                result['QualityResultResponseList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.quality_result_response_list = []
        if m.get('QualityResultResponseList') is not None:
            for k in m.get('QualityResultResponseList'):
                temp_model = GetQualityResultResponseBodyDataQualityResultResponseList()
                self.quality_result_response_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        return self


class GetQualityResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetQualityResultResponseBodyData = None,
        code: str = None,
        channel_type_name: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.channel_type_name = channel_type_name
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.channel_type_name is not None:
            result['ChannelTypeName'] = self.channel_type_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetQualityResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ChannelTypeName') is not None:
            self.channel_type_name = m.get('ChannelTypeName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQualityResultResponseBody = None,
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
            temp_model = GetQualityResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIndexCurrentValueRequest(TeaModel):
    def __init__(
        self,
        dep_ids: str = None,
        group_ids: str = None,
        instance_id: str = None,
    ):
        self.dep_ids = dep_ids
        self.group_ids = group_ids
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetIndexCurrentValueResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[Dict[str, Any]] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIndexCurrentValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIndexCurrentValueResponseBody = None,
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
            temp_model = GetIndexCurrentValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateWebSocketSignRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GenerateWebSocketSignResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GenerateWebSocketSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateWebSocketSignResponseBody = None,
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
            temp_model = GenerateWebSocketSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAgentRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        display_name: str = None,
        skill_group_id: List[int] = None,
        skill_group_id_list: List[int] = None,
    ):
        # js sdk中自动生成的鉴权token
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.display_name = display_name
        self.skill_group_id = skill_group_id
        self.skill_group_id_list = skill_group_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_id_list is not None:
            result['SkillGroupIdList'] = self.skill_group_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupIdList') is not None:
            self.skill_group_id_list = m.get('SkillGroupIdList')
        return self


class CreateAgentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: int = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class CreateAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAgentResponseBody = None,
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
            temp_model = CreateAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTaskDetailRequest(TeaModel):
    def __init__(
        self,
        outbound_task_id: str = None,
        status_list: str = None,
        end_reason_list: str = None,
        skill_group: str = None,
        servicer_name: str = None,
        servicer_id: str = None,
        priority_list: str = None,
        task_id: int = None,
        ani: str = None,
        dnis: str = None,
        sid: str = None,
        department_id_list: str = None,
        instance_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.outbound_task_id = outbound_task_id
        self.status_list = status_list
        self.end_reason_list = end_reason_list
        self.skill_group = skill_group
        self.servicer_name = servicer_name
        self.servicer_id = servicer_id
        self.priority_list = priority_list
        self.task_id = task_id
        self.ani = ani
        self.dnis = dnis
        self.sid = sid
        self.department_id_list = department_id_list
        self.instance_id = instance_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.end_reason_list is not None:
            result['EndReasonList'] = self.end_reason_list
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.priority_list is not None:
            result['PriorityList'] = self.priority_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.ani is not None:
            result['Ani'] = self.ani
        if self.dnis is not None:
            result['Dnis'] = self.dnis
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.department_id_list is not None:
            result['DepartmentIdList'] = self.department_id_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('EndReasonList') is not None:
            self.end_reason_list = m.get('EndReasonList')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('PriorityList') is not None:
            self.priority_list = m.get('PriorityList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('DepartmentIdList') is not None:
            self.department_id_list = m.get('DepartmentIdList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTaskDetailResponseBodyDataList(TeaModel):
    def __init__(
        self,
        status: int = None,
        member_name: str = None,
        servicer_name: str = None,
        outbound_num: int = None,
        retry_time: str = None,
        priority: int = None,
        gmt_modified: int = None,
        dnis: str = None,
        servicer_id: int = None,
        outbound_task_id: int = None,
        bu_id: int = None,
        end_reason: int = None,
        gmt_create: int = None,
        department_id: int = None,
        ani: str = None,
        member_id: int = None,
        skill_group: int = None,
        ext_attrs: str = None,
        id: int = None,
    ):
        self.status = status
        self.member_name = member_name
        self.servicer_name = servicer_name
        self.outbound_num = outbound_num
        self.retry_time = retry_time
        self.priority = priority
        self.gmt_modified = gmt_modified
        self.dnis = dnis
        self.servicer_id = servicer_id
        self.outbound_task_id = outbound_task_id
        self.bu_id = bu_id
        self.end_reason = end_reason
        self.gmt_create = gmt_create
        self.department_id = department_id
        self.ani = ani
        self.member_id = member_id
        self.skill_group = skill_group
        self.ext_attrs = ext_attrs
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.outbound_num is not None:
            result['OutboundNum'] = self.outbound_num
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.dnis is not None:
            result['Dnis'] = self.dnis
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.end_reason is not None:
            result['EndReason'] = self.end_reason
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.ani is not None:
            result['Ani'] = self.ani
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('OutboundNum') is not None:
            self.outbound_num = m.get('OutboundNum')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryTaskDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        total_results: str = None,
        current_page: str = None,
        list: List[QueryTaskDetailResponseBodyDataList] = None,
        page_size: str = None,
    ):
        self.total_results = total_results
        self.current_page = current_page
        self.list = list
        self.page_size = page_size

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryTaskDetailResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: str = None,
        data: QueryTaskDetailResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = QueryTaskDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTaskDetailResponseBody = None,
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
            temp_model = QueryTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditQualityRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        rule_tag: int = None,
        match_type: int = None,
        quality_rule_id: int = None,
        key_words: List[str] = None,
    ):
        self.instance_id = instance_id
        self.name = name
        self.rule_tag = rule_tag
        self.match_type = match_type
        self.quality_rule_id = quality_rule_id
        self.key_words = key_words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.quality_rule_id is not None:
            result['QualityRuleId'] = self.quality_rule_id
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('QualityRuleId') is not None:
            self.quality_rule_id = m.get('QualityRuleId')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        return self


class EditQualityRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EditQualityRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditQualityRuleResponseBody = None,
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
            temp_model = EditQualityRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMcuLvsIpRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # 实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetMcuLvsIpResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # success
        self.success = success
        # error code
        self.code = code
        # error message
        self.message = message
        # result data
        self.data = data

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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetMcuLvsIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMcuLvsIpResponseBody = None,
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
            temp_model = GetMcuLvsIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDepGroupTreeDataRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        agent_id: int = None,
    ):
        # 租户实例ID
        self.instance_id = instance_id
        # 坐席ID
        self.agent_id = agent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        return self


class GetDepGroupTreeDataResponseBodyDataGroupDTOS(TeaModel):
    def __init__(
        self,
        skill_group_id: int = None,
        name: str = None,
    ):
        # skillGroupId
        self.skill_group_id = skill_group_id
        # name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetDepGroupTreeDataResponseBodyData(TeaModel):
    def __init__(
        self,
        dep_group_name: str = None,
        dep_group_id: str = None,
        group_dtos: List[GetDepGroupTreeDataResponseBodyDataGroupDTOS] = None,
    ):
        # depGroupName
        self.dep_group_name = dep_group_name
        # depGroupId
        self.dep_group_id = dep_group_id
        # groupDTOS
        self.group_dtos = group_dtos

    def validate(self):
        if self.group_dtos:
            for k in self.group_dtos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dep_group_name is not None:
            result['DepGroupName'] = self.dep_group_name
        if self.dep_group_id is not None:
            result['DepGroupId'] = self.dep_group_id
        result['GroupDTOS'] = []
        if self.group_dtos is not None:
            for k in self.group_dtos:
                result['GroupDTOS'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepGroupName') is not None:
            self.dep_group_name = m.get('DepGroupName')
        if m.get('DepGroupId') is not None:
            self.dep_group_id = m.get('DepGroupId')
        self.group_dtos = []
        if m.get('GroupDTOS') is not None:
            for k in m.get('GroupDTOS'):
                temp_model = GetDepGroupTreeDataResponseBodyDataGroupDTOS()
                self.group_dtos.append(temp_model.from_map(k))
        return self


class GetDepGroupTreeDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: List[GetDepGroupTreeDataResponseBodyData] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # Message
        self.message = message
        # Code
        self.code = code
        # Success
        self.success = success
        # Data
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetDepGroupTreeDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetDepGroupTreeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDepGroupTreeDataResponseBody = None,
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
            temp_model = GetDepGroupTreeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAgentRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        # js sdk中自动生成的鉴权token
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DeleteAgentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class DeleteAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAgentResponseBody = None,
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
            temp_model = DeleteAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        member_id: int = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 会员ID
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        return self


class GetCustomerInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        nick: str = None,
        photo: str = None,
        user_id: int = None,
        real_name: str = None,
        outer_id: str = None,
        customize_fields: Dict[str, Any] = None,
    ):
        # 昵称
        self.nick = nick
        # 头像
        self.photo = photo
        # 会员ID
        self.user_id = user_id
        # 真实姓名
        self.real_name = real_name
        # 外部ID
        self.outer_id = outer_id
        # 自定义字段
        self.customize_fields = customize_fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.photo is not None:
            result['Photo'] = self.photo
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.real_name is not None:
            result['RealName'] = self.real_name
        if self.outer_id is not None:
            result['OuterId'] = self.outer_id
        if self.customize_fields is not None:
            result['CustomizeFields'] = self.customize_fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Photo') is not None:
            self.photo = m.get('Photo')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RealName') is not None:
            self.real_name = m.get('RealName')
        if m.get('OuterId') is not None:
            self.outer_id = m.get('OuterId')
        if m.get('CustomizeFields') is not None:
            self.customize_fields = m.get('CustomizeFields')
        return self


class GetCustomerInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: bool = None,
        data: GetCustomerInfoResponseBodyData = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 错误信息
        self.message = message
        # 错误码
        self.code = code
        # 是否请求成功
        self.success = success
        # 会员信息
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetCustomerInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetCustomerInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCustomerInfoResponseBody = None,
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
            temp_model = GetCustomerInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineAgentDetailReportRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        start_date: int = None,
        end_date: int = None,
        instance_id: str = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date
        self.instance_id = instance_id
        self.dep_ids = dep_ids
        self.group_ids = group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        return self


class GetHotlineAgentDetailReportResponseBodyDataColumns(TeaModel):
    def __init__(
        self,
        key: str = None,
        title: str = None,
    ):
        self.key = key
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetHotlineAgentDetailReportResponseBodyData(TeaModel):
    def __init__(
        self,
        rows: List[Dict[str, Any]] = None,
        page_size: int = None,
        total: int = None,
        columns: List[GetHotlineAgentDetailReportResponseBodyDataColumns] = None,
        page: int = None,
    ):
        self.rows = rows
        self.page_size = page_size
        self.total = total
        self.columns = columns
        self.page = page

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = GetHotlineAgentDetailReportResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetHotlineAgentDetailReportResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetHotlineAgentDetailReportResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineAgentDetailReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotlineAgentDetailReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineAgentDetailReportResponseBody = None,
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
            temp_model = GetHotlineAgentDetailReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCcoSmartCallRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        called_show_number: str = None,
        called_number: str = None,
        voice_code: str = None,
        out_id: str = None,
        play_times: int = None,
        volume: int = None,
        speed: int = None,
        asr_model_id: str = None,
        asr_base_id: str = None,
        asr_als_am_id: str = None,
        asr_vocabulary_id: str = None,
        record_flag: bool = None,
        pause_time: int = None,
        mute_time: int = None,
        action_code_break: bool = None,
        dynamic_id: str = None,
        early_media_asr: bool = None,
        voice_code_param: str = None,
        session_timeout: int = None,
        action_code_time_break: int = None,
        tts_conf: bool = None,
        tts_style: str = None,
        tts_volume: int = None,
        tts_speed: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.called_show_number = called_show_number
        self.called_number = called_number
        self.voice_code = voice_code
        self.out_id = out_id
        self.play_times = play_times
        self.volume = volume
        self.speed = speed
        self.asr_model_id = asr_model_id
        self.asr_base_id = asr_base_id
        self.asr_als_am_id = asr_als_am_id
        self.asr_vocabulary_id = asr_vocabulary_id
        self.record_flag = record_flag
        self.pause_time = pause_time
        self.mute_time = mute_time
        self.action_code_break = action_code_break
        self.dynamic_id = dynamic_id
        self.early_media_asr = early_media_asr
        self.voice_code_param = voice_code_param
        self.session_timeout = session_timeout
        self.action_code_time_break = action_code_time_break
        self.tts_conf = tts_conf
        self.tts_style = tts_style
        self.tts_volume = tts_volume
        self.tts_speed = tts_speed

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
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id
        if self.asr_base_id is not None:
            result['AsrBaseId'] = self.asr_base_id
        if self.asr_als_am_id is not None:
            result['AsrAlsAmId'] = self.asr_als_am_id
        if self.asr_vocabulary_id is not None:
            result['AsrVocabularyId'] = self.asr_vocabulary_id
        if self.record_flag is not None:
            result['RecordFlag'] = self.record_flag
        if self.pause_time is not None:
            result['PauseTime'] = self.pause_time
        if self.mute_time is not None:
            result['MuteTime'] = self.mute_time
        if self.action_code_break is not None:
            result['ActionCodeBreak'] = self.action_code_break
        if self.dynamic_id is not None:
            result['DynamicId'] = self.dynamic_id
        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr
        if self.voice_code_param is not None:
            result['VoiceCodeParam'] = self.voice_code_param
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.action_code_time_break is not None:
            result['ActionCodeTimeBreak'] = self.action_code_time_break
        if self.tts_conf is not None:
            result['TtsConf'] = self.tts_conf
        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style
        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume
        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')
        if m.get('AsrBaseId') is not None:
            self.asr_base_id = m.get('AsrBaseId')
        if m.get('AsrAlsAmId') is not None:
            self.asr_als_am_id = m.get('AsrAlsAmId')
        if m.get('AsrVocabularyId') is not None:
            self.asr_vocabulary_id = m.get('AsrVocabularyId')
        if m.get('RecordFlag') is not None:
            self.record_flag = m.get('RecordFlag')
        if m.get('PauseTime') is not None:
            self.pause_time = m.get('PauseTime')
        if m.get('MuteTime') is not None:
            self.mute_time = m.get('MuteTime')
        if m.get('ActionCodeBreak') is not None:
            self.action_code_break = m.get('ActionCodeBreak')
        if m.get('DynamicId') is not None:
            self.dynamic_id = m.get('DynamicId')
        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')
        if m.get('VoiceCodeParam') is not None:
            self.voice_code_param = m.get('VoiceCodeParam')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('ActionCodeTimeBreak') is not None:
            self.action_code_time_break = m.get('ActionCodeTimeBreak')
        if m.get('TtsConf') is not None:
            self.tts_conf = m.get('TtsConf')
        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')
        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')
        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')
        return self


class SendCcoSmartCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SendCcoSmartCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendCcoSmartCallResponseBody = None,
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
            temp_model = SendCcoSmartCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChatRecordDetailRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        close_time_end: int = None,
        current_page: int = None,
        page_size: int = None,
        close_time_start: int = None,
    ):
        # clientToken
        self.client_token = client_token
        # 实例id
        self.instance_id = instance_id
        # 在线挂断的时间范围
        self.close_time_end = close_time_end
        # 当前页
        self.current_page = current_page
        # 每页数据量
        self.page_size = page_size
        # 在线挂断的时间范围
        self.close_time_start = close_time_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.close_time_end is not None:
            result['CloseTimeEnd'] = self.close_time_end
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.close_time_start is not None:
            result['CloseTimeStart'] = self.close_time_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CloseTimeEnd') is not None:
            self.close_time_end = m.get('CloseTimeEnd')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CloseTimeStart') is not None:
            self.close_time_start = m.get('CloseTimeStart')
        return self


class ListChatRecordDetailResponseBodyResultDataDataMessageList(TeaModel):
    def __init__(
        self,
        sender_name: str = None,
        content: str = None,
        sender_type: int = None,
        create_time: int = None,
        msg_type: str = None,
    ):
        self.sender_name = sender_name
        self.content = content
        self.sender_type = sender_type
        self.create_time = create_time
        self.msg_type = msg_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sender_name is not None:
            result['SenderName'] = self.sender_name
        if self.content is not None:
            result['Content'] = self.content
        if self.sender_type is not None:
            result['SenderType'] = self.sender_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.msg_type is not None:
            result['MsgType'] = self.msg_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SenderName') is not None:
            self.sender_name = m.get('SenderName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('SenderType') is not None:
            self.sender_type = m.get('SenderType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')
        return self


class ListChatRecordDetailResponseBodyResultDataData(TeaModel):
    def __init__(
        self,
        servicer_name: str = None,
        start_time: int = None,
        end_time: int = None,
        message_list: List[ListChatRecordDetailResponseBodyResultDataDataMessageList] = None,
    ):
        self.servicer_name = servicer_name
        # 在线开始时间
        self.start_time = start_time
        # 在线结束时间
        self.end_time = end_time
        # 在线会话详细信息
        self.message_list = message_list

    def validate(self):
        if self.message_list:
            for k in self.message_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        result['MessageList'] = []
        if self.message_list is not None:
            for k in self.message_list:
                result['MessageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        self.message_list = []
        if m.get('MessageList') is not None:
            for k in m.get('MessageList'):
                temp_model = ListChatRecordDetailResponseBodyResultDataDataMessageList()
                self.message_list.append(temp_model.from_map(k))
        return self


class ListChatRecordDetailResponseBodyResultData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        total_results: int = None,
        total_page: int = None,
        one_page_size: int = None,
        data: List[ListChatRecordDetailResponseBodyResultDataData] = None,
    ):
        self.current_page = current_page
        self.total_results = total_results
        self.total_page = total_page
        self.one_page_size = one_page_size
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListChatRecordDetailResponseBodyResultDataData()
                self.data.append(temp_model.from_map(k))
        return self


class ListChatRecordDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        result_data: ListChatRecordDetailResponseBodyResultData = None,
        code: str = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # httpStatusCode
        self.http_status_code = http_status_code
        # data
        self.result_data = result_data
        # code
        self.code = code
        # success
        self.success = success

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ResultData') is not None:
            temp_model = ListChatRecordDetailResponseBodyResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListChatRecordDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListChatRecordDetailResponseBody = None,
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
            temp_model = ListChatRecordDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSkillGroupRequest(TeaModel):
    def __init__(
        self,
        outer_group_id: str = None,
        outer_group_name: str = None,
        outer_group_type: str = None,
        outer_department_id: str = None,
        outer_department_type: str = None,
    ):
        self.outer_group_id = outer_group_id
        self.outer_group_name = outer_group_name
        self.outer_group_type = outer_group_type
        self.outer_department_id = outer_department_id
        self.outer_department_type = outer_department_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_group_id is not None:
            result['OuterGroupId'] = self.outer_group_id
        if self.outer_group_name is not None:
            result['OuterGroupName'] = self.outer_group_name
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        if self.outer_department_id is not None:
            result['OuterDepartmentId'] = self.outer_department_id
        if self.outer_department_type is not None:
            result['OuterDepartmentType'] = self.outer_department_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterGroupId') is not None:
            self.outer_group_id = m.get('OuterGroupId')
        if m.get('OuterGroupName') is not None:
            self.outer_group_name = m.get('OuterGroupName')
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        if m.get('OuterDepartmentId') is not None:
            self.outer_department_id = m.get('OuterDepartmentId')
        if m.get('OuterDepartmentType') is not None:
            self.outer_department_type = m.get('OuterDepartmentType')
        return self


class AddSkillGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSkillGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSkillGroupResponseBody = None,
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
            temp_model = AddSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HangupCallRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.call_id = call_id
        self.job_id = job_id
        self.connection_id = connection_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        return self


class HangupCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HangupCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HangupCallResponseBody = None,
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
            temp_model = HangupCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSkillGroupRequest(TeaModel):
    def __init__(
        self,
        outer_group_type: str = None,
        outer_group_id: str = None,
    ):
        self.outer_group_type = outer_group_type
        self.outer_group_id = outer_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        if self.outer_group_id is not None:
            result['OuterGroupId'] = self.outer_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        if m.get('OuterGroupId') is not None:
            self.outer_group_id = m.get('OuterGroupId')
        return self


class DeleteSkillGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSkillGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSkillGroupResponseBody = None,
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
            temp_model = DeleteSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQualityProjectRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        check_freq_type: int = None,
        scope_type: int = None,
        time_range_start: str = None,
        time_range_end: str = None,
        instance_id: str = None,
        channel_touch_type: List[int] = None,
        dep_list: List[int] = None,
        group_list: List[int] = None,
        servicer_list: List[str] = None,
        analysis_ids: List[int] = None,
    ):
        self.project_name = project_name
        self.check_freq_type = check_freq_type
        self.scope_type = scope_type
        self.time_range_start = time_range_start
        self.time_range_end = time_range_end
        self.instance_id = instance_id
        self.channel_touch_type = channel_touch_type
        self.dep_list = dep_list
        self.group_list = group_list
        self.servicer_list = servicer_list
        self.analysis_ids = analysis_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start
        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.channel_touch_type is not None:
            result['ChannelTouchType'] = self.channel_touch_type
        if self.dep_list is not None:
            result['DepList'] = self.dep_list
        if self.group_list is not None:
            result['GroupList'] = self.group_list
        if self.servicer_list is not None:
            result['ServicerList'] = self.servicer_list
        if self.analysis_ids is not None:
            result['AnalysisIds'] = self.analysis_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')
        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ChannelTouchType') is not None:
            self.channel_touch_type = m.get('ChannelTouchType')
        if m.get('DepList') is not None:
            self.dep_list = m.get('DepList')
        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')
        if m.get('ServicerList') is not None:
            self.servicer_list = m.get('ServicerList')
        if m.get('AnalysisIds') is not None:
            self.analysis_ids = m.get('AnalysisIds')
        return self


class CreateQualityProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        version: int = None,
        project_id: int = None,
        instance_id: str = None,
    ):
        self.version = version
        self.project_id = project_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateQualityProjectResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateQualityProjectResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateQualityProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQualityProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateQualityProjectResponseBody = None,
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
            temp_model = CreateQualityProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySkillGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        client_token: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class QuerySkillGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        description: str = None,
        channel_type: int = None,
        skill_group_name: str = None,
        skill_group_id: int = None,
    ):
        self.display_name = display_name
        self.description = description
        self.channel_type = channel_type
        self.skill_group_name = skill_group_name
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        return self


class QuerySkillGroupsResponseBody(TeaModel):
    def __init__(
        self,
        one_page_size: int = None,
        total_page: int = None,
        request_id: str = None,
        current_page: int = None,
        total_results: int = None,
        data: List[QuerySkillGroupsResponseBodyData] = None,
    ):
        self.one_page_size = one_page_size
        self.total_page = total_page
        self.request_id = request_id
        self.current_page = current_page
        self.total_results = total_results
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QuerySkillGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class QuerySkillGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySkillGroupsResponseBody = None,
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
            temp_model = QuerySkillGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQualityRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        rule_tag: int = None,
        match_type: int = None,
        key_words: List[str] = None,
    ):
        self.instance_id = instance_id
        self.name = name
        self.rule_tag = rule_tag
        self.match_type = match_type
        self.key_words = key_words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        return self


class CreateQualityRuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateQualityRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateQualityRuleResponseBody = None,
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
            temp_model = CreateQualityRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRolesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
    ):
        # clientToken
        self.client_token = client_token
        # 租户实例id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListRolesResponseBodyData(TeaModel):
    def __init__(
        self,
        role_id: int = None,
        create_time: str = None,
        bu_id: int = None,
        title: str = None,
        code: str = None,
        description: str = None,
        role_group_id: int = None,
        role_group_name: str = None,
    ):
        # 角色id
        self.role_id = role_id
        # 创建时间
        self.create_time = create_time
        # 租户id
        self.bu_id = bu_id
        # 角色名称
        self.title = title
        # 角色code
        self.code = code
        # 角色描述
        self.description = description
        # 所属角色组id
        self.role_group_id = role_group_id
        # 所属角色组名称
        self.role_group_name = role_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.title is not None:
            result['Title'] = self.title
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.role_group_id is not None:
            result['RoleGroupId'] = self.role_group_id
        if self.role_group_name is not None:
            result['RoleGroupName'] = self.role_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RoleGroupId') is not None:
            self.role_group_id = m.get('RoleGroupId')
        if m.get('RoleGroupName') is not None:
            self.role_group_name = m.get('RoleGroupName')
        return self


class ListRolesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        data: List[ListRolesResponseBodyData] = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # httpStatusCode
        self.http_status_code = http_status_code
        # data
        self.data = data
        # success
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListRolesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRolesResponseBody = None,
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
            temp_model = ListRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineCallActionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        act: int = None,
        from_source: str = None,
        biz: str = None,
        acc: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.act = act
        self.from_source = from_source
        self.biz = biz
        self.acc = acc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.act is not None:
            result['Act'] = self.act
        if self.from_source is not None:
            result['FromSource'] = self.from_source
        if self.biz is not None:
            result['Biz'] = self.biz
        if self.acc is not None:
            result['Acc'] = self.acc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Act') is not None:
            self.act = m.get('Act')
        if m.get('FromSource') is not None:
            self.from_source = m.get('FromSource')
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')
        return self


class GetHotlineCallActionResponseBodyData(TeaModel):
    def __init__(
        self,
        touch_id: int = None,
        dep_id: int = None,
        member_name: str = None,
        servicer_name: str = None,
        channel_type: int = None,
        action_id: int = None,
        callout_name: str = None,
        sub_touch_id: int = None,
        servicer_id: int = None,
        bu_id: int = None,
        callout_id: int = None,
        case_id: int = None,
        channel_id: str = None,
        is_transfer: str = None,
        member_id: int = None,
        task_id: int = None,
        member_list: str = None,
    ):
        self.touch_id = touch_id
        self.dep_id = dep_id
        self.member_name = member_name
        self.servicer_name = servicer_name
        self.channel_type = channel_type
        self.action_id = action_id
        self.callout_name = callout_name
        self.sub_touch_id = sub_touch_id
        self.servicer_id = servicer_id
        self.bu_id = bu_id
        self.callout_id = callout_id
        self.case_id = case_id
        self.channel_id = channel_id
        self.is_transfer = is_transfer
        self.member_id = member_id
        self.task_id = task_id
        self.member_list = member_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.dep_id is not None:
            result['DepId'] = self.dep_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.action_id is not None:
            result['ActionId'] = self.action_id
        if self.callout_name is not None:
            result['CalloutName'] = self.callout_name
        if self.sub_touch_id is not None:
            result['SubTouchId'] = self.sub_touch_id
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.callout_id is not None:
            result['CalloutId'] = self.callout_id
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.is_transfer is not None:
            result['IsTransfer'] = self.is_transfer
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.member_list is not None:
            result['MemberList'] = self.member_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('DepId') is not None:
            self.dep_id = m.get('DepId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ActionId') is not None:
            self.action_id = m.get('ActionId')
        if m.get('CalloutName') is not None:
            self.callout_name = m.get('CalloutName')
        if m.get('SubTouchId') is not None:
            self.sub_touch_id = m.get('SubTouchId')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('CalloutId') is not None:
            self.callout_id = m.get('CalloutId')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('IsTransfer') is not None:
            self.is_transfer = m.get('IsTransfer')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('MemberList') is not None:
            self.member_list = m.get('MemberList')
        return self


class GetHotlineCallActionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetHotlineCallActionResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineCallActionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotlineCallActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineCallActionResponseBody = None,
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
            temp_model = GetHotlineCallActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSkillGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        channel_type: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.channel_type = channel_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        return self


class ListSkillGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        description: str = None,
        channel_type: int = None,
        skill_group_id: int = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.description = description
        self.channel_type = channel_type
        self.skill_group_id = skill_group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListSkillGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListSkillGroupResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSkillGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSkillGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSkillGroupResponseBody = None,
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
            temp_model = ListSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOnlineSeatInformationRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        return self


class GetOnlineSeatInformationShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        return self


class GetOnlineSeatInformationResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetOnlineSeatInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetOnlineSeatInformationResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetOnlineSeatInformationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetOnlineSeatInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOnlineSeatInformationResponseBody = None,
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
            temp_model = GetOnlineSeatInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQualityProjectRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        project_id: int = None,
    ):
        self.instance_id = instance_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteQualityProjectResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteQualityProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteQualityProjectResponseBody = None,
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
            temp_model = DeleteQualityProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTouchListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        first_time_start: int = None,
        first_time_end: int = None,
        close_time_start: int = None,
        close_time_end: int = None,
        touch_id: List[int] = None,
        channel_id: List[str] = None,
        channel_type: List[int] = None,
        touch_type: List[int] = None,
        member_id: List[int] = None,
        member_name: List[str] = None,
        servicer_id: List[int] = None,
        servicer_name: List[str] = None,
        queue_id: List[int] = None,
        evaluation_status: List[int] = None,
        evaluation_level: List[int] = None,
        evaluation_score: List[int] = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.instance_id = instance_id
        self.first_time_start = first_time_start
        self.first_time_end = first_time_end
        self.close_time_start = close_time_start
        self.close_time_end = close_time_end
        self.touch_id = touch_id
        self.channel_id = channel_id
        self.channel_type = channel_type
        self.touch_type = touch_type
        self.member_id = member_id
        self.member_name = member_name
        self.servicer_id = servicer_id
        self.servicer_name = servicer_name
        self.queue_id = queue_id
        self.evaluation_status = evaluation_status
        self.evaluation_level = evaluation_level
        self.evaluation_score = evaluation_score
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.first_time_start is not None:
            result['FirstTimeStart'] = self.first_time_start
        if self.first_time_end is not None:
            result['FirstTimeEnd'] = self.first_time_end
        if self.close_time_start is not None:
            result['CloseTimeStart'] = self.close_time_start
        if self.close_time_end is not None:
            result['CloseTimeEnd'] = self.close_time_end
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.touch_type is not None:
            result['TouchType'] = self.touch_type
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.queue_id is not None:
            result['QueueId'] = self.queue_id
        if self.evaluation_status is not None:
            result['EvaluationStatus'] = self.evaluation_status
        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level
        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('FirstTimeStart') is not None:
            self.first_time_start = m.get('FirstTimeStart')
        if m.get('FirstTimeEnd') is not None:
            self.first_time_end = m.get('FirstTimeEnd')
        if m.get('CloseTimeStart') is not None:
            self.close_time_start = m.get('CloseTimeStart')
        if m.get('CloseTimeEnd') is not None:
            self.close_time_end = m.get('CloseTimeEnd')
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('TouchType') is not None:
            self.touch_type = m.get('TouchType')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')
        if m.get('EvaluationStatus') is not None:
            self.evaluation_status = m.get('EvaluationStatus')
        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')
        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTouchListResponseBodyResultDataDataExtAttrs(TeaModel):
    def __init__(
        self,
        evaluation_score: int = None,
        evaluation_level: int = None,
        evaluation_solution: int = None,
        online_session_source: int = None,
        online_join_resp_interval: int = None,
        evaluation_status: int = None,
        out_call_route_number: str = None,
        dnis: str = None,
        ani: str = None,
    ):
        self.evaluation_score = evaluation_score
        self.evaluation_level = evaluation_level
        self.evaluation_solution = evaluation_solution
        self.online_session_source = online_session_source
        self.online_join_resp_interval = online_join_resp_interval
        self.evaluation_status = evaluation_status
        # 外呼为主叫号码
        self.out_call_route_number = out_call_route_number
        # 外呼为被叫号码,入呼为被叫号码
        self.dnis = dnis
        # 入呼为主叫号码
        self.ani = ani

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score
        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level
        if self.evaluation_solution is not None:
            result['EvaluationSolution'] = self.evaluation_solution
        if self.online_session_source is not None:
            result['OnlineSessionSource'] = self.online_session_source
        if self.online_join_resp_interval is not None:
            result['OnlineJoinRespInterval'] = self.online_join_resp_interval
        if self.evaluation_status is not None:
            result['EvaluationStatus'] = self.evaluation_status
        if self.out_call_route_number is not None:
            result['OutCallRouteNumber'] = self.out_call_route_number
        if self.dnis is not None:
            result['Dnis'] = self.dnis
        if self.ani is not None:
            result['Ani'] = self.ani
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')
        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')
        if m.get('EvaluationSolution') is not None:
            self.evaluation_solution = m.get('EvaluationSolution')
        if m.get('OnlineSessionSource') is not None:
            self.online_session_source = m.get('OnlineSessionSource')
        if m.get('OnlineJoinRespInterval') is not None:
            self.online_join_resp_interval = m.get('OnlineJoinRespInterval')
        if m.get('EvaluationStatus') is not None:
            self.evaluation_status = m.get('EvaluationStatus')
        if m.get('OutCallRouteNumber') is not None:
            self.out_call_route_number = m.get('OutCallRouteNumber')
        if m.get('Dnis') is not None:
            self.dnis = m.get('Dnis')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        return self


class QueryTouchListResponseBodyResultDataData(TeaModel):
    def __init__(
        self,
        status: int = None,
        to_id: int = None,
        parent_touch_id: int = None,
        servicer_name: str = None,
        channel_type: int = None,
        close_time: int = None,
        gmt_modified: int = None,
        servicer_id: int = None,
        switch_user: str = None,
        bu_id: int = None,
        from_id: int = None,
        user_touch_id: int = None,
        touch_time: str = None,
        touch_content: str = None,
        feedback: str = None,
        touch_id: str = None,
        queue_id: int = None,
        dep_id: int = None,
        touch_end_reason: int = None,
        member_name: str = None,
        common_queue_name: str = None,
        first_time: int = None,
        touch_type: int = None,
        channel_id: str = None,
        gmt_create: int = None,
        member_id: int = None,
        ext_attrs: QueryTouchListResponseBodyResultDataDataExtAttrs = None,
    ):
        self.status = status
        self.to_id = to_id
        self.parent_touch_id = parent_touch_id
        self.servicer_name = servicer_name
        self.channel_type = channel_type
        self.close_time = close_time
        self.gmt_modified = gmt_modified
        self.servicer_id = servicer_id
        self.switch_user = switch_user
        self.bu_id = bu_id
        self.from_id = from_id
        self.user_touch_id = user_touch_id
        self.touch_time = touch_time
        self.touch_content = touch_content
        self.feedback = feedback
        self.touch_id = touch_id
        self.queue_id = queue_id
        self.dep_id = dep_id
        self.touch_end_reason = touch_end_reason
        self.member_name = member_name
        self.common_queue_name = common_queue_name
        self.first_time = first_time
        self.touch_type = touch_type
        self.channel_id = channel_id
        self.gmt_create = gmt_create
        self.member_id = member_id
        self.ext_attrs = ext_attrs

    def validate(self):
        if self.ext_attrs:
            self.ext_attrs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.to_id is not None:
            result['ToId'] = self.to_id
        if self.parent_touch_id is not None:
            result['ParentTouchId'] = self.parent_touch_id
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.close_time is not None:
            result['CloseTime'] = self.close_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.switch_user is not None:
            result['SwitchUser'] = self.switch_user
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.from_id is not None:
            result['FromId'] = self.from_id
        if self.user_touch_id is not None:
            result['UserTouchId'] = self.user_touch_id
        if self.touch_time is not None:
            result['TouchTime'] = self.touch_time
        if self.touch_content is not None:
            result['TouchContent'] = self.touch_content
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.queue_id is not None:
            result['QueueId'] = self.queue_id
        if self.dep_id is not None:
            result['DepId'] = self.dep_id
        if self.touch_end_reason is not None:
            result['TouchEndReason'] = self.touch_end_reason
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.common_queue_name is not None:
            result['CommonQueueName'] = self.common_queue_name
        if self.first_time is not None:
            result['FirstTime'] = self.first_time
        if self.touch_type is not None:
            result['TouchType'] = self.touch_type
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToId') is not None:
            self.to_id = m.get('ToId')
        if m.get('ParentTouchId') is not None:
            self.parent_touch_id = m.get('ParentTouchId')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('CloseTime') is not None:
            self.close_time = m.get('CloseTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('SwitchUser') is not None:
            self.switch_user = m.get('SwitchUser')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('FromId') is not None:
            self.from_id = m.get('FromId')
        if m.get('UserTouchId') is not None:
            self.user_touch_id = m.get('UserTouchId')
        if m.get('TouchTime') is not None:
            self.touch_time = m.get('TouchTime')
        if m.get('TouchContent') is not None:
            self.touch_content = m.get('TouchContent')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')
        if m.get('DepId') is not None:
            self.dep_id = m.get('DepId')
        if m.get('TouchEndReason') is not None:
            self.touch_end_reason = m.get('TouchEndReason')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('CommonQueueName') is not None:
            self.common_queue_name = m.get('CommonQueueName')
        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')
        if m.get('TouchType') is not None:
            self.touch_type = m.get('TouchType')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('ExtAttrs') is not None:
            temp_model = QueryTouchListResponseBodyResultDataDataExtAttrs()
            self.ext_attrs = temp_model.from_map(m['ExtAttrs'])
        return self


class QueryTouchListResponseBodyResultData(TeaModel):
    def __init__(
        self,
        total_results: int = None,
        next_page: int = None,
        current_page: int = None,
        data: List[QueryTouchListResponseBodyResultDataData] = None,
        total_page: int = None,
        previous_page: int = None,
        one_page_size: int = None,
        empty: bool = None,
    ):
        self.total_results = total_results
        self.next_page = next_page
        self.current_page = current_page
        self.data = data
        self.total_page = total_page
        self.previous_page = previous_page
        self.one_page_size = one_page_size
        self.empty = empty

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.next_page is not None:
            result['NextPage'] = self.next_page
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.previous_page is not None:
            result['PreviousPage'] = self.previous_page
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        if self.empty is not None:
            result['Empty'] = self.empty
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTouchListResponseBodyResultDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PreviousPage') is not None:
            self.previous_page = m.get('PreviousPage')
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        if m.get('Empty') is not None:
            self.empty = m.get('Empty')
        return self


class QueryTouchListResponseBody(TeaModel):
    def __init__(
        self,
        result_data: QueryTouchListResponseBodyResultData = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.result_data = result_data
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        if self.result_data:
            self.result_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_data is not None:
            result['ResultData'] = self.result_data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultData') is not None:
            temp_model = QueryTouchListResponseBodyResultData()
            self.result_data = temp_model.from_map(m['ResultData'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTouchListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTouchListResponseBody = None,
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
            temp_model = QueryTouchListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHotlineInQueueRequest(TeaModel):
    def __init__(
        self,
        outer_group_id: str = None,
        outer_group_type: str = None,
    ):
        self.outer_group_id = outer_group_id
        self.outer_group_type = outer_group_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_group_id is not None:
            result['OuterGroupId'] = self.outer_group_id
        if self.outer_group_type is not None:
            result['OuterGroupType'] = self.outer_group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterGroupId') is not None:
            self.outer_group_id = m.get('OuterGroupId')
        if m.get('OuterGroupType') is not None:
            self.outer_group_type = m.get('OuterGroupType')
        return self


class QueryHotlineInQueueResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryHotlineInQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryHotlineInQueueResponseBody = None,
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
            temp_model = QueryHotlineInQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FinishHotlineServiceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class FinishHotlineServiceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class FinishHotlineServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FinishHotlineServiceResponseBody = None,
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
            temp_model = FinishHotlineServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOutboundStrategiesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        bu_id: int = None,
        keyword: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.bu_id = bu_id
        self.keyword = keyword

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
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class ListOutboundStrategiesResponseBodyOutboundStrategies(TeaModel):
    def __init__(
        self,
        status: int = None,
        success_rate: int = None,
        process: int = None,
        gmt_modified_str: str = None,
        outbound_num: str = None,
        modifier_id: int = None,
        outbound_strategy_name: str = None,
        outbound_strategy_id: int = None,
        scene_name: str = None,
        creator_id: int = None,
        robot_name: str = None,
        modifier_name: str = None,
        resource_allocation: int = None,
        ext_attr: str = None,
        num_type: int = None,
        bu_id: int = None,
        robot_id: str = None,
        creator_name: str = None,
        department_id: int = None,
        robot_type: int = None,
        rule_code: int = None,
        gmt_create_str: str = None,
    ):
        self.status = status
        self.success_rate = success_rate
        self.process = process
        self.gmt_modified_str = gmt_modified_str
        self.outbound_num = outbound_num
        self.modifier_id = modifier_id
        self.outbound_strategy_name = outbound_strategy_name
        self.outbound_strategy_id = outbound_strategy_id
        self.scene_name = scene_name
        self.creator_id = creator_id
        self.robot_name = robot_name
        self.modifier_name = modifier_name
        self.resource_allocation = resource_allocation
        self.ext_attr = ext_attr
        self.num_type = num_type
        self.bu_id = bu_id
        self.robot_id = robot_id
        self.creator_name = creator_name
        self.department_id = department_id
        self.robot_type = robot_type
        self.rule_code = rule_code
        self.gmt_create_str = gmt_create_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.success_rate is not None:
            result['SuccessRate'] = self.success_rate
        if self.process is not None:
            result['Process'] = self.process
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.outbound_num is not None:
            result['OutboundNum'] = self.outbound_num
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.outbound_strategy_name is not None:
            result['OutboundStrategyName'] = self.outbound_strategy_name
        if self.outbound_strategy_id is not None:
            result['OutboundStrategyId'] = self.outbound_strategy_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name
        if self.resource_allocation is not None:
            result['ResourceAllocation'] = self.resource_allocation
        if self.ext_attr is not None:
            result['ExtAttr'] = self.ext_attr
        if self.num_type is not None:
            result['NumType'] = self.num_type
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        if self.rule_code is not None:
            result['RuleCode'] = self.rule_code
        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessRate') is not None:
            self.success_rate = m.get('SuccessRate')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('OutboundNum') is not None:
            self.outbound_num = m.get('OutboundNum')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('OutboundStrategyName') is not None:
            self.outbound_strategy_name = m.get('OutboundStrategyName')
        if m.get('OutboundStrategyId') is not None:
            self.outbound_strategy_id = m.get('OutboundStrategyId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')
        if m.get('ResourceAllocation') is not None:
            self.resource_allocation = m.get('ResourceAllocation')
        if m.get('ExtAttr') is not None:
            self.ext_attr = m.get('ExtAttr')
        if m.get('NumType') is not None:
            self.num_type = m.get('NumType')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        if m.get('RuleCode') is not None:
            self.rule_code = m.get('RuleCode')
        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')
        return self


class ListOutboundStrategiesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        outbound_strategies: List[ListOutboundStrategiesResponseBodyOutboundStrategies] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.outbound_strategies = outbound_strategies
        self.code = code

    def validate(self):
        if self.outbound_strategies:
            for k in self.outbound_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OutboundStrategies'] = []
        if self.outbound_strategies is not None:
            for k in self.outbound_strategies:
                result['OutboundStrategies'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.outbound_strategies = []
        if m.get('OutboundStrategies') is not None:
            for k in m.get('OutboundStrategies'):
                temp_model = ListOutboundStrategiesResponseBodyOutboundStrategies()
                self.outbound_strategies.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ListOutboundStrategiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOutboundStrategiesResponseBody = None,
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
            temp_model = ListOutboundStrategiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotlineRecordRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        call_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.call_id = call_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class ListHotlineRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        connection_id: str = None,
        call_id: str = None,
        url: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.connection_id = connection_id
        self.call_id = call_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListHotlineRecordResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[ListHotlineRecordResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListHotlineRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotlineRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHotlineRecordResponseBody = None,
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
            temp_model = ListHotlineRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeQualityProjectStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        status: int = None,
        project_id: int = None,
    ):
        self.instance_id = instance_id
        self.status = status
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ChangeQualityProjectStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeQualityProjectStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeQualityProjectStatusResponseBody = None,
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
            temp_model = ChangeQualityProjectStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferCallToSkillGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        skill_group_id: int = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
        hold_connection_id: str = None,
        type: int = None,
        is_single_transfer: bool = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.skill_group_id = skill_group_id
        self.call_id = call_id
        self.job_id = job_id
        self.connection_id = connection_id
        self.hold_connection_id = hold_connection_id
        self.type = type
        self.is_single_transfer = is_single_transfer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.hold_connection_id is not None:
            result['HoldConnectionId'] = self.hold_connection_id
        if self.type is not None:
            result['Type'] = self.type
        if self.is_single_transfer is not None:
            result['IsSingleTransfer'] = self.is_single_transfer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('HoldConnectionId') is not None:
            self.hold_connection_id = m.get('HoldConnectionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('IsSingleTransfer') is not None:
            self.is_single_transfer = m.get('IsSingleTransfer')
        return self


class TransferCallToSkillGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferCallToSkillGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferCallToSkillGroupResponseBody = None,
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
            temp_model = TransferCallToSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupServiceCapabilityRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupServiceCapabilityShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupServiceCapabilityResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupServiceCapabilityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetSkillGroupServiceCapabilityResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupServiceCapabilityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupServiceCapabilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSkillGroupServiceCapabilityResponseBody = None,
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
            temp_model = GetSkillGroupServiceCapabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSkillGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        skill_group_id: str = None,
        client_token: str = None,
    ):
        self.instance_id = instance_id
        self.skill_group_id = skill_group_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RemoveSkillGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveSkillGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveSkillGroupResponseBody = None,
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
            temp_model = RemoveSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCallV2Request(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        caller: str = None,
        caller_type: int = None,
        callee: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.caller = caller
        self.caller_type = caller_type
        self.callee = callee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.callee is not None:
            result['Callee'] = self.callee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        return self


class StartCallV2ResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartCallV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartCallV2ResponseBody = None,
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
            temp_model = StartCallV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeChatAgentStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        method: str = None,
    ):
        # clientToken
        self.client_token = client_token
        # 示例id
        self.instance_id = instance_id
        # 账户名称
        self.account_name = account_name
        # 修改到的状态类型
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.method is not None:
            result['Method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        return self


class ChangeChatAgentStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # httpStatusCode
        self.http_status_code = http_status_code
        # data
        self.data = data
        # code
        self.code = code
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ChangeChatAgentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeChatAgentStatusResponseBody = None,
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
            temp_model = ChangeChatAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordDataRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        account_type: str = None,
        account_id: str = None,
        acid: str = None,
        sec_level: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.account_type = account_type
        self.account_id = account_id
        self.acid = acid
        self.sec_level = sec_level

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
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.sec_level is not None:
            result['SecLevel'] = self.sec_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('SecLevel') is not None:
            self.sec_level = m.get('SecLevel')
        return self


class DescribeRecordDataResponseBody(TeaModel):
    def __init__(
        self,
        acid: str = None,
        request_id: str = None,
        message: str = None,
        oss_link: str = None,
        agent_id: str = None,
        code: str = None,
    ):
        self.acid = acid
        self.request_id = request_id
        self.message = message
        self.oss_link = oss_link
        self.agent_id = agent_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.oss_link is not None:
            result['OssLink'] = self.oss_link
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OssLink') is not None:
            self.oss_link = m.get('OssLink')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeRecordDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRecordDataResponseBody = None,
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
            temp_model = DescribeRecordDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOuterAccountRequest(TeaModel):
    def __init__(
        self,
        outer_account_id: str = None,
        outer_account_type: str = None,
    ):
        self.outer_account_id = outer_account_id
        self.outer_account_type = outer_account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id
        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')
        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')
        return self


class DeleteOuterAccountResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteOuterAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOuterAccountResponseBody = None,
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
            temp_model = DeleteOuterAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDepartmentalLatitudeAgentStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        exist_department_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 技能组分组id列表
        self.dep_ids = dep_ids
        # 是否根据技能组分组id分组显示
        self.exist_department_grouping = exist_department_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        return self


class GetDepartmentalLatitudeAgentStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids_shrink: str = None,
        exist_department_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 技能组分组id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 是否根据技能组分组id分组显示
        self.exist_department_grouping = exist_department_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        return self


class GetDepartmentalLatitudeAgentStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 每页的数量
        self.page_size = page_size
        # 总共记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetDepartmentalLatitudeAgentStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetDepartmentalLatitudeAgentStatusResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        # 错误描述
        self.message = message
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 数据
        self.data = data
        # 错误编码
        self.code = code
        # 接口调用是否成功
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetDepartmentalLatitudeAgentStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDepartmentalLatitudeAgentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDepartmentalLatitudeAgentStatusResponseBody = None,
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
            temp_model = GetDepartmentalLatitudeAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineAgentDetailRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetHotlineAgentDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_status_code: str = None,
        token: str = None,
        agent_id: int = None,
        assigned: bool = None,
        rest_type: int = None,
        agent_status: int = None,
        tenant_id: int = None,
    ):
        self.agent_status_code = agent_status_code
        self.token = token
        self.agent_id = agent_id
        self.assigned = assigned
        self.rest_type = rest_type
        self.agent_status = agent_status
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_status_code is not None:
            result['AgentStatusCode'] = self.agent_status_code
        if self.token is not None:
            result['Token'] = self.token
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.assigned is not None:
            result['Assigned'] = self.assigned
        if self.rest_type is not None:
            result['RestType'] = self.rest_type
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStatusCode') is not None:
            self.agent_status_code = m.get('AgentStatusCode')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('Assigned') is not None:
            self.assigned = m.get('Assigned')
        if m.get('RestType') is not None:
            self.rest_type = m.get('RestType')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetHotlineAgentDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetHotlineAgentDetailResponseBodyData = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineAgentDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetHotlineAgentDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineAgentDetailResponseBody = None,
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
            temp_model = GetHotlineAgentDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MakeCallRequest(TeaModel):
    def __init__(
        self,
        outer_account_id: str = None,
        outer_account_type: str = None,
        command_code: str = None,
        calling_number: str = None,
        called_number: str = None,
        ext_info: str = None,
    ):
        self.outer_account_id = outer_account_id
        self.outer_account_type = outer_account_type
        self.command_code = command_code
        self.calling_number = calling_number
        self.called_number = called_number
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id
        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type
        if self.command_code is not None:
            result['CommandCode'] = self.command_code
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')
        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')
        if m.get('CommandCode') is not None:
            self.command_code = m.get('CommandCode')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class MakeCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MakeCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MakeCallResponseBody = None,
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
            temp_model = MakeCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchCallRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
        hold_connection_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.call_id = call_id
        self.job_id = job_id
        self.connection_id = connection_id
        self.hold_connection_id = hold_connection_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.hold_connection_id is not None:
            result['HoldConnectionId'] = self.hold_connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('HoldConnectionId') is not None:
            self.hold_connection_id = m.get('HoldConnectionId')
        return self


class FetchCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FetchCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FetchCallResponseBody = None,
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
            temp_model = FetchCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineAgentStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        account_name: str = None,
    ):
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetHotlineAgentStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetHotlineAgentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotlineAgentStatusResponseBody = None,
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
            temp_model = GetHotlineAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCallRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        caller: str = None,
        callee: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.caller = caller
        self.callee = callee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.callee is not None:
            result['Callee'] = self.callee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        return self


class StartCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartCallResponseBody = None,
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
            temp_model = StartCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQualityRuleTagListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetQualityRuleTagListResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_tag_id: int = None,
        rule_tag_name: str = None,
    ):
        self.rule_tag_id = rule_tag_id
        self.rule_tag_name = rule_tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_tag_id is not None:
            result['RuleTagId'] = self.rule_tag_id
        if self.rule_tag_name is not None:
            result['RuleTagName'] = self.rule_tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleTagId') is not None:
            self.rule_tag_id = m.get('RuleTagId')
        if m.get('RuleTagName') is not None:
            self.rule_tag_name = m.get('RuleTagName')
        return self


class GetQualityRuleTagListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetQualityRuleTagListResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetQualityRuleTagListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQualityRuleTagListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQualityRuleTagListResponseBody = None,
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
            temp_model = GetQualityRuleTagListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOutbounNumListRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class GetOutbounNumListResponseBodyDataNumGroup(TeaModel):
    def __init__(
        self,
        type: int = None,
        value: str = None,
        description: str = None,
    ):
        self.type = type
        self.value = value
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetOutbounNumListResponseBodyDataNum(TeaModel):
    def __init__(
        self,
        type: int = None,
        value: str = None,
        description: str = None,
    ):
        self.type = type
        self.value = value
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class GetOutbounNumListResponseBodyData(TeaModel):
    def __init__(
        self,
        num_group: List[GetOutbounNumListResponseBodyDataNumGroup] = None,
        num: List[GetOutbounNumListResponseBodyDataNum] = None,
    ):
        self.num_group = num_group
        self.num = num

    def validate(self):
        if self.num_group:
            for k in self.num_group:
                if k:
                    k.validate()
        if self.num:
            for k in self.num:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NumGroup'] = []
        if self.num_group is not None:
            for k in self.num_group:
                result['NumGroup'].append(k.to_map() if k else None)
        result['Num'] = []
        if self.num is not None:
            for k in self.num:
                result['Num'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.num_group = []
        if m.get('NumGroup') is not None:
            for k in m.get('NumGroup'):
                temp_model = GetOutbounNumListResponseBodyDataNumGroup()
                self.num_group.append(temp_model.from_map(k))
        self.num = []
        if m.get('Num') is not None:
            for k in m.get('Num'):
                temp_model = GetOutbounNumListResponseBodyDataNum()
                self.num.append(temp_model.from_map(k))
        return self


class GetOutbounNumListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetOutbounNumListResponseBodyData = None,
        code: str = None,
        success: bool = None,
        http_status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetOutbounNumListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetOutbounNumListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOutbounNumListResponseBody = None,
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
            temp_model = GetOutbounNumListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateThirdSsoAgentRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        client_id: str = None,
        account_id: str = None,
        account_name: str = None,
        display_name: str = None,
        skill_group_ids: List[int] = None,
        role_ids: List[int] = None,
    ):
        # clientToken
        self.client_token = client_token
        # param1
        self.instance_id = instance_id
        # param2
        self.client_id = client_id
        # param3
        self.account_id = account_id
        # param4
        self.account_name = account_name
        # param5
        self.display_name = display_name
        # param6
        self.skill_group_ids = skill_group_ids
        # param7
        self.role_ids = role_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.skill_group_ids is not None:
            result['SkillGroupIds'] = self.skill_group_ids
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('SkillGroupIds') is not None:
            self.skill_group_ids = m.get('SkillGroupIds')
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')
        return self


class CreateThirdSsoAgentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        data: int = None,
        code: str = None,
        success: bool = None,
    ):
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # httpStatusCode
        self.http_status_code = http_status_code
        # 新创建的坐席id
        self.data = data
        # code
        self.code = code
        # success
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateThirdSsoAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateThirdSsoAgentResponseBody = None,
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
            temp_model = CreateThirdSsoAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupStatusTotalRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupStatusTotalShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据坐席分组
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetSkillGroupStatusTotalResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetSkillGroupStatusTotalResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetSkillGroupStatusTotalResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 接口调用是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupStatusTotalResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupStatusTotalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSkillGroupStatusTotalResponseBody = None,
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
            temp_model = GetSkillGroupStatusTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateQualityProjectsRequest(TeaModel):
    def __init__(
        self,
        project_name: str = None,
        check_freq_type: int = None,
        time_range_start: str = None,
        time_range_end: str = None,
        analysis_ids: List[int] = None,
        instance_list: List[str] = None,
        channel_touch_type: List[int] = None,
    ):
        self.project_name = project_name
        self.check_freq_type = check_freq_type
        self.time_range_start = time_range_start
        self.time_range_end = time_range_end
        self.analysis_ids = analysis_ids
        self.instance_list = instance_list
        self.channel_touch_type = channel_touch_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.check_freq_type is not None:
            result['CheckFreqType'] = self.check_freq_type
        if self.time_range_start is not None:
            result['TimeRangeStart'] = self.time_range_start
        if self.time_range_end is not None:
            result['TimeRangeEnd'] = self.time_range_end
        if self.analysis_ids is not None:
            result['AnalysisIds'] = self.analysis_ids
        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list
        if self.channel_touch_type is not None:
            result['ChannelTouchType'] = self.channel_touch_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('CheckFreqType') is not None:
            self.check_freq_type = m.get('CheckFreqType')
        if m.get('TimeRangeStart') is not None:
            self.time_range_start = m.get('TimeRangeStart')
        if m.get('TimeRangeEnd') is not None:
            self.time_range_end = m.get('TimeRangeEnd')
        if m.get('AnalysisIds') is not None:
            self.analysis_ids = m.get('AnalysisIds')
        if m.get('InstanceList') is not None:
            self.instance_list = m.get('InstanceList')
        if m.get('ChannelTouchType') is not None:
            self.channel_touch_type = m.get('ChannelTouchType')
        return self


class BatchCreateQualityProjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        version: int = None,
        project_id: int = None,
        instance_id: str = None,
    ):
        self.version = version
        self.project_id = project_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class BatchCreateQualityProjectsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[BatchCreateQualityProjectsResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = BatchCreateQualityProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchCreateQualityProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchCreateQualityProjectsResponseBody = None,
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
            temp_model = BatchCreateQualityProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertTaskDetailRequest(TeaModel):
    def __init__(
        self,
        outbound_task_id: int = None,
        call_infos: str = None,
        instance_id: str = None,
    ):
        self.outbound_task_id = outbound_task_id
        self.call_infos = call_infos
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.call_infos is not None:
            result['CallInfos'] = self.call_infos
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('CallInfos') is not None:
            self.call_infos = m.get('CallInfos')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class InsertTaskDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertTaskDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InsertTaskDetailResponseBody = None,
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
            temp_model = InsertTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSkillGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        skill_group_id: int = None,
        skill_group_name: str = None,
        description: str = None,
        display_name: str = None,
        client_token: str = None,
    ):
        self.instance_id = instance_id
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name
        self.description = description
        self.display_name = display_name
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class UpdateSkillGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSkillGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSkillGroupResponseBody = None,
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
            temp_model = UpdateSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HotlineSessionQueryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        acid: str = None,
        call_type: int = None,
        called_number: str = None,
        calling_number: str = None,
        group_id: int = None,
        group_name: str = None,
        member_id: str = None,
        member_name: str = None,
        query_end_time: int = None,
        query_start_time: int = None,
        request_id: str = None,
        servicer_name: str = None,
        servicer_id: str = None,
        params: str = None,
        page_size: int = None,
        page_no: int = None,
        call_result: str = None,
        id: str = None,
        acid_list: List[str] = None,
        call_type_list: List[int] = None,
        group_id_list: List[int] = None,
        calling_number_list: List[str] = None,
        called_number_list: List[str] = None,
        member_id_list: List[str] = None,
        servicer_id_list: List[str] = None,
        call_result_list: List[str] = None,
    ):
        self.instance_id = instance_id
        self.acid = acid
        self.call_type = call_type
        self.called_number = called_number
        self.calling_number = calling_number
        self.group_id = group_id
        self.group_name = group_name
        self.member_id = member_id
        self.member_name = member_name
        self.query_end_time = query_end_time
        self.query_start_time = query_start_time
        self.request_id = request_id
        self.servicer_name = servicer_name
        self.servicer_id = servicer_id
        self.params = params
        self.page_size = page_size
        self.page_no = page_no
        self.call_result = call_result
        self.id = id
        self.acid_list = acid_list
        self.call_type_list = call_type_list
        self.group_id_list = group_id_list
        self.calling_number_list = calling_number_list
        self.called_number_list = called_number_list
        self.member_id_list = member_id_list
        self.servicer_id_list = servicer_id_list
        self.call_result_list = call_result_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.query_end_time is not None:
            result['QueryEndTime'] = self.query_end_time
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.params is not None:
            result['Params'] = self.params
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.id is not None:
            result['Id'] = self.id
        if self.acid_list is not None:
            result['AcidList'] = self.acid_list
        if self.call_type_list is not None:
            result['CallTypeList'] = self.call_type_list
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list
        if self.calling_number_list is not None:
            result['CallingNumberList'] = self.calling_number_list
        if self.called_number_list is not None:
            result['CalledNumberList'] = self.called_number_list
        if self.member_id_list is not None:
            result['MemberIdList'] = self.member_id_list
        if self.servicer_id_list is not None:
            result['ServicerIdList'] = self.servicer_id_list
        if self.call_result_list is not None:
            result['CallResultList'] = self.call_result_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('QueryEndTime') is not None:
            self.query_end_time = m.get('QueryEndTime')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AcidList') is not None:
            self.acid_list = m.get('AcidList')
        if m.get('CallTypeList') is not None:
            self.call_type_list = m.get('CallTypeList')
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')
        if m.get('CallingNumberList') is not None:
            self.calling_number_list = m.get('CallingNumberList')
        if m.get('CalledNumberList') is not None:
            self.called_number_list = m.get('CalledNumberList')
        if m.get('MemberIdList') is not None:
            self.member_id_list = m.get('MemberIdList')
        if m.get('ServicerIdList') is not None:
            self.servicer_id_list = m.get('ServicerIdList')
        if m.get('CallResultList') is not None:
            self.call_result_list = m.get('CallResultList')
        return self


class HotlineSessionQueryResponseBodyDataCallDetailRecord(TeaModel):
    def __init__(
        self,
        call_result: str = None,
        trunk_call: str = None,
        servicer_name: str = None,
        out_queue_time: str = None,
        call_continue_time: int = None,
        create_time: str = None,
        pick_up_time: str = None,
        ring_continue_time: int = None,
        called_number: str = None,
        servicer_id: str = None,
        hang_up_time: str = None,
        evaluation_level: int = None,
        passive_transfer_id: str = None,
        active_transfer_id: str = None,
        hang_up_role: str = None,
        passive_transfer_id_type: str = None,
        member_name: str = None,
        evaluation_score: int = None,
        acid: str = None,
        ring_start_time: str = None,
        call_type: int = None,
        group_name: str = None,
        group_id: int = None,
        ring_end_time: str = None,
        calling_number: str = None,
        in_queue_time: str = None,
        member_id: str = None,
        id: str = None,
        queue_up_continue_time: int = None,
    ):
        self.call_result = call_result
        self.trunk_call = trunk_call
        self.servicer_name = servicer_name
        self.out_queue_time = out_queue_time
        self.call_continue_time = call_continue_time
        self.create_time = create_time
        self.pick_up_time = pick_up_time
        self.ring_continue_time = ring_continue_time
        self.called_number = called_number
        self.servicer_id = servicer_id
        self.hang_up_time = hang_up_time
        self.evaluation_level = evaluation_level
        self.passive_transfer_id = passive_transfer_id
        self.active_transfer_id = active_transfer_id
        self.hang_up_role = hang_up_role
        self.passive_transfer_id_type = passive_transfer_id_type
        self.member_name = member_name
        self.evaluation_score = evaluation_score
        self.acid = acid
        self.ring_start_time = ring_start_time
        self.call_type = call_type
        self.group_name = group_name
        self.group_id = group_id
        self.ring_end_time = ring_end_time
        self.calling_number = calling_number
        self.in_queue_time = in_queue_time
        self.member_id = member_id
        self.id = id
        self.queue_up_continue_time = queue_up_continue_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.trunk_call is not None:
            result['TrunkCall'] = self.trunk_call
        if self.servicer_name is not None:
            result['ServicerName'] = self.servicer_name
        if self.out_queue_time is not None:
            result['OutQueueTime'] = self.out_queue_time
        if self.call_continue_time is not None:
            result['CallContinueTime'] = self.call_continue_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pick_up_time is not None:
            result['PickUpTime'] = self.pick_up_time
        if self.ring_continue_time is not None:
            result['RingContinueTime'] = self.ring_continue_time
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.servicer_id is not None:
            result['ServicerId'] = self.servicer_id
        if self.hang_up_time is not None:
            result['HangUpTime'] = self.hang_up_time
        if self.evaluation_level is not None:
            result['EvaluationLevel'] = self.evaluation_level
        if self.passive_transfer_id is not None:
            result['PassiveTransferId'] = self.passive_transfer_id
        if self.active_transfer_id is not None:
            result['ActiveTransferId'] = self.active_transfer_id
        if self.hang_up_role is not None:
            result['HangUpRole'] = self.hang_up_role
        if self.passive_transfer_id_type is not None:
            result['PassiveTransferIdType'] = self.passive_transfer_id_type
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.evaluation_score is not None:
            result['EvaluationScore'] = self.evaluation_score
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.ring_start_time is not None:
            result['RingStartTime'] = self.ring_start_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.ring_end_time is not None:
            result['RingEndTime'] = self.ring_end_time
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.in_queue_time is not None:
            result['InQueueTime'] = self.in_queue_time
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.id is not None:
            result['Id'] = self.id
        if self.queue_up_continue_time is not None:
            result['QueueUpContinueTime'] = self.queue_up_continue_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('TrunkCall') is not None:
            self.trunk_call = m.get('TrunkCall')
        if m.get('ServicerName') is not None:
            self.servicer_name = m.get('ServicerName')
        if m.get('OutQueueTime') is not None:
            self.out_queue_time = m.get('OutQueueTime')
        if m.get('CallContinueTime') is not None:
            self.call_continue_time = m.get('CallContinueTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PickUpTime') is not None:
            self.pick_up_time = m.get('PickUpTime')
        if m.get('RingContinueTime') is not None:
            self.ring_continue_time = m.get('RingContinueTime')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ServicerId') is not None:
            self.servicer_id = m.get('ServicerId')
        if m.get('HangUpTime') is not None:
            self.hang_up_time = m.get('HangUpTime')
        if m.get('EvaluationLevel') is not None:
            self.evaluation_level = m.get('EvaluationLevel')
        if m.get('PassiveTransferId') is not None:
            self.passive_transfer_id = m.get('PassiveTransferId')
        if m.get('ActiveTransferId') is not None:
            self.active_transfer_id = m.get('ActiveTransferId')
        if m.get('HangUpRole') is not None:
            self.hang_up_role = m.get('HangUpRole')
        if m.get('PassiveTransferIdType') is not None:
            self.passive_transfer_id_type = m.get('PassiveTransferIdType')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('EvaluationScore') is not None:
            self.evaluation_score = m.get('EvaluationScore')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('RingStartTime') is not None:
            self.ring_start_time = m.get('RingStartTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RingEndTime') is not None:
            self.ring_end_time = m.get('RingEndTime')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('InQueueTime') is not None:
            self.in_queue_time = m.get('InQueueTime')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('QueueUpContinueTime') is not None:
            self.queue_up_continue_time = m.get('QueueUpContinueTime')
        return self


class HotlineSessionQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        call_detail_record: List[HotlineSessionQueryResponseBodyDataCallDetailRecord] = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
    ):
        self.call_detail_record = call_detail_record
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count

    def validate(self):
        if self.call_detail_record:
            for k in self.call_detail_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallDetailRecord'] = []
        if self.call_detail_record is not None:
            for k in self.call_detail_record:
                result['CallDetailRecord'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_detail_record = []
        if m.get('CallDetailRecord') is not None:
            for k in m.get('CallDetailRecord'):
                temp_model = HotlineSessionQueryResponseBodyDataCallDetailRecord()
                self.call_detail_record.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class HotlineSessionQueryResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: HotlineSessionQueryResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = HotlineSessionQueryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HotlineSessionQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: HotlineSessionQueryResponseBody = None,
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
            temp_model = HotlineSessionQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueInformationRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetQueueInformationShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        return self


class GetQueueInformationResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetQueueInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetQueueInformationResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetQueueInformationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetQueueInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetQueueInformationResponseBody = None,
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
            temp_model = GetQueueInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSkillGroupServiceStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
        group_ids: List[int] = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
        exist_robot_instance_grouping: bool = None,
        exist_channel_instance_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 技能组id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids
        # 技能组id列表
        self.group_ids = group_ids
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据技能组分组
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping
        # 是否根据机器实例分组
        self.exist_robot_instance_grouping = exist_robot_instance_grouping
        # 是否根据渠道实例分组
        self.exist_channel_instance_grouping = exist_channel_instance_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        if self.exist_robot_instance_grouping is not None:
            result['ExistRobotInstanceGrouping'] = self.exist_robot_instance_grouping
        if self.exist_channel_instance_grouping is not None:
            result['ExistChannelInstanceGrouping'] = self.exist_channel_instance_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        if m.get('ExistRobotInstanceGrouping') is not None:
            self.exist_robot_instance_grouping = m.get('ExistRobotInstanceGrouping')
        if m.get('ExistChannelInstanceGrouping') is not None:
            self.exist_channel_instance_grouping = m.get('ExistChannelInstanceGrouping')
        return self


class GetSkillGroupServiceStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
        group_ids_shrink: str = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
        exist_skill_group_grouping: bool = None,
        exist_robot_instance_grouping: bool = None,
        exist_channel_instance_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 技能组id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 技能组id列表
        self.group_ids_shrink = group_ids_shrink
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据技能组分组
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组
        self.exist_department_grouping = exist_department_grouping
        # 是否根据技能组分组
        self.exist_skill_group_grouping = exist_skill_group_grouping
        # 是否根据机器实例分组
        self.exist_robot_instance_grouping = exist_robot_instance_grouping
        # 是否根据渠道实例分组
        self.exist_channel_instance_grouping = exist_channel_instance_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.group_ids_shrink is not None:
            result['GroupIds'] = self.group_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        if self.exist_skill_group_grouping is not None:
            result['ExistSkillGroupGrouping'] = self.exist_skill_group_grouping
        if self.exist_robot_instance_grouping is not None:
            result['ExistRobotInstanceGrouping'] = self.exist_robot_instance_grouping
        if self.exist_channel_instance_grouping is not None:
            result['ExistChannelInstanceGrouping'] = self.exist_channel_instance_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('GroupIds') is not None:
            self.group_ids_shrink = m.get('GroupIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        if m.get('ExistSkillGroupGrouping') is not None:
            self.exist_skill_group_grouping = m.get('ExistSkillGroupGrouping')
        if m.get('ExistRobotInstanceGrouping') is not None:
            self.exist_robot_instance_grouping = m.get('ExistRobotInstanceGrouping')
        if m.get('ExistChannelInstanceGrouping') is not None:
            self.exist_channel_instance_grouping = m.get('ExistChannelInstanceGrouping')
        return self


class GetSkillGroupServiceStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
        page_num: int = None,
    ):
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows
        # 当前页数
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        return self


class GetSkillGroupServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetSkillGroupServiceStatusResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetSkillGroupServiceStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetSkillGroupServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSkillGroupServiceStatusResponseBody = None,
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
            temp_model = GetSkillGroupServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentDetailReportRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids: List[int] = None,
        dep_ids: List[int] = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids = agent_ids
        # 部门id列表
        self.dep_ids = dep_ids
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据坐席分组显示
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组显示
        self.exist_department_grouping = exist_department_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        return self


class GetAgentDetailReportShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_date: int = None,
        end_date: int = None,
        page_size: int = None,
        current_page: int = None,
        agent_ids_shrink: str = None,
        dep_ids_shrink: str = None,
        time_latitude_type: str = None,
        exist_agent_grouping: bool = None,
        exist_department_grouping: bool = None,
    ):
        # AICCS实例ID，在智能联络中心控制台上可以看到
        self.instance_id = instance_id
        # 开始日期时间戳（毫秒）
        self.start_date = start_date
        # 结束日期时间戳（毫秒）
        self.end_date = end_date
        # 每页大小（默认为10)
        self.page_size = page_size
        # 当前页（默认为1）
        self.current_page = current_page
        # 坐席id列表
        self.agent_ids_shrink = agent_ids_shrink
        # 部门id列表
        self.dep_ids_shrink = dep_ids_shrink
        # 时间纬度类型
        self.time_latitude_type = time_latitude_type
        # 是否根据坐席分组显示
        self.exist_agent_grouping = exist_agent_grouping
        # 是否根据部门分组显示
        self.exist_department_grouping = exist_department_grouping

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.agent_ids_shrink is not None:
            result['AgentIds'] = self.agent_ids_shrink
        if self.dep_ids_shrink is not None:
            result['DepIds'] = self.dep_ids_shrink
        if self.time_latitude_type is not None:
            result['TimeLatitudeType'] = self.time_latitude_type
        if self.exist_agent_grouping is not None:
            result['ExistAgentGrouping'] = self.exist_agent_grouping
        if self.exist_department_grouping is not None:
            result['ExistDepartmentGrouping'] = self.exist_department_grouping
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('AgentIds') is not None:
            self.agent_ids_shrink = m.get('AgentIds')
        if m.get('DepIds') is not None:
            self.dep_ids_shrink = m.get('DepIds')
        if m.get('TimeLatitudeType') is not None:
            self.time_latitude_type = m.get('TimeLatitudeType')
        if m.get('ExistAgentGrouping') is not None:
            self.exist_agent_grouping = m.get('ExistAgentGrouping')
        if m.get('ExistDepartmentGrouping') is not None:
            self.exist_department_grouping = m.get('ExistDepartmentGrouping')
        return self


class GetAgentDetailReportResponseBodyData(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        rows: str = None,
    ):
        # 当前页数
        self.page_num = page_num
        # 页大小
        self.page_size = page_size
        # 总记录数
        self.total_num = total_num
        # 信息为list<map>类型的json字符串
        self.rows = rows

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class GetAgentDetailReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        code: str = None,
        success: str = None,
        data: GetAgentDetailReportResponseBodyData = None,
    ):
        # 请求ID，用于跟踪错误原因
        self.request_id = request_id
        # 错误描述
        self.message = message
        # 错误编码
        self.code = code
        # 调用接口是否成功
        self.success = success
        # data
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            temp_model = GetAgentDetailReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAgentDetailReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentDetailReportResponseBody = None,
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
            temp_model = GetAgentDetailReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTicketsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        case_id: int = None,
        case_type: int = None,
        case_status: int = None,
        sr_type: int = None,
        task_status: int = None,
        channel_id: str = None,
        channel_type: int = None,
        touch_id: int = None,
        deal_id: int = None,
        extra: Dict[str, Any] = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.instance_id = instance_id
        self.case_id = case_id
        self.case_type = case_type
        self.case_status = case_status
        self.sr_type = sr_type
        self.task_status = task_status
        self.channel_id = channel_id
        self.channel_type = channel_type
        self.touch_id = touch_id
        self.deal_id = deal_id
        self.extra = extra
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.case_type is not None:
            result['CaseType'] = self.case_type
        if self.case_status is not None:
            result['CaseStatus'] = self.case_status
        if self.sr_type is not None:
            result['SrType'] = self.sr_type
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.deal_id is not None:
            result['DealId'] = self.deal_id
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('CaseType') is not None:
            self.case_type = m.get('CaseType')
        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')
        if m.get('SrType') is not None:
            self.sr_type = m.get('SrType')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('DealId') is not None:
            self.deal_id = m.get('DealId')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTicketsShrinkRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        case_id: int = None,
        case_type: int = None,
        case_status: int = None,
        sr_type: int = None,
        task_status: int = None,
        channel_id: str = None,
        channel_type: int = None,
        touch_id: int = None,
        deal_id: int = None,
        extra_shrink: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.instance_id = instance_id
        self.case_id = case_id
        self.case_type = case_type
        self.case_status = case_status
        self.sr_type = sr_type
        self.task_status = task_status
        self.channel_id = channel_id
        self.channel_type = channel_type
        self.touch_id = touch_id
        self.deal_id = deal_id
        self.extra_shrink = extra_shrink
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.case_id is not None:
            result['CaseId'] = self.case_id
        if self.case_type is not None:
            result['CaseType'] = self.case_type
        if self.case_status is not None:
            result['CaseStatus'] = self.case_status
        if self.sr_type is not None:
            result['SrType'] = self.sr_type
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.touch_id is not None:
            result['TouchId'] = self.touch_id
        if self.deal_id is not None:
            result['DealId'] = self.deal_id
        if self.extra_shrink is not None:
            result['Extra'] = self.extra_shrink
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')
        if m.get('CaseType') is not None:
            self.case_type = m.get('CaseType')
        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')
        if m.get('SrType') is not None:
            self.sr_type = m.get('SrType')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('TouchId') is not None:
            self.touch_id = m.get('TouchId')
        if m.get('DealId') is not None:
            self.deal_id = m.get('DealId')
        if m.get('Extra') is not None:
            self.extra_shrink = m.get('Extra')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryTicketsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTicketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTicketsResponseBody = None,
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
            temp_model = QueryTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOutboundTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        task_type: int = None,
        task_name: str = None,
        start_date: str = None,
        end_date: str = None,
        start_time: str = None,
        end_time: str = None,
        skill_group: int = None,
        ani: str = None,
        status: str = None,
        group_name: str = None,
        department_id: str = None,
        instance_id: str = None,
        page_size: int = None,
        current_page: int = None,
    ):
        self.task_id = task_id
        self.task_type = task_type
        self.task_name = task_name
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.skill_group = skill_group
        self.ani = ani
        self.status = status
        self.group_name = group_name
        self.department_id = department_id
        self.instance_id = instance_id
        self.page_size = page_size
        self.current_page = current_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.ani is not None:
            result['Ani'] = self.ani
        if self.status is not None:
            result['Status'] = self.status
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('Ani') is not None:
            self.ani = m.get('Ani')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        return self


class QueryOutboundTaskResponseBodyDataList(TeaModel):
    def __init__(
        self,
        status: int = None,
        type: int = None,
        end_date: str = None,
        retry_time: int = None,
        retry_interval: int = None,
        start_date: str = None,
        gmt_modified: int = None,
        creator: str = None,
        end_time: str = None,
        start_time: str = None,
        model: int = None,
        bu_id: int = None,
        modifier: str = None,
        group_name: str = None,
        description: str = None,
        department_id: int = None,
        gmt_create: int = None,
        skill_group: int = None,
        name: str = None,
        ext_attrs: str = None,
        caller_num: str = None,
        id: int = None,
    ):
        self.status = status
        self.type = type
        self.end_date = end_date
        self.retry_time = retry_time
        self.retry_interval = retry_interval
        self.start_date = start_date
        self.gmt_modified = gmt_modified
        self.creator = creator
        self.end_time = end_time
        self.start_time = start_time
        self.model = model
        self.bu_id = bu_id
        self.modifier = modifier
        self.group_name = group_name
        self.description = description
        self.department_id = department_id
        self.gmt_create = gmt_create
        self.skill_group = skill_group
        self.name = name
        self.ext_attrs = ext_attrs
        self.caller_num = caller_num
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.model is not None:
            result['Model'] = self.model
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.skill_group is not None:
            result['SkillGroup'] = self.skill_group
        if self.name is not None:
            result['Name'] = self.name
        if self.ext_attrs is not None:
            result['ExtAttrs'] = self.ext_attrs
        if self.caller_num is not None:
            result['CallerNum'] = self.caller_num
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SkillGroup') is not None:
            self.skill_group = m.get('SkillGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtAttrs') is not None:
            self.ext_attrs = m.get('ExtAttrs')
        if m.get('CallerNum') is not None:
            self.caller_num = m.get('CallerNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryOutboundTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        total_results: str = None,
        current_page: str = None,
        list: List[QueryOutboundTaskResponseBodyDataList] = None,
        page_size: str = None,
    ):
        self.total_results = total_results
        self.current_page = current_page
        self.list = list
        self.page_size = page_size

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryOutboundTaskResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryOutboundTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: str = None,
        data: QueryOutboundTaskResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Data') is not None:
            temp_model = QueryOutboundTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOutboundTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOutboundTaskResponseBody = None,
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
            temp_model = QueryOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JoinThirdCallRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
        hold_connection_id: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.call_id = call_id
        self.job_id = job_id
        self.connection_id = connection_id
        self.hold_connection_id = hold_connection_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.hold_connection_id is not None:
            result['HoldConnectionId'] = self.hold_connection_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('HoldConnectionId') is not None:
            self.hold_connection_id = m.get('HoldConnectionId')
        return self


class JoinThirdCallResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class JoinThirdCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: JoinThirdCallResponseBody = None,
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
            temp_model = JoinThirdCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSkillGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        skill_group_name: str = None,
        description: str = None,
        display_name: str = None,
        channel_type: int = None,
        client_token: str = None,
    ):
        self.instance_id = instance_id
        self.skill_group_name = skill_group_name
        self.description = description
        self.display_name = display_name
        self.channel_type = channel_type
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.skill_group_name is not None:
            result['SkillGroupName'] = self.skill_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SkillGroupName') is not None:
            self.skill_group_name = m.get('SkillGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateSkillGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSkillGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSkillGroupResponseBody = None,
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
            temp_model = CreateSkillGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartOutboundTaskRequest(TeaModel):
    def __init__(
        self,
        outbound_task_id: int = None,
        instance_id: str = None,
    ):
        self.outbound_task_id = outbound_task_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outbound_task_id is not None:
            result['OutboundTaskId'] = self.outbound_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutboundTaskId') is not None:
            self.outbound_task_id = m.get('OutboundTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RestartOutboundTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RestartOutboundTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartOutboundTaskResponseBody = None,
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
            temp_model = RestartOutboundTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


