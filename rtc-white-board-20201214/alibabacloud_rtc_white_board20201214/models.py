# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
    ):
        # 白板应用名，由不超过32位的中文、英文、数字或下划线组成
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class CreateAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # 白板应用唯一标识符
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: CreateAppResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 返回结果体
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = CreateAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWhiteBoardRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        app_id: str = None,
    ):
        # 创建白板的用户ID（客户业务用户），由纯数字组成。
        self.user_id = user_id
        # 白板应用唯一标识符
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.app_id is not None:
            result['AppID'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        return self


class CreateWhiteBoardResponseBodyResult(TeaModel):
    def __init__(
        self,
        doc_key: str = None,
    ):
        # 文档唯一标识符，由大小写字母和数字组成
        self.doc_key = doc_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        return self


class CreateWhiteBoardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: CreateWhiteBoardResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 返回结果体
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = CreateWhiteBoardResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateWhiteBoardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWhiteBoardResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateWhiteBoardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenWhiteBoardRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        user_id: str = None,
        doc_key: str = None,
    ):
        # 白板应用唯一标识符
        self.app_id = app_id
        # 打开白板的用户ID（客户业务用户），由纯数字组成
        self.user_id = user_id
        # 白板文档唯一标识符
        self.doc_key = doc_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        return self


class OpenWhiteBoardResponseBodyResultDocumentAccessInfoUserInfo(TeaModel):
    def __init__(
        self,
        avatar_url: str = None,
        nick: str = None,
        nick_pinyin: str = None,
        user_id: str = None,
    ):
        # 用户头像的URL
        self.avatar_url = avatar_url
        # 用户昵称
        self.nick = nick
        # 用户的拼音昵称
        self.nick_pinyin = nick_pinyin
        # 打开白板的用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.nick_pinyin is not None:
            result['NickPinyin'] = self.nick_pinyin
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('NickPinyin') is not None:
            self.nick_pinyin = m.get('NickPinyin')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class OpenWhiteBoardResponseBodyResultDocumentAccessInfo(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        collab_host: str = None,
        permission: int = None,
        user_info: OpenWhiteBoardResponseBodyResultDocumentAccessInfoUserInfo = None,
        ws_domain: str = None,
    ):
        # 连接签名
        self.access_token = access_token
        # 白板长连接地址
        self.collab_host = collab_host
        # 权限码，取值：0:无权限，1:只读，2:读写
        self.permission = permission
        # 用户信息
        self.user_info = user_info
        # 新协议长连接服务域名
        self.ws_domain = ws_domain

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.collab_host is not None:
            result['CollabHost'] = self.collab_host
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.ws_domain is not None:
            result['WsDomain'] = self.ws_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('CollabHost') is not None:
            self.collab_host = m.get('CollabHost')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('UserInfo') is not None:
            temp_model = OpenWhiteBoardResponseBodyResultDocumentAccessInfoUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('WsDomain') is not None:
            self.ws_domain = m.get('WsDomain')
        return self


class OpenWhiteBoardResponseBodyResult(TeaModel):
    def __init__(
        self,
        document_access_info: OpenWhiteBoardResponseBodyResultDocumentAccessInfo = None,
    ):
        # 白板连接信息
        self.document_access_info = document_access_info

    def validate(self):
        if self.document_access_info:
            self.document_access_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_access_info is not None:
            result['DocumentAccessInfo'] = self.document_access_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentAccessInfo') is not None:
            temp_model = OpenWhiteBoardResponseBodyResultDocumentAccessInfo()
            self.document_access_info = temp_model.from_map(m['DocumentAccessInfo'])
        return self


class OpenWhiteBoardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: OpenWhiteBoardResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 返回结果体
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            temp_model = OpenWhiteBoardResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class OpenWhiteBoardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenWhiteBoardResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenWhiteBoardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshUsersPermissionsRequest(TeaModel):
    def __init__(
        self,
        user_ids: str = None,
        doc_key: str = None,
        app_id: str = None,
    ):
        # 需要刷新权限的用户ID，多个用英文逗号（,）分隔，最多30个，每个ID由纯数字组成
        self.user_ids = user_ids
        # 白板文档唯一标识符
        self.doc_key = doc_key
        # 白板应用唯一标识符
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.doc_key is not None:
            result['DocKey'] = self.doc_key
        if self.app_id is not None:
            result['AppID'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('DocKey') is not None:
            self.doc_key = m.get('DocKey')
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        return self


class RefreshUsersPermissionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 返回结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RefreshUsersPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshUsersPermissionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshUsersPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppCallbackUrlRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_callback_url: str = None,
        app_callback_auth_key: str = None,
    ):
        # 白板应用唯一标识符
        self.app_id = app_id
        # 白板应用回调地址URL
        self.app_callback_url = app_callback_url
        # 白板应用回调鉴权码，由8~20位大小写字母、数字或下划线组成
        self.app_callback_auth_key = app_callback_auth_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_callback_url is not None:
            result['AppCallbackUrl'] = self.app_callback_url
        if self.app_callback_auth_key is not None:
            result['AppCallbackAuthKey'] = self.app_callback_auth_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppCallbackUrl') is not None:
            self.app_callback_url = m.get('AppCallbackUrl')
        if m.get('AppCallbackAuthKey') is not None:
            self.app_callback_auth_key = m.get('AppCallbackAuthKey')
        return self


class SetAppCallbackUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 返回结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppCallbackUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetAppCallbackUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppCallbackUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppDomainNamesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_domain_names: str = None,
    ):
        # 白板应用唯一标识符
        self.app_id = app_id
        # 所有会使用到白板应用的客户网站域名，多个使用英文逗号(,)分隔，最多传10个
        self.app_domain_names = app_domain_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_domain_names is not None:
            result['AppDomainNames'] = self.app_domain_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppDomainNames') is not None:
            self.app_domain_names = m.get('AppDomainNames')
        return self


class SetAppDomainNamesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 返回结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppDomainNamesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetAppDomainNamesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppDomainNamesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppNameRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
    ):
        # 白板应用唯一标识符
        self.app_id = app_id
        # 白板应用名，由不超过32位的中文、英文、数字或下划线组成
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class SetAppNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 返回结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetAppNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetAppStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_status: int = None,
    ):
        # 白板应用唯一标识符
        self.app_id = app_id
        # 白板应用状态（取值：1:启用，2:停用）
        self.app_status = app_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppID'] = self.app_id
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppID') is not None:
            self.app_id = m.get('AppID')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        return self


class SetAppStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 请求结果
        self.response_success = response_success
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_msg = error_msg
        # 返回结果
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetAppStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetAppStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetAppStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


