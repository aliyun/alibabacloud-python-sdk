# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class BatchContentAsyncDetectRequestServiceParameterList(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class BatchContentAsyncDetectRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
        service_parameter_list: List[BatchContentAsyncDetectRequestServiceParameterList] = None,
    ):
        self.region_id = region_id
        self.scene_name = scene_name
        self.service_name = service_name
        self.service_parameter_list = service_parameter_list

    def validate(self):
        if self.service_parameter_list:
            for k in self.service_parameter_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        result['serviceParameterList'] = []
        if self.service_parameter_list is not None:
            for k in self.service_parameter_list:
                result['serviceParameterList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        self.service_parameter_list = []
        if m.get('serviceParameterList') is not None:
            for k in m.get('serviceParameterList'):
                temp_model = BatchContentAsyncDetectRequestServiceParameterList()
                self.service_parameter_list.append(temp_model.from_map(k))
        return self


class BatchContentAsyncDetectResponseBodyData(TeaModel):
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
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BatchContentAsyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchContentAsyncDetectResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = BatchContentAsyncDetectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchContentAsyncDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchContentAsyncDetectResponseBody = None,
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
            temp_model = BatchContentAsyncDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchContentSyncDetectRequestServiceParameterList(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class BatchContentSyncDetectRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
        service_parameter_list: List[BatchContentSyncDetectRequestServiceParameterList] = None,
    ):
        self.region_id = region_id
        self.scene_name = scene_name
        self.service_name = service_name
        self.service_parameter_list = service_parameter_list

    def validate(self):
        if self.service_parameter_list:
            for k in self.service_parameter_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        result['serviceParameterList'] = []
        if self.service_parameter_list is not None:
            for k in self.service_parameter_list:
                result['serviceParameterList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        self.service_parameter_list = []
        if m.get('serviceParameterList') is not None:
            for k in m.get('serviceParameterList'):
                temp_model = BatchContentSyncDetectRequestServiceParameterList()
                self.service_parameter_list.append(temp_model.from_map(k))
        return self


class BatchContentSyncDetectResponseBodyDataDetectResultList(TeaModel):
    def __init__(
        self,
        risk_info: str = None,
        risk_result: int = None,
    ):
        self.risk_info = risk_info
        self.risk_result = risk_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskInfo') is not None:
            self.risk_info = m.get('RiskInfo')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class BatchContentSyncDetectResponseBodyData(TeaModel):
    def __init__(
        self,
        detect_result_list: List[BatchContentSyncDetectResponseBodyDataDetectResultList] = None,
    ):
        self.detect_result_list = detect_result_list

    def validate(self):
        if self.detect_result_list:
            for k in self.detect_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetectResultList'] = []
        if self.detect_result_list is not None:
            for k in self.detect_result_list:
                result['DetectResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detect_result_list = []
        if m.get('DetectResultList') is not None:
            for k in m.get('DetectResultList'):
                temp_model = BatchContentSyncDetectResponseBodyDataDetectResultList()
                self.detect_result_list.append(temp_model.from_map(k))
        return self


class BatchContentSyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BatchContentSyncDetectResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = BatchContentSyncDetectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchContentSyncDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchContentSyncDetectResponseBody = None,
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
            temp_model = BatchContentSyncDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAccountRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        check_result: int = None,
    ):
        self.check_result = check_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        return self


class CheckAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CheckAccountResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = CheckAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAccountResponseBody = None,
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
            temp_model = CheckAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContentAsyncDetectRequestServiceParameter(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class ContentAsyncDetectRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
        service_parameter: ContentAsyncDetectRequestServiceParameter = None,
    ):
        self.region_id = region_id
        self.scene_name = scene_name
        self.service_name = service_name
        self.service_parameter = service_parameter

    def validate(self):
        if self.service_parameter:
            self.service_parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_parameter is not None:
            result['serviceParameter'] = self.service_parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('serviceParameter') is not None:
            temp_model = ContentAsyncDetectRequestServiceParameter()
            self.service_parameter = temp_model.from_map(m['serviceParameter'])
        return self


class ContentAsyncDetectResponseBodyData(TeaModel):
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
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ContentAsyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ContentAsyncDetectResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = ContentAsyncDetectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ContentAsyncDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContentAsyncDetectResponseBody = None,
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
            temp_model = ContentAsyncDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContentSyncDetectRequestServiceParameter(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class ContentSyncDetectRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
        service_parameter: ContentSyncDetectRequestServiceParameter = None,
    ):
        self.region_id = region_id
        self.scene_name = scene_name
        self.service_name = service_name
        self.service_parameter = service_parameter

    def validate(self):
        if self.service_parameter:
            self.service_parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_parameter is not None:
            result['serviceParameter'] = self.service_parameter.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('serviceParameter') is not None:
            temp_model = ContentSyncDetectRequestServiceParameter()
            self.service_parameter = temp_model.from_map(m['serviceParameter'])
        return self


class ContentSyncDetectResponseBodyData(TeaModel):
    def __init__(
        self,
        risk_info: str = None,
        risk_result: int = None,
    ):
        self.risk_info = risk_info
        self.risk_result = risk_result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskInfo') is not None:
            self.risk_info = m.get('RiskInfo')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class ContentSyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ContentSyncDetectResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = ContentSyncDetectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ContentSyncDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContentSyncDetectResponseBody = None,
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
            temp_model = ContentSyncDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModelInstanceRequest(TeaModel):
    def __init__(
        self,
        eas_service_id: str = None,
        eas_service_name: str = None,
        model_call_name: str = None,
        model_category_id: int = None,
        model_token: str = None,
        model_url: str = None,
        model_vpc_url: str = None,
        workspace_id: int = None,
    ):
        self.eas_service_id = eas_service_id
        self.eas_service_name = eas_service_name
        self.model_call_name = model_call_name
        self.model_category_id = model_category_id
        # EAS Token
        self.model_token = model_token
        self.model_url = model_url
        self.model_vpc_url = model_vpc_url
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eas_service_id is not None:
            result['EasServiceId'] = self.eas_service_id
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.model_call_name is not None:
            result['ModelCallName'] = self.model_call_name
        if self.model_category_id is not None:
            result['ModelCategoryId'] = self.model_category_id
        if self.model_token is not None:
            result['ModelToken'] = self.model_token
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.model_vpc_url is not None:
            result['ModelVpcUrl'] = self.model_vpc_url
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EasServiceId') is not None:
            self.eas_service_id = m.get('EasServiceId')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('ModelCallName') is not None:
            self.model_call_name = m.get('ModelCallName')
        if m.get('ModelCategoryId') is not None:
            self.model_category_id = m.get('ModelCategoryId')
        if m.get('ModelToken') is not None:
            self.model_token = m.get('ModelToken')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModelVpcUrl') is not None:
            self.model_vpc_url = m.get('ModelVpcUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateModelInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        model_instance_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.model_instance_id = model_instance_id
        # Id of the request
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateModelInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModelInstanceResponseBody = None,
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
            temp_model = CreateModelInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequestHarmfulCategoryConfigInfoList(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_label: str = None,
        category_type: int = None,
        input_output_type: int = None,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category ID
        self.category_id = category_id
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type
        # Whether it is enabled
        # 0: Not enabled
        # 1: Enabled
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class CreatePolicyRequestPromptAttackInfo(TeaModel):
    def __init__(
        self,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Prompt attack configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class CreatePolicyRequestPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_label: str = None,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category ID
        self.category_id = category_id
        # Category name
        self.category_label = category_label
        # Prompt attack configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class CreatePolicyRequestRegularExpressList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        regular_express: str = None,
        regular_express_name: str = None,
    ):
        self.action_type = action_type
        self.regular_express = regular_express
        self.regular_express_name = regular_express_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.regular_express is not None:
            result['RegularExpress'] = self.regular_express
        if self.regular_express_name is not None:
            result['RegularExpressName'] = self.regular_express_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('RegularExpress') is not None:
            self.regular_express = m.get('RegularExpress')
        if m.get('RegularExpressName') is not None:
            self.regular_express_name = m.get('RegularExpressName')
        return self


class CreatePolicyRequestSensitiveConfigList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        is_enabled: int = None,
        sensitive_config_id: int = None,
    ):
        self.action_type = action_type
        self.is_enabled = is_enabled
        self.sensitive_config_id = sensitive_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.sensitive_config_id is not None:
            result['SensitiveConfigId'] = self.sensitive_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SensitiveConfigId') is not None:
            self.sensitive_config_id = m.get('SensitiveConfigId')
        return self


class CreatePolicyRequestSensitiveTopicListTopicExampleInfoList(TeaModel):
    def __init__(
        self,
        content: str = None,
        example_type: int = None,
    ):
        self.content = content
        self.example_type = example_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.example_type is not None:
            result['ExampleType'] = self.example_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExampleType') is not None:
            self.example_type = m.get('ExampleType')
        return self


class CreatePolicyRequestSensitiveTopicList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        security_level: int = None,
        topic_definition: str = None,
        topic_example_info_list: List[CreatePolicyRequestSensitiveTopicListTopicExampleInfoList] = None,
        topic_name: str = None,
    ):
        self.category_type = category_type
        self.security_level = security_level
        self.topic_definition = topic_definition
        self.topic_example_info_list = topic_example_info_list
        self.topic_name = topic_name

    def validate(self):
        if self.topic_example_info_list:
            for k in self.topic_example_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        result['TopicExampleInfoList'] = []
        if self.topic_example_info_list is not None:
            for k in self.topic_example_info_list:
                result['TopicExampleInfoList'].append(k.to_map() if k else None)
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        self.topic_example_info_list = []
        if m.get('TopicExampleInfoList') is not None:
            for k in m.get('TopicExampleInfoList'):
                temp_model = CreatePolicyRequestSensitiveTopicListTopicExampleInfoList()
                self.topic_example_info_list.append(temp_model.from_map(k))
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class CreatePolicyRequestSensitiveWordList(TeaModel):
    def __init__(
        self,
        label: str = None,
        word: str = None,
    ):
        self.label = label
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class CreatePolicyRequestTopicConfigInfoList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        input_output_type: int = None,
        security_level: int = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Sensitive topic ID
        self.topic_id = topic_id
        # Topic Name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class CreatePolicyRequestWordGroupInfoList(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        group_name: str = None,
        input_output_type: int = None,
    ):
        # Keyword group ID.
        self.group_id = group_id
        # Keyword group name
        self.group_name = group_name
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        content_safe_model_instance_id: int = None,
        enable_sensitive_input_check: int = None,
        enable_sensitive_output_check: int = None,
        harmful_category_config_info_list: List[CreatePolicyRequestHarmfulCategoryConfigInfoList] = None,
        input_safe_answer: str = None,
        input_safe_answer_switch: int = None,
        is_sidecar_policy: int = None,
        output_safe_answer: str = None,
        output_safe_answer_switch: int = None,
        policy_name: str = None,
        prompt_attack_info: CreatePolicyRequestPromptAttackInfo = None,
        prompt_attack_info_list: List[CreatePolicyRequestPromptAttackInfoList] = None,
        prompt_attack_model_instance_id: int = None,
        region_id: str = None,
        regular_express_list: List[CreatePolicyRequestRegularExpressList] = None,
        scene_type: int = None,
        sensitive_config_list: List[CreatePolicyRequestSensitiveConfigList] = None,
        sensitive_topic_list: List[CreatePolicyRequestSensitiveTopicList] = None,
        sensitive_topic_model_instance_id: int = None,
        sensitive_word_list: List[CreatePolicyRequestSensitiveWordList] = None,
        topic_config_info_list: List[CreatePolicyRequestTopicConfigInfoList] = None,
        word_group_info_list: List[CreatePolicyRequestWordGroupInfoList] = None,
        workspace_id: int = None,
    ):
        self.content_safe_model_instance_id = content_safe_model_instance_id
        self.enable_sensitive_input_check = enable_sensitive_input_check
        self.enable_sensitive_output_check = enable_sensitive_output_check
        # List of harmful category configurations
        self.harmful_category_config_info_list = harmful_category_config_info_list
        self.input_safe_answer = input_safe_answer
        self.input_safe_answer_switch = input_safe_answer_switch
        self.is_sidecar_policy = is_sidecar_policy
        self.output_safe_answer = output_safe_answer
        self.output_safe_answer_switch = output_safe_answer_switch
        # Detection policy name.
        self.policy_name = policy_name
        # Prompt attack detection result object
        self.prompt_attack_info = prompt_attack_info
        # List of prompt attacks
        self.prompt_attack_info_list = prompt_attack_info_list
        self.prompt_attack_model_instance_id = prompt_attack_model_instance_id
        # Region ID.
        self.region_id = region_id
        self.regular_express_list = regular_express_list
        self.scene_type = scene_type
        self.sensitive_config_list = sensitive_config_list
        self.sensitive_topic_list = sensitive_topic_list
        self.sensitive_topic_model_instance_id = sensitive_topic_model_instance_id
        self.sensitive_word_list = sensitive_word_list
        # List of sensitive topics
        self.topic_config_info_list = topic_config_info_list
        # List of keyword group objects
        self.word_group_info_list = word_group_info_list
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        if self.harmful_category_config_info_list:
            for k in self.harmful_category_config_info_list:
                if k:
                    k.validate()
        if self.prompt_attack_info:
            self.prompt_attack_info.validate()
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()
        if self.regular_express_list:
            for k in self.regular_express_list:
                if k:
                    k.validate()
        if self.sensitive_config_list:
            for k in self.sensitive_config_list:
                if k:
                    k.validate()
        if self.sensitive_topic_list:
            for k in self.sensitive_topic_list:
                if k:
                    k.validate()
        if self.sensitive_word_list:
            for k in self.sensitive_word_list:
                if k:
                    k.validate()
        if self.topic_config_info_list:
            for k in self.topic_config_info_list:
                if k:
                    k.validate()
        if self.word_group_info_list:
            for k in self.word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_safe_model_instance_id is not None:
            result['ContentSafeModelInstanceId'] = self.content_safe_model_instance_id
        if self.enable_sensitive_input_check is not None:
            result['EnableSensitiveInputCheck'] = self.enable_sensitive_input_check
        if self.enable_sensitive_output_check is not None:
            result['EnableSensitiveOutputCheck'] = self.enable_sensitive_output_check
        result['HarmfulCategoryConfigInfoList'] = []
        if self.harmful_category_config_info_list is not None:
            for k in self.harmful_category_config_info_list:
                result['HarmfulCategoryConfigInfoList'].append(k.to_map() if k else None)
        if self.input_safe_answer is not None:
            result['InputSafeAnswer'] = self.input_safe_answer
        if self.input_safe_answer_switch is not None:
            result['InputSafeAnswerSwitch'] = self.input_safe_answer_switch
        if self.is_sidecar_policy is not None:
            result['IsSidecarPolicy'] = self.is_sidecar_policy
        if self.output_safe_answer is not None:
            result['OutputSafeAnswer'] = self.output_safe_answer
        if self.output_safe_answer_switch is not None:
            result['OutputSafeAnswerSwitch'] = self.output_safe_answer_switch
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info.to_map()
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.prompt_attack_model_instance_id is not None:
            result['PromptAttackModelInstanceId'] = self.prompt_attack_model_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RegularExpressList'] = []
        if self.regular_express_list is not None:
            for k in self.regular_express_list:
                result['RegularExpressList'].append(k.to_map() if k else None)
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        result['SensitiveConfigList'] = []
        if self.sensitive_config_list is not None:
            for k in self.sensitive_config_list:
                result['SensitiveConfigList'].append(k.to_map() if k else None)
        result['SensitiveTopicList'] = []
        if self.sensitive_topic_list is not None:
            for k in self.sensitive_topic_list:
                result['SensitiveTopicList'].append(k.to_map() if k else None)
        if self.sensitive_topic_model_instance_id is not None:
            result['SensitiveTopicModelInstanceId'] = self.sensitive_topic_model_instance_id
        result['SensitiveWordList'] = []
        if self.sensitive_word_list is not None:
            for k in self.sensitive_word_list:
                result['SensitiveWordList'].append(k.to_map() if k else None)
        result['TopicConfigInfoList'] = []
        if self.topic_config_info_list is not None:
            for k in self.topic_config_info_list:
                result['TopicConfigInfoList'].append(k.to_map() if k else None)
        result['WordGroupInfoList'] = []
        if self.word_group_info_list is not None:
            for k in self.word_group_info_list:
                result['WordGroupInfoList'].append(k.to_map() if k else None)
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentSafeModelInstanceId') is not None:
            self.content_safe_model_instance_id = m.get('ContentSafeModelInstanceId')
        if m.get('EnableSensitiveInputCheck') is not None:
            self.enable_sensitive_input_check = m.get('EnableSensitiveInputCheck')
        if m.get('EnableSensitiveOutputCheck') is not None:
            self.enable_sensitive_output_check = m.get('EnableSensitiveOutputCheck')
        self.harmful_category_config_info_list = []
        if m.get('HarmfulCategoryConfigInfoList') is not None:
            for k in m.get('HarmfulCategoryConfigInfoList'):
                temp_model = CreatePolicyRequestHarmfulCategoryConfigInfoList()
                self.harmful_category_config_info_list.append(temp_model.from_map(k))
        if m.get('InputSafeAnswer') is not None:
            self.input_safe_answer = m.get('InputSafeAnswer')
        if m.get('InputSafeAnswerSwitch') is not None:
            self.input_safe_answer_switch = m.get('InputSafeAnswerSwitch')
        if m.get('IsSidecarPolicy') is not None:
            self.is_sidecar_policy = m.get('IsSidecarPolicy')
        if m.get('OutputSafeAnswer') is not None:
            self.output_safe_answer = m.get('OutputSafeAnswer')
        if m.get('OutputSafeAnswerSwitch') is not None:
            self.output_safe_answer_switch = m.get('OutputSafeAnswerSwitch')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PromptAttackInfo') is not None:
            temp_model = CreatePolicyRequestPromptAttackInfo()
            self.prompt_attack_info = temp_model.from_map(m['PromptAttackInfo'])
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = CreatePolicyRequestPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('PromptAttackModelInstanceId') is not None:
            self.prompt_attack_model_instance_id = m.get('PromptAttackModelInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.regular_express_list = []
        if m.get('RegularExpressList') is not None:
            for k in m.get('RegularExpressList'):
                temp_model = CreatePolicyRequestRegularExpressList()
                self.regular_express_list.append(temp_model.from_map(k))
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        self.sensitive_config_list = []
        if m.get('SensitiveConfigList') is not None:
            for k in m.get('SensitiveConfigList'):
                temp_model = CreatePolicyRequestSensitiveConfigList()
                self.sensitive_config_list.append(temp_model.from_map(k))
        self.sensitive_topic_list = []
        if m.get('SensitiveTopicList') is not None:
            for k in m.get('SensitiveTopicList'):
                temp_model = CreatePolicyRequestSensitiveTopicList()
                self.sensitive_topic_list.append(temp_model.from_map(k))
        if m.get('SensitiveTopicModelInstanceId') is not None:
            self.sensitive_topic_model_instance_id = m.get('SensitiveTopicModelInstanceId')
        self.sensitive_word_list = []
        if m.get('SensitiveWordList') is not None:
            for k in m.get('SensitiveWordList'):
                temp_model = CreatePolicyRequestSensitiveWordList()
                self.sensitive_word_list.append(temp_model.from_map(k))
        self.topic_config_info_list = []
        if m.get('TopicConfigInfoList') is not None:
            for k in m.get('TopicConfigInfoList'):
                temp_model = CreatePolicyRequestTopicConfigInfoList()
                self.topic_config_info_list.append(temp_model.from_map(k))
        self.word_group_info_list = []
        if m.get('WordGroupInfoList') is not None:
            for k in m.get('WordGroupInfoList'):
                temp_model = CreatePolicyRequestWordGroupInfoList()
                self.word_group_info_list.append(temp_model.from_map(k))
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreatePolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        content_safe_model_instance_id: int = None,
        enable_sensitive_input_check: int = None,
        enable_sensitive_output_check: int = None,
        harmful_category_config_info_list_shrink: str = None,
        input_safe_answer: str = None,
        input_safe_answer_switch: int = None,
        is_sidecar_policy: int = None,
        output_safe_answer: str = None,
        output_safe_answer_switch: int = None,
        policy_name: str = None,
        prompt_attack_info_shrink: str = None,
        prompt_attack_info_list_shrink: str = None,
        prompt_attack_model_instance_id: int = None,
        region_id: str = None,
        regular_express_list_shrink: str = None,
        scene_type: int = None,
        sensitive_config_list_shrink: str = None,
        sensitive_topic_list_shrink: str = None,
        sensitive_topic_model_instance_id: int = None,
        sensitive_word_list_shrink: str = None,
        topic_config_info_list_shrink: str = None,
        word_group_info_list_shrink: str = None,
        workspace_id: int = None,
    ):
        self.content_safe_model_instance_id = content_safe_model_instance_id
        self.enable_sensitive_input_check = enable_sensitive_input_check
        self.enable_sensitive_output_check = enable_sensitive_output_check
        # List of harmful category configurations
        self.harmful_category_config_info_list_shrink = harmful_category_config_info_list_shrink
        self.input_safe_answer = input_safe_answer
        self.input_safe_answer_switch = input_safe_answer_switch
        self.is_sidecar_policy = is_sidecar_policy
        self.output_safe_answer = output_safe_answer
        self.output_safe_answer_switch = output_safe_answer_switch
        # Detection policy name.
        self.policy_name = policy_name
        # Prompt attack detection result object
        self.prompt_attack_info_shrink = prompt_attack_info_shrink
        # List of prompt attacks
        self.prompt_attack_info_list_shrink = prompt_attack_info_list_shrink
        self.prompt_attack_model_instance_id = prompt_attack_model_instance_id
        # Region ID.
        self.region_id = region_id
        self.regular_express_list_shrink = regular_express_list_shrink
        self.scene_type = scene_type
        self.sensitive_config_list_shrink = sensitive_config_list_shrink
        self.sensitive_topic_list_shrink = sensitive_topic_list_shrink
        self.sensitive_topic_model_instance_id = sensitive_topic_model_instance_id
        self.sensitive_word_list_shrink = sensitive_word_list_shrink
        # List of sensitive topics
        self.topic_config_info_list_shrink = topic_config_info_list_shrink
        # List of keyword group objects
        self.word_group_info_list_shrink = word_group_info_list_shrink
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_safe_model_instance_id is not None:
            result['ContentSafeModelInstanceId'] = self.content_safe_model_instance_id
        if self.enable_sensitive_input_check is not None:
            result['EnableSensitiveInputCheck'] = self.enable_sensitive_input_check
        if self.enable_sensitive_output_check is not None:
            result['EnableSensitiveOutputCheck'] = self.enable_sensitive_output_check
        if self.harmful_category_config_info_list_shrink is not None:
            result['HarmfulCategoryConfigInfoList'] = self.harmful_category_config_info_list_shrink
        if self.input_safe_answer is not None:
            result['InputSafeAnswer'] = self.input_safe_answer
        if self.input_safe_answer_switch is not None:
            result['InputSafeAnswerSwitch'] = self.input_safe_answer_switch
        if self.is_sidecar_policy is not None:
            result['IsSidecarPolicy'] = self.is_sidecar_policy
        if self.output_safe_answer is not None:
            result['OutputSafeAnswer'] = self.output_safe_answer
        if self.output_safe_answer_switch is not None:
            result['OutputSafeAnswerSwitch'] = self.output_safe_answer_switch
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.prompt_attack_info_shrink is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info_shrink
        if self.prompt_attack_info_list_shrink is not None:
            result['PromptAttackInfoList'] = self.prompt_attack_info_list_shrink
        if self.prompt_attack_model_instance_id is not None:
            result['PromptAttackModelInstanceId'] = self.prompt_attack_model_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.regular_express_list_shrink is not None:
            result['RegularExpressList'] = self.regular_express_list_shrink
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.sensitive_config_list_shrink is not None:
            result['SensitiveConfigList'] = self.sensitive_config_list_shrink
        if self.sensitive_topic_list_shrink is not None:
            result['SensitiveTopicList'] = self.sensitive_topic_list_shrink
        if self.sensitive_topic_model_instance_id is not None:
            result['SensitiveTopicModelInstanceId'] = self.sensitive_topic_model_instance_id
        if self.sensitive_word_list_shrink is not None:
            result['SensitiveWordList'] = self.sensitive_word_list_shrink
        if self.topic_config_info_list_shrink is not None:
            result['TopicConfigInfoList'] = self.topic_config_info_list_shrink
        if self.word_group_info_list_shrink is not None:
            result['WordGroupInfoList'] = self.word_group_info_list_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentSafeModelInstanceId') is not None:
            self.content_safe_model_instance_id = m.get('ContentSafeModelInstanceId')
        if m.get('EnableSensitiveInputCheck') is not None:
            self.enable_sensitive_input_check = m.get('EnableSensitiveInputCheck')
        if m.get('EnableSensitiveOutputCheck') is not None:
            self.enable_sensitive_output_check = m.get('EnableSensitiveOutputCheck')
        if m.get('HarmfulCategoryConfigInfoList') is not None:
            self.harmful_category_config_info_list_shrink = m.get('HarmfulCategoryConfigInfoList')
        if m.get('InputSafeAnswer') is not None:
            self.input_safe_answer = m.get('InputSafeAnswer')
        if m.get('InputSafeAnswerSwitch') is not None:
            self.input_safe_answer_switch = m.get('InputSafeAnswerSwitch')
        if m.get('IsSidecarPolicy') is not None:
            self.is_sidecar_policy = m.get('IsSidecarPolicy')
        if m.get('OutputSafeAnswer') is not None:
            self.output_safe_answer = m.get('OutputSafeAnswer')
        if m.get('OutputSafeAnswerSwitch') is not None:
            self.output_safe_answer_switch = m.get('OutputSafeAnswerSwitch')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info_shrink = m.get('PromptAttackInfo')
        if m.get('PromptAttackInfoList') is not None:
            self.prompt_attack_info_list_shrink = m.get('PromptAttackInfoList')
        if m.get('PromptAttackModelInstanceId') is not None:
            self.prompt_attack_model_instance_id = m.get('PromptAttackModelInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegularExpressList') is not None:
            self.regular_express_list_shrink = m.get('RegularExpressList')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('SensitiveConfigList') is not None:
            self.sensitive_config_list_shrink = m.get('SensitiveConfigList')
        if m.get('SensitiveTopicList') is not None:
            self.sensitive_topic_list_shrink = m.get('SensitiveTopicList')
        if m.get('SensitiveTopicModelInstanceId') is not None:
            self.sensitive_topic_model_instance_id = m.get('SensitiveTopicModelInstanceId')
        if m.get('SensitiveWordList') is not None:
            self.sensitive_word_list_shrink = m.get('SensitiveWordList')
        if m.get('TopicConfigInfoList') is not None:
            self.topic_config_info_list_shrink = m.get('TopicConfigInfoList')
        if m.get('WordGroupInfoList') is not None:
            self.word_group_info_list_shrink = m.get('WordGroupInfoList')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        policy_id: int = None,
        policy_identifier: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # If there is an error, returns the error message.
        self.message = message
        # Policy ID.
        self.policy_id = policy_id
        # Policy identifier
        self.policy_identifier = policy_identifier
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful. true indicates success, false indicates failure.
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyResponseBody = None,
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTopicRequestBodyDataTopicExampleInfoList(TeaModel):
    def __init__(
        self,
        content: str = None,
        example_type: int = None,
    ):
        self.content = content
        self.example_type = example_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.example_type is not None:
            result['ExampleType'] = self.example_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExampleType') is not None:
            self.example_type = m.get('ExampleType')
        return self


