# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class BusinessResultServiceRequest(TeaModel):
    def __init__(
        self,
        action_code: str = None,
        bussiness_code: str = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
        success: bool = None,
    ):
        self.action_code = action_code
        self.bussiness_code = bussiness_code
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BusinessResultServiceShrinkRequest(TeaModel):
    def __init__(
        self,
        action_code: str = None,
        bussiness_code: str = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        result_shrink: str = None,
        success: bool = None,
    ):
        self.action_code = action_code
        self.bussiness_code = bussiness_code
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.result_shrink = result_shrink
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_shrink is not None:
            result['Result'] = self.result_shrink
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result_shrink = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BusinessResultServiceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BusinessResultServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BusinessResultServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BusinessResultServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserInvestigationInfoQueryTaskRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        employee_id: str = None,
        end_time: int = None,
        oss_file_name: str = None,
        start_time: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.data_type = data_type
        # This parameter is required.
        self.employee_id = employee_id
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.oss_file_name = oss_file_name
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.employee_id is not None:
            result['employeeId'] = self.employee_id
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.oss_file_name is not None:
            result['ossFileName'] = self.oss_file_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('employeeId') is not None:
            self.employee_id = m.get('employeeId')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('ossFileName') is not None:
            self.oss_file_name = m.get('ossFileName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateUserInvestigationInfoQueryTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateUserInvestigationInfoQueryTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateUserInvestigationInfoQueryTaskResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateUserInvestigationInfoQueryTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateUserInvestigationInfoQueryTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserInvestigationInfoQueryTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateUserInvestigationInfoQueryTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindInstanceInfoRequest(TeaModel):
    def __init__(
        self,
        business_codes: str = None,
        bussiness_code: str = None,
        domain: str = None,
        end_time: int = None,
        extras: Dict[str, Any] = None,
        ip: str = None,
        need_dns: bool = None,
        start_time: int = None,
        url: str = None,
        user_id: str = None,
    ):
        self.business_codes = business_codes
        self.bussiness_code = bussiness_code
        self.domain = domain
        self.end_time = end_time
        self.extras = extras
        self.ip = ip
        self.need_dns = need_dns
        self.start_time = start_time
        self.url = url
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_codes is not None:
            result['businessCodes'] = self.business_codes
        if self.bussiness_code is not None:
            result['bussinessCode'] = self.bussiness_code
        if self.domain is not None:
            result['domain'] = self.domain
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.extras is not None:
            result['extras'] = self.extras
        if self.ip is not None:
            result['ip'] = self.ip
        if self.need_dns is not None:
            result['needDNS'] = self.need_dns
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.url is not None:
            result['url'] = self.url
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessCodes') is not None:
            self.business_codes = m.get('businessCodes')
        if m.get('bussinessCode') is not None:
            self.bussiness_code = m.get('bussinessCode')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('extras') is not None:
            self.extras = m.get('extras')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('needDNS') is not None:
            self.need_dns = m.get('needDNS')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class FindInstanceInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        business_codes: str = None,
        bussiness_code: str = None,
        domain: str = None,
        end_time: int = None,
        extras_shrink: str = None,
        ip: str = None,
        need_dns: bool = None,
        start_time: int = None,
        url: str = None,
        user_id: str = None,
    ):
        self.business_codes = business_codes
        self.bussiness_code = bussiness_code
        self.domain = domain
        self.end_time = end_time
        self.extras_shrink = extras_shrink
        self.ip = ip
        self.need_dns = need_dns
        self.start_time = start_time
        self.url = url
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_codes is not None:
            result['businessCodes'] = self.business_codes
        if self.bussiness_code is not None:
            result['bussinessCode'] = self.bussiness_code
        if self.domain is not None:
            result['domain'] = self.domain
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.extras_shrink is not None:
            result['extras'] = self.extras_shrink
        if self.ip is not None:
            result['ip'] = self.ip
        if self.need_dns is not None:
            result['needDNS'] = self.need_dns
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.url is not None:
            result['url'] = self.url
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessCodes') is not None:
            self.business_codes = m.get('businessCodes')
        if m.get('bussinessCode') is not None:
            self.bussiness_code = m.get('bussinessCode')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('extras') is not None:
            self.extras_shrink = m.get('extras')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('needDNS') is not None:
            self.need_dns = m.get('needDNS')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class FindInstanceInfoResponseBodyDataPegInstanceInfoListUserInfo(TeaModel):
    def __init__(
        self,
        gc_level: str = None,
        hit_white_reason: str = None,
        user_id: str = None,
        user_site: str = None,
        white_user: bool = None,
    ):
        self.gc_level = gc_level
        self.hit_white_reason = hit_white_reason
        self.user_id = user_id
        self.user_site = user_site
        self.white_user = white_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gc_level is not None:
            result['GcLevel'] = self.gc_level
        if self.hit_white_reason is not None:
            result['HitWhiteReason'] = self.hit_white_reason
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_site is not None:
            result['UserSite'] = self.user_site
        if self.white_user is not None:
            result['WhiteUser'] = self.white_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GcLevel') is not None:
            self.gc_level = m.get('GcLevel')
        if m.get('HitWhiteReason') is not None:
            self.hit_white_reason = m.get('HitWhiteReason')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSite') is not None:
            self.user_site = m.get('UserSite')
        if m.get('WhiteUser') is not None:
            self.white_user = m.get('WhiteUser')
        return self


