# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class GetOssUploadParamRequest(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        data_source_id: str = None,
        file_name: str = None,
        file_type: int = None,
    ):
        # App版本号
        self.app_version = app_version
        # 数据源id（appKey)
        self.data_source_id = data_source_id
        # 文件名称，后缀只允许为txt,so,sym,zip,gz
        self.file_name = file_name
        # 文件类型(1 mapping文件；2 so文件；3 dSYM文件压缩包)
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['appVersion'] = self.app_version
        if self.data_source_id is not None:
            result['dataSourceId'] = self.data_source_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_type is not None:
            result['fileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appVersion') is not None:
            self.app_version = m.get('appVersion')
        if m.get('dataSourceId') is not None:
            self.data_source_id = m.get('dataSourceId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileType') is not None:
            self.file_type = m.get('fileType')
        return self


class GetOssUploadParamResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        callback: str = None,
        key: str = None,
        policy: str = None,
        signature: str = None,
        upload_address: str = None,
    ):
        # 文件上传表单必要参数
        self.access_key_id = access_key_id
        # 文件上传表单必要参数
        self.callback = callback
        # 文件上传表单必要参数
        self.key = key
        # 文件上传表单必要参数
        self.policy = policy
        # 文件上传表单必要参数
        self.signature = signature
        # 文件上传地址
        self.upload_address = upload_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.callback is not None:
            result['callback'] = self.callback
        if self.key is not None:
            result['key'] = self.key
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        if self.upload_address is not None:
            result['uploadAddress'] = self.upload_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('callback') is not None:
            self.callback = m.get('callback')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('uploadAddress') is not None:
            self.upload_address = m.get('uploadAddress')
        return self


class GetOssUploadParamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        data: GetOssUploadParamResponseBodyData = None,
        msg: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # 请求唯一ID
        self.request_id = request_id
        # code
        self.code = code
        # data
        self.data = data
        # 异常描述
        self.msg = msg
        # 是否成功
        self.success = success
        # traceId
        self.trace_id = trace_id

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
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetOssUploadParamResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class GetOssUploadParamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOssUploadParamResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOssUploadParamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


