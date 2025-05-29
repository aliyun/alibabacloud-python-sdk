# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateChannelSignRequest(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        contact: str = None,
        description: str = None,
        phone: str = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.channel_name = channel_name
        self.contact = contact
        self.description = description
        self.phone = phone
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.contact is not None:
            result['contact'] = self.contact
        if self.description is not None:
            result['description'] = self.description
        if self.phone is not None:
            result['phone'] = self.phone
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('contact') is not None:
            self.contact = m.get('contact')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CreateChannelSignResponseBodyData(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        contact: str = None,
        create_time: str = None,
        description: str = None,
        modify_time: str = None,
        phone: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.channel_name = channel_name
        self.contact = contact
        self.create_time = create_time
        self.description = description
        self.modify_time = modify_time
        self.phone = phone
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.contact is not None:
            result['contact'] = self.contact
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.phone is not None:
            result['phone'] = self.phone
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('contact') is not None:
            self.contact = m.get('contact')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class CreateChannelSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateChannelSignResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateChannelSignResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateChannelSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChannelSignResponseBody = None,
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
            temp_model = CreateChannelSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        euid: str = None,
        product_name: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.euid = euid
        # This parameter is required.
        self.product_name = product_name
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.euid is not None:
            result['euid'] = self.euid
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('euid') is not None:
            self.euid = m.get('euid')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateProductResponseBodyData(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        description: str = None,
        product_key: str = None,
        product_name: str = None,
        product_secret: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.api_key = api_key
        self.description = description
        self.product_key = product_key
        self.product_name = product_name
        self.product_secret = product_secret
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.description is not None:
            result['description'] = self.description
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_secret is not None:
            result['productSecret'] = self.product_secret
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productSecret') is not None:
            self.product_secret = m.get('productSecret')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateProductResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductResponseBody = None,
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
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductRequest(TeaModel):
    def __init__(
        self,
        product_key: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.product_key = product_key
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeleteProductResponseBodyData(TeaModel):
    def __init__(
        self,
        product_key: str = None,
        product_name: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.product_key = product_key
        self.product_name = product_name
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class DeleteProductResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteProductResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = DeleteProductResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductResponseBody = None,
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
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeviceRegisterRequest(TeaModel):
    def __init__(
        self,
        nonce: str = None,
        product_key: str = None,
        request_time: str = None,
        signature: str = None,
    ):
        # This parameter is required.
        self.nonce = nonce
        # This parameter is required.
        self.product_key = product_key
        # This parameter is required.
        self.request_time = request_time
        # This parameter is required.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.request_time is not None:
            result['requestTime'] = self.request_time
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class DeviceRegisterResponseBodyData(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        nonce: str = None,
        product_key: str = None,
        response_time: str = None,
        signature: str = None,
    ):
        self.device_name = device_name
        self.nonce = nonce
        self.product_key = product_key
        self.response_time = response_time
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class DeviceRegisterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeviceRegisterResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = DeviceRegisterResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeviceRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeviceRegisterResponseBody = None,
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
            temp_model = DeviceRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChannelSignResponseBodyData(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        contact: str = None,
        create_time: str = None,
        description: str = None,
        modify_time: str = None,
        phone: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.channel_name = channel_name
        self.contact = contact
        self.create_time = create_time
        self.description = description
        self.modify_time = modify_time
        self.phone = phone
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.contact is not None:
            result['contact'] = self.contact
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.phone is not None:
            result['phone'] = self.phone
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('contact') is not None:
            self.contact = m.get('contact')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetChannelSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetChannelSignResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetChannelSignResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetChannelSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChannelSignResponseBody = None,
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
            temp_model = GetChannelSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQuotaInfoRequest(TeaModel):
    def __init__(
        self,
        record_id: int = None,
    ):
        # This parameter is required.
        self.record_id = record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_id is not None:
            result['recordId'] = self.record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        return self


class GetQuotaInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        active_license_count: int = None,
        duration: int = None,
        duration_type: int = None,
        license_count: int = None,
        max_qps: int = None,
        product_key: str = None,
        purchase_model: int = None,
        tenant_id: str = None,
        token_number: int = None,
        user_id: str = None,
    ):
        self.active_license_count = active_license_count
        self.duration = duration
        self.duration_type = duration_type
        self.license_count = license_count
        self.max_qps = max_qps
        self.product_key = product_key
        self.purchase_model = purchase_model
        self.tenant_id = tenant_id
        self.token_number = token_number
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_license_count is not None:
            result['activeLicenseCount'] = self.active_license_count
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_type is not None:
            result['durationType'] = self.duration_type
        if self.license_count is not None:
            result['licenseCount'] = self.license_count
        if self.max_qps is not None:
            result['maxQps'] = self.max_qps
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.purchase_model is not None:
            result['purchaseModel'] = self.purchase_model
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.token_number is not None:
            result['tokenNumber'] = self.token_number
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeLicenseCount') is not None:
            self.active_license_count = m.get('activeLicenseCount')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationType') is not None:
            self.duration_type = m.get('durationType')
        if m.get('licenseCount') is not None:
            self.license_count = m.get('licenseCount')
        if m.get('maxQps') is not None:
            self.max_qps = m.get('maxQps')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('purchaseModel') is not None:
            self.purchase_model = m.get('purchaseModel')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('tokenNumber') is not None:
            self.token_number = m.get('tokenNumber')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetQuotaInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQuotaInfoResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetQuotaInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetQuotaInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQuotaInfoResponseBody = None,
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
            temp_model = GetQuotaInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        nonce: str = None,
        product_key: str = None,
        request_time: str = None,
        signature: str = None,
        token_key: str = None,
        token_type: str = None,
    ):
        # This parameter is required.
        self.device_name = device_name
        # This parameter is required.
        self.nonce = nonce
        # This parameter is required.
        self.product_key = product_key
        # This parameter is required.
        self.request_time = request_time
        # This parameter is required.
        self.signature = signature
        self.token_key = token_key
        # This parameter is required.
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.request_time is not None:
            result['requestTime'] = self.request_time
        if self.signature is not None:
            result['signature'] = self.signature
        if self.token_key is not None:
            result['tokenKey'] = self.token_key
        if self.token_type is not None:
            result['tokenType'] = self.token_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('requestTime') is not None:
            self.request_time = m.get('requestTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('tokenKey') is not None:
            self.token_key = m.get('tokenKey')
        if m.get('tokenType') is not None:
            self.token_type = m.get('tokenType')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        nonce: str = None,
        product_key: str = None,
        request_ip: str = None,
        response_time: str = None,
        signature: str = None,
    ):
        self.device_name = device_name
        self.nonce = nonce
        self.product_key = product_key
        self.request_ip = request_ip
        self.response_time = response_time
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.request_ip is not None:
            result['requestIp'] = self.request_ip
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('requestIp') is not None:
            self.request_ip = m.get('requestIp')
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTokenResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
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


class HalfLLMAppCallRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        biz_param: Dict[str, str] = None,
        device_name: str = None,
        model_type_list: List[str] = None,
        product_key: str = None,
        session_id: str = None,
        tenant_id: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.biz_param = biz_param
        # This parameter is required.
        self.device_name = device_name
        # This parameter is required.
        self.model_type_list = model_type_list
        # This parameter is required.
        self.product_key = product_key
        self.session_id = session_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.biz_param is not None:
            result['bizParam'] = self.biz_param
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.model_type_list is not None:
            result['modelTypeList'] = self.model_type_list
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bizParam') is not None:
            self.biz_param = m.get('bizParam')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('modelTypeList') is not None:
            self.model_type_list = m.get('modelTypeList')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class HalfLLMAppCallShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        biz_param_shrink: str = None,
        device_name: str = None,
        model_type_list_shrink: str = None,
        product_key: str = None,
        session_id: str = None,
        tenant_id: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.biz_param_shrink = biz_param_shrink
        # This parameter is required.
        self.device_name = device_name
        # This parameter is required.
        self.model_type_list_shrink = model_type_list_shrink
        # This parameter is required.
        self.product_key = product_key
        self.session_id = session_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.biz_param_shrink is not None:
            result['bizParam'] = self.biz_param_shrink
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.model_type_list_shrink is not None:
            result['modelTypeList'] = self.model_type_list_shrink
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bizParam') is not None:
            self.biz_param_shrink = m.get('bizParam')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('modelTypeList') is not None:
            self.model_type_list_shrink = m.get('modelTypeList')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class HalfLLMAppCallResponseBodyDataOutputChoicesMessage(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class HalfLLMAppCallResponseBodyDataOutputChoices(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        message: HalfLLMAppCallResponseBodyDataOutputChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('message') is not None:
            temp_model = HalfLLMAppCallResponseBodyDataOutputChoicesMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class HalfLLMAppCallResponseBodyDataOutput(TeaModel):
    def __init__(
        self,
        choices: List[HalfLLMAppCallResponseBodyDataOutputChoices] = None,
    ):
        self.choices = choices

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = HalfLLMAppCallResponseBodyDataOutputChoices()
                self.choices.append(temp_model.from_map(k))
        return self


class HalfLLMAppCallResponseBodyDataRt(TeaModel):
    def __init__(
        self,
        first_rt: int = None,
        total_rt: int = None,
    ):
        self.first_rt = first_rt
        self.total_rt = total_rt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_rt is not None:
            result['firstRt'] = self.first_rt
        if self.total_rt is not None:
            result['totalRt'] = self.total_rt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstRt') is not None:
            self.first_rt = m.get('firstRt')
        if m.get('totalRt') is not None:
            self.total_rt = m.get('totalRt')
        return self


class HalfLLMAppCallResponseBodyDataUsages(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        return self


class HalfLLMAppCallResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: HalfLLMAppCallResponseBodyDataOutput = None,
        request_id: str = None,
        rt: HalfLLMAppCallResponseBodyDataRt = None,
        session_id: str = None,
        usages: HalfLLMAppCallResponseBodyDataUsages = None,
    ):
        self.code = code
        self.message = message
        self.output = output
        self.request_id = request_id
        self.rt = rt
        self.session_id = session_id
        self.usages = usages

    def validate(self):
        if self.output:
            self.output.validate()
        if self.rt:
            self.rt.validate()
        if self.usages:
            self.usages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.rt is not None:
            result['rt'] = self.rt.to_map()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.usages is not None:
            result['usages'] = self.usages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('output') is not None:
            temp_model = HalfLLMAppCallResponseBodyDataOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('rt') is not None:
            temp_model = HalfLLMAppCallResponseBodyDataRt()
            self.rt = temp_model.from_map(m['rt'])
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('usages') is not None:
            temp_model = HalfLLMAppCallResponseBodyDataUsages()
            self.usages = temp_model.from_map(m['usages'])
        return self


class HalfLLMAppCallResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HalfLLMAppCallResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = HalfLLMAppCallResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class HalfLLMAppCallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HalfLLMAppCallResponseBody = None,
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
            temp_model = HalfLLMAppCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HalfLLMChatRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        enable_search: bool = None,
        input_text: str = None,
        model: str = None,
        product_key: str = None,
        prompt: str = None,
        session_id: str = None,
        stream: bool = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.device_name = device_name
        self.enable_search = enable_search
        # This parameter is required.
        self.input_text = input_text
        self.model = model
        # This parameter is required.
        self.product_key = product_key
        self.prompt = prompt
        self.session_id = session_id
        self.stream = stream
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search
        if self.input_text is not None:
            result['inputText'] = self.input_text
        if self.model is not None:
            result['model'] = self.model
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.stream is not None:
            result['stream'] = self.stream
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')
        if m.get('inputText') is not None:
            self.input_text = m.get('inputText')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class HalfLLMChatResponseBodyDataOutputChoicesMessage(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class HalfLLMChatResponseBodyDataOutputChoices(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        message: HalfLLMChatResponseBodyDataOutputChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('message') is not None:
            temp_model = HalfLLMChatResponseBodyDataOutputChoicesMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class HalfLLMChatResponseBodyDataOutput(TeaModel):
    def __init__(
        self,
        choices: List[HalfLLMChatResponseBodyDataOutputChoices] = None,
    ):
        self.choices = choices

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = HalfLLMChatResponseBodyDataOutputChoices()
                self.choices.append(temp_model.from_map(k))
        return self


class HalfLLMChatResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: HalfLLMChatResponseBodyDataOutput = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.code = code
        self.message = message
        self.output = output
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.output:
            self.output.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('output') is not None:
            temp_model = HalfLLMChatResponseBodyDataOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class HalfLLMChatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HalfLLMChatResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = HalfLLMChatResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class HalfLLMChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HalfLLMChatResponseBody = None,
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
            temp_model = HalfLLMChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HalfLLMImageChatRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        enable_search: bool = None,
        image_url: str = None,
        input_text: str = None,
        model: str = None,
        product_key: str = None,
        prompt: str = None,
        session_id: str = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.device_name = device_name
        self.enable_search = enable_search
        # This parameter is required.
        self.image_url = image_url
        # This parameter is required.
        self.input_text = input_text
        self.model = model
        # This parameter is required.
        self.product_key = product_key
        self.prompt = prompt
        self.session_id = session_id
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.input_text is not None:
            result['inputText'] = self.input_text
        if self.model is not None:
            result['model'] = self.model
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('inputText') is not None:
            self.input_text = m.get('inputText')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class HalfLLMImageChatResponseBodyDataOutputChoicesMessage(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class HalfLLMImageChatResponseBodyDataOutputChoices(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        message: HalfLLMImageChatResponseBodyDataOutputChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('message') is not None:
            temp_model = HalfLLMImageChatResponseBodyDataOutputChoicesMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class HalfLLMImageChatResponseBodyDataOutput(TeaModel):
    def __init__(
        self,
        choices: List[HalfLLMImageChatResponseBodyDataOutputChoices] = None,
    ):
        self.choices = choices

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = HalfLLMImageChatResponseBodyDataOutputChoices()
                self.choices.append(temp_model.from_map(k))
        return self


class HalfLLMImageChatResponseBodyDataRt(TeaModel):
    def __init__(
        self,
        first_rt: int = None,
        total_rt: int = None,
    ):
        self.first_rt = first_rt
        self.total_rt = total_rt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_rt is not None:
            result['firstRt'] = self.first_rt
        if self.total_rt is not None:
            result['totalRt'] = self.total_rt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstRt') is not None:
            self.first_rt = m.get('firstRt')
        if m.get('totalRt') is not None:
            self.total_rt = m.get('totalRt')
        return self


class HalfLLMImageChatResponseBodyDataUsages(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        return self


class HalfLLMImageChatResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: HalfLLMImageChatResponseBodyDataOutput = None,
        request_id: str = None,
        rt: HalfLLMImageChatResponseBodyDataRt = None,
        session_id: str = None,
        usages: HalfLLMImageChatResponseBodyDataUsages = None,
    ):
        self.code = code
        self.message = message
        self.output = output
        self.request_id = request_id
        self.rt = rt
        self.session_id = session_id
        self.usages = usages

    def validate(self):
        if self.output:
            self.output.validate()
        if self.rt:
            self.rt.validate()
        if self.usages:
            self.usages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.rt is not None:
            result['rt'] = self.rt.to_map()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.usages is not None:
            result['usages'] = self.usages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('output') is not None:
            temp_model = HalfLLMImageChatResponseBodyDataOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('rt') is not None:
            temp_model = HalfLLMImageChatResponseBodyDataRt()
            self.rt = temp_model.from_map(m['rt'])
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('usages') is not None:
            temp_model = HalfLLMImageChatResponseBodyDataUsages()
            self.usages = temp_model.from_map(m['usages'])
        return self


class HalfLLMImageChatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HalfLLMImageChatResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = HalfLLMImageChatResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class HalfLLMImageChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HalfLLMImageChatResponseBody = None,
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
            temp_model = HalfLLMImageChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HalfLLMImageOcrRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        image_url: str = None,
        model: str = None,
        product_key: str = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.device_name = device_name
        # This parameter is required.
        self.image_url = image_url
        self.model = model
        # This parameter is required.
        self.product_key = product_key
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.model is not None:
            result['model'] = self.model
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class HalfLLMImageOcrResponseBodyDataOutputChoicesMessage(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class HalfLLMImageOcrResponseBodyDataOutputChoices(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        message: HalfLLMImageOcrResponseBodyDataOutputChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.message is not None:
            result['message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('message') is not None:
            temp_model = HalfLLMImageOcrResponseBodyDataOutputChoicesMessage()
            self.message = temp_model.from_map(m['message'])
        return self


class HalfLLMImageOcrResponseBodyDataOutput(TeaModel):
    def __init__(
        self,
        choices: List[HalfLLMImageOcrResponseBodyDataOutputChoices] = None,
    ):
        self.choices = choices

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['choices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('choices') is not None:
            for k in m.get('choices'):
                temp_model = HalfLLMImageOcrResponseBodyDataOutputChoices()
                self.choices.append(temp_model.from_map(k))
        return self


class HalfLLMImageOcrResponseBodyDataRt(TeaModel):
    def __init__(
        self,
        first_rt: int = None,
        total_rt: int = None,
    ):
        self.first_rt = first_rt
        self.total_rt = total_rt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_rt is not None:
            result['firstRt'] = self.first_rt
        if self.total_rt is not None:
            result['totalRt'] = self.total_rt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstRt') is not None:
            self.first_rt = m.get('firstRt')
        if m.get('totalRt') is not None:
            self.total_rt = m.get('totalRt')
        return self


class HalfLLMImageOcrResponseBodyDataUsages(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        return self


class HalfLLMImageOcrResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: HalfLLMImageOcrResponseBodyDataOutput = None,
        request_id: str = None,
        rt: HalfLLMImageOcrResponseBodyDataRt = None,
        session_id: str = None,
        usages: HalfLLMImageOcrResponseBodyDataUsages = None,
    ):
        self.code = code
        self.message = message
        self.output = output
        self.request_id = request_id
        self.rt = rt
        self.session_id = session_id
        self.usages = usages

    def validate(self):
        if self.output:
            self.output.validate()
        if self.rt:
            self.rt.validate()
        if self.usages:
            self.usages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.output is not None:
            result['output'] = self.output.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.rt is not None:
            result['rt'] = self.rt.to_map()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.usages is not None:
            result['usages'] = self.usages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('output') is not None:
            temp_model = HalfLLMImageOcrResponseBodyDataOutput()
            self.output = temp_model.from_map(m['output'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('rt') is not None:
            temp_model = HalfLLMImageOcrResponseBodyDataRt()
            self.rt = temp_model.from_map(m['rt'])
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('usages') is not None:
            temp_model = HalfLLMImageOcrResponseBodyDataUsages()
            self.usages = temp_model.from_map(m['usages'])
        return self


class HalfLLMImageOcrResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HalfLLMImageOcrResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = HalfLLMImageOcrResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class HalfLLMImageOcrResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HalfLLMImageOcrResponseBody = None,
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
            temp_model = HalfLLMImageOcrResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HalfLLMTTSChatRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        enable_search: bool = None,
        format: str = None,
        model: str = None,
        pitch_rate: int = None,
        product_key: str = None,
        prompt: str = None,
        sample_rate: int = None,
        session_id: str = None,
        speech_rate: int = None,
        stream: bool = None,
        tenant_id: str = None,
        text: str = None,
        url: str = None,
        voice: str = None,
        volume: int = None,
    ):
        # This parameter is required.
        self.device_name = device_name
        self.enable_search = enable_search
        self.format = format
        self.model = model
        self.pitch_rate = pitch_rate
        # This parameter is required.
        self.product_key = product_key
        self.prompt = prompt
        self.sample_rate = sample_rate
        self.session_id = session_id
        self.speech_rate = speech_rate
        self.stream = stream
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.text = text
        self.url = url
        self.voice = voice
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.enable_search is not None:
            result['enableSearch'] = self.enable_search
        if self.format is not None:
            result['format'] = self.format
        if self.model is not None:
            result['model'] = self.model
        if self.pitch_rate is not None:
            result['pitchRate'] = self.pitch_rate
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.prompt is not None:
            result['prompt'] = self.prompt
        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.speech_rate is not None:
            result['speechRate'] = self.speech_rate
        if self.stream is not None:
            result['stream'] = self.stream
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.text is not None:
            result['text'] = self.text
        if self.url is not None:
            result['url'] = self.url
        if self.voice is not None:
            result['voice'] = self.voice
        if self.volume is not None:
            result['volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('enableSearch') is not None:
            self.enable_search = m.get('enableSearch')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('pitchRate') is not None:
            self.pitch_rate = m.get('pitchRate')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')
        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('speechRate') is not None:
            self.speech_rate = m.get('speechRate')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('voice') is not None:
            self.voice = m.get('voice')
        if m.get('volume') is not None:
            self.volume = m.get('volume')
        return self


class HalfLLMTTSChatResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bytes = None,
        message: str = None,
        request_id: str = None,
        session_id: str = None,
        text: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.session_id = session_id
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class HalfLLMTTSChatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HalfLLMTTSChatResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = HalfLLMTTSChatResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class HalfLLMTTSChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HalfLLMTTSChatResponseBody = None,
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
            temp_model = HalfLLMTTSChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePageRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        disable_status: int = None,
        page_index: int = None,
        page_size: int = None,
        product_key: str = None,
        product_name: str = None,
        status: int = None,
    ):
        self.device_name = device_name
        self.disable_status = disable_status
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size
        self.product_key = product_key
        self.product_name = product_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.disable_status is not None:
            result['disableStatus'] = self.disable_status
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('disableStatus') is not None:
            self.disable_status = m.get('disableStatus')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class QueryDevicePageResponseBodyDataData(TeaModel):
    def __init__(
        self,
        active_time: str = None,
        aliyun_uid: str = None,
        batch_no: str = None,
        device_name: str = None,
        disable_status: int = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        id: int = None,
        product_key: str = None,
        product_name: str = None,
        remark: str = None,
        status: int = None,
        tenant_id: str = None,
    ):
        self.active_time = active_time
        self.aliyun_uid = aliyun_uid
        self.batch_no = batch_no
        self.device_name = device_name
        self.disable_status = disable_status
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        # ID。
        self.id = id
        self.product_key = product_key
        self.product_name = product_name
        self.remark = remark
        self.status = status
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['activeTime'] = self.active_time
        if self.aliyun_uid is not None:
            result['aliyunUid'] = self.aliyun_uid
        if self.batch_no is not None:
            result['batchNo'] = self.batch_no
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.disable_status is not None:
            result['disableStatus'] = self.disable_status
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmtModify'] = self.gmt_modify
        if self.id is not None:
            result['id'] = self.id
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeTime') is not None:
            self.active_time = m.get('activeTime')
        if m.get('aliyunUid') is not None:
            self.aliyun_uid = m.get('aliyunUid')
        if m.get('batchNo') is not None:
            self.batch_no = m.get('batchNo')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('disableStatus') is not None:
            self.disable_status = m.get('disableStatus')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModify') is not None:
            self.gmt_modify = m.get('gmtModify')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class QueryDevicePageResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[QueryDevicePageResponseBodyDataData] = None,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page_index = page_index
        self.page_size = page_size
        self.total = total

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryDevicePageResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryDevicePageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryDevicePageResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = QueryDevicePageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryDevicePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDevicePageResponseBody = None,
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
            temp_model = QueryDevicePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProductPageRequest(TeaModel):
    def __init__(
        self,
        model_type: bytes = None,
        page_index: int = None,
        page_size: int = None,
        product_name: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.model_type = model_type
        self.page_index = page_index
        self.page_size = page_size
        self.product_name = product_name
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_type is not None:
            result['modelType'] = self.model_type
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryProductPageResponseBodyDataData(TeaModel):
    def __init__(
        self,
        active_license_count: int = None,
        api_key: str = None,
        create_time: str = None,
        description: str = None,
        license_count: int = None,
        max_qps: int = None,
        product_key: str = None,
        product_name: str = None,
        product_secret: str = None,
        tenant_id: str = None,
        token_count: int = None,
        update_time: str = None,
        used_token: int = None,
        user_id: str = None,
    ):
        self.active_license_count = active_license_count
        self.api_key = api_key
        self.create_time = create_time
        self.description = description
        self.license_count = license_count
        self.max_qps = max_qps
        self.product_key = product_key
        self.product_name = product_name
        self.product_secret = product_secret
        self.tenant_id = tenant_id
        self.token_count = token_count
        self.update_time = update_time
        self.used_token = used_token
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_license_count is not None:
            result['activeLicenseCount'] = self.active_license_count
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.license_count is not None:
            result['licenseCount'] = self.license_count
        if self.max_qps is not None:
            result['maxQps'] = self.max_qps
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_secret is not None:
            result['productSecret'] = self.product_secret
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.token_count is not None:
            result['tokenCount'] = self.token_count
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.used_token is not None:
            result['usedToken'] = self.used_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeLicenseCount') is not None:
            self.active_license_count = m.get('activeLicenseCount')
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('licenseCount') is not None:
            self.license_count = m.get('licenseCount')
        if m.get('maxQps') is not None:
            self.max_qps = m.get('maxQps')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productSecret') is not None:
            self.product_secret = m.get('productSecret')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('tokenCount') is not None:
            self.token_count = m.get('tokenCount')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('usedToken') is not None:
            self.used_token = m.get('usedToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryProductPageResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[QueryProductPageResponseBodyDataData] = None,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page_index = page_index
        self.page_size = page_size
        self.total = total

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryProductPageResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryProductPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryProductPageResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = QueryProductPageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryProductPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProductPageResponseBody = None,
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
            temp_model = QueryProductPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProductQuotaPageRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        product_key: str = None,
        product_name: str = None,
        purchase_time_end: str = None,
        purchase_time_start: str = None,
        purchase_type: int = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.product_key = product_key
        self.product_name = product_name
        self.purchase_time_end = purchase_time_end
        self.purchase_time_start = purchase_time_start
        self.purchase_type = purchase_type
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.purchase_time_end is not None:
            result['purchaseTimeEnd'] = self.purchase_time_end
        if self.purchase_time_start is not None:
            result['purchaseTimeStart'] = self.purchase_time_start
        if self.purchase_type is not None:
            result['purchaseType'] = self.purchase_type
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('purchaseTimeEnd') is not None:
            self.purchase_time_end = m.get('purchaseTimeEnd')
        if m.get('purchaseTimeStart') is not None:
            self.purchase_time_start = m.get('purchaseTimeStart')
        if m.get('purchaseType') is not None:
            self.purchase_type = m.get('purchaseType')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryProductQuotaPageResponseBodyDataData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        duration: int = None,
        duration_type: int = None,
        expire_time: str = None,
        id: int = None,
        if_unsubscribe: int = None,
        if_used: int = None,
        license_count: int = None,
        max_qps: int = None,
        order_id: str = None,
        product_key: str = None,
        product_name: str = None,
        purchase_model: int = None,
        purchase_type: int = None,
        settlement_fee: float = None,
        tenant_id: str = None,
        token_number: int = None,
        unit_price: float = None,
        update_time: str = None,
        user_id: str = None,
    ):
        self.create_time = create_time
        self.duration = duration
        self.duration_type = duration_type
        self.expire_time = expire_time
        # ID。
        self.id = id
        self.if_unsubscribe = if_unsubscribe
        self.if_used = if_used
        self.license_count = license_count
        self.max_qps = max_qps
        self.order_id = order_id
        self.product_key = product_key
        self.product_name = product_name
        self.purchase_model = purchase_model
        self.purchase_type = purchase_type
        self.settlement_fee = settlement_fee
        self.tenant_id = tenant_id
        self.token_number = token_number
        self.unit_price = unit_price
        self.update_time = update_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_type is not None:
            result['durationType'] = self.duration_type
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.id is not None:
            result['id'] = self.id
        if self.if_unsubscribe is not None:
            result['ifUnsubscribe'] = self.if_unsubscribe
        if self.if_used is not None:
            result['ifUsed'] = self.if_used
        if self.license_count is not None:
            result['licenseCount'] = self.license_count
        if self.max_qps is not None:
            result['maxQps'] = self.max_qps
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.purchase_model is not None:
            result['purchaseModel'] = self.purchase_model
        if self.purchase_type is not None:
            result['purchaseType'] = self.purchase_type
        if self.settlement_fee is not None:
            result['settlementFee'] = self.settlement_fee
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.token_number is not None:
            result['tokenNumber'] = self.token_number
        if self.unit_price is not None:
            result['unitPrice'] = self.unit_price
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationType') is not None:
            self.duration_type = m.get('durationType')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('ifUnsubscribe') is not None:
            self.if_unsubscribe = m.get('ifUnsubscribe')
        if m.get('ifUsed') is not None:
            self.if_used = m.get('ifUsed')
        if m.get('licenseCount') is not None:
            self.license_count = m.get('licenseCount')
        if m.get('maxQps') is not None:
            self.max_qps = m.get('maxQps')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('purchaseModel') is not None:
            self.purchase_model = m.get('purchaseModel')
        if m.get('purchaseType') is not None:
            self.purchase_type = m.get('purchaseType')
        if m.get('settlementFee') is not None:
            self.settlement_fee = m.get('settlementFee')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('tokenNumber') is not None:
            self.token_number = m.get('tokenNumber')
        if m.get('unitPrice') is not None:
            self.unit_price = m.get('unitPrice')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class QueryProductQuotaPageResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[QueryProductQuotaPageResponseBodyDataData] = None,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page_index = page_index
        self.page_size = page_size
        self.total = total

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryProductQuotaPageResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryProductQuotaPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryProductQuotaPageResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = QueryProductQuotaPageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryProductQuotaPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryProductQuotaPageResponseBody = None,
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
            temp_model = QueryProductQuotaPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTokenUsageRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        product_key: str = None,
        start_date: str = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.end_date = end_date
        self.product_key = product_key
        # This parameter is required.
        self.start_date = start_date
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        return self


class QueryTokenUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        input_token: int = None,
        output_token: int = None,
        product_key: str = None,
        product_name: str = None,
        tenant_id: str = None,
        usage_time: str = None,
    ):
        self.api_key = api_key
        self.input_token = input_token
        self.output_token = output_token
        self.product_key = product_key
        self.product_name = product_name
        self.tenant_id = tenant_id
        self.usage_time = usage_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['apiKey'] = self.api_key
        if self.input_token is not None:
            result['inputToken'] = self.input_token
        if self.output_token is not None:
            result['outputToken'] = self.output_token
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.usage_time is not None:
            result['usageTime'] = self.usage_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')
        if m.get('inputToken') is not None:
            self.input_token = m.get('inputToken')
        if m.get('outputToken') is not None:
            self.output_token = m.get('outputToken')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('usageTime') is not None:
            self.usage_time = m.get('usageTime')
        return self


class QueryTokenUsageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryTokenUsageResponseBodyData] = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = QueryTokenUsageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryTokenUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTokenUsageResponseBody = None,
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
            temp_model = QueryTokenUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeChannelSignResponseBodyData(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        contact: str = None,
        create_time: str = None,
        description: str = None,
        modify_time: str = None,
        phone: str = None,
        remark: str = None,
        status: str = None,
    ):
        self.channel_name = channel_name
        self.contact = contact
        self.create_time = create_time
        self.description = description
        self.modify_time = modify_time
        self.phone = phone
        self.remark = remark
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['channelName'] = self.channel_name
        if self.contact is not None:
            result['contact'] = self.contact
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.phone is not None:
            result['phone'] = self.phone
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelName') is not None:
            self.channel_name = m.get('channelName')
        if m.get('contact') is not None:
            self.contact = m.get('contact')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class RevokeChannelSignResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RevokeChannelSignResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = RevokeChannelSignResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RevokeChannelSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RevokeChannelSignResponseBody = None,
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
            temp_model = RevokeChannelSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeviceStatusRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        product_key: str = None,
        remark: str = None,
        status: int = None,
    ):
        # This parameter is required.
        self.device_name = device_name
        # This parameter is required.
        self.product_key = product_key
        self.remark = remark
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateDeviceStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateDeviceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeviceStatusResponseBody = None,
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
            temp_model = UpdateDeviceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageQuotaRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        duration_type: int = None,
        image_count: int = None,
        license_count: int = None,
        package_type: int = None,
        product_key: str = None,
        purchase_type: int = None,
        record_id: int = None,
        settlement_amount: float = None,
        tenant_id: str = None,
        unit_price: float = None,
        user_id: str = None,
    ):
        self.duration = duration
        self.duration_type = duration_type
        self.image_count = image_count
        self.license_count = license_count
        self.package_type = package_type
        # This parameter is required.
        self.product_key = product_key
        # This parameter is required.
        self.purchase_type = purchase_type
        self.record_id = record_id
        # This parameter is required.
        self.settlement_amount = settlement_amount
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.unit_price = unit_price
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_type is not None:
            result['durationType'] = self.duration_type
        if self.image_count is not None:
            result['imageCount'] = self.image_count
        if self.license_count is not None:
            result['licenseCount'] = self.license_count
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.purchase_type is not None:
            result['purchaseType'] = self.purchase_type
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.settlement_amount is not None:
            result['settlementAmount'] = self.settlement_amount
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.unit_price is not None:
            result['unitPrice'] = self.unit_price
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationType') is not None:
            self.duration_type = m.get('durationType')
        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')
        if m.get('licenseCount') is not None:
            self.license_count = m.get('licenseCount')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('purchaseType') is not None:
            self.purchase_type = m.get('purchaseType')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('settlementAmount') is not None:
            self.settlement_amount = m.get('settlementAmount')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('unitPrice') is not None:
            self.unit_price = m.get('unitPrice')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateImageQuotaResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        product_key: str = None,
        product_name: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.order_id = order_id
        self.product_key = product_key
        self.product_name = product_name
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateImageQuotaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateImageQuotaResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = UpdateImageQuotaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateImageQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateImageQuotaResponseBody = None,
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
            temp_model = UpdateImageQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateQuotaRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        duration_type: int = None,
        license_count: int = None,
        max_qps: int = None,
        package_type: int = None,
        product_key: str = None,
        purchase_type: int = None,
        record_id: int = None,
        settlement_amount: float = None,
        tenant_id: str = None,
        token_number: int = None,
        unit_price: float = None,
        user_id: str = None,
    ):
        self.duration = duration
        self.duration_type = duration_type
        self.license_count = license_count
        self.max_qps = max_qps
        self.package_type = package_type
        # This parameter is required.
        self.product_key = product_key
        # This parameter is required.
        self.purchase_type = purchase_type
        self.record_id = record_id
        # This parameter is required.
        self.settlement_amount = settlement_amount
        # This parameter is required.
        self.tenant_id = tenant_id
        self.token_number = token_number
        # This parameter is required.
        self.unit_price = unit_price
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.duration_type is not None:
            result['durationType'] = self.duration_type
        if self.license_count is not None:
            result['licenseCount'] = self.license_count
        if self.max_qps is not None:
            result['maxQps'] = self.max_qps
        if self.package_type is not None:
            result['packageType'] = self.package_type
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.purchase_type is not None:
            result['purchaseType'] = self.purchase_type
        if self.record_id is not None:
            result['recordId'] = self.record_id
        if self.settlement_amount is not None:
            result['settlementAmount'] = self.settlement_amount
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.token_number is not None:
            result['tokenNumber'] = self.token_number
        if self.unit_price is not None:
            result['unitPrice'] = self.unit_price
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('durationType') is not None:
            self.duration_type = m.get('durationType')
        if m.get('licenseCount') is not None:
            self.license_count = m.get('licenseCount')
        if m.get('maxQps') is not None:
            self.max_qps = m.get('maxQps')
        if m.get('packageType') is not None:
            self.package_type = m.get('packageType')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('purchaseType') is not None:
            self.purchase_type = m.get('purchaseType')
        if m.get('recordId') is not None:
            self.record_id = m.get('recordId')
        if m.get('settlementAmount') is not None:
            self.settlement_amount = m.get('settlementAmount')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('tokenNumber') is not None:
            self.token_number = m.get('tokenNumber')
        if m.get('unitPrice') is not None:
            self.unit_price = m.get('unitPrice')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateQuotaResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        product_key: str = None,
        product_name: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        self.order_id = order_id
        self.product_key = product_key
        self.product_name = product_name
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.product_key is not None:
            result['productKey'] = self.product_key
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('productKey') is not None:
            self.product_key = m.get('productKey')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class UpdateQuotaResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateQuotaResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = UpdateQuotaResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateQuotaResponseBody = None,
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
            temp_model = UpdateQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


