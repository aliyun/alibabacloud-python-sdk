# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BuildStsAKRequest(TeaModel):
    def __init__(
        self,
        body: int = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class BuildStsAKResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        endpoint: str = None,
        id: str = None,
        path: str = None,
        secret: str = None,
        token: str = None,
    ):
        self.bucket = bucket
        self.endpoint = endpoint
        self.id = id
        self.path = path
        self.secret = secret
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.id is not None:
            result['id'] = self.id
        if self.path is not None:
            result['path'] = self.path
        if self.secret is not None:
            result['secret'] = self.secret
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class BuildStsAKResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BuildStsAKResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = BuildStsAKResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BuildStsAKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BuildStsAKResponseBody = None,
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
            temp_model = BuildStsAKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BuildStsAK2Request(TeaModel):
    def __init__(
        self,
        client_id: int = None,
        data_set_id: int = None,
    ):
        self.client_id = client_id
        self.data_set_id = data_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.data_set_id is not None:
            result['dataSetId'] = self.data_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('dataSetId') is not None:
            self.data_set_id = m.get('dataSetId')
        return self


class BuildStsAK2ResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        endpoint: str = None,
        id: str = None,
        path: str = None,
        secret: str = None,
        token: str = None,
    ):
        self.bucket = bucket
        self.endpoint = endpoint
        self.id = id
        self.path = path
        self.secret = secret
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.id is not None:
            result['id'] = self.id
        if self.path is not None:
            result['path'] = self.path
        if self.secret is not None:
            result['secret'] = self.secret
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class BuildStsAK2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BuildStsAK2ResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = BuildStsAK2ResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BuildStsAK2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BuildStsAK2ResponseBody = None,
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
            temp_model = BuildStsAK2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTaskRequest(TeaModel):
    def __init__(
        self,
        body: int = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class CancelTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelTaskResponseBody = None,
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
            temp_model = CancelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelTask2Request(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
        client_id: int = None,
    ):
        self.bc_id = bc_id
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.client_id is not None:
            result['clientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        return self


class CancelTask2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelTask2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelTask2ResponseBody = None,
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
            temp_model = CancelTask2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateComputeTaskRequestMorseInfoList(TeaModel):
    def __init__(
        self,
        cu_id: str = None,
        cu_version: str = None,
    ):
        self.cu_id = cu_id
        self.cu_version = cu_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_id is not None:
            result['cuId'] = self.cu_id
        if self.cu_version is not None:
            result['cuVersion'] = self.cu_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuId') is not None:
            self.cu_id = m.get('cuId')
        if m.get('cuVersion') is not None:
            self.cu_version = m.get('cuVersion')
        return self


class CreateComputeTaskRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        data_set_ids: str = None,
        morse_info_list: List[CreateComputeTaskRequestMorseInfoList] = None,
        name: str = None,
        remarks: str = None,
        type: str = None,
    ):
        self.app_id = app_id
        self.data_set_ids = data_set_ids
        self.morse_info_list = morse_info_list
        self.name = name
        self.remarks = remarks
        self.type = type

    def validate(self):
        if self.morse_info_list:
            for k in self.morse_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.data_set_ids is not None:
            result['dataSetIds'] = self.data_set_ids
        result['morseInfoList'] = []
        if self.morse_info_list is not None:
            for k in self.morse_info_list:
                result['morseInfoList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('dataSetIds') is not None:
            self.data_set_ids = m.get('dataSetIds')
        self.morse_info_list = []
        if m.get('morseInfoList') is not None:
            for k in m.get('morseInfoList'):
                temp_model = CreateComputeTaskRequestMorseInfoList()
                self.morse_info_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateComputeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateComputeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateComputeTaskResponseBody = None,
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
            temp_model = CreateComputeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateComputeTask2RequestMorseInfoList(TeaModel):
    def __init__(
        self,
        cu_id: str = None,
        cu_version: str = None,
    ):
        self.cu_id = cu_id
        self.cu_version = cu_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_id is not None:
            result['cuId'] = self.cu_id
        if self.cu_version is not None:
            result['cuVersion'] = self.cu_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuId') is not None:
            self.cu_id = m.get('cuId')
        if m.get('cuVersion') is not None:
            self.cu_version = m.get('cuVersion')
        return self


class CreateComputeTask2Request(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        client_id: int = None,
        data_set_ids: str = None,
        morse_info_list: List[CreateComputeTask2RequestMorseInfoList] = None,
        name: str = None,
        remarks: str = None,
        task_source: str = None,
        type: str = None,
    ):
        self.app_id = app_id
        self.client_id = client_id
        self.data_set_ids = data_set_ids
        self.morse_info_list = morse_info_list
        self.name = name
        self.remarks = remarks
        self.task_source = task_source
        self.type = type

    def validate(self):
        if self.morse_info_list:
            for k in self.morse_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.data_set_ids is not None:
            result['dataSetIds'] = self.data_set_ids
        result['morseInfoList'] = []
        if self.morse_info_list is not None:
            for k in self.morse_info_list:
                result['morseInfoList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.task_source is not None:
            result['taskSource'] = self.task_source
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('dataSetIds') is not None:
            self.data_set_ids = m.get('dataSetIds')
        self.morse_info_list = []
        if m.get('morseInfoList') is not None:
            for k in m.get('morseInfoList'):
                temp_model = CreateComputeTask2RequestMorseInfoList()
                self.morse_info_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('taskSource') is not None:
            self.task_source = m.get('taskSource')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateComputeTask2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateComputeTask2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateComputeTask2ResponseBody = None,
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
            temp_model = CreateComputeTask2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSetRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataSetResponseBody = None,
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
            temp_model = CreateDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSet2Request(TeaModel):
    def __init__(
        self,
        client_id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.client_id = client_id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateDataSet2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDataSet2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataSet2ResponseBody = None,
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
            temp_model = CreateDataSet2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKnowLedgeRequestBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        internal_knowledge_id: str = None,
        knowledge_name: str = None,
    ):
        self.app_id = app_id
        self.internal_knowledge_id = internal_knowledge_id
        self.knowledge_name = knowledge_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.internal_knowledge_id is not None:
            result['internalKnowledgeId'] = self.internal_knowledge_id
        if self.knowledge_name is not None:
            result['knowledgeName'] = self.knowledge_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('internalKnowledgeId') is not None:
            self.internal_knowledge_id = m.get('internalKnowledgeId')
        if m.get('knowledgeName') is not None:
            self.knowledge_name = m.get('knowledgeName')
        return self


class CreateKnowLedgeRequest(TeaModel):
    def __init__(
        self,
        body: CreateKnowLedgeRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateKnowLedgeRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKnowLedgeShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class CreateKnowLedgeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateKnowLedgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKnowLedgeResponseBody = None,
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
            temp_model = CreateKnowLedgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncryptInvokeRequest(TeaModel):
    def __init__(
        self,
        client_id: int = None,
        data: str = None,
        encrypt_key: str = None,
        method_name: str = None,
        sign: str = None,
    ):
        self.client_id = client_id
        self.data = data
        self.encrypt_key = encrypt_key
        self.method_name = method_name
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.data is not None:
            result['data'] = self.data
        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.sign is not None:
            result['sign'] = self.sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('sign') is not None:
            self.sign = m.get('sign')
        return self


class EncryptInvokeResponseBodyData(TeaModel):
    def __init__(
        self,
        encrypt_data: str = None,
        encrypt_key: str = None,
        sign: str = None,
    ):
        self.encrypt_data = encrypt_data
        self.encrypt_key = encrypt_key
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_data is not None:
            result['encryptData'] = self.encrypt_data
        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key
        if self.sign is not None:
            result['sign'] = self.sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encryptData') is not None:
            self.encrypt_data = m.get('encryptData')
        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')
        if m.get('sign') is not None:
            self.sign = m.get('sign')
        return self


class EncryptInvokeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: EncryptInvokeResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = EncryptInvokeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EncryptInvokeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EncryptInvokeResponseBody = None,
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
            temp_model = EncryptInvokeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCrowdDatasetRequestBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        return self


class GetCrowdDatasetRequest(TeaModel):
    def __init__(
        self,
        body: GetCrowdDatasetRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = GetCrowdDatasetRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCrowdDatasetShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class GetCrowdDatasetResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        crowd_dataset_id: str = None,
        dataset_ids: str = None,
        description: str = None,
        name: str = None,
        upload_status: str = None,
    ):
        self.app_id = app_id
        self.crowd_dataset_id = crowd_dataset_id
        self.dataset_ids = dataset_ids
        self.description = description
        self.name = name
        self.upload_status = upload_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.crowd_dataset_id is not None:
            result['crowdDatasetId'] = self.crowd_dataset_id
        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.upload_status is not None:
            result['uploadStatus'] = self.upload_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('crowdDatasetId') is not None:
            self.crowd_dataset_id = m.get('crowdDatasetId')
        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uploadStatus') is not None:
            self.upload_status = m.get('uploadStatus')
        return self


class GetCrowdDatasetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCrowdDatasetResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = GetCrowdDatasetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCrowdDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCrowdDatasetResponseBody = None,
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
            temp_model = GetCrowdDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKnowledgeDataRequestBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        knowledge_id_list: List[str] = None,
    ):
        self.app_id = app_id
        self.knowledge_id_list = knowledge_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.knowledge_id_list is not None:
            result['knowledgeIdList'] = self.knowledge_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('knowledgeIdList') is not None:
            self.knowledge_id_list = m.get('knowledgeIdList')
        return self


class GetKnowledgeDataRequest(TeaModel):
    def __init__(
        self,
        body: GetKnowledgeDataRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = GetKnowledgeDataRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKnowledgeDataShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class GetKnowledgeDataResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        internal_knowledge_id: str = None,
        knowledge_name: str = None,
        message: str = None,
        status: str = None,
    ):
        self.app_id = app_id
        self.internal_knowledge_id = internal_knowledge_id
        self.knowledge_name = knowledge_name
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.internal_knowledge_id is not None:
            result['internalKnowledgeId'] = self.internal_knowledge_id
        if self.knowledge_name is not None:
            result['knowledgeName'] = self.knowledge_name
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('internalKnowledgeId') is not None:
            self.internal_knowledge_id = m.get('internalKnowledgeId')
        if m.get('knowledgeName') is not None:
            self.knowledge_name = m.get('knowledgeName')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetKnowledgeDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetKnowledgeDataResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
                temp_model = GetKnowledgeDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetKnowledgeDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKnowledgeDataResponseBody = None,
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
            temp_model = GetKnowledgeDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetYzdInstanceTaskResultRequestBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        range_time_end_time: str = None,
        range_time_start_time: str = None,
    ):
        self.app_id = app_id
        self.range_time_end_time = range_time_end_time
        self.range_time_start_time = range_time_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.range_time_end_time is not None:
            result['rangeTimeEndTime'] = self.range_time_end_time
        if self.range_time_start_time is not None:
            result['rangeTimeStartTime'] = self.range_time_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('rangeTimeEndTime') is not None:
            self.range_time_end_time = m.get('rangeTimeEndTime')
        if m.get('rangeTimeStartTime') is not None:
            self.range_time_start_time = m.get('rangeTimeStartTime')
        return self


class GetYzdInstanceTaskResultRequest(TeaModel):
    def __init__(
        self,
        body: GetYzdInstanceTaskResultRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = GetYzdInstanceTaskResultRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetYzdInstanceTaskResultShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class GetYzdInstanceTaskResultResponseBodyDataDownloadUrls(TeaModel):
    def __init__(
        self,
        pwd: str = None,
        url: str = None,
    ):
        self.pwd = pwd
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pwd is not None:
            result['pwd'] = self.pwd
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pwd') is not None:
            self.pwd = m.get('pwd')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetYzdInstanceTaskResultResponseBodyData(TeaModel):
    def __init__(
        self,
        appid: str = None,
        bcid: str = None,
        dataset_ids: str = None,
        download_urls: List[GetYzdInstanceTaskResultResponseBodyDataDownloadUrls] = None,
        result_cnt: str = None,
        status: str = None,
        time_duration: str = None,
    ):
        self.appid = appid
        self.bcid = bcid
        self.dataset_ids = dataset_ids
        self.download_urls = download_urls
        self.result_cnt = result_cnt
        self.status = status
        self.time_duration = time_duration

    def validate(self):
        if self.download_urls:
            for k in self.download_urls:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appid is not None:
            result['appid'] = self.appid
        if self.bcid is not None:
            result['bcid'] = self.bcid
        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids
        result['downloadUrls'] = []
        if self.download_urls is not None:
            for k in self.download_urls:
                result['downloadUrls'].append(k.to_map() if k else None)
        if self.result_cnt is not None:
            result['resultCnt'] = self.result_cnt
        if self.status is not None:
            result['status'] = self.status
        if self.time_duration is not None:
            result['timeDuration'] = self.time_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appid') is not None:
            self.appid = m.get('appid')
        if m.get('bcid') is not None:
            self.bcid = m.get('bcid')
        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')
        self.download_urls = []
        if m.get('downloadUrls') is not None:
            for k in m.get('downloadUrls'):
                temp_model = GetYzdInstanceTaskResultResponseBodyDataDownloadUrls()
                self.download_urls.append(temp_model.from_map(k))
        if m.get('resultCnt') is not None:
            self.result_cnt = m.get('resultCnt')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timeDuration') is not None:
            self.time_duration = m.get('timeDuration')
        return self


class GetYzdInstanceTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        code: bool = None,
        data: List[GetYzdInstanceTaskResultResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
                temp_model = GetYzdInstanceTaskResultResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetYzdInstanceTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetYzdInstanceTaskResultResponseBody = None,
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
            temp_model = GetYzdInstanceTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetYzdStsAKResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        bucket: str = None,
        endpoint: str = None,
        id: str = None,
        internal_knowledge_id: str = None,
        path: str = None,
        secret: str = None,
        token: str = None,
    ):
        self.app_id = app_id
        self.bucket = bucket
        self.endpoint = endpoint
        self.id = id
        self.internal_knowledge_id = internal_knowledge_id
        self.path = path
        self.secret = secret
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.id is not None:
            result['id'] = self.id
        if self.internal_knowledge_id is not None:
            result['internalKnowledgeId'] = self.internal_knowledge_id
        if self.path is not None:
            result['path'] = self.path
        if self.secret is not None:
            result['secret'] = self.secret
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('internalKnowledgeId') is not None:
            self.internal_knowledge_id = m.get('internalKnowledgeId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetYzdStsAKResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetYzdStsAKResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = GetYzdStsAKResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetYzdStsAKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetYzdStsAKResponseBody = None,
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
            temp_model = GetYzdStsAKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComputeTaskResponseBodyDataTaskResultList(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
        code: int = None,
        line_num: int = None,
    ):
        self.bc_id = bc_id
        self.code = code
        self.line_num = line_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.code is not None:
            result['code'] = self.code
        if self.line_num is not None:
            result['lineNum'] = self.line_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')
        return self


class ListComputeTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        bc_id: int = None,
        compute_oss_file_title: str = None,
        dataset_ids: str = None,
        ext_info: str = None,
        file_num: int = None,
        name: str = None,
        remarks: str = None,
        status: str = None,
        task_result_list: List[ListComputeTaskResponseBodyDataTaskResultList] = None,
    ):
        self.app_id = app_id
        self.bc_id = bc_id
        self.compute_oss_file_title = compute_oss_file_title
        self.dataset_ids = dataset_ids
        self.ext_info = ext_info
        self.file_num = file_num
        self.name = name
        self.remarks = remarks
        self.status = status
        self.task_result_list = task_result_list

    def validate(self):
        if self.task_result_list:
            for k in self.task_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.compute_oss_file_title is not None:
            result['computeOssFileTitle'] = self.compute_oss_file_title
        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.file_num is not None:
            result['fileNum'] = self.file_num
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.status is not None:
            result['status'] = self.status
        result['taskResultList'] = []
        if self.task_result_list is not None:
            for k in self.task_result_list:
                result['taskResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('computeOssFileTitle') is not None:
            self.compute_oss_file_title = m.get('computeOssFileTitle')
        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.task_result_list = []
        if m.get('taskResultList') is not None:
            for k in m.get('taskResultList'):
                temp_model = ListComputeTaskResponseBodyDataTaskResultList()
                self.task_result_list.append(temp_model.from_map(k))
        return self


class ListComputeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListComputeTaskResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
                temp_model = ListComputeTaskResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListComputeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListComputeTaskResponseBody = None,
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
            temp_model = ListComputeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComputeTask2Request(TeaModel):
    def __init__(
        self,
        client_id: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.client_id = client_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.page_num is not None:
            result['pageNum'] = self.page_num
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListComputeTask2ResponseBodyDataDataTaskResultList(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
        code: int = None,
        line_num: int = None,
    ):
        self.bc_id = bc_id
        self.code = code
        self.line_num = line_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.code is not None:
            result['code'] = self.code
        if self.line_num is not None:
            result['lineNum'] = self.line_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')
        return self


class ListComputeTask2ResponseBodyDataData(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        bc_id: int = None,
        compute_oss_file_title: str = None,
        dataset_ids: str = None,
        ext_info: str = None,
        file_num: int = None,
        name: str = None,
        remarks: str = None,
        status: str = None,
        task_result_list: List[ListComputeTask2ResponseBodyDataDataTaskResultList] = None,
    ):
        self.app_id = app_id
        self.bc_id = bc_id
        self.compute_oss_file_title = compute_oss_file_title
        self.dataset_ids = dataset_ids
        self.ext_info = ext_info
        self.file_num = file_num
        self.name = name
        self.remarks = remarks
        self.status = status
        self.task_result_list = task_result_list

    def validate(self):
        if self.task_result_list:
            for k in self.task_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.compute_oss_file_title is not None:
            result['computeOssFileTitle'] = self.compute_oss_file_title
        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.file_num is not None:
            result['fileNum'] = self.file_num
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.status is not None:
            result['status'] = self.status
        result['taskResultList'] = []
        if self.task_result_list is not None:
            for k in self.task_result_list:
                result['taskResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('computeOssFileTitle') is not None:
            self.compute_oss_file_title = m.get('computeOssFileTitle')
        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.task_result_list = []
        if m.get('taskResultList') is not None:
            for k in m.get('taskResultList'):
                temp_model = ListComputeTask2ResponseBodyDataDataTaskResultList()
                self.task_result_list.append(temp_model.from_map(k))
        return self


class ListComputeTask2ResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[ListComputeTask2ResponseBodyDataData] = None,
        total_num: int = None,
    ):
        self.data = data
        self.total_num = total_num

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
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListComputeTask2ResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        return self


class ListComputeTask2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListComputeTask2ResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = ListComputeTask2ResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListComputeTask2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListComputeTask2ResponseBody = None,
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
            temp_model = ListComputeTask2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSetResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_id: int = None,
        line_num: int = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.dataset_id = dataset_id
        self.line_num = line_num
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.line_num is not None:
            result['lineNum'] = self.line_num
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListDataSetResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
                temp_model = ListDataSetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSetResponseBody = None,
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
            temp_model = ListDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSet2Request(TeaModel):
    def __init__(
        self,
        client_id: int = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.client_id = client_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDataSet2ResponseBodyDataData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_id: int = None,
        line_num: int = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.dataset_id = dataset_id
        self.line_num = line_num
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.line_num is not None:
            result['lineNum'] = self.line_num
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDataSet2ResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[ListDataSet2ResponseBodyDataData] = None,
        total_num: int = None,
    ):
        self.data = data
        self.total_num = total_num

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
        if self.total_num is not None:
            result['totalNum'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListDataSet2ResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('totalNum') is not None:
            self.total_num = m.get('totalNum')
        return self


class ListDataSet2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListDataSet2ResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = ListDataSet2ResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDataSet2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSet2ResponseBody = None,
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
            temp_model = ListDataSet2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDataSetRequest(TeaModel):
    def __init__(
        self,
        body: int = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class RemoveDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveDataSetResponseBody = None,
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
            temp_model = RemoveDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDataSet2Request(TeaModel):
    def __init__(
        self,
        client_id: int = None,
        data_set_id: int = None,
    ):
        self.client_id = client_id
        self.data_set_id = data_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.data_set_id is not None:
            result['dataSetId'] = self.data_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('dataSetId') is not None:
            self.data_set_id = m.get('dataSetId')
        return self


class RemoveDataSet2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveDataSet2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveDataSet2ResponseBody = None,
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
            temp_model = RemoveDataSet2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveCrowdDatasetAndBindingDatasetRequestBody(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        dataset_ids: List[str] = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.dataset_ids = dataset_ids
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class SaveCrowdDatasetAndBindingDatasetRequest(TeaModel):
    def __init__(
        self,
        body: SaveCrowdDatasetAndBindingDatasetRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SaveCrowdDatasetAndBindingDatasetRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveCrowdDatasetAndBindingDatasetShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class SaveCrowdDatasetAndBindingDatasetResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        crowd_dataset_id: str = None,
        dataset_ids: List[str] = None,
        description: str = None,
        name: str = None,
        upload_status: str = None,
    ):
        self.app_id = app_id
        self.crowd_dataset_id = crowd_dataset_id
        self.dataset_ids = dataset_ids
        self.description = description
        self.name = name
        self.upload_status = upload_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.crowd_dataset_id is not None:
            result['crowdDatasetId'] = self.crowd_dataset_id
        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.upload_status is not None:
            result['uploadStatus'] = self.upload_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('crowdDatasetId') is not None:
            self.crowd_dataset_id = m.get('crowdDatasetId')
        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('uploadStatus') is not None:
            self.upload_status = m.get('uploadStatus')
        return self


class SaveCrowdDatasetAndBindingDatasetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SaveCrowdDatasetAndBindingDatasetResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = SaveCrowdDatasetAndBindingDatasetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveCrowdDatasetAndBindingDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveCrowdDatasetAndBindingDatasetResponseBody = None,
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
            temp_model = SaveCrowdDatasetAndBindingDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectComputeTaskRequest(TeaModel):
    def __init__(
        self,
        body: int = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class SelectComputeTaskResponseBodyDataExportOssFileList(TeaModel):
    def __init__(
        self,
        down_load_url: str = None,
        password: str = None,
    ):
        self.down_load_url = down_load_url
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_load_url is not None:
            result['downLoadUrl'] = self.down_load_url
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downLoadUrl') is not None:
            self.down_load_url = m.get('downLoadUrl')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self


class SelectComputeTaskResponseBodyDataTaskResultList(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
        code: int = None,
        line_num: int = None,
    ):
        self.bc_id = bc_id
        self.code = code
        self.line_num = line_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.code is not None:
            result['code'] = self.code
        if self.line_num is not None:
            result['lineNum'] = self.line_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')
        return self


class SelectComputeTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        bc_id: int = None,
        compute_oss_file_title: str = None,
        dataset_ids: str = None,
        export_oss_file_list: List[SelectComputeTaskResponseBodyDataExportOssFileList] = None,
        ext_info: str = None,
        file_num: int = None,
        name: str = None,
        remarks: str = None,
        status: str = None,
        task_result_list: List[SelectComputeTaskResponseBodyDataTaskResultList] = None,
    ):
        self.app_id = app_id
        self.bc_id = bc_id
        self.compute_oss_file_title = compute_oss_file_title
        self.dataset_ids = dataset_ids
        self.export_oss_file_list = export_oss_file_list
        self.ext_info = ext_info
        self.file_num = file_num
        self.name = name
        self.remarks = remarks
        self.status = status
        self.task_result_list = task_result_list

    def validate(self):
        if self.export_oss_file_list:
            for k in self.export_oss_file_list:
                if k:
                    k.validate()
        if self.task_result_list:
            for k in self.task_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.compute_oss_file_title is not None:
            result['computeOssFileTitle'] = self.compute_oss_file_title
        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids
        result['exportOssFileList'] = []
        if self.export_oss_file_list is not None:
            for k in self.export_oss_file_list:
                result['exportOssFileList'].append(k.to_map() if k else None)
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.file_num is not None:
            result['fileNum'] = self.file_num
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.status is not None:
            result['status'] = self.status
        result['taskResultList'] = []
        if self.task_result_list is not None:
            for k in self.task_result_list:
                result['taskResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('computeOssFileTitle') is not None:
            self.compute_oss_file_title = m.get('computeOssFileTitle')
        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')
        self.export_oss_file_list = []
        if m.get('exportOssFileList') is not None:
            for k in m.get('exportOssFileList'):
                temp_model = SelectComputeTaskResponseBodyDataExportOssFileList()
                self.export_oss_file_list.append(temp_model.from_map(k))
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.task_result_list = []
        if m.get('taskResultList') is not None:
            for k in m.get('taskResultList'):
                temp_model = SelectComputeTaskResponseBodyDataTaskResultList()
                self.task_result_list.append(temp_model.from_map(k))
        return self


class SelectComputeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SelectComputeTaskResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = SelectComputeTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectComputeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SelectComputeTaskResponseBody = None,
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
            temp_model = SelectComputeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectComputeTask2Request(TeaModel):
    def __init__(
        self,
        bc_confirm: bool = None,
        bc_id: int = None,
        client_id: int = None,
    ):
        self.bc_confirm = bc_confirm
        self.bc_id = bc_id
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_confirm is not None:
            result['bcConfirm'] = self.bc_confirm
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.client_id is not None:
            result['clientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcConfirm') is not None:
            self.bc_confirm = m.get('bcConfirm')
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        return self


class SelectComputeTask2ResponseBodyDataExportOssFileList(TeaModel):
    def __init__(
        self,
        down_load_url: str = None,
        password: str = None,
    ):
        self.down_load_url = down_load_url
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.down_load_url is not None:
            result['downLoadUrl'] = self.down_load_url
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downLoadUrl') is not None:
            self.down_load_url = m.get('downLoadUrl')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self


class SelectComputeTask2ResponseBodyDataTaskResultList(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
        code: int = None,
        line_num: int = None,
    ):
        self.bc_id = bc_id
        self.code = code
        self.line_num = line_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.code is not None:
            result['code'] = self.code
        if self.line_num is not None:
            result['lineNum'] = self.line_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')
        return self


class SelectComputeTask2ResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        bc_id: int = None,
        compute_oss_file_title: str = None,
        dataset_ids: str = None,
        export_oss_file_list: List[SelectComputeTask2ResponseBodyDataExportOssFileList] = None,
        ext_info: str = None,
        file_num: int = None,
        hint: str = None,
        name: str = None,
        remarks: str = None,
        status: str = None,
        task_result_list: List[SelectComputeTask2ResponseBodyDataTaskResultList] = None,
    ):
        self.app_id = app_id
        self.bc_id = bc_id
        self.compute_oss_file_title = compute_oss_file_title
        self.dataset_ids = dataset_ids
        self.export_oss_file_list = export_oss_file_list
        self.ext_info = ext_info
        self.file_num = file_num
        self.hint = hint
        self.name = name
        self.remarks = remarks
        self.status = status
        self.task_result_list = task_result_list

    def validate(self):
        if self.export_oss_file_list:
            for k in self.export_oss_file_list:
                if k:
                    k.validate()
        if self.task_result_list:
            for k in self.task_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.compute_oss_file_title is not None:
            result['computeOssFileTitle'] = self.compute_oss_file_title
        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids
        result['exportOssFileList'] = []
        if self.export_oss_file_list is not None:
            for k in self.export_oss_file_list:
                result['exportOssFileList'].append(k.to_map() if k else None)
        if self.ext_info is not None:
            result['extInfo'] = self.ext_info
        if self.file_num is not None:
            result['fileNum'] = self.file_num
        if self.hint is not None:
            result['hint'] = self.hint
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.status is not None:
            result['status'] = self.status
        result['taskResultList'] = []
        if self.task_result_list is not None:
            for k in self.task_result_list:
                result['taskResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('computeOssFileTitle') is not None:
            self.compute_oss_file_title = m.get('computeOssFileTitle')
        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')
        self.export_oss_file_list = []
        if m.get('exportOssFileList') is not None:
            for k in m.get('exportOssFileList'):
                temp_model = SelectComputeTask2ResponseBodyDataExportOssFileList()
                self.export_oss_file_list.append(temp_model.from_map(k))
        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')
        if m.get('fileNum') is not None:
            self.file_num = m.get('fileNum')
        if m.get('hint') is not None:
            self.hint = m.get('hint')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.task_result_list = []
        if m.get('taskResultList') is not None:
            for k in m.get('taskResultList'):
                temp_model = SelectComputeTask2ResponseBodyDataTaskResultList()
                self.task_result_list.append(temp_model.from_map(k))
        return self


class SelectComputeTask2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SelectComputeTask2ResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = SelectComputeTask2ResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectComputeTask2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SelectComputeTask2ResponseBody = None,
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
            temp_model = SelectComputeTask2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectDataSetRequest(TeaModel):
    def __init__(
        self,
        body: int = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class SelectDataSetResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_id: int = None,
        line_num: int = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.dataset_id = dataset_id
        self.line_num = line_num
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.line_num is not None:
            result['lineNum'] = self.line_num
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SelectDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SelectDataSetResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = SelectDataSetResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SelectDataSetResponseBody = None,
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
            temp_model = SelectDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SelectDataSet2Request(TeaModel):
    def __init__(
        self,
        client_id: int = None,
        data_set_id: int = None,
    ):
        self.client_id = client_id
        self.data_set_id = data_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.data_set_id is not None:
            result['dataSetId'] = self.data_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('dataSetId') is not None:
            self.data_set_id = m.get('dataSetId')
        return self


class SelectDataSet2ResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dataset_id: int = None,
        line_num: int = None,
        name: str = None,
        oss_file_count: int = None,
        status: str = None,
        status_msg: str = None,
        type: str = None,
    ):
        self.create_time = create_time
        self.dataset_id = dataset_id
        self.line_num = line_num
        self.name = name
        self.oss_file_count = oss_file_count
        self.status = status
        self.status_msg = status_msg
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.line_num is not None:
            result['lineNum'] = self.line_num
        if self.name is not None:
            result['name'] = self.name
        if self.oss_file_count is not None:
            result['ossFileCount'] = self.oss_file_count
        if self.status is not None:
            result['status'] = self.status
        if self.status_msg is not None:
            result['statusMsg'] = self.status_msg
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('lineNum') is not None:
            self.line_num = m.get('lineNum')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ossFileCount') is not None:
            self.oss_file_count = m.get('ossFileCount')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusMsg') is not None:
            self.status_msg = m.get('statusMsg')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SelectDataSet2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SelectDataSet2ResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
            temp_model = SelectDataSet2ResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SelectDataSet2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SelectDataSet2ResponseBody = None,
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
            temp_model = SelectDataSet2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDataSetTaskRequest(TeaModel):
    def __init__(
        self,
        body: int = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class SubmitDataSetTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitDataSetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDataSetTaskResponseBody = None,
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
            temp_model = SubmitDataSetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDataSetTask2Request(TeaModel):
    def __init__(
        self,
        client_id: int = None,
        data_set_id: int = None,
    ):
        self.client_id = client_id
        self.data_set_id = data_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['clientId'] = self.client_id
        if self.data_set_id is not None:
            result['dataSetId'] = self.data_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientId') is not None:
            self.client_id = m.get('clientId')
        if m.get('dataSetId') is not None:
            self.data_set_id = m.get('dataSetId')
        return self


class SubmitDataSetTask2ResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitDataSetTask2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDataSetTask2ResponseBody = None,
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
            temp_model = SubmitDataSetTask2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateKnowLedgeRequest(TeaModel):
    def __init__(
        self,
        body: List[str] = None,
    ):
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class ValidateKnowLedgeShrinkRequest(TeaModel):
    def __init__(
        self,
        body_shrink: str = None,
    ):
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class ValidateKnowLedgeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['Msg'] = self.msg
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
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidateKnowLedgeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateKnowLedgeResponseBody = None,
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
            temp_model = ValidateKnowLedgeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


