# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class ConvertUrlHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_airticket_access_token: str = None,
        x_acs_airticket_language: str = None,
    ):
        self.common_headers = common_headers
        # token
        # 
        # This parameter is required.
        self.x_acs_airticket_access_token = x_acs_airticket_access_token
        self.x_acs_airticket_language = x_acs_airticket_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['xAcsAirticketAccessToken'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['xAcsAirticketLanguage'] = self.x_acs_airticket_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('xAcsAirticketAccessToken') is not None:
            self.x_acs_airticket_access_token = m.get('xAcsAirticketAccessToken')
        if m.get('xAcsAirticketLanguage') is not None:
            self.x_acs_airticket_language = m.get('xAcsAirticketLanguage')
        return self


class ConvertUrlRequest(TeaModel):
    def __init__(
        self,
        country_calling_code: str = None,
        jump_url: str = None,
        phone: str = None,
        scene: str = None,
        source: str = None,
        third_id: str = None,
        uid: str = None,
        xenv: str = None,
    ):
        self.country_calling_code = country_calling_code
        # This parameter is required.
        self.jump_url = jump_url
        # This parameter is required.
        self.phone = phone
        # This parameter is required.
        self.scene = scene
        # This parameter is required.
        self.source = source
        self.third_id = third_id
        # This parameter is required.
        self.uid = uid
        # This parameter is required.
        self.xenv = xenv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_calling_code is not None:
            result['countryCallingCode'] = self.country_calling_code
        if self.jump_url is not None:
            result['jumpUrl'] = self.jump_url
        if self.phone is not None:
            result['phone'] = self.phone
        if self.scene is not None:
            result['scene'] = self.scene
        if self.source is not None:
            result['source'] = self.source
        if self.third_id is not None:
            result['thirdId'] = self.third_id
        if self.uid is not None:
            result['uid'] = self.uid
        if self.xenv is not None:
            result['xenv'] = self.xenv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('countryCallingCode') is not None:
            self.country_calling_code = m.get('countryCallingCode')
        if m.get('jumpUrl') is not None:
            self.jump_url = m.get('jumpUrl')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('thirdId') is not None:
            self.third_id = m.get('thirdId')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('xenv') is not None:
            self.xenv = m.get('xenv')
        return self


class ConvertUrlResponseBodyDataStatus(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_msg: str = None,
    ):
        self.code = code
        self.error_msg = error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        return self


class ConvertUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        auth_url: str = None,
        status: ConvertUrlResponseBodyDataStatus = None,
        version: str = None,
    ):
        self.app_id = app_id
        self.auth_url = auth_url
        # This parameter is required.
        self.status = status
        self.version = version

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.auth_url is not None:
            result['authUrl'] = self.auth_url
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('authUrl') is not None:
            self.auth_url = m.get('authUrl')
        if m.get('status') is not None:
            temp_model = ConvertUrlResponseBodyDataStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ConvertUrlResponseBodyErrorData(TeaModel):
    def __init__(
        self,
        raw_error_code: str = None,
        raw_error_msg: str = None,
    ):
        self.raw_error_code = raw_error_code
        self.raw_error_msg = raw_error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw_error_code is not None:
            result['rawErrorCode'] = self.raw_error_code
        if self.raw_error_msg is not None:
            result['rawErrorMsg'] = self.raw_error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rawErrorCode') is not None:
            self.raw_error_code = m.get('rawErrorCode')
        if m.get('rawErrorMsg') is not None:
            self.raw_error_msg = m.get('rawErrorMsg')
        return self


