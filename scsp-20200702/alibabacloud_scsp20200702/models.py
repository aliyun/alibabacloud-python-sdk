# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class GetUserTokenRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        user_id: str = None,
        nick: str = None,
        app_key: str = None,
    ):
        # 实例id
        self.instance_id = instance_id
        # 用户id
        self.user_id = user_id
        # 昵称
        self.nick = nick
        # appKey
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetUserTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        expires: int = None,
        token: str = None,
    ):
        self.expires = expires
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expires is not None:
            result['Expires'] = self.expires
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expires') is not None:
            self.expires = m.get('Expires')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetUserTokenResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetUserTokenResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        # 错误信息
        self.message = message
        # 鹰眼id
        self.request_id = request_id
        self.data = data
        # 错误码
        self.code = code
        # 是否调用成功
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
            temp_model = GetUserTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserTokenResponseBody = None,
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
            temp_model = GetUserTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTicketListRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        operator_id: int = None,
        ticket_status: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.operator_id = operator_id
        self.ticket_status = ticket_status
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time

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
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.ticket_status is not None:
            result['TicketStatus'] = self.ticket_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('TicketStatus') is not None:
            self.ticket_status = m.get('TicketStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class SearchTicketListResponseBodyData(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        carbon_copy: str = None,
        create_time: int = None,
        service_id: int = None,
        ticket_id: int = None,
        priority: int = None,
        creator_id: int = None,
        form_data: str = None,
        from_info: str = None,
        modified_time: int = None,
        task_status: str = None,
        creator_name: str = None,
        category_id: int = None,
        creator_type: int = None,
        member_id: int = None,
        case_status: int = None,
        template_id: int = None,
    ):
        self.member_name = member_name
        self.carbon_copy = carbon_copy
        self.create_time = create_time
        self.service_id = service_id
        self.ticket_id = ticket_id
        self.priority = priority
        self.creator_id = creator_id
        self.form_data = form_data
        self.from_info = from_info
        self.modified_time = modified_time
        self.task_status = task_status
        self.creator_name = creator_name
        self.category_id = category_id
        self.creator_type = creator_type
        self.member_id = member_id
        self.case_status = case_status
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.carbon_copy is not None:
            result['CarbonCopy'] = self.carbon_copy
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.form_data is not None:
            result['FormData'] = self.form_data
        if self.from_info is not None:
            result['FromInfo'] = self.from_info
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.case_status is not None:
            result['CaseStatus'] = self.case_status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('CarbonCopy') is not None:
            self.carbon_copy = m.get('CarbonCopy')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('FormData') is not None:
            self.form_data = m.get('FormData')
        if m.get('FromInfo') is not None:
            self.from_info = m.get('FromInfo')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SearchTicketListResponseBody(TeaModel):
    def __init__(
        self,
        one_page_size: int = None,
        request_id: str = None,
        message: str = None,
        total_page: int = None,
        total_results: int = None,
        page_no: int = None,
        data: List[SearchTicketListResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.one_page_size = one_page_size
        self.request_id = request_id
        self.message = message
        self.total_page = total_page
        self.total_results = total_results
        self.page_no = page_no
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
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.page_no is not None:
            result['PageNo'] = self.page_no
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
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchTicketListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchTicketListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTicketListResponseBody = None,
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
            temp_model = SearchTicketListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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


class EditEntityRouteRequest(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_name: str = None,
        entity_biz_code: str = None,
        entity_biz_code_type: str = None,
        entity_relation_number: str = None,
        department_id: str = None,
        group_id: int = None,
        service_id: int = None,
        ext_info: str = None,
        instance_id: str = None,
        unique_id: int = None,
    ):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_biz_code = entity_biz_code
        self.entity_biz_code_type = entity_biz_code_type
        self.entity_relation_number = entity_relation_number
        self.department_id = department_id
        self.group_id = group_id
        self.service_id = service_id
        self.ext_info = ext_info
        self.instance_id = instance_id
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_biz_code is not None:
            result['EntityBizCode'] = self.entity_biz_code
        if self.entity_biz_code_type is not None:
            result['EntityBizCodeType'] = self.entity_biz_code_type
        if self.entity_relation_number is not None:
            result['EntityRelationNumber'] = self.entity_relation_number
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityBizCode') is not None:
            self.entity_biz_code = m.get('EntityBizCode')
        if m.get('EntityBizCodeType') is not None:
            self.entity_biz_code_type = m.get('EntityBizCodeType')
        if m.get('EntityRelationNumber') is not None:
            self.entity_relation_number = m.get('EntityRelationNumber')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        return self


class EditEntityRouteResponseBody(TeaModel):
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


class EditEntityRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EditEntityRouteResponseBody = None,
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
            temp_model = EditEntityRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTagListRequest(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
        instance_id: str = None,
    ):
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetTagListResponseBodyDataTagValues(TeaModel):
    def __init__(
        self,
        status: str = None,
        description: str = None,
        tag_name: str = None,
        tag_group_code: str = None,
        tag_code: str = None,
        tag_group_name: str = None,
        entity_relation_number: str = None,
    ):
        self.status = status
        self.description = description
        self.tag_name = tag_name
        self.tag_group_code = tag_group_code
        self.tag_code = tag_code
        self.tag_group_name = tag_group_name
        self.entity_relation_number = entity_relation_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.description is not None:
            result['Description'] = self.description
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_group_code is not None:
            result['TagGroupCode'] = self.tag_group_code
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.tag_group_name is not None:
            result['TagGroupName'] = self.tag_group_name
        if self.entity_relation_number is not None:
            result['EntityRelationNumber'] = self.entity_relation_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagGroupCode') is not None:
            self.tag_group_code = m.get('TagGroupCode')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('TagGroupName') is not None:
            self.tag_group_name = m.get('TagGroupName')
        if m.get('EntityRelationNumber') is not None:
            self.entity_relation_number = m.get('EntityRelationNumber')
        return self


class GetTagListResponseBodyData(TeaModel):
    def __init__(
        self,
        scenario_code: str = None,
        tag_group_code: str = None,
        tag_values: List[GetTagListResponseBodyDataTagValues] = None,
        tag_group_name: str = None,
    ):
        self.scenario_code = scenario_code
        self.tag_group_code = tag_group_code
        self.tag_values = tag_values
        self.tag_group_name = tag_group_name

    def validate(self):
        if self.tag_values:
            for k in self.tag_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scenario_code is not None:
            result['ScenarioCode'] = self.scenario_code
        if self.tag_group_code is not None:
            result['TagGroupCode'] = self.tag_group_code
        result['TagValues'] = []
        if self.tag_values is not None:
            for k in self.tag_values:
                result['TagValues'].append(k.to_map() if k else None)
        if self.tag_group_name is not None:
            result['TagGroupName'] = self.tag_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScenarioCode') is not None:
            self.scenario_code = m.get('ScenarioCode')
        if m.get('TagGroupCode') is not None:
            self.tag_group_code = m.get('TagGroupCode')
        self.tag_values = []
        if m.get('TagValues') is not None:
            for k in m.get('TagValues'):
                temp_model = GetTagListResponseBodyDataTagValues()
                self.tag_values.append(temp_model.from_map(k))
        if m.get('TagGroupName') is not None:
            self.tag_group_name = m.get('TagGroupName')
        return self


class GetTagListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetTagListResponseBodyData] = None,
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
                temp_model = GetTagListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTagListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTagListResponseBody = None,
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
            temp_model = GetTagListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTicketRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        ticket_id: int = None,
        operator_id: int = None,
        form_data: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.ticket_id = ticket_id
        self.operator_id = operator_id
        self.form_data = form_data

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
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.form_data is not None:
            result['FormData'] = self.form_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('FormData') is not None:
            self.form_data = m.get('FormData')
        return self


class UpdateTicketResponseBody(TeaModel):
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


class UpdateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTicketResponseBody = None,
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
            temp_model = UpdateTicketResponseBody()
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


class QueryHotlineSessionRequest(TeaModel):
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
        return self


class QueryHotlineSessionResponseBodyDataCallDetailRecord(TeaModel):
    def __init__(
        self,
        call_result: str = None,
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
        hang_up_role: str = None,
        member_name: str = None,
        evaluation_score: int = None,
        acid: str = None,
        ring_start_time: str = None,
        call_type: int = None,
        group_name: str = None,
        group_id: int = None,
        ring_end_time: str = None,
        in_queue_time: str = None,
        calling_number: str = None,
        member_id: str = None,
        queue_up_continue_time: int = None,
    ):
        self.call_result = call_result
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
        self.hang_up_role = hang_up_role
        self.member_name = member_name
        self.evaluation_score = evaluation_score
        self.acid = acid
        self.ring_start_time = ring_start_time
        self.call_type = call_type
        self.group_name = group_name
        self.group_id = group_id
        self.ring_end_time = ring_end_time
        self.in_queue_time = in_queue_time
        self.calling_number = calling_number
        self.member_id = member_id
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
        if self.hang_up_role is not None:
            result['HangUpRole'] = self.hang_up_role
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
        if self.in_queue_time is not None:
            result['InQueueTime'] = self.in_queue_time
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.queue_up_continue_time is not None:
            result['QueueUpContinueTime'] = self.queue_up_continue_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
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
        if m.get('HangUpRole') is not None:
            self.hang_up_role = m.get('HangUpRole')
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
        if m.get('InQueueTime') is not None:
            self.in_queue_time = m.get('InQueueTime')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('QueueUpContinueTime') is not None:
            self.queue_up_continue_time = m.get('QueueUpContinueTime')
        return self


class QueryHotlineSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        call_detail_record: List[QueryHotlineSessionResponseBodyDataCallDetailRecord] = None,
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
                temp_model = QueryHotlineSessionResponseBodyDataCallDetailRecord()
                self.call_detail_record.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryHotlineSessionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: QueryHotlineSessionResponseBodyData = None,
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
            temp_model = QueryHotlineSessionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryHotlineSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryHotlineSessionResponseBody = None,
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
            temp_model = QueryHotlineSessionResponseBody()
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


class StartCallV2Request(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        caller: str = None,
        callee: str = None,
        json_msg: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.caller = caller
        self.callee = callee
        self.json_msg = json_msg

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
        if self.json_msg is not None:
            result['JsonMsg'] = self.json_msg
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
        if m.get('JsonMsg') is not None:
            self.json_msg = m.get('JsonMsg')
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


class EnableRoleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        role_id: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.role_id = role_id

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
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class EnableRoleResponseBody(TeaModel):
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


class EnableRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableRoleResponseBody = None,
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
            temp_model = EnableRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentRequest(TeaModel):
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
        message: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success
        self.http_status_code = http_status_code
        self.message = message

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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
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


class GetCMSIdByForeignIdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        nick: str = None,
        foreign_id: str = None,
        source_id: int = None,
    ):
        self.instance_id = instance_id
        self.nick = nick
        self.foreign_id = foreign_id
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.foreign_id is not None:
            result['ForeignId'] = self.foreign_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('ForeignId') is not None:
            self.foreign_id = m.get('ForeignId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        return self


class GetCMSIdByForeignIdResponseBodyData(TeaModel):
    def __init__(
        self,
        status: int = None,
        customer_type_id: int = None,
        avatar: str = None,
        gender: str = None,
        foreign_id: str = None,
        user_id: str = None,
        nick: str = None,
        anonymity: bool = None,
        phone: str = None,
    ):
        self.status = status
        self.customer_type_id = customer_type_id
        self.avatar = avatar
        self.gender = gender
        self.foreign_id = foreign_id
        self.user_id = user_id
        self.nick = nick
        self.anonymity = anonymity
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.customer_type_id is not None:
            result['CustomerTypeId'] = self.customer_type_id
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.foreign_id is not None:
            result['ForeignId'] = self.foreign_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.anonymity is not None:
            result['Anonymity'] = self.anonymity
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CustomerTypeId') is not None:
            self.customer_type_id = m.get('CustomerTypeId')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('ForeignId') is not None:
            self.foreign_id = m.get('ForeignId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Anonymity') is not None:
            self.anonymity = m.get('Anonymity')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class GetCMSIdByForeignIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetCMSIdByForeignIdResponseBodyData = None,
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
            temp_model = GetCMSIdByForeignIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCMSIdByForeignIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCMSIdByForeignIdResponseBody = None,
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
            temp_model = GetCMSIdByForeignIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferToThirdCallRequest(TeaModel):
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


class TransferToThirdCallResponseBody(TeaModel):
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


class TransferToThirdCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferToThirdCallResponseBody = None,
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
            temp_model = TransferToThirdCallResponseBody()
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


class UpdateRingStatusRequest(TeaModel):
    def __init__(
        self,
        unique_biz_id: str = None,
        call_out_status: str = None,
        extra: str = None,
        instance_id: str = None,
    ):
        self.unique_biz_id = unique_biz_id
        self.call_out_status = call_out_status
        self.extra = extra
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unique_biz_id is not None:
            result['UniqueBizId'] = self.unique_biz_id
        if self.call_out_status is not None:
            result['CallOutStatus'] = self.call_out_status
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UniqueBizId') is not None:
            self.unique_biz_id = m.get('UniqueBizId')
        if m.get('CallOutStatus') is not None:
            self.call_out_status = m.get('CallOutStatus')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateRingStatusResponseBody(TeaModel):
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


class UpdateRingStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRingStatusResponseBody = None,
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
            temp_model = UpdateRingStatusResponseBody()
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


class DeleteEntityRouteRequest(TeaModel):
    def __init__(
        self,
        unique_id: int = None,
        instance_id: str = None,
    ):
        self.unique_id = unique_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteEntityRouteResponseBody(TeaModel):
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


class DeleteEntityRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteEntityRouteResponseBody = None,
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
            temp_model = DeleteEntityRouteResponseBody()
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


class CreateTicketRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        template_id: int = None,
        category_id: int = None,
        creator_id: int = None,
        creator_type: int = None,
        creator_name: str = None,
        member_id: int = None,
        member_name: str = None,
        from_info: str = None,
        priority: int = None,
        carbon_copy: str = None,
        form_data: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.template_id = template_id
        self.category_id = category_id
        self.creator_id = creator_id
        self.creator_type = creator_type
        self.creator_name = creator_name
        self.member_id = member_id
        self.member_name = member_name
        self.from_info = from_info
        self.priority = priority
        self.carbon_copy = carbon_copy
        self.form_data = form_data

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
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.from_info is not None:
            result['FromInfo'] = self.from_info
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.carbon_copy is not None:
            result['CarbonCopy'] = self.carbon_copy
        if self.form_data is not None:
            result['FormData'] = self.form_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('FromInfo') is not None:
            self.from_info = m.get('FromInfo')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CarbonCopy') is not None:
            self.carbon_copy = m.get('CarbonCopy')
        if m.get('FormData') is not None:
            self.form_data = m.get('FormData')
        return self


class CreateTicketResponseBody(TeaModel):
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


class CreateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTicketResponseBody = None,
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
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomerRequest(TeaModel):
    def __init__(
        self,
        prod_line_id: int = None,
        biz_type: str = None,
        name: str = None,
        type_code: str = None,
        phone: str = None,
        instance_id: str = None,
        manager_name: str = None,
        contacter: str = None,
        industry: str = None,
        position: str = None,
        email: str = None,
        dingding: str = None,
        outer_id: str = None,
        outer_id_type: int = None,
        customer_id: int = None,
    ):
        self.prod_line_id = prod_line_id
        self.biz_type = biz_type
        self.name = name
        self.type_code = type_code
        self.phone = phone
        self.instance_id = instance_id
        self.manager_name = manager_name
        self.contacter = contacter
        self.industry = industry
        self.position = position
        self.email = email
        self.dingding = dingding
        self.outer_id = outer_id
        self.outer_id_type = outer_id_type
        self.customer_id = customer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prod_line_id is not None:
            result['ProdLineId'] = self.prod_line_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.name is not None:
            result['Name'] = self.name
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.manager_name is not None:
            result['ManagerName'] = self.manager_name
        if self.contacter is not None:
            result['Contacter'] = self.contacter
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.position is not None:
            result['Position'] = self.position
        if self.email is not None:
            result['Email'] = self.email
        if self.dingding is not None:
            result['Dingding'] = self.dingding
        if self.outer_id is not None:
            result['OuterId'] = self.outer_id
        if self.outer_id_type is not None:
            result['OuterIdType'] = self.outer_id_type
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProdLineId') is not None:
            self.prod_line_id = m.get('ProdLineId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ManagerName') is not None:
            self.manager_name = m.get('ManagerName')
        if m.get('Contacter') is not None:
            self.contacter = m.get('Contacter')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Dingding') is not None:
            self.dingding = m.get('Dingding')
        if m.get('OuterId') is not None:
            self.outer_id = m.get('OuterId')
        if m.get('OuterIdType') is not None:
            self.outer_id_type = m.get('OuterIdType')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        return self


class UpdateCustomerResponseBody(TeaModel):
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


class UpdateCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateCustomerResponseBody = None,
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
            temp_model = UpdateCustomerResponseBody()
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


class DeleteAgentRequest(TeaModel):
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


class GetEntityTagRelationRequest(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
        instance_id: str = None,
    ):
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetEntityTagRelationResponseBodyData(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
        tag_group_code: str = None,
        entity_id: str = None,
        tag_code: str = None,
        entity_type: str = None,
        tag_group_name: str = None,
    ):
        self.tag_name = tag_name
        self.tag_group_code = tag_group_code
        self.entity_id = entity_id
        self.tag_code = tag_code
        self.entity_type = entity_type
        self.tag_group_name = tag_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_group_code is not None:
            result['TagGroupCode'] = self.tag_group_code
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.tag_code is not None:
            result['TagCode'] = self.tag_code
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.tag_group_name is not None:
            result['TagGroupName'] = self.tag_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagGroupCode') is not None:
            self.tag_group_code = m.get('TagGroupCode')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('TagCode') is not None:
            self.tag_code = m.get('TagCode')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('TagGroupName') is not None:
            self.tag_group_name = m.get('TagGroupName')
        return self


class GetEntityTagRelationResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetEntityTagRelationResponseBodyData] = None,
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
                temp_model = GetEntityTagRelationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEntityTagRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEntityTagRelationResponseBody = None,
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
            temp_model = GetEntityTagRelationResponseBody()
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


class GetCallsPerDayRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        data_id_start: str = None,
        data_id_end: str = None,
        data_id: str = None,
        hour_id: str = None,
        minute_id: str = None,
        phone_numbers: str = None,
        have_phone_numbers: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.data_id_start = data_id_start
        self.data_id_end = data_id_end
        self.data_id = data_id
        self.hour_id = hour_id
        self.minute_id = minute_id
        self.phone_numbers = phone_numbers
        self.have_phone_numbers = have_phone_numbers
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
        if self.data_id_start is not None:
            result['DataIdStart'] = self.data_id_start
        if self.data_id_end is not None:
            result['DataIdEnd'] = self.data_id_end
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.hour_id is not None:
            result['HourId'] = self.hour_id
        if self.minute_id is not None:
            result['MinuteId'] = self.minute_id
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.have_phone_numbers is not None:
            result['HavePhoneNumbers'] = self.have_phone_numbers
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DataIdStart') is not None:
            self.data_id_start = m.get('DataIdStart')
        if m.get('DataIdEnd') is not None:
            self.data_id_end = m.get('DataIdEnd')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('HourId') is not None:
            self.hour_id = m.get('HourId')
        if m.get('MinuteId') is not None:
            self.minute_id = m.get('MinuteId')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('HavePhoneNumbers') is not None:
            self.have_phone_numbers = m.get('HavePhoneNumbers')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetCallsPerDayResponseBodyDataCallsPerdayResponseList(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        hour_id: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        phone_num: str = None,
        call_out_cnt: str = None,
        call_in_cnt: str = None,
        minute_id: str = None,
    ):
        self.data_id = data_id
        self.hour_id = hour_id
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.phone_num = phone_num
        self.call_out_cnt = call_out_cnt
        self.call_in_cnt = call_in_cnt
        self.minute_id = minute_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.hour_id is not None:
            result['HourId'] = self.hour_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.call_out_cnt is not None:
            result['CallOutCnt'] = self.call_out_cnt
        if self.call_in_cnt is not None:
            result['CallInCnt'] = self.call_in_cnt
        if self.minute_id is not None:
            result['MinuteId'] = self.minute_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('HourId') is not None:
            self.hour_id = m.get('HourId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('CallOutCnt') is not None:
            self.call_out_cnt = m.get('CallOutCnt')
        if m.get('CallInCnt') is not None:
            self.call_in_cnt = m.get('CallInCnt')
        if m.get('MinuteId') is not None:
            self.minute_id = m.get('MinuteId')
        return self


class GetCallsPerDayResponseBodyData(TeaModel):
    def __init__(
        self,
        total_num: int = None,
        page_size: int = None,
        page_no: str = None,
        calls_perday_response_list: List[GetCallsPerDayResponseBodyDataCallsPerdayResponseList] = None,
    ):
        self.total_num = total_num
        self.page_size = page_size
        self.page_no = page_no
        self.calls_perday_response_list = calls_perday_response_list

    def validate(self):
        if self.calls_perday_response_list:
            for k in self.calls_perday_response_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_num is not None:
            result['TotalNum'] = self.total_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        result['CallsPerdayResponseList'] = []
        if self.calls_perday_response_list is not None:
            for k in self.calls_perday_response_list:
                result['CallsPerdayResponseList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.calls_perday_response_list = []
        if m.get('CallsPerdayResponseList') is not None:
            for k in m.get('CallsPerdayResponseList'):
                temp_model = GetCallsPerDayResponseBodyDataCallsPerdayResponseList()
                self.calls_perday_response_list.append(temp_model.from_map(k))
        return self


class GetCallsPerDayResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: str = None,
        data: GetCallsPerDayResponseBodyData = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success
        self.data = data

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
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetCallsPerDayResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetCallsPerDayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCallsPerDayResponseBody = None,
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
            temp_model = GetCallsPerDayResponseBody()
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


class QueryTicketCountRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        operator_id: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.operator_id = operator_id

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
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        return self


class QueryTicketCountResponseBody(TeaModel):
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


class QueryTicketCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTicketCountResponseBody = None,
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
            temp_model = QueryTicketCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppMessagePushRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        user_id: str = None,
        status: int = None,
        expiration_time: int = None,
    ):
        # 实例ID
        self.instance_id = instance_id
        # 用户编号
        self.user_id = user_id
        # APP状态
        self.status = status
        # 过期时间
        self.expiration_time = expiration_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.status is not None:
            result['Status'] = self.status
        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')
        return self


class AppMessagePushResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        code: str = None,
        message: str = None,
        success: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 返回数据
        self.data = data
        # 错误码
        self.code = code
        # 错误信息
        self.message = message
        # 通信码
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppMessagePushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AppMessagePushResponseBody = None,
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
            temp_model = AppMessagePushResponseBody()
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


class AssignTicketRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        ticket_id: int = None,
        operator_id: int = None,
        acceptor_id: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.ticket_id = ticket_id
        self.operator_id = operator_id
        self.acceptor_id = acceptor_id

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
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.acceptor_id is not None:
            result['AcceptorId'] = self.acceptor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('AcceptorId') is not None:
            self.acceptor_id = m.get('AcceptorId')
        return self


class AssignTicketResponseBody(TeaModel):
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


class AssignTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssignTicketResponseBody = None,
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
            temp_model = AssignTicketResponseBody()
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


class CreateTicketWithBizDataRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        template_id: int = None,
        category_id: int = None,
        creator_id: int = None,
        creator_type: int = None,
        creator_name: str = None,
        member_id: int = None,
        member_name: str = None,
        from_info: str = None,
        priority: int = None,
        carbon_copy: str = None,
        form_data: str = None,
        biz_data: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.template_id = template_id
        self.category_id = category_id
        self.creator_id = creator_id
        self.creator_type = creator_type
        self.creator_name = creator_name
        self.member_id = member_id
        self.member_name = member_name
        self.from_info = from_info
        self.priority = priority
        self.carbon_copy = carbon_copy
        self.form_data = form_data
        self.biz_data = biz_data

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
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.from_info is not None:
            result['FromInfo'] = self.from_info
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.carbon_copy is not None:
            result['CarbonCopy'] = self.carbon_copy
        if self.form_data is not None:
            result['FormData'] = self.form_data
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('FromInfo') is not None:
            self.from_info = m.get('FromInfo')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CarbonCopy') is not None:
            self.carbon_copy = m.get('CarbonCopy')
        if m.get('FormData') is not None:
            self.form_data = m.get('FormData')
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        return self


class CreateTicketWithBizDataResponseBody(TeaModel):
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


class CreateTicketWithBizDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTicketWithBizDataResponseBody = None,
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
            temp_model = CreateTicketWithBizDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTicketByPhoneRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        phone: str = None,
        template_id: int = None,
        ticket_status: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.phone = phone
        self.template_id = template_id
        self.ticket_status = ticket_status
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time

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
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.ticket_status is not None:
            result['TicketStatus'] = self.ticket_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TicketStatus') is not None:
            self.ticket_status = m.get('TicketStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class SearchTicketByPhoneResponseBodyData(TeaModel):
    def __init__(
        self,
        member_name: str = None,
        carbon_copy: str = None,
        create_time: int = None,
        service_id: int = None,
        ticket_id: int = None,
        priority: int = None,
        creator_id: int = None,
        form_data: str = None,
        from_info: str = None,
        modified_time: int = None,
        task_status: str = None,
        creator_name: str = None,
        category_id: int = None,
        creator_type: int = None,
        member_id: int = None,
        case_status: int = None,
        template_id: int = None,
    ):
        self.member_name = member_name
        self.carbon_copy = carbon_copy
        self.create_time = create_time
        self.service_id = service_id
        self.ticket_id = ticket_id
        self.priority = priority
        self.creator_id = creator_id
        self.form_data = form_data
        self.from_info = from_info
        self.modified_time = modified_time
        self.task_status = task_status
        self.creator_name = creator_name
        self.category_id = category_id
        self.creator_type = creator_type
        self.member_id = member_id
        self.case_status = case_status
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.carbon_copy is not None:
            result['CarbonCopy'] = self.carbon_copy
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.form_data is not None:
            result['FormData'] = self.form_data
        if self.from_info is not None:
            result['FromInfo'] = self.from_info
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.case_status is not None:
            result['CaseStatus'] = self.case_status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('CarbonCopy') is not None:
            self.carbon_copy = m.get('CarbonCopy')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('FormData') is not None:
            self.form_data = m.get('FormData')
        if m.get('FromInfo') is not None:
            self.from_info = m.get('FromInfo')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class SearchTicketByPhoneResponseBody(TeaModel):
    def __init__(
        self,
        one_page_size: int = None,
        request_id: str = None,
        message: str = None,
        total_page: int = None,
        total_results: int = None,
        page_no: int = None,
        data: List[SearchTicketByPhoneResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.one_page_size = one_page_size
        self.request_id = request_id
        self.message = message
        self.total_page = total_page
        self.total_results = total_results
        self.page_no = page_no
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
        if self.one_page_size is not None:
            result['OnePageSize'] = self.one_page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.total_results is not None:
            result['TotalResults'] = self.total_results
        if self.page_no is not None:
            result['PageNo'] = self.page_no
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
        if m.get('OnePageSize') is not None:
            self.one_page_size = m.get('OnePageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchTicketByPhoneResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchTicketByPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTicketByPhoneResponseBody = None,
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
            temp_model = SearchTicketByPhoneResponseBody()
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


class CreateEntityIvrRouteRequest(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_name: str = None,
        entity_biz_code: str = None,
        entity_biz_code_type: str = None,
        entity_relation_number: str = None,
        department_id: str = None,
        group_id: int = None,
        service_id: int = None,
        ext_info: str = None,
        instance_id: str = None,
    ):
        self.entity_id = entity_id
        self.entity_name = entity_name
        self.entity_biz_code = entity_biz_code
        self.entity_biz_code_type = entity_biz_code_type
        self.entity_relation_number = entity_relation_number
        self.department_id = department_id
        self.group_id = group_id
        self.service_id = service_id
        self.ext_info = ext_info
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_biz_code is not None:
            result['EntityBizCode'] = self.entity_biz_code
        if self.entity_biz_code_type is not None:
            result['EntityBizCodeType'] = self.entity_biz_code_type
        if self.entity_relation_number is not None:
            result['EntityRelationNumber'] = self.entity_relation_number
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityBizCode') is not None:
            self.entity_biz_code = m.get('EntityBizCode')
        if m.get('EntityBizCodeType') is not None:
            self.entity_biz_code_type = m.get('EntityBizCodeType')
        if m.get('EntityRelationNumber') is not None:
            self.entity_relation_number = m.get('EntityRelationNumber')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateEntityIvrRouteResponseBody(TeaModel):
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


class CreateEntityIvrRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateEntityIvrRouteResponseBody = None,
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
            temp_model = CreateEntityIvrRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseTicketRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        ticket_id: int = None,
        action_items: str = None,
        operator_id: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.ticket_id = ticket_id
        self.action_items = action_items
        self.operator_id = operator_id

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
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.action_items is not None:
            result['ActionItems'] = self.action_items
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('ActionItems') is not None:
            self.action_items = m.get('ActionItems')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        return self


class CloseTicketResponseBody(TeaModel):
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


class CloseTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseTicketResponseBody = None,
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
            temp_model = CloseTicketResponseBody()
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


class QueryRingDetailListRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_no: int = None,
        start_date: int = None,
        end_date: int = None,
        call_out_status: str = None,
        extra: str = None,
        instance_id: str = None,
        from_phone_num_list: Dict[str, Any] = None,
        to_phone_num_list: Dict[str, Any] = None,
    ):
        self.page_size = page_size
        self.page_no = page_no
        self.start_date = start_date
        self.end_date = end_date
        self.call_out_status = call_out_status
        self.extra = extra
        self.instance_id = instance_id
        self.from_phone_num_list = from_phone_num_list
        self.to_phone_num_list = to_phone_num_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.call_out_status is not None:
            result['CallOutStatus'] = self.call_out_status
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.from_phone_num_list is not None:
            result['FromPhoneNumList'] = self.from_phone_num_list
        if self.to_phone_num_list is not None:
            result['ToPhoneNumList'] = self.to_phone_num_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('CallOutStatus') is not None:
            self.call_out_status = m.get('CallOutStatus')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('FromPhoneNumList') is not None:
            self.from_phone_num_list = m.get('FromPhoneNumList')
        if m.get('ToPhoneNumList') is not None:
            self.to_phone_num_list = m.get('ToPhoneNumList')
        return self


class QueryRingDetailListShrinkRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_no: int = None,
        start_date: int = None,
        end_date: int = None,
        call_out_status: str = None,
        extra: str = None,
        instance_id: str = None,
        from_phone_num_list_shrink: str = None,
        to_phone_num_list_shrink: str = None,
    ):
        self.page_size = page_size
        self.page_no = page_no
        self.start_date = start_date
        self.end_date = end_date
        self.call_out_status = call_out_status
        self.extra = extra
        self.instance_id = instance_id
        self.from_phone_num_list_shrink = from_phone_num_list_shrink
        self.to_phone_num_list_shrink = to_phone_num_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.call_out_status is not None:
            result['CallOutStatus'] = self.call_out_status
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.from_phone_num_list_shrink is not None:
            result['FromPhoneNumList'] = self.from_phone_num_list_shrink
        if self.to_phone_num_list_shrink is not None:
            result['ToPhoneNumList'] = self.to_phone_num_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('CallOutStatus') is not None:
            self.call_out_status = m.get('CallOutStatus')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('FromPhoneNumList') is not None:
            self.from_phone_num_list_shrink = m.get('FromPhoneNumList')
        if m.get('ToPhoneNumList') is not None:
            self.to_phone_num_list_shrink = m.get('ToPhoneNumList')
        return self


class QueryRingDetailListResponseBody(TeaModel):
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


class QueryRingDetailListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRingDetailListResponseBody = None,
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
            temp_model = QueryRingDetailListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTicketByIdRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        ticket_id: int = None,
        status_code: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.ticket_id = ticket_id
        self.status_code = status_code

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
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class SearchTicketByIdResponseBodyDataActivities(TeaModel):
    def __init__(
        self,
        activity_form_data: str = None,
        activity_code: str = None,
    ):
        self.activity_form_data = activity_form_data
        self.activity_code = activity_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_form_data is not None:
            result['ActivityFormData'] = self.activity_form_data
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityFormData') is not None:
            self.activity_form_data = m.get('ActivityFormData')
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')
        return self


class SearchTicketByIdResponseBodyDataActivityRecords(TeaModel):
    def __init__(
        self,
        action_code: str = None,
        action_code_desc: str = None,
        operator_name: str = None,
        memo: str = None,
        gmt_create: int = None,
    ):
        self.action_code = action_code
        self.action_code_desc = action_code_desc
        self.operator_name = operator_name
        self.memo = memo
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_code_desc is not None:
            result['ActionCodeDesc'] = self.action_code_desc
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionCodeDesc') is not None:
            self.action_code_desc = m.get('ActionCodeDesc')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class SearchTicketByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        carbon_copy: str = None,
        member_name: str = None,
        create_time: int = None,
        service_id: int = None,
        ticket_id: int = None,
        priority: int = None,
        creator_id: int = None,
        form_data: str = None,
        activities: List[SearchTicketByIdResponseBodyDataActivities] = None,
        activity_records: List[SearchTicketByIdResponseBodyDataActivityRecords] = None,
        from_info: str = None,
        modified_time: int = None,
        creator_name: str = None,
        category_id: int = None,
        creator_type: int = None,
        member_id: int = None,
        case_status: int = None,
        template_id: int = None,
        ticket_name: str = None,
    ):
        self.carbon_copy = carbon_copy
        self.member_name = member_name
        self.create_time = create_time
        self.service_id = service_id
        self.ticket_id = ticket_id
        self.priority = priority
        self.creator_id = creator_id
        self.form_data = form_data
        self.activities = activities
        self.activity_records = activity_records
        self.from_info = from_info
        self.modified_time = modified_time
        self.creator_name = creator_name
        self.category_id = category_id
        self.creator_type = creator_type
        self.member_id = member_id
        self.case_status = case_status
        self.template_id = template_id
        self.ticket_name = ticket_name

    def validate(self):
        if self.activities:
            for k in self.activities:
                if k:
                    k.validate()
        if self.activity_records:
            for k in self.activity_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.carbon_copy is not None:
            result['CarbonCopy'] = self.carbon_copy
        if self.member_name is not None:
            result['MemberName'] = self.member_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.form_data is not None:
            result['FormData'] = self.form_data
        result['Activities'] = []
        if self.activities is not None:
            for k in self.activities:
                result['Activities'].append(k.to_map() if k else None)
        result['ActivityRecords'] = []
        if self.activity_records is not None:
            for k in self.activity_records:
                result['ActivityRecords'].append(k.to_map() if k else None)
        if self.from_info is not None:
            result['FromInfo'] = self.from_info
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.case_status is not None:
            result['CaseStatus'] = self.case_status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.ticket_name is not None:
            result['TicketName'] = self.ticket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CarbonCopy') is not None:
            self.carbon_copy = m.get('CarbonCopy')
        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('FormData') is not None:
            self.form_data = m.get('FormData')
        self.activities = []
        if m.get('Activities') is not None:
            for k in m.get('Activities'):
                temp_model = SearchTicketByIdResponseBodyDataActivities()
                self.activities.append(temp_model.from_map(k))
        self.activity_records = []
        if m.get('ActivityRecords') is not None:
            for k in m.get('ActivityRecords'):
                temp_model = SearchTicketByIdResponseBodyDataActivityRecords()
                self.activity_records.append(temp_model.from_map(k))
        if m.get('FromInfo') is not None:
            self.from_info = m.get('FromInfo')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('CaseStatus') is not None:
            self.case_status = m.get('CaseStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TicketName') is not None:
            self.ticket_name = m.get('TicketName')
        return self


class SearchTicketByIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: SearchTicketByIdResponseBodyData = None,
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
            temp_model = SearchTicketByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class SearchTicketByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTicketByIdResponseBody = None,
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
            temp_model = SearchTicketByIdResponseBody()
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
        channel_type: int = None,
    ):
        self.instance_id = instance_id
        self.skill_group_id = skill_group_id
        self.skill_group_name = skill_group_name
        self.description = description
        self.display_name = display_name
        self.client_token = client_token
        # 渠道类型
        self.channel_type = channel_type

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
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
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
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        return self


class UpdateSkillGroupResponseBody(TeaModel):
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


class QueryServiceConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        view_code: str = None,
        parameters: str = None,
    ):
        self.instance_id = instance_id
        self.view_code = view_code
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.view_code is not None:
            result['ViewCode'] = self.view_code
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ViewCode') is not None:
            self.view_code = m.get('ViewCode')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class QueryServiceConfigResponseBody(TeaModel):
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


class QueryServiceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryServiceConfigResponseBody = None,
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
            temp_model = QueryServiceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableRoleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        role_id: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.role_id = role_id

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
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class DisableRoleResponseBody(TeaModel):
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


class DisableRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableRoleResponseBody = None,
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
            temp_model = DisableRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEntityRouteListRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_no: int = None,
        instance_id: str = None,
        entity_relation_number: str = None,
        entity_name: str = None,
    ):
        self.page_size = page_size
        self.page_no = page_no
        self.instance_id = instance_id
        self.entity_relation_number = entity_relation_number
        self.entity_name = entity_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.entity_relation_number is not None:
            result['EntityRelationNumber'] = self.entity_relation_number
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EntityRelationNumber') is not None:
            self.entity_relation_number = m.get('EntityRelationNumber')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        return self