class CreateTopicRequestBodyData(TeaModel):
    def __init__(
        self,
        topic_example_info_list: List[CreateTopicRequestBodyDataTopicExampleInfoList] = None,
    ):
        self.topic_example_info_list = topic_example_info_list

    def validate(self):
        if self.topic_example_info_list:
            for k in self.topic_example_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopicExampleInfoList'] = []
        if self.topic_example_info_list is not None:
            for k in self.topic_example_info_list:
                result['TopicExampleInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topic_example_info_list = []
        if m.get('TopicExampleInfoList') is not None:
            for k in m.get('TopicExampleInfoList'):
                temp_model = CreateTopicRequestBodyDataTopicExampleInfoList()
                self.topic_example_info_list.append(temp_model.from_map(k))
        return self


class CreateTopicRequest(TeaModel):
    def __init__(
        self,
        body_data: CreateTopicRequestBodyData = None,
        region_id: str = None,
        topic_definition: str = None,
        topic_name: str = None,
        workspace_id: int = None,
    ):
        self.body_data = body_data
        self.region_id = region_id
        self.topic_definition = topic_definition
        self.topic_name = topic_name
        self.workspace_id = workspace_id

    def validate(self):
        if self.body_data:
            self.body_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data is not None:
            result['BodyData'] = self.body_data.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = CreateTopicRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateTopicShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        region_id: str = None,
        topic_definition: str = None,
        topic_name: str = None,
        workspace_id: int = None,
    ):
        self.body_data_shrink = body_data_shrink
        self.region_id = region_id
        self.topic_definition = topic_definition
        self.topic_name = topic_name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data_shrink is not None:
            result['BodyData'] = self.body_data_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        topic_id: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class CreateTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTopicResponseBody = None,
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
            temp_model = CreateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWordGroupRequestBodyDataWordInfoList(TeaModel):
    def __init__(
        self,
        label: str = None,
        word: str = None,
    ):
        # Label
        self.label = label
        # Keyword
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class CreateWordGroupRequestBodyData(TeaModel):
    def __init__(
        self,
        word_info_list: List[CreateWordGroupRequestBodyDataWordInfoList] = None,
    ):
        # Keyword group list
        self.word_info_list = word_info_list

    def validate(self):
        if self.word_info_list:
            for k in self.word_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WordInfoList'] = []
        if self.word_info_list is not None:
            for k in self.word_info_list:
                result['WordInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.word_info_list = []
        if m.get('WordInfoList') is not None:
            for k in m.get('WordInfoList'):
                temp_model = CreateWordGroupRequestBodyDataWordInfoList()
                self.word_info_list.append(temp_model.from_map(k))
        return self


class CreateWordGroupRequest(TeaModel):
    def __init__(
        self,
        body_data: CreateWordGroupRequestBodyData = None,
        commit: bool = None,
        group_name: str = None,
        region_id: str = None,
        workspace_id: int = None,
    ):
        # Request object
        self.body_data = body_data
        # Whether to commit.
        # false: Not actually saved, only checked
        # true: Commit and save
        self.commit = commit
        # Keyword group name
        self.group_name = group_name
        # Region ID.
        self.region_id = region_id
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        if self.body_data:
            self.body_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data is not None:
            result['BodyData'] = self.body_data.to_map()
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = CreateWordGroupRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateWordGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        commit: bool = None,
        group_name: str = None,
        region_id: str = None,
        workspace_id: int = None,
    ):
        # Request object
        self.body_data_shrink = body_data_shrink
        # Whether to commit.
        # false: Not actually saved, only checked
        # true: Commit and save
        self.commit = commit
        # Keyword group name
        self.group_name = group_name
        # Region ID.
        self.region_id = region_id
        # Workspace ID
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data_shrink is not None:
            result['BodyData'] = self.body_data_shrink
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateWordGroupResponseBodyWordErrorInfoList(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        error_status: int = None,
        index: int = None,
        label: str = None,
        word: str = None,
    ):
        # Error message description
        self.error_message = error_message
        # Error status information.
        self.error_status = error_status
        # Position of the error information in the array.
        self.index = index
        # Label
        self.label = label
        # Keyword
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_status is not None:
            result['ErrorStatus'] = self.error_status
        if self.index is not None:
            result['Index'] = self.index
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorStatus') is not None:
            self.error_status = m.get('ErrorStatus')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class CreateWordGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        word_error_info_list: List[CreateWordGroupResponseBodyWordErrorInfoList] = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # If there is an error, returns the error message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Indicates whether the call was successful. true: Call succeeded. false: Call failed.
        self.success = success
        # Error information list
        self.word_error_info_list = word_error_info_list

    def validate(self):
        if self.word_error_info_list:
            for k in self.word_error_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['WordErrorInfoList'] = []
        if self.word_error_info_list is not None:
            for k in self.word_error_info_list:
                result['WordErrorInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.word_error_info_list = []
        if m.get('WordErrorInfoList') is not None:
            for k in m.get('WordErrorInfoList'):
                temp_model = CreateWordGroupResponseBodyWordErrorInfoList()
                self.word_error_info_list.append(temp_model.from_map(k))
        return self


class CreateWordGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWordGroupResponseBody = None,
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
            temp_model = CreateWordGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModelInstanceRequest(TeaModel):
    def __init__(
        self,
        model_instance_id_list: List[int] = None,
    ):
        self.model_instance_id_list = model_instance_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_instance_id_list is not None:
            result['ModelInstanceIdList'] = self.model_instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelInstanceIdList') is not None:
            self.model_instance_id_list = m.get('ModelInstanceIdList')
        return self


class DeleteModelInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        model_instance_id_list_shrink: str = None,
    ):
        self.model_instance_id_list_shrink = model_instance_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_instance_id_list_shrink is not None:
            result['ModelInstanceIdList'] = self.model_instance_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelInstanceIdList') is not None:
            self.model_instance_id_list_shrink = m.get('ModelInstanceIdList')
        return self


class DeleteModelInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteModelInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModelInstanceResponseBody = None,
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
            temp_model = DeleteModelInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id_list: List[int] = None,
        region_id: str = None,
    ):
        # List of detection policy IDs
        self.policy_id_list = policy_id_list
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id_list is not None:
            result['PolicyIdList'] = self.policy_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIdList') is not None:
            self.policy_id_list = m.get('PolicyIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        policy_id_list_shrink: str = None,
        region_id: str = None,
    ):
        # List of detection policy IDs
        self.policy_id_list_shrink = policy_id_list_shrink
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id_list_shrink is not None:
            result['PolicyIdList'] = self.policy_id_list_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIdList') is not None:
            self.policy_id_list_shrink = m.get('PolicyIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code description
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Indicates whether the operation was successful. true means success, false means failure.
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyResponseBody = None,
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTopicRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        topic_id_list: List[int] = None,
    ):
        self.region_id = region_id
        self.topic_id_list = topic_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic_id_list is not None:
            result['TopicIdList'] = self.topic_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopicIdList') is not None:
            self.topic_id_list = m.get('TopicIdList')
        return self


class DeleteTopicShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        topic_id_list_shrink: str = None,
    ):
        self.region_id = region_id
        self.topic_id_list_shrink = topic_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic_id_list_shrink is not None:
            result['TopicIdList'] = self.topic_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopicIdList') is not None:
            self.topic_id_list_shrink = m.get('TopicIdList')
        return self


class DeleteTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTopicResponseBody = None,
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
            temp_model = DeleteTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWordGroupRequest(TeaModel):
    def __init__(
        self,
        group_id_list: List[int] = None,
        region_id: str = None,
    ):
        # List of keyword strategy IDs.
        self.group_id_list = group_id_list
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteWordGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        group_id_list_shrink: str = None,
        region_id: str = None,
    ):
        # List of keyword strategy IDs.
        self.group_id_list_shrink = group_id_list_shrink
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id_list_shrink is not None:
            result['GroupIdList'] = self.group_id_list_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIdList') is not None:
            self.group_id_list_shrink = m.get('GroupIdList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteWordGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Result code, 200 indicates success; others indicate failure.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # If an error occurs, returns the error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Possible values:
        # - True indicates success.
        # - False indicates failure.
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteWordGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWordGroupResponseBody = None,
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
            temp_model = DeleteWordGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContentDetectResultRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
    ):
        self.region_id = region_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetContentDetectResultResponseBodyDataDetectResultList(TeaModel):
    def __init__(
        self,
        risk_info: str = None,
        risk_result: int = None,
        status: int = None,
    ):
        self.risk_info = risk_info
        self.risk_result = risk_result
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskInfo') is not None:
            self.risk_info = m.get('RiskInfo')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetContentDetectResultResponseBodyData(TeaModel):
    def __init__(
        self,
        detect_result_list: List[GetContentDetectResultResponseBodyDataDetectResultList] = None,
        processed_count: int = None,
        task_id: str = None,
        task_status: int = None,
        total_count: int = None,
    ):
        self.detect_result_list = detect_result_list
        self.processed_count = processed_count
        self.task_id = task_id
        self.task_status = task_status
        self.total_count = total_count

    def validate(self):
        if self.detect_result_list:
            for k in self.detect_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetectResultList'] = []
        if self.detect_result_list is not None:
            for k in self.detect_result_list:
                result['DetectResultList'].append(k.to_map() if k else None)
        if self.processed_count is not None:
            result['ProcessedCount'] = self.processed_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detect_result_list = []
        if m.get('DetectResultList') is not None:
            for k in m.get('DetectResultList'):
                temp_model = GetContentDetectResultResponseBodyDataDetectResultList()
                self.detect_result_list.append(temp_model.from_map(k))
        if m.get('ProcessedCount') is not None:
            self.processed_count = m.get('ProcessedCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetContentDetectResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetContentDetectResultResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = GetContentDetectResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetContentDetectResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetContentDetectResultResponseBody = None,
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
            temp_model = GetContentDetectResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelInputContentDetectResultRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
    ):
        # Region ID.
        self.region_id = region_id
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoListBlockWordList(TeaModel):
    def __init__(
        self,
        word: str = None,
        word_label: str = None,
    ):
        # Word
        self.word = word
        # Label
        self.word_label = word_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['Word'] = self.word
        if self.word_label is not None:
            result['WordLabel'] = self.word_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')
        if m.get('WordLabel') is not None:
            self.word_label = m.get('WordLabel')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoList(TeaModel):
    def __init__(
        self,
        block_word_list: List[GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoListBlockWordList] = None,
        group_name: str = None,
    ):
        # Keyword detection result object list
        self.block_word_list = block_word_list
        # Keyword group name
        self.group_name = group_name

    def validate(self):
        if self.block_word_list:
            for k in self.block_word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockWordList'] = []
        if self.block_word_list is not None:
            for k in self.block_word_list:
                result['BlockWordList'].append(k.to_map() if k else None)
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_word_list = []
        if m.get('BlockWordList') is not None:
            for k in m.get('BlockWordList'):
                temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoListBlockWordList()
                self.block_word_list.append(temp_model.from_map(k))
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWord(TeaModel):
    def __init__(
        self,
        block_word_group_info_list: List[GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoList] = None,
        risk_result: int = None,
    ):
        # Keyword detection result object list
        self.block_word_group_info_list = block_word_group_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result

    def validate(self):
        if self.block_word_group_info_list:
            for k in self.block_word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockWordGroupInfoList'] = []
        if self.block_word_group_info_list is not None:
            for k in self.block_word_group_info_list:
                result['BlockWordGroupInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_word_group_info_list = []
        if m.get('BlockWordGroupInfoList') is not None:
            for k in m.get('BlockWordGroupInfoList'):
                temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoList()
                self.block_word_group_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopicsTopicInfoList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
        topic_name: str = None,
    ):
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Topic name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopics(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        risk_result: int = None,
        topic_info_list: List[GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopicsTopicInfoList] = None,
    ):
        # ConfidenceScore
        self.confidence_score = confidence_score
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # List of sensitive topics
        self.topic_info_list = topic_info_list

    def validate(self):
        if self.topic_info_list:
            for k in self.topic_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        result['TopicInfoList'] = []
        if self.topic_info_list is not None:
            for k in self.topic_info_list:
                result['TopicInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        self.topic_info_list = []
        if m.get('TopicInfoList') is not None:
            for k in m.get('TopicInfoList'):
                temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopicsTopicInfoList()
                self.topic_info_list.append(temp_model.from_map(k))
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
        sub_category_label: str = None,
    ):
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Sub-category label
        self.sub_category_label = sub_category_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.sub_category_label is not None:
            result['SubCategoryLabel'] = self.sub_category_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('SubCategoryLabel') is not None:
            self.sub_category_label = m.get('SubCategoryLabel')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        harmful_category_info_list: List[GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList] = None,
        risk_result: int = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # List of harmful category objects
        self.harmful_category_info_list = harmful_category_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result

    def validate(self):
        if self.harmful_category_info_list:
            for k in self.harmful_category_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        result['HarmfulCategoryInfoList'] = []
        if self.harmful_category_info_list is not None:
            for k in self.harmful_category_info_list:
                result['HarmfulCategoryInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        self.harmful_category_info_list = []
        if m.get('HarmfulCategoryInfoList') is not None:
            for k in m.get('HarmfulCategoryInfoList'):
                temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList()
                self.harmful_category_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttackPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        prompt_attack_info: str = None,
        prompt_attack_info_list: List[GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttackPromptAttackInfoList] = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # Prompt attack detection result object
        self.prompt_attack_info = prompt_attack_info
        # Prompt attack list
        self.prompt_attack_info_list = prompt_attack_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info = m.get('PromptAttackInfo')
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttackPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfo(TeaModel):
    def __init__(
        self,
        block_word: GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWord = None,
        deny_topics: GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopics = None,
        harmful_categories: GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories = None,
        prompt_attack: GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack = None,
    ):
        # Detected keywords
        self.block_word = block_word
        # Sensitive topic object list
        self.deny_topics = deny_topics
        # List of harmful category result objects
        self.harmful_categories = harmful_categories
        # Prompt attack information
        self.prompt_attack = prompt_attack

    def validate(self):
        if self.block_word:
            self.block_word.validate()
        if self.deny_topics:
            self.deny_topics.validate()
        if self.harmful_categories:
            self.harmful_categories.validate()
        if self.prompt_attack:
            self.prompt_attack.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_word is not None:
            result['BlockWord'] = self.block_word.to_map()
        if self.deny_topics is not None:
            result['DenyTopics'] = self.deny_topics.to_map()
        if self.harmful_categories is not None:
            result['HarmfulCategories'] = self.harmful_categories.to_map()
        if self.prompt_attack is not None:
            result['PromptAttack'] = self.prompt_attack.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockWord') is not None:
            temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWord()
            self.block_word = temp_model.from_map(m['BlockWord'])
        if m.get('DenyTopics') is not None:
            temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopics()
            self.deny_topics = temp_model.from_map(m['DenyTopics'])
        if m.get('HarmfulCategories') is not None:
            temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories()
            self.harmful_categories = temp_model.from_map(m['HarmfulCategories'])
        if m.get('PromptAttack') is not None:
            temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack()
            self.prompt_attack = temp_model.from_map(m['PromptAttack'])
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultList(TeaModel):
    def __init__(
        self,
        risk_result: int = None,
        status: int = None,
        trace_info: GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfo = None,
    ):
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # 0: Queued
        # 1: Processing
        # 2: Completed
        # 3: Failed
        self.status = status
        # Inspection result
        self.trace_info = trace_info

    def validate(self):
        if self.trace_info:
            self.trace_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.status is not None:
            result['Status'] = self.status
        if self.trace_info is not None:
            result['TraceInfo'] = self.trace_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TraceInfo') is not None:
            temp_model = GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfo()
            self.trace_info = temp_model.from_map(m['TraceInfo'])
        return self


class GetModelInputContentDetectResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        detect_result_list: List[GetModelInputContentDetectResultResponseBodyDetectResultList] = None,
        http_status_code: int = None,
        message: str = None,
        processed_count: int = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
        task_status: int = None,
        total_count: int = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # Detection result object
        self.detect_result_list = detect_result_list
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Number of processed items in the task.
        self.processed_count = processed_count
        # Request ID
        self.request_id = request_id
        # Indicates whether the operation was successful. true means success, false means failure.
        self.success = success
        # Task ID.
        self.task_id = task_id
        # Task processing status:
        # 0: Queued
        # 1: Processing
        # 2: Completed
        # 3: Failed
        self.task_status = task_status
        # Total number of items
        self.total_count = total_count

    def validate(self):
        if self.detect_result_list:
            for k in self.detect_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DetectResultList'] = []
        if self.detect_result_list is not None:
            for k in self.detect_result_list:
                result['DetectResultList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.processed_count is not None:
            result['ProcessedCount'] = self.processed_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.detect_result_list = []
        if m.get('DetectResultList') is not None:
            for k in m.get('DetectResultList'):
                temp_model = GetModelInputContentDetectResultResponseBodyDetectResultList()
                self.detect_result_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProcessedCount') is not None:
            self.processed_count = m.get('ProcessedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetModelInputContentDetectResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelInputContentDetectResultResponseBody = None,
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
            temp_model = GetModelInputContentDetectResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelInstanceInfoRequest(TeaModel):
    def __init__(
        self,
        model_instance_id: int = None,
        scene_type: int = None,
    ):
        self.model_instance_id = model_instance_id
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class GetModelInstanceInfoResponseBodyHarmfulCategoryConfigInfoList(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_label: str = None,
        category_type: int = None,
        input_output_type: int = None,
        security_level: int = None,
    ):
        self.category_id = category_id
        self.category_label = category_label
        self.category_type = category_type
        self.input_output_type = input_output_type
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetModelInstanceInfoResponseBodyPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_label: str = None,
        security_level: int = None,
    ):
        self.category_id = category_id
        self.category_label = category_label
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetModelInstanceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        eas_service_id: str = None,
        eas_service_name: str = None,
        gmt_modified: int = None,
        harmful_category_config_info_list: List[GetModelInstanceInfoResponseBodyHarmfulCategoryConfigInfoList] = None,
        http_status_code: int = None,
        is_support_image: bool = None,
        is_support_text: bool = None,
        message: str = None,
        model_call_name: str = None,
        model_category_id: int = None,
        model_instance_id: int = None,
        model_source: int = None,
        model_token: str = None,
        model_url: str = None,
        model_vpc_url: str = None,
        prompt_attack_info_list: List[GetModelInstanceInfoResponseBodyPromptAttackInfoList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.description = description
        self.eas_service_id = eas_service_id
        self.eas_service_name = eas_service_name
        self.gmt_modified = gmt_modified
        self.harmful_category_config_info_list = harmful_category_config_info_list
        self.http_status_code = http_status_code
        self.is_support_image = is_support_image
        self.is_support_text = is_support_text
        self.message = message
        self.model_call_name = model_call_name
        self.model_category_id = model_category_id
        self.model_instance_id = model_instance_id
        self.model_source = model_source
        self.model_token = model_token
        self.model_url = model_url
        self.model_vpc_url = model_vpc_url
        self.prompt_attack_info_list = prompt_attack_info_list
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.harmful_category_config_info_list:
            for k in self.harmful_category_config_info_list:
                if k:
                    k.validate()
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.eas_service_id is not None:
            result['EasServiceId'] = self.eas_service_id
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        result['HarmfulCategoryConfigInfoList'] = []
        if self.harmful_category_config_info_list is not None:
            for k in self.harmful_category_config_info_list:
                result['HarmfulCategoryConfigInfoList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.is_support_image is not None:
            result['IsSupportImage'] = self.is_support_image
        if self.is_support_text is not None:
            result['IsSupportText'] = self.is_support_text
        if self.message is not None:
            result['Message'] = self.message
        if self.model_call_name is not None:
            result['ModelCallName'] = self.model_call_name
        if self.model_category_id is not None:
            result['ModelCategoryId'] = self.model_category_id
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        if self.model_source is not None:
            result['ModelSource'] = self.model_source
        if self.model_token is not None:
            result['ModelToken'] = self.model_token
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.model_vpc_url is not None:
            result['ModelVpcUrl'] = self.model_vpc_url
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EasServiceId') is not None:
            self.eas_service_id = m.get('EasServiceId')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        self.harmful_category_config_info_list = []
        if m.get('HarmfulCategoryConfigInfoList') is not None:
            for k in m.get('HarmfulCategoryConfigInfoList'):
                temp_model = GetModelInstanceInfoResponseBodyHarmfulCategoryConfigInfoList()
                self.harmful_category_config_info_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('IsSupportImage') is not None:
            self.is_support_image = m.get('IsSupportImage')
        if m.get('IsSupportText') is not None:
            self.is_support_text = m.get('IsSupportText')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModelCallName') is not None:
            self.model_call_name = m.get('ModelCallName')
        if m.get('ModelCategoryId') is not None:
            self.model_category_id = m.get('ModelCategoryId')
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        if m.get('ModelSource') is not None:
            self.model_source = m.get('ModelSource')
        if m.get('ModelToken') is not None:
            self.model_token = m.get('ModelToken')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModelVpcUrl') is not None:
            self.model_vpc_url = m.get('ModelVpcUrl')
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = GetModelInstanceInfoResponseBodyPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetModelInstanceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelInstanceInfoResponseBody = None,
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
            temp_model = GetModelInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModelOutputContentDetectResultRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
    ):
        # Region ID.
        self.region_id = region_id
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoListBlockWordList(TeaModel):
    def __init__(
        self,
        word: str = None,
        word_label: str = None,
    ):
        # Word
        self.word = word
        # Label
        self.word_label = word_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['Word'] = self.word
        if self.word_label is not None:
            result['WordLabel'] = self.word_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')
        if m.get('WordLabel') is not None:
            self.word_label = m.get('WordLabel')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoList(TeaModel):
    def __init__(
        self,
        block_word_list: List[GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoListBlockWordList] = None,
        group_name: str = None,
    ):
        # List of keyword detection results
        self.block_word_list = block_word_list
        # Keyword group name
        self.group_name = group_name

    def validate(self):
        if self.block_word_list:
            for k in self.block_word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockWordList'] = []
        if self.block_word_list is not None:
            for k in self.block_word_list:
                result['BlockWordList'].append(k.to_map() if k else None)
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_word_list = []
        if m.get('BlockWordList') is not None:
            for k in m.get('BlockWordList'):
                temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoListBlockWordList()
                self.block_word_list.append(temp_model.from_map(k))
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWord(TeaModel):
    def __init__(
        self,
        block_word_group_info_list: List[GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoList] = None,
        risk_result: int = None,
    ):
        # List of keyword detection result objects
        self.block_word_group_info_list = block_word_group_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result

    def validate(self):
        if self.block_word_group_info_list:
            for k in self.block_word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockWordGroupInfoList'] = []
        if self.block_word_group_info_list is not None:
            for k in self.block_word_group_info_list:
                result['BlockWordGroupInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_word_group_info_list = []
        if m.get('BlockWordGroupInfoList') is not None:
            for k in m.get('BlockWordGroupInfoList'):
                temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoList()
                self.block_word_group_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopicsTopicInfoList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
        topic_name: str = None,
    ):
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Topic name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopics(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        risk_result: int = None,
        topic_info_list: List[GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopicsTopicInfoList] = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # List of sensitive topics
        self.topic_info_list = topic_info_list

    def validate(self):
        if self.topic_info_list:
            for k in self.topic_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        result['TopicInfoList'] = []
        if self.topic_info_list is not None:
            for k in self.topic_info_list:
                result['TopicInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        self.topic_info_list = []
        if m.get('TopicInfoList') is not None:
            for k in m.get('TopicInfoList'):
                temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopicsTopicInfoList()
                self.topic_info_list.append(temp_model.from_map(k))
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
        sub_category_label: str = None,
    ):
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Sub-category label
        self.sub_category_label = sub_category_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.sub_category_label is not None:
            result['SubCategoryLabel'] = self.sub_category_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('SubCategoryLabel') is not None:
            self.sub_category_label = m.get('SubCategoryLabel')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        harmful_category_info_list: List[GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList] = None,
        risk_result: int = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # List of harmful category objects
        self.harmful_category_info_list = harmful_category_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result

    def validate(self):
        if self.harmful_category_info_list:
            for k in self.harmful_category_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        result['HarmfulCategoryInfoList'] = []
        if self.harmful_category_info_list is not None:
            for k in self.harmful_category_info_list:
                result['HarmfulCategoryInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        self.harmful_category_info_list = []
        if m.get('HarmfulCategoryInfoList') is not None:
            for k in m.get('HarmfulCategoryInfoList'):
                temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList()
                self.harmful_category_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttackPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        prompt_attack_info: str = None,
        prompt_attack_info_list: List[GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttackPromptAttackInfoList] = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # Prompt attack detection result object
        self.prompt_attack_info = prompt_attack_info
        # Prompt attack list
        self.prompt_attack_info_list = prompt_attack_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info = m.get('PromptAttackInfo')
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttackPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfo(TeaModel):
    def __init__(
        self,
        block_word: GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWord = None,
        deny_topics: GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopics = None,
        harmful_categories: GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories = None,
        prompt_attack: GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack = None,
    ):
        # Detected keywords
        self.block_word = block_word
        # Sensitive topic object list
        self.deny_topics = deny_topics
        # List of harmful category result objects
        self.harmful_categories = harmful_categories
        # PromptAttack
        self.prompt_attack = prompt_attack

    def validate(self):
        if self.block_word:
            self.block_word.validate()
        if self.deny_topics:
            self.deny_topics.validate()
        if self.harmful_categories:
            self.harmful_categories.validate()
        if self.prompt_attack:
            self.prompt_attack.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_word is not None:
            result['BlockWord'] = self.block_word.to_map()
        if self.deny_topics is not None:
            result['DenyTopics'] = self.deny_topics.to_map()
        if self.harmful_categories is not None:
            result['HarmfulCategories'] = self.harmful_categories.to_map()
        if self.prompt_attack is not None:
            result['PromptAttack'] = self.prompt_attack.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockWord') is not None:
            temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWord()
            self.block_word = temp_model.from_map(m['BlockWord'])
        if m.get('DenyTopics') is not None:
            temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoDenyTopics()
            self.deny_topics = temp_model.from_map(m['DenyTopics'])
        if m.get('HarmfulCategories') is not None:
            temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories()
            self.harmful_categories = temp_model.from_map(m['HarmfulCategories'])
        if m.get('PromptAttack') is not None:
            temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack()
            self.prompt_attack = temp_model.from_map(m['PromptAttack'])
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultList(TeaModel):
    def __init__(
        self,
        risk_result: int = None,
        status: int = None,
        trace_info: GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfo = None,
    ):
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # 0: Queued
        # 1: Processing
        # 2: Completed
        # 3: Failed
        self.status = status
        # Inspection results
        self.trace_info = trace_info

    def validate(self):
        if self.trace_info:
            self.trace_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.status is not None:
            result['Status'] = self.status
        if self.trace_info is not None:
            result['TraceInfo'] = self.trace_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TraceInfo') is not None:
            temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfo()
            self.trace_info = temp_model.from_map(m['TraceInfo'])
        return self


class GetModelOutputContentDetectResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        detect_result_list: List[GetModelOutputContentDetectResultResponseBodyDetectResultList] = None,
        http_status_code: int = None,
        message: str = None,
        processed_count: int = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
        task_status: int = None,
        total_count: int = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # List of detection result objects
        self.detect_result_list = detect_result_list
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Number of processed items in the task.
        self.processed_count = processed_count
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful. true indicates success, false indicates failure.
        self.success = success
        # Task ID.
        self.task_id = task_id
        # Task processing status:
        # 0: Queued
        # 1: Processing
        # 2: Completed
        # 3: Failed
        self.task_status = task_status
        # Total number of items
        self.total_count = total_count

    def validate(self):
        if self.detect_result_list:
            for k in self.detect_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['DetectResultList'] = []
        if self.detect_result_list is not None:
            for k in self.detect_result_list:
                result['DetectResultList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.processed_count is not None:
            result['ProcessedCount'] = self.processed_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.detect_result_list = []
        if m.get('DetectResultList') is not None:
            for k in m.get('DetectResultList'):
                temp_model = GetModelOutputContentDetectResultResponseBodyDetectResultList()
                self.detect_result_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProcessedCount') is not None:
            self.processed_count = m.get('ProcessedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetModelOutputContentDetectResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModelOutputContentDetectResultResponseBody = None,
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
            temp_model = GetModelOutputContentDetectResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyDefaultOptionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPolicyDefaultOptionsResponseBodyHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_label: str = None,
        category_type: int = None,
        input_output_type: int = None,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category ID
        self.category_id = category_id
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type
        # Harmful category configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetPolicyDefaultOptionsResponseBodyPromptAttackInfo(TeaModel):
    def __init__(
        self,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetPolicyDefaultOptionsResponseBodyPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_label: str = None,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category ID
        self.category_id = category_id
        # Category name
        self.category_label = category_label
        # Prompt attack configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetPolicyDefaultOptionsResponseBodySensitiveDataTypeList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        data_type: str = None,
        example: str = None,
        example_processed: str = None,
        is_enabled: int = None,
        match_and_replace: str = None,
        sensitive_config_id: int = None,
        sensitive_name: str = None,
    ):
        self.action_type = action_type
        self.data_type = data_type
        self.example = example
        self.example_processed = example_processed
        self.is_enabled = is_enabled
        self.match_and_replace = match_and_replace
        self.sensitive_config_id = sensitive_config_id
        self.sensitive_name = sensitive_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.example is not None:
            result['Example'] = self.example
        if self.example_processed is not None:
            result['ExampleProcessed'] = self.example_processed
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.match_and_replace is not None:
            result['MatchAndReplace'] = self.match_and_replace
        if self.sensitive_config_id is not None:
            result['SensitiveConfigId'] = self.sensitive_config_id
        if self.sensitive_name is not None:
            result['SensitiveName'] = self.sensitive_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('ExampleProcessed') is not None:
            self.example_processed = m.get('ExampleProcessed')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('MatchAndReplace') is not None:
            self.match_and_replace = m.get('MatchAndReplace')
        if m.get('SensitiveConfigId') is not None:
            self.sensitive_config_id = m.get('SensitiveConfigId')
        if m.get('SensitiveName') is not None:
            self.sensitive_name = m.get('SensitiveName')
        return self


class GetPolicyDefaultOptionsResponseBodyTopicConfigInfoList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        input_output_type: int = None,
        security_level: int = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Sensitive topic ID
        self.topic_id = topic_id
        # Topic name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetPolicyDefaultOptionsResponseBodyWordGroupInfoList(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        group_name: str = None,
        input_output_type: int = None,
    ):
        # Keyword group ID.
        self.group_id = group_id
        # Keyword group name
        self.group_name = group_name
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        return self


class GetPolicyDefaultOptionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        enable_sensitive_input_check: int = None,
        enable_sensitive_output_check: int = None,
        harmful_category_info_list: List[GetPolicyDefaultOptionsResponseBodyHarmfulCategoryInfoList] = None,
        http_status_code: int = None,
        input_safe_answer: str = None,
        input_safe_answer_switch: int = None,
        message: str = None,
        output_safe_answer: str = None,
        output_safe_answer_switch: int = None,
        prompt_attack_info: GetPolicyDefaultOptionsResponseBodyPromptAttackInfo = None,
        prompt_attack_info_list: List[GetPolicyDefaultOptionsResponseBodyPromptAttackInfoList] = None,
        request_id: str = None,
        sensitive_data_type_list: List[GetPolicyDefaultOptionsResponseBodySensitiveDataTypeList] = None,
        success: bool = None,
        topic_config_info_list: List[GetPolicyDefaultOptionsResponseBodyTopicConfigInfoList] = None,
        word_group_info_list: List[GetPolicyDefaultOptionsResponseBodyWordGroupInfoList] = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        self.enable_sensitive_input_check = enable_sensitive_input_check
        self.enable_sensitive_output_check = enable_sensitive_output_check
        # List of harmful category objects
        self.harmful_category_info_list = harmful_category_info_list
        # HTTP status code
        self.http_status_code = http_status_code
        self.input_safe_answer = input_safe_answer
        self.input_safe_answer_switch = input_safe_answer_switch
        # Return message.
        self.message = message
        self.output_safe_answer = output_safe_answer
        self.output_safe_answer_switch = output_safe_answer_switch
        # Prompt attack detection result object
        self.prompt_attack_info = prompt_attack_info
        # Prompt attack list
        self.prompt_attack_info_list = prompt_attack_info_list
        # Request ID
        self.request_id = request_id
        self.sensitive_data_type_list = sensitive_data_type_list
        # Indicates whether the operation was successful. `true` means success, `false` means failure.
        self.success = success
        # Sensitive topic list
        self.topic_config_info_list = topic_config_info_list
        # List of keyword group objects
        self.word_group_info_list = word_group_info_list

    def validate(self):
        if self.harmful_category_info_list:
            for k in self.harmful_category_info_list:
                if k:
                    k.validate()
        if self.prompt_attack_info:
            self.prompt_attack_info.validate()
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()
        if self.sensitive_data_type_list:
            for k in self.sensitive_data_type_list:
                if k:
                    k.validate()
        if self.topic_config_info_list:
            for k in self.topic_config_info_list:
                if k:
                    k.validate()
        if self.word_group_info_list:
            for k in self.word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.enable_sensitive_input_check is not None:
            result['EnableSensitiveInputCheck'] = self.enable_sensitive_input_check
        if self.enable_sensitive_output_check is not None:
            result['EnableSensitiveOutputCheck'] = self.enable_sensitive_output_check
        result['HarmfulCategoryInfoList'] = []
        if self.harmful_category_info_list is not None:
            for k in self.harmful_category_info_list:
                result['HarmfulCategoryInfoList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.input_safe_answer is not None:
            result['InputSafeAnswer'] = self.input_safe_answer
        if self.input_safe_answer_switch is not None:
            result['InputSafeAnswerSwitch'] = self.input_safe_answer_switch
        if self.message is not None:
            result['Message'] = self.message
        if self.output_safe_answer is not None:
            result['OutputSafeAnswer'] = self.output_safe_answer
        if self.output_safe_answer_switch is not None:
            result['OutputSafeAnswerSwitch'] = self.output_safe_answer_switch
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info.to_map()
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SensitiveDataTypeList'] = []
        if self.sensitive_data_type_list is not None:
            for k in self.sensitive_data_type_list:
                result['SensitiveDataTypeList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        result['TopicConfigInfoList'] = []
        if self.topic_config_info_list is not None:
            for k in self.topic_config_info_list:
                result['TopicConfigInfoList'].append(k.to_map() if k else None)
        result['WordGroupInfoList'] = []
        if self.word_group_info_list is not None:
            for k in self.word_group_info_list:
                result['WordGroupInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EnableSensitiveInputCheck') is not None:
            self.enable_sensitive_input_check = m.get('EnableSensitiveInputCheck')
        if m.get('EnableSensitiveOutputCheck') is not None:
            self.enable_sensitive_output_check = m.get('EnableSensitiveOutputCheck')
        self.harmful_category_info_list = []
        if m.get('HarmfulCategoryInfoList') is not None:
            for k in m.get('HarmfulCategoryInfoList'):
                temp_model = GetPolicyDefaultOptionsResponseBodyHarmfulCategoryInfoList()
                self.harmful_category_info_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InputSafeAnswer') is not None:
            self.input_safe_answer = m.get('InputSafeAnswer')
        if m.get('InputSafeAnswerSwitch') is not None:
            self.input_safe_answer_switch = m.get('InputSafeAnswerSwitch')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OutputSafeAnswer') is not None:
            self.output_safe_answer = m.get('OutputSafeAnswer')
        if m.get('OutputSafeAnswerSwitch') is not None:
            self.output_safe_answer_switch = m.get('OutputSafeAnswerSwitch')
        if m.get('PromptAttackInfo') is not None:
            temp_model = GetPolicyDefaultOptionsResponseBodyPromptAttackInfo()
            self.prompt_attack_info = temp_model.from_map(m['PromptAttackInfo'])
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = GetPolicyDefaultOptionsResponseBodyPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sensitive_data_type_list = []
        if m.get('SensitiveDataTypeList') is not None:
            for k in m.get('SensitiveDataTypeList'):
                temp_model = GetPolicyDefaultOptionsResponseBodySensitiveDataTypeList()
                self.sensitive_data_type_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.topic_config_info_list = []
        if m.get('TopicConfigInfoList') is not None:
            for k in m.get('TopicConfigInfoList'):
                temp_model = GetPolicyDefaultOptionsResponseBodyTopicConfigInfoList()
                self.topic_config_info_list.append(temp_model.from_map(k))
        self.word_group_info_list = []
        if m.get('WordGroupInfoList') is not None:
            for k in m.get('WordGroupInfoList'):
                temp_model = GetPolicyDefaultOptionsResponseBodyWordGroupInfoList()
                self.word_group_info_list.append(temp_model.from_map(k))
        return self


class GetPolicyDefaultOptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyDefaultOptionsResponseBody = None,
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
            temp_model = GetPolicyDefaultOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyInfoRequest(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
        region_id: str = None,
    ):
        # Detection policy ID
        self.policy_id = policy_id
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPolicyInfoResponseBodyContentSafeModelInfo(TeaModel):
    def __init__(
        self,
        eas_service_name: str = None,
        model_instance_id: int = None,
    ):
        self.eas_service_name = eas_service_name
        self.model_instance_id = model_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        return self


class GetPolicyInfoResponseBodyHarmfulCategoryConfigInfoList(TeaModel):
    def __init__(
        self,
        category_config_id: int = None,
        category_id: int = None,
        category_label: str = None,
        category_type: int = None,
        input_output_type: int = None,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category configuration ID
        self.category_config_id = category_config_id
        self.category_id = category_id
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type
        # Harmful category configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_config_id is not None:
            result['CategoryConfigId'] = self.category_config_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryConfigId') is not None:
            self.category_config_id = m.get('CategoryConfigId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetPolicyInfoResponseBodyPromptAttackInfo(TeaModel):
    def __init__(
        self,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Prompt attack configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetPolicyInfoResponseBodyPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_config_id: int = None,
        category_id: int = None,
        category_label: str = None,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category configuration ID
        self.category_config_id = category_config_id
        self.category_id = category_id
        # Category name
        self.category_label = category_label
        # Harmful category configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_config_id is not None:
            result['CategoryConfigId'] = self.category_config_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryConfigId') is not None:
            self.category_config_id = m.get('CategoryConfigId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetPolicyInfoResponseBodyPromptAttackModelInfo(TeaModel):
    def __init__(
        self,
        eas_service_name: str = None,
        model_instance_id: int = None,
    ):
        self.eas_service_name = eas_service_name
        self.model_instance_id = model_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        return self


class GetPolicyInfoResponseBodyRegularExpressList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        input_output_type: int = None,
        is_enabled: int = None,
        match_and_replace: str = None,
        regular_express: str = None,
        regular_express_id: int = None,
        regular_express_name: str = None,
    ):
        self.action_type = action_type
        self.input_output_type = input_output_type
        self.is_enabled = is_enabled
        self.match_and_replace = match_and_replace
        self.regular_express = regular_express
        self.regular_express_id = regular_express_id
        self.regular_express_name = regular_express_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.match_and_replace is not None:
            result['MatchAndReplace'] = self.match_and_replace
        if self.regular_express is not None:
            result['RegularExpress'] = self.regular_express
        if self.regular_express_id is not None:
            result['RegularExpressId'] = self.regular_express_id
        if self.regular_express_name is not None:
            result['RegularExpressName'] = self.regular_express_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('MatchAndReplace') is not None:
            self.match_and_replace = m.get('MatchAndReplace')
        if m.get('RegularExpress') is not None:
            self.regular_express = m.get('RegularExpress')
        if m.get('RegularExpressId') is not None:
            self.regular_express_id = m.get('RegularExpressId')
        if m.get('RegularExpressName') is not None:
            self.regular_express_name = m.get('RegularExpressName')
        return self


class GetPolicyInfoResponseBodySensitiveConfigList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        input_output_type: int = None,
        is_enabled: int = None,
        match_and_replace: str = None,
        sensitive_config_id: int = None,
        sensitive_name: str = None,
    ):
        self.action_type = action_type
        self.input_output_type = input_output_type
        self.is_enabled = is_enabled
        self.match_and_replace = match_and_replace
        self.sensitive_config_id = sensitive_config_id
        self.sensitive_name = sensitive_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.match_and_replace is not None:
            result['MatchAndReplace'] = self.match_and_replace
        if self.sensitive_config_id is not None:
            result['SensitiveConfigId'] = self.sensitive_config_id
        if self.sensitive_name is not None:
            result['SensitiveName'] = self.sensitive_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('MatchAndReplace') is not None:
            self.match_and_replace = m.get('MatchAndReplace')
        if m.get('SensitiveConfigId') is not None:
            self.sensitive_config_id = m.get('SensitiveConfigId')
        if m.get('SensitiveName') is not None:
            self.sensitive_name = m.get('SensitiveName')
        return self


class GetPolicyInfoResponseBodySensitiveTopicListTopicExampleInfoList(TeaModel):
    def __init__(
        self,
        content: str = None,
        example_type: int = None,
    ):
        self.content = content
        self.example_type = example_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.example_type is not None:
            result['ExampleType'] = self.example_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExampleType') is not None:
            self.example_type = m.get('ExampleType')
        return self


class GetPolicyInfoResponseBodySensitiveTopicList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        input_output_type: int = None,
        security_level: int = None,
        topic_definition: str = None,
        topic_example_info_list: List[GetPolicyInfoResponseBodySensitiveTopicListTopicExampleInfoList] = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        self.category_type = category_type
        self.input_output_type = input_output_type
        self.security_level = security_level
        self.topic_definition = topic_definition
        self.topic_example_info_list = topic_example_info_list
        self.topic_id = topic_id
        self.topic_name = topic_name

    def validate(self):
        if self.topic_example_info_list:
            for k in self.topic_example_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        result['TopicExampleInfoList'] = []
        if self.topic_example_info_list is not None:
            for k in self.topic_example_info_list:
                result['TopicExampleInfoList'].append(k.to_map() if k else None)
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        self.topic_example_info_list = []
        if m.get('TopicExampleInfoList') is not None:
            for k in m.get('TopicExampleInfoList'):
                temp_model = GetPolicyInfoResponseBodySensitiveTopicListTopicExampleInfoList()
                self.topic_example_info_list.append(temp_model.from_map(k))
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetPolicyInfoResponseBodySensitiveTopicModelInfo(TeaModel):
    def __init__(
        self,
        eas_service_name: str = None,
        model_instance_id: int = None,
    ):
        self.eas_service_name = eas_service_name
        self.model_instance_id = model_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        return self


class GetPolicyInfoResponseBodySensitiveWordList(TeaModel):
    def __init__(
        self,
        input_output_type: int = None,
        label: str = None,
        word: str = None,
    ):
        self.input_output_type = input_output_type
        self.label = label
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class GetPolicyInfoResponseBodyTopicConfigInfoList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        input_output_type: int = None,
        security_level: int = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Sensitive topic ID
        self.topic_id = topic_id
        # Topic name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetPolicyInfoResponseBodyWordGroupInfoList(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        group_name: str = None,
        input_output_type: int = None,
    ):
        # Keyword group ID.
        self.group_id = group_id
        # Keyword group name
        self.group_name = group_name
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        return self


class GetPolicyInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        content_safe_model_info: GetPolicyInfoResponseBodyContentSafeModelInfo = None,
        enable_sensitive_input_check: int = None,
        enable_sensitive_output_check: int = None,
        gmt_modified: int = None,
        harmful_category_config_info_list: List[GetPolicyInfoResponseBodyHarmfulCategoryConfigInfoList] = None,
        http_status_code: int = None,
        input_safe_answer: str = None,
        input_safe_answer_switch: int = None,
        is_sidecar_policy: int = None,
        message: str = None,
        output_safe_answer: str = None,
        output_safe_answer_switch: int = None,
        policy_identifier: str = None,
        policy_name: str = None,
        prompt_attack_info: GetPolicyInfoResponseBodyPromptAttackInfo = None,
        prompt_attack_info_list: List[GetPolicyInfoResponseBodyPromptAttackInfoList] = None,
        prompt_attack_model_info: GetPolicyInfoResponseBodyPromptAttackModelInfo = None,
        regular_express_list: List[GetPolicyInfoResponseBodyRegularExpressList] = None,
        request_id: str = None,
        scene_type: int = None,
        sensitive_config_list: List[GetPolicyInfoResponseBodySensitiveConfigList] = None,
        sensitive_topic_list: List[GetPolicyInfoResponseBodySensitiveTopicList] = None,
        sensitive_topic_model_info: GetPolicyInfoResponseBodySensitiveTopicModelInfo = None,
        sensitive_word_list: List[GetPolicyInfoResponseBodySensitiveWordList] = None,
        success: bool = None,
        topic_config_info_list: List[GetPolicyInfoResponseBodyTopicConfigInfoList] = None,
        word_group_info_list: List[GetPolicyInfoResponseBodyWordGroupInfoList] = None,
    ):
        # Result code, 00000 indicates success; others indicate failure.
        self.code = code
        self.content_safe_model_info = content_safe_model_info
        self.enable_sensitive_input_check = enable_sensitive_input_check
        self.enable_sensitive_output_check = enable_sensitive_output_check
        # Policy modification time
        self.gmt_modified = gmt_modified
        # Harmful category configuration list
        self.harmful_category_config_info_list = harmful_category_config_info_list
        # HTTP status code
        self.http_status_code = http_status_code
        self.input_safe_answer = input_safe_answer
        self.input_safe_answer_switch = input_safe_answer_switch
        self.is_sidecar_policy = is_sidecar_policy
        # Error message.
        self.message = message
        self.output_safe_answer = output_safe_answer
        self.output_safe_answer_switch = output_safe_answer_switch
        # Policy identifier
        self.policy_identifier = policy_identifier
        # Detection policy name.
        self.policy_name = policy_name
        # Prompt attack detection result object
        self.prompt_attack_info = prompt_attack_info
        # Prompt attack list
        self.prompt_attack_info_list = prompt_attack_info_list
        self.prompt_attack_model_info = prompt_attack_model_info
        self.regular_express_list = regular_express_list
        # Request ID
        self.request_id = request_id
        self.scene_type = scene_type
        self.sensitive_config_list = sensitive_config_list
        self.sensitive_topic_list = sensitive_topic_list
        self.sensitive_topic_model_info = sensitive_topic_model_info
        self.sensitive_word_list = sensitive_word_list
        # Indicates whether the operation was successful. `true` for success, `false` for failure.
        self.success = success
        # Sensitive topic list
        self.topic_config_info_list = topic_config_info_list
        # Keyword group object list
        self.word_group_info_list = word_group_info_list

    def validate(self):
        if self.content_safe_model_info:
            self.content_safe_model_info.validate()
        if self.harmful_category_config_info_list:
            for k in self.harmful_category_config_info_list:
                if k:
                    k.validate()
        if self.prompt_attack_info:
            self.prompt_attack_info.validate()
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()
        if self.prompt_attack_model_info:
            self.prompt_attack_model_info.validate()
        if self.regular_express_list:
            for k in self.regular_express_list:
                if k:
                    k.validate()
        if self.sensitive_config_list:
            for k in self.sensitive_config_list:
                if k:
                    k.validate()
        if self.sensitive_topic_list:
            for k in self.sensitive_topic_list:
                if k:
                    k.validate()
        if self.sensitive_topic_model_info:
            self.sensitive_topic_model_info.validate()
        if self.sensitive_word_list:
            for k in self.sensitive_word_list:
                if k:
                    k.validate()
        if self.topic_config_info_list:
            for k in self.topic_config_info_list:
                if k:
                    k.validate()
        if self.word_group_info_list:
            for k in self.word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content_safe_model_info is not None:
            result['ContentSafeModelInfo'] = self.content_safe_model_info.to_map()
        if self.enable_sensitive_input_check is not None:
            result['EnableSensitiveInputCheck'] = self.enable_sensitive_input_check
        if self.enable_sensitive_output_check is not None:
            result['EnableSensitiveOutputCheck'] = self.enable_sensitive_output_check
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        result['HarmfulCategoryConfigInfoList'] = []
        if self.harmful_category_config_info_list is not None:
            for k in self.harmful_category_config_info_list:
                result['HarmfulCategoryConfigInfoList'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.input_safe_answer is not None:
            result['InputSafeAnswer'] = self.input_safe_answer
        if self.input_safe_answer_switch is not None:
            result['InputSafeAnswerSwitch'] = self.input_safe_answer_switch
        if self.is_sidecar_policy is not None:
            result['IsSidecarPolicy'] = self.is_sidecar_policy
        if self.message is not None:
            result['Message'] = self.message
        if self.output_safe_answer is not None:
            result['OutputSafeAnswer'] = self.output_safe_answer
        if self.output_safe_answer_switch is not None:
            result['OutputSafeAnswerSwitch'] = self.output_safe_answer_switch
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info.to_map()
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.prompt_attack_model_info is not None:
            result['PromptAttackModelInfo'] = self.prompt_attack_model_info.to_map()
        result['RegularExpressList'] = []
        if self.regular_express_list is not None:
            for k in self.regular_express_list:
                result['RegularExpressList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        result['SensitiveConfigList'] = []
        if self.sensitive_config_list is not None:
            for k in self.sensitive_config_list:
                result['SensitiveConfigList'].append(k.to_map() if k else None)
        result['SensitiveTopicList'] = []
        if self.sensitive_topic_list is not None:
            for k in self.sensitive_topic_list:
                result['SensitiveTopicList'].append(k.to_map() if k else None)
        if self.sensitive_topic_model_info is not None:
            result['SensitiveTopicModelInfo'] = self.sensitive_topic_model_info.to_map()
        result['SensitiveWordList'] = []
        if self.sensitive_word_list is not None:
            for k in self.sensitive_word_list:
                result['SensitiveWordList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        result['TopicConfigInfoList'] = []
        if self.topic_config_info_list is not None:
            for k in self.topic_config_info_list:
                result['TopicConfigInfoList'].append(k.to_map() if k else None)
        result['WordGroupInfoList'] = []
        if self.word_group_info_list is not None:
            for k in self.word_group_info_list:
                result['WordGroupInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContentSafeModelInfo') is not None:
            temp_model = GetPolicyInfoResponseBodyContentSafeModelInfo()
            self.content_safe_model_info = temp_model.from_map(m['ContentSafeModelInfo'])
        if m.get('EnableSensitiveInputCheck') is not None:
            self.enable_sensitive_input_check = m.get('EnableSensitiveInputCheck')
        if m.get('EnableSensitiveOutputCheck') is not None:
            self.enable_sensitive_output_check = m.get('EnableSensitiveOutputCheck')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        self.harmful_category_config_info_list = []
        if m.get('HarmfulCategoryConfigInfoList') is not None:
            for k in m.get('HarmfulCategoryConfigInfoList'):
                temp_model = GetPolicyInfoResponseBodyHarmfulCategoryConfigInfoList()
                self.harmful_category_config_info_list.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('InputSafeAnswer') is not None:
            self.input_safe_answer = m.get('InputSafeAnswer')
        if m.get('InputSafeAnswerSwitch') is not None:
            self.input_safe_answer_switch = m.get('InputSafeAnswerSwitch')
        if m.get('IsSidecarPolicy') is not None:
            self.is_sidecar_policy = m.get('IsSidecarPolicy')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OutputSafeAnswer') is not None:
            self.output_safe_answer = m.get('OutputSafeAnswer')
        if m.get('OutputSafeAnswerSwitch') is not None:
            self.output_safe_answer_switch = m.get('OutputSafeAnswerSwitch')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PromptAttackInfo') is not None:
            temp_model = GetPolicyInfoResponseBodyPromptAttackInfo()
            self.prompt_attack_info = temp_model.from_map(m['PromptAttackInfo'])
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = GetPolicyInfoResponseBodyPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('PromptAttackModelInfo') is not None:
            temp_model = GetPolicyInfoResponseBodyPromptAttackModelInfo()
            self.prompt_attack_model_info = temp_model.from_map(m['PromptAttackModelInfo'])
        self.regular_express_list = []
        if m.get('RegularExpressList') is not None:
            for k in m.get('RegularExpressList'):
                temp_model = GetPolicyInfoResponseBodyRegularExpressList()
                self.regular_express_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        self.sensitive_config_list = []
        if m.get('SensitiveConfigList') is not None:
            for k in m.get('SensitiveConfigList'):
                temp_model = GetPolicyInfoResponseBodySensitiveConfigList()
                self.sensitive_config_list.append(temp_model.from_map(k))
        self.sensitive_topic_list = []
        if m.get('SensitiveTopicList') is not None:
            for k in m.get('SensitiveTopicList'):
                temp_model = GetPolicyInfoResponseBodySensitiveTopicList()
                self.sensitive_topic_list.append(temp_model.from_map(k))
        if m.get('SensitiveTopicModelInfo') is not None:
            temp_model = GetPolicyInfoResponseBodySensitiveTopicModelInfo()
            self.sensitive_topic_model_info = temp_model.from_map(m['SensitiveTopicModelInfo'])
        self.sensitive_word_list = []
        if m.get('SensitiveWordList') is not None:
            for k in m.get('SensitiveWordList'):
                temp_model = GetPolicyInfoResponseBodySensitiveWordList()
                self.sensitive_word_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.topic_config_info_list = []
        if m.get('TopicConfigInfoList') is not None:
            for k in m.get('TopicConfigInfoList'):
                temp_model = GetPolicyInfoResponseBodyTopicConfigInfoList()
                self.topic_config_info_list.append(temp_model.from_map(k))
        self.word_group_info_list = []
        if m.get('WordGroupInfoList') is not None:
            for k in m.get('WordGroupInfoList'):
                temp_model = GetPolicyInfoResponseBodyWordGroupInfoList()
                self.word_group_info_list.append(temp_model.from_map(k))
        return self


class GetPolicyInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyInfoResponseBody = None,
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
            temp_model = GetPolicyInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        topic_id: int = None,
    ):
        self.region_id = region_id
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class GetTopicResponseBodyPolicyInfoList(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
        policy_identifier: str = None,
        policy_name: str = None,
    ):
        self.policy_id = policy_id
        self.policy_identifier = policy_identifier
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class GetTopicResponseBodyTopicExampleInfoList(TeaModel):
    def __init__(
        self,
        content: str = None,
        example_id: int = None,
        example_type: int = None,
    ):
        self.content = content
        self.example_id = example_id
        self.example_type = example_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.example_id is not None:
            result['ExampleId'] = self.example_id
        if self.example_type is not None:
            result['ExampleType'] = self.example_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExampleId') is not None:
            self.example_id = m.get('ExampleId')
        if m.get('ExampleType') is not None:
            self.example_type = m.get('ExampleType')
        return self


class GetTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        gmt_modified: int = None,
        http_status_code: int = None,
        message: str = None,
        policy_info_list: List[GetTopicResponseBodyPolicyInfoList] = None,
        request_id: str = None,
        success: bool = None,
        topic_definition: str = None,
        topic_example_info_list: List[GetTopicResponseBodyTopicExampleInfoList] = None,
        topic_name: str = None,
    ):
        self.code = code
        self.gmt_modified = gmt_modified
        self.http_status_code = http_status_code
        self.message = message
        self.policy_info_list = policy_info_list
        self.request_id = request_id
        self.success = success
        self.topic_definition = topic_definition
        self.topic_example_info_list = topic_example_info_list
        self.topic_name = topic_name

    def validate(self):
        if self.policy_info_list:
            for k in self.policy_info_list:
                if k:
                    k.validate()
        if self.topic_example_info_list:
            for k in self.topic_example_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        result['PolicyInfoList'] = []
        if self.policy_info_list is not None:
            for k in self.policy_info_list:
                result['PolicyInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        result['TopicExampleInfoList'] = []
        if self.topic_example_info_list is not None:
            for k in self.topic_example_info_list:
                result['TopicExampleInfoList'].append(k.to_map() if k else None)
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.policy_info_list = []
        if m.get('PolicyInfoList') is not None:
            for k in m.get('PolicyInfoList'):
                temp_model = GetTopicResponseBodyPolicyInfoList()
                self.policy_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        self.topic_example_info_list = []
        if m.get('TopicExampleInfoList') is not None:
            for k in m.get('TopicExampleInfoList'):
                temp_model = GetTopicResponseBodyTopicExampleInfoList()
                self.topic_example_info_list.append(temp_model.from_map(k))
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class GetTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicResponseBody = None,
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
            temp_model = GetTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWordGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        region_id: str = None,
    ):
        # Keyword group ID.
        self.group_id = group_id
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetWordGroupResponseBodyWordInfoList(TeaModel):
    def __init__(
        self,
        label: str = None,
        word: str = None,
        word_id: int = None,
    ):
        # Label.
        self.label = label
        # Keyword.
        self.word = word
        # ID of the successfully added word.
        self.word_id = word_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        if self.word_id is not None:
            result['WordId'] = self.word_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        if m.get('WordId') is not None:
            self.word_id = m.get('WordId')
        return self


class GetWordGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        group_name: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        word_info_list: List[GetWordGroupResponseBodyWordInfoList] = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # Keyword group name.
        self.group_name = group_name
        # HTTP status code.
        self.http_status_code = http_status_code
        # If there is an error, returns the error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful.
        self.success = success
        # Total count.
        self.total_count = total_count
        # Keyword group list.
        self.word_info_list = word_info_list

    def validate(self):
        if self.word_info_list:
            for k in self.word_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WordInfoList'] = []
        if self.word_info_list is not None:
            for k in self.word_info_list:
                result['WordInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.word_info_list = []
        if m.get('WordInfoList') is not None:
            for k in m.get('WordInfoList'):
                temp_model = GetWordGroupResponseBodyWordInfoList()
                self.word_info_list.append(temp_model.from_map(k))
        return self


class GetWordGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWordGroupResponseBody = None,
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
            temp_model = GetWordGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelCategoryRequest(TeaModel):
    def __init__(
        self,
        content_safe_image_supported: int = None,
        content_safe_text_supported: int = None,
        model_category_name: str = None,
        model_source: str = None,
        prompt_attack_text_supported: int = None,
        sensitive_topic_text_supported: int = None,
    ):
        self.content_safe_image_supported = content_safe_image_supported
        self.content_safe_text_supported = content_safe_text_supported
        self.model_category_name = model_category_name
        self.model_source = model_source
        self.prompt_attack_text_supported = prompt_attack_text_supported
        self.sensitive_topic_text_supported = sensitive_topic_text_supported

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_safe_image_supported is not None:
            result['ContentSafeImageSupported'] = self.content_safe_image_supported
        if self.content_safe_text_supported is not None:
            result['ContentSafeTextSupported'] = self.content_safe_text_supported
        if self.model_category_name is not None:
            result['ModelCategoryName'] = self.model_category_name
        if self.model_source is not None:
            result['ModelSource'] = self.model_source
        if self.prompt_attack_text_supported is not None:
            result['PromptAttackTextSupported'] = self.prompt_attack_text_supported
        if self.sensitive_topic_text_supported is not None:
            result['SensitiveTopicTextSupported'] = self.sensitive_topic_text_supported
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentSafeImageSupported') is not None:
            self.content_safe_image_supported = m.get('ContentSafeImageSupported')
        if m.get('ContentSafeTextSupported') is not None:
            self.content_safe_text_supported = m.get('ContentSafeTextSupported')
        if m.get('ModelCategoryName') is not None:
            self.model_category_name = m.get('ModelCategoryName')
        if m.get('ModelSource') is not None:
            self.model_source = m.get('ModelSource')
        if m.get('PromptAttackTextSupported') is not None:
            self.prompt_attack_text_supported = m.get('PromptAttackTextSupported')
        if m.get('SensitiveTopicTextSupported') is not None:
            self.sensitive_topic_text_supported = m.get('SensitiveTopicTextSupported')
        return self


class ListModelCategoryResponseBodyModelCategoryInfoList(TeaModel):
    def __init__(
        self,
        content_safe_image_supported: int = None,
        content_safe_text_supported: int = None,
        model_category_id: int = None,
        model_category_name: str = None,
        model_source: int = None,
        priority: int = None,
        prompt_attack_text_supported: int = None,
        sensitive_topic_text_supported: int = None,
    ):
        self.content_safe_image_supported = content_safe_image_supported
        self.content_safe_text_supported = content_safe_text_supported
        self.model_category_id = model_category_id
        self.model_category_name = model_category_name
        self.model_source = model_source
        self.priority = priority
        self.prompt_attack_text_supported = prompt_attack_text_supported
        self.sensitive_topic_text_supported = sensitive_topic_text_supported

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_safe_image_supported is not None:
            result['ContentSafeImageSupported'] = self.content_safe_image_supported
        if self.content_safe_text_supported is not None:
            result['ContentSafeTextSupported'] = self.content_safe_text_supported
        if self.model_category_id is not None:
            result['ModelCategoryId'] = self.model_category_id
        if self.model_category_name is not None:
            result['ModelCategoryName'] = self.model_category_name
        if self.model_source is not None:
            result['ModelSource'] = self.model_source
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.prompt_attack_text_supported is not None:
            result['PromptAttackTextSupported'] = self.prompt_attack_text_supported
        if self.sensitive_topic_text_supported is not None:
            result['SensitiveTopicTextSupported'] = self.sensitive_topic_text_supported
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentSafeImageSupported') is not None:
            self.content_safe_image_supported = m.get('ContentSafeImageSupported')
        if m.get('ContentSafeTextSupported') is not None:
            self.content_safe_text_supported = m.get('ContentSafeTextSupported')
        if m.get('ModelCategoryId') is not None:
            self.model_category_id = m.get('ModelCategoryId')
        if m.get('ModelCategoryName') is not None:
            self.model_category_name = m.get('ModelCategoryName')
        if m.get('ModelSource') is not None:
            self.model_source = m.get('ModelSource')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('PromptAttackTextSupported') is not None:
            self.prompt_attack_text_supported = m.get('PromptAttackTextSupported')
        if m.get('SensitiveTopicTextSupported') is not None:
            self.sensitive_topic_text_supported = m.get('SensitiveTopicTextSupported')
        return self


class ListModelCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        model_category_info_list: List[ListModelCategoryResponseBodyModelCategoryInfoList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.model_category_info_list = model_category_info_list
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model_category_info_list:
            for k in self.model_category_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        result['ModelCategoryInfoList'] = []
        if self.model_category_info_list is not None:
            for k in self.model_category_info_list:
                result['ModelCategoryInfoList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model_category_info_list = []
        if m.get('ModelCategoryInfoList') is not None:
            for k in m.get('ModelCategoryInfoList'):
                temp_model = ListModelCategoryResponseBodyModelCategoryInfoList()
                self.model_category_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListModelCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModelCategoryResponseBody = None,
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
            temp_model = ListModelCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModelInstanceRequest(TeaModel):
    def __init__(
        self,
        eas_service_name: str = None,
        is_sidecar_policy: int = None,
        is_support_content_safe: int = None,
        is_support_prompt_attack: int = None,
        is_support_sensitive_topic: int = None,
        model_source: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        sort_by: str = None,
        workspace_id: int = None,
    ):
        self.eas_service_name = eas_service_name
        self.is_sidecar_policy = is_sidecar_policy
        self.is_support_content_safe = is_support_content_safe
        self.is_support_prompt_attack = is_support_prompt_attack
        self.is_support_sensitive_topic = is_support_sensitive_topic
        self.model_source = model_source
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.sort_by = sort_by
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.is_sidecar_policy is not None:
            result['IsSidecarPolicy'] = self.is_sidecar_policy
        if self.is_support_content_safe is not None:
            result['IsSupportContentSafe'] = self.is_support_content_safe
        if self.is_support_prompt_attack is not None:
            result['IsSupportPromptAttack'] = self.is_support_prompt_attack
        if self.is_support_sensitive_topic is not None:
            result['IsSupportSensitiveTopic'] = self.is_support_sensitive_topic
        if self.model_source is not None:
            result['ModelSource'] = self.model_source
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('IsSidecarPolicy') is not None:
            self.is_sidecar_policy = m.get('IsSidecarPolicy')
        if m.get('IsSupportContentSafe') is not None:
            self.is_support_content_safe = m.get('IsSupportContentSafe')
        if m.get('IsSupportPromptAttack') is not None:
            self.is_support_prompt_attack = m.get('IsSupportPromptAttack')
        if m.get('IsSupportSensitiveTopic') is not None:
            self.is_support_sensitive_topic = m.get('IsSupportSensitiveTopic')
        if m.get('ModelSource') is not None:
            self.model_source = m.get('ModelSource')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListModelInstanceResponseBodyModelInstanceInfoList(TeaModel):
    def __init__(
        self,
        eas_service_name: str = None,
        gmt_modified: int = None,
        is_support_content_safe: int = None,
        is_support_image: bool = None,
        is_support_prompt_attack: int = None,
        is_support_sensitive_topic: int = None,
        is_support_text: bool = None,
        model_instance_id: int = None,
        model_source: int = None,
        workspace_id: int = None,
    ):
        self.eas_service_name = eas_service_name
        self.gmt_modified = gmt_modified
        self.is_support_content_safe = is_support_content_safe
        self.is_support_image = is_support_image
        self.is_support_prompt_attack = is_support_prompt_attack
        self.is_support_sensitive_topic = is_support_sensitive_topic
        self.is_support_text = is_support_text
        self.model_instance_id = model_instance_id
        self.model_source = model_source
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_support_content_safe is not None:
            result['IsSupportContentSafe'] = self.is_support_content_safe
        if self.is_support_image is not None:
            result['IsSupportImage'] = self.is_support_image
        if self.is_support_prompt_attack is not None:
            result['IsSupportPromptAttack'] = self.is_support_prompt_attack
        if self.is_support_sensitive_topic is not None:
            result['IsSupportSensitiveTopic'] = self.is_support_sensitive_topic
        if self.is_support_text is not None:
            result['IsSupportText'] = self.is_support_text
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        if self.model_source is not None:
            result['ModelSource'] = self.model_source
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsSupportContentSafe') is not None:
            self.is_support_content_safe = m.get('IsSupportContentSafe')
        if m.get('IsSupportImage') is not None:
            self.is_support_image = m.get('IsSupportImage')
        if m.get('IsSupportPromptAttack') is not None:
            self.is_support_prompt_attack = m.get('IsSupportPromptAttack')
        if m.get('IsSupportSensitiveTopic') is not None:
            self.is_support_sensitive_topic = m.get('IsSupportSensitiveTopic')
        if m.get('IsSupportText') is not None:
            self.is_support_text = m.get('IsSupportText')
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        if m.get('ModelSource') is not None:
            self.model_source = m.get('ModelSource')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListModelInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        model_instance_info_list: List[ListModelInstanceResponseBodyModelInstanceInfoList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.model_instance_info_list = model_instance_info_list
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.model_instance_info_list:
            for k in self.model_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        result['ModelInstanceInfoList'] = []
        if self.model_instance_info_list is not None:
            for k in self.model_instance_info_list:
                result['ModelInstanceInfoList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.model_instance_info_list = []
        if m.get('ModelInstanceInfoList') is not None:
            for k in m.get('ModelInstanceInfoList'):
                temp_model = ListModelInstanceResponseBodyModelInstanceInfoList()
                self.model_instance_info_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListModelInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModelInstanceResponseBody = None,
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
            temp_model = ListModelInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPolicyRequest(TeaModel):
    def __init__(
        self,
        is_sidecar_policy: int = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_identifier: str = None,
        policy_name: str = None,
        region_id: str = None,
        scene_type: int = None,
        sort_by: str = None,
        workspace_id: int = None,
    ):
        self.is_sidecar_policy = is_sidecar_policy
        # Sort order. The value range is as follows:
        # 
        # - asc (default): ascending
        # 
        # - desc: descending
        self.order = order
        # Page number.
        self.page_number = page_number
        # Page size, the maximum number of results returned per page.
        # Maximum limit: 100.
        self.page_size = page_size
        # Policy identifier.
        self.policy_identifier = policy_identifier
        # Detection policy name.
        self.policy_name = policy_name
        # Region ID.
        self.region_id = region_id
        self.scene_type = scene_type
        # Sort field.
        self.sort_by = sort_by
        # Workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_sidecar_policy is not None:
            result['IsSidecarPolicy'] = self.is_sidecar_policy
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSidecarPolicy') is not None:
            self.is_sidecar_policy = m.get('IsSidecarPolicy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListPolicyResponseBodyPolicyInfoList(TeaModel):
    def __init__(
        self,
        gmt_modified: int = None,
        is_sidecar_policy: int = None,
        policy_id: int = None,
        policy_identifier: str = None,
        policy_name: str = None,
        scene_type: int = None,
    ):
        # Modification time.
        self.gmt_modified = gmt_modified
        self.is_sidecar_policy = is_sidecar_policy
        # Tag policy ID.
        self.policy_id = policy_id
        # Policy identifier.
        self.policy_identifier = policy_identifier
        # Permission policy name.
        self.policy_name = policy_name
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_sidecar_policy is not None:
            result['IsSidecarPolicy'] = self.is_sidecar_policy
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsSidecarPolicy') is not None:
            self.is_sidecar_policy = m.get('IsSidecarPolicy')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class ListPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_info_list: List[ListPolicyResponseBodyPolicyInfoList] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # Status code, 00000 indicates success; other values indicate failure.
        self.code = code
        # HTTP status code description.
        self.http_status_code = http_status_code
        # If there is an error, returns the error message.
        self.message = message
        # Page number, consistent with the PageNumber in the request.
        self.page_number = page_number
        # Page size, the maximum number of results returned per page.
        self.page_size = page_size
        # List of policy objects.
        self.policy_info_list = policy_info_list
        # Request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Possible values are:
        # - True: Call succeeded.
        # - False: Call failed.
        self.success = success
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.policy_info_list:
            for k in self.policy_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PolicyInfoList'] = []
        if self.policy_info_list is not None:
            for k in self.policy_info_list:
                result['PolicyInfoList'].append(k.to_map() if k else None)
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.policy_info_list = []
        if m.get('PolicyInfoList') is not None:
            for k in m.get('PolicyInfoList'):
                temp_model = ListPolicyResponseBodyPolicyInfoList()
                self.policy_info_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPolicyResponseBody = None,
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
            temp_model = ListPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicRequest(TeaModel):
    def __init__(
        self,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        sort_by: str = None,
        topic_name: str = None,
        workspace_id: int = None,
    ):
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.sort_by = sort_by
        self.topic_name = topic_name
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListTopicResponseBodyTopicInfoListPolicyInfoList(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
        policy_identifier: str = None,
        policy_name: str = None,
    ):
        self.policy_id = policy_id
        self.policy_identifier = policy_identifier
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class ListTopicResponseBodyTopicInfoList(TeaModel):
    def __init__(
        self,
        gmt_modified: int = None,
        policy_info_list: List[ListTopicResponseBodyTopicInfoListPolicyInfoList] = None,
        topic_definition: str = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        self.gmt_modified = gmt_modified
        self.policy_info_list = policy_info_list
        self.topic_definition = topic_definition
        self.topic_id = topic_id
        self.topic_name = topic_name

    def validate(self):
        if self.policy_info_list:
            for k in self.policy_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        result['PolicyInfoList'] = []
        if self.policy_info_list is not None:
            for k in self.policy_info_list:
                result['PolicyInfoList'].append(k.to_map() if k else None)
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        self.policy_info_list = []
        if m.get('PolicyInfoList') is not None:
            for k in m.get('PolicyInfoList'):
                temp_model = ListTopicResponseBodyTopicInfoListPolicyInfoList()
                self.policy_info_list.append(temp_model.from_map(k))
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ListTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        topic_info_list: List[ListTopicResponseBodyTopicInfoList] = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.topic_info_list = topic_info_list
        self.total_count = total_count

    def validate(self):
        if self.topic_info_list:
            for k in self.topic_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TopicInfoList'] = []
        if self.topic_info_list is not None:
            for k in self.topic_info_list:
                result['TopicInfoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.topic_info_list = []
        if m.get('TopicInfoList') is not None:
            for k in m.get('TopicInfoList'):
                temp_model = ListTopicResponseBodyTopicInfoList()
                self.topic_info_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTopicResponseBody = None,
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
            temp_model = ListTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWordGroupRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        sort_by: str = None,
        workspace_id: int = None,
    ):
        # Keyword group name.
        self.group_name = group_name
        # When performing a paginated query, sort the specified field in ascending or descending order. Values are as follows:
        # * asc: Ascending.
        # * desc: Descending.
        self.order = order
        # Page number.
        self.page_number = page_number
        # Page size, the maximum number of results returned per page.
        # Maximum limit: 100.
        self.page_size = page_size
        # Region ID.
        self.region_id = region_id
        # Sort field.
        self.sort_by = sort_by
        # Workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class ListWordGroupResponseBodyWordGroupInfoListPolicyInfoList(TeaModel):
    def __init__(
        self,
        policy_id: int = None,
        policy_identifier: str = None,
        policy_name: str = None,
    ):
        # Detection policy ID.
        self.policy_id = policy_id
        # Policy identifier.
        self.policy_identifier = policy_identifier
        # Detection policy name.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class ListWordGroupResponseBodyWordGroupInfoList(TeaModel):
    def __init__(
        self,
        gmt_modified: int = None,
        group_id: int = None,
        group_name: str = None,
        policy_info_list: List[ListWordGroupResponseBodyWordGroupInfoListPolicyInfoList] = None,
    ):
        # Policy modification time.
        self.gmt_modified = gmt_modified
        # Keyword group ID.
        self.group_id = group_id
        # Keyword group name.
        self.group_name = group_name
        # List of associated policy objects.
        self.policy_info_list = policy_info_list

    def validate(self):
        if self.policy_info_list:
            for k in self.policy_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        result['PolicyInfoList'] = []
        if self.policy_info_list is not None:
            for k in self.policy_info_list:
                result['PolicyInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        self.policy_info_list = []
        if m.get('PolicyInfoList') is not None:
            for k in m.get('PolicyInfoList'):
                temp_model = ListWordGroupResponseBodyWordGroupInfoListPolicyInfoList()
                self.policy_info_list.append(temp_model.from_map(k))
        return self


class ListWordGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        word_group_info_list: List[ListWordGroupResponseBodyWordGroupInfoList] = None,
    ):
        # Status code, 00000 indicates success; other values indicate failure.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # If an error occurs, returns the error message.
        self.message = message
        # Page number.
        self.page_number = page_number
        # Page size, the maximum number of results returned per page.
        # Maximum limit: 100.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Indicates whether the call was successful: true means the call was successful; false means the call failed.
        self.success = success
        # Total count.
        self.total_count = total_count
        # List of keyword group objects.
        self.word_group_info_list = word_group_info_list

    def validate(self):
        if self.word_group_info_list:
            for k in self.word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WordGroupInfoList'] = []
        if self.word_group_info_list is not None:
            for k in self.word_group_info_list:
                result['WordGroupInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.word_group_info_list = []
        if m.get('WordGroupInfoList') is not None:
            for k in m.get('WordGroupInfoList'):
                temp_model = ListWordGroupResponseBodyWordGroupInfoList()
                self.word_group_info_list.append(temp_model.from_map(k))
        return self


class ListWordGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWordGroupResponseBody = None,
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
            temp_model = ListWordGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModelInputContentAsyncDetectRequestBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # 1. The text content to be reviewed, with a maximum limit of 10000 characters (including English and Chinese).
        # 2. Or the URL address of the image to be reviewed.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ModelInputContentAsyncDetectRequest(TeaModel):
    def __init__(
        self,
        body_data: ModelInputContentAsyncDetectRequestBodyData = None,
        policy_identifier: str = None,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
    ):
        # Request object
        self.body_data = body_data
        # Policy ID
        self.policy_identifier = policy_identifier
        # Region ID.
        self.region_id = region_id
        # Scene name.
        self.scene_name = scene_name
        # Service name
        self.service_name = service_name

    def validate(self):
        if self.body_data:
            self.body_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data is not None:
            result['BodyData'] = self.body_data.to_map()
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = ModelInputContentAsyncDetectRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModelInputContentAsyncDetectShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        policy_identifier: str = None,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
    ):
        # Request object
        self.body_data_shrink = body_data_shrink
        # Policy ID
        self.policy_identifier = policy_identifier
        # Region ID.
        self.region_id = region_id
        # Scene name.
        self.scene_name = scene_name
        # Service name
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data_shrink is not None:
            result['BodyData'] = self.body_data_shrink
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModelInputContentAsyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # Result code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # 操作是否成功。true表示成功，false表示失败。
        self.success = success
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModelInputContentAsyncDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModelInputContentAsyncDetectResponseBody = None,
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
            temp_model = ModelInputContentAsyncDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModelInputContentSyncDetectRequestBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # 1. The text content to be checked, with a maximum limit of 10,000 characters (including English and Chinese).
        # 2. Or the URL address of the image to be checked.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ModelInputContentSyncDetectRequest(TeaModel):
    def __init__(
        self,
        body_data: ModelInputContentSyncDetectRequestBodyData = None,
        policy_identifier: str = None,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
    ):
        # Request object
        self.body_data = body_data
        # Policy Identifier
        self.policy_identifier = policy_identifier
        # Region ID.
        self.region_id = region_id
        # Scene name.
        self.scene_name = scene_name
        # Service name
        self.service_name = service_name

    def validate(self):
        if self.body_data:
            self.body_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data is not None:
            result['BodyData'] = self.body_data.to_map()
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = ModelInputContentSyncDetectRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModelInputContentSyncDetectShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        policy_identifier: str = None,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
    ):
        # Request object
        self.body_data_shrink = body_data_shrink
        # Policy Identifier
        self.policy_identifier = policy_identifier
        # Region ID.
        self.region_id = region_id
        # Scene name.
        self.scene_name = scene_name
        # Service name
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data_shrink is not None:
            result['BodyData'] = self.body_data_shrink
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoListBlockWordList(TeaModel):
    def __init__(
        self,
        word: str = None,
        word_label: str = None,
    ):
        # Keyword
        self.word = word
        # Label
        self.word_label = word_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['Word'] = self.word
        if self.word_label is not None:
            result['WordLabel'] = self.word_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')
        if m.get('WordLabel') is not None:
            self.word_label = m.get('WordLabel')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoList(TeaModel):
    def __init__(
        self,
        block_word_list: List[ModelInputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoListBlockWordList] = None,
        group_name: str = None,
    ):
        # List of keyword detection results
        self.block_word_list = block_word_list
        # Keyword group name
        self.group_name = group_name

    def validate(self):
        if self.block_word_list:
            for k in self.block_word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockWordList'] = []
        if self.block_word_list is not None:
            for k in self.block_word_list:
                result['BlockWordList'].append(k.to_map() if k else None)
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_word_list = []
        if m.get('BlockWordList') is not None:
            for k in m.get('BlockWordList'):
                temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoListBlockWordList()
                self.block_word_list.append(temp_model.from_map(k))
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoBlockWord(TeaModel):
    def __init__(
        self,
        block_word_group_info_list: List[ModelInputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoList] = None,
        risk_result: int = None,
    ):
        # List of keyword detection result objects
        self.block_word_group_info_list = block_word_group_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result

    def validate(self):
        if self.block_word_group_info_list:
            for k in self.block_word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockWordGroupInfoList'] = []
        if self.block_word_group_info_list is not None:
            for k in self.block_word_group_info_list:
                result['BlockWordGroupInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_word_group_info_list = []
        if m.get('BlockWordGroupInfoList') is not None:
            for k in m.get('BlockWordGroupInfoList'):
                temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoList()
                self.block_word_group_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoDenyTopicsTopicInfoList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
        topic_name: str = None,
    ):
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Topic name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoDenyTopics(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        risk_result: int = None,
        topic_info_list: List[ModelInputContentSyncDetectResponseBodyTraceInfoDenyTopicsTopicInfoList] = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Sensitive topic list
        self.topic_info_list = topic_info_list

    def validate(self):
        if self.topic_info_list:
            for k in self.topic_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        result['TopicInfoList'] = []
        if self.topic_info_list is not None:
            for k in self.topic_info_list:
                result['TopicInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        self.topic_info_list = []
        if m.get('TopicInfoList') is not None:
            for k in m.get('TopicInfoList'):
                temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoDenyTopicsTopicInfoList()
                self.topic_info_list.append(temp_model.from_map(k))
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
        sub_category_label: str = None,
    ):
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Subcategory label
        self.sub_category_label = sub_category_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.sub_category_label is not None:
            result['SubCategoryLabel'] = self.sub_category_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('SubCategoryLabel') is not None:
            self.sub_category_label = m.get('SubCategoryLabel')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategories(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        harmful_category_info_list: List[ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList] = None,
        risk_result: int = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # List of harmful category objects
        self.harmful_category_info_list = harmful_category_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result

    def validate(self):
        if self.harmful_category_info_list:
            for k in self.harmful_category_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        result['HarmfulCategoryInfoList'] = []
        if self.harmful_category_info_list is not None:
            for k in self.harmful_category_info_list:
                result['HarmfulCategoryInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        self.harmful_category_info_list = []
        if m.get('HarmfulCategoryInfoList') is not None:
            for k in m.get('HarmfulCategoryInfoList'):
                temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList()
                self.harmful_category_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttackPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttack(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        prompt_attack_info: str = None,
        prompt_attack_info_list: List[ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttackPromptAttackInfoList] = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # Prompt attack detection result object
        self.prompt_attack_info = prompt_attack_info
        # List of prompt attack objects
        self.prompt_attack_info_list = prompt_attack_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info = m.get('PromptAttackInfo')
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttackPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoSensitiveTypeSensitiveTypeInfoList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        masked_content: str = None,
        sensitive_category: int = None,
        sensitive_content: str = None,
        sensitive_type_name: str = None,
    ):
        self.action_type = action_type
        self.masked_content = masked_content
        self.sensitive_category = sensitive_category
        self.sensitive_content = sensitive_content
        self.sensitive_type_name = sensitive_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.masked_content is not None:
            result['MaskedContent'] = self.masked_content
        if self.sensitive_category is not None:
            result['SensitiveCategory'] = self.sensitive_category
        if self.sensitive_content is not None:
            result['SensitiveContent'] = self.sensitive_content
        if self.sensitive_type_name is not None:
            result['SensitiveTypeName'] = self.sensitive_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('MaskedContent') is not None:
            self.masked_content = m.get('MaskedContent')
        if m.get('SensitiveCategory') is not None:
            self.sensitive_category = m.get('SensitiveCategory')
        if m.get('SensitiveContent') is not None:
            self.sensitive_content = m.get('SensitiveContent')
        if m.get('SensitiveTypeName') is not None:
            self.sensitive_type_name = m.get('SensitiveTypeName')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfoSensitiveType(TeaModel):
    def __init__(
        self,
        masked_content: str = None,
        risk_result: int = None,
        sensitive_type_info_list: List[ModelInputContentSyncDetectResponseBodyTraceInfoSensitiveTypeSensitiveTypeInfoList] = None,
    ):
        self.masked_content = masked_content
        self.risk_result = risk_result
        self.sensitive_type_info_list = sensitive_type_info_list

    def validate(self):
        if self.sensitive_type_info_list:
            for k in self.sensitive_type_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.masked_content is not None:
            result['MaskedContent'] = self.masked_content
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        result['SensitiveTypeInfoList'] = []
        if self.sensitive_type_info_list is not None:
            for k in self.sensitive_type_info_list:
                result['SensitiveTypeInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaskedContent') is not None:
            self.masked_content = m.get('MaskedContent')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        self.sensitive_type_info_list = []
        if m.get('SensitiveTypeInfoList') is not None:
            for k in m.get('SensitiveTypeInfoList'):
                temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoSensitiveTypeSensitiveTypeInfoList()
                self.sensitive_type_info_list.append(temp_model.from_map(k))
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfo(TeaModel):
    def __init__(
        self,
        block_word: ModelInputContentSyncDetectResponseBodyTraceInfoBlockWord = None,
        deny_topics: ModelInputContentSyncDetectResponseBodyTraceInfoDenyTopics = None,
        harmful_categories: ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategories = None,
        prompt_attack: ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttack = None,
        sensitive_type: ModelInputContentSyncDetectResponseBodyTraceInfoSensitiveType = None,
    ):
        # Detected keywords
        self.block_word = block_word
        # Sensitive topic object list
        self.deny_topics = deny_topics
        # HarmfulCategories
        self.harmful_categories = harmful_categories
        # Prompt attack information
        self.prompt_attack = prompt_attack
        self.sensitive_type = sensitive_type

    def validate(self):
        if self.block_word:
            self.block_word.validate()
        if self.deny_topics:
            self.deny_topics.validate()
        if self.harmful_categories:
            self.harmful_categories.validate()
        if self.prompt_attack:
            self.prompt_attack.validate()
        if self.sensitive_type:
            self.sensitive_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_word is not None:
            result['BlockWord'] = self.block_word.to_map()
        if self.deny_topics is not None:
            result['DenyTopics'] = self.deny_topics.to_map()
        if self.harmful_categories is not None:
            result['HarmfulCategories'] = self.harmful_categories.to_map()
        if self.prompt_attack is not None:
            result['PromptAttack'] = self.prompt_attack.to_map()
        if self.sensitive_type is not None:
            result['SensitiveType'] = self.sensitive_type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockWord') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoBlockWord()
            self.block_word = temp_model.from_map(m['BlockWord'])
        if m.get('DenyTopics') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoDenyTopics()
            self.deny_topics = temp_model.from_map(m['DenyTopics'])
        if m.get('HarmfulCategories') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategories()
            self.harmful_categories = temp_model.from_map(m['HarmfulCategories'])
        if m.get('PromptAttack') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttack()
            self.prompt_attack = temp_model.from_map(m['PromptAttack'])
        if m.get('SensitiveType') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoSensitiveType()
            self.sensitive_type = temp_model.from_map(m['SensitiveType'])
        return self


class ModelInputContentSyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        risk_result: int = None,
        safe_answer: str = None,
        success: bool = None,
        trace_info: ModelInputContentSyncDetectResponseBodyTraceInfo = None,
    ):
        # Result code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        self.safe_answer = safe_answer
        # Whether the operation was successful. true indicates success, false indicates failure.
        self.success = success
        # Inspection result
        self.trace_info = trace_info

    def validate(self):
        if self.trace_info:
            self.trace_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.safe_answer is not None:
            result['SafeAnswer'] = self.safe_answer
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_info is not None:
            result['TraceInfo'] = self.trace_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SafeAnswer') is not None:
            self.safe_answer = m.get('SafeAnswer')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceInfo') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfo()
            self.trace_info = temp_model.from_map(m['TraceInfo'])
        return self


class ModelInputContentSyncDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModelInputContentSyncDetectResponseBody = None,
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
            temp_model = ModelInputContentSyncDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModelOutputContentAsyncDetectRequestBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # 1. The text content to be reviewed, with a maximum limit of 10000 characters (including English and Chinese).
        # 2. Or the URL address of the image to be reviewed.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ModelOutputContentAsyncDetectRequest(TeaModel):
    def __init__(
        self,
        body_data: ModelOutputContentAsyncDetectRequestBodyData = None,
        policy_identifier: str = None,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
    ):
        # Request object
        self.body_data = body_data
        # Policy ID
        self.policy_identifier = policy_identifier
        # Region ID.
        self.region_id = region_id
        # Scene name.
        self.scene_name = scene_name
        # Service name
        self.service_name = service_name

    def validate(self):
        if self.body_data:
            self.body_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data is not None:
            result['BodyData'] = self.body_data.to_map()
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = ModelOutputContentAsyncDetectRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModelOutputContentAsyncDetectShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        policy_identifier: str = None,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
    ):
        # Request object
        self.body_data_shrink = body_data_shrink
        # Policy ID
        self.policy_identifier = policy_identifier
        # Region ID.
        self.region_id = region_id
        # Scene name.
        self.scene_name = scene_name
        # Service name
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data_shrink is not None:
            result['BodyData'] = self.body_data_shrink
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModelOutputContentAsyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # 操作是否成功。true表示成功，false表示失败。
        self.success = success
        # Task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModelOutputContentAsyncDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModelOutputContentAsyncDetectResponseBody = None,
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
            temp_model = ModelOutputContentAsyncDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModelOutputContentSyncDetectRequestBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # 1. The text content to be reviewed, with a maximum limit of 10,000 characters (including English and Chinese).
        # 2. Or the URL address of the image to be reviewed.
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ModelOutputContentSyncDetectRequest(TeaModel):
    def __init__(
        self,
        body_data: ModelOutputContentSyncDetectRequestBodyData = None,
        policy_identifier: str = None,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
    ):
        # Request object
        self.body_data = body_data
        # Policy ID
        self.policy_identifier = policy_identifier
        # Region ID.
        self.region_id = region_id
        # Scene name.
        self.scene_name = scene_name
        # Service name
        self.service_name = service_name

    def validate(self):
        if self.body_data:
            self.body_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data is not None:
            result['BodyData'] = self.body_data.to_map()
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = ModelOutputContentSyncDetectRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModelOutputContentSyncDetectShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        policy_identifier: str = None,
        region_id: str = None,
        scene_name: str = None,
        service_name: str = None,
    ):
        # Request object
        self.body_data_shrink = body_data_shrink
        # Policy ID
        self.policy_identifier = policy_identifier
        # Region ID.
        self.region_id = region_id
        # Scene name.
        self.scene_name = scene_name
        # Service name
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data_shrink is not None:
            result['BodyData'] = self.body_data_shrink
        if self.policy_identifier is not None:
            result['PolicyIdentifier'] = self.policy_identifier
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('PolicyIdentifier') is not None:
            self.policy_identifier = m.get('PolicyIdentifier')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoListBlockWordList(TeaModel):
    def __init__(
        self,
        word: str = None,
        word_label: str = None,
    ):
        # Keyword
        self.word = word
        # Label
        self.word_label = word_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.word is not None:
            result['Word'] = self.word
        if self.word_label is not None:
            result['WordLabel'] = self.word_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Word') is not None:
            self.word = m.get('Word')
        if m.get('WordLabel') is not None:
            self.word_label = m.get('WordLabel')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoList(TeaModel):
    def __init__(
        self,
        block_word_list: List[ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoListBlockWordList] = None,
        group_name: str = None,
    ):
        # List of keyword detection result objects
        self.block_word_list = block_word_list
        # Keyword group name
        self.group_name = group_name

    def validate(self):
        if self.block_word_list:
            for k in self.block_word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockWordList'] = []
        if self.block_word_list is not None:
            for k in self.block_word_list:
                result['BlockWordList'].append(k.to_map() if k else None)
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_word_list = []
        if m.get('BlockWordList') is not None:
            for k in m.get('BlockWordList'):
                temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoListBlockWordList()
                self.block_word_list.append(temp_model.from_map(k))
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWord(TeaModel):
    def __init__(
        self,
        block_word_group_info_list: List[ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoList] = None,
        risk_result: int = None,
    ):
        # List of keyword detection result objects
        self.block_word_group_info_list = block_word_group_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result

    def validate(self):
        if self.block_word_group_info_list:
            for k in self.block_word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BlockWordGroupInfoList'] = []
        if self.block_word_group_info_list is not None:
            for k in self.block_word_group_info_list:
                result['BlockWordGroupInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_word_group_info_list = []
        if m.get('BlockWordGroupInfoList') is not None:
            for k in m.get('BlockWordGroupInfoList'):
                temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWordBlockWordGroupInfoList()
                self.block_word_group_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoDenyTopicsTopicInfoList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
        topic_name: str = None,
    ):
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk present
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Topic name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoDenyTopics(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        risk_result: int = None,
        topic_info_list: List[ModelOutputContentSyncDetectResponseBodyTraceInfoDenyTopicsTopicInfoList] = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # 0: No risk
        # 1: Risk present
        self.risk_result = risk_result
        # Sensitive topic list
        self.topic_info_list = topic_info_list

    def validate(self):
        if self.topic_info_list:
            for k in self.topic_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        result['TopicInfoList'] = []
        if self.topic_info_list is not None:
            for k in self.topic_info_list:
                result['TopicInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        self.topic_info_list = []
        if m.get('TopicInfoList') is not None:
            for k in m.get('TopicInfoList'):
                temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoDenyTopicsTopicInfoList()
                self.topic_info_list.append(temp_model.from_map(k))
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
        sub_category_label: str = None,
    ):
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Subcategory label
        self.sub_category_label = sub_category_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.sub_category_label is not None:
            result['SubCategoryLabel'] = self.sub_category_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('SubCategoryLabel') is not None:
            self.sub_category_label = m.get('SubCategoryLabel')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategories(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        harmful_category_info_list: List[ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList] = None,
        risk_result: int = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # List of harmful category objects
        self.harmful_category_info_list = harmful_category_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result

    def validate(self):
        if self.harmful_category_info_list:
            for k in self.harmful_category_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        result['HarmfulCategoryInfoList'] = []
        if self.harmful_category_info_list is not None:
            for k in self.harmful_category_info_list:
                result['HarmfulCategoryInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        self.harmful_category_info_list = []
        if m.get('HarmfulCategoryInfoList') is not None:
            for k in m.get('HarmfulCategoryInfoList'):
                temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList()
                self.harmful_category_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttackPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # 0: No risk
        # 1: Risk present
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttack(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        prompt_attack_info: str = None,
        prompt_attack_info_list: List[ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttackPromptAttackInfoList] = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        # Confidence score
        self.confidence_score = confidence_score
        # Prompt attack detection result object
        self.prompt_attack_info = prompt_attack_info
        # List of prompt attacks
        self.prompt_attack_info_list = prompt_attack_info_list
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidenceScore') is not None:
            self.confidence_score = m.get('ConfidenceScore')
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info = m.get('PromptAttackInfo')
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttackPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoSensitiveTypeSensitiveTypeInfoList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        masked_content: str = None,
        sensitive_category: int = None,
        sensitive_content: str = None,
        sensitive_type_name: str = None,
    ):
        self.action_type = action_type
        self.masked_content = masked_content
        self.sensitive_category = sensitive_category
        self.sensitive_content = sensitive_content
        self.sensitive_type_name = sensitive_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.masked_content is not None:
            result['MaskedContent'] = self.masked_content
        if self.sensitive_category is not None:
            result['SensitiveCategory'] = self.sensitive_category
        if self.sensitive_content is not None:
            result['SensitiveContent'] = self.sensitive_content
        if self.sensitive_type_name is not None:
            result['SensitiveTypeName'] = self.sensitive_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('MaskedContent') is not None:
            self.masked_content = m.get('MaskedContent')
        if m.get('SensitiveCategory') is not None:
            self.sensitive_category = m.get('SensitiveCategory')
        if m.get('SensitiveContent') is not None:
            self.sensitive_content = m.get('SensitiveContent')
        if m.get('SensitiveTypeName') is not None:
            self.sensitive_type_name = m.get('SensitiveTypeName')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfoSensitiveType(TeaModel):
    def __init__(
        self,
        masked_content: str = None,
        risk_result: int = None,
        sensitive_type_info_list: List[ModelOutputContentSyncDetectResponseBodyTraceInfoSensitiveTypeSensitiveTypeInfoList] = None,
    ):
        self.masked_content = masked_content
        self.risk_result = risk_result
        self.sensitive_type_info_list = sensitive_type_info_list

    def validate(self):
        if self.sensitive_type_info_list:
            for k in self.sensitive_type_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.masked_content is not None:
            result['MaskedContent'] = self.masked_content
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        result['SensitiveTypeInfoList'] = []
        if self.sensitive_type_info_list is not None:
            for k in self.sensitive_type_info_list:
                result['SensitiveTypeInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaskedContent') is not None:
            self.masked_content = m.get('MaskedContent')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        self.sensitive_type_info_list = []
        if m.get('SensitiveTypeInfoList') is not None:
            for k in m.get('SensitiveTypeInfoList'):
                temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoSensitiveTypeSensitiveTypeInfoList()
                self.sensitive_type_info_list.append(temp_model.from_map(k))
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfo(TeaModel):
    def __init__(
        self,
        block_word: ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWord = None,
        deny_topics: ModelOutputContentSyncDetectResponseBodyTraceInfoDenyTopics = None,
        harmful_categories: ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategories = None,
        prompt_attack: ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttack = None,
        sensitive_type: ModelOutputContentSyncDetectResponseBodyTraceInfoSensitiveType = None,
    ):
        # Detected keywords
        self.block_word = block_word
        # Sensitive topic object list
        self.deny_topics = deny_topics
        # HarmfulCategories
        self.harmful_categories = harmful_categories
        # Prompt attack information
        self.prompt_attack = prompt_attack
        self.sensitive_type = sensitive_type

    def validate(self):
        if self.block_word:
            self.block_word.validate()
        if self.deny_topics:
            self.deny_topics.validate()
        if self.harmful_categories:
            self.harmful_categories.validate()
        if self.prompt_attack:
            self.prompt_attack.validate()
        if self.sensitive_type:
            self.sensitive_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_word is not None:
            result['BlockWord'] = self.block_word.to_map()
        if self.deny_topics is not None:
            result['DenyTopics'] = self.deny_topics.to_map()
        if self.harmful_categories is not None:
            result['HarmfulCategories'] = self.harmful_categories.to_map()
        if self.prompt_attack is not None:
            result['PromptAttack'] = self.prompt_attack.to_map()
        if self.sensitive_type is not None:
            result['SensitiveType'] = self.sensitive_type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockWord') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWord()
            self.block_word = temp_model.from_map(m['BlockWord'])
        if m.get('DenyTopics') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoDenyTopics()
            self.deny_topics = temp_model.from_map(m['DenyTopics'])
        if m.get('HarmfulCategories') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategories()
            self.harmful_categories = temp_model.from_map(m['HarmfulCategories'])
        if m.get('PromptAttack') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttack()
            self.prompt_attack = temp_model.from_map(m['PromptAttack'])
        if m.get('SensitiveType') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoSensitiveType()
            self.sensitive_type = temp_model.from_map(m['SensitiveType'])
        return self


class ModelOutputContentSyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        risk_info: str = None,
        risk_result: int = None,
        safe_answer: str = None,
        success: bool = None,
        trace_info: ModelOutputContentSyncDetectResponseBodyTraceInfo = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code
        self.http_status_code = http_status_code
        # Error message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Risk labels, separated by commas if multiple.
        self.risk_info = risk_info
        # 0: No risk
        # 1: Risk exists
        self.risk_result = risk_result
        self.safe_answer = safe_answer
        # 操作是否成功。true表示成功，false表示失败。
        self.success = success
        # Inspection result
        self.trace_info = trace_info

    def validate(self):
        if self.trace_info:
            self.trace_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.risk_info is not None:
            result['RiskInfo'] = self.risk_info
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.safe_answer is not None:
            result['SafeAnswer'] = self.safe_answer
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_info is not None:
            result['TraceInfo'] = self.trace_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RiskInfo') is not None:
            self.risk_info = m.get('RiskInfo')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SafeAnswer') is not None:
            self.safe_answer = m.get('SafeAnswer')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceInfo') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfo()
            self.trace_info = temp_model.from_map(m['TraceInfo'])
        return self


class ModelOutputContentSyncDetectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModelOutputContentSyncDetectResponseBody = None,
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
            temp_model = ModelOutputContentSyncDetectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterAccountRequest(TeaModel):
    def __init__(
        self,
        memo: str = None,
        region_id: str = None,
    ):
        self.memo = memo
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RegisterAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RegisterAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterAccountResponseBody = None,
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
            temp_model = RegisterAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModelInstanceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        eas_service_id: str = None,
        eas_service_name: str = None,
        model_call_name: str = None,
        model_category_id: int = None,
        model_instance_id: int = None,
        model_token: str = None,
        model_url: str = None,
        model_vpc_url: str = None,
        workspace_id: int = None,
    ):
        self.description = description
        self.eas_service_id = eas_service_id
        self.eas_service_name = eas_service_name
        self.model_call_name = model_call_name
        self.model_category_id = model_category_id
        self.model_instance_id = model_instance_id
        self.model_token = model_token
        self.model_url = model_url
        self.model_vpc_url = model_vpc_url
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.eas_service_id is not None:
            result['EasServiceId'] = self.eas_service_id
        if self.eas_service_name is not None:
            result['EasServiceName'] = self.eas_service_name
        if self.model_call_name is not None:
            result['ModelCallName'] = self.model_call_name
        if self.model_category_id is not None:
            result['ModelCategoryId'] = self.model_category_id
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        if self.model_token is not None:
            result['ModelToken'] = self.model_token
        if self.model_url is not None:
            result['ModelUrl'] = self.model_url
        if self.model_vpc_url is not None:
            result['ModelVpcUrl'] = self.model_vpc_url
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EasServiceId') is not None:
            self.eas_service_id = m.get('EasServiceId')
        if m.get('EasServiceName') is not None:
            self.eas_service_name = m.get('EasServiceName')
        if m.get('ModelCallName') is not None:
            self.model_call_name = m.get('ModelCallName')
        if m.get('ModelCategoryId') is not None:
            self.model_category_id = m.get('ModelCategoryId')
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        if m.get('ModelToken') is not None:
            self.model_token = m.get('ModelToken')
        if m.get('ModelUrl') is not None:
            self.model_url = m.get('ModelUrl')
        if m.get('ModelVpcUrl') is not None:
            self.model_vpc_url = m.get('ModelVpcUrl')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdateModelInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        model_instance_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.model_instance_id = model_instance_id
        # Id of the request
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model_instance_id is not None:
            result['ModelInstanceId'] = self.model_instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModelInstanceId') is not None:
            self.model_instance_id = m.get('ModelInstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateModelInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModelInstanceResponseBody = None,
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
            temp_model = UpdateModelInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePolicyRequestHarmfulCategoryConfigInfoList(TeaModel):
    def __init__(
        self,
        category_config_id: int = None,
        category_id: int = None,
        category_label: str = None,
        category_type: int = None,
        input_output_type: int = None,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category configuration ID
        self.category_config_id = category_config_id
        self.category_id = category_id
        # Category name
        self.category_label = category_label
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type
        # Prompt attack configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_config_id is not None:
            result['CategoryConfigId'] = self.category_config_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryConfigId') is not None:
            self.category_config_id = m.get('CategoryConfigId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class UpdatePolicyRequestPromptAttackInfo(TeaModel):
    def __init__(
        self,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Prompt attack configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class UpdatePolicyRequestPromptAttackInfoList(TeaModel):
    def __init__(
        self,
        category_config_id: int = None,
        category_id: int = None,
        category_label: str = None,
        is_enabled: int = None,
        security_level: int = None,
    ):
        # Harmful category configuration ID
        self.category_config_id = category_config_id
        self.category_id = category_id
        # Category name
        self.category_label = category_label
        # Prompt attack configuration switch
        # 0: Off
        # 1: On
        self.is_enabled = is_enabled
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_config_id is not None:
            result['CategoryConfigId'] = self.category_config_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_label is not None:
            result['CategoryLabel'] = self.category_label
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryConfigId') is not None:
            self.category_config_id = m.get('CategoryConfigId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLabel') is not None:
            self.category_label = m.get('CategoryLabel')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class UpdatePolicyRequestRegularExpressList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        regular_express: str = None,
        regular_express_name: str = None,
    ):
        self.action_type = action_type
        self.regular_express = regular_express
        self.regular_express_name = regular_express_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.regular_express is not None:
            result['RegularExpress'] = self.regular_express
        if self.regular_express_name is not None:
            result['RegularExpressName'] = self.regular_express_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('RegularExpress') is not None:
            self.regular_express = m.get('RegularExpress')
        if m.get('RegularExpressName') is not None:
            self.regular_express_name = m.get('RegularExpressName')
        return self


class UpdatePolicyRequestSensitiveConfigList(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        is_enabled: int = None,
        sensitive_config_id: int = None,
    ):
        self.action_type = action_type
        self.is_enabled = is_enabled
        self.sensitive_config_id = sensitive_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled
        if self.sensitive_config_id is not None:
            result['SensitiveConfigId'] = self.sensitive_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')
        if m.get('SensitiveConfigId') is not None:
            self.sensitive_config_id = m.get('SensitiveConfigId')
        return self


class UpdatePolicyRequestSensitiveTopicListTopicExampleInfoList(TeaModel):
    def __init__(
        self,
        content: str = None,
        example_type: int = None,
    ):
        self.content = content
        self.example_type = example_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.example_type is not None:
            result['ExampleType'] = self.example_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExampleType') is not None:
            self.example_type = m.get('ExampleType')
        return self


class UpdatePolicyRequestSensitiveTopicList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        security_level: int = None,
        topic_definition: str = None,
        topic_example_info_list: List[UpdatePolicyRequestSensitiveTopicListTopicExampleInfoList] = None,
        topic_name: str = None,
    ):
        self.category_type = category_type
        self.security_level = security_level
        self.topic_definition = topic_definition
        self.topic_example_info_list = topic_example_info_list
        self.topic_name = topic_name

    def validate(self):
        if self.topic_example_info_list:
            for k in self.topic_example_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        result['TopicExampleInfoList'] = []
        if self.topic_example_info_list is not None:
            for k in self.topic_example_info_list:
                result['TopicExampleInfoList'].append(k.to_map() if k else None)
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        self.topic_example_info_list = []
        if m.get('TopicExampleInfoList') is not None:
            for k in m.get('TopicExampleInfoList'):
                temp_model = UpdatePolicyRequestSensitiveTopicListTopicExampleInfoList()
                self.topic_example_info_list.append(temp_model.from_map(k))
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class UpdatePolicyRequestSensitiveWordList(TeaModel):
    def __init__(
        self,
        label: str = None,
        word: str = None,
    ):
        self.label = label
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class UpdatePolicyRequestTopicConfigInfoList(TeaModel):
    def __init__(
        self,
        category_type: int = None,
        input_output_type: int = None,
        security_level: int = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        # 0: Text
        # 1: Image
        self.category_type = category_type
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type
        # Security level
        # 0: Low
        # 1: Medium
        # 2: High
        self.security_level = security_level
        # Sensitive topic ID
        self.topic_id = topic_id
        # Topic name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_type is not None:
            result['CategoryType'] = self.category_type
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryType') is not None:
            self.category_type = m.get('CategoryType')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class UpdatePolicyRequestWordGroupInfoList(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        group_name: str = None,
        input_output_type: int = None,
    ):
        # Keyword group ID.
        self.group_id = group_id
        # Keyword group name
        self.group_name = group_name
        # Model input/output type
        # 0: Input
        # 1: Output
        self.input_output_type = input_output_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.input_output_type is not None:
            result['InputOutputType'] = self.input_output_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InputOutputType') is not None:
            self.input_output_type = m.get('InputOutputType')
        return self


class UpdatePolicyRequest(TeaModel):
    def __init__(
        self,
        content_safe_model_instance_id: int = None,
        enable_sensitive_input_check: int = None,
        enable_sensitive_output_check: int = None,
        harmful_category_config_info_list: List[UpdatePolicyRequestHarmfulCategoryConfigInfoList] = None,
        input_safe_answer: str = None,
        input_safe_answer_switch: int = None,
        is_sidecar_policy: int = None,
        output_safe_answer: str = None,
        output_safe_answer_switch: int = None,
        policy_id: int = None,
        policy_name: str = None,
        prompt_attack_info: UpdatePolicyRequestPromptAttackInfo = None,
        prompt_attack_info_list: List[UpdatePolicyRequestPromptAttackInfoList] = None,
        prompt_attack_model_instance_id: int = None,
        region_id: str = None,
        regular_express_list: List[UpdatePolicyRequestRegularExpressList] = None,
        scene_type: int = None,
        sensitive_config_list: List[UpdatePolicyRequestSensitiveConfigList] = None,
        sensitive_topic_list: List[UpdatePolicyRequestSensitiveTopicList] = None,
        sensitive_topic_model_instance_id: int = None,
        sensitive_word_list: List[UpdatePolicyRequestSensitiveWordList] = None,
        topic_config_info_list: List[UpdatePolicyRequestTopicConfigInfoList] = None,
        word_group_info_list: List[UpdatePolicyRequestWordGroupInfoList] = None,
        workspace_id: int = None,
    ):
        self.content_safe_model_instance_id = content_safe_model_instance_id
        self.enable_sensitive_input_check = enable_sensitive_input_check
        self.enable_sensitive_output_check = enable_sensitive_output_check
        # List of harmful category configurations
        self.harmful_category_config_info_list = harmful_category_config_info_list
        self.input_safe_answer = input_safe_answer
        self.input_safe_answer_switch = input_safe_answer_switch
        self.is_sidecar_policy = is_sidecar_policy
        self.output_safe_answer = output_safe_answer
        self.output_safe_answer_switch = output_safe_answer_switch
        # Detection policy ID
        self.policy_id = policy_id
        # Detection policy name.
        self.policy_name = policy_name
        # Prompt attack detection result object
        self.prompt_attack_info = prompt_attack_info
        # List of prompt attacks
        self.prompt_attack_info_list = prompt_attack_info_list
        self.prompt_attack_model_instance_id = prompt_attack_model_instance_id
        # Region ID.
        self.region_id = region_id
        self.regular_express_list = regular_express_list
        self.scene_type = scene_type
        self.sensitive_config_list = sensitive_config_list
        self.sensitive_topic_list = sensitive_topic_list
        self.sensitive_topic_model_instance_id = sensitive_topic_model_instance_id
        self.sensitive_word_list = sensitive_word_list
        # List of sensitive topics
        self.topic_config_info_list = topic_config_info_list
        # List of keyword group objects
        self.word_group_info_list = word_group_info_list
        self.workspace_id = workspace_id

    def validate(self):
        if self.harmful_category_config_info_list:
            for k in self.harmful_category_config_info_list:
                if k:
                    k.validate()
        if self.prompt_attack_info:
            self.prompt_attack_info.validate()
        if self.prompt_attack_info_list:
            for k in self.prompt_attack_info_list:
                if k:
                    k.validate()
        if self.regular_express_list:
            for k in self.regular_express_list:
                if k:
                    k.validate()
        if self.sensitive_config_list:
            for k in self.sensitive_config_list:
                if k:
                    k.validate()
        if self.sensitive_topic_list:
            for k in self.sensitive_topic_list:
                if k:
                    k.validate()
        if self.sensitive_word_list:
            for k in self.sensitive_word_list:
                if k:
                    k.validate()
        if self.topic_config_info_list:
            for k in self.topic_config_info_list:
                if k:
                    k.validate()
        if self.word_group_info_list:
            for k in self.word_group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_safe_model_instance_id is not None:
            result['ContentSafeModelInstanceId'] = self.content_safe_model_instance_id
        if self.enable_sensitive_input_check is not None:
            result['EnableSensitiveInputCheck'] = self.enable_sensitive_input_check
        if self.enable_sensitive_output_check is not None:
            result['EnableSensitiveOutputCheck'] = self.enable_sensitive_output_check
        result['HarmfulCategoryConfigInfoList'] = []
        if self.harmful_category_config_info_list is not None:
            for k in self.harmful_category_config_info_list:
                result['HarmfulCategoryConfigInfoList'].append(k.to_map() if k else None)
        if self.input_safe_answer is not None:
            result['InputSafeAnswer'] = self.input_safe_answer
        if self.input_safe_answer_switch is not None:
            result['InputSafeAnswerSwitch'] = self.input_safe_answer_switch
        if self.is_sidecar_policy is not None:
            result['IsSidecarPolicy'] = self.is_sidecar_policy
        if self.output_safe_answer is not None:
            result['OutputSafeAnswer'] = self.output_safe_answer
        if self.output_safe_answer_switch is not None:
            result['OutputSafeAnswerSwitch'] = self.output_safe_answer_switch
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info.to_map()
        result['PromptAttackInfoList'] = []
        if self.prompt_attack_info_list is not None:
            for k in self.prompt_attack_info_list:
                result['PromptAttackInfoList'].append(k.to_map() if k else None)
        if self.prompt_attack_model_instance_id is not None:
            result['PromptAttackModelInstanceId'] = self.prompt_attack_model_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RegularExpressList'] = []
        if self.regular_express_list is not None:
            for k in self.regular_express_list:
                result['RegularExpressList'].append(k.to_map() if k else None)
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        result['SensitiveConfigList'] = []
        if self.sensitive_config_list is not None:
            for k in self.sensitive_config_list:
                result['SensitiveConfigList'].append(k.to_map() if k else None)
        result['SensitiveTopicList'] = []
        if self.sensitive_topic_list is not None:
            for k in self.sensitive_topic_list:
                result['SensitiveTopicList'].append(k.to_map() if k else None)
        if self.sensitive_topic_model_instance_id is not None:
            result['SensitiveTopicModelInstanceId'] = self.sensitive_topic_model_instance_id
        result['SensitiveWordList'] = []
        if self.sensitive_word_list is not None:
            for k in self.sensitive_word_list:
                result['SensitiveWordList'].append(k.to_map() if k else None)
        result['TopicConfigInfoList'] = []
        if self.topic_config_info_list is not None:
            for k in self.topic_config_info_list:
                result['TopicConfigInfoList'].append(k.to_map() if k else None)
        result['WordGroupInfoList'] = []
        if self.word_group_info_list is not None:
            for k in self.word_group_info_list:
                result['WordGroupInfoList'].append(k.to_map() if k else None)
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentSafeModelInstanceId') is not None:
            self.content_safe_model_instance_id = m.get('ContentSafeModelInstanceId')
        if m.get('EnableSensitiveInputCheck') is not None:
            self.enable_sensitive_input_check = m.get('EnableSensitiveInputCheck')
        if m.get('EnableSensitiveOutputCheck') is not None:
            self.enable_sensitive_output_check = m.get('EnableSensitiveOutputCheck')
        self.harmful_category_config_info_list = []
        if m.get('HarmfulCategoryConfigInfoList') is not None:
            for k in m.get('HarmfulCategoryConfigInfoList'):
                temp_model = UpdatePolicyRequestHarmfulCategoryConfigInfoList()
                self.harmful_category_config_info_list.append(temp_model.from_map(k))
        if m.get('InputSafeAnswer') is not None:
            self.input_safe_answer = m.get('InputSafeAnswer')
        if m.get('InputSafeAnswerSwitch') is not None:
            self.input_safe_answer_switch = m.get('InputSafeAnswerSwitch')
        if m.get('IsSidecarPolicy') is not None:
            self.is_sidecar_policy = m.get('IsSidecarPolicy')
        if m.get('OutputSafeAnswer') is not None:
            self.output_safe_answer = m.get('OutputSafeAnswer')
        if m.get('OutputSafeAnswerSwitch') is not None:
            self.output_safe_answer_switch = m.get('OutputSafeAnswerSwitch')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PromptAttackInfo') is not None:
            temp_model = UpdatePolicyRequestPromptAttackInfo()
            self.prompt_attack_info = temp_model.from_map(m['PromptAttackInfo'])
        self.prompt_attack_info_list = []
        if m.get('PromptAttackInfoList') is not None:
            for k in m.get('PromptAttackInfoList'):
                temp_model = UpdatePolicyRequestPromptAttackInfoList()
                self.prompt_attack_info_list.append(temp_model.from_map(k))
        if m.get('PromptAttackModelInstanceId') is not None:
            self.prompt_attack_model_instance_id = m.get('PromptAttackModelInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.regular_express_list = []
        if m.get('RegularExpressList') is not None:
            for k in m.get('RegularExpressList'):
                temp_model = UpdatePolicyRequestRegularExpressList()
                self.regular_express_list.append(temp_model.from_map(k))
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        self.sensitive_config_list = []
        if m.get('SensitiveConfigList') is not None:
            for k in m.get('SensitiveConfigList'):
                temp_model = UpdatePolicyRequestSensitiveConfigList()
                self.sensitive_config_list.append(temp_model.from_map(k))
        self.sensitive_topic_list = []
        if m.get('SensitiveTopicList') is not None:
            for k in m.get('SensitiveTopicList'):
                temp_model = UpdatePolicyRequestSensitiveTopicList()
                self.sensitive_topic_list.append(temp_model.from_map(k))
        if m.get('SensitiveTopicModelInstanceId') is not None:
            self.sensitive_topic_model_instance_id = m.get('SensitiveTopicModelInstanceId')
        self.sensitive_word_list = []
        if m.get('SensitiveWordList') is not None:
            for k in m.get('SensitiveWordList'):
                temp_model = UpdatePolicyRequestSensitiveWordList()
                self.sensitive_word_list.append(temp_model.from_map(k))
        self.topic_config_info_list = []
        if m.get('TopicConfigInfoList') is not None:
            for k in m.get('TopicConfigInfoList'):
                temp_model = UpdatePolicyRequestTopicConfigInfoList()
                self.topic_config_info_list.append(temp_model.from_map(k))
        self.word_group_info_list = []
        if m.get('WordGroupInfoList') is not None:
            for k in m.get('WordGroupInfoList'):
                temp_model = UpdatePolicyRequestWordGroupInfoList()
                self.word_group_info_list.append(temp_model.from_map(k))
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdatePolicyShrinkRequest(TeaModel):
    def __init__(
        self,
        content_safe_model_instance_id: int = None,
        enable_sensitive_input_check: int = None,
        enable_sensitive_output_check: int = None,
        harmful_category_config_info_list_shrink: str = None,
        input_safe_answer: str = None,
        input_safe_answer_switch: int = None,
        is_sidecar_policy: int = None,
        output_safe_answer: str = None,
        output_safe_answer_switch: int = None,
        policy_id: int = None,
        policy_name: str = None,
        prompt_attack_info_shrink: str = None,
        prompt_attack_info_list_shrink: str = None,
        prompt_attack_model_instance_id: int = None,
        region_id: str = None,
        regular_express_list_shrink: str = None,
        scene_type: int = None,
        sensitive_config_list_shrink: str = None,
        sensitive_topic_list_shrink: str = None,
        sensitive_topic_model_instance_id: int = None,
        sensitive_word_list_shrink: str = None,
        topic_config_info_list_shrink: str = None,
        word_group_info_list_shrink: str = None,
        workspace_id: int = None,
    ):
        self.content_safe_model_instance_id = content_safe_model_instance_id
        self.enable_sensitive_input_check = enable_sensitive_input_check
        self.enable_sensitive_output_check = enable_sensitive_output_check
        # List of harmful category configurations
        self.harmful_category_config_info_list_shrink = harmful_category_config_info_list_shrink
        self.input_safe_answer = input_safe_answer
        self.input_safe_answer_switch = input_safe_answer_switch
        self.is_sidecar_policy = is_sidecar_policy
        self.output_safe_answer = output_safe_answer
        self.output_safe_answer_switch = output_safe_answer_switch
        # Detection policy ID
        self.policy_id = policy_id
        # Detection policy name.
        self.policy_name = policy_name
        # Prompt attack detection result object
        self.prompt_attack_info_shrink = prompt_attack_info_shrink
        # List of prompt attacks
        self.prompt_attack_info_list_shrink = prompt_attack_info_list_shrink
        self.prompt_attack_model_instance_id = prompt_attack_model_instance_id
        # Region ID.
        self.region_id = region_id
        self.regular_express_list_shrink = regular_express_list_shrink
        self.scene_type = scene_type
        self.sensitive_config_list_shrink = sensitive_config_list_shrink
        self.sensitive_topic_list_shrink = sensitive_topic_list_shrink
        self.sensitive_topic_model_instance_id = sensitive_topic_model_instance_id
        self.sensitive_word_list_shrink = sensitive_word_list_shrink
        # List of sensitive topics
        self.topic_config_info_list_shrink = topic_config_info_list_shrink
        # List of keyword group objects
        self.word_group_info_list_shrink = word_group_info_list_shrink
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_safe_model_instance_id is not None:
            result['ContentSafeModelInstanceId'] = self.content_safe_model_instance_id
        if self.enable_sensitive_input_check is not None:
            result['EnableSensitiveInputCheck'] = self.enable_sensitive_input_check
        if self.enable_sensitive_output_check is not None:
            result['EnableSensitiveOutputCheck'] = self.enable_sensitive_output_check
        if self.harmful_category_config_info_list_shrink is not None:
            result['HarmfulCategoryConfigInfoList'] = self.harmful_category_config_info_list_shrink
        if self.input_safe_answer is not None:
            result['InputSafeAnswer'] = self.input_safe_answer
        if self.input_safe_answer_switch is not None:
            result['InputSafeAnswerSwitch'] = self.input_safe_answer_switch
        if self.is_sidecar_policy is not None:
            result['IsSidecarPolicy'] = self.is_sidecar_policy
        if self.output_safe_answer is not None:
            result['OutputSafeAnswer'] = self.output_safe_answer
        if self.output_safe_answer_switch is not None:
            result['OutputSafeAnswerSwitch'] = self.output_safe_answer_switch
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.prompt_attack_info_shrink is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info_shrink
        if self.prompt_attack_info_list_shrink is not None:
            result['PromptAttackInfoList'] = self.prompt_attack_info_list_shrink
        if self.prompt_attack_model_instance_id is not None:
            result['PromptAttackModelInstanceId'] = self.prompt_attack_model_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.regular_express_list_shrink is not None:
            result['RegularExpressList'] = self.regular_express_list_shrink
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        if self.sensitive_config_list_shrink is not None:
            result['SensitiveConfigList'] = self.sensitive_config_list_shrink
        if self.sensitive_topic_list_shrink is not None:
            result['SensitiveTopicList'] = self.sensitive_topic_list_shrink
        if self.sensitive_topic_model_instance_id is not None:
            result['SensitiveTopicModelInstanceId'] = self.sensitive_topic_model_instance_id
        if self.sensitive_word_list_shrink is not None:
            result['SensitiveWordList'] = self.sensitive_word_list_shrink
        if self.topic_config_info_list_shrink is not None:
            result['TopicConfigInfoList'] = self.topic_config_info_list_shrink
        if self.word_group_info_list_shrink is not None:
            result['WordGroupInfoList'] = self.word_group_info_list_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentSafeModelInstanceId') is not None:
            self.content_safe_model_instance_id = m.get('ContentSafeModelInstanceId')
        if m.get('EnableSensitiveInputCheck') is not None:
            self.enable_sensitive_input_check = m.get('EnableSensitiveInputCheck')
        if m.get('EnableSensitiveOutputCheck') is not None:
            self.enable_sensitive_output_check = m.get('EnableSensitiveOutputCheck')
        if m.get('HarmfulCategoryConfigInfoList') is not None:
            self.harmful_category_config_info_list_shrink = m.get('HarmfulCategoryConfigInfoList')
        if m.get('InputSafeAnswer') is not None:
            self.input_safe_answer = m.get('InputSafeAnswer')
        if m.get('InputSafeAnswerSwitch') is not None:
            self.input_safe_answer_switch = m.get('InputSafeAnswerSwitch')
        if m.get('IsSidecarPolicy') is not None:
            self.is_sidecar_policy = m.get('IsSidecarPolicy')
        if m.get('OutputSafeAnswer') is not None:
            self.output_safe_answer = m.get('OutputSafeAnswer')
        if m.get('OutputSafeAnswerSwitch') is not None:
            self.output_safe_answer_switch = m.get('OutputSafeAnswerSwitch')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info_shrink = m.get('PromptAttackInfo')
        if m.get('PromptAttackInfoList') is not None:
            self.prompt_attack_info_list_shrink = m.get('PromptAttackInfoList')
        if m.get('PromptAttackModelInstanceId') is not None:
            self.prompt_attack_model_instance_id = m.get('PromptAttackModelInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegularExpressList') is not None:
            self.regular_express_list_shrink = m.get('RegularExpressList')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        if m.get('SensitiveConfigList') is not None:
            self.sensitive_config_list_shrink = m.get('SensitiveConfigList')
        if m.get('SensitiveTopicList') is not None:
            self.sensitive_topic_list_shrink = m.get('SensitiveTopicList')
        if m.get('SensitiveTopicModelInstanceId') is not None:
            self.sensitive_topic_model_instance_id = m.get('SensitiveTopicModelInstanceId')
        if m.get('SensitiveWordList') is not None:
            self.sensitive_word_list_shrink = m.get('SensitiveWordList')
        if m.get('TopicConfigInfoList') is not None:
            self.topic_config_info_list_shrink = m.get('TopicConfigInfoList')
        if m.get('WordGroupInfoList') is not None:
            self.word_group_info_list_shrink = m.get('WordGroupInfoList')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class UpdatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Whether the operation was successful. true indicates success, false indicates failure.
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePolicyResponseBody = None,
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
            temp_model = UpdatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTopicRequestBodyDataTopicExampleInfoList(TeaModel):
    def __init__(
        self,
        content: str = None,
        example_type: int = None,
    ):
        self.content = content
        self.example_type = example_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.example_type is not None:
            result['ExampleType'] = self.example_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExampleType') is not None:
            self.example_type = m.get('ExampleType')
        return self


class UpdateTopicRequestBodyData(TeaModel):
    def __init__(
        self,
        topic_example_info_list: List[UpdateTopicRequestBodyDataTopicExampleInfoList] = None,
    ):
        self.topic_example_info_list = topic_example_info_list

    def validate(self):
        if self.topic_example_info_list:
            for k in self.topic_example_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TopicExampleInfoList'] = []
        if self.topic_example_info_list is not None:
            for k in self.topic_example_info_list:
                result['TopicExampleInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topic_example_info_list = []
        if m.get('TopicExampleInfoList') is not None:
            for k in m.get('TopicExampleInfoList'):
                temp_model = UpdateTopicRequestBodyDataTopicExampleInfoList()
                self.topic_example_info_list.append(temp_model.from_map(k))
        return self


class UpdateTopicRequest(TeaModel):
    def __init__(
        self,
        body_data: UpdateTopicRequestBodyData = None,
        region_id: str = None,
        topic_definition: str = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        self.body_data = body_data
        self.region_id = region_id
        self.topic_definition = topic_definition
        self.topic_id = topic_id
        self.topic_name = topic_name

    def validate(self):
        if self.body_data:
            self.body_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data is not None:
            result['BodyData'] = self.body_data.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = UpdateTopicRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class UpdateTopicShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        region_id: str = None,
        topic_definition: str = None,
        topic_id: int = None,
        topic_name: str = None,
    ):
        self.body_data_shrink = body_data_shrink
        self.region_id = region_id
        self.topic_definition = topic_definition
        self.topic_id = topic_id
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data_shrink is not None:
            result['BodyData'] = self.body_data_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.topic_definition is not None:
            result['TopicDefinition'] = self.topic_definition
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_name is not None:
            result['TopicName'] = self.topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TopicDefinition') is not None:
            self.topic_definition = m.get('TopicDefinition')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')
        return self


class UpdateTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTopicResponseBody = None,
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
            temp_model = UpdateTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWordGroupRequestBodyDataWordInfoList(TeaModel):
    def __init__(
        self,
        label: str = None,
        word: str = None,
    ):
        # Label.
        self.label = label
        # Keyword.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class UpdateWordGroupRequestBodyData(TeaModel):
    def __init__(
        self,
        word_info_list: List[UpdateWordGroupRequestBodyDataWordInfoList] = None,
    ):
        # List of keyword groups.
        self.word_info_list = word_info_list

    def validate(self):
        if self.word_info_list:
            for k in self.word_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['WordInfoList'] = []
        if self.word_info_list is not None:
            for k in self.word_info_list:
                result['WordInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.word_info_list = []
        if m.get('WordInfoList') is not None:
            for k in m.get('WordInfoList'):
                temp_model = UpdateWordGroupRequestBodyDataWordInfoList()
                self.word_info_list.append(temp_model.from_map(k))
        return self


class UpdateWordGroupRequest(TeaModel):
    def __init__(
        self,
        body_data: UpdateWordGroupRequestBodyData = None,
        commit: bool = None,
        group_id: int = None,
        group_name: str = None,
        region_id: str = None,
        word_info_list_modified: bool = None,
    ):
        # Request object.
        self.body_data = body_data
        # Whether to commit.
        # false: Not actually saved, only checked
        # true: Commit and save
        self.commit = commit
        # Keyword group ID.
        self.group_id = group_id
        # Keyword group name.
        self.group_name = group_name
        # Region ID.
        self.region_id = region_id
        # Whether the keyword information has been modified.
        self.word_info_list_modified = word_info_list_modified

    def validate(self):
        if self.body_data:
            self.body_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data is not None:
            result['BodyData'] = self.body_data.to_map()
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.word_info_list_modified is not None:
            result['WordInfoListModified'] = self.word_info_list_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = UpdateWordGroupRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WordInfoListModified') is not None:
            self.word_info_list_modified = m.get('WordInfoListModified')
        return self


class UpdateWordGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        commit: bool = None,
        group_id: int = None,
        group_name: str = None,
        region_id: str = None,
        word_info_list_modified: bool = None,
    ):
        # Request object.
        self.body_data_shrink = body_data_shrink
        # Whether to commit.
        # false: Not actually saved, only checked
        # true: Commit and save
        self.commit = commit
        # Keyword group ID.
        self.group_id = group_id
        # Keyword group name.
        self.group_name = group_name
        # Region ID.
        self.region_id = region_id
        # Whether the keyword information has been modified.
        self.word_info_list_modified = word_info_list_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_data_shrink is not None:
            result['BodyData'] = self.body_data_shrink
        if self.commit is not None:
            result['Commit'] = self.commit
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.word_info_list_modified is not None:
            result['WordInfoListModified'] = self.word_info_list_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WordInfoListModified') is not None:
            self.word_info_list_modified = m.get('WordInfoListModified')
        return self


class UpdateWordGroupResponseBodyWordErrorInfoList(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        error_status: int = None,
        index: int = None,
        label: str = None,
        word: str = None,
    ):
        # Error message description.
        self.error_message = error_message
        # Error status information.
        self.error_status = error_status
        # Position of the error information in the array.
        self.index = index
        # Label.
        self.label = label
        # Keyword.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_status is not None:
            result['ErrorStatus'] = self.error_status
        if self.index is not None:
            result['Index'] = self.index
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorStatus') is not None:
            self.error_status = m.get('ErrorStatus')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class UpdateWordGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        word_error_info_list: List[UpdateWordGroupResponseBodyWordErrorInfoList] = None,
    ):
        # Status code, 00000 indicates success; others indicate failure.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # If there is an error, return the error message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Whether it was successful.
        self.success = success
        # List of error information.
        self.word_error_info_list = word_error_info_list

    def validate(self):
        if self.word_error_info_list:
            for k in self.word_error_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['WordErrorInfoList'] = []
        if self.word_error_info_list is not None:
            for k in self.word_error_info_list:
                result['WordErrorInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.word_error_info_list = []
        if m.get('WordErrorInfoList') is not None:
            for k in m.get('WordErrorInfoList'):
                temp_model = UpdateWordGroupResponseBodyWordErrorInfoList()
                self.word_error_info_list.append(temp_model.from_map(k))
        return self


class UpdateWordGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWordGroupResponseBody = None,
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
            temp_model = UpdateWordGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


