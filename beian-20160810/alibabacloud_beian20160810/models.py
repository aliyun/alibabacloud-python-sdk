# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DeleteUnbeianIpCheckTypeRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        check_type: int = None,
        ip: str = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.check_type = check_type
        # This parameter is required.
        self.ip = ip
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class DeleteUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO(TeaModel):
    def __init__(
        self,
        msg: str = None,
        success: bool = None,
    ):
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUnbeianIpCheckTypeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        huntress_ip_check_type_result_do: DeleteUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.huntress_ip_check_type_result_do = huntress_ip_check_type_result_do
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.huntress_ip_check_type_result_do:
            self.huntress_ip_check_type_result_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.huntress_ip_check_type_result_do is not None:
            result['HuntressIpCheckTypeResultDO'] = self.huntress_ip_check_type_result_do.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HuntressIpCheckTypeResultDO') is not None:
            temp_model = DeleteUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO()
            self.huntress_ip_check_type_result_do = temp_model.from_map(m['HuntressIpCheckTypeResultDO'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUnbeianIpCheckTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUnbeianIpCheckTypeResponseBody = None,
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
            temp_model = DeleteUnbeianIpCheckTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMainDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetMainDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return self


class GetMainDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMainDomainResponseBody = None,
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
            temp_model = GetMainDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertUnbeianIpCheckTypeRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        check_type: int = None,
        ip: str = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.check_type = check_type
        # This parameter is required.
        self.ip = ip
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class InsertUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO(TeaModel):
    def __init__(
        self,
        msg: str = None,
        success: bool = None,
    ):
        self.msg = msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertUnbeianIpCheckTypeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        huntress_ip_check_type_result_do: InsertUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.huntress_ip_check_type_result_do = huntress_ip_check_type_result_do
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.huntress_ip_check_type_result_do:
            self.huntress_ip_check_type_result_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.huntress_ip_check_type_result_do is not None:
            result['HuntressIpCheckTypeResultDO'] = self.huntress_ip_check_type_result_do.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HuntressIpCheckTypeResultDO') is not None:
            temp_model = InsertUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO()
            self.huntress_ip_check_type_result_do = temp_model.from_map(m['HuntressIpCheckTypeResultDO'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertUnbeianIpCheckTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertUnbeianIpCheckTypeResponseBody = None,
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
            temp_model = InsertUnbeianIpCheckTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUnbeianIpCheckTypeRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        check_type: int = None,
        ip: str = None,
        limit: int = None,
        page: int = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        self.check_type = check_type
        self.ip = ip
        self.limit = limit
        self.page = page
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.page is not None:
            result['Page'] = self.page
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ListUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDOList(TeaModel):
    def __init__(
        self,
        aliuid: int = None,
        caller: str = None,
        check_type: int = None,
        ip: str = None,
        remark: str = None,
    ):
        self.aliuid = aliuid
        self.caller = caller
        self.check_type = check_type
        self.ip = ip
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ListUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO(TeaModel):
    def __init__(
        self,
        list: List[ListUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDOList] = None,
        msg: str = None,
        success: bool = None,
    ):
        self.list = list
        self.msg = msg
        self.success = success

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
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDOList()
                self.list.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUnbeianIpCheckTypeResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_message: str = None,
        huntress_ip_check_type_result_do: ListUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.huntress_ip_check_type_result_do = huntress_ip_check_type_result_do
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.huntress_ip_check_type_result_do:
            self.huntress_ip_check_type_result_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.huntress_ip_check_type_result_do is not None:
            result['HuntressIpCheckTypeResultDO'] = self.huntress_ip_check_type_result_do.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HuntressIpCheckTypeResultDO') is not None:
            temp_model = ListUnbeianIpCheckTypeResponseBodyHuntressIpCheckTypeResultDO()
            self.huntress_ip_check_type_result_do = temp_model.from_map(m['HuntressIpCheckTypeResultDO'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUnbeianIpCheckTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUnbeianIpCheckTypeResponseBody = None,
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
            temp_model = ListUnbeianIpCheckTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManageAccessorDomainRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
        operation: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class ManageAccessorDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ManageAccessorDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ManageAccessorDomainResponseBody = None,
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
            temp_model = ManageAccessorDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManageAccessorDomainWhiteListRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domains: List[str] = None,
        end_time: str = None,
        operation: str = None,
        remark: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.domains = domains
        self.end_time = end_time
        # This parameter is required.
        self.operation = operation
        self.remark = remark
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ManageAccessorDomainWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ManageAccessorDomainWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ManageAccessorDomainWhiteListResponseBody = None,
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
            temp_model = ManageAccessorDomainWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ManageAccessorIpRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        ip: str = None,
        ip_version: int = None,
        operation: str = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.ip = ip
        # This parameter is required.
        self.ip_version = ip_version
        # This parameter is required.
        self.operation = operation
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class ManageAccessorIpResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ManageAccessorIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ManageAccessorIpResponseBody = None,
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
            temp_model = ManageAccessorIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccessorDomainRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class QueryAccessorDomainResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return self


class QueryAccessorDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAccessorDomainResponseBody = None,
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
            temp_model = QueryAccessorDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccessorDomainListRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryAccessorDomainListResponseBodyData(TeaModel):
    def __init__(
        self,
        domains: List[str] = None,
    ):
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class QueryAccessorDomainListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryAccessorDomainListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryAccessorDomainListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAccessorDomainListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAccessorDomainListResponseBody = None,
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
            temp_model = QueryAccessorDomainListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccessorDomainStatusRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class QueryAccessorDomainStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        reason: str = None,
        reason_code: int = None,
        status: str = None,
    ):
        self.domain = domain
        self.reason = reason
        self.reason_code = reason_code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryAccessorDomainStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryAccessorDomainStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryAccessorDomainStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAccessorDomainStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAccessorDomainStatusResponseBody = None,
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
            temp_model = QueryAccessorDomainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccessorDomainWhiteListRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domain: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class QueryAccessorDomainWhiteListResponseBodyDataItems(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        end_time: str = None,
        start_time: str = None,
        type: str = None,
        valid: bool = None,
    ):
        self.create_time = create_time
        self.end_time = end_time
        self.start_time = start_time
        self.type = type
        self.valid = valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class QueryAccessorDomainWhiteListResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[QueryAccessorDomainWhiteListResponseBodyDataItems] = None,
        white: bool = None,
    ):
        self.items = items
        self.white = white

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.white is not None:
            result['White'] = self.white
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QueryAccessorDomainWhiteListResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('White') is not None:
            self.white = m.get('White')
        return self


class QueryAccessorDomainWhiteListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryAccessorDomainWhiteListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryAccessorDomainWhiteListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAccessorDomainWhiteListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAccessorDomainWhiteListResponseBody = None,
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
            temp_model = QueryAccessorDomainWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccessorDomainsStatusRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        domains: List[str] = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.domains is not None:
            result['Domains'] = self.domains
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        return self


class QueryAccessorDomainsStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        domain: str = None,
        reason: str = None,
        reason_code: int = None,
        status: str = None,
    ):
        self.domain = domain
        self.reason = reason
        self.reason_code = reason_code
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryAccessorDomainsStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[QueryAccessorDomainsStatusResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryAccessorDomainsStatusResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAccessorDomainsStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAccessorDomainsStatusResponseBody = None,
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
            temp_model = QueryAccessorDomainsStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccessorIpRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        ip: str = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class QueryAccessorIpResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        return self


class QueryAccessorIpResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAccessorIpResponseBody = None,
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
            temp_model = QueryAccessorIpResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAccessorFullDomainsOssListRequest(TeaModel):
    def __init__(
        self,
        caller: str = None,
        oss_list: List[str] = None,
    ):
        # This parameter is required.
        self.caller = caller
        # This parameter is required.
        self.oss_list = oss_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.oss_list is not None:
            result['OssList'] = self.oss_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('OssList') is not None:
            self.oss_list = m.get('OssList')
        return self


class SubmitAccessorFullDomainsOssListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitAccessorFullDomainsOssListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitAccessorFullDomainsOssListResponseBody = None,
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
            temp_model = SubmitAccessorFullDomainsOssListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