class FindInstanceInfoResponseBodyDataPegInstanceInfoList(TeaModel):
    def __init__(
        self,
        bussiness_code: str = None,
        coordinate: Dict[str, Any] = None,
        id_type: str = None,
        instance_id: str = None,
        service_created_time: str = None,
        user_id: str = None,
        user_info: FindInstanceInfoResponseBodyDataPegInstanceInfoListUserInfo = None,
    ):
        self.bussiness_code = bussiness_code
        self.coordinate = coordinate
        self.id_type = id_type
        self.instance_id = instance_id
        self.service_created_time = service_created_time
        self.user_id = user_id
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.coordinate is not None:
            result['Coordinate'] = self.coordinate
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.service_created_time is not None:
            result['ServiceCreatedTime'] = self.service_created_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('Coordinate') is not None:
            self.coordinate = m.get('Coordinate')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServiceCreatedTime') is not None:
            self.service_created_time = m.get('ServiceCreatedTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserInfo') is not None:
            temp_model = FindInstanceInfoResponseBodyDataPegInstanceInfoListUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class FindInstanceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        peg_instance_info_list: List[FindInstanceInfoResponseBodyDataPegInstanceInfoList] = None,
    ):
        self.peg_instance_info_list = peg_instance_info_list

    def validate(self):
        if self.peg_instance_info_list:
            for k in self.peg_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PegInstanceInfoList'] = []
        if self.peg_instance_info_list is not None:
            for k in self.peg_instance_info_list:
                result['PegInstanceInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.peg_instance_info_list = []
        if m.get('PegInstanceInfoList') is not None:
            for k in m.get('PegInstanceInfoList'):
                temp_model = FindInstanceInfoResponseBodyDataPegInstanceInfoList()
                self.peg_instance_info_list.append(temp_model.from_map(k))
        return self


class FindInstanceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: FindInstanceInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = FindInstanceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FindInstanceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindInstanceInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FindInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindUserAvailbleResourcesRequest(TeaModel):
    def __init__(
        self,
        bussiness_code: str = None,
        curr_page: int = None,
        page_size: int = None,
        resource_type: str = None,
        user_id: str = None,
    ):
        self.bussiness_code = bussiness_code
        self.curr_page = curr_page
        self.page_size = page_size
        self.resource_type = resource_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bussiness_code is not None:
            result['bussinessCode'] = self.bussiness_code
        if self.curr_page is not None:
            result['currPage'] = self.curr_page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bussinessCode') is not None:
            self.bussiness_code = m.get('bussinessCode')
        if m.get('currPage') is not None:
            self.curr_page = m.get('currPage')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class FindUserAvailbleResourcesResponseBodyDataPegCoordinates(TeaModel):
    def __init__(
        self,
        bussiness_code: str = None,
        charge_type: str = None,
        coordinate: Dict[str, Any] = None,
        id_type: str = None,
        instance_id: str = None,
        region: str = None,
        release_time: str = None,
        res_create_time: str = None,
        resource_status: str = None,
        resource_type: str = None,
        service_created_time: str = None,
        user_id: str = None,
    ):
        self.bussiness_code = bussiness_code
        self.charge_type = charge_type
        self.coordinate = coordinate
        self.id_type = id_type
        self.instance_id = instance_id
        self.region = region
        self.release_time = release_time
        self.res_create_time = res_create_time
        self.resource_status = resource_status
        self.resource_type = resource_type
        self.service_created_time = service_created_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.coordinate is not None:
            result['Coordinate'] = self.coordinate
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region is not None:
            result['Region'] = self.region
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.res_create_time is not None:
            result['ResCreateTime'] = self.res_create_time
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_created_time is not None:
            result['ServiceCreatedTime'] = self.service_created_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Coordinate') is not None:
            self.coordinate = m.get('Coordinate')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('ResCreateTime') is not None:
            self.res_create_time = m.get('ResCreateTime')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceCreatedTime') is not None:
            self.service_created_time = m.get('ServiceCreatedTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class FindUserAvailbleResourcesResponseBodyDataUserInfo(TeaModel):
    def __init__(
        self,
        gc_level: str = None,
        hit_white_reason: str = None,
        user_id: str = None,
        user_site: str = None,
        white_user: bool = None,
    ):
        self.gc_level = gc_level
        self.hit_white_reason = hit_white_reason
        self.user_id = user_id
        self.user_site = user_site
        self.white_user = white_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gc_level is not None:
            result['GcLevel'] = self.gc_level
        if self.hit_white_reason is not None:
            result['HitWhiteReason'] = self.hit_white_reason
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_site is not None:
            result['UserSite'] = self.user_site
        if self.white_user is not None:
            result['WhiteUser'] = self.white_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GcLevel') is not None:
            self.gc_level = m.get('GcLevel')
        if m.get('HitWhiteReason') is not None:
            self.hit_white_reason = m.get('HitWhiteReason')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSite') is not None:
            self.user_site = m.get('UserSite')
        if m.get('WhiteUser') is not None:
            self.white_user = m.get('WhiteUser')
        return self


class FindUserAvailbleResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        peg_coordinates: List[FindUserAvailbleResourcesResponseBodyDataPegCoordinates] = None,
        user_info: FindUserAvailbleResourcesResponseBodyDataUserInfo = None,
    ):
        self.peg_coordinates = peg_coordinates
        self.user_info = user_info

    def validate(self):
        if self.peg_coordinates:
            for k in self.peg_coordinates:
                if k:
                    k.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PegCoordinates'] = []
        if self.peg_coordinates is not None:
            for k in self.peg_coordinates:
                result['PegCoordinates'].append(k.to_map() if k else None)
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.peg_coordinates = []
        if m.get('PegCoordinates') is not None:
            for k in m.get('PegCoordinates'):
                temp_model = FindUserAvailbleResourcesResponseBodyDataPegCoordinates()
                self.peg_coordinates.append(temp_model.from_map(k))
        if m.get('UserInfo') is not None:
            temp_model = FindUserAvailbleResourcesResponseBodyDataUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class FindUserAvailbleResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: FindUserAvailbleResourcesResponseBodyData = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.max_results = max_results
        self.message = message
        # This parameter is required.
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            temp_model = FindUserAvailbleResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class FindUserAvailbleResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindUserAvailbleResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FindUserAvailbleResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecurityEventDetailRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        event_id: str = None,
        caller_parent_id: int = None,
        caller_type: str = None,
        caller_uid: int = None,
    ):
        self.ali_uid = ali_uid
        self.event_id = event_id
        self.caller_parent_id = caller_parent_id
        self.caller_type = caller_type
        self.caller_uid = caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.caller_parent_id is not None:
            result['callerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['callerType'] = self.caller_type
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('callerParentId') is not None:
            self.caller_parent_id = m.get('callerParentId')
        if m.get('callerType') is not None:
            self.caller_type = m.get('callerType')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        return self


class GetSecurityEventDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        aliuid: str = None,
        data_source: str = None,
        event_code: str = None,
        event_id: str = None,
        event_time: str = None,
        extra: str = None,
        level: str = None,
        principal_id: str = None,
        resource_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.aliuid = aliuid
        self.data_source = data_source
        self.event_code = event_code
        self.event_id = event_id
        self.event_time = event_time
        self.extra = extra
        self.level = level
        self.principal_id = principal_id
        self.resource_id = resource_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.level is not None:
            result['Level'] = self.level
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSecurityEventDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSecurityEventDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSecurityEventDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSecurityEventDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSecurityEventDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetSecurityEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PunishResourceSearchRequest(TeaModel):
    def __init__(
        self,
        action_codes: List[str] = None,
        bussiness_codes: List[str] = None,
        class_: str = None,
        domain: str = None,
        end_date: int = None,
        instance_id: str = None,
        ip: str = None,
        page: int = None,
        page_size: int = None,
        source_codes: List[str] = None,
        start_date: int = None,
        status: str = None,
        url: str = None,
        user_ids: List[str] = None,
    ):
        self.action_codes = action_codes
        self.bussiness_codes = bussiness_codes
        self.class_ = class_
        self.domain = domain
        self.end_date = end_date
        self.instance_id = instance_id
        self.ip = ip
        self.page = page
        self.page_size = page_size
        self.source_codes = source_codes
        self.start_date = start_date
        self.status = status
        self.url = url
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_codes is not None:
            result['ActionCodes'] = self.action_codes
        if self.bussiness_codes is not None:
            result['BussinessCodes'] = self.bussiness_codes
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_codes is not None:
            result['SourceCodes'] = self.source_codes
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCodes') is not None:
            self.action_codes = m.get('ActionCodes')
        if m.get('BussinessCodes') is not None:
            self.bussiness_codes = m.get('BussinessCodes')
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceCodes') is not None:
            self.source_codes = m.get('SourceCodes')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class PunishResourceSearchShrinkRequest(TeaModel):
    def __init__(
        self,
        action_codes_shrink: str = None,
        bussiness_codes_shrink: str = None,
        class_: str = None,
        domain: str = None,
        end_date: int = None,
        instance_id: str = None,
        ip: str = None,
        page: int = None,
        page_size: int = None,
        source_codes_shrink: str = None,
        start_date: int = None,
        status: str = None,
        url: str = None,
        user_ids_shrink: str = None,
    ):
        self.action_codes_shrink = action_codes_shrink
        self.bussiness_codes_shrink = bussiness_codes_shrink
        self.class_ = class_
        self.domain = domain
        self.end_date = end_date
        self.instance_id = instance_id
        self.ip = ip
        self.page = page
        self.page_size = page_size
        self.source_codes_shrink = source_codes_shrink
        self.start_date = start_date
        self.status = status
        self.url = url
        self.user_ids_shrink = user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_codes_shrink is not None:
            result['ActionCodes'] = self.action_codes_shrink
        if self.bussiness_codes_shrink is not None:
            result['BussinessCodes'] = self.bussiness_codes_shrink
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_codes_shrink is not None:
            result['SourceCodes'] = self.source_codes_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        if self.user_ids_shrink is not None:
            result['UserIds'] = self.user_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCodes') is not None:
            self.action_codes_shrink = m.get('ActionCodes')
        if m.get('BussinessCodes') is not None:
            self.bussiness_codes_shrink = m.get('BussinessCodes')
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceCodes') is not None:
            self.source_codes_shrink = m.get('SourceCodes')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserIds') is not None:
            self.user_ids_shrink = m.get('UserIds')
        return self


class PunishResourceSearchResponseBodyDataList(TeaModel):
    def __init__(
        self,
        action_code: str = None,
        bussiness_code: str = None,
        class_: str = None,
        coordinate: str = None,
        creator: str = None,
        deleted: bool = None,
        domain: str = None,
        extras: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        ip: str = None,
        modifier: str = None,
        object_id: str = None,
        object_type: str = None,
        object_value: str = None,
        punish_from: str = None,
        reason: str = None,
        request_id: int = None,
        source_code: str = None,
        status: str = None,
        url: str = None,
        user_id: str = None,
    ):
        self.action_code = action_code
        self.bussiness_code = bussiness_code
        self.class_ = class_
        self.coordinate = coordinate
        self.creator = creator
        self.deleted = deleted
        self.domain = domain
        self.extras = extras
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.ip = ip
        self.modifier = modifier
        self.object_id = object_id
        self.object_type = object_type
        self.object_value = object_value
        self.punish_from = punish_from
        self.reason = reason
        self.request_id = request_id
        self.source_code = source_code
        self.status = status
        self.url = url
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.coordinate is not None:
            result['Coordinate'] = self.coordinate
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.extras is not None:
            result['Extras'] = self.extras
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.object_value is not None:
            result['ObjectValue'] = self.object_value
        if self.punish_from is not None:
            result['PunishFrom'] = self.punish_from
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('Coordinate') is not None:
            self.coordinate = m.get('Coordinate')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Extras') is not None:
            self.extras = m.get('Extras')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ObjectValue') is not None:
            self.object_value = m.get('ObjectValue')
        if m.get('PunishFrom') is not None:
            self.punish_from = m.get('PunishFrom')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class PunishResourceSearchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data_list: List[PunishResourceSearchResponseBodyDataList] = None,
        message: str = None,
        success: str = None,
        total_count: int = None,
        view_count: int = None,
    ):
        self.code = code
        self.data_list = data_list
        self.message = message
        self.success = success
        self.total_count = total_count
        self.view_count = view_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.view_count is not None:
            result['ViewCount'] = self.view_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = PunishResourceSearchResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')
        return self


class PunishResourceSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PunishResourceSearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PunishResourceSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordClickLinkActionRequest(TeaModel):
    def __init__(
        self,
        tag: str = None,
    ):
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class RecordClickLinkActionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecordClickLinkActionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecordClickLinkActionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RecordClickLinkActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RiskEventSyncRequest(TeaModel):
    def __init__(
        self,
        deleted: bool = None,
        discovery_time: int = None,
        event_name: str = None,
        event_number: str = None,
        relevance_bu: str = None,
        risk_detail: str = None,
        risk_effect_type: str = None,
        risk_level: str = None,
        risk_type: str = None,
        source: str = None,
        submitter: str = None,
    ):
        self.deleted = deleted
        # This parameter is required.
        self.discovery_time = discovery_time
        # This parameter is required.
        self.event_name = event_name
        self.event_number = event_number
        self.relevance_bu = relevance_bu
        # This parameter is required.
        self.risk_detail = risk_detail
        # This parameter is required.
        self.risk_effect_type = risk_effect_type
        self.risk_level = risk_level
        # This parameter is required.
        self.risk_type = risk_type
        # This parameter is required.
        self.source = source
        # This parameter is required.
        self.submitter = submitter

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.discovery_time is not None:
            result['DiscoveryTime'] = self.discovery_time
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.event_number is not None:
            result['EventNumber'] = self.event_number
        if self.relevance_bu is not None:
            result['RelevanceBu'] = self.relevance_bu
        if self.risk_detail is not None:
            result['RiskDetail'] = self.risk_detail
        if self.risk_effect_type is not None:
            result['RiskEffectType'] = self.risk_effect_type
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.risk_type is not None:
            result['RiskType'] = self.risk_type
        if self.source is not None:
            result['Source'] = self.source
        if self.submitter is not None:
            result['Submitter'] = self.submitter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('DiscoveryTime') is not None:
            self.discovery_time = m.get('DiscoveryTime')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('EventNumber') is not None:
            self.event_number = m.get('EventNumber')
        if m.get('RelevanceBu') is not None:
            self.relevance_bu = m.get('RelevanceBu')
        if m.get('RiskDetail') is not None:
            self.risk_detail = m.get('RiskDetail')
        if m.get('RiskEffectType') is not None:
            self.risk_effect_type = m.get('RiskEffectType')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Submitter') is not None:
            self.submitter = m.get('Submitter')
        return self


class RiskEventSyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RiskEventSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RiskEventSyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RiskEventSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchPunishEventsRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        bussiness_codes: List[str] = None,
        case_codes: List[str] = None,
        event_codes: List[str] = None,
        resource_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        self.bussiness_codes = bussiness_codes
        self.case_codes = case_codes
        self.event_codes = event_codes
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bussiness_codes is not None:
            result['BussinessCodes'] = self.bussiness_codes
        if self.case_codes is not None:
            result['CaseCodes'] = self.case_codes
        if self.event_codes is not None:
            result['EventCodes'] = self.event_codes
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BussinessCodes') is not None:
            self.bussiness_codes = m.get('BussinessCodes')
        if m.get('CaseCodes') is not None:
            self.case_codes = m.get('CaseCodes')
        if m.get('EventCodes') is not None:
            self.event_codes = m.get('EventCodes')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class SearchPunishEventsShrinkRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        bussiness_codes_shrink: str = None,
        case_codes_shrink: str = None,
        event_codes_shrink: str = None,
        resource_id: str = None,
    ):
        # This parameter is required.
        self.ali_uid = ali_uid
        self.bussiness_codes_shrink = bussiness_codes_shrink
        self.case_codes_shrink = case_codes_shrink
        self.event_codes_shrink = event_codes_shrink
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bussiness_codes_shrink is not None:
            result['BussinessCodes'] = self.bussiness_codes_shrink
        if self.case_codes_shrink is not None:
            result['CaseCodes'] = self.case_codes_shrink
        if self.event_codes_shrink is not None:
            result['EventCodes'] = self.event_codes_shrink
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BussinessCodes') is not None:
            self.bussiness_codes_shrink = m.get('BussinessCodes')
        if m.get('CaseCodes') is not None:
            self.case_codes_shrink = m.get('CaseCodes')
        if m.get('EventCodes') is not None:
            self.event_codes_shrink = m.get('EventCodes')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class SearchPunishEventsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        bussiness_code: str = None,
        case_code: str = None,
        records_count: int = None,
        resource_id: str = None,
        tips_code: str = None,
        user_id: str = None,
    ):
        self.bussiness_code = bussiness_code
        self.case_code = case_code
        self.records_count = records_count
        self.resource_id = resource_id
        self.tips_code = tips_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.case_code is not None:
            result['CaseCode'] = self.case_code
        if self.records_count is not None:
            result['RecordsCount'] = self.records_count
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tips_code is not None:
            result['TipsCode'] = self.tips_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('CaseCode') is not None:
            self.case_code = m.get('CaseCode')
        if m.get('RecordsCount') is not None:
            self.records_count = m.get('RecordsCount')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TipsCode') is not None:
            self.tips_code = m.get('TipsCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchPunishEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data_list: List[SearchPunishEventsResponseBodyDataList] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.data_list = data_list
        self.message = message
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = SearchPunishEventsResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchPunishEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchPunishEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SearchPunishEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchPunishRecordsRequest(TeaModel):
    def __init__(
        self,
        action_codes: List[str] = None,
        ali_uid: str = None,
        bussiness_codes: str = None,
        case_codes: List[str] = None,
        domain: str = None,
        end_time: int = None,
        event_codes: List[str] = None,
        ip: str = None,
        page: str = None,
        page_size: str = None,
        punish_status: List[str] = None,
        resource_id: str = None,
        source_codes: List[str] = None,
        start_time: int = None,
        url: str = None,
        url_fuzzy: str = None,
    ):
        self.action_codes = action_codes
        # This parameter is required.
        self.ali_uid = ali_uid
        self.bussiness_codes = bussiness_codes
        self.case_codes = case_codes
        self.domain = domain
        self.end_time = end_time
        self.event_codes = event_codes
        self.ip = ip
        self.page = page
        self.page_size = page_size
        self.punish_status = punish_status
        self.resource_id = resource_id
        self.source_codes = source_codes
        self.start_time = start_time
        self.url = url
        self.url_fuzzy = url_fuzzy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_codes is not None:
            result['ActionCodes'] = self.action_codes
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bussiness_codes is not None:
            result['BussinessCodes'] = self.bussiness_codes
        if self.case_codes is not None:
            result['CaseCodes'] = self.case_codes
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_codes is not None:
            result['EventCodes'] = self.event_codes
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source_codes is not None:
            result['SourceCodes'] = self.source_codes
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.url is not None:
            result['Url'] = self.url
        if self.url_fuzzy is not None:
            result['UrlFuzzy'] = self.url_fuzzy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCodes') is not None:
            self.action_codes = m.get('ActionCodes')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BussinessCodes') is not None:
            self.bussiness_codes = m.get('BussinessCodes')
        if m.get('CaseCodes') is not None:
            self.case_codes = m.get('CaseCodes')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventCodes') is not None:
            self.event_codes = m.get('EventCodes')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('SourceCodes') is not None:
            self.source_codes = m.get('SourceCodes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlFuzzy') is not None:
            self.url_fuzzy = m.get('UrlFuzzy')
        return self


class SearchPunishRecordsShrinkRequest(TeaModel):
    def __init__(
        self,
        action_codes_shrink: str = None,
        ali_uid: str = None,
        bussiness_codes: str = None,
        case_codes_shrink: str = None,
        domain: str = None,
        end_time: int = None,
        event_codes_shrink: str = None,
        ip: str = None,
        page: str = None,
        page_size: str = None,
        punish_status_shrink: str = None,
        resource_id: str = None,
        source_codes_shrink: str = None,
        start_time: int = None,
        url: str = None,
        url_fuzzy: str = None,
    ):
        self.action_codes_shrink = action_codes_shrink
        # This parameter is required.
        self.ali_uid = ali_uid
        self.bussiness_codes = bussiness_codes
        self.case_codes_shrink = case_codes_shrink
        self.domain = domain
        self.end_time = end_time
        self.event_codes_shrink = event_codes_shrink
        self.ip = ip
        self.page = page
        self.page_size = page_size
        self.punish_status_shrink = punish_status_shrink
        self.resource_id = resource_id
        self.source_codes_shrink = source_codes_shrink
        self.start_time = start_time
        self.url = url
        self.url_fuzzy = url_fuzzy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_codes_shrink is not None:
            result['ActionCodes'] = self.action_codes_shrink
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.bussiness_codes is not None:
            result['BussinessCodes'] = self.bussiness_codes
        if self.case_codes_shrink is not None:
            result['CaseCodes'] = self.case_codes_shrink
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_codes_shrink is not None:
            result['EventCodes'] = self.event_codes_shrink
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.punish_status_shrink is not None:
            result['PunishStatus'] = self.punish_status_shrink
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.source_codes_shrink is not None:
            result['SourceCodes'] = self.source_codes_shrink
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.url is not None:
            result['Url'] = self.url
        if self.url_fuzzy is not None:
            result['UrlFuzzy'] = self.url_fuzzy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCodes') is not None:
            self.action_codes_shrink = m.get('ActionCodes')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('BussinessCodes') is not None:
            self.bussiness_codes = m.get('BussinessCodes')
        if m.get('CaseCodes') is not None:
            self.case_codes_shrink = m.get('CaseCodes')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventCodes') is not None:
            self.event_codes_shrink = m.get('EventCodes')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PunishStatus') is not None:
            self.punish_status_shrink = m.get('PunishStatus')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('SourceCodes') is not None:
            self.source_codes_shrink = m.get('SourceCodes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UrlFuzzy') is not None:
            self.url_fuzzy = m.get('UrlFuzzy')
        return self


class SearchPunishRecordsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        action_code: str = None,
        anti_status: str = None,
        bussiness_code: str = None,
        case_code: str = None,
        create_time: str = None,
        domain: str = None,
        event_code: str = None,
        ip: str = None,
        punish_status: str = None,
        reason: str = None,
        resource_id: str = None,
        tips_code: str = None,
        url: str = None,
    ):
        self.action_code = action_code
        self.anti_status = anti_status
        self.bussiness_code = bussiness_code
        self.case_code = case_code
        self.create_time = create_time
        self.domain = domain
        self.event_code = event_code
        self.ip = ip
        self.punish_status = punish_status
        self.reason = reason
        self.resource_id = resource_id
        self.tips_code = tips_code
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.anti_status is not None:
            result['AntiStatus'] = self.anti_status
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.case_code is not None:
            result['CaseCode'] = self.case_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tips_code is not None:
            result['TipsCode'] = self.tips_code
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('AntiStatus') is not None:
            self.anti_status = m.get('AntiStatus')
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('CaseCode') is not None:
            self.case_code = m.get('CaseCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TipsCode') is not None:
            self.tips_code = m.get('TipsCode')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SearchPunishRecordsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data_list: List[SearchPunishRecordsResponseBodyDataList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data_list = data_list
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = SearchPunishRecordsResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchPunishRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchPunishRecordsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SearchPunishRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchPunishRequestRequest(TeaModel):
    def __init__(
        self,
        anti_statuses: List[str] = None,
        bussiness_codes: List[str] = None,
        class_: str = None,
        end_date: int = None,
        event_codes: List[str] = None,
        ext_request_id: str = None,
        id: int = None,
        id_type: str = None,
        instance_id: str = None,
        page: int = None,
        page_size: int = None,
        punish_domain: str = None,
        punish_ip: str = None,
        punish_statuses: List[str] = None,
        punish_url: str = None,
        punish_url_full: str = None,
        source_codes: List[str] = None,
        start_date: int = None,
        user_ids: List[str] = None,
    ):
        self.anti_statuses = anti_statuses
        self.bussiness_codes = bussiness_codes
        self.class_ = class_
        self.end_date = end_date
        self.event_codes = event_codes
        self.ext_request_id = ext_request_id
        self.id = id
        self.id_type = id_type
        self.instance_id = instance_id
        self.page = page
        self.page_size = page_size
        self.punish_domain = punish_domain
        self.punish_ip = punish_ip
        self.punish_statuses = punish_statuses
        self.punish_url = punish_url
        self.punish_url_full = punish_url_full
        self.source_codes = source_codes
        self.start_date = start_date
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_statuses is not None:
            result['AntiStatuses'] = self.anti_statuses
        if self.bussiness_codes is not None:
            result['BussinessCodes'] = self.bussiness_codes
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.event_codes is not None:
            result['EventCodes'] = self.event_codes
        if self.ext_request_id is not None:
            result['ExtRequestId'] = self.ext_request_id
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.punish_domain is not None:
            result['PunishDomain'] = self.punish_domain
        if self.punish_ip is not None:
            result['PunishIp'] = self.punish_ip
        if self.punish_statuses is not None:
            result['PunishStatuses'] = self.punish_statuses
        if self.punish_url is not None:
            result['PunishUrl'] = self.punish_url
        if self.punish_url_full is not None:
            result['PunishUrlFull'] = self.punish_url_full
        if self.source_codes is not None:
            result['SourceCodes'] = self.source_codes
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiStatuses') is not None:
            self.anti_statuses = m.get('AntiStatuses')
        if m.get('BussinessCodes') is not None:
            self.bussiness_codes = m.get('BussinessCodes')
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('EventCodes') is not None:
            self.event_codes = m.get('EventCodes')
        if m.get('ExtRequestId') is not None:
            self.ext_request_id = m.get('ExtRequestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PunishDomain') is not None:
            self.punish_domain = m.get('PunishDomain')
        if m.get('PunishIp') is not None:
            self.punish_ip = m.get('PunishIp')
        if m.get('PunishStatuses') is not None:
            self.punish_statuses = m.get('PunishStatuses')
        if m.get('PunishUrl') is not None:
            self.punish_url = m.get('PunishUrl')
        if m.get('PunishUrlFull') is not None:
            self.punish_url_full = m.get('PunishUrlFull')
        if m.get('SourceCodes') is not None:
            self.source_codes = m.get('SourceCodes')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class SearchPunishRequestShrinkRequest(TeaModel):
    def __init__(
        self,
        anti_statuses_shrink: str = None,
        bussiness_codes_shrink: str = None,
        class_: str = None,
        end_date: int = None,
        event_codes_shrink: str = None,
        ext_request_id: str = None,
        id: int = None,
        id_type: str = None,
        instance_id: str = None,
        page: int = None,
        page_size: int = None,
        punish_domain: str = None,
        punish_ip: str = None,
        punish_statuses_shrink: str = None,
        punish_url: str = None,
        punish_url_full: str = None,
        source_codes_shrink: str = None,
        start_date: int = None,
        user_ids_shrink: str = None,
    ):
        self.anti_statuses_shrink = anti_statuses_shrink
        self.bussiness_codes_shrink = bussiness_codes_shrink
        self.class_ = class_
        self.end_date = end_date
        self.event_codes_shrink = event_codes_shrink
        self.ext_request_id = ext_request_id
        self.id = id
        self.id_type = id_type
        self.instance_id = instance_id
        self.page = page
        self.page_size = page_size
        self.punish_domain = punish_domain
        self.punish_ip = punish_ip
        self.punish_statuses_shrink = punish_statuses_shrink
        self.punish_url = punish_url
        self.punish_url_full = punish_url_full
        self.source_codes_shrink = source_codes_shrink
        self.start_date = start_date
        self.user_ids_shrink = user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_statuses_shrink is not None:
            result['AntiStatuses'] = self.anti_statuses_shrink
        if self.bussiness_codes_shrink is not None:
            result['BussinessCodes'] = self.bussiness_codes_shrink
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.event_codes_shrink is not None:
            result['EventCodes'] = self.event_codes_shrink
        if self.ext_request_id is not None:
            result['ExtRequestId'] = self.ext_request_id
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.punish_domain is not None:
            result['PunishDomain'] = self.punish_domain
        if self.punish_ip is not None:
            result['PunishIp'] = self.punish_ip
        if self.punish_statuses_shrink is not None:
            result['PunishStatuses'] = self.punish_statuses_shrink
        if self.punish_url is not None:
            result['PunishUrl'] = self.punish_url
        if self.punish_url_full is not None:
            result['PunishUrlFull'] = self.punish_url_full
        if self.source_codes_shrink is not None:
            result['SourceCodes'] = self.source_codes_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.user_ids_shrink is not None:
            result['UserIds'] = self.user_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiStatuses') is not None:
            self.anti_statuses_shrink = m.get('AntiStatuses')
        if m.get('BussinessCodes') is not None:
            self.bussiness_codes_shrink = m.get('BussinessCodes')
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('EventCodes') is not None:
            self.event_codes_shrink = m.get('EventCodes')
        if m.get('ExtRequestId') is not None:
            self.ext_request_id = m.get('ExtRequestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PunishDomain') is not None:
            self.punish_domain = m.get('PunishDomain')
        if m.get('PunishIp') is not None:
            self.punish_ip = m.get('PunishIp')
        if m.get('PunishStatuses') is not None:
            self.punish_statuses_shrink = m.get('PunishStatuses')
        if m.get('PunishUrl') is not None:
            self.punish_url = m.get('PunishUrl')
        if m.get('PunishUrlFull') is not None:
            self.punish_url_full = m.get('PunishUrlFull')
        if m.get('SourceCodes') is not None:
            self.source_codes_shrink = m.get('SourceCodes')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('UserIds') is not None:
            self.user_ids_shrink = m.get('UserIds')
        return self


class SearchPunishRequestResponseBodyDataList(TeaModel):
    def __init__(
        self,
        anti_punish_resp_time: str = None,
        anti_punish_time: str = None,
        anti_result: str = None,
        anti_status: str = None,
        bussiness_code: str = None,
        case_code: str = None,
        case_extend_code: str = None,
        case_sub_code: str = None,
        class_: str = None,
        creator: str = None,
        deleted: bool = None,
        event_code: str = None,
        expected_remove_time: str = None,
        ext_request_id: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        id_type: str = None,
        instance_id: str = None,
        ip_string: str = None,
        modifier: str = None,
        operator: str = None,
        operator_num: str = None,
        punish_domain: str = None,
        punish_ip: str = None,
        punish_officer: str = None,
        punish_officer_num: str = None,
        punish_request: str = None,
        punish_resp_time: str = None,
        punish_result: str = None,
        punish_status: str = None,
        punish_time: str = None,
        punish_url: str = None,
        reason: str = None,
        source_code: str = None,
        user_id: str = None,
    ):
        self.anti_punish_resp_time = anti_punish_resp_time
        self.anti_punish_time = anti_punish_time
        self.anti_result = anti_result
        self.anti_status = anti_status
        self.bussiness_code = bussiness_code
        self.case_code = case_code
        self.case_extend_code = case_extend_code
        self.case_sub_code = case_sub_code
        self.class_ = class_
        self.creator = creator
        self.deleted = deleted
        self.event_code = event_code
        self.expected_remove_time = expected_remove_time
        self.ext_request_id = ext_request_id
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.id_type = id_type
        self.instance_id = instance_id
        self.ip_string = ip_string
        self.modifier = modifier
        self.operator = operator
        self.operator_num = operator_num
        self.punish_domain = punish_domain
        self.punish_ip = punish_ip
        self.punish_officer = punish_officer
        self.punish_officer_num = punish_officer_num
        self.punish_request = punish_request
        self.punish_resp_time = punish_resp_time
        self.punish_result = punish_result
        self.punish_status = punish_status
        self.punish_time = punish_time
        self.punish_url = punish_url
        self.reason = reason
        self.source_code = source_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anti_punish_resp_time is not None:
            result['AntiPunishRespTime'] = self.anti_punish_resp_time
        if self.anti_punish_time is not None:
            result['AntiPunishTime'] = self.anti_punish_time
        if self.anti_result is not None:
            result['AntiResult'] = self.anti_result
        if self.anti_status is not None:
            result['AntiStatus'] = self.anti_status
        if self.bussiness_code is not None:
            result['BussinessCode'] = self.bussiness_code
        if self.case_code is not None:
            result['CaseCode'] = self.case_code
        if self.case_extend_code is not None:
            result['CaseExtendCode'] = self.case_extend_code
        if self.case_sub_code is not None:
            result['CaseSubCode'] = self.case_sub_code
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.expected_remove_time is not None:
            result['ExpectedRemoveTime'] = self.expected_remove_time
        if self.ext_request_id is not None:
            result['ExtRequestId'] = self.ext_request_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_string is not None:
            result['IpString'] = self.ip_string
        if self.modifier is not None:
            result['Modifier'] = self.modifier
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.operator_num is not None:
            result['OperatorNum'] = self.operator_num
        if self.punish_domain is not None:
            result['PunishDomain'] = self.punish_domain
        if self.punish_ip is not None:
            result['PunishIp'] = self.punish_ip
        if self.punish_officer is not None:
            result['PunishOfficer'] = self.punish_officer
        if self.punish_officer_num is not None:
            result['PunishOfficerNum'] = self.punish_officer_num
        if self.punish_request is not None:
            result['PunishRequest'] = self.punish_request
        if self.punish_resp_time is not None:
            result['PunishRespTime'] = self.punish_resp_time
        if self.punish_result is not None:
            result['PunishResult'] = self.punish_result
        if self.punish_status is not None:
            result['PunishStatus'] = self.punish_status
        if self.punish_time is not None:
            result['PunishTime'] = self.punish_time
        if self.punish_url is not None:
            result['PunishUrl'] = self.punish_url
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AntiPunishRespTime') is not None:
            self.anti_punish_resp_time = m.get('AntiPunishRespTime')
        if m.get('AntiPunishTime') is not None:
            self.anti_punish_time = m.get('AntiPunishTime')
        if m.get('AntiResult') is not None:
            self.anti_result = m.get('AntiResult')
        if m.get('AntiStatus') is not None:
            self.anti_status = m.get('AntiStatus')
        if m.get('BussinessCode') is not None:
            self.bussiness_code = m.get('BussinessCode')
        if m.get('CaseCode') is not None:
            self.case_code = m.get('CaseCode')
        if m.get('CaseExtendCode') is not None:
            self.case_extend_code = m.get('CaseExtendCode')
        if m.get('CaseSubCode') is not None:
            self.case_sub_code = m.get('CaseSubCode')
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('ExpectedRemoveTime') is not None:
            self.expected_remove_time = m.get('ExpectedRemoveTime')
        if m.get('ExtRequestId') is not None:
            self.ext_request_id = m.get('ExtRequestId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpString') is not None:
            self.ip_string = m.get('IpString')
        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OperatorNum') is not None:
            self.operator_num = m.get('OperatorNum')
        if m.get('PunishDomain') is not None:
            self.punish_domain = m.get('PunishDomain')
        if m.get('PunishIp') is not None:
            self.punish_ip = m.get('PunishIp')
        if m.get('PunishOfficer') is not None:
            self.punish_officer = m.get('PunishOfficer')
        if m.get('PunishOfficerNum') is not None:
            self.punish_officer_num = m.get('PunishOfficerNum')
        if m.get('PunishRequest') is not None:
            self.punish_request = m.get('PunishRequest')
        if m.get('PunishRespTime') is not None:
            self.punish_resp_time = m.get('PunishRespTime')
        if m.get('PunishResult') is not None:
            self.punish_result = m.get('PunishResult')
        if m.get('PunishStatus') is not None:
            self.punish_status = m.get('PunishStatus')
        if m.get('PunishTime') is not None:
            self.punish_time = m.get('PunishTime')
        if m.get('PunishUrl') is not None:
            self.punish_url = m.get('PunishUrl')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchPunishRequestResponseBody(TeaModel):
    def __init__(
        self,
        class_: str = None,
        code: str = None,
        count: int = None,
        data_list: List[SearchPunishRequestResponseBodyDataList] = None,
        message: str = None,
        success: bool = None,
        total_count: int = None,
        view_count: int = None,
    ):
        self.class_ = class_
        self.code = code
        self.count = count
        self.data_list = data_list
        self.message = message
        self.success = success
        self.total_count = total_count
        self.view_count = view_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.view_count is not None:
            result['ViewCount'] = self.view_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = SearchPunishRequestResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')
        return self


class SearchPunishRequestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchPunishRequestResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SearchPunishRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecurityEventStatusRequest(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        event_id: str = None,
        status: str = None,
        caller_parent_id: int = None,
        caller_type: str = None,
        caller_uid: int = None,
    ):
        self.ali_uid = ali_uid
        self.event_id = event_id
        self.status = status
        self.caller_parent_id = caller_parent_id
        self.caller_type = caller_type
        self.caller_uid = caller_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.status is not None:
            result['Status'] = self.status
        if self.caller_parent_id is not None:
            result['callerParentId'] = self.caller_parent_id
        if self.caller_type is not None:
            result['callerType'] = self.caller_type
        if self.caller_uid is not None:
            result['callerUid'] = self.caller_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('callerParentId') is not None:
            self.caller_parent_id = m.get('callerParentId')
        if m.get('callerType') is not None:
            self.caller_type = m.get('callerType')
        if m.get('callerUid') is not None:
            self.caller_uid = m.get('callerUid')
        return self


class UpdateSecurityEventStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSecurityEventStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSecurityEventStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateSecurityEventStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