class GetEntityRouteListResponseBodyDataEntityRouteList(TeaModel):
    def __init__(
        self,
        entity_biz_code_type: str = None,
        group_id: str = None,
        entity_id: str = None,
        service_id: str = None,
        department_id: str = None,
        entity_biz_code: str = None,
        unique_id: int = None,
        entity_name: str = None,
        ext_info: str = None,
        entity_relation_number: str = None,
    ):
        self.entity_biz_code_type = entity_biz_code_type
        self.group_id = group_id
        self.entity_id = entity_id
        self.service_id = service_id
        self.department_id = department_id
        self.entity_biz_code = entity_biz_code
        self.unique_id = unique_id
        self.entity_name = entity_name
        self.ext_info = ext_info
        self.entity_relation_number = entity_relation_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_biz_code_type is not None:
            result['EntityBizCodeType'] = self.entity_biz_code_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.entity_biz_code is not None:
            result['EntityBizCode'] = self.entity_biz_code
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.entity_relation_number is not None:
            result['EntityRelationNumber'] = self.entity_relation_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityBizCodeType') is not None:
            self.entity_biz_code_type = m.get('EntityBizCodeType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('EntityBizCode') is not None:
            self.entity_biz_code = m.get('EntityBizCode')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('EntityRelationNumber') is not None:
            self.entity_relation_number = m.get('EntityRelationNumber')
        return self


class GetEntityRouteListResponseBodyData(TeaModel):
    def __init__(
        self,
        entity_route_list: List[GetEntityRouteListResponseBodyDataEntityRouteList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.entity_route_list = entity_route_list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.entity_route_list:
            for k in self.entity_route_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EntityRouteList'] = []
        if self.entity_route_list is not None:
            for k in self.entity_route_list:
                result['EntityRouteList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_route_list = []
        if m.get('EntityRouteList') is not None:
            for k in m.get('EntityRouteList'):
                temp_model = GetEntityRouteListResponseBodyDataEntityRouteList()
                self.entity_route_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetEntityRouteListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetEntityRouteListResponseBodyData = None,
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
            temp_model = GetEntityRouteListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEntityRouteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEntityRouteListResponseBody = None,
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
            temp_model = GetEntityRouteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        foreign_id: str = None,
        app_key: str = None,
    ):
        self.instance_id = instance_id
        self.foreign_id = foreign_id
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.foreign_id is not None:
            result['ForeignId'] = self.foreign_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ForeignId') is not None:
            self.foreign_id = m.get('ForeignId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAuthInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        time: int = None,
        app_key: str = None,
        app: str = None,
        user_id: str = None,
        code: str = None,
        session_id: str = None,
        user_name: str = None,
        tenant_id: str = None,
    ):
        self.app_name = app_name
        self.time = time
        self.app_key = app_key
        self.app = app
        self.user_id = user_id
        self.code = code
        self.session_id = session_id
        self.user_name = user_name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.time is not None:
            result['Time'] = self.time
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app is not None:
            result['App'] = self.app
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code is not None:
            result['Code'] = self.code
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('App') is not None:
            self.app = m.get('App')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetAuthInfoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAuthInfoResponseBodyData = None,
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
            temp_model = GetAuthInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAuthInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthInfoResponseBody = None,
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
            temp_model = GetAuthInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        role_id: int = None,
        role_name: str = None,
        operator: str = None,
        permission_id: List[int] = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.role_id = role_id
        self.role_name = role_name
        self.operator = operator
        self.permission_id = permission_id

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
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.permission_id is not None:
            result['PermissionId'] = self.permission_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PermissionId') is not None:
            self.permission_id = m.get('PermissionId')
        return self


class UpdateRoleResponseBody(TeaModel):
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


class UpdateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRoleResponseBody = None,
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
            temp_model = UpdateRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTicketTemplateSchemaRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        template_id: int = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.template_id = template_id

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
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTicketTemplateSchemaResponseBody(TeaModel):
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


class GetTicketTemplateSchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTicketTemplateSchemaResponseBody = None,
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
            temp_model = GetTicketTemplateSchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferCallToPhoneRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        caller: str = None,
        callee: str = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
        hold_connection_id: str = None,
        type: int = None,
        is_single_transfer: bool = None,
        caller_phone: str = None,
        callee_phone: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.caller = caller
        self.callee = callee
        self.call_id = call_id
        self.job_id = job_id
        self.connection_id = connection_id
        self.hold_connection_id = hold_connection_id
        self.type = type
        self.is_single_transfer = is_single_transfer
        self.caller_phone = caller_phone
        self.callee_phone = callee_phone

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
        if self.caller_phone is not None:
            result['callerPhone'] = self.caller_phone
        if self.callee_phone is not None:
            result['calleePhone'] = self.callee_phone
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
        if m.get('callerPhone') is not None:
            self.caller_phone = m.get('callerPhone')
        if m.get('calleePhone') is not None:
            self.callee_phone = m.get('calleePhone')
        return self


class TransferCallToPhoneResponseBody(TeaModel):
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


class TransferCallToPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferCallToPhoneResponseBody = None,
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
            temp_model = TransferCallToPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySkillGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        client_token: str = None,
        group_name: str = None,
        group_type: int = None,
        group_id: int = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.client_token = client_token
        self.group_name = group_name
        self.group_type = group_type
        self.group_id = group_id

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
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
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
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
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


class GetEntityRouteRequest(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        unique_id: int = None,
        instance_id: str = None,
        entity_name: str = None,
        entity_relation_number: str = None,
        entity_biz_code: str = None,
    ):
        self.entity_id = entity_id
        self.unique_id = unique_id
        self.instance_id = instance_id
        self.entity_name = entity_name
        self.entity_relation_number = entity_relation_number
        self.entity_biz_code = entity_biz_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.entity_relation_number is not None:
            result['EntityRelationNumber'] = self.entity_relation_number
        if self.entity_biz_code is not None:
            result['EntityBizCode'] = self.entity_biz_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('EntityRelationNumber') is not None:
            self.entity_relation_number = m.get('EntityRelationNumber')
        if m.get('EntityBizCode') is not None:
            self.entity_biz_code = m.get('EntityBizCode')
        return self


class GetEntityRouteResponseBodyData(TeaModel):
    def __init__(
        self,
        entity_biz_code_type: str = None,
        group_id: int = None,
        entity_id: str = None,
        service_id: int = None,
        entity_biz_code: str = None,
        department_id: str = None,
        unique_id: int = None,
        entity_name: str = None,
        ext_info: str = None,
        entity_relation_number: str = None,
    ):
        self.entity_biz_code_type = entity_biz_code_type
        self.group_id = group_id
        self.entity_id = entity_id
        self.service_id = service_id
        self.entity_biz_code = entity_biz_code
        self.department_id = department_id
        self.unique_id = unique_id
        self.entity_name = entity_name
        self.ext_info = ext_info
        self.entity_relation_number = entity_relation_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_biz_code_type is not None:
            result['EntityBizCodeType'] = self.entity_biz_code_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.entity_biz_code is not None:
            result['EntityBizCode'] = self.entity_biz_code
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id
        if self.entity_name is not None:
            result['EntityName'] = self.entity_name
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.entity_relation_number is not None:
            result['EntityRelationNumber'] = self.entity_relation_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityBizCodeType') is not None:
            self.entity_biz_code_type = m.get('EntityBizCodeType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('EntityBizCode') is not None:
            self.entity_biz_code = m.get('EntityBizCode')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')
        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('EntityRelationNumber') is not None:
            self.entity_relation_number = m.get('EntityRelationNumber')
        return self


class GetEntityRouteResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetEntityRouteResponseBodyData = None,
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
            temp_model = GetEntityRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEntityRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEntityRouteResponseBody = None,
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
            temp_model = GetEntityRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEntityTagRelationRequest(TeaModel):
    def __init__(
        self,
        entity_tag_param: str = None,
        instance_id: str = None,
    ):
        self.entity_tag_param = entity_tag_param
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_tag_param is not None:
            result['EntityTagParam'] = self.entity_tag_param
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityTagParam') is not None:
            self.entity_tag_param = m.get('EntityTagParam')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateEntityTagRelationResponseBody(TeaModel):
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


class UpdateEntityTagRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEntityTagRelationResponseBody = None,
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
            temp_model = UpdateEntityTagRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOuterCallCenterDataRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        intervene_time: str = None,
        call_type: str = None,
        from_phone_num: str = None,
        to_phone_num: str = None,
        end_reason: str = None,
        user_info: str = None,
        record_url: str = None,
        biz_type: str = None,
        biz_id: str = None,
        tenant_id: str = None,
        ext_info: str = None,
        instance_id: str = None,
    ):
        self.session_id = session_id
        self.intervene_time = intervene_time
        self.call_type = call_type
        self.from_phone_num = from_phone_num
        self.to_phone_num = to_phone_num
        self.end_reason = end_reason
        self.user_info = user_info
        self.record_url = record_url
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.tenant_id = tenant_id
        self.ext_info = ext_info
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.intervene_time is not None:
            result['InterveneTime'] = self.intervene_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.from_phone_num is not None:
            result['FromPhoneNum'] = self.from_phone_num
        if self.to_phone_num is not None:
            result['ToPhoneNum'] = self.to_phone_num
        if self.end_reason is not None:
            result['EndReason'] = self.end_reason
        if self.user_info is not None:
            result['UserInfo'] = self.user_info
        if self.record_url is not None:
            result['RecordUrl'] = self.record_url
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('InterveneTime') is not None:
            self.intervene_time = m.get('InterveneTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('FromPhoneNum') is not None:
            self.from_phone_num = m.get('FromPhoneNum')
        if m.get('ToPhoneNum') is not None:
            self.to_phone_num = m.get('ToPhoneNum')
        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')
        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')
        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateOuterCallCenterDataResponseBody(TeaModel):
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


class CreateOuterCallCenterDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOuterCallCenterDataResponseBody = None,
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
            temp_model = CreateOuterCallCenterDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendOutboundCommandRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        account_name: str = None,
        calling_number: str = None,
        called_number: str = None,
        customer_info: str = None,
    ):
        self.instance_id = instance_id
        self.account_name = account_name
        self.calling_number = calling_number
        self.called_number = called_number
        self.customer_info = customer_info

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
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.customer_info is not None:
            result['CustomerInfo'] = self.customer_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CustomerInfo') is not None:
            self.customer_info = m.get('CustomerInfo')
        return self


class SendOutboundCommandResponseBody(TeaModel):
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


class SendOutboundCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendOutboundCommandResponseBody = None,
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
            temp_model = SendOutboundCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        role_name: str = None,
        operator: str = None,
        permission_id: List[int] = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.role_name = role_name
        self.operator = operator
        self.permission_id = permission_id

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
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.permission_id is not None:
            result['PermissionId'] = self.permission_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('PermissionId') is not None:
            self.permission_id = m.get('PermissionId')
        return self


class CreateRoleResponseBody(TeaModel):
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


class CreateRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRoleResponseBody = None,
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
            temp_model = CreateRoleResponseBody()
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


class GrantRolesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        operator: str = None,
        role_id: List[int] = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.operator = operator
        self.role_id = role_id

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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.role_id is not None:
            result['RoleId'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')
        return self


class GrantRolesResponseBody(TeaModel):
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


class GrantRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GrantRolesResponseBody = None,
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
            temp_model = GrantRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOuterCallCenterDataListRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        from_phone_num: str = None,
        to_phone_num: str = None,
        biz_id: str = None,
        instance_id: str = None,
        query_start_time: str = None,
        query_end_time: str = None,
    ):
        self.session_id = session_id
        self.from_phone_num = from_phone_num
        self.to_phone_num = to_phone_num
        self.biz_id = biz_id
        self.instance_id = instance_id
        self.query_start_time = query_start_time
        self.query_end_time = query_end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.from_phone_num is not None:
            result['FromPhoneNum'] = self.from_phone_num
        if self.to_phone_num is not None:
            result['ToPhoneNum'] = self.to_phone_num
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time
        if self.query_end_time is not None:
            result['QueryEndTime'] = self.query_end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('FromPhoneNum') is not None:
            self.from_phone_num = m.get('FromPhoneNum')
        if m.get('ToPhoneNum') is not None:
            self.to_phone_num = m.get('ToPhoneNum')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')
        if m.get('QueryEndTime') is not None:
            self.query_end_time = m.get('QueryEndTime')
        return self


class GetOuterCallCenterDataListResponseBodyData(TeaModel):
    def __init__(
        self,
        end_reason: str = None,
        call_type: str = None,
        acid: str = None,
        to_phone_num: str = None,
        user_info: str = None,
        intervene_time: str = None,
        biz_id: str = None,
        session_id: str = None,
        from_phone_num: str = None,
        ext_info: str = None,
        biz_type: str = None,
    ):
        self.end_reason = end_reason
        self.call_type = call_type
        self.acid = acid
        self.to_phone_num = to_phone_num
        self.user_info = user_info
        self.intervene_time = intervene_time
        self.biz_id = biz_id
        self.session_id = session_id
        self.from_phone_num = from_phone_num
        self.ext_info = ext_info
        self.biz_type = biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_reason is not None:
            result['EndReason'] = self.end_reason
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.to_phone_num is not None:
            result['ToPhoneNum'] = self.to_phone_num
        if self.user_info is not None:
            result['UserInfo'] = self.user_info
        if self.intervene_time is not None:
            result['InterveneTime'] = self.intervene_time
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.from_phone_num is not None:
            result['FromPhoneNum'] = self.from_phone_num
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('ToPhoneNum') is not None:
            self.to_phone_num = m.get('ToPhoneNum')
        if m.get('UserInfo') is not None:
            self.user_info = m.get('UserInfo')
        if m.get('InterveneTime') is not None:
            self.intervene_time = m.get('InterveneTime')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('FromPhoneNum') is not None:
            self.from_phone_num = m.get('FromPhoneNum')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class GetOuterCallCenterDataListResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[GetOuterCallCenterDataListResponseBodyData] = None,
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = GetOuterCallCenterDataListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class GetOuterCallCenterDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOuterCallCenterDataListResponseBody = None,
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
            temp_model = GetOuterCallCenterDataListResponseBody()
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
        account_name: str = None,
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
        self.account_name = account_name
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
        if self.account_name is not None:
            result['AccountName'] = self.account_name
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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
        account_name: str = None,
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
        self.account_name = account_name
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
        if self.account_name is not None:
            result['AccountName'] = self.account_name
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
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
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


class QueryTicketActionsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ticket_id: str = None,
        action_code_list: List[int] = None,
    ):
        self.instance_id = instance_id
        self.ticket_id = ticket_id
        self.action_code_list = action_code_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.action_code_list is not None:
            result['ActionCodeList'] = self.action_code_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('ActionCodeList') is not None:
            self.action_code_list = m.get('ActionCodeList')
        return self


class QueryTicketActionsResponseBody(TeaModel):
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


class QueryTicketActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTicketActionsResponseBody = None,
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
            temp_model = QueryTicketActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferCallToAgentRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        account_name: str = None,
        target_account_name: str = None,
        call_id: str = None,
        job_id: str = None,
        connection_id: str = None,
        hold_connection_id: str = None,
        type: int = None,
        is_single_transfer: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.account_name = account_name
        self.target_account_name = target_account_name
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
        if self.target_account_name is not None:
            result['TargetAccountName'] = self.target_account_name
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
        if m.get('TargetAccountName') is not None:
            self.target_account_name = m.get('TargetAccountName')
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


class TransferCallToAgentResponseBody(TeaModel):
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


class TransferCallToAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferCallToAgentResponseBody = None,
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
            temp_model = TransferCallToAgentResponseBody()
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


class ExecuteActivityRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        ticket_id: int = None,
        operator_id: int = None,
        activity_code: str = None,
        activity_form: str = None,
    ):
        self.client_token = client_token
        self.instance_id = instance_id
        self.ticket_id = ticket_id
        self.operator_id = operator_id
        self.activity_code = activity_code
        self.activity_form = activity_form

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
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code
        if self.activity_form is not None:
            result['ActivityForm'] = self.activity_form
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')
        if m.get('ActivityForm') is not None:
            self.activity_form = m.get('ActivityForm')
        return self


class ExecuteActivityResponseBody(TeaModel):
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


class ExecuteActivityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteActivityResponseBody = None,
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
            temp_model = ExecuteActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGrantedRoleIdsRequest(TeaModel):
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


class GetGrantedRoleIdsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[int] = None,
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


class GetGrantedRoleIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGrantedRoleIdsResponseBody = None,
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
            temp_model = GetGrantedRoleIdsResponseBody()
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
        end_time: bool = None,
        start_time: bool = None,
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class CreateCustomerRequest(TeaModel):
    def __init__(
        self,
        prod_line_id: int = None,
        biz_type: str = None,
        name: str = None,
        type_code: str = None,
        phone: str = None,
        instance_id: str = None,
        manager_name: str = None,
        contacter: str = None,
        industry: str = None,
        position: str = None,
        email: str = None,
        dingding: str = None,
        outer_id: str = None,
        outer_id_type: int = None,
    ):
        self.prod_line_id = prod_line_id
        self.biz_type = biz_type
        self.name = name
        self.type_code = type_code
        self.phone = phone
        self.instance_id = instance_id
        self.manager_name = manager_name
        self.contacter = contacter
        self.industry = industry
        self.position = position
        self.email = email
        self.dingding = dingding
        self.outer_id = outer_id
        self.outer_id_type = outer_id_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prod_line_id is not None:
            result['ProdLineId'] = self.prod_line_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.name is not None:
            result['Name'] = self.name
        if self.type_code is not None:
            result['TypeCode'] = self.type_code
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.manager_name is not None:
            result['ManagerName'] = self.manager_name
        if self.contacter is not None:
            result['Contacter'] = self.contacter
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.position is not None:
            result['Position'] = self.position
        if self.email is not None:
            result['Email'] = self.email
        if self.dingding is not None:
            result['Dingding'] = self.dingding
        if self.outer_id is not None:
            result['OuterId'] = self.outer_id
        if self.outer_id_type is not None:
            result['OuterIdType'] = self.outer_id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProdLineId') is not None:
            self.prod_line_id = m.get('ProdLineId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TypeCode') is not None:
            self.type_code = m.get('TypeCode')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ManagerName') is not None:
            self.manager_name = m.get('ManagerName')
        if m.get('Contacter') is not None:
            self.contacter = m.get('Contacter')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Dingding') is not None:
            self.dingding = m.get('Dingding')
        if m.get('OuterId') is not None:
            self.outer_id = m.get('OuterId')
        if m.get('OuterIdType') is not None:
            self.outer_id_type = m.get('OuterIdType')
        return self


class CreateCustomerResponseBody(TeaModel):
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


class CreateCustomerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCustomerResponseBody = None,
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
            temp_model = CreateCustomerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


