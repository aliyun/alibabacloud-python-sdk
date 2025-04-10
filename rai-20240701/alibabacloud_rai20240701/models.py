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


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoListBlockWordList(TeaModel):
    def __init__(
        self,
        word: str = None,
        word_label: str = None,
    ):
        self.word = word
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
        self.block_word_list = block_word_list
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
        self.block_word_group_info_list = block_word_group_info_list
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


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        self.category_label = category_label
        self.category_type = category_type
        self.risk_result = risk_result
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


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        harmful_category_info_list: List[GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList] = None,
        risk_result: int = None,
    ):
        self.confidence_score = confidence_score
        self.harmful_category_info_list = harmful_category_info_list
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


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack(TeaModel):
    def __init__(
        self,
        prompt_attack_info: str = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        self.prompt_attack_info = prompt_attack_info
        self.risk_result = risk_result
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info = m.get('PromptAttackInfo')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfo(TeaModel):
    def __init__(
        self,
        block_word: GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWord = None,
        harmful_categories: GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories = None,
        prompt_attack: GetModelInputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack = None,
    ):
        self.block_word = block_word
        self.harmful_categories = harmful_categories
        self.prompt_attack = prompt_attack

    def validate(self):
        if self.block_word:
            self.block_word.validate()
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
        self.risk_result = risk_result
        self.status = status
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
        self.code = code
        self.detect_result_list = detect_result_list
        self.http_status_code = http_status_code
        self.message = message
        self.processed_count = processed_count
        self.request_id = request_id
        self.success = success
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


class GetModelOutputContentDetectResultRequest(TeaModel):
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


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWordBlockWordGroupInfoListBlockWordList(TeaModel):
    def __init__(
        self,
        word: str = None,
        word_label: str = None,
    ):
        self.word = word
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
        self.block_word_list = block_word_list
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
        self.block_word_group_info_list = block_word_group_info_list
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


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        self.category_label = category_label
        self.category_type = category_type
        self.risk_result = risk_result
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


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        harmful_category_info_list: List[GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategoriesHarmfulCategoryInfoList] = None,
        risk_result: int = None,
    ):
        self.confidence_score = confidence_score
        self.harmful_category_info_list = harmful_category_info_list
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


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack(TeaModel):
    def __init__(
        self,
        prompt_attack_info: str = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        self.prompt_attack_info = prompt_attack_info
        self.risk_result = risk_result
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info = m.get('PromptAttackInfo')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfo(TeaModel):
    def __init__(
        self,
        block_word: GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoBlockWord = None,
        harmful_categories: GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoHarmfulCategories = None,
        prompt_attack: GetModelOutputContentDetectResultResponseBodyDetectResultListTraceInfoPromptAttack = None,
    ):
        self.block_word = block_word
        self.harmful_categories = harmful_categories
        self.prompt_attack = prompt_attack

    def validate(self):
        if self.block_word:
            self.block_word.validate()
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
        self.risk_result = risk_result
        self.status = status
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
        self.code = code
        self.detect_result_list = detect_result_list
        self.http_status_code = http_status_code
        self.message = message
        self.processed_count = processed_count
        self.request_id = request_id
        self.success = success
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


class ListSensitiveWordRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListSensitiveWordResponseBodyDataSensitiveWordList(TeaModel):
    def __init__(
        self,
        id: int = None,
        label: str = None,
        word: str = None,
    ):
        self.id = id
        self.label = label
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class ListSensitiveWordResponseBodyData(TeaModel):
    def __init__(
        self,
        max_count: int = None,
        page_number: int = None,
        page_size: int = None,
        sensitive_word_list: List[ListSensitiveWordResponseBodyDataSensitiveWordList] = None,
        total_count: int = None,
    ):
        self.max_count = max_count
        self.page_number = page_number
        self.page_size = page_size
        self.sensitive_word_list = sensitive_word_list
        self.total_count = total_count

    def validate(self):
        if self.sensitive_word_list:
            for k in self.sensitive_word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_count is not None:
            result['MaxCount'] = self.max_count
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['SensitiveWordList'] = []
        if self.sensitive_word_list is not None:
            for k in self.sensitive_word_list:
                result['SensitiveWordList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.sensitive_word_list = []
        if m.get('SensitiveWordList') is not None:
            for k in m.get('SensitiveWordList'):
                temp_model = ListSensitiveWordResponseBodyDataSensitiveWordList()
                self.sensitive_word_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSensitiveWordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListSensitiveWordResponseBodyData = None,
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
            temp_model = ListSensitiveWordResponseBodyData()
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


class ListSensitiveWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSensitiveWordResponseBody = None,
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
            temp_model = ListSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModelInputContentAsyncDetectRequestBodyData(TeaModel):
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
        self.body_data = body_data
        self.policy_identifier = policy_identifier
        self.region_id = region_id
        self.scene_name = scene_name
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
        self.body_data_shrink = body_data_shrink
        self.policy_identifier = policy_identifier
        self.region_id = region_id
        self.scene_name = scene_name
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
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
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
        self.body_data = body_data
        self.policy_identifier = policy_identifier
        self.region_id = region_id
        self.scene_name = scene_name
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
        self.body_data_shrink = body_data_shrink
        self.policy_identifier = policy_identifier
        self.region_id = region_id
        self.scene_name = scene_name
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
        self.word = word
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
        self.block_word_list = block_word_list
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
        self.block_word_group_info_list = block_word_group_info_list
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


class ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        self.category_label = category_label
        self.category_type = category_type
        self.risk_result = risk_result
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


class ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategories(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        harmful_category_info_list: List[ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList] = None,
        risk_result: int = None,
    ):
        self.confidence_score = confidence_score
        self.harmful_category_info_list = harmful_category_info_list
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


class ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttack(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        prompt_attack_info: str = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        self.confidence_score = confidence_score
        self.prompt_attack_info = prompt_attack_info
        self.risk_result = risk_result
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence_score is not None:
            result['ConfidenceScore'] = self.confidence_score
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info
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
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class ModelInputContentSyncDetectResponseBodyTraceInfo(TeaModel):
    def __init__(
        self,
        block_word: ModelInputContentSyncDetectResponseBodyTraceInfoBlockWord = None,
        harmful_categories: ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategories = None,
        prompt_attack: ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttack = None,
    ):
        self.block_word = block_word
        self.harmful_categories = harmful_categories
        self.prompt_attack = prompt_attack

    def validate(self):
        if self.block_word:
            self.block_word.validate()
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
        if self.harmful_categories is not None:
            result['HarmfulCategories'] = self.harmful_categories.to_map()
        if self.prompt_attack is not None:
            result['PromptAttack'] = self.prompt_attack.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockWord') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoBlockWord()
            self.block_word = temp_model.from_map(m['BlockWord'])
        if m.get('HarmfulCategories') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoHarmfulCategories()
            self.harmful_categories = temp_model.from_map(m['HarmfulCategories'])
        if m.get('PromptAttack') is not None:
            temp_model = ModelInputContentSyncDetectResponseBodyTraceInfoPromptAttack()
            self.prompt_attack = temp_model.from_map(m['PromptAttack'])
        return self


class ModelInputContentSyncDetectResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        risk_result: int = None,
        success: bool = None,
        trace_info: ModelInputContentSyncDetectResponseBodyTraceInfo = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.risk_result = risk_result
        self.success = success
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
        self.body_data = body_data
        self.policy_identifier = policy_identifier
        self.region_id = region_id
        self.scene_name = scene_name
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
        self.body_data_shrink = body_data_shrink
        self.policy_identifier = policy_identifier
        self.region_id = region_id
        self.scene_name = scene_name
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
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
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
        self.body_data = body_data
        self.policy_identifier = policy_identifier
        self.region_id = region_id
        self.scene_name = scene_name
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
        self.body_data_shrink = body_data_shrink
        self.policy_identifier = policy_identifier
        self.region_id = region_id
        self.scene_name = scene_name
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
        self.word = word
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
        self.block_word_list = block_word_list
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
        self.block_word_group_info_list = block_word_group_info_list
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


class ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList(TeaModel):
    def __init__(
        self,
        category_label: str = None,
        category_type: int = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        self.category_label = category_label
        self.category_type = category_type
        self.risk_result = risk_result
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


class ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategories(TeaModel):
    def __init__(
        self,
        confidence_score: float = None,
        harmful_category_info_list: List[ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategoriesHarmfulCategoryInfoList] = None,
        risk_result: int = None,
    ):
        self.confidence_score = confidence_score
        self.harmful_category_info_list = harmful_category_info_list
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


class ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttack(TeaModel):
    def __init__(
        self,
        prompt_attack_info: str = None,
        risk_result: int = None,
        security_level: int = None,
    ):
        self.prompt_attack_info = prompt_attack_info
        self.risk_result = risk_result
        self.security_level = security_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt_attack_info is not None:
            result['PromptAttackInfo'] = self.prompt_attack_info
        if self.risk_result is not None:
            result['RiskResult'] = self.risk_result
        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromptAttackInfo') is not None:
            self.prompt_attack_info = m.get('PromptAttackInfo')
        if m.get('RiskResult') is not None:
            self.risk_result = m.get('RiskResult')
        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')
        return self


class ModelOutputContentSyncDetectResponseBodyTraceInfo(TeaModel):
    def __init__(
        self,
        block_word: ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWord = None,
        harmful_categories: ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategories = None,
        prompt_attack: ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttack = None,
    ):
        self.block_word = block_word
        self.harmful_categories = harmful_categories
        self.prompt_attack = prompt_attack

    def validate(self):
        if self.block_word:
            self.block_word.validate()
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
        if self.harmful_categories is not None:
            result['HarmfulCategories'] = self.harmful_categories.to_map()
        if self.prompt_attack is not None:
            result['PromptAttack'] = self.prompt_attack.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockWord') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoBlockWord()
            self.block_word = temp_model.from_map(m['BlockWord'])
        if m.get('HarmfulCategories') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoHarmfulCategories()
            self.harmful_categories = temp_model.from_map(m['HarmfulCategories'])
        if m.get('PromptAttack') is not None:
            temp_model = ModelOutputContentSyncDetectResponseBodyTraceInfoPromptAttack()
            self.prompt_attack = temp_model.from_map(m['PromptAttack'])
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
        success: bool = None,
        trace_info: ModelOutputContentSyncDetectResponseBodyTraceInfo = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.risk_info = risk_info
        self.risk_result = risk_result
        self.success = success
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


class SyncSensitiveWordRequestBodyDataSensitiveWordList(TeaModel):
    def __init__(
        self,
        id: int = None,
        label: str = None,
        status: int = None,
        word: str = None,
    ):
        self.id = id
        self.label = label
        self.status = status
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.label is not None:
            result['Label'] = self.label
        if self.status is not None:
            result['Status'] = self.status
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class SyncSensitiveWordRequestBodyData(TeaModel):
    def __init__(
        self,
        sensitive_word_list: List[SyncSensitiveWordRequestBodyDataSensitiveWordList] = None,
    ):
        self.sensitive_word_list = sensitive_word_list

    def validate(self):
        if self.sensitive_word_list:
            for k in self.sensitive_word_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SensitiveWordList'] = []
        if self.sensitive_word_list is not None:
            for k in self.sensitive_word_list:
                result['SensitiveWordList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_word_list = []
        if m.get('SensitiveWordList') is not None:
            for k in m.get('SensitiveWordList'):
                temp_model = SyncSensitiveWordRequestBodyDataSensitiveWordList()
                self.sensitive_word_list.append(temp_model.from_map(k))
        return self


class SyncSensitiveWordRequest(TeaModel):
    def __init__(
        self,
        body_data: SyncSensitiveWordRequestBodyData = None,
        commit: bool = None,
        region_id: str = None,
    ):
        self.body_data = body_data
        self.commit = commit
        self.region_id = region_id

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            temp_model = SyncSensitiveWordRequestBodyData()
            self.body_data = temp_model.from_map(m['BodyData'])
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SyncSensitiveWordShrinkRequest(TeaModel):
    def __init__(
        self,
        body_data_shrink: str = None,
        commit: bool = None,
        region_id: str = None,
    ):
        self.body_data_shrink = body_data_shrink
        self.commit = commit
        self.region_id = region_id

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyData') is not None:
            self.body_data_shrink = m.get('BodyData')
        if m.get('Commit') is not None:
            self.commit = m.get('Commit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SyncSensitiveWordResponseBodyDataSensitiveWordErrorList(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        err_status: int = None,
        index: int = None,
        label: str = None,
        word: str = None,
    ):
        self.err_message = err_message
        self.err_status = err_status
        self.index = index
        self.label = label
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.err_status is not None:
            result['ErrStatus'] = self.err_status
        if self.index is not None:
            result['Index'] = self.index
        if self.label is not None:
            result['Label'] = self.label
        if self.word is not None:
            result['Word'] = self.word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrStatus') is not None:
            self.err_status = m.get('ErrStatus')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Word') is not None:
            self.word = m.get('Word')
        return self


class SyncSensitiveWordResponseBodyData(TeaModel):
    def __init__(
        self,
        sensitive_word_error_list: List[SyncSensitiveWordResponseBodyDataSensitiveWordErrorList] = None,
    ):
        self.sensitive_word_error_list = sensitive_word_error_list

    def validate(self):
        if self.sensitive_word_error_list:
            for k in self.sensitive_word_error_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SensitiveWordErrorList'] = []
        if self.sensitive_word_error_list is not None:
            for k in self.sensitive_word_error_list:
                result['SensitiveWordErrorList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_word_error_list = []
        if m.get('SensitiveWordErrorList') is not None:
            for k in m.get('SensitiveWordErrorList'):
                temp_model = SyncSensitiveWordResponseBodyDataSensitiveWordErrorList()
                self.sensitive_word_error_list.append(temp_model.from_map(k))
        return self


class SyncSensitiveWordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SyncSensitiveWordResponseBodyData = None,
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
            temp_model = SyncSensitiveWordResponseBodyData()
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


class SyncSensitiveWordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncSensitiveWordResponseBody = None,
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
            temp_model = SyncSensitiveWordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