class ConvertUrlResponseBody(TeaModel):
    def __init__(
        self,
        data: ConvertUrlResponseBodyData = None,
        error_code: str = None,
        error_data: ConvertUrlResponseBodyErrorData = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_data = error_data
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        # This parameter is required.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.error_data:
            self.error_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_data is not None:
            result['errorData'] = self.error_data.to_map()
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ConvertUrlResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorData') is not None:
            temp_model = ConvertUrlResponseBodyErrorData()
            self.error_data = temp_model.from_map(m['errorData'])
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ConvertUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConvertUrlResponseBody = None,
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
            temp_model = ConvertUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.app_secret = app_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['appKey'] = self.app_key
        if self.app_secret is not None:
            result['appSecret'] = self.app_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')
        if m.get('appSecret') is not None:
            self.app_secret = m.get('appSecret')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        expire_time: str = None,
        generate_time: str = None,
        token: str = None,
    ):
        self.expire_time = expire_time
        self.generate_time = generate_time
        # token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.generate_time is not None:
            result['generateTime'] = self.generate_time
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('generateTime') is not None:
            self.generate_time = m.get('generateTime')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetTokenResponseBodyErrorData(TeaModel):
    def __init__(
        self,
        raw_error_code: str = None,
        raw_error_msg: str = None,
    ):
        self.raw_error_code = raw_error_code
        self.raw_error_msg = raw_error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw_error_code is not None:
            result['rawErrorCode'] = self.raw_error_code
        if self.raw_error_msg is not None:
            result['rawErrorMsg'] = self.raw_error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rawErrorCode') is not None:
            self.raw_error_code = m.get('rawErrorCode')
        if m.get('rawErrorMsg') is not None:
            self.raw_error_msg = m.get('rawErrorMsg')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTokenResponseBodyData = None,
        error_code: str = None,
        error_data: GetTokenResponseBodyErrorData = None,
        error_msg: str = None,
        request_id: str = None,
        status: int = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_data = error_data
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.error_data:
            self.error_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_data is not None:
            result['errorData'] = self.error_data.to_map()
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorData') is not None:
            temp_model = GetTokenResponseBodyErrorData()
            self.error_data = temp_model.from_map(m['errorData'])
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTokenResponseBody = None,
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
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_airticket_access_token: str = None,
        x_acs_airticket_language: str = None,
    ):
        self.common_headers = common_headers
        # token
        # 
        # This parameter is required.
        self.x_acs_airticket_access_token = x_acs_airticket_access_token
        self.x_acs_airticket_language = x_acs_airticket_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_airticket_access_token is not None:
            result['xAcsAirticketAccessToken'] = self.x_acs_airticket_access_token
        if self.x_acs_airticket_language is not None:
            result['xAcsAirticketLanguage'] = self.x_acs_airticket_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('xAcsAirticketAccessToken') is not None:
            self.x_acs_airticket_access_token = m.get('xAcsAirticketAccessToken')
        if m.get('xAcsAirticketLanguage') is not None:
            self.x_acs_airticket_language = m.get('xAcsAirticketLanguage')
        return self


class SearchRequest(TeaModel):
    def __init__(
        self,
        scene: str = None,
        search_param: str = None,
        source: str = None,
        terminal: str = None,
        user_id: str = None,
    ):
        self.scene = scene
        # This parameter is required.
        self.search_param = search_param
        # This parameter is required.
        self.source = source
        # This parameter is required.
        self.terminal = terminal
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['scene'] = self.scene
        if self.search_param is not None:
            result['searchParam'] = self.search_param
        if self.source is not None:
            result['source'] = self.source
        if self.terminal is not None:
            result['terminal'] = self.terminal
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('searchParam') is not None:
            self.search_param = m.get('searchParam')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SearchResponseBodyErrorData(TeaModel):
    def __init__(
        self,
        raw_error_code: str = None,
        raw_error_msg: str = None,
    ):
        self.raw_error_code = raw_error_code
        self.raw_error_msg = raw_error_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw_error_code is not None:
            result['rawErrorCode'] = self.raw_error_code
        if self.raw_error_msg is not None:
            result['rawErrorMsg'] = self.raw_error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rawErrorCode') is not None:
            self.raw_error_code = m.get('rawErrorCode')
        if m.get('rawErrorMsg') is not None:
            self.raw_error_msg = m.get('rawErrorMsg')
        return self


class SearchResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_data: SearchResponseBodyErrorData = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # This parameter is required.
        self.data = data
        self.error_code = error_code
        self.error_data = error_data
        self.error_msg = error_msg
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.error_data:
            self.error_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_data is not None:
            result['errorData'] = self.error_data.to_map()
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorData') is not None:
            temp_model = SearchResponseBodyErrorData()
            self.error_data = temp_model.from_map(m['errorData'])
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchResponseBody = None,
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
            temp_model = SearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


