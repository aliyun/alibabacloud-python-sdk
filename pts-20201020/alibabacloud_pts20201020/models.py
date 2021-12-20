# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreatePtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene: str = None,
    ):
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class CreatePtsSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scene_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.scene_id = scene_id
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
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
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
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePtsSceneResponseBody = None,
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
            temp_model = CreatePtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePtsSceneBaseLineFromReportRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
        scene_id: str = None,
    ):
        self.report_id = report_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class CreatePtsSceneBaseLineFromReportResponseBody(TeaModel):
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


class CreatePtsSceneBaseLineFromReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePtsSceneBaseLineFromReportResponseBody = None,
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
            temp_model = CreatePtsSceneBaseLineFromReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DeletePtsSceneResponseBody(TeaModel):
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


class DeletePtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePtsSceneResponseBody = None,
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
            temp_model = DeletePtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePtsSceneBaseLineRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class DeletePtsSceneBaseLineResponseBody(TeaModel):
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


class DeletePtsSceneBaseLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePtsSceneBaseLineResponseBody = None,
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
            temp_model = DeletePtsSceneBaseLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePtsScenesRequest(TeaModel):
    def __init__(
        self,
        scene_ids: Dict[str, Any] = None,
    ):
        self.scene_ids = scene_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_ids is not None:
            result['SceneIds'] = self.scene_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneIds') is not None:
            self.scene_ids = m.get('SceneIds')
        return self


class DeletePtsScenesShrinkRequest(TeaModel):
    def __init__(
        self,
        scene_ids_shrink: str = None,
    ):
        self.scene_ids_shrink = scene_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_ids_shrink is not None:
            result['SceneIds'] = self.scene_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneIds') is not None:
            self.scene_ids_shrink = m.get('SceneIds')
        return self


class DeletePtsScenesResponseBody(TeaModel):
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


class DeletePtsScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePtsScenesResponseBody = None,
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
            temp_model = DeletePtsScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJMeterLogsRequest(TeaModel):
    def __init__(
        self,
        agent_index: int = None,
        begin_time: int = None,
        end_time: int = None,
        keyword: str = None,
        level: str = None,
        page_number: int = None,
        page_size: int = None,
        report_id: str = None,
        thread: str = None,
    ):
        # 第几台引擎，起始为0
        self.agent_index = agent_index
        # 开始时间
        self.begin_time = begin_time
        # 结束时间
        self.end_time = end_time
        # 关键字
        self.keyword = keyword
        # 日志等级
        self.level = level
        self.page_number = page_number
        self.page_size = page_size
        # 报告ID
        self.report_id = report_id
        # 线程名
        self.thread = thread

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_index is not None:
            result['AgentIndex'] = self.agent_index
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.level is not None:
            result['Level'] = self.level
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.thread is not None:
            result['Thread'] = self.thread
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentIndex') is not None:
            self.agent_index = m.get('AgentIndex')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        return self


class GetJMeterLogsResponseBody(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        code: str = None,
        logs: List[Dict[str, Any]] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # 引擎数量，想要获得第几台引擎的日志可以根据引擎数量传值
        self.agent_count = agent_count
        self.code = code
        # 日志内容
        self.logs = logs
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_count is not None:
            result['AgentCount'] = self.agent_count
        if self.code is not None:
            result['Code'] = self.code
        if self.logs is not None:
            result['Logs'] = self.logs
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Logs') is not None:
            self.logs = m.get('Logs')
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
        return self


class GetJMeterLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJMeterLogsResponseBody = None,
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
            temp_model = GetJMeterLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJMeterSampleMetricsRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        report_id: str = None,
        sampler_id: int = None,
    ):
        # 开始时间
        self.begin_time = begin_time
        # 结束时间
        self.end_time = end_time
        # 报告ID
        self.report_id = report_id
        # 采样器索引，从0开始。-1返回全场景
        self.sampler_id = sampler_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.sampler_id is not None:
            result['SamplerId'] = self.sampler_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('SamplerId') is not None:
            self.sampler_id = m.get('SamplerId')
        return self


class GetJMeterSampleMetricsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        sample_metric_list: List[str] = None,
        sampler_map: Dict[str, Any] = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        # 采样器聚合数据列表
        self.sample_metric_list = sample_metric_list
        # 采样器列表，可根据该列表传递需要查询的采样器
        self.sampler_map = sampler_map
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample_metric_list is not None:
            result['SampleMetricList'] = self.sample_metric_list
        if self.sampler_map is not None:
            result['SamplerMap'] = self.sampler_map
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SampleMetricList') is not None:
            self.sample_metric_list = m.get('SampleMetricList')
        if m.get('SamplerMap') is not None:
            self.sampler_map = m.get('SamplerMap')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJMeterSampleMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJMeterSampleMetricsResponseBody = None,
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
            temp_model = GetJMeterSampleMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJMeterSamplingLogsRequest(TeaModel):
    def __init__(
        self,
        agent_id: int = None,
        begin_time: int = None,
        end_time: int = None,
        keyword: str = None,
        max_rt: int = None,
        min_rt: int = None,
        page_number: int = None,
        page_size: int = None,
        report_id: str = None,
        response_code: str = None,
        sampler_id: int = None,
        success: bool = None,
        thread: str = None,
    ):
        # 压测引擎编号
        self.agent_id = agent_id
        # 开始时间
        self.begin_time = begin_time
        # 结束时间
        self.end_time = end_time
        # 关键字
        self.keyword = keyword
        # 最大响应时间，单位ms
        self.max_rt = max_rt
        # 最小响应时间，单位ms
        self.min_rt = min_rt
        self.page_number = page_number
        self.page_size = page_size
        # 报告ID
        self.report_id = report_id
        self.response_code = response_code
        # 第几个采样器，从0开始
        self.sampler_id = sampler_id
        # 采样结果是否成功
        self.success = success
        # 线程
        self.thread = thread

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_rt is not None:
            result['MaxRT'] = self.max_rt
        if self.min_rt is not None:
            result['MinRT'] = self.min_rt
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.response_code is not None:
            result['ResponseCode'] = self.response_code
        if self.sampler_id is not None:
            result['SamplerId'] = self.sampler_id
        if self.success is not None:
            result['Success'] = self.success
        if self.thread is not None:
            result['Thread'] = self.thread
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxRT') is not None:
            self.max_rt = m.get('MaxRT')
        if m.get('MinRT') is not None:
            self.min_rt = m.get('MinRT')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ResponseCode') is not None:
            self.response_code = m.get('ResponseCode')
        if m.get('SamplerId') is not None:
            self.sampler_id = m.get('SamplerId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        return self


class GetJMeterSamplingLogsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sample_results: List[str] = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        # 采样器的采样结果
        self.sample_results = sample_results
        self.success = success
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sample_results is not None:
            result['SampleResults'] = self.sample_results
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SampleResults') is not None:
            self.sample_results = m.get('SampleResults')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetJMeterSamplingLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJMeterSamplingLogsResponseBody = None,
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
            temp_model = GetJMeterSamplingLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJMeterSceneRunningDataRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetJMeterSceneRunningDataResponseBodyRunningData(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        agent_id_list: List[str] = None,
        all_sample_stat: Dict[str, Any] = None,
        concurrency: int = None,
        has_report: bool = None,
        hold_for: int = None,
        is_debugging: bool = None,
        sample_stat_list: List[Dict[str, Any]] = None,
        scene_id: str = None,
        scene_name: str = None,
        stage_name: str = None,
        start_time_ts: int = None,
        status: str = None,
        vum: int = None,
    ):
        # 压测引擎数量
        self.agent_count = agent_count
        # 压测引擎列表
        self.agent_id_list = agent_id_list
        # 场景整体的采样状态
        self.all_sample_stat = all_sample_stat
        # 并发量
        self.concurrency = concurrency
        # 是否生成了报告
        self.has_report = has_report
        # 压测计划持续时间，单位s
        self.hold_for = hold_for
        # 是否是调试
        self.is_debugging = is_debugging
        # 每一个采样器的状态
        self.sample_stat_list = sample_stat_list
        # 场景id
        self.scene_id = scene_id
        # 场景名称
        self.scene_name = scene_name
        # 当前所处阶段
        self.stage_name = stage_name
        # 压测计划开始时间戳，单位ms
        self.start_time_ts = start_time_ts
        # 状态
        self.status = status
        # 目前消耗的vum
        self.vum = vum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_count is not None:
            result['AgentCount'] = self.agent_count
        if self.agent_id_list is not None:
            result['AgentIdList'] = self.agent_id_list
        if self.all_sample_stat is not None:
            result['AllSampleStat'] = self.all_sample_stat
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.has_report is not None:
            result['HasReport'] = self.has_report
        if self.hold_for is not None:
            result['HoldFor'] = self.hold_for
        if self.is_debugging is not None:
            result['IsDebugging'] = self.is_debugging
        if self.sample_stat_list is not None:
            result['SampleStatList'] = self.sample_stat_list
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.start_time_ts is not None:
            result['StartTimeTS'] = self.start_time_ts
        if self.status is not None:
            result['Status'] = self.status
        if self.vum is not None:
            result['Vum'] = self.vum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        if m.get('AgentIdList') is not None:
            self.agent_id_list = m.get('AgentIdList')
        if m.get('AllSampleStat') is not None:
            self.all_sample_stat = m.get('AllSampleStat')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('HasReport') is not None:
            self.has_report = m.get('HasReport')
        if m.get('HoldFor') is not None:
            self.hold_for = m.get('HoldFor')
        if m.get('IsDebugging') is not None:
            self.is_debugging = m.get('IsDebugging')
        if m.get('SampleStatList') is not None:
            self.sample_stat_list = m.get('SampleStatList')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('StartTimeTS') is not None:
            self.start_time_ts = m.get('StartTimeTS')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vum') is not None:
            self.vum = m.get('Vum')
        return self


class GetJMeterSceneRunningDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        document_url: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        running_data: GetJMeterSceneRunningDataResponseBodyRunningData = None,
        success: bool = None,
    ):
        self.code = code
        self.document_url = document_url
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        # 运行中的数据
        self.running_data = running_data
        self.success = success

    def validate(self):
        if self.running_data:
            self.running_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.running_data is not None:
            result['RunningData'] = self.running_data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunningData') is not None:
            temp_model = GetJMeterSceneRunningDataResponseBodyRunningData()
            self.running_data = temp_model.from_map(m['RunningData'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJMeterSceneRunningDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJMeterSceneRunningDataResponseBody = None,
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
            temp_model = GetJMeterSceneRunningDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetOpenJMeterSceneResponseBodySceneBaseInfo(TeaModel):
    def __init__(
        self,
        create_name: str = None,
        modify_name: str = None,
        operate_type: str = None,
        principal: str = None,
        remark: str = None,
        resource: str = None,
    ):
        # 创建人名
        self.create_name = create_name
        # 修改人名
        self.modify_name = modify_name
        # 操作类型
        self.operate_type = operate_type
        # 场景压测负责人
        self.principal = principal
        # 备注
        self.remark = remark
        # 场景来源
        self.resource = resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_name is not None:
            result['CreateName'] = self.create_name
        if self.modify_name is not None:
            result['ModifyName'] = self.modify_name
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.principal is not None:
            result['Principal'] = self.principal
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource is not None:
            result['Resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateName') is not None:
            self.create_name = m.get('CreateName')
        if m.get('ModifyName') is not None:
            self.modify_name = m.get('ModifyName')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Principal') is not None:
            self.principal = m.get('Principal')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        return self


class GetOpenJMeterSceneResponseBodySceneDnsCacheConfig(TeaModel):
    def __init__(
        self,
        clear_cache_each_iteration: bool = None,
        dns_servers: List[str] = None,
        host_table: Dict[str, Any] = None,
    ):
        # 是否清除缓存
        self.clear_cache_each_iteration = clear_cache_each_iteration
        # DNS服务器
        self.dns_servers = dns_servers
        # 域名绑定
        self.host_table = host_table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clear_cache_each_iteration is not None:
            result['ClearCacheEachIteration'] = self.clear_cache_each_iteration
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers
        if self.host_table is not None:
            result['HostTable'] = self.host_table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClearCacheEachIteration') is not None:
            self.clear_cache_each_iteration = m.get('ClearCacheEachIteration')
        if m.get('DnsServers') is not None:
            self.dns_servers = m.get('DnsServers')
        if m.get('HostTable') is not None:
            self.host_table = m.get('HostTable')
        return self


class GetOpenJMeterSceneResponseBodySceneFileList(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_oss_address: str = None,
        file_size: int = None,
        file_type: str = None,
        id: int = None,
        md_5: str = None,
        split_csv: bool = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件地址
        self.file_oss_address = file_oss_address
        # 文件大小
        self.file_size = file_size
        # 文件类型
        self.file_type = file_type
        # 文件ID
        self.id = id
        # 文件的md5值
        self.md_5 = md_5
        # csv文件是否切分
        self.split_csv = split_csv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_oss_address is not None:
            result['FileOssAddress'] = self.file_oss_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.id is not None:
            result['Id'] = self.id
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.split_csv is not None:
            result['SplitCsv'] = self.split_csv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileOssAddress') is not None:
            self.file_oss_address = m.get('FileOssAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('SplitCsv') is not None:
            self.split_csv = m.get('SplitCsv')
        return self


class GetOpenJMeterSceneResponseBodyScene(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        base_info: GetOpenJMeterSceneResponseBodySceneBaseInfo = None,
        concurrency: int = None,
        constant_throughput_timer_type: str = None,
        dns_cache_config: GetOpenJMeterSceneResponseBodySceneDnsCacheConfig = None,
        duration: int = None,
        environment_id: str = None,
        file_list: List[GetOpenJMeterSceneResponseBodySceneFileList] = None,
        is_vpc_test: bool = None,
        ramp_up: int = None,
        region_id: str = None,
        scene_id: str = None,
        scene_name: str = None,
        security_group_id: str = None,
        steps: int = None,
        sync_timer_type: str = None,
        test_file: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # 施压机数量
        self.agent_count = agent_count
        # 基本信息
        self.base_info = base_info
        # 最大并发
        self.concurrency = concurrency
        # constantThroughputTimerType
        self.constant_throughput_timer_type = constant_throughput_timer_type
        # DNS配置
        self.dns_cache_config = dns_cache_config
        # 压测持续时间，单位为s
        self.duration = duration
        # 环境id
        self.environment_id = environment_id
        # 文件列表
        self.file_list = file_list
        # 是否为VPC压测
        self.is_vpc_test = is_vpc_test
        # 递增时间，单位s
        self.ramp_up = ramp_up
        # VPC压测时配置
        self.region_id = region_id
        # 场景id
        self.scene_id = scene_id
        # 场景名
        self.scene_name = scene_name
        # 安全组id，VPC压测时配置
        self.security_group_id = security_group_id
        # 递增阶梯数。预热时间和预热阶段数都不配置时 使用固定压力值 只配置预热时间，不配置阶段数时 使用均匀递增 预热时间和阶段数都配置时，并且steps<rampUp 使用阶梯递增 不能只配置steps，不配置rampUp 如果这样配置，默认使用固定压力值
        self.steps = steps
        # synchronizing timer 类型
        self.sync_timer_type = sync_timer_type
        # 测试文件
        self.test_file = test_file
        # 交换机id，VPC压测时配置
        self.v_switch_id = v_switch_id
        # vpc的id，VPC压测时配置
        self.vpc_id = vpc_id

    def validate(self):
        if self.base_info:
            self.base_info.validate()
        if self.dns_cache_config:
            self.dns_cache_config.validate()
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_count is not None:
            result['AgentCount'] = self.agent_count
        if self.base_info is not None:
            result['BaseInfo'] = self.base_info.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.constant_throughput_timer_type is not None:
            result['ConstantThroughputTimerType'] = self.constant_throughput_timer_type
        if self.dns_cache_config is not None:
            result['DnsCacheConfig'] = self.dns_cache_config.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.is_vpc_test is not None:
            result['IsVpcTest'] = self.is_vpc_test
        if self.ramp_up is not None:
            result['RampUp'] = self.ramp_up
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.steps is not None:
            result['Steps'] = self.steps
        if self.sync_timer_type is not None:
            result['SyncTimerType'] = self.sync_timer_type
        if self.test_file is not None:
            result['TestFile'] = self.test_file
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        if m.get('BaseInfo') is not None:
            temp_model = GetOpenJMeterSceneResponseBodySceneBaseInfo()
            self.base_info = temp_model.from_map(m['BaseInfo'])
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConstantThroughputTimerType') is not None:
            self.constant_throughput_timer_type = m.get('ConstantThroughputTimerType')
        if m.get('DnsCacheConfig') is not None:
            temp_model = GetOpenJMeterSceneResponseBodySceneDnsCacheConfig()
            self.dns_cache_config = temp_model.from_map(m['DnsCacheConfig'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = GetOpenJMeterSceneResponseBodySceneFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('IsVpcTest') is not None:
            self.is_vpc_test = m.get('IsVpcTest')
        if m.get('RampUp') is not None:
            self.ramp_up = m.get('RampUp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Steps') is not None:
            self.steps = m.get('Steps')
        if m.get('SyncTimerType') is not None:
            self.sync_timer_type = m.get('SyncTimerType')
        if m.get('TestFile') is not None:
            self.test_file = m.get('TestFile')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetOpenJMeterSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scene: GetOpenJMeterSceneResponseBodyScene = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        # 场景详情
        self.scene = scene
        self.success = success

    def validate(self):
        if self.scene:
            self.scene.validate()

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
        if self.scene is not None:
            result['Scene'] = self.scene.to_map()
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
        if m.get('Scene') is not None:
            temp_model = GetOpenJMeterSceneResponseBodyScene()
            self.scene = temp_model.from_map(m['Scene'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOpenJMeterSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOpenJMeterSceneResponseBody = None,
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
            temp_model = GetOpenJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsReportDetailsRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        scene_id: str = None,
    ):
        self.plan_id = plan_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetPtsReportDetailsResponseBodyApiMetricsList(TeaModel):
    def __init__(
        self,
        all_count: int = None,
        api_name: str = None,
        avg_rt: float = None,
        avg_tps: float = None,
        fail_count_biz: int = None,
        fail_count_req: int = None,
        max_rt: float = None,
        min_rt: float = None,
        seg_50rt: float = None,
        seg_75rt: float = None,
        seg_90rt: float = None,
        seg_99rt: float = None,
        success_rate_biz: float = None,
        success_rate_req: float = None,
    ):
        self.all_count = all_count
        self.api_name = api_name
        self.avg_rt = avg_rt
        self.avg_tps = avg_tps
        self.fail_count_biz = fail_count_biz
        self.fail_count_req = fail_count_req
        self.max_rt = max_rt
        self.min_rt = min_rt
        self.seg_50rt = seg_50rt
        self.seg_75rt = seg_75rt
        self.seg_90rt = seg_90rt
        self.seg_99rt = seg_99rt
        self.success_rate_biz = success_rate_biz
        self.success_rate_req = success_rate_req

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_count is not None:
            result['AllCount'] = self.all_count
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt
        if self.avg_tps is not None:
            result['AvgTps'] = self.avg_tps
        if self.fail_count_biz is not None:
            result['FailCountBiz'] = self.fail_count_biz
        if self.fail_count_req is not None:
            result['FailCountReq'] = self.fail_count_req
        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt
        if self.min_rt is not None:
            result['MinRt'] = self.min_rt
        if self.seg_50rt is not None:
            result['Seg50Rt'] = self.seg_50rt
        if self.seg_75rt is not None:
            result['Seg75Rt'] = self.seg_75rt
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.seg_99rt is not None:
            result['Seg99Rt'] = self.seg_99rt
        if self.success_rate_biz is not None:
            result['SuccessRateBiz'] = self.success_rate_biz
        if self.success_rate_req is not None:
            result['SuccessRateReq'] = self.success_rate_req
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllCount') is not None:
            self.all_count = m.get('AllCount')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')
        if m.get('AvgTps') is not None:
            self.avg_tps = m.get('AvgTps')
        if m.get('FailCountBiz') is not None:
            self.fail_count_biz = m.get('FailCountBiz')
        if m.get('FailCountReq') is not None:
            self.fail_count_req = m.get('FailCountReq')
        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')
        if m.get('MinRt') is not None:
            self.min_rt = m.get('MinRt')
        if m.get('Seg50Rt') is not None:
            self.seg_50rt = m.get('Seg50Rt')
        if m.get('Seg75Rt') is not None:
            self.seg_75rt = m.get('Seg75Rt')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('Seg99Rt') is not None:
            self.seg_99rt = m.get('Seg99Rt')
        if m.get('SuccessRateBiz') is not None:
            self.success_rate_biz = m.get('SuccessRateBiz')
        if m.get('SuccessRateReq') is not None:
            self.success_rate_req = m.get('SuccessRateReq')
        return self


class GetPtsReportDetailsResponseBodyReportOverView(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        end_time: str = None,
        report_id: str = None,
        report_name: str = None,
        start_time: str = None,
        vum: int = None,
    ):
        self.agent_count = agent_count
        self.end_time = end_time
        self.report_id = report_id
        self.report_name = report_name
        self.start_time = start_time
        self.vum = vum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_count is not None:
            result['AgentCount'] = self.agent_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.report_name is not None:
            result['ReportName'] = self.report_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vum is not None:
            result['Vum'] = self.vum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ReportName') is not None:
            self.report_name = m.get('ReportName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Vum') is not None:
            self.vum = m.get('Vum')
        return self


class GetPtsReportDetailsResponseBodySceneMetrics(TeaModel):
    def __init__(
        self,
        all_count: int = None,
        avg_rt: float = None,
        avg_tps: float = None,
        fail_count_biz: int = None,
        fail_count_req: int = None,
        seg_90rt: float = None,
        seg_99rt: float = None,
        success_rate_biz: float = None,
        success_rate_req: float = None,
    ):
        self.all_count = all_count
        self.avg_rt = avg_rt
        self.avg_tps = avg_tps
        self.fail_count_biz = fail_count_biz
        self.fail_count_req = fail_count_req
        self.seg_90rt = seg_90rt
        self.seg_99rt = seg_99rt
        self.success_rate_biz = success_rate_biz
        self.success_rate_req = success_rate_req

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_count is not None:
            result['AllCount'] = self.all_count
        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt
        if self.avg_tps is not None:
            result['AvgTps'] = self.avg_tps
        if self.fail_count_biz is not None:
            result['FailCountBiz'] = self.fail_count_biz
        if self.fail_count_req is not None:
            result['FailCountReq'] = self.fail_count_req
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.seg_99rt is not None:
            result['Seg99Rt'] = self.seg_99rt
        if self.success_rate_biz is not None:
            result['SuccessRateBiz'] = self.success_rate_biz
        if self.success_rate_req is not None:
            result['SuccessRateReq'] = self.success_rate_req
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllCount') is not None:
            self.all_count = m.get('AllCount')
        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')
        if m.get('AvgTps') is not None:
            self.avg_tps = m.get('AvgTps')
        if m.get('FailCountBiz') is not None:
            self.fail_count_biz = m.get('FailCountBiz')
        if m.get('FailCountReq') is not None:
            self.fail_count_req = m.get('FailCountReq')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('Seg99Rt') is not None:
            self.seg_99rt = m.get('Seg99Rt')
        if m.get('SuccessRateBiz') is not None:
            self.success_rate_biz = m.get('SuccessRateBiz')
        if m.get('SuccessRateReq') is not None:
            self.success_rate_req = m.get('SuccessRateReq')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotAdvanceSettingDomainBindingList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        ips: List[str] = None,
    ):
        self.domain = domain
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ips is not None:
            result['Ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotAdvanceSetting(TeaModel):
    def __init__(
        self,
        connection_timeout_in_second: int = None,
        domain_binding_list: List[GetPtsReportDetailsResponseBodySceneSnapShotAdvanceSettingDomainBindingList] = None,
        log_rate: int = None,
        success_code: str = None,
    ):
        self.connection_timeout_in_second = connection_timeout_in_second
        self.domain_binding_list = domain_binding_list
        self.log_rate = log_rate
        self.success_code = success_code

    def validate(self):
        if self.domain_binding_list:
            for k in self.domain_binding_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_timeout_in_second is not None:
            result['ConnectionTimeoutInSecond'] = self.connection_timeout_in_second
        result['DomainBindingList'] = []
        if self.domain_binding_list is not None:
            for k in self.domain_binding_list:
                result['DomainBindingList'].append(k.to_map() if k else None)
        if self.log_rate is not None:
            result['LogRate'] = self.log_rate
        if self.success_code is not None:
            result['SuccessCode'] = self.success_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionTimeoutInSecond') is not None:
            self.connection_timeout_in_second = m.get('ConnectionTimeoutInSecond')
        self.domain_binding_list = []
        if m.get('DomainBindingList') is not None:
            for k in m.get('DomainBindingList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotAdvanceSettingDomainBindingList()
                self.domain_binding_list.append(temp_model.from_map(k))
        if m.get('LogRate') is not None:
            self.log_rate = m.get('LogRate')
        if m.get('SuccessCode') is not None:
            self.success_code = m.get('SuccessCode')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotFileParameterList(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_oss_address: str = None,
    ):
        self.file_name = file_name
        self.file_oss_address = file_oss_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_oss_address is not None:
            result['FileOssAddress'] = self.file_oss_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileOssAddress') is not None:
            self.file_oss_address = m.get('FileOssAddress')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotGlobalParameterList(TeaModel):
    def __init__(
        self,
        param_name: str = None,
        param_value: str = None,
    ):
        self.param_name = param_name
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_value is not None:
            result['ParamValue'] = self.param_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigApiLoadConfigList(TeaModel):
    def __init__(
        self,
        rps_begin: int = None,
        rps_limit: int = None,
    ):
        self.rps_begin = rps_begin
        self.rps_limit = rps_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rps_begin is not None:
            result['RpsBegin'] = self.rps_begin
        if self.rps_limit is not None:
            result['RpsLimit'] = self.rps_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RpsBegin') is not None:
            self.rps_begin = m.get('RpsBegin')
        if m.get('RpsLimit') is not None:
            self.rps_limit = m.get('RpsLimit')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigConfiguration(TeaModel):
    def __init__(
        self,
        all_concurrency_begin: int = None,
        all_concurrency_limit: int = None,
        all_rps_begin: int = None,
        all_rps_limit: int = None,
    ):
        self.all_concurrency_begin = all_concurrency_begin
        self.all_concurrency_limit = all_concurrency_limit
        self.all_rps_begin = all_rps_begin
        self.all_rps_limit = all_rps_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_concurrency_begin is not None:
            result['AllConcurrencyBegin'] = self.all_concurrency_begin
        if self.all_concurrency_limit is not None:
            result['AllConcurrencyLimit'] = self.all_concurrency_limit
        if self.all_rps_begin is not None:
            result['AllRpsBegin'] = self.all_rps_begin
        if self.all_rps_limit is not None:
            result['AllRpsLimit'] = self.all_rps_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllConcurrencyBegin') is not None:
            self.all_concurrency_begin = m.get('AllConcurrencyBegin')
        if m.get('AllConcurrencyLimit') is not None:
            self.all_concurrency_limit = m.get('AllConcurrencyLimit')
        if m.get('AllRpsBegin') is not None:
            self.all_rps_begin = m.get('AllRpsBegin')
        if m.get('AllRpsLimit') is not None:
            self.all_rps_limit = m.get('AllRpsLimit')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigRelationLoadConfigList(TeaModel):
    def __init__(
        self,
        concurrency_begin: int = None,
        concurrency_limit: int = None,
    ):
        self.concurrency_begin = concurrency_begin
        self.concurrency_limit = concurrency_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_begin is not None:
            result['ConcurrencyBegin'] = self.concurrency_begin
        if self.concurrency_limit is not None:
            result['ConcurrencyLimit'] = self.concurrency_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyBegin') is not None:
            self.concurrency_begin = m.get('ConcurrencyBegin')
        if m.get('ConcurrencyLimit') is not None:
            self.concurrency_limit = m.get('ConcurrencyLimit')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotLoadConfig(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        api_load_config_list: List[GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigApiLoadConfigList] = None,
        configuration: GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigConfiguration = None,
        max_running_time: int = None,
        relation_load_config_list: List[GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigRelationLoadConfigList] = None,
        test_mode: str = None,
    ):
        self.agent_count = agent_count
        self.api_load_config_list = api_load_config_list
        self.configuration = configuration
        self.max_running_time = max_running_time
        self.relation_load_config_list = relation_load_config_list
        self.test_mode = test_mode

    def validate(self):
        if self.api_load_config_list:
            for k in self.api_load_config_list:
                if k:
                    k.validate()
        if self.configuration:
            self.configuration.validate()
        if self.relation_load_config_list:
            for k in self.relation_load_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_count is not None:
            result['AgentCount'] = self.agent_count
        result['ApiLoadConfigList'] = []
        if self.api_load_config_list is not None:
            for k in self.api_load_config_list:
                result['ApiLoadConfigList'].append(k.to_map() if k else None)
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.max_running_time is not None:
            result['MaxRunningTime'] = self.max_running_time
        result['RelationLoadConfigList'] = []
        if self.relation_load_config_list is not None:
            for k in self.relation_load_config_list:
                result['RelationLoadConfigList'].append(k.to_map() if k else None)
        if self.test_mode is not None:
            result['TestMode'] = self.test_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        self.api_load_config_list = []
        if m.get('ApiLoadConfigList') is not None:
            for k in m.get('ApiLoadConfigList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigApiLoadConfigList()
                self.api_load_config_list.append(temp_model.from_map(k))
        if m.get('Configuration') is not None:
            temp_model = GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('MaxRunningTime') is not None:
            self.max_running_time = m.get('MaxRunningTime')
        self.relation_load_config_list = []
        if m.get('RelationLoadConfigList') is not None:
            for k in m.get('RelationLoadConfigList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotLoadConfigRelationLoadConfigList()
                self.relation_load_config_list.append(temp_model.from_map(k))
        if m.get('TestMode') is not None:
            self.test_mode = m.get('TestMode')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListBody(TeaModel):
    def __init__(
        self,
        body_value: str = None,
        content_type: str = None,
    ):
        self.body_value = body_value
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_value is not None:
            result['BodyValue'] = self.body_value
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyValue') is not None:
            self.body_value = m.get('BodyValue')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListCheckPointList(TeaModel):
    def __init__(
        self,
        check_point: str = None,
        check_type: str = None,
        expect_value: str = None,
        operator: str = None,
    ):
        self.check_point = check_point
        self.check_type = check_type
        self.expect_value = expect_value
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_point is not None:
            result['CheckPoint'] = self.check_point
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.expect_value is not None:
            result['ExpectValue'] = self.expect_value
        if self.operator is not None:
            result['Operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckPoint') is not None:
            self.check_point = m.get('CheckPoint')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('ExpectValue') is not None:
            self.expect_value = m.get('ExpectValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListExportList(TeaModel):
    def __init__(
        self,
        count: str = None,
        export_name: str = None,
        export_type: str = None,
        export_value: str = None,
    ):
        self.count = count
        self.export_name = export_name
        self.export_type = export_type
        self.export_value = export_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.export_name is not None:
            result['ExportName'] = self.export_name
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.export_value is not None:
            result['ExportValue'] = self.export_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ExportName') is not None:
            self.export_name = m.get('ExportName')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('ExportValue') is not None:
            self.export_value = m.get('ExportValue')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListHeaderList(TeaModel):
    def __init__(
        self,
        header_name: str = None,
        header_value: str = None,
    ):
        self.header_name = header_name
        self.header_value = header_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_name is not None:
            result['HeaderName'] = self.header_name
        if self.header_value is not None:
            result['HeaderValue'] = self.header_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')
        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiList(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        body: GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListBody = None,
        check_point_list: List[GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListCheckPointList] = None,
        export_list: List[GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListExportList] = None,
        header_list: List[GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListHeaderList] = None,
        method: str = None,
        redirect_count_limit: int = None,
        timeout_in_second: int = None,
        url: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.body = body
        self.check_point_list = check_point_list
        self.export_list = export_list
        self.header_list = header_list
        self.method = method
        self.redirect_count_limit = redirect_count_limit
        self.timeout_in_second = timeout_in_second
        self.url = url

    def validate(self):
        if self.body:
            self.body.validate()
        if self.check_point_list:
            for k in self.check_point_list:
                if k:
                    k.validate()
        if self.export_list:
            for k in self.export_list:
                if k:
                    k.validate()
        if self.header_list:
            for k in self.header_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.body is not None:
            result['Body'] = self.body.to_map()
        result['CheckPointList'] = []
        if self.check_point_list is not None:
            for k in self.check_point_list:
                result['CheckPointList'].append(k.to_map() if k else None)
        result['ExportList'] = []
        if self.export_list is not None:
            for k in self.export_list:
                result['ExportList'].append(k.to_map() if k else None)
        result['HeaderList'] = []
        if self.header_list is not None:
            for k in self.header_list:
                result['HeaderList'].append(k.to_map() if k else None)
        if self.method is not None:
            result['Method'] = self.method
        if self.redirect_count_limit is not None:
            result['RedirectCountLimit'] = self.redirect_count_limit
        if self.timeout_in_second is not None:
            result['TimeoutInSecond'] = self.timeout_in_second
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Body') is not None:
            temp_model = GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListBody()
            self.body = temp_model.from_map(m['Body'])
        self.check_point_list = []
        if m.get('CheckPointList') is not None:
            for k in m.get('CheckPointList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListCheckPointList()
                self.check_point_list.append(temp_model.from_map(k))
        self.export_list = []
        if m.get('ExportList') is not None:
            for k in m.get('ExportList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListExportList()
                self.export_list.append(temp_model.from_map(k))
        self.header_list = []
        if m.get('HeaderList') is not None:
            for k in m.get('HeaderList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiListHeaderList()
                self.header_list.append(temp_model.from_map(k))
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RedirectCountLimit') is not None:
            self.redirect_count_limit = m.get('RedirectCountLimit')
        if m.get('TimeoutInSecond') is not None:
            self.timeout_in_second = m.get('TimeoutInSecond')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotRelationListFileParameterExplainList(TeaModel):
    def __init__(
        self,
        base_file: bool = None,
        cycle_once: bool = None,
        file_name: str = None,
        file_param_name: str = None,
    ):
        self.base_file = base_file
        self.cycle_once = cycle_once
        self.file_name = file_name
        self.file_param_name = file_param_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_file is not None:
            result['BaseFile'] = self.base_file
        if self.cycle_once is not None:
            result['CycleOnce'] = self.cycle_once
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_param_name is not None:
            result['FileParamName'] = self.file_param_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseFile') is not None:
            self.base_file = m.get('BaseFile')
        if m.get('CycleOnce') is not None:
            self.cycle_once = m.get('CycleOnce')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileParamName') is not None:
            self.file_param_name = m.get('FileParamName')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShotRelationList(TeaModel):
    def __init__(
        self,
        api_list: List[GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiList] = None,
        file_parameter_explain_list: List[GetPtsReportDetailsResponseBodySceneSnapShotRelationListFileParameterExplainList] = None,
        relation_id: str = None,
        relation_name: str = None,
    ):
        self.api_list = api_list
        self.file_parameter_explain_list = file_parameter_explain_list
        self.relation_id = relation_id
        self.relation_name = relation_name

    def validate(self):
        if self.api_list:
            for k in self.api_list:
                if k:
                    k.validate()
        if self.file_parameter_explain_list:
            for k in self.file_parameter_explain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiList'] = []
        if self.api_list is not None:
            for k in self.api_list:
                result['ApiList'].append(k.to_map() if k else None)
        result['FileParameterExplainList'] = []
        if self.file_parameter_explain_list is not None:
            for k in self.file_parameter_explain_list:
                result['FileParameterExplainList'].append(k.to_map() if k else None)
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        if self.relation_name is not None:
            result['RelationName'] = self.relation_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_list = []
        if m.get('ApiList') is not None:
            for k in m.get('ApiList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotRelationListApiList()
                self.api_list.append(temp_model.from_map(k))
        self.file_parameter_explain_list = []
        if m.get('FileParameterExplainList') is not None:
            for k in m.get('FileParameterExplainList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotRelationListFileParameterExplainList()
                self.file_parameter_explain_list.append(temp_model.from_map(k))
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        if m.get('RelationName') is not None:
            self.relation_name = m.get('RelationName')
        return self


class GetPtsReportDetailsResponseBodySceneSnapShot(TeaModel):
    def __init__(
        self,
        advance_setting: GetPtsReportDetailsResponseBodySceneSnapShotAdvanceSetting = None,
        create_time: str = None,
        file_parameter_list: List[GetPtsReportDetailsResponseBodySceneSnapShotFileParameterList] = None,
        global_parameter_list: List[GetPtsReportDetailsResponseBodySceneSnapShotGlobalParameterList] = None,
        load_config: GetPtsReportDetailsResponseBodySceneSnapShotLoadConfig = None,
        modified_time: str = None,
        relation_list: List[GetPtsReportDetailsResponseBodySceneSnapShotRelationList] = None,
        scene_id: str = None,
        scene_name: str = None,
        status: str = None,
    ):
        self.advance_setting = advance_setting
        self.create_time = create_time
        self.file_parameter_list = file_parameter_list
        self.global_parameter_list = global_parameter_list
        self.load_config = load_config
        self.modified_time = modified_time
        self.relation_list = relation_list
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.status = status

    def validate(self):
        if self.advance_setting:
            self.advance_setting.validate()
        if self.file_parameter_list:
            for k in self.file_parameter_list:
                if k:
                    k.validate()
        if self.global_parameter_list:
            for k in self.global_parameter_list:
                if k:
                    k.validate()
        if self.load_config:
            self.load_config.validate()
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_setting is not None:
            result['AdvanceSetting'] = self.advance_setting.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['FileParameterList'] = []
        if self.file_parameter_list is not None:
            for k in self.file_parameter_list:
                result['FileParameterList'].append(k.to_map() if k else None)
        result['GlobalParameterList'] = []
        if self.global_parameter_list is not None:
            for k in self.global_parameter_list:
                result['GlobalParameterList'].append(k.to_map() if k else None)
        if self.load_config is not None:
            result['LoadConfig'] = self.load_config.to_map()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        result['RelationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['RelationList'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvanceSetting') is not None:
            temp_model = GetPtsReportDetailsResponseBodySceneSnapShotAdvanceSetting()
            self.advance_setting = temp_model.from_map(m['AdvanceSetting'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.file_parameter_list = []
        if m.get('FileParameterList') is not None:
            for k in m.get('FileParameterList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotFileParameterList()
                self.file_parameter_list.append(temp_model.from_map(k))
        self.global_parameter_list = []
        if m.get('GlobalParameterList') is not None:
            for k in m.get('GlobalParameterList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotGlobalParameterList()
                self.global_parameter_list.append(temp_model.from_map(k))
        if m.get('LoadConfig') is not None:
            temp_model = GetPtsReportDetailsResponseBodySceneSnapShotLoadConfig()
            self.load_config = temp_model.from_map(m['LoadConfig'])
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        self.relation_list = []
        if m.get('RelationList') is not None:
            for k in m.get('RelationList'):
                temp_model = GetPtsReportDetailsResponseBodySceneSnapShotRelationList()
                self.relation_list.append(temp_model.from_map(k))
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetPtsReportDetailsResponseBody(TeaModel):
    def __init__(
        self,
        api_metrics_list: List[GetPtsReportDetailsResponseBodyApiMetricsList] = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        report_over_view: GetPtsReportDetailsResponseBodyReportOverView = None,
        request_id: str = None,
        scene_metrics: GetPtsReportDetailsResponseBodySceneMetrics = None,
        scene_snap_shot: GetPtsReportDetailsResponseBodySceneSnapShot = None,
        success: bool = None,
    ):
        self.api_metrics_list = api_metrics_list
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.report_over_view = report_over_view
        self.request_id = request_id
        self.scene_metrics = scene_metrics
        self.scene_snap_shot = scene_snap_shot
        self.success = success

    def validate(self):
        if self.api_metrics_list:
            for k in self.api_metrics_list:
                if k:
                    k.validate()
        if self.report_over_view:
            self.report_over_view.validate()
        if self.scene_metrics:
            self.scene_metrics.validate()
        if self.scene_snap_shot:
            self.scene_snap_shot.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiMetricsList'] = []
        if self.api_metrics_list is not None:
            for k in self.api_metrics_list:
                result['ApiMetricsList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.report_over_view is not None:
            result['ReportOverView'] = self.report_over_view.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_metrics is not None:
            result['SceneMetrics'] = self.scene_metrics.to_map()
        if self.scene_snap_shot is not None:
            result['SceneSnapShot'] = self.scene_snap_shot.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_metrics_list = []
        if m.get('ApiMetricsList') is not None:
            for k in m.get('ApiMetricsList'):
                temp_model = GetPtsReportDetailsResponseBodyApiMetricsList()
                self.api_metrics_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReportOverView') is not None:
            temp_model = GetPtsReportDetailsResponseBodyReportOverView()
            self.report_over_view = temp_model.from_map(m['ReportOverView'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneMetrics') is not None:
            temp_model = GetPtsReportDetailsResponseBodySceneMetrics()
            self.scene_metrics = temp_model.from_map(m['SceneMetrics'])
        if m.get('SceneSnapShot') is not None:
            temp_model = GetPtsReportDetailsResponseBodySceneSnapShot()
            self.scene_snap_shot = temp_model.from_map(m['SceneSnapShot'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPtsReportDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPtsReportDetailsResponseBody = None,
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
            temp_model = GetPtsReportDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsReportsBySceneIdRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        scene_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.scene_id = scene_id

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
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetPtsReportsBySceneIdResponseBodyReportOverViewList(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        end_time: str = None,
        report_id: str = None,
        report_name: str = None,
        start_time: str = None,
        vum: int = None,
    ):
        self.agent_count = agent_count
        self.end_time = end_time
        self.report_id = report_id
        self.report_name = report_name
        self.start_time = start_time
        self.vum = vum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_count is not None:
            result['AgentCount'] = self.agent_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.report_name is not None:
            result['ReportName'] = self.report_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vum is not None:
            result['Vum'] = self.vum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ReportName') is not None:
            self.report_name = m.get('ReportName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Vum') is not None:
            self.vum = m.get('Vum')
        return self


class GetPtsReportsBySceneIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        report_over_view_list: List[GetPtsReportsBySceneIdResponseBodyReportOverViewList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.report_over_view_list = report_over_view_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.report_over_view_list:
            for k in self.report_over_view_list:
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
        result['ReportOverViewList'] = []
        if self.report_over_view_list is not None:
            for k in self.report_over_view_list:
                result['ReportOverViewList'].append(k.to_map() if k else None)
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
        self.report_over_view_list = []
        if m.get('ReportOverViewList') is not None:
            for k in m.get('ReportOverViewList'):
                temp_model = GetPtsReportsBySceneIdResponseBodyReportOverViewList()
                self.report_over_view_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPtsReportsBySceneIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPtsReportsBySceneIdResponseBody = None,
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
            temp_model = GetPtsReportsBySceneIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetPtsSceneResponseBodySceneAdvanceSettingDomainBindingList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        ips: List[str] = None,
    ):
        self.domain = domain
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.ips is not None:
            result['Ips'] = self.ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        return self


class GetPtsSceneResponseBodySceneAdvanceSetting(TeaModel):
    def __init__(
        self,
        connection_timeout_in_second: int = None,
        domain_binding_list: List[GetPtsSceneResponseBodySceneAdvanceSettingDomainBindingList] = None,
        log_rate: int = None,
        success_code: str = None,
    ):
        self.connection_timeout_in_second = connection_timeout_in_second
        self.domain_binding_list = domain_binding_list
        self.log_rate = log_rate
        self.success_code = success_code

    def validate(self):
        if self.domain_binding_list:
            for k in self.domain_binding_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_timeout_in_second is not None:
            result['ConnectionTimeoutInSecond'] = self.connection_timeout_in_second
        result['DomainBindingList'] = []
        if self.domain_binding_list is not None:
            for k in self.domain_binding_list:
                result['DomainBindingList'].append(k.to_map() if k else None)
        if self.log_rate is not None:
            result['LogRate'] = self.log_rate
        if self.success_code is not None:
            result['SuccessCode'] = self.success_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionTimeoutInSecond') is not None:
            self.connection_timeout_in_second = m.get('ConnectionTimeoutInSecond')
        self.domain_binding_list = []
        if m.get('DomainBindingList') is not None:
            for k in m.get('DomainBindingList'):
                temp_model = GetPtsSceneResponseBodySceneAdvanceSettingDomainBindingList()
                self.domain_binding_list.append(temp_model.from_map(k))
        if m.get('LogRate') is not None:
            self.log_rate = m.get('LogRate')
        if m.get('SuccessCode') is not None:
            self.success_code = m.get('SuccessCode')
        return self


class GetPtsSceneResponseBodySceneFileParameterList(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_oss_address: str = None,
    ):
        self.file_name = file_name
        self.file_oss_address = file_oss_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_oss_address is not None:
            result['FileOssAddress'] = self.file_oss_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileOssAddress') is not None:
            self.file_oss_address = m.get('FileOssAddress')
        return self


class GetPtsSceneResponseBodySceneGlobalParameterList(TeaModel):
    def __init__(
        self,
        param_name: str = None,
        param_value: str = None,
    ):
        self.param_name = param_name
        self.param_value = param_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_name is not None:
            result['ParamName'] = self.param_name
        if self.param_value is not None:
            result['ParamValue'] = self.param_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')
        if m.get('ParamValue') is not None:
            self.param_value = m.get('ParamValue')
        return self


class GetPtsSceneResponseBodySceneLoadConfigApiLoadConfigList(TeaModel):
    def __init__(
        self,
        rps_begin: int = None,
        rps_limit: int = None,
    ):
        self.rps_begin = rps_begin
        self.rps_limit = rps_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rps_begin is not None:
            result['RpsBegin'] = self.rps_begin
        if self.rps_limit is not None:
            result['RpsLimit'] = self.rps_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RpsBegin') is not None:
            self.rps_begin = m.get('RpsBegin')
        if m.get('RpsLimit') is not None:
            self.rps_limit = m.get('RpsLimit')
        return self


class GetPtsSceneResponseBodySceneLoadConfigConfiguration(TeaModel):
    def __init__(
        self,
        all_concurrency_begin: int = None,
        all_concurrency_limit: int = None,
        all_rps_begin: int = None,
        all_rps_limit: int = None,
    ):
        self.all_concurrency_begin = all_concurrency_begin
        self.all_concurrency_limit = all_concurrency_limit
        self.all_rps_begin = all_rps_begin
        self.all_rps_limit = all_rps_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_concurrency_begin is not None:
            result['AllConcurrencyBegin'] = self.all_concurrency_begin
        if self.all_concurrency_limit is not None:
            result['AllConcurrencyLimit'] = self.all_concurrency_limit
        if self.all_rps_begin is not None:
            result['AllRpsBegin'] = self.all_rps_begin
        if self.all_rps_limit is not None:
            result['AllRpsLimit'] = self.all_rps_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllConcurrencyBegin') is not None:
            self.all_concurrency_begin = m.get('AllConcurrencyBegin')
        if m.get('AllConcurrencyLimit') is not None:
            self.all_concurrency_limit = m.get('AllConcurrencyLimit')
        if m.get('AllRpsBegin') is not None:
            self.all_rps_begin = m.get('AllRpsBegin')
        if m.get('AllRpsLimit') is not None:
            self.all_rps_limit = m.get('AllRpsLimit')
        return self


class GetPtsSceneResponseBodySceneLoadConfigRelationLoadConfigList(TeaModel):
    def __init__(
        self,
        concurrency_begin: int = None,
        concurrency_limit: int = None,
    ):
        self.concurrency_begin = concurrency_begin
        self.concurrency_limit = concurrency_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_begin is not None:
            result['ConcurrencyBegin'] = self.concurrency_begin
        if self.concurrency_limit is not None:
            result['ConcurrencyLimit'] = self.concurrency_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyBegin') is not None:
            self.concurrency_begin = m.get('ConcurrencyBegin')
        if m.get('ConcurrencyLimit') is not None:
            self.concurrency_limit = m.get('ConcurrencyLimit')
        return self


class GetPtsSceneResponseBodySceneLoadConfig(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        api_load_config_list: List[GetPtsSceneResponseBodySceneLoadConfigApiLoadConfigList] = None,
        configuration: GetPtsSceneResponseBodySceneLoadConfigConfiguration = None,
        max_running_time: int = None,
        relation_load_config_list: List[GetPtsSceneResponseBodySceneLoadConfigRelationLoadConfigList] = None,
        test_mode: str = None,
    ):
        self.agent_count = agent_count
        self.api_load_config_list = api_load_config_list
        self.configuration = configuration
        self.max_running_time = max_running_time
        self.relation_load_config_list = relation_load_config_list
        self.test_mode = test_mode

    def validate(self):
        if self.api_load_config_list:
            for k in self.api_load_config_list:
                if k:
                    k.validate()
        if self.configuration:
            self.configuration.validate()
        if self.relation_load_config_list:
            for k in self.relation_load_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_count is not None:
            result['AgentCount'] = self.agent_count
        result['ApiLoadConfigList'] = []
        if self.api_load_config_list is not None:
            for k in self.api_load_config_list:
                result['ApiLoadConfigList'].append(k.to_map() if k else None)
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.max_running_time is not None:
            result['MaxRunningTime'] = self.max_running_time
        result['RelationLoadConfigList'] = []
        if self.relation_load_config_list is not None:
            for k in self.relation_load_config_list:
                result['RelationLoadConfigList'].append(k.to_map() if k else None)
        if self.test_mode is not None:
            result['TestMode'] = self.test_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        self.api_load_config_list = []
        if m.get('ApiLoadConfigList') is not None:
            for k in m.get('ApiLoadConfigList'):
                temp_model = GetPtsSceneResponseBodySceneLoadConfigApiLoadConfigList()
                self.api_load_config_list.append(temp_model.from_map(k))
        if m.get('Configuration') is not None:
            temp_model = GetPtsSceneResponseBodySceneLoadConfigConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('MaxRunningTime') is not None:
            self.max_running_time = m.get('MaxRunningTime')
        self.relation_load_config_list = []
        if m.get('RelationLoadConfigList') is not None:
            for k in m.get('RelationLoadConfigList'):
                temp_model = GetPtsSceneResponseBodySceneLoadConfigRelationLoadConfigList()
                self.relation_load_config_list.append(temp_model.from_map(k))
        if m.get('TestMode') is not None:
            self.test_mode = m.get('TestMode')
        return self


class GetPtsSceneResponseBodySceneRelationListApiListBody(TeaModel):
    def __init__(
        self,
        body_value: str = None,
        content_type: str = None,
    ):
        self.body_value = body_value
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_value is not None:
            result['BodyValue'] = self.body_value
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyValue') is not None:
            self.body_value = m.get('BodyValue')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        return self


class GetPtsSceneResponseBodySceneRelationListApiListCheckPointList(TeaModel):
    def __init__(
        self,
        check_point: str = None,
        check_type: str = None,
        expect_value: str = None,
        operator: str = None,
    ):
        self.check_point = check_point
        self.check_type = check_type
        self.expect_value = expect_value
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_point is not None:
            result['CheckPoint'] = self.check_point
        if self.check_type is not None:
            result['CheckType'] = self.check_type
        if self.expect_value is not None:
            result['ExpectValue'] = self.expect_value
        if self.operator is not None:
            result['Operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckPoint') is not None:
            self.check_point = m.get('CheckPoint')
        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')
        if m.get('ExpectValue') is not None:
            self.expect_value = m.get('ExpectValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        return self


class GetPtsSceneResponseBodySceneRelationListApiListExportList(TeaModel):
    def __init__(
        self,
        count: str = None,
        export_name: str = None,
        export_type: str = None,
        export_value: str = None,
    ):
        self.count = count
        self.export_name = export_name
        self.export_type = export_type
        self.export_value = export_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.export_name is not None:
            result['ExportName'] = self.export_name
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.export_value is not None:
            result['ExportValue'] = self.export_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ExportName') is not None:
            self.export_name = m.get('ExportName')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('ExportValue') is not None:
            self.export_value = m.get('ExportValue')
        return self


class GetPtsSceneResponseBodySceneRelationListApiListHeaderList(TeaModel):
    def __init__(
        self,
        header_name: str = None,
        header_value: str = None,
    ):
        self.header_name = header_name
        self.header_value = header_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header_name is not None:
            result['HeaderName'] = self.header_name
        if self.header_value is not None:
            result['HeaderValue'] = self.header_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeaderName') is not None:
            self.header_name = m.get('HeaderName')
        if m.get('HeaderValue') is not None:
            self.header_value = m.get('HeaderValue')
        return self


class GetPtsSceneResponseBodySceneRelationListApiList(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        body: GetPtsSceneResponseBodySceneRelationListApiListBody = None,
        check_point_list: List[GetPtsSceneResponseBodySceneRelationListApiListCheckPointList] = None,
        export_list: List[GetPtsSceneResponseBodySceneRelationListApiListExportList] = None,
        header_list: List[GetPtsSceneResponseBodySceneRelationListApiListHeaderList] = None,
        method: str = None,
        redirect_count_limit: int = None,
        timeout_in_second: int = None,
        url: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.body = body
        self.check_point_list = check_point_list
        self.export_list = export_list
        self.header_list = header_list
        self.method = method
        self.redirect_count_limit = redirect_count_limit
        self.timeout_in_second = timeout_in_second
        self.url = url

    def validate(self):
        if self.body:
            self.body.validate()
        if self.check_point_list:
            for k in self.check_point_list:
                if k:
                    k.validate()
        if self.export_list:
            for k in self.export_list:
                if k:
                    k.validate()
        if self.header_list:
            for k in self.header_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.body is not None:
            result['Body'] = self.body.to_map()
        result['CheckPointList'] = []
        if self.check_point_list is not None:
            for k in self.check_point_list:
                result['CheckPointList'].append(k.to_map() if k else None)
        result['ExportList'] = []
        if self.export_list is not None:
            for k in self.export_list:
                result['ExportList'].append(k.to_map() if k else None)
        result['HeaderList'] = []
        if self.header_list is not None:
            for k in self.header_list:
                result['HeaderList'].append(k.to_map() if k else None)
        if self.method is not None:
            result['Method'] = self.method
        if self.redirect_count_limit is not None:
            result['RedirectCountLimit'] = self.redirect_count_limit
        if self.timeout_in_second is not None:
            result['TimeoutInSecond'] = self.timeout_in_second
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('Body') is not None:
            temp_model = GetPtsSceneResponseBodySceneRelationListApiListBody()
            self.body = temp_model.from_map(m['Body'])
        self.check_point_list = []
        if m.get('CheckPointList') is not None:
            for k in m.get('CheckPointList'):
                temp_model = GetPtsSceneResponseBodySceneRelationListApiListCheckPointList()
                self.check_point_list.append(temp_model.from_map(k))
        self.export_list = []
        if m.get('ExportList') is not None:
            for k in m.get('ExportList'):
                temp_model = GetPtsSceneResponseBodySceneRelationListApiListExportList()
                self.export_list.append(temp_model.from_map(k))
        self.header_list = []
        if m.get('HeaderList') is not None:
            for k in m.get('HeaderList'):
                temp_model = GetPtsSceneResponseBodySceneRelationListApiListHeaderList()
                self.header_list.append(temp_model.from_map(k))
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('RedirectCountLimit') is not None:
            self.redirect_count_limit = m.get('RedirectCountLimit')
        if m.get('TimeoutInSecond') is not None:
            self.timeout_in_second = m.get('TimeoutInSecond')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetPtsSceneResponseBodySceneRelationListFileParameterExplainList(TeaModel):
    def __init__(
        self,
        base_file: bool = None,
        cycle_once: bool = None,
        file_name: str = None,
        file_param_name: str = None,
    ):
        self.base_file = base_file
        self.cycle_once = cycle_once
        self.file_name = file_name
        self.file_param_name = file_param_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_file is not None:
            result['BaseFile'] = self.base_file
        if self.cycle_once is not None:
            result['CycleOnce'] = self.cycle_once
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_param_name is not None:
            result['FileParamName'] = self.file_param_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseFile') is not None:
            self.base_file = m.get('BaseFile')
        if m.get('CycleOnce') is not None:
            self.cycle_once = m.get('CycleOnce')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileParamName') is not None:
            self.file_param_name = m.get('FileParamName')
        return self


class GetPtsSceneResponseBodySceneRelationList(TeaModel):
    def __init__(
        self,
        api_list: List[GetPtsSceneResponseBodySceneRelationListApiList] = None,
        file_parameter_explain_list: List[GetPtsSceneResponseBodySceneRelationListFileParameterExplainList] = None,
        relation_id: str = None,
        relation_name: str = None,
    ):
        self.api_list = api_list
        self.file_parameter_explain_list = file_parameter_explain_list
        self.relation_id = relation_id
        self.relation_name = relation_name

    def validate(self):
        if self.api_list:
            for k in self.api_list:
                if k:
                    k.validate()
        if self.file_parameter_explain_list:
            for k in self.file_parameter_explain_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiList'] = []
        if self.api_list is not None:
            for k in self.api_list:
                result['ApiList'].append(k.to_map() if k else None)
        result['FileParameterExplainList'] = []
        if self.file_parameter_explain_list is not None:
            for k in self.file_parameter_explain_list:
                result['FileParameterExplainList'].append(k.to_map() if k else None)
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        if self.relation_name is not None:
            result['RelationName'] = self.relation_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_list = []
        if m.get('ApiList') is not None:
            for k in m.get('ApiList'):
                temp_model = GetPtsSceneResponseBodySceneRelationListApiList()
                self.api_list.append(temp_model.from_map(k))
        self.file_parameter_explain_list = []
        if m.get('FileParameterExplainList') is not None:
            for k in m.get('FileParameterExplainList'):
                temp_model = GetPtsSceneResponseBodySceneRelationListFileParameterExplainList()
                self.file_parameter_explain_list.append(temp_model.from_map(k))
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        if m.get('RelationName') is not None:
            self.relation_name = m.get('RelationName')
        return self


class GetPtsSceneResponseBodyScene(TeaModel):
    def __init__(
        self,
        advance_setting: GetPtsSceneResponseBodySceneAdvanceSetting = None,
        create_time: str = None,
        file_parameter_list: List[GetPtsSceneResponseBodySceneFileParameterList] = None,
        global_parameter_list: List[GetPtsSceneResponseBodySceneGlobalParameterList] = None,
        load_config: GetPtsSceneResponseBodySceneLoadConfig = None,
        modified_time: str = None,
        relation_list: List[GetPtsSceneResponseBodySceneRelationList] = None,
        scene_id: str = None,
        scene_name: str = None,
        status: str = None,
    ):
        self.advance_setting = advance_setting
        self.create_time = create_time
        self.file_parameter_list = file_parameter_list
        self.global_parameter_list = global_parameter_list
        self.load_config = load_config
        self.modified_time = modified_time
        self.relation_list = relation_list
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.status = status

    def validate(self):
        if self.advance_setting:
            self.advance_setting.validate()
        if self.file_parameter_list:
            for k in self.file_parameter_list:
                if k:
                    k.validate()
        if self.global_parameter_list:
            for k in self.global_parameter_list:
                if k:
                    k.validate()
        if self.load_config:
            self.load_config.validate()
        if self.relation_list:
            for k in self.relation_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_setting is not None:
            result['AdvanceSetting'] = self.advance_setting.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['FileParameterList'] = []
        if self.file_parameter_list is not None:
            for k in self.file_parameter_list:
                result['FileParameterList'].append(k.to_map() if k else None)
        result['GlobalParameterList'] = []
        if self.global_parameter_list is not None:
            for k in self.global_parameter_list:
                result['GlobalParameterList'].append(k.to_map() if k else None)
        if self.load_config is not None:
            result['LoadConfig'] = self.load_config.to_map()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        result['RelationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['RelationList'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvanceSetting') is not None:
            temp_model = GetPtsSceneResponseBodySceneAdvanceSetting()
            self.advance_setting = temp_model.from_map(m['AdvanceSetting'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.file_parameter_list = []
        if m.get('FileParameterList') is not None:
            for k in m.get('FileParameterList'):
                temp_model = GetPtsSceneResponseBodySceneFileParameterList()
                self.file_parameter_list.append(temp_model.from_map(k))
        self.global_parameter_list = []
        if m.get('GlobalParameterList') is not None:
            for k in m.get('GlobalParameterList'):
                temp_model = GetPtsSceneResponseBodySceneGlobalParameterList()
                self.global_parameter_list.append(temp_model.from_map(k))
        if m.get('LoadConfig') is not None:
            temp_model = GetPtsSceneResponseBodySceneLoadConfig()
            self.load_config = temp_model.from_map(m['LoadConfig'])
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        self.relation_list = []
        if m.get('RelationList') is not None:
            for k in m.get('RelationList'):
                temp_model = GetPtsSceneResponseBodySceneRelationList()
                self.relation_list.append(temp_model.from_map(k))
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetPtsSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scene: GetPtsSceneResponseBodyScene = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.scene = scene
        self.success = success

    def validate(self):
        if self.scene:
            self.scene.validate()

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
        if self.scene is not None:
            result['Scene'] = self.scene.to_map()
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
        if m.get('Scene') is not None:
            temp_model = GetPtsSceneResponseBodyScene()
            self.scene = temp_model.from_map(m['Scene'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPtsSceneResponseBody = None,
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
            temp_model = GetPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsSceneBaseLineRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetPtsSceneBaseLineResponseBodyBaselineApiBaselines(TeaModel):
    def __init__(
        self,
        avg_rt: float = None,
        avg_tps: float = None,
        fail_count_biz: int = None,
        fail_count_req: int = None,
        id: int = None,
        max_rt: int = None,
        min_rt: int = None,
        name: str = None,
        seg_90rt: float = None,
        seg_99rt: float = None,
        success_rate_biz: float = None,
        success_rate_req: float = None,
    ):
        self.avg_rt = avg_rt
        self.avg_tps = avg_tps
        self.fail_count_biz = fail_count_biz
        self.fail_count_req = fail_count_req
        self.id = id
        self.max_rt = max_rt
        self.min_rt = min_rt
        self.name = name
        self.seg_90rt = seg_90rt
        self.seg_99rt = seg_99rt
        self.success_rate_biz = success_rate_biz
        self.success_rate_req = success_rate_req

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt
        if self.avg_tps is not None:
            result['AvgTps'] = self.avg_tps
        if self.fail_count_biz is not None:
            result['FailCountBiz'] = self.fail_count_biz
        if self.fail_count_req is not None:
            result['FailCountReq'] = self.fail_count_req
        if self.id is not None:
            result['Id'] = self.id
        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt
        if self.min_rt is not None:
            result['MinRt'] = self.min_rt
        if self.name is not None:
            result['Name'] = self.name
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.seg_99rt is not None:
            result['Seg99Rt'] = self.seg_99rt
        if self.success_rate_biz is not None:
            result['SuccessRateBiz'] = self.success_rate_biz
        if self.success_rate_req is not None:
            result['SuccessRateReq'] = self.success_rate_req
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')
        if m.get('AvgTps') is not None:
            self.avg_tps = m.get('AvgTps')
        if m.get('FailCountBiz') is not None:
            self.fail_count_biz = m.get('FailCountBiz')
        if m.get('FailCountReq') is not None:
            self.fail_count_req = m.get('FailCountReq')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')
        if m.get('MinRt') is not None:
            self.min_rt = m.get('MinRt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('Seg99Rt') is not None:
            self.seg_99rt = m.get('Seg99Rt')
        if m.get('SuccessRateBiz') is not None:
            self.success_rate_biz = m.get('SuccessRateBiz')
        if m.get('SuccessRateReq') is not None:
            self.success_rate_req = m.get('SuccessRateReq')
        return self


class GetPtsSceneBaseLineResponseBodyBaselineSceneBaseline(TeaModel):
    def __init__(
        self,
        avg_rt: float = None,
        avg_tps: float = None,
        fail_count_biz: int = None,
        fail_count_req: int = None,
        seg_90rt: float = None,
        seg_99rt: float = None,
        success_rate_biz: float = None,
        success_rate_req: float = None,
    ):
        self.avg_rt = avg_rt
        self.avg_tps = avg_tps
        self.fail_count_biz = fail_count_biz
        self.fail_count_req = fail_count_req
        self.seg_90rt = seg_90rt
        self.seg_99rt = seg_99rt
        self.success_rate_biz = success_rate_biz
        self.success_rate_req = success_rate_req

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt
        if self.avg_tps is not None:
            result['AvgTps'] = self.avg_tps
        if self.fail_count_biz is not None:
            result['FailCountBiz'] = self.fail_count_biz
        if self.fail_count_req is not None:
            result['FailCountReq'] = self.fail_count_req
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.seg_99rt is not None:
            result['Seg99Rt'] = self.seg_99rt
        if self.success_rate_biz is not None:
            result['SuccessRateBiz'] = self.success_rate_biz
        if self.success_rate_req is not None:
            result['SuccessRateReq'] = self.success_rate_req
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')
        if m.get('AvgTps') is not None:
            self.avg_tps = m.get('AvgTps')
        if m.get('FailCountBiz') is not None:
            self.fail_count_biz = m.get('FailCountBiz')
        if m.get('FailCountReq') is not None:
            self.fail_count_req = m.get('FailCountReq')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('Seg99Rt') is not None:
            self.seg_99rt = m.get('Seg99Rt')
        if m.get('SuccessRateBiz') is not None:
            self.success_rate_biz = m.get('SuccessRateBiz')
        if m.get('SuccessRateReq') is not None:
            self.success_rate_req = m.get('SuccessRateReq')
        return self


class GetPtsSceneBaseLineResponseBodyBaseline(TeaModel):
    def __init__(
        self,
        api_baselines: List[GetPtsSceneBaseLineResponseBodyBaselineApiBaselines] = None,
        name: str = None,
        scene_baseline: GetPtsSceneBaseLineResponseBodyBaselineSceneBaseline = None,
    ):
        self.api_baselines = api_baselines
        self.name = name
        self.scene_baseline = scene_baseline

    def validate(self):
        if self.api_baselines:
            for k in self.api_baselines:
                if k:
                    k.validate()
        if self.scene_baseline:
            self.scene_baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiBaselines'] = []
        if self.api_baselines is not None:
            for k in self.api_baselines:
                result['ApiBaselines'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_baseline is not None:
            result['SceneBaseline'] = self.scene_baseline.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_baselines = []
        if m.get('ApiBaselines') is not None:
            for k in m.get('ApiBaselines'):
                temp_model = GetPtsSceneBaseLineResponseBodyBaselineApiBaselines()
                self.api_baselines.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneBaseline') is not None:
            temp_model = GetPtsSceneBaseLineResponseBodyBaselineSceneBaseline()
            self.scene_baseline = temp_model.from_map(m['SceneBaseline'])
        return self


class GetPtsSceneBaseLineResponseBody(TeaModel):
    def __init__(
        self,
        baseline: GetPtsSceneBaseLineResponseBodyBaseline = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scene_id: str = None,
        success: bool = None,
    ):
        self.baseline = baseline
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.scene_id = scene_id
        self.success = success

    def validate(self):
        if self.baseline:
            self.baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline is not None:
            result['Baseline'] = self.baseline.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Baseline') is not None:
            temp_model = GetPtsSceneBaseLineResponseBodyBaseline()
            self.baseline = temp_model.from_map(m['Baseline'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPtsSceneBaseLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPtsSceneBaseLineResponseBody = None,
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
            temp_model = GetPtsSceneBaseLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsSceneRunningDataRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        scene_id: str = None,
    ):
        self.plan_id = plan_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetPtsSceneRunningDataResponseBodyAgentLocation(TeaModel):
    def __init__(
        self,
        count: int = None,
        isp: str = None,
        province: str = None,
        region: str = None,
    ):
        self.count = count
        self.isp = isp
        self.province = province
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class GetPtsSceneRunningDataResponseBodyChainMonitorDataListCheckPointResult(TeaModel):
    def __init__(
        self,
        failed_business_count: int = None,
        failed_business_qps: float = None,
        succeed_business_count: int = None,
        succeed_business_qps: float = None,
    ):
        self.failed_business_count = failed_business_count
        self.failed_business_qps = failed_business_qps
        self.succeed_business_count = succeed_business_count
        self.succeed_business_qps = succeed_business_qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_business_count is not None:
            result['FailedBusinessCount'] = self.failed_business_count
        if self.failed_business_qps is not None:
            result['FailedBusinessQps'] = self.failed_business_qps
        if self.succeed_business_count is not None:
            result['SucceedBusinessCount'] = self.succeed_business_count
        if self.succeed_business_qps is not None:
            result['SucceedBusinessQps'] = self.succeed_business_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedBusinessCount') is not None:
            self.failed_business_count = m.get('FailedBusinessCount')
        if m.get('FailedBusinessQps') is not None:
            self.failed_business_qps = m.get('FailedBusinessQps')
        if m.get('SucceedBusinessCount') is not None:
            self.succeed_business_count = m.get('SucceedBusinessCount')
        if m.get('SucceedBusinessQps') is not None:
            self.succeed_business_qps = m.get('SucceedBusinessQps')
        return self


class GetPtsSceneRunningDataResponseBodyChainMonitorDataList(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        average_rt: int = None,
        check_point_result: GetPtsSceneRunningDataResponseBodyChainMonitorDataListCheckPointResult = None,
        concurrency: float = None,
        config_qps: int = None,
        count_2xx: int = None,
        failed_count: int = None,
        failed_qps: float = None,
        max_rt: int = None,
        min_rt: int = None,
        node_id: int = None,
        qps_2xx: float = None,
        real_qps: float = None,
        time_point: int = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.average_rt = average_rt
        self.check_point_result = check_point_result
        self.concurrency = concurrency
        self.config_qps = config_qps
        self.count_2xx = count_2xx
        self.failed_count = failed_count
        self.failed_qps = failed_qps
        self.max_rt = max_rt
        self.min_rt = min_rt
        self.node_id = node_id
        self.qps_2xx = qps_2xx
        self.real_qps = real_qps
        self.time_point = time_point

    def validate(self):
        if self.check_point_result:
            self.check_point_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.average_rt is not None:
            result['AverageRt'] = self.average_rt
        if self.check_point_result is not None:
            result['CheckPointResult'] = self.check_point_result.to_map()
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.config_qps is not None:
            result['ConfigQps'] = self.config_qps
        if self.count_2xx is not None:
            result['Count2XX'] = self.count_2xx
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.failed_qps is not None:
            result['FailedQps'] = self.failed_qps
        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt
        if self.min_rt is not None:
            result['MinRt'] = self.min_rt
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.qps_2xx is not None:
            result['Qps2XX'] = self.qps_2xx
        if self.real_qps is not None:
            result['RealQps'] = self.real_qps
        if self.time_point is not None:
            result['TimePoint'] = self.time_point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('AverageRt') is not None:
            self.average_rt = m.get('AverageRt')
        if m.get('CheckPointResult') is not None:
            temp_model = GetPtsSceneRunningDataResponseBodyChainMonitorDataListCheckPointResult()
            self.check_point_result = temp_model.from_map(m['CheckPointResult'])
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConfigQps') is not None:
            self.config_qps = m.get('ConfigQps')
        if m.get('Count2XX') is not None:
            self.count_2xx = m.get('Count2XX')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('FailedQps') is not None:
            self.failed_qps = m.get('FailedQps')
        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')
        if m.get('MinRt') is not None:
            self.min_rt = m.get('MinRt')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Qps2XX') is not None:
            self.qps_2xx = m.get('Qps2XX')
        if m.get('RealQps') is not None:
            self.real_qps = m.get('RealQps')
        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')
        return self


class GetPtsSceneRunningDataResponseBody(TeaModel):
    def __init__(
        self,
        agent_location: List[GetPtsSceneRunningDataResponseBodyAgentLocation] = None,
        alive_agents: int = None,
        average_rt: int = None,
        begin_time: int = None,
        chain_monitor_data_list: List[GetPtsSceneRunningDataResponseBodyChainMonitorDataList] = None,
        code: str = None,
        concurrency: int = None,
        concurrency_limit: int = None,
        failed_business_count: int = None,
        failed_request_count: int = None,
        has_report: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_bps: str = None,
        request_id: str = None,
        response_bps: str = None,
        seg_90rt: int = None,
        status: int = None,
        success: bool = None,
        total_agents: int = None,
        total_request_count: int = None,
        tps_limit: int = None,
        vum: int = None,
    ):
        self.agent_location = agent_location
        self.alive_agents = alive_agents
        self.average_rt = average_rt
        self.begin_time = begin_time
        self.chain_monitor_data_list = chain_monitor_data_list
        self.code = code
        self.concurrency = concurrency
        self.concurrency_limit = concurrency_limit
        self.failed_business_count = failed_business_count
        self.failed_request_count = failed_request_count
        self.has_report = has_report
        self.http_status_code = http_status_code
        self.message = message
        self.request_bps = request_bps
        self.request_id = request_id
        self.response_bps = response_bps
        self.seg_90rt = seg_90rt
        self.status = status
        self.success = success
        self.total_agents = total_agents
        self.total_request_count = total_request_count
        self.tps_limit = tps_limit
        self.vum = vum

    def validate(self):
        if self.agent_location:
            for k in self.agent_location:
                if k:
                    k.validate()
        if self.chain_monitor_data_list:
            for k in self.chain_monitor_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AgentLocation'] = []
        if self.agent_location is not None:
            for k in self.agent_location:
                result['AgentLocation'].append(k.to_map() if k else None)
        if self.alive_agents is not None:
            result['AliveAgents'] = self.alive_agents
        if self.average_rt is not None:
            result['AverageRt'] = self.average_rt
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        result['ChainMonitorDataList'] = []
        if self.chain_monitor_data_list is not None:
            for k in self.chain_monitor_data_list:
                result['ChainMonitorDataList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.concurrency_limit is not None:
            result['ConcurrencyLimit'] = self.concurrency_limit
        if self.failed_business_count is not None:
            result['FailedBusinessCount'] = self.failed_business_count
        if self.failed_request_count is not None:
            result['FailedRequestCount'] = self.failed_request_count
        if self.has_report is not None:
            result['HasReport'] = self.has_report
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_bps is not None:
            result['RequestBps'] = self.request_bps
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_bps is not None:
            result['ResponseBps'] = self.response_bps
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.total_agents is not None:
            result['TotalAgents'] = self.total_agents
        if self.total_request_count is not None:
            result['TotalRequestCount'] = self.total_request_count
        if self.tps_limit is not None:
            result['TpsLimit'] = self.tps_limit
        if self.vum is not None:
            result['Vum'] = self.vum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_location = []
        if m.get('AgentLocation') is not None:
            for k in m.get('AgentLocation'):
                temp_model = GetPtsSceneRunningDataResponseBodyAgentLocation()
                self.agent_location.append(temp_model.from_map(k))
        if m.get('AliveAgents') is not None:
            self.alive_agents = m.get('AliveAgents')
        if m.get('AverageRt') is not None:
            self.average_rt = m.get('AverageRt')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        self.chain_monitor_data_list = []
        if m.get('ChainMonitorDataList') is not None:
            for k in m.get('ChainMonitorDataList'):
                temp_model = GetPtsSceneRunningDataResponseBodyChainMonitorDataList()
                self.chain_monitor_data_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConcurrencyLimit') is not None:
            self.concurrency_limit = m.get('ConcurrencyLimit')
        if m.get('FailedBusinessCount') is not None:
            self.failed_business_count = m.get('FailedBusinessCount')
        if m.get('FailedRequestCount') is not None:
            self.failed_request_count = m.get('FailedRequestCount')
        if m.get('HasReport') is not None:
            self.has_report = m.get('HasReport')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestBps') is not None:
            self.request_bps = m.get('RequestBps')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseBps') is not None:
            self.response_bps = m.get('ResponseBps')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalAgents') is not None:
            self.total_agents = m.get('TotalAgents')
        if m.get('TotalRequestCount') is not None:
            self.total_request_count = m.get('TotalRequestCount')
        if m.get('TpsLimit') is not None:
            self.tps_limit = m.get('TpsLimit')
        if m.get('Vum') is not None:
            self.vum = m.get('Vum')
        return self


class GetPtsSceneRunningDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPtsSceneRunningDataResponseBody = None,
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
            temp_model = GetPtsSceneRunningDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsSceneRunningStatusRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetPtsSceneRunningStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_time: str = None,
        http_status_code: int = None,
        message: str = None,
        modified_time: str = None,
        request_id: str = None,
        scene_name: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.create_time = create_time
        self.http_status_code = http_status_code
        self.message = message
        self.modified_time = modified_time
        self.request_id = request_id
        self.scene_name = scene_name
        self.status = status
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPtsSceneRunningStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPtsSceneRunningStatusResponseBody = None,
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
            temp_model = GetPtsSceneRunningStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnvsRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        env_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 环境ID
        self.env_id = env_id
        # 环境名
        self.env_name = env_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListEnvsResponseBodyEnvsFiles(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        file_name: str = None,
        file_oss_address: str = None,
        file_size: int = None,
        md_5: str = None,
    ):
        # 文件ID
        self.file_id = file_id
        # 文件名
        self.file_name = file_name
        # 文件的oss地址
        self.file_oss_address = file_oss_address
        # 文件大小，单位为Byte
        self.file_size = file_size
        # jar包的md5值
        self.md_5 = md_5

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_oss_address is not None:
            result['FileOssAddress'] = self.file_oss_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileOssAddress') is not None:
            self.file_oss_address = m.get('FileOssAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        return self


class ListEnvsResponseBodyEnvsProperties(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        # 描述
        self.description = description
        # 属性名
        self.name = name
        # 属性值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListEnvsResponseBodyEnvs(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        env_id: str = None,
        env_name: str = None,
        env_version: str = None,
        files: List[ListEnvsResponseBodyEnvsFiles] = None,
        modified_time: int = None,
        properties: List[ListEnvsResponseBodyEnvsProperties] = None,
        related_scenes: List[str] = None,
        running_scenes: List[str] = None,
        used_capacity: int = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 环境ID
        self.env_id = env_id
        # 环境名
        self.env_name = env_name
        # 依赖的jmeter版本
        self.env_version = env_version
        # 包含的jar包
        self.files = files
        # 修改时间
        self.modified_time = modified_time
        # jmeter属性
        self.properties = properties
        # 关联的场景
        self.related_scenes = related_scenes
        # 关联的场景id
        self.running_scenes = running_scenes
        # 环境的文件总大小
        self.used_capacity = used_capacity

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        if self.env_version is not None:
            result['EnvVersion'] = self.env_version
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        result['Properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['Properties'].append(k.to_map() if k else None)
        if self.related_scenes is not None:
            result['RelatedScenes'] = self.related_scenes
        if self.running_scenes is not None:
            result['RunningScenes'] = self.running_scenes
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        if m.get('EnvVersion') is not None:
            self.env_version = m.get('EnvVersion')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = ListEnvsResponseBodyEnvsFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        self.properties = []
        if m.get('Properties') is not None:
            for k in m.get('Properties'):
                temp_model = ListEnvsResponseBodyEnvsProperties()
                self.properties.append(temp_model.from_map(k))
        if m.get('RelatedScenes') is not None:
            self.related_scenes = m.get('RelatedScenes')
        if m.get('RunningScenes') is not None:
            self.running_scenes = m.get('RunningScenes')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        return self


class ListEnvsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        envs: List[ListEnvsResponseBodyEnvs] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        # 环境列表
        self.envs = envs
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.envs:
            for k in self.envs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Envs'] = []
        if self.envs is not None:
            for k in self.envs:
                result['Envs'].append(k.to_map() if k else None)
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.envs = []
        if m.get('Envs') is not None:
            for k in m.get('Envs'):
                temp_model = ListEnvsResponseBodyEnvs()
                self.envs.append(temp_model.from_map(k))
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
        return self


class ListEnvsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEnvsResponseBody = None,
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
            temp_model = ListEnvsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJMeterReportsRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        report_id: str = None,
        scene_id: str = None,
    ):
        # 报告的起始时间，单位为ms
        self.begin_time = begin_time
        # 报告的结束时间
        self.end_time = end_time
        # 报告关键字
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        # 报告ID
        self.report_id = report_id
        # 要查看的报告的场景id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListJMeterReportsResponseBodyReports(TeaModel):
    def __init__(
        self,
        actual_start_time: int = None,
        duration: str = None,
        report_id: str = None,
        report_name: str = None,
        vum: int = None,
    ):
        # 压测开始时间
        self.actual_start_time = actual_start_time
        # 压测持续时间
        self.duration = duration
        # 报告id
        self.report_id = report_id
        # 报告名称
        self.report_name = report_name
        # 消耗的vum
        self.vum = vum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_start_time is not None:
            result['ActualStartTime'] = self.actual_start_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.report_name is not None:
            result['ReportName'] = self.report_name
        if self.vum is not None:
            result['Vum'] = self.vum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualStartTime') is not None:
            self.actual_start_time = m.get('ActualStartTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('ReportName') is not None:
            self.report_name = m.get('ReportName')
        if m.get('Vum') is not None:
            self.vum = m.get('Vum')
        return self


class ListJMeterReportsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        reports: List[ListJMeterReportsResponseBodyReports] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.reports = reports
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.reports:
            for k in self.reports:
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
        result['Reports'] = []
        if self.reports is not None:
            for k in self.reports:
                result['Reports'].append(k.to_map() if k else None)
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
        self.reports = []
        if m.get('Reports') is not None:
            for k in m.get('Reports'):
                temp_model = ListJMeterReportsResponseBodyReports()
                self.reports.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJMeterReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListJMeterReportsResponseBody = None,
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
            temp_model = ListJMeterReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpenJMeterScenesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        scene_id: str = None,
        scene_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # 场景id
        self.scene_id = scene_id
        # 场景名
        self.scene_name = scene_name

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
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class ListOpenJMeterScenesResponseBodyJMeterScene(TeaModel):
    def __init__(
        self,
        duration_str: str = None,
        scene_id: str = None,
        scene_name: str = None,
    ):
        # 压测持续时间
        self.duration_str = duration_str
        # 场景id
        self.scene_id = scene_id
        # 场景名
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration_str is not None:
            result['DurationStr'] = self.duration_str
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationStr') is not None:
            self.duration_str = m.get('DurationStr')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class ListOpenJMeterScenesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        jmeter_scene: List[ListOpenJMeterScenesResponseBodyJMeterScene] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.jmeter_scene = jmeter_scene
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.jmeter_scene:
            for k in self.jmeter_scene:
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
        result['JMeterScene'] = []
        if self.jmeter_scene is not None:
            for k in self.jmeter_scene:
                result['JMeterScene'].append(k.to_map() if k else None)
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.jmeter_scene = []
        if m.get('JMeterScene') is not None:
            for k in m.get('JMeterScene'):
                temp_model = ListOpenJMeterScenesResponseBodyJMeterScene()
                self.jmeter_scene.append(temp_model.from_map(k))
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
        return self


class ListOpenJMeterScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOpenJMeterScenesResponseBody = None,
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
            temp_model = ListOpenJMeterScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPtsSceneRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.key_word = key_word
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_word is not None:
            result['KeyWord'] = self.key_word
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListPtsSceneResponseBodySceneViewList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        scene_id: str = None,
        scene_name: str = None,
    ):
        self.create_time = create_time
        self.scene_id = scene_id
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class ListPtsSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scene_view_list: List[ListPtsSceneResponseBodySceneViewList] = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.scene_view_list = scene_view_list
        self.success = success

    def validate(self):
        if self.scene_view_list:
            for k in self.scene_view_list:
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
        result['SceneViewList'] = []
        if self.scene_view_list is not None:
            for k in self.scene_view_list:
                result['SceneViewList'].append(k.to_map() if k else None)
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
        self.scene_view_list = []
        if m.get('SceneViewList') is not None:
            for k in m.get('SceneViewList'):
                temp_model = ListPtsSceneResponseBodySceneViewList()
                self.scene_view_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListPtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPtsSceneResponseBody = None,
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
            temp_model = ListPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene: str = None,
    ):
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ModifyPtsSceneResponseBody(TeaModel):
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


class ModifyPtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyPtsSceneResponseBody = None,
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
            temp_model = ModifyPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
    ):
        # 要删除的环境ID
        self.env_id = env_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        return self


class RemoveEnvResponseBody(TeaModel):
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


class RemoveEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveEnvResponseBody = None,
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
            temp_model = RemoveEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveOpenJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class RemoveOpenJMeterSceneResponseBody(TeaModel):
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


class RemoveOpenJMeterSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveOpenJMeterSceneResponseBody = None,
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
            temp_model = RemoveOpenJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveEnvRequestEnvFiles(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_oss_address: str = None,
    ):
        # 文件名
        self.file_name = file_name
        # 文件oss地址，目前只支持上海region的oss地址
        self.file_oss_address = file_oss_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_oss_address is not None:
            result['FileOssAddress'] = self.file_oss_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileOssAddress') is not None:
            self.file_oss_address = m.get('FileOssAddress')
        return self


class SaveEnvRequestEnvProperties(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        # 描述
        self.description = description
        # 属性名
        self.name = name
        # 属性值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SaveEnvRequestEnv(TeaModel):
    def __init__(
        self,
        env_id: str = None,
        env_name: str = None,
        files: List[SaveEnvRequestEnvFiles] = None,
        jmeter_plugin_label: str = None,
        properties: List[SaveEnvRequestEnvProperties] = None,
    ):
        # 环境id，不填表示新建环境，填了表示修改该环境
        self.env_id = env_id
        # 环境名称
        self.env_name = env_name
        # 环境依赖的文件
        self.files = files
        # jmeter插件的环境标签
        self.jmeter_plugin_label = jmeter_plugin_label
        # jmeter属性
        self.properties = properties

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_id is not None:
            result['EnvId'] = self.env_id
        if self.env_name is not None:
            result['EnvName'] = self.env_name
        result['Files'] = []
        if self.files is not None:
            for k in self.files:
                result['Files'].append(k.to_map() if k else None)
        if self.jmeter_plugin_label is not None:
            result['JmeterPluginLabel'] = self.jmeter_plugin_label
        result['Properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['Properties'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('EnvName') is not None:
            self.env_name = m.get('EnvName')
        self.files = []
        if m.get('Files') is not None:
            for k in m.get('Files'):
                temp_model = SaveEnvRequestEnvFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('JmeterPluginLabel') is not None:
            self.jmeter_plugin_label = m.get('JmeterPluginLabel')
        self.properties = []
        if m.get('Properties') is not None:
            for k in m.get('Properties'):
                temp_model = SaveEnvRequestEnvProperties()
                self.properties.append(temp_model.from_map(k))
        return self


class SaveEnvRequest(TeaModel):
    def __init__(
        self,
        env: SaveEnvRequestEnv = None,
    ):
        # 环境
        self.env = env

    def validate(self):
        if self.env:
            self.env.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            temp_model = SaveEnvRequestEnv()
            self.env = temp_model.from_map(m['Env'])
        return self


class SaveEnvShrinkRequest(TeaModel):
    def __init__(
        self,
        env_shrink: str = None,
    ):
        # 环境
        self.env_shrink = env_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_shrink is not None:
            result['Env'] = self.env_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env_shrink = m.get('Env')
        return self


class SaveEnvResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        env_id: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # 操作的环境id
        self.env_id = env_id
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
        if self.env_id is not None:
            result['EnvId'] = self.env_id
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
        if m.get('EnvId') is not None:
            self.env_id = m.get('EnvId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveEnvResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveEnvResponseBody = None,
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
            temp_model = SaveEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveOpenJMeterSceneRequestOpenJMeterSceneDnsCacheConfig(TeaModel):
    def __init__(
        self,
        clear_cache_each_iteration: bool = None,
        dns_servers: List[str] = None,
        host_table: Dict[str, str] = None,
    ):
        self.clear_cache_each_iteration = clear_cache_each_iteration
        self.dns_servers = dns_servers
        self.host_table = host_table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clear_cache_each_iteration is not None:
            result['ClearCacheEachIteration'] = self.clear_cache_each_iteration
        if self.dns_servers is not None:
            result['DnsServers'] = self.dns_servers
        if self.host_table is not None:
            result['HostTable'] = self.host_table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClearCacheEachIteration') is not None:
            self.clear_cache_each_iteration = m.get('ClearCacheEachIteration')
        if m.get('DnsServers') is not None:
            self.dns_servers = m.get('DnsServers')
        if m.get('HostTable') is not None:
            self.host_table = m.get('HostTable')
        return self


class SaveOpenJMeterSceneRequestOpenJMeterSceneFileList(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        file_name: str = None,
        file_oss_address: str = None,
        file_size: int = None,
        md_5: str = None,
        split_csv: bool = None,
        tags: str = None,
    ):
        # 文件id
        self.file_id = file_id
        # 文件名
        self.file_name = file_name
        # 文件公网可访问的oss地址
        self.file_oss_address = file_oss_address
        # 文件大小，单位byte
        self.file_size = file_size
        # 文件的MD5
        self.md_5 = md_5
        # 是否切分，仅针对csv有效
        self.split_csv = split_csv
        # 文件tag
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_oss_address is not None:
            result['FileOssAddress'] = self.file_oss_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.split_csv is not None:
            result['SplitCsv'] = self.split_csv
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileOssAddress') is not None:
            self.file_oss_address = m.get('FileOssAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('SplitCsv') is not None:
            self.split_csv = m.get('SplitCsv')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SaveOpenJMeterSceneRequestOpenJMeterSceneJMeterProperties(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SaveOpenJMeterSceneRequestOpenJMeterScene(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        concurrency: int = None,
        constant_throughput_timer_type: str = None,
        dns_cache_config: SaveOpenJMeterSceneRequestOpenJMeterSceneDnsCacheConfig = None,
        duration: int = None,
        environment_id: str = None,
        file_list: List[SaveOpenJMeterSceneRequestOpenJMeterSceneFileList] = None,
        is_vpc_test: bool = None,
        jmeter_properties: List[SaveOpenJMeterSceneRequestOpenJMeterSceneJMeterProperties] = None,
        jmeter_plugin_label: str = None,
        ramp_up: int = None,
        region_id: str = None,
        scene_id: str = None,
        scene_name: str = None,
        security_group_id: str = None,
        steps: int = None,
        sync_timer_type: str = None,
        test_file: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # 施压引擎数量
        self.agent_count = agent_count
        # 最大并发
        self.concurrency = concurrency
        # constantThroughputTimerType
        self.constant_throughput_timer_type = constant_throughput_timer_type
        # DNS配置
        self.dns_cache_config = dns_cache_config
        # 压测持续时间
        self.duration = duration
        # 关联的环境id
        self.environment_id = environment_id
        # 文件列表
        self.file_list = file_list
        # 是否为VPC测试，默认为false表示公网测试，此值为true时VPC相关配置才生效
        self.is_vpc_test = is_vpc_test
        # Jmeter属性
        self.jmeter_properties = jmeter_properties
        # jmeter插件的环境标签
        self.jmeter_plugin_label = jmeter_plugin_label
        # 预热时间
        self.ramp_up = ramp_up
        # region的id，VPC压测时配置
        self.region_id = region_id
        # 场景ID
        self.scene_id = scene_id
        # 场景名
        self.scene_name = scene_name
        # 安全组id，VPC压测时配置
        self.security_group_id = security_group_id
        # 预热阶段
        self.steps = steps
        # synchronizing timer 类型
        self.sync_timer_type = sync_timer_type
        # 测试文件
        self.test_file = test_file
        # 交换机id，VPC压测时配置
        self.v_switch_id = v_switch_id
        # vpc的id，VPC压测时配置
        self.vpc_id = vpc_id

    def validate(self):
        if self.dns_cache_config:
            self.dns_cache_config.validate()
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()
        if self.jmeter_properties:
            for k in self.jmeter_properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_count is not None:
            result['AgentCount'] = self.agent_count
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.constant_throughput_timer_type is not None:
            result['ConstantThroughputTimerType'] = self.constant_throughput_timer_type
        if self.dns_cache_config is not None:
            result['DnsCacheConfig'] = self.dns_cache_config.to_map()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.is_vpc_test is not None:
            result['IsVpcTest'] = self.is_vpc_test
        result['JMeterProperties'] = []
        if self.jmeter_properties is not None:
            for k in self.jmeter_properties:
                result['JMeterProperties'].append(k.to_map() if k else None)
        if self.jmeter_plugin_label is not None:
            result['JmeterPluginLabel'] = self.jmeter_plugin_label
        if self.ramp_up is not None:
            result['RampUp'] = self.ramp_up
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.steps is not None:
            result['Steps'] = self.steps
        if self.sync_timer_type is not None:
            result['SyncTimerType'] = self.sync_timer_type
        if self.test_file is not None:
            result['TestFile'] = self.test_file
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConstantThroughputTimerType') is not None:
            self.constant_throughput_timer_type = m.get('ConstantThroughputTimerType')
        if m.get('DnsCacheConfig') is not None:
            temp_model = SaveOpenJMeterSceneRequestOpenJMeterSceneDnsCacheConfig()
            self.dns_cache_config = temp_model.from_map(m['DnsCacheConfig'])
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = SaveOpenJMeterSceneRequestOpenJMeterSceneFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('IsVpcTest') is not None:
            self.is_vpc_test = m.get('IsVpcTest')
        self.jmeter_properties = []
        if m.get('JMeterProperties') is not None:
            for k in m.get('JMeterProperties'):
                temp_model = SaveOpenJMeterSceneRequestOpenJMeterSceneJMeterProperties()
                self.jmeter_properties.append(temp_model.from_map(k))
        if m.get('JmeterPluginLabel') is not None:
            self.jmeter_plugin_label = m.get('JmeterPluginLabel')
        if m.get('RampUp') is not None:
            self.ramp_up = m.get('RampUp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Steps') is not None:
            self.steps = m.get('Steps')
        if m.get('SyncTimerType') is not None:
            self.sync_timer_type = m.get('SyncTimerType')
        if m.get('TestFile') is not None:
            self.test_file = m.get('TestFile')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class SaveOpenJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        open_jmeter_scene: SaveOpenJMeterSceneRequestOpenJMeterScene = None,
    ):
        # 场景详情
        self.open_jmeter_scene = open_jmeter_scene

    def validate(self):
        if self.open_jmeter_scene:
            self.open_jmeter_scene.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_jmeter_scene is not None:
            result['OpenJMeterScene'] = self.open_jmeter_scene.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenJMeterScene') is not None:
            temp_model = SaveOpenJMeterSceneRequestOpenJMeterScene()
            self.open_jmeter_scene = temp_model.from_map(m['OpenJMeterScene'])
        return self


class SaveOpenJMeterSceneShrinkRequest(TeaModel):
    def __init__(
        self,
        open_jmeter_scene_shrink: str = None,
    ):
        # 场景详情
        self.open_jmeter_scene_shrink = open_jmeter_scene_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_jmeter_scene_shrink is not None:
            result['OpenJMeterScene'] = self.open_jmeter_scene_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenJMeterScene') is not None:
            self.open_jmeter_scene_shrink = m.get('OpenJMeterScene')
        return self


class SaveOpenJMeterSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scene_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        # 场景id
        self.scene_id = scene_id
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
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
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
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveOpenJMeterSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveOpenJMeterSceneResponseBody = None,
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
            temp_model = SaveOpenJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDebugPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StartDebugPtsSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        plan_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.plan_id = plan_id
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
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
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
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartDebugPtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDebugPtsSceneResponseBody = None,
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
            temp_model = StartDebugPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDebuggingJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StartDebuggingJMeterSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        report_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.report_id = report_id
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
        if self.report_id is not None:
            result['ReportId'] = self.report_id
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
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartDebuggingJMeterSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDebuggingJMeterSceneResponseBody = None,
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
            temp_model = StartDebuggingJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StartPtsSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        plan_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.plan_id = plan_id
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
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
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
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartPtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartPtsSceneResponseBody = None,
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
            temp_model = StartPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTestingJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StartTestingJMeterSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        report_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.report_id = report_id
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
        if self.report_id is not None:
            result['ReportId'] = self.report_id
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
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartTestingJMeterSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartTestingJMeterSceneResponseBody = None,
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
            temp_model = StartTestingJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDebugPtsSceneRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        scene_id: str = None,
    ):
        self.plan_id = plan_id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StopDebugPtsSceneResponseBody(TeaModel):
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


class StopDebugPtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDebugPtsSceneResponseBody = None,
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
            temp_model = StopDebugPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDebuggingJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StopDebuggingJMeterSceneResponseBody(TeaModel):
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


class StopDebuggingJMeterSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDebuggingJMeterSceneResponseBody = None,
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
            temp_model = StopDebuggingJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StopPtsSceneResponseBody(TeaModel):
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


class StopPtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopPtsSceneResponseBody = None,
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
            temp_model = StopPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTestingJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景id
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class StopTestingJMeterSceneResponseBody(TeaModel):
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


class StopTestingJMeterSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopTestingJMeterSceneResponseBody = None,
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
            temp_model = StopTestingJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePtsSceneBaseLineRequest(TeaModel):
    def __init__(
        self,
        api_baselines: Dict[str, Any] = None,
        scene_baseline: Dict[str, Any] = None,
        scene_id: str = None,
    ):
        self.api_baselines = api_baselines
        self.scene_baseline = scene_baseline
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_baselines is not None:
            result['ApiBaselines'] = self.api_baselines
        if self.scene_baseline is not None:
            result['SceneBaseline'] = self.scene_baseline
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiBaselines') is not None:
            self.api_baselines = m.get('ApiBaselines')
        if m.get('SceneBaseline') is not None:
            self.scene_baseline = m.get('SceneBaseline')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class UpdatePtsSceneBaseLineShrinkRequest(TeaModel):
    def __init__(
        self,
        api_baselines_shrink: str = None,
        scene_baseline_shrink: str = None,
        scene_id: str = None,
    ):
        self.api_baselines_shrink = api_baselines_shrink
        self.scene_baseline_shrink = scene_baseline_shrink
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_baselines_shrink is not None:
            result['ApiBaselines'] = self.api_baselines_shrink
        if self.scene_baseline_shrink is not None:
            result['SceneBaseline'] = self.scene_baseline_shrink
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiBaselines') is not None:
            self.api_baselines_shrink = m.get('ApiBaselines')
        if m.get('SceneBaseline') is not None:
            self.scene_baseline_shrink = m.get('SceneBaseline')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class UpdatePtsSceneBaseLineResponseBody(TeaModel):
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


class UpdatePtsSceneBaseLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePtsSceneBaseLineResponseBody = None,
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
            temp_model = UpdatePtsSceneBaseLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


