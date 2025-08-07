# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DelMessageRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        client_source: str = None,
        cookies: str = None,
        msg_id: str = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.client_source = client_source
        self.cookies = cookies
        self.msg_id = msg_id
        self.src_url = src_url
        self.tenant_code = tenant_code
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class DelMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class DelMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DelMessageResponseBody = None,
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
            temp_model = DelMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAllMessageRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        class_id: int = None,
        client_source: str = None,
        cookies: str = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.class_id = class_id
        self.client_source = client_source
        self.cookies = cookies
        self.src_url = src_url
        self.tenant_code = tenant_code
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class DeleteAllMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class DeleteAllMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAllMessageResponseBody = None,
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
            temp_model = DeleteAllMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadAllMessageRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        class_id: int = None,
        client_source: str = None,
        cookies: str = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.class_id = class_id
        self.client_source = client_source
        self.cookies = cookies
        self.src_url = src_url
        self.tenant_code = tenant_code
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class ReadAllMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class ReadAllMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadAllMessageResponseBody = None,
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
            temp_model = ReadAllMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadClassNameRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        client_source: str = None,
        cookies: str = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.client_source = client_source
        self.cookies = cookies
        self.src_url = src_url
        self.tenant_code = tenant_code
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class ReadClassNameResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ReadClassNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ReadClassNameResponseBodyData] = None,
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ReadClassNameResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReadClassNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadClassNameResponseBody = None,
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
            temp_model = ReadClassNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadMessageRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        client_source: str = None,
        cookies: str = None,
        msg_id: str = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.client_source = client_source
        self.cookies = cookies
        self.msg_id = msg_id
        self.src_url = src_url
        self.tenant_code = tenant_code
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class ReadMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class ReadMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadMessageResponseBody = None,
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
            temp_model = ReadMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadMessageContentRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        class_id: int = None,
        client_source: str = None,
        cookies: str = None,
        msg_id: str = None,
        src_url: str = None,
        status: int = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.class_id = class_id
        self.client_source = client_source
        self.cookies = cookies
        self.msg_id = msg_id
        self.src_url = src_url
        self.status = status
        self.tenant_code = tenant_code
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class ReadMessageContentResponseBodyDataDatasItem(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        class_id: int = None,
        content: str = None,
        deleted: int = None,
        gmt_created: int = None,
        gmt_update: int = None,
        mass_id: int = None,
        memo: str = None,
        msg_id: int = None,
        status: int = None,
        title: str = None,
    ):
        self.category_name = category_name
        self.class_id = class_id
        self.content = content
        self.deleted = deleted
        self.gmt_created = gmt_created
        self.gmt_update = gmt_update
        self.mass_id = mass_id
        self.memo = memo
        self.msg_id = msg_id
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.content is not None:
            result['Content'] = self.content
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_update is not None:
            result['GmtUpdate'] = self.gmt_update
        if self.mass_id is not None:
            result['MassId'] = self.mass_id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtUpdate') is not None:
            self.gmt_update = m.get('GmtUpdate')
        if m.get('MassId') is not None:
            self.mass_id = m.get('MassId')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ReadMessageContentResponseBodyDataDatasLastItem(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        class_id: int = None,
        content: str = None,
        deleted: int = None,
        gmt_created: int = None,
        gmt_update: int = None,
        mass_id: int = None,
        memo: str = None,
        msg_id: int = None,
        status: int = None,
        title: str = None,
    ):
        self.category_name = category_name
        self.class_id = class_id
        self.content = content
        self.deleted = deleted
        self.gmt_created = gmt_created
        self.gmt_update = gmt_update
        self.mass_id = mass_id
        self.memo = memo
        self.msg_id = msg_id
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.content is not None:
            result['Content'] = self.content
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_update is not None:
            result['GmtUpdate'] = self.gmt_update
        if self.mass_id is not None:
            result['MassId'] = self.mass_id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtUpdate') is not None:
            self.gmt_update = m.get('GmtUpdate')
        if m.get('MassId') is not None:
            self.mass_id = m.get('MassId')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ReadMessageContentResponseBodyDataDatasNextItem(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        class_id: int = None,
        content: str = None,
        deleted: int = None,
        gmt_created: int = None,
        gmt_update: int = None,
        mass_id: int = None,
        memo: str = None,
        msg_id: int = None,
        status: int = None,
        title: str = None,
    ):
        self.category_name = category_name
        self.class_id = class_id
        self.content = content
        self.deleted = deleted
        self.gmt_created = gmt_created
        self.gmt_update = gmt_update
        self.mass_id = mass_id
        self.memo = memo
        self.msg_id = msg_id
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.content is not None:
            result['Content'] = self.content
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_update is not None:
            result['GmtUpdate'] = self.gmt_update
        if self.mass_id is not None:
            result['MassId'] = self.mass_id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtUpdate') is not None:
            self.gmt_update = m.get('GmtUpdate')
        if m.get('MassId') is not None:
            self.mass_id = m.get('MassId')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ReadMessageContentResponseBodyDataDatas(TeaModel):
    def __init__(
        self,
        item: List[ReadMessageContentResponseBodyDataDatasItem] = None,
        last_item: List[ReadMessageContentResponseBodyDataDatasLastItem] = None,
        next_item: List[ReadMessageContentResponseBodyDataDatasNextItem] = None,
    ):
        self.item = item
        self.last_item = last_item
        self.next_item = next_item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()
        if self.last_item:
            for k in self.last_item:
                if k:
                    k.validate()
        if self.next_item:
            for k in self.next_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        result['LastItem'] = []
        if self.last_item is not None:
            for k in self.last_item:
                result['LastItem'].append(k.to_map() if k else None)
        result['NextItem'] = []
        if self.next_item is not None:
            for k in self.next_item:
                result['NextItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = ReadMessageContentResponseBodyDataDatasItem()
                self.item.append(temp_model.from_map(k))
        self.last_item = []
        if m.get('LastItem') is not None:
            for k in m.get('LastItem'):
                temp_model = ReadMessageContentResponseBodyDataDatasLastItem()
                self.last_item.append(temp_model.from_map(k))
        self.next_item = []
        if m.get('NextItem') is not None:
            for k in m.get('NextItem'):
                temp_model = ReadMessageContentResponseBodyDataDatasNextItem()
                self.next_item.append(temp_model.from_map(k))
        return self


class ReadMessageContentResponseBodyData(TeaModel):
    def __init__(
        self,
        datas: ReadMessageContentResponseBodyDataDatas = None,
    ):
        self.datas = datas

    def validate(self):
        if self.datas:
            self.datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datas is not None:
            result['Datas'] = self.datas.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Datas') is not None:
            temp_model = ReadMessageContentResponseBodyDataDatas()
            self.datas = temp_model.from_map(m['Datas'])
        return self


class ReadMessageContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReadMessageContentResponseBodyData = None,
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
            temp_model = ReadMessageContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReadMessageContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadMessageContentResponseBody = None,
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
            temp_model = ReadMessageContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadMessageListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        class_id: int = None,
        client_source: str = None,
        content: str = None,
        cookies: str = None,
        loc: str = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        src_url: str = None,
        status: int = None,
        tenant_code: str = None,
        title: str = None,
        uid_type: str = None,
    ):
        # 语言，默认为简体中文
        self.accept_language = accept_language
        # 系统参数，无需填写
        self.app_name = app_name
        # 系统参数，无需填写
        self.biz_name = biz_name
        # 系统参数，无需填写
        self.caller_protocol = caller_protocol
        # 消息类目ID
        self.class_id = class_id
        # 系统参数，无需填写
        self.client_source = client_source
        # 消息内容，用于模糊搜索
        self.content = content
        # 系统参数，无需填写
        self.cookies = cookies
        # 栏位 nav代表控制台topbar
        self.loc = loc
        # 系统参数，无需填写
        self.max_results = max_results
        # 系统参数，无需填写
        self.next_token = next_token
        # 分页查询页码
        self.page = page
        # 分页查询大小
        self.page_size = page_size
        # 系统参数，无需填写
        self.src_url = src_url
        # 消息状态，已读为1，未读为0
        self.status = status
        # 系统参数，无需填写
        self.tenant_code = tenant_code
        # 消息标题，用于模糊搜索
        self.title = title
        # 系统参数，无需填写
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.content is not None:
            result['Content'] = self.content
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.loc is not None:
            result['Loc'] = self.loc
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.title is not None:
            result['Title'] = self.title
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('Loc') is not None:
            self.loc = m.get('Loc')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class ReadMessageListResponseBodyDataRows(TeaModel):
    def __init__(
        self,
        category_name: str = None,
        class_: str = None,
        class_id: int = None,
        content: str = None,
        deleted: int = None,
        gmt_created: int = None,
        gmt_update: int = None,
        mass_id: int = None,
        memo: str = None,
        msg_id: int = None,
        status: int = None,
        title: str = None,
        titleh: str = None,
    ):
        # CategoryName
        self.category_name = category_name
        # Class
        self.class_ = class_
        # ClassId
        self.class_id = class_id
        # 内容
        self.content = content
        # 删除
        self.deleted = deleted
        # 创建时间
        self.gmt_created = gmt_created
        self.gmt_update = gmt_update
        # massId
        self.mass_id = mass_id
        # 描述
        self.memo = memo
        # 消息id
        self.msg_id = msg_id
        # 状态
        self.status = status
        # 标题
        self.title = title
        self.titleh = titleh

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.content is not None:
            result['Content'] = self.content
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_update is not None:
            result['GmtUpdate'] = self.gmt_update
        if self.mass_id is not None:
            result['MassId'] = self.mass_id
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        if self.titleh is not None:
            result['Titleh'] = self.titleh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtUpdate') is not None:
            self.gmt_update = m.get('GmtUpdate')
        if m.get('MassId') is not None:
            self.mass_id = m.get('MassId')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Titleh') is not None:
            self.titleh = m.get('Titleh')
        return self


class ReadMessageListResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        rows: List[ReadMessageListResponseBodyDataRows] = None,
    ):
        # The number of entries returned.
        self.count = count
        # The maximum number of entries returned.
        self.max_results = max_results
        # If excess return values exist, this parameter is returned.
        self.next_token = next_token
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The number of rows updated or returned on PolarDB-X 2.0 compute nodes.
        self.rows = rows

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['Rows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.rows = []
        if m.get('Rows') is not None:
            for k in m.get('Rows'):
                temp_model = ReadMessageListResponseBodyDataRows()
                self.rows.append(temp_model.from_map(k))
        return self


class ReadMessageListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ReadMessageListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The value Success indicates that the request is successful. Other values indicate that the request failed. For more information about error codes, see Error codes.
        self.code = code
        # Data
        self.data = data
        # message
        self.message = message
        # 唯一请求id
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**: The call was successful.
        # *   **false**: The call failed.
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
            temp_model = ReadMessageListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReadMessageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadMessageListResponseBody = None,
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
            temp_model = ReadMessageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadMessageNewTotalRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        client_source: str = None,
        cookies: str = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.client_source = client_source
        self.cookies = cookies
        self.src_url = src_url
        self.tenant_code = tenant_code
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class ReadMessageNewTotalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
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


class ReadMessageNewTotalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadMessageNewTotalResponseBody = None,
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
            temp_model = ReadMessageNewTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadNumGroupByClassRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        client_source: str = None,
        cookies: str = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.client_source = client_source
        self.cookies = cookies
        self.src_url = src_url
        self.tenant_code = tenant_code
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class ReadNumGroupByClassResponseBodyData(TeaModel):
    def __init__(
        self,
        class_id: int = None,
        msg_count: int = None,
    ):
        self.class_id = class_id
        self.msg_count = msg_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_id is not None:
            result['ClassId'] = self.class_id
        if self.msg_count is not None:
            result['MsgCount'] = self.msg_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')
        if m.get('MsgCount') is not None:
            self.msg_count = m.get('MsgCount')
        return self


class ReadNumGroupByClassResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ReadNumGroupByClassResponseBodyData] = None,
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ReadNumGroupByClassResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReadNumGroupByClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadNumGroupByClassResponseBody = None,
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
            temp_model = ReadNumGroupByClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadNumGroupTotalRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        client_source: str = None,
        cookies: str = None,
        src_url: str = None,
        tenant_code: str = None,
        title: str = None,
        uid_type: str = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.biz_name = biz_name
        self.caller_protocol = caller_protocol
        self.client_source = client_source
        self.cookies = cookies
        self.src_url = src_url
        self.tenant_code = tenant_code
        self.title = title
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.biz_name is not None:
            result['BizName'] = self.biz_name
        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol
        if self.client_source is not None:
            result['ClientSource'] = self.client_source
        if self.cookies is not None:
            result['Cookies'] = self.cookies
        if self.src_url is not None:
            result['SrcUrl'] = self.src_url
        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code
        if self.title is not None:
            result['Title'] = self.title
        if self.uid_type is not None:
            result['UidType'] = self.uid_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')
        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')
        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')
        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')
        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')
        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')
        return self


class ReadNumGroupTotalResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        read_count: int = None,
        total_count: int = None,
        un_read_count: int = None,
    ):
        self.id = id
        self.read_count = read_count
        self.total_count = total_count
        self.un_read_count = un_read_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.read_count is not None:
            result['ReadCount'] = self.read_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.un_read_count is not None:
            result['UnReadCount'] = self.un_read_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UnReadCount') is not None:
            self.un_read_count = m.get('UnReadCount')
        return self


class ReadNumGroupTotalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ReadNumGroupTotalResponseBodyData] = None,
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ReadNumGroupTotalResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReadNumGroupTotalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadNumGroupTotalResponseBody = None,
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
            temp_model = ReadNumGroupTotalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


