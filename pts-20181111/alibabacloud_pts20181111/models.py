# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class GetReportRequest(TeaModel):
    def __init__(
        self,
        report_id: int = None,
    ):
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        return self


class GetReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        snapshot: str = None,
        success: bool = None,
        summary: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.snapshot = snapshot
        self.success = success
        self.summary = summary

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
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        if self.success is not None:
            result['Success'] = self.success
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReportResponseBody = None,
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
            temp_model = GetReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRunnableScenesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRunnableScenesResponseBodyScenesScene(TeaModel):
    def __init__(
        self,
        duration: int = None,
        modified_time: int = None,
        scene_id: int = None,
        scene_name: str = None,
    ):
        self.duration = duration
        self.modified_time = modified_time
        self.scene_id = scene_id
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class ListRunnableScenesResponseBodyScenes(TeaModel):
    def __init__(
        self,
        scene: List[ListRunnableScenesResponseBodyScenesScene] = None,
    ):
        self.scene = scene

    def validate(self):
        if self.scene:
            for k in self.scene:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Scene'] = []
        if self.scene is not None:
            for k in self.scene:
                result['Scene'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scene = []
        if m.get('Scene') is not None:
            for k in m.get('Scene'):
                temp_model = ListRunnableScenesResponseBodyScenesScene()
                self.scene.append(temp_model.from_map(k))
        return self


class ListRunnableScenesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scenes: ListRunnableScenesResponseBodyScenes = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.scenes = scenes
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.scenes:
            self.scenes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scenes is not None:
            result['Scenes'] = self.scenes.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scenes') is not None:
            temp_model = ListRunnableScenesResponseBodyScenes()
            self.scenes = temp_model.from_map(m['Scenes'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRunnableScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRunnableScenesResponseBody = None,
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
            temp_model = ListRunnableScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPlanStatusRequest(TeaModel):
    def __init__(
        self,
        report_id: int = None,
        scene_id: int = None,
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


class QueryPlanStatusResponseBodyAgentLocations(TeaModel):
    def __init__(
        self,
        agent_location: List[Dict[str, Any]] = None,
    ):
        self.agent_location = agent_location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_location is not None:
            result['AgentLocation'] = self.agent_location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentLocation') is not None:
            self.agent_location = m.get('AgentLocation')
        return self


class QueryPlanStatusResponseBodyMonitorData(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryPlanStatusResponseBody(TeaModel):
    def __init__(
        self,
        agent_locations: QueryPlanStatusResponseBodyAgentLocations = None,
        alive_agent_count: int = None,
        average_rt: int = None,
        bps_request: str = None,
        bps_response: str = None,
        code: str = None,
        concurrency: int = None,
        concurrency_limit: int = None,
        current_time: int = None,
        failed_business_count: int = None,
        failed_request_count: int = None,
        message: str = None,
        monitor_data: QueryPlanStatusResponseBodyMonitorData = None,
        report_id: int = None,
        request_count: str = None,
        request_id: str = None,
        seg_90rt: int = None,
        start_time: int = None,
        success: bool = None,
        tips: str = None,
        total_agent_count: int = None,
        tps: int = None,
        tps_limit: int = None,
        vum: int = None,
    ):
        self.agent_locations = agent_locations
        self.alive_agent_count = alive_agent_count
        self.average_rt = average_rt
        self.bps_request = bps_request
        self.bps_response = bps_response
        self.code = code
        self.concurrency = concurrency
        self.concurrency_limit = concurrency_limit
        self.current_time = current_time
        self.failed_business_count = failed_business_count
        self.failed_request_count = failed_request_count
        self.message = message
        self.monitor_data = monitor_data
        self.report_id = report_id
        self.request_count = request_count
        self.request_id = request_id
        self.seg_90rt = seg_90rt
        self.start_time = start_time
        self.success = success
        self.tips = tips
        self.total_agent_count = total_agent_count
        self.tps = tps
        self.tps_limit = tps_limit
        self.vum = vum

    def validate(self):
        if self.agent_locations:
            self.agent_locations.validate()
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_locations is not None:
            result['AgentLocations'] = self.agent_locations.to_map()
        if self.alive_agent_count is not None:
            result['AliveAgentCount'] = self.alive_agent_count
        if self.average_rt is not None:
            result['AverageRt'] = self.average_rt
        if self.bps_request is not None:
            result['BpsRequest'] = self.bps_request
        if self.bps_response is not None:
            result['BpsResponse'] = self.bps_response
        if self.code is not None:
            result['Code'] = self.code
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.concurrency_limit is not None:
            result['ConcurrencyLimit'] = self.concurrency_limit
        if self.current_time is not None:
            result['CurrentTime'] = self.current_time
        if self.failed_business_count is not None:
            result['FailedBusinessCount'] = self.failed_business_count
        if self.failed_request_count is not None:
            result['FailedRequestCount'] = self.failed_request_count
        if self.message is not None:
            result['Message'] = self.message
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_count is not None:
            result['RequestCount'] = self.request_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.success is not None:
            result['Success'] = self.success
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.total_agent_count is not None:
            result['TotalAgentCount'] = self.total_agent_count
        if self.tps is not None:
            result['Tps'] = self.tps
        if self.tps_limit is not None:
            result['TpsLimit'] = self.tps_limit
        if self.vum is not None:
            result['Vum'] = self.vum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentLocations') is not None:
            temp_model = QueryPlanStatusResponseBodyAgentLocations()
            self.agent_locations = temp_model.from_map(m['AgentLocations'])
        if m.get('AliveAgentCount') is not None:
            self.alive_agent_count = m.get('AliveAgentCount')
        if m.get('AverageRt') is not None:
            self.average_rt = m.get('AverageRt')
        if m.get('BpsRequest') is not None:
            self.bps_request = m.get('BpsRequest')
        if m.get('BpsResponse') is not None:
            self.bps_response = m.get('BpsResponse')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConcurrencyLimit') is not None:
            self.concurrency_limit = m.get('ConcurrencyLimit')
        if m.get('CurrentTime') is not None:
            self.current_time = m.get('CurrentTime')
        if m.get('FailedBusinessCount') is not None:
            self.failed_business_count = m.get('FailedBusinessCount')
        if m.get('FailedRequestCount') is not None:
            self.failed_request_count = m.get('FailedRequestCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('MonitorData') is not None:
            temp_model = QueryPlanStatusResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m['MonitorData'])
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('TotalAgentCount') is not None:
            self.total_agent_count = m.get('TotalAgentCount')
        if m.get('Tps') is not None:
            self.tps = m.get('Tps')
        if m.get('TpsLimit') is not None:
            self.tps_limit = m.get('TpsLimit')
        if m.get('Vum') is not None:
            self.vum = m.get('Vum')
        return self


class QueryPlanStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPlanStatusResponseBody = None,
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
            temp_model = QueryPlanStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
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


class StartSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        report_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSceneResponseBody = None,
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
            temp_model = StartSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: int = None,
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


class StopSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopSceneResponseBody = None,
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
            temp_model = StopSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


