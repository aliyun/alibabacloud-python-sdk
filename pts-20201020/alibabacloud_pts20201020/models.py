# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AdjustJMeterSceneSpeedRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
        speed: int = None,
    ):
        # The ID of the report.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The load to which you want to adjust.
        # 
        # This parameter is required.
        self.speed = speed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.speed is not None:
            result['Speed'] = self.speed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        return self


class AdjustJMeterSceneSpeedResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        report_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the report.
        self.report_id = report_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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


class AdjustJMeterSceneSpeedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AdjustJMeterSceneSpeedResponseBody = None,
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
            temp_model = AdjustJMeterSceneSpeedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AdjustPtsSceneSpeedRequestApiSpeedList(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        speed: int = None,
    ):
        # The API ID. You can find the information of the API corresponding to the ID in the Relation response parameter of the GetPtsSceneRunningData operation based on the ID.
        self.api_id = api_id
        # The new stress. In concurrency mode, the new stress is the concurrency. In RPS mode, the new stress is the RPS.
        self.speed = speed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.speed is not None:
            result['Speed'] = self.speed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        return self


class AdjustPtsSceneSpeedRequest(TeaModel):
    def __init__(
        self,
        api_speed_list: List[AdjustPtsSceneSpeedRequestApiSpeedList] = None,
        scene_id: str = None,
    ):
        # The stress testing speed in the PTS scenario.
        self.api_speed_list = api_speed_list
        # The scenario ID.
        # 
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        if self.api_speed_list:
            for k in self.api_speed_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApiSpeedList'] = []
        if self.api_speed_list is not None:
            for k in self.api_speed_list:
                result['ApiSpeedList'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_speed_list = []
        if m.get('ApiSpeedList') is not None:
            for k in m.get('ApiSpeedList'):
                temp_model = AdjustPtsSceneSpeedRequestApiSpeedList()
                self.api_speed_list.append(temp_model.from_map(k))
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class AdjustPtsSceneSpeedShrinkRequest(TeaModel):
    def __init__(
        self,
        api_speed_list_shrink: str = None,
        scene_id: str = None,
    ):
        # The stress testing speed in the PTS scenario.
        self.api_speed_list_shrink = api_speed_list_shrink
        # The scenario ID.
        # 
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_speed_list_shrink is not None:
            result['ApiSpeedList'] = self.api_speed_list_shrink
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiSpeedList') is not None:
            self.api_speed_list_shrink = m.get('ApiSpeedList')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class AdjustPtsSceneSpeedResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, no data is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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


class AdjustPtsSceneSpeedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AdjustPtsSceneSpeedResponseBody = None,
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
            temp_model = AdjustPtsSceneSpeedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene: str = None,
    ):
        # The scenario details.
        # 
        # This parameter is required.
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
        # The system status code. If the request was successful, no data is returned.
        self.code = code
        # The HTTP status code. If the request was successful, no data is returned.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, no data is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The ID of the created scenario.
        self.scene_id = scene_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: CreatePtsSceneResponseBody = None,
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
            temp_model = CreatePtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePtsSceneBaseLineFromReportRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
        scene_id: str = None,
    ):
        # The ID of the report. For more information, see the [table](https://help.aliyun.com/document_detail/201321.html) provided in this topic.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The ID of the scene. For more information, see the [table](https://help.aliyun.com/document_detail/201321.html) provided in this topic.
        # 
        # This parameter is required.
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # null
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false:
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
        status_code: int = None,
        body: CreatePtsSceneBaseLineFromReportResponseBody = None,
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
            temp_model = CreatePtsSceneBaseLineFromReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the PTS scenario that you want to delete.
        # 
        # This parameter is required.
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
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: DeletePtsSceneResponseBody = None,
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
            temp_model = DeletePtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePtsSceneBaseLineRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # This parameter is required.
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
        status_code: int = None,
        body: DeletePtsSceneBaseLineResponseBody = None,
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
            temp_model = DeletePtsSceneBaseLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePtsScenesRequest(TeaModel):
    def __init__(
        self,
        scene_ids: List[str] = None,
    ):
        # This parameter is required.
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
        # This parameter is required.
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
        status_code: int = None,
        body: DeletePtsScenesResponseBody = None,
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
            temp_model = DeletePtsScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllRegionsResponseBody(TeaModel):
    def __init__(
        self,
        all_regions: Dict[str, str] = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The supported regions.
        self.all_regions = all_regions
        # The system status code. If the request was successful, no data is returned.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, no data is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_regions is not None:
            result['AllRegions'] = self.all_regions
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
        if m.get('AllRegions') is not None:
            self.all_regions = m.get('AllRegions')
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


class GetAllRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAllRegionsResponseBody = None,
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
            temp_model = GetAllRegionsResponseBody()
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
        # Specifies that the operational logs of the stress tester identified as number 0 are returned if the agent index is invalid.
        self.agent_index = agent_index
        # The beginning of the time range to query. Unit: seconds.
        self.begin_time = begin_time
        # The end of the time range to query. Unit: seconds.
        self.end_time = end_time
        # The keyword.
        self.keyword = keyword
        # The log level. Valid values:
        # 
        # *   ERROR
        # *   WARN
        # *   INFO (default)
        # *   DEBUG
        # *   TRACE
        self.level = level
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The report ID.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The thread name.
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
        # The number of engines. The AgentCount value must be greater than the PageNumber value.
        self.agent_count = agent_count
        # The system status code. If the request was successful, this parameter is left empty.
        self.code = code
        # The returned entries.
        self.logs = logs
        # The returned message. If the request was successful, this parameter is left empty.
        self.message = message
        # The number of the returned page.
        self.page_number = page_number
        # The number of returned entries.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of returned entries.
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
        status_code: int = None,
        body: GetJMeterLogsResponseBody = None,
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
            temp_model = GetJMeterLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJMeterReportDetailsRequest(TeaModel):
    def __init__(
        self,
        report_id: str = None,
    ):
        # The report ID.
        # 
        # This parameter is required.
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


class GetJMeterReportDetailsResponseBodyReportOverView(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        end_time: str = None,
        report_id: str = None,
        report_name: str = None,
        start_time: str = None,
        vum: int = None,
    ):
        # The number of used engines.
        self.agent_count = agent_count
        # The end of the queried time range.
        self.end_time = end_time
        # The report ID.
        self.report_id = report_id
        # The report name.
        self.report_name = report_name
        # The beginning of the queried time range.
        self.start_time = start_time
        # The consumed Virtual User Minutes (VUM).
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


class GetJMeterReportDetailsResponseBodySamplerMetricsList(TeaModel):
    def __init__(
        self,
        all_count: int = None,
        api_name: str = None,
        avg_rt: float = None,
        avg_tps: float = None,
        fail_count_req: int = None,
        max_rt: float = None,
        min_rt: float = None,
        seg_75rt: float = None,
        seg_90rt: float = None,
        seg_99rt: float = None,
        success_rate_req: float = None,
    ):
        # The total number of requests.
        self.all_count = all_count
        # The API name.
        self.api_name = api_name
        # The average RT. Unit: milliseconds.
        self.avg_rt = avg_rt
        # The average TPS.
        self.avg_tps = avg_tps
        # The request failure rate.
        self.fail_count_req = fail_count_req
        # The maximum RT. Unit: milliseconds.
        self.max_rt = max_rt
        # The minimum RT. Unit: milliseconds.
        self.min_rt = min_rt
        # The 75th percentile of RT. Unit: milliseconds.
        self.seg_75rt = seg_75rt
        # The 90th percentile of RT. Unit: milliseconds.
        self.seg_90rt = seg_90rt
        # The 99th percentile of RT. Unit: milliseconds.
        self.seg_99rt = seg_99rt
        # The request success rate. The parameter value must be a non-negative number less than or equal to 100.
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
        if self.fail_count_req is not None:
            result['FailCountReq'] = self.fail_count_req
        if self.max_rt is not None:
            result['MaxRt'] = self.max_rt
        if self.min_rt is not None:
            result['MinRt'] = self.min_rt
        if self.seg_75rt is not None:
            result['Seg75Rt'] = self.seg_75rt
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.seg_99rt is not None:
            result['Seg99Rt'] = self.seg_99rt
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
        if m.get('FailCountReq') is not None:
            self.fail_count_req = m.get('FailCountReq')
        if m.get('MaxRt') is not None:
            self.max_rt = m.get('MaxRt')
        if m.get('MinRt') is not None:
            self.min_rt = m.get('MinRt')
        if m.get('Seg75Rt') is not None:
            self.seg_75rt = m.get('Seg75Rt')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('Seg99Rt') is not None:
            self.seg_99rt = m.get('Seg99Rt')
        if m.get('SuccessRateReq') is not None:
            self.success_rate_req = m.get('SuccessRateReq')
        return self


class GetJMeterReportDetailsResponseBodySceneMetrics(TeaModel):
    def __init__(
        self,
        all_count: int = None,
        avg_rt: float = None,
        avg_tps: float = None,
        fail_count_req: int = None,
        seg_90rt: float = None,
        seg_99rt: float = None,
        success_rate_req: float = None,
    ):
        # The total number of requests.
        self.all_count = all_count
        # The average response time (RT). Unit: milliseconds.
        self.avg_rt = avg_rt
        # The average transactions per second (TPS).
        self.avg_tps = avg_tps
        # The request failure rate.
        self.fail_count_req = fail_count_req
        # The 90th percentile of RT. Unit: milliseconds.
        self.seg_90rt = seg_90rt
        # The 99th percentile of RT. Unit: milliseconds.
        self.seg_99rt = seg_99rt
        # The request success rate. The parameter value must be a non-negative number less than or equal to 100.
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
        if self.fail_count_req is not None:
            result['FailCountReq'] = self.fail_count_req
        if self.seg_90rt is not None:
            result['Seg90Rt'] = self.seg_90rt
        if self.seg_99rt is not None:
            result['Seg99Rt'] = self.seg_99rt
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
        if m.get('FailCountReq') is not None:
            self.fail_count_req = m.get('FailCountReq')
        if m.get('Seg90Rt') is not None:
            self.seg_90rt = m.get('Seg90Rt')
        if m.get('Seg99Rt') is not None:
            self.seg_99rt = m.get('Seg99Rt')
        if m.get('SuccessRateReq') is not None:
            self.success_rate_req = m.get('SuccessRateReq')
        return self


class GetJMeterReportDetailsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        code_key: str = None,
        document_url: str = None,
        dynamic_ctx: str = None,
        http_status_code: int = None,
        message: str = None,
        report_over_view: GetJMeterReportDetailsResponseBodyReportOverView = None,
        request_id: str = None,
        sampler_metrics_list: List[GetJMeterReportDetailsResponseBodySamplerMetricsList] = None,
        scene_metrics: GetJMeterReportDetailsResponseBodySceneMetrics = None,
        success: bool = None,
    ):
        # The system status code. If the request was successful, this parameter is not returned.
        self.code = code
        # The code key that corresponds to the key in Medusa. If no code key is available, or if the content corresponding to the code key fails to be obtained or is empty, the returned message is displayed as the default information.
        self.code_key = code_key
        # The URL used to access the document.
        self.document_url = document_url
        # The returned dynamic contents that are separated by the && operator.
        self.dynamic_ctx = dynamic_ctx
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is not returned.
        self.message = message
        # The details of the report.
        self.report_over_view = report_over_view
        # The request ID.
        self.request_id = request_id
        # The dimensions of APIs.
        self.sampler_metrics_list = sampler_metrics_list
        # The dimensions of the whole scenario.
        self.scene_metrics = scene_metrics
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.report_over_view:
            self.report_over_view.validate()
        if self.sampler_metrics_list:
            for k in self.sampler_metrics_list:
                if k:
                    k.validate()
        if self.scene_metrics:
            self.scene_metrics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.code_key is not None:
            result['CodeKey'] = self.code_key
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.dynamic_ctx is not None:
            result['DynamicCtx'] = self.dynamic_ctx
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.report_over_view is not None:
            result['ReportOverView'] = self.report_over_view.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SamplerMetricsList'] = []
        if self.sampler_metrics_list is not None:
            for k in self.sampler_metrics_list:
                result['SamplerMetricsList'].append(k.to_map() if k else None)
        if self.scene_metrics is not None:
            result['SceneMetrics'] = self.scene_metrics.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeKey') is not None:
            self.code_key = m.get('CodeKey')
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('DynamicCtx') is not None:
            self.dynamic_ctx = m.get('DynamicCtx')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReportOverView') is not None:
            temp_model = GetJMeterReportDetailsResponseBodyReportOverView()
            self.report_over_view = temp_model.from_map(m['ReportOverView'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sampler_metrics_list = []
        if m.get('SamplerMetricsList') is not None:
            for k in m.get('SamplerMetricsList'):
                temp_model = GetJMeterReportDetailsResponseBodySamplerMetricsList()
                self.sampler_metrics_list.append(temp_model.from_map(k))
        if m.get('SceneMetrics') is not None:
            temp_model = GetJMeterReportDetailsResponseBodySceneMetrics()
            self.scene_metrics = temp_model.from_map(m['SceneMetrics'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJMeterReportDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJMeterReportDetailsResponseBody = None,
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
            temp_model = GetJMeterReportDetailsResponseBody()
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
        # The beginning of the time range to query.
        self.begin_time = begin_time
        # The end of the time range to query.
        self.end_time = end_time
        # The report ID.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The sampler ID. This parameter value starts from 0. If this parameter value is -1, the data of the whole scenario is returned.
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
        # The system status code.
        self.code = code
        # The returned message. If the request was successful, this parameter is left empty.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The metrics of the samplers.
        self.sample_metric_list = sample_metric_list
        # The sampler list. You can find the sampler to be queried based on this list.
        self.sampler_map = sampler_map
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: GetJMeterSampleMetricsResponseBody = None,
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
        # The ID of the load generator. This parameter is disabled.
        self.agent_id = agent_id
        # The beginning of the time range to query. Unit: milliseconds.
        self.begin_time = begin_time
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time
        # The keyword. You can use the keyword in the value of **SceneName** for fuzzy searching or use the value of **SceneID** for exact searching.
        self.keyword = keyword
        # The maximum response time. Unit: ms.
        self.max_rt = max_rt
        # The minimum response time. Unit: ms.
        self.min_rt = min_rt
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the report.
        # 
        # This parameter is required.
        self.report_id = report_id
        # The response code.
        self.response_code = response_code
        # The ID of the sampler. The value starts from 0.
        self.sampler_id = sampler_id
        # Specifies whether the sampling is successful.
        self.success = success
        # The name of the thread. Fuzzy searching is supported. If you specify multiple threads, separate the threads with spaces.
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
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of log entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The sampling results of the sampler.
        self.sample_results = sample_results
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of log entries.
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
        status_code: int = None,
        body: GetJMeterSamplingLogsResponseBody = None,
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
            temp_model = GetJMeterSamplingLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJMeterSceneRunningDataRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The scenario ID.
        # 
        # This parameter is required.
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
        error_message: str = None,
        has_error: bool = None,
        has_report: bool = None,
        hold_for: int = None,
        is_debugging: bool = None,
        report_id: str = None,
        sample_stat_list: List[Dict[str, Any]] = None,
        scene_id: str = None,
        scene_name: str = None,
        stage_name: str = None,
        start_time_ts: int = None,
        status: str = None,
        vum: int = None,
    ):
        # The number of stress testing engines.
        self.agent_count = agent_count
        # The stress testing engines.
        self.agent_id_list = agent_id_list
        # The sampling status of the scenario.
        self.all_sample_stat = all_sample_stat
        # The concurrency.
        self.concurrency = concurrency
        # The error message returned for the stress testing process. If the request was successful, this parameter is not returned.
        self.error_message = error_message
        # Indicates whether an error occurs in the stress testing process.
        self.has_error = has_error
        # Indicates whether the report is generated.
        self.has_report = has_report
        # The duration of the stress testing plan. Unit: seconds.
        self.hold_for = hold_for
        # Indicates whether a debugging is performed.
        self.is_debugging = is_debugging
        # The stress testing task ID. This ID also means the report ID.
        self.report_id = report_id
        # The status of samplers.
        self.sample_stat_list = sample_stat_list
        # The scenario ID.
        self.scene_id = scene_id
        # The scenario name.
        self.scene_name = scene_name
        # The current stage.
        self.stage_name = stage_name
        # The timestamp when the stress testing is scheduled to start. Unit: ms.
        self.start_time_ts = start_time_ts
        # The stress testing status of the scenario.
        self.status = status
        # The consumed Virtual User Minutes (VUM).
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
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.has_error is not None:
            result['HasError'] = self.has_error
        if self.has_report is not None:
            result['HasReport'] = self.has_report
        if self.hold_for is not None:
            result['HoldFor'] = self.hold_for
        if self.is_debugging is not None:
            result['IsDebugging'] = self.is_debugging
        if self.report_id is not None:
            result['ReportId'] = self.report_id
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HasError') is not None:
            self.has_error = m.get('HasError')
        if m.get('HasReport') is not None:
            self.has_report = m.get('HasReport')
        if m.get('HoldFor') is not None:
            self.hold_for = m.get('HoldFor')
        if m.get('IsDebugging') is not None:
            self.is_debugging = m.get('IsDebugging')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
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
        # The system status code. If the request was successful, this parameter is not returned.
        self.code = code
        # The URL that is used to access the document.
        self.document_url = document_url
        # The HTTP status code. If the request was successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is not returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The running data.
        self.running_data = running_data
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: GetJMeterSceneRunningDataResponseBody = None,
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
            temp_model = GetJMeterSceneRunningDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario.
        # 
        # This parameter is required.
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
        # The name of the creator.
        self.create_name = create_name
        # The name of the modifier.
        self.modify_name = modify_name
        # The type of the operation.
        self.operate_type = operate_type
        # The person who takes charge of the performance testing.
        self.principal = principal
        # The comment.
        self.remark = remark
        # The origin of the scenario.
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
        # Indicates whether the cache is cleared.
        self.clear_cache_each_iteration = clear_cache_each_iteration
        # The DNS servers
        self.dns_servers = dns_servers
        # The domain name and its bounded IP address.
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
        # The name of the file.
        self.file_name = file_name
        # The Object Storage Service (OSS) URL of the file.
        self.file_oss_address = file_oss_address
        # The size of the file. Unit: bytes.
        self.file_size = file_size
        # The type of the file.
        self.file_type = file_type
        # The ID of the file.
        self.id = id
        # The MD5 value of the JAR package.
        self.md_5 = md_5
        # Indicates whether the file is split.
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


class GetOpenJMeterSceneResponseBodySceneRegionalCondition(TeaModel):
    def __init__(
        self,
        amount: int = None,
        region: str = None,
    ):
        # The number of load generators.
        self.amount = amount
        # The ID of the region.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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
        max_rps: int = None,
        mode: str = None,
        pool: str = None,
        ramp_up: int = None,
        region_id: str = None,
        regional_condition: List[GetOpenJMeterSceneResponseBodySceneRegionalCondition] = None,
        scene_id: str = None,
        scene_name: str = None,
        security_group_id: str = None,
        start_concurrency: int = None,
        start_rps: int = None,
        steps: int = None,
        sync_timer_type: str = None,
        test_file: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The number of load generators. A load generator supports up to 500 concurrent virtual users.
        self.agent_count = agent_count
        # The basic information.
        self.base_info = base_info
        # The maximum number of concurrent virtual users.
        self.concurrency = concurrency
        # The type of the constant throughput timer.
        self.constant_throughput_timer_type = constant_throughput_timer_type
        # The DNS settings.
        self.dns_cache_config = dns_cache_config
        # The duration of the performance testing. Unit: seconds.
        self.duration = duration
        # The ID of the environment.
        self.environment_id = environment_id
        # The files.
        self.file_list = file_list
        # Indicates whether the load is from a virtual private cloud (VPC).
        self.is_vpc_test = is_vpc_test
        # The maximum RPS. This parameter is returned if you set Mode to tps_mode.
        self.max_rps = max_rps
        # The load application mode. Valid values: concurrency_mode and tps_mode.
        self.mode = mode
        # The origin of the load. "" indicates the Internet and intranet-vpc indicates the VPC.
        self.pool = pool
        # The period of time during which the load is gradually increased to the desired level. Unit: seconds.
        self.ramp_up = ramp_up
        # The region ID. This parameter is returned if the load is from a VPC.
        self.region_id = region_id
        # Customized load generator settings for regions
        self.regional_condition = regional_condition
        # The ID of the scenario.
        self.scene_id = scene_id
        # The name of the scenario.
        self.scene_name = scene_name
        # The ID of the security group. This parameter is returned if the load is from a VPC.
        self.security_group_id = security_group_id
        # The start number of concurrent virtual users.
        self.start_concurrency = start_concurrency
        # The start requests per second (RPS). This parameter is returned if you set Mode to tps_mode.
        self.start_rps = start_rps
        # The number of incremented users per step. If RampUp or Steps is not specified, the fixed load is used. If RampUp is specified but Steps is not specified, the load increases uniformly based on the value of RampUp. If RampUp and Steps are specified and Steps is less than RampUp, the load increases based on the value of Steps. You cannot specify Steps without specifying RampUp. If you do so, the fixed load is used.
        self.steps = steps
        # The type of the synchronization timer.
        self.sync_timer_type = sync_timer_type
        # The test file.
        self.test_file = test_file
        # The ID of the vSwitch. This parameter is returned if the load is from a VPC.
        self.v_switch_id = v_switch_id
        # The ID of the VPC. This parameter is returned if the load is from a VPC.
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
        if self.regional_condition:
            for k in self.regional_condition:
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
        if self.max_rps is not None:
            result['MaxRps'] = self.max_rps
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.pool is not None:
            result['Pool'] = self.pool
        if self.ramp_up is not None:
            result['RampUp'] = self.ramp_up
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RegionalCondition'] = []
        if self.regional_condition is not None:
            for k in self.regional_condition:
                result['RegionalCondition'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.start_concurrency is not None:
            result['StartConcurrency'] = self.start_concurrency
        if self.start_rps is not None:
            result['StartRps'] = self.start_rps
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
        if m.get('MaxRps') is not None:
            self.max_rps = m.get('MaxRps')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Pool') is not None:
            self.pool = m.get('Pool')
        if m.get('RampUp') is not None:
            self.ramp_up = m.get('RampUp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.regional_condition = []
        if m.get('RegionalCondition') is not None:
            for k in m.get('RegionalCondition'):
                temp_model = GetOpenJMeterSceneResponseBodySceneRegionalCondition()
                self.regional_condition.append(temp_model.from_map(k))
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StartConcurrency') is not None:
            self.start_concurrency = m.get('StartConcurrency')
        if m.get('StartRps') is not None:
            self.start_rps = m.get('StartRps')
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The information about the scenario.
        self.scene = scene
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: GetOpenJMeterSceneResponseBody = None,
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
            temp_model = GetOpenJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsDebugSampleLogsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        plan_id: str = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the debugging task.
        self.plan_id = plan_id

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
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class GetPtsDebugSampleLogsResponseBodySamplingLogs(TeaModel):
    def __init__(
        self,
        chain_id: str = None,
        chain_name: str = None,
        check_result: str = None,
        export_config: str = None,
        export_content: str = None,
        http_request_body: str = None,
        http_request_headers: str = None,
        http_request_method: str = None,
        http_request_url: str = None,
        http_response_body: str = None,
        http_response_fail_msg: str = None,
        http_response_headers: str = None,
        http_response_status: str = None,
        http_start_time: int = None,
        http_timing: str = None,
        import_content: str = None,
        node_id: str = None,
        rt: str = None,
        timestamp: int = None,
    ):
        # The ID of the session.
        self.chain_id = chain_id
        # The name of the session.
        self.chain_name = chain_name
        # The assertion check result.
        self.check_result = check_result
        # The parameter export configuration.
        self.export_config = export_config
        # The exported parameters.
        self.export_content = export_content
        # The body of the request.
        self.http_request_body = http_request_body
        # The request headers.
        self.http_request_headers = http_request_headers
        # The request method.
        self.http_request_method = http_request_method
        # The endpoint that specifies where the request is directed.
        self.http_request_url = http_request_url
        # The response body.
        self.http_response_body = http_response_body
        # The error message.
        self.http_response_fail_msg = http_response_fail_msg
        # The response headers.
        self.http_response_headers = http_response_headers
        # The HTTP status code.
        self.http_response_status = http_response_status
        # The time when the request was sent.
        self.http_start_time = http_start_time
        # The HTTP timing information in a waterfall format.
        self.http_timing = http_timing
        # The imported parameters.
        self.import_content = import_content
        # The ID of the node.
        self.node_id = node_id
        # The response time. Unit: ms.
        self.rt = rt
        # The timestamp. Unit: ms.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.chain_name is not None:
            result['ChainName'] = self.chain_name
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.export_config is not None:
            result['ExportConfig'] = self.export_config
        if self.export_content is not None:
            result['ExportContent'] = self.export_content
        if self.http_request_body is not None:
            result['HttpRequestBody'] = self.http_request_body
        if self.http_request_headers is not None:
            result['HttpRequestHeaders'] = self.http_request_headers
        if self.http_request_method is not None:
            result['HttpRequestMethod'] = self.http_request_method
        if self.http_request_url is not None:
            result['HttpRequestUrl'] = self.http_request_url
        if self.http_response_body is not None:
            result['HttpResponseBody'] = self.http_response_body
        if self.http_response_fail_msg is not None:
            result['HttpResponseFailMsg'] = self.http_response_fail_msg
        if self.http_response_headers is not None:
            result['HttpResponseHeaders'] = self.http_response_headers
        if self.http_response_status is not None:
            result['HttpResponseStatus'] = self.http_response_status
        if self.http_start_time is not None:
            result['HttpStartTime'] = self.http_start_time
        if self.http_timing is not None:
            result['HttpTiming'] = self.http_timing
        if self.import_content is not None:
            result['ImportContent'] = self.import_content
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('ChainName') is not None:
            self.chain_name = m.get('ChainName')
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('ExportConfig') is not None:
            self.export_config = m.get('ExportConfig')
        if m.get('ExportContent') is not None:
            self.export_content = m.get('ExportContent')
        if m.get('HttpRequestBody') is not None:
            self.http_request_body = m.get('HttpRequestBody')
        if m.get('HttpRequestHeaders') is not None:
            self.http_request_headers = m.get('HttpRequestHeaders')
        if m.get('HttpRequestMethod') is not None:
            self.http_request_method = m.get('HttpRequestMethod')
        if m.get('HttpRequestUrl') is not None:
            self.http_request_url = m.get('HttpRequestUrl')
        if m.get('HttpResponseBody') is not None:
            self.http_response_body = m.get('HttpResponseBody')
        if m.get('HttpResponseFailMsg') is not None:
            self.http_response_fail_msg = m.get('HttpResponseFailMsg')
        if m.get('HttpResponseHeaders') is not None:
            self.http_response_headers = m.get('HttpResponseHeaders')
        if m.get('HttpResponseStatus') is not None:
            self.http_response_status = m.get('HttpResponseStatus')
        if m.get('HttpStartTime') is not None:
            self.http_start_time = m.get('HttpStartTime')
        if m.get('HttpTiming') is not None:
            self.http_timing = m.get('HttpTiming')
        if m.get('ImportContent') is not None:
            self.import_content = m.get('ImportContent')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetPtsDebugSampleLogsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sampling_logs: List[GetPtsDebugSampleLogsResponseBodySamplingLogs] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The sampling logs.
        self.sampling_logs = sampling_logs
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.sampling_logs:
            for k in self.sampling_logs:
                if k:
                    k.validate()

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
        result['SamplingLogs'] = []
        if self.sampling_logs is not None:
            for k in self.sampling_logs:
                result['SamplingLogs'].append(k.to_map() if k else None)
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
        self.sampling_logs = []
        if m.get('SamplingLogs') is not None:
            for k in m.get('SamplingLogs'):
                temp_model = GetPtsDebugSampleLogsResponseBodySamplingLogs()
                self.sampling_logs.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetPtsDebugSampleLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPtsDebugSampleLogsResponseBody = None,
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
            temp_model = GetPtsDebugSampleLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsReportDetailsRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        scene_id: str = None,
    ):
        # The ID of the performance testing task. A task ID is generated each time a PTS scenario is started.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The ID of the scenario.
        # 
        # This parameter is required.
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
        # The total number of requests.
        self.all_count = all_count
        # The name of the API.
        self.api_name = api_name
        # The average response time. Unit: ms.
        self.avg_rt = avg_rt
        # The average TPS.
        self.avg_tps = avg_tps
        # The number of business-related failures. If a checkpoint is defined, a failure occurs when the conditions for the checkpoint are not satisfied.
        self.fail_count_biz = fail_count_biz
        # The number of failed requests.
        self.fail_count_req = fail_count_req
        # The maximum response time. Unit: ms.
        self.max_rt = max_rt
        # The minimum response time. Unit: ms.
        self.min_rt = min_rt
        # The 50th percentile response time.
        self.seg_50rt = seg_50rt
        # The 75th percentile response time.
        self.seg_75rt = seg_75rt
        # The 90th percentile response time.
        self.seg_90rt = seg_90rt
        # The 99th percentile response time.
        self.seg_99rt = seg_99rt
        # The business success rate. The value is the ratio of the number of successful business to the total number of business.
        self.success_rate_biz = success_rate_biz
        # The request success rate. The value is the ratio of the number of successful requests to the total number of requests.
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
        # The number of load generators. Each load generator has an IP address.
        self.agent_count = agent_count
        # The end time of the performance testing task.
        self.end_time = end_time
        # The ID of the report.
        self.report_id = report_id
        # The name of the report.
        self.report_name = report_name
        # The start time of the performance testing task.
        self.start_time = start_time
        # The virtual user minutes (VUM).
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
        # The number of requests in the scenario.
        self.all_count = all_count
        # The average response time in the scenario.
        self.avg_rt = avg_rt
        # The average transactions per second (TPS) in the scenario.
        self.avg_tps = avg_tps
        # The number of business failures in the scenario.
        self.fail_count_biz = fail_count_biz
        # The number of failed requests in the scenario.
        self.fail_count_req = fail_count_req
        # The 90th percentile response time.
        self.seg_90rt = seg_90rt
        # The 99th percentile response time.
        self.seg_99rt = seg_99rt
        # The business success rate in the scenario.
        self.success_rate_biz = success_rate_biz
        # The request success rate in the scenario.
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
        # The domain name.
        self.domain = domain
        # The IP addresses bound to the domain name.
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
        # The timeout period of the scenario.
        self.connection_timeout_in_second = connection_timeout_in_second
        # The domain name-IP address binding relationships.
        self.domain_binding_list = domain_binding_list
        # The log sampling rate.
        self.log_rate = log_rate
        # The custom success code.
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
        # The name of the file.
        self.file_name = file_name
        # The Object Storage Service (OSS) URL of the file.
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
        # The name of the parameter.
        self.param_name = param_name
        # The value of the parameter.
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
        # The starting requests per second (RPS).
        self.rps_begin = rps_begin
        # The maximum RPS.
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
        # The starting number of concurrent virtual users in the scenario.
        self.all_concurrency_begin = all_concurrency_begin
        # The maximum number of concurrent virtual users in the scenario.
        self.all_concurrency_limit = all_concurrency_limit
        # The starting RPS in the scenario.
        self.all_rps_begin = all_rps_begin
        # The maximum RPS in the scenario.
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
        # The starting number of concurrent virtual users.
        self.concurrency_begin = concurrency_begin
        # The maximum number of concurrent virtual users.
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
        # The number of load generators.
        self.agent_count = agent_count
        # The API request load settings.
        self.api_load_config_list = api_load_config_list
        # The concurrency and RPS limits in the scenario.
        self.configuration = configuration
        # The maximum running time. Unit: minutes.
        self.max_running_time = max_running_time
        # The settings of the session.
        self.relation_load_config_list = relation_load_config_list
        # The load application mode.
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
        # The content of the request body.
        self.body_value = body_value
        # The type of the request body.
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
        # The checked item.
        self.check_point = check_point
        # The check type.
        self.check_type = check_type
        # The expected value.
        self.expect_value = expect_value
        # The check operator.
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
        # The index of the export parameter.
        self.count = count
        # The name of the export parameter.
        self.export_name = export_name
        # The source of the export parameter.
        self.export_type = export_type
        # The actual path from which you want to extract the export parameter values.
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
        # The name of the header.
        self.header_name = header_name
        # The value of the header.
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
        # The ID of the API operation.
        self.api_id = api_id
        # The name of the API operation.
        self.api_name = api_name
        # The request body.
        self.body = body
        # The checkpoints of the API operation.
        self.check_point_list = check_point_list
        # The export parameters.
        self.export_list = export_list
        # The headers.
        self.header_list = header_list
        # The method of the request.
        self.method = method
        # The number of redirections.
        self.redirect_count_limit = redirect_count_limit
        # The timeout period.
        self.timeout_in_second = timeout_in_second
        # The URL to which the API request is sent.
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
        # Indicates whether the file is used as the baseline file.
        self.base_file = base_file
        # Indicates whether the parameters are used once.
        self.cycle_once = cycle_once
        # The name of the file.
        self.file_name = file_name
        # The parameters in the file.
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
        # The settings of the API operation.
        self.api_list = api_list
        # The file parameters used by the session.
        self.file_parameter_explain_list = file_parameter_explain_list
        # The ID of the session.
        self.relation_id = relation_id
        # The name of the session.
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
        # The advanced settings of the scenario.
        self.advance_setting = advance_setting
        # The time when the scenario was created.
        self.create_time = create_time
        # The file used in the scenario.
        self.file_parameter_list = file_parameter_list
        # The global parameters.
        self.global_parameter_list = global_parameter_list
        # The load settings.
        self.load_config = load_config
        # The last modification time of the scenario.
        self.modified_time = modified_time
        # The sessions.
        self.relation_list = relation_list
        # The ID of the scenario.
        self.scene_id = scene_id
        # The name of the scenario.
        self.scene_name = scene_name
        # The status of the scenario.
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
        # The metrics for API operations in the PTS scenario
        self.api_metrics_list = api_metrics_list
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The summary of the report.
        self.report_over_view = report_over_view
        # The ID of the request.
        self.request_id = request_id
        # The metrics of the scenario.
        self.scene_metrics = scene_metrics
        # The snapshot of the scenario.
        self.scene_snap_shot = scene_snap_shot
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: GetPtsReportDetailsResponseBody = None,
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
        # The number of the page to display in the paging operation.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of reports to display per page. Valid values: 5 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The scenario ID.
        # 
        # This parameter is required.
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
        # The number of stress testers.
        self.agent_count = agent_count
        # The end time of the stress testing.
        self.end_time = end_time
        # The report ID.
        self.report_id = report_id
        # The title of the report.
        self.report_name = report_name
        # The start time of the stress testing.
        self.start_time = start_time
        # The consumed Virtual User Minutes (VUM).
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is left empty.
        self.message = message
        # The reports.
        self.report_over_view_list = report_over_view_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: GetPtsReportsBySceneIdResponseBody = None,
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
            temp_model = GetPtsReportsBySceneIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario.
        # 
        # This parameter is required.
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
        # The domain name.
        self.domain = domain
        # The IPs bound to the domain name.
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
        # The timeout period of the scenario. Unit: seconds.
        self.connection_timeout_in_second = connection_timeout_in_second
        # The IP-domain name bindings.
        self.domain_binding_list = domain_binding_list
        # The log sampling rate.
        self.log_rate = log_rate
        # The custom success code.
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
        # The file name.
        self.file_name = file_name
        # The OSS address of the file. Make sure that the address is accessible from the Internet.
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
        # The name of the parameter.
        self.param_name = param_name
        # The value of the parameter.
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


class GetPtsSceneResponseBodySceneHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the header.
        self.name = name
        # The value of the header.
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


class GetPtsSceneResponseBodySceneLoadConfigApiLoadConfigList(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        rps_begin: int = None,
        rps_limit: int = None,
    ):
        # The API ID. You can track an API by its ID in sessions.
        self.api_id = api_id
        # The starting requests per second (RPS).
        self.rps_begin = rps_begin
        # The maximum RPS.
        self.rps_limit = rps_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.rps_begin is not None:
            result['RpsBegin'] = self.rps_begin
        if self.rps_limit is not None:
            result['RpsLimit'] = self.rps_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
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
        # The starting number of concurrent sessions.
        self.all_concurrency_begin = all_concurrency_begin
        # The maximum number of concurrent sessions.
        self.all_concurrency_limit = all_concurrency_limit
        # The starting RPS.
        self.all_rps_begin = all_rps_begin
        # The maximum RPS.
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
        relation_id: str = None,
    ):
        # The starting number of concurrent sessions.
        self.concurrency_begin = concurrency_begin
        # The maximum number of concurrent sessions.
        self.concurrency_limit = concurrency_limit
        # The session ID.
        self.relation_id = relation_id

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
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyBegin') is not None:
            self.concurrency_begin = m.get('ConcurrencyBegin')
        if m.get('ConcurrencyLimit') is not None:
            self.concurrency_limit = m.get('ConcurrencyLimit')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        return self


class GetPtsSceneResponseBodySceneLoadConfigVpcLoadConfig(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetPtsSceneResponseBodySceneLoadConfig(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        api_load_config_list: List[GetPtsSceneResponseBodySceneLoadConfigApiLoadConfigList] = None,
        auto_step: bool = None,
        configuration: GetPtsSceneResponseBodySceneLoadConfigConfiguration = None,
        increment: int = None,
        keep_time: int = None,
        max_running_time: int = None,
        relation_load_config_list: List[GetPtsSceneResponseBodySceneLoadConfigRelationLoadConfigList] = None,
        test_mode: str = None,
        vpc_load_config: GetPtsSceneResponseBodySceneLoadConfigVpcLoadConfig = None,
    ):
        # The number of load generators.
        self.agent_count = agent_count
        # The API request load settings.
        self.api_load_config_list = api_load_config_list
        # Indicates whether the load is automatically incremented.
        self.auto_step = auto_step
        # The concurrency and RPS settings of the scenario.
        self.configuration = configuration
        # The increment percentage. The valid values are 10 to 100, in increments of 10. This parameter is returned only if you set testMode to concurrency_mode and set autoStep to true.
        self.increment = increment
        # The duration during which a specific load level is applied. The duration is less than the value of maxRunningTime. Unit: minutes.
        self.keep_time = keep_time
        # The maximum duration of load application. Unit: minutes.
        self.max_running_time = max_running_time
        # The session load settings.
        self.relation_load_config_list = relation_load_config_list
        # The load application mode. Transactions per second (TPS) indicates the RPS mode.
        # 
        # >  The load application mode is CONCURRENCY/TPS.
        self.test_mode = test_mode
        # The virtual private cloud (VPC) settings. This information is returned only if you set the testing mode to VPC.
        self.vpc_load_config = vpc_load_config

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
        if self.vpc_load_config:
            self.vpc_load_config.validate()

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
        if self.auto_step is not None:
            result['AutoStep'] = self.auto_step
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.increment is not None:
            result['Increment'] = self.increment
        if self.keep_time is not None:
            result['KeepTime'] = self.keep_time
        if self.max_running_time is not None:
            result['MaxRunningTime'] = self.max_running_time
        result['RelationLoadConfigList'] = []
        if self.relation_load_config_list is not None:
            for k in self.relation_load_config_list:
                result['RelationLoadConfigList'].append(k.to_map() if k else None)
        if self.test_mode is not None:
            result['TestMode'] = self.test_mode
        if self.vpc_load_config is not None:
            result['VpcLoadConfig'] = self.vpc_load_config.to_map()
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
        if m.get('AutoStep') is not None:
            self.auto_step = m.get('AutoStep')
        if m.get('Configuration') is not None:
            temp_model = GetPtsSceneResponseBodySceneLoadConfigConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('Increment') is not None:
            self.increment = m.get('Increment')
        if m.get('KeepTime') is not None:
            self.keep_time = m.get('KeepTime')
        if m.get('MaxRunningTime') is not None:
            self.max_running_time = m.get('MaxRunningTime')
        self.relation_load_config_list = []
        if m.get('RelationLoadConfigList') is not None:
            for k in m.get('RelationLoadConfigList'):
                temp_model = GetPtsSceneResponseBodySceneLoadConfigRelationLoadConfigList()
                self.relation_load_config_list.append(temp_model.from_map(k))
        if m.get('TestMode') is not None:
            self.test_mode = m.get('TestMode')
        if m.get('VpcLoadConfig') is not None:
            temp_model = GetPtsSceneResponseBodySceneLoadConfigVpcLoadConfig()
            self.vpc_load_config = temp_model.from_map(m['VpcLoadConfig'])
        return self


class GetPtsSceneResponseBodySceneRelationListApiListBody(TeaModel):
    def __init__(
        self,
        body_value: str = None,
        content_type: str = None,
    ):
        # The body value.
        self.body_value = body_value
        # The body type.
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
        # The checked parameter.
        self.check_point = check_point
        # The check type.
        self.check_type = check_type
        # The expected value.
        self.expect_value = expect_value
        # The check operator.
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
        # The number of items or entries related to the export operation.
        self.count = count
        # The path where the exported value can be found.
        self.export_name = export_name
        # The format in which data is exported.
        self.export_type = export_type
        # The parameter that is exported.
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
        # The header name.
        self.header_name = header_name
        # The header value.
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
        # The API ID. You can track an API by its ID in sessions.
        self.api_id = api_id
        # The API name.
        self.api_name = api_name
        # The request body.
        self.body = body
        # The checkpoints.
        self.check_point_list = check_point_list
        # The exported parameters.
        self.export_list = export_list
        # The headers used in the API request.
        self.header_list = header_list
        # The request method.
        self.method = method
        # The number of redirections.
        self.redirect_count_limit = redirect_count_limit
        # The timeout period. Unit: seconds.
        self.timeout_in_second = timeout_in_second
        # The URL to which the request is sent.
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
        # Indicates whether the file serves as the primary dataset for the test.
        self.base_file = base_file
        # Indicates whether the parameters are used for a single test execution.
        self.cycle_once = cycle_once
        # The file name.
        self.file_name = file_name
        # The parameter names in the file.
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
        # The APIs.
        self.api_list = api_list
        # The file parameters.
        self.file_parameter_explain_list = file_parameter_explain_list
        # The session ID.
        self.relation_id = relation_id
        # The session name.
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
        headers: List[GetPtsSceneResponseBodySceneHeaders] = None,
        load_config: GetPtsSceneResponseBodySceneLoadConfig = None,
        modified_time: str = None,
        relation_list: List[GetPtsSceneResponseBodySceneRelationList] = None,
        scene_id: str = None,
        scene_name: str = None,
        status: str = None,
    ):
        # The advanced settings.
        self.advance_setting = advance_setting
        # The creation time of the scenario.
        self.create_time = create_time
        # The file parameters.
        self.file_parameter_list = file_parameter_list
        # Global parameters
        self.global_parameter_list = global_parameter_list
        # The global headers for the scenario.
        self.headers = headers
        # The load settings.
        self.load_config = load_config
        # The last modification time of the scenario.
        self.modified_time = modified_time
        # The sessions.
        self.relation_list = relation_list
        # The ID of the scenario.
        self.scene_id = scene_id
        # The name of the scenario
        self.scene_name = scene_name
        # The status of the scenario.
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
        if self.headers:
            for k in self.headers:
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
        result['Headers'] = []
        if self.headers is not None:
            for k in self.headers:
                result['Headers'].append(k.to_map() if k else None)
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
        self.headers = []
        if m.get('Headers') is not None:
            for k in m.get('Headers'):
                temp_model = GetPtsSceneResponseBodySceneHeaders()
                self.headers.append(temp_model.from_map(k))
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, N/A is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The structure of the scenario.
        self.scene = scene
        # Indicates whether the operation is successful.
        # 
        # *   `true`
        # *   `false`
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
        status_code: int = None,
        body: GetPtsSceneResponseBody = None,
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
            temp_model = GetPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsSceneBaseLineRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scene. For more information, see the [table](https://help.aliyun.com/document_detail/201321.html) provided in this topic.
        # 
        # This parameter is required.
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
        # Average RT
        self.avg_rt = avg_rt
        # null
        self.avg_tps = avg_tps
        # null
        self.fail_count_biz = fail_count_biz
        # Failures
        self.fail_count_req = fail_count_req
        # The API ID.
        self.id = id
        # null
        self.max_rt = max_rt
        # null
        self.min_rt = min_rt
        # The name of the API operation.
        self.name = name
        # null
        self.seg_90rt = seg_90rt
        # null
        self.seg_99rt = seg_99rt
        # null
        self.success_rate_biz = success_rate_biz
        # request success rate
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
        # Average RT
        self.avg_rt = avg_rt
        # null
        self.avg_tps = avg_tps
        # null
        self.fail_count_biz = fail_count_biz
        # Failures
        self.fail_count_req = fail_count_req
        # null
        self.seg_90rt = seg_90rt
        # null
        self.seg_99rt = seg_99rt
        # null
        self.success_rate_biz = success_rate_biz
        # request success rate
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
        # null
        self.api_baselines = api_baselines
        # Scenario
        self.name = name
        # null
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
        # Baseline data
        self.baseline = baseline
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # null
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The ID of the scene.
        self.scene_id = scene_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false:
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
        status_code: int = None,
        body: GetPtsSceneBaseLineResponseBody = None,
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
            temp_model = GetPtsSceneBaseLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsSceneRunningDataRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        scene_id: str = None,
    ):
        # The ID of the stress testing task. You can obtain the task ID by calling the StartPtsScene operation.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The scenario ID.
        # 
        # This parameter is required.
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
        # The number of stress testers.
        self.count = count
        # The provider of the stress tester.
        self.isp = isp
        # The province in which the stress tester resides.
        self.province = province
        # The region in which the stress tester resides.
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
        # The number of failed businesses.
        self.failed_business_count = failed_business_count
        # The RPS of failed businesses.
        self.failed_business_qps = failed_business_qps
        # The number of successful businesses.
        self.succeed_business_count = succeed_business_count
        # The RPS of the successful businesses.
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
        # The API ID.
        self.api_id = api_id
        # The API name.
        self.api_name = api_name
        # The average RT.
        self.average_rt = average_rt
        # The check point results.
        self.check_point_result = check_point_result
        # The concurrency.
        self.concurrency = concurrency
        # The RPS of successful and failed requests.
        self.config_qps = config_qps
        # The number of successful requests.
        self.count_2xx = count_2xx
        # The total number of failed requests.
        self.failed_count = failed_count
        # The RPS of failed requests.
        self.failed_qps = failed_qps
        # The maximum RT.
        self.max_rt = max_rt
        # The minimum RT.
        self.min_rt = min_rt
        # The API ID.
        self.node_id = node_id
        # The Requests Per Second (RPS) of successful requests.
        self.qps_2xx = qps_2xx
        # The actual RPS.
        self.real_qps = real_qps
        # The point in time at which the stress testing is performed.
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
        total_real_qps: int = None,
        total_request_count: int = None,
        tps_limit: int = None,
        vum: int = None,
    ):
        # The location information of stress testers.
        self.agent_location = agent_location
        # The number of healthy engines.
        self.alive_agents = alive_agents
        # The average RT.
        self.average_rt = average_rt
        # The start time of the stress testing that is displayed as a timestamp. Unit: ms.
        self.begin_time = begin_time
        # The stress testing details of the GetPtsSceneRunningData operation.
        self.chain_monitor_data_list = chain_monitor_data_list
        # The system status code. If the request was successful, this parameter is not returned.
        self.code = code
        # The total concurrency.
        self.concurrency = concurrency
        # The maximum concurrency.
        self.concurrency_limit = concurrency_limit
        # The total number of failed businesses.
        self.failed_business_count = failed_business_count
        # The number of failed requests.
        self.failed_request_count = failed_request_count
        # Indicates whether a report is generated.
        self.has_report = has_report
        # The HTTP status code. If the request was successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is not returned.
        self.message = message
        # The size of the request body.
        self.request_bps = request_bps
        # The request ID.
        self.request_id = request_id
        # The size of the response body.
        self.response_bps = response_bps
        # The 90th percentile of reaction time (RT).
        self.seg_90rt = seg_90rt
        # The scenario status. The default parameter value is 7.
        self.status = status
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of stress testers.
        self.total_agents = total_agents
        # The total number of queries per second (QPS).
        self.total_real_qps = total_real_qps
        # The total number of requests.
        self.total_request_count = total_request_count
        # The maximum transactions per second (TPS).
        self.tps_limit = tps_limit
        # The consumed Virtual User Minutes (VUM).
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
        if self.total_real_qps is not None:
            result['TotalRealQps'] = self.total_real_qps
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
        if m.get('TotalRealQps') is not None:
            self.total_real_qps = m.get('TotalRealQps')
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
        status_code: int = None,
        body: GetPtsSceneRunningDataResponseBody = None,
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
            temp_model = GetPtsSceneRunningDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPtsSceneRunningStatusRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario.
        # 
        # This parameter is required.
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
        # The system status code. If the operation is successful, this parameter is not returned
        self.code = code
        # The time when the scenario was created.
        self.create_time = create_time
        # The request status code. If the operation is successful, this parameter is not returned
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The last modification time of the scenario.
        self.modified_time = modified_time
        # The ID of the request.
        self.request_id = request_id
        # The name of the scenario.
        self.scene_name = scene_name
        # The status of the scenario. Valid values:
        # 
        # *   CREATED
        # *   SYNCING
        # *   SYNC_DONE
        # *   UPLOADING
        # *   UPLOADED
        # *   PREPARING
        # *   READY
        # *   RUNNING
        # *   STOPPING
        # *   STOPPED
        self.status = status
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: GetPtsSceneRunningStatusResponseBody = None,
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
            temp_model = GetPtsSceneRunningStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserVpcSecurityGroupRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetUserVpcSecurityGroupResponseBodySecurityGroupList(TeaModel):
    def __init__(
        self,
        description: str = None,
        security_group_id: str = None,
        security_group_name: str = None,
        vpc_id: str = None,
    ):
        # The description of the security group.
        self.description = description
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The name of the security group.
        self.security_group_name = security_group_name
        # The ID of the VPC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetUserVpcSecurityGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        security_group_count: int = None,
        security_group_list: List[GetUserVpcSecurityGroupResponseBodySecurityGroupList] = None,
        success: bool = None,
    ):
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of security groups.
        self.security_group_count = security_group_count
        # The security groups.
        self.security_group_list = security_group_list
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.security_group_list:
            for k in self.security_group_list:
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
        if self.security_group_count is not None:
            result['SecurityGroupCount'] = self.security_group_count
        result['SecurityGroupList'] = []
        if self.security_group_list is not None:
            for k in self.security_group_list:
                result['SecurityGroupList'].append(k.to_map() if k else None)
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupCount') is not None:
            self.security_group_count = m.get('SecurityGroupCount')
        self.security_group_list = []
        if m.get('SecurityGroupList') is not None:
            for k in m.get('SecurityGroupList'):
                temp_model = GetUserVpcSecurityGroupResponseBodySecurityGroupList()
                self.security_group_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserVpcSecurityGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserVpcSecurityGroupResponseBody = None,
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
            temp_model = GetUserVpcSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserVpcVSwitchRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetUserVpcVSwitchResponseBodyVSwitchList(TeaModel):
    def __init__(
        self,
        available_ip_address_count: int = None,
        max_agent_count: int = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
        vpc_id: str = None,
    ):
        # The number of available IP addresses in the vSwitch.
        self.available_ip_address_count = available_ip_address_count
        # The maximum number of stress testers to be added.
        self.max_agent_count = max_agent_count
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The vSwitch name.
        self.v_switch_name = v_switch_name
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count
        if self.max_agent_count is not None:
            result['MaxAgentCount'] = self.max_agent_count
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')
        if m.get('MaxAgentCount') is not None:
            self.max_agent_count = m.get('MaxAgentCount')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetUserVpcVSwitchResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        v_switch_count: int = None,
        v_switch_list: List[GetUserVpcVSwitchResponseBodyVSwitchList] = None,
    ):
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is left empty.
        self.message = message
        # The number of the returned page.
        self.page_number = page_number
        # The number of returned entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The number of vSwitches.
        self.v_switch_count = v_switch_count
        # The vSwitches.
        self.v_switch_list = v_switch_list

    def validate(self):
        if self.v_switch_list:
            for k in self.v_switch_list:
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
        if self.v_switch_count is not None:
            result['VSwitchCount'] = self.v_switch_count
        result['VSwitchList'] = []
        if self.v_switch_list is not None:
            for k in self.v_switch_list:
                result['VSwitchList'].append(k.to_map() if k else None)
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
        if m.get('VSwitchCount') is not None:
            self.v_switch_count = m.get('VSwitchCount')
        self.v_switch_list = []
        if m.get('VSwitchList') is not None:
            for k in m.get('VSwitchList'):
                temp_model = GetUserVpcVSwitchResponseBodyVSwitchList()
                self.v_switch_list.append(temp_model.from_map(k))
        return self


class GetUserVpcVSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserVpcVSwitchResponseBody = None,
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
            temp_model = GetUserVpcVSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserVpcsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetUserVpcsResponseBodyVpcs(TeaModel):
    def __init__(
        self,
        cidr_block: str = None,
        description: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        router_table_ids: List[str] = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The IPv4 CIDR block of the VPC.
        self.cidr_block = cidr_block
        # The description of the VPC.
        self.description = description
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group to which the VPC belongs.
        self.resource_group_id = resource_group_id
        # The IDs of the route tables.
        self.router_table_ids = router_table_ids
        # The vSwitches.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.router_table_ids is not None:
            result['RouterTableIds'] = self.router_table_ids
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RouterTableIds') is not None:
            self.router_table_ids = m.get('RouterTableIds')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class GetUserVpcsResponseBody(TeaModel):
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
        vpcs: List[GetUserVpcsResponseBodyVpcs] = None,
    ):
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count
        # The VPCs.
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            for k in self.vpcs:
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
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
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
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = GetUserVpcsResponseBodyVpcs()
                self.vpcs.append(temp_model.from_map(k))
        return self


class GetUserVpcsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserVpcsResponseBody = None,
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
            temp_model = GetUserVpcsResponseBody()
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
        # The ID of the environment. If you specify this parameter, the operation returns the information about the environment identified by the ID.
        self.env_id = env_id
        # The keyword of the environment name. If you specify this parameter, the operation returns the information about the environments whose names contain the keyword.
        self.env_name = env_name
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of environments per page.
        # 
        # This parameter is required.
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
        # The ID of the file.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The OSS address of the file.
        self.file_oss_address = file_oss_address
        # The size of the file. Unit: bytes.
        self.file_size = file_size
        # The MD5 checksum of the file.
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
        # The description of the attribute.
        self.description = description
        # The name of the attribute.
        self.name = name
        # The value of the attribute.
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
        # The time when the environment was created.
        self.create_time = create_time
        # The ID of the environment.
        self.env_id = env_id
        # The name of the environment.
        self.env_name = env_name
        # The JMeter version of the environment.
        self.env_version = env_version
        # The JAR files.
        self.files = files
        # The time when the environment was last modified.
        self.modified_time = modified_time
        # The JMeter attributes.
        self.properties = properties
        # The scenarios related to the environment.
        self.related_scenes = related_scenes
        # The IDs of the scenarios that run in the environment.
        self.running_scenes = running_scenes
        # The total size of the environment file.
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
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The environments.
        self.envs = envs
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of environments per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of environments.
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
        status_code: int = None,
        body: ListEnvsResponseBody = None,
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
        # The beginning of the time range to query. Unit: ms.
        self.begin_time = begin_time
        # The end of the time range to query.
        self.end_time = end_time
        # The report keyword.
        self.keyword = keyword
        # The number of the report page to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of reports to return.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The report ID.
        self.report_id = report_id
        # The ID of the scenario whose report you want to view.
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
        # The start time of the stress testing.
        self.actual_start_time = actual_start_time
        # The stress testing duration.
        self.duration = duration
        # The report ID.
        self.report_id = report_id
        # The report name.
        self.report_name = report_name
        # The consumed Virtual User Minutes (VUM).
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is left empty.
        self.message = message
        # The number of the returned report page.
        self.page_number = page_number
        # The number of returned reports.
        self.page_size = page_size
        # The reports.
        self.reports = reports
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of reports returned based on the condition.
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
        status_code: int = None,
        body: ListJMeterReportsResponseBody = None,
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
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of scenarios to return.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The scenario ID.
        self.scene_id = scene_id
        # The scenario name.
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
        status: str = None,
    ):
        # The stress testing duration.
        self.duration_str = duration_str
        # The scenario ID.
        self.scene_id = scene_id
        # The scenario name.
        self.scene_name = scene_name
        # The status of the scenario. Valid values:
        # 
        # *   PREPARING: The scenario is being prepared.
        # *   PREPARED: The scenario has been prepared.
        # *   STARTING: The scenario is starting.
        # *   RUNNING: The scenario is running.
        # *   STOPPING: The scenario is being stopped.
        # *   STOPPED: The scenario waits for startup
        self.status = status

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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationStr') is not None:
            self.duration_str = m.get('DurationStr')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
        # The system status code. If the request was successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the request was successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The scenarios.
        self.jmeter_scene = jmeter_scene
        # The returned message. If the request was successful, this parameter is left empty.
        self.message = message
        # The number of the returned page.
        self.page_number = page_number
        # The number of returned scenarios.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of returned scenarios.
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
        status_code: int = None,
        body: ListOpenJMeterScenesResponseBody = None,
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
            temp_model = ListOpenJMeterScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPtsReportsRequest(TeaModel):
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
        # The timestamp when the stress testing starts. Unit: ms.
        self.begin_time = begin_time
        # The timestamp when the stress testing ends. Unit: ms.
        self.end_time = end_time
        # The report keyword.
        self.keyword = keyword
        # The number of the page to return. The page number starts from 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of reports to return per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The report ID.
        self.report_id = report_id
        # The ID of the scenario whose report you want to view.
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


class ListPtsReportsResponseBodyReports(TeaModel):
    def __init__(
        self,
        actual_start_time: int = None,
        duration: str = None,
        report_id: str = None,
        report_name: str = None,
        vum: int = None,
    ):
        # The timestamp when the stress testing starts. Unit: ms.
        self.actual_start_time = actual_start_time
        # The stress testing duration.
        self.duration = duration
        # The report ID.
        self.report_id = report_id
        # The report name.
        self.report_name = report_name
        # The consumed Virtual User Minutes (VUM).
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


class ListPtsReportsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        reports: List[ListPtsReportsResponseBodyReports] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, an empty string is returned.
        self.message = message
        # The number of the returned page. The page number starts from 1.
        self.page_number = page_number
        # The number of reports returned per page.
        self.page_size = page_size
        # The reports.
        self.reports = reports
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true false
        self.success = success
        # The total number of reports returned based on the condition.
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
                temp_model = ListPtsReportsResponseBodyReports()
                self.reports.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPtsReportsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPtsReportsResponseBody = None,
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
            temp_model = ListPtsReportsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPtsSceneRequest(TeaModel):
    def __init__(
        self,
        key_word: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The keyword based on which you can search for the PTS scenario. You can perform a fuzzy search on the scenario name (**SceneName**) or an exact search on the scenario ID (**SceneId**).
        self.key_word = key_word
        # The number of the page to return. Valid values: 1 to 1073741824.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of scenario entries to return per page. Valid values: 10 to 1000.
        # 
        # This parameter is required.
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
        status: str = None,
    ):
        # The time when the PTS scenario was created.
        self.create_time = create_time
        # The scenario ID.
        self.scene_id = scene_id
        # The scenario name.
        self.scene_name = scene_name
        # The status of the PTS scenario. Valid values:
        self.status = status

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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
        # The system status code. If the request was successful, no data is returned.
        self.code = code
        # The HTTP status code. If the request was successful, no data is returned.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, no data is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned scenarios.
        self.scene_view_list = scene_view_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: ListPtsSceneResponseBody = None,
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
            temp_model = ListPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcConfigsRequest(TeaModel):
    def __init__(
        self,
        config_id: str = None,
        config_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        self.config_id = config_id
        self.config_name = config_name
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.region_id = region_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcConfigsResponseBodyVpcConfigList(TeaModel):
    def __init__(
        self,
        config_description: str = None,
        config_id: str = None,
        config_name: str = None,
        region_id: str = None,
        security_group_id: str = None,
        sort_priority: int = None,
        v_switch_id: str = None,
        vpc_cidr: str = None,
        vpc_id: str = None,
    ):
        self.config_description = config_description
        self.config_id = config_id
        self.config_name = config_name
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.sort_priority = sort_priority
        self.v_switch_id = v_switch_id
        self.vpc_cidr = vpc_cidr
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_id is not None:
            result['ConfigId'] = self.config_id
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.sort_priority is not None:
            result['SortPriority'] = self.sort_priority
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_cidr is not None:
            result['VpcCidr'] = self.vpc_cidr
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SortPriority') is not None:
            self.sort_priority = m.get('SortPriority')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcCidr') is not None:
            self.vpc_cidr = m.get('VpcCidr')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcConfigsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpc_config_list: List[ListVpcConfigsResponseBodyVpcConfigList] = None,
    ):
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vpc_config_list = vpc_config_list

    def validate(self):
        if self.vpc_config_list:
            for k in self.vpc_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VpcConfigList'] = []
        if self.vpc_config_list is not None:
            for k in self.vpc_config_list:
                result['VpcConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpc_config_list = []
        if m.get('VpcConfigList') is not None:
            for k in m.get('VpcConfigList'):
                temp_model = ListVpcConfigsResponseBodyVpcConfigList()
                self.vpc_config_list.append(temp_model.from_map(k))
        return self


class ListVpcConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVpcConfigsResponseBody = None,
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
            temp_model = ListVpcConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene: str = None,
    ):
        # null
        # 
        # This parameter is required.
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
        # The system status code.
        self.code = code
        # The HTTP status code that is returned.
        self.http_status_code = http_status_code
        # null
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false:
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
        status_code: int = None,
        body: ModifyPtsSceneResponseBody = None,
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
            temp_model = ModifyPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveEnvRequest(TeaModel):
    def __init__(
        self,
        env_id: str = None,
    ):
        # The ID of the environment that you want to delete.
        # 
        # This parameter is required.
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
        # The system status code. If the request was successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the request was successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is not returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: RemoveEnvResponseBody = None,
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
            temp_model = RemoveEnvResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveOpenJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario that you want to remove.
        # 
        # This parameter is required.
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
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: RemoveOpenJMeterSceneResponseBody = None,
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
            temp_model = RemoveOpenJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveEnvRequestEnvFiles(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_oss_address: str = None,
    ):
        # The name of the file. Make sure that the file name is the same as the file name in the value of **FileOssAddress**.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The Object Storage Service (OSS) URL of the file. Make sure that the file is accessible from the Internet.
        # 
        # >  Only OSS URLs in the China (Shanghai) region are supported.
        # 
        # This parameter is required.
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
        # The description of the attribute.
        self.description = description
        # The name of the attribute.
        self.name = name
        # The value of the attribute.
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
        # The ID of the JMeter environment. To create a JMeter environment, leave this parameter empty. To update a JMeter environment, specify the ID of the environment.
        self.env_id = env_id
        # The name of the environment.
        # 
        # This parameter is required.
        self.env_name = env_name
        # The files on which the environment depends.
        # 
        # This parameter is required.
        self.files = files
        # The extension label.
        self.jmeter_plugin_label = jmeter_plugin_label
        # The JMeter attributes.
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
        # The JMeter environment.
        # 
        # This parameter is required.
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
        # The JMeter environment.
        # 
        # This parameter is required.
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
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The ID of the environment.
        self.env_id = env_id
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: SaveEnvResponseBody = None,
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
        # Specifies whether to clear the cache in each iteration.
        self.clear_cache_each_iteration = clear_cache_each_iteration
        # The DNS servers.
        self.dns_servers = dns_servers
        # The table that contains bound domain names.
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
        # The file ID.
        self.file_id = file_id
        # The name of the test file.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The Object Storage Service (OSS) path that is used to access the test file over the Internet.
        # 
        # >  Only test files in the China (Shanghai) region can be accessed.
        # 
        # This parameter is required.
        self.file_oss_address = file_oss_address
        # The file size. The total file size cannot exceed 500 MB. Unit: bytes.
        self.file_size = file_size
        # The MD5 hash of the test file.
        self.md_5 = md_5
        # Specifies whether to split the test file. This parameter is valid only for CSV files.
        self.split_csv = split_csv
        # The file tag.
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
        # The property name.
        self.name = name
        # The values of the property.
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


class SaveOpenJMeterSceneRequestOpenJMeterSceneRegionalCondition(TeaModel):
    def __init__(
        self,
        amount: int = None,
        region: str = None,
    ):
        # The number of stress tests. The sum of the number of stress tests in all regions must be equal to the AgentCount value of a specified scenario.
        self.amount = amount
        # The region ID.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
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
        max_rps: int = None,
        mode: str = None,
        ramp_up: int = None,
        region_id: str = None,
        regional_condition: List[SaveOpenJMeterSceneRequestOpenJMeterSceneRegionalCondition] = None,
        scene_id: str = None,
        scene_name: str = None,
        security_group_id: str = None,
        start_concurrency: int = None,
        start_rps: int = None,
        steps: int = None,
        sync_timer_type: str = None,
        test_file: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The number of stress testers.
        # 
        # This parameter is required.
        self.agent_count = agent_count
        # The maximum concurrency that is determined by the resource plans of users. You must configure this parameter when the mode is set to CONCURRENCY.
        self.concurrency = concurrency
        # The type of the synchronization timer with fixed throughput in JMeter.
        self.constant_throughput_timer_type = constant_throughput_timer_type
        # The settings of Domain Name System (DNS).
        self.dns_cache_config = dns_cache_config
        # The stress testing duration. The maximum stress testing duration is no more than one day, Unit: seconds. Valid values: 60 to 86400.
        # 
        # This parameter is required.
        self.duration = duration
        # The ID of the environment associated with the scenario.
        self.environment_id = environment_id
        # The test files.
        # 
        # This parameter is required.
        self.file_list = file_list
        # Specifies whether the test is a virtual private cloud (VPC) test. The default value is false, which indicates a public network test. VPC-related settings take effect only when you set this parameter to true.
        self.is_vpc_test = is_vpc_test
        # The JMeter properties.
        self.jmeter_properties = jmeter_properties
        # The JMeter plug-in tag.
        self.jmeter_plugin_label = jmeter_plugin_label
        # The maximum RPS that takes effect in RPS mode.
        self.max_rps = max_rps
        # The stress model.
        # 
        # This parameter is required.
        self.mode = mode
        # The ramp-up period. Unit: seconds.
        self.ramp_up = ramp_up
        # The region ID that is specified in the VPC test.
        self.region_id = region_id
        # The requirements for the regions of the stress testers.
        self.regional_condition = regional_condition
        # The scenario ID. If you do not configure this parameter, the system creates a scenario. If you configure this parameter, the system updates the scenario corresponding to the ID specified by this parameter.
        self.scene_id = scene_id
        # The scenario name.
        # 
        # This parameter is required.
        self.scene_name = scene_name
        # The security group ID that is specified in the VPC test.
        self.security_group_id = security_group_id
        # The initial concurrency that takes effect in concurrency mode. You must configure this parameter when the mode is set to CONCURRENCY.
        self.start_concurrency = start_concurrency
        # The initial RPS that takes effect in RPS mode.
        self.start_rps = start_rps
        # The number of ramp-up steps.
        self.steps = steps
        # The type of the synchronization timer in JMeter.
        self.sync_timer_type = sync_timer_type
        # The test file.
        # 
        # This parameter is required.
        self.test_file = test_file
        # The vSwitch ID that is specified in the VPC test.
        self.v_switch_id = v_switch_id
        # The VPC ID that is specified in the VPC test.
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
        if self.regional_condition:
            for k in self.regional_condition:
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
        if self.max_rps is not None:
            result['MaxRps'] = self.max_rps
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ramp_up is not None:
            result['RampUp'] = self.ramp_up
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RegionalCondition'] = []
        if self.regional_condition is not None:
            for k in self.regional_condition:
                result['RegionalCondition'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.start_concurrency is not None:
            result['StartConcurrency'] = self.start_concurrency
        if self.start_rps is not None:
            result['StartRps'] = self.start_rps
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
        if m.get('MaxRps') is not None:
            self.max_rps = m.get('MaxRps')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('RampUp') is not None:
            self.ramp_up = m.get('RampUp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.regional_condition = []
        if m.get('RegionalCondition') is not None:
            for k in m.get('RegionalCondition'):
                temp_model = SaveOpenJMeterSceneRequestOpenJMeterSceneRegionalCondition()
                self.regional_condition.append(temp_model.from_map(k))
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('StartConcurrency') is not None:
            self.start_concurrency = m.get('StartConcurrency')
        if m.get('StartRps') is not None:
            self.start_rps = m.get('StartRps')
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
        # The details of the scenario.
        # 
        # This parameter is required.
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
        # The details of the scenario.
        # 
        # This parameter is required.
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
        # The system status code. If the request was successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the request was successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is not returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The ID of the created or updated scenario.
        self.scene_id = scene_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: SaveOpenJMeterSceneResponseBody = None,
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
            temp_model = SaveOpenJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SavePtsSceneRequestSceneAdvanceSettingDomainBindingList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        ips: List[str] = None,
    ):
        # The domain name.
        self.domain = domain
        # The IP addresses.
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


class SavePtsSceneRequestSceneAdvanceSetting(TeaModel):
    def __init__(
        self,
        connection_timeout_in_second: int = None,
        domain_binding_list: List[SavePtsSceneRequestSceneAdvanceSettingDomainBindingList] = None,
        log_rate: int = None,
        success_code: str = None,
    ):
        # The timeout period. Unit: seconds.
        self.connection_timeout_in_second = connection_timeout_in_second
        # The domain name-IP address binding relationships
        self.domain_binding_list = domain_binding_list
        # The log sampling rate. Valid values: 1, 10, 20, 30, 40, and 50.
        self.log_rate = log_rate
        # The success status code. Separate multiple status codes with commas (,).
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
                temp_model = SavePtsSceneRequestSceneAdvanceSettingDomainBindingList()
                self.domain_binding_list.append(temp_model.from_map(k))
        if m.get('LogRate') is not None:
            self.log_rate = m.get('LogRate')
        if m.get('SuccessCode') is not None:
            self.success_code = m.get('SuccessCode')
        return self


class SavePtsSceneRequestSceneFileParameterList(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_oss_address: str = None,
    ):
        # The name of the file.
        self.file_name = file_name
        # The OSS URL of the file, which must be accessible over the Internet.
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


class SavePtsSceneRequestSceneGlobalParameterList(TeaModel):
    def __init__(
        self,
        param_name: str = None,
        param_value: str = None,
    ):
        # The name of the parameter.
        self.param_name = param_name
        # The value of the parameter.
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


class SavePtsSceneRequestSceneLoadConfigApiLoadConfigList(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        rps_begin: int = None,
        rps_limit: int = None,
    ):
        # The ID of the API.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The starting RPS.
        # 
        # This parameter is required.
        self.rps_begin = rps_begin
        # The maximum RPS.
        # 
        # This parameter is required.
        self.rps_limit = rps_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.rps_begin is not None:
            result['RpsBegin'] = self.rps_begin
        if self.rps_limit is not None:
            result['RpsLimit'] = self.rps_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('RpsBegin') is not None:
            self.rps_begin = m.get('RpsBegin')
        if m.get('RpsLimit') is not None:
            self.rps_limit = m.get('RpsLimit')
        return self


class SavePtsSceneRequestSceneLoadConfigConfiguration(TeaModel):
    def __init__(
        self,
        all_concurrency_begin: int = None,
        all_concurrency_limit: int = None,
        all_rps_begin: int = None,
        all_rps_limit: int = None,
    ):
        # The starting total number of concurrent virtual users in all sessions.
        # 
        # The value is evenly distributed among all sessions if you set TestMode to concurrency_mode. If you do not specify this parameter, you must configure **relationLoadConfig**.
        self.all_concurrency_begin = all_concurrency_begin
        # The maximum total number of concurrent virtual users in all sessions.
        # 
        # The value is evenly distributed among all sessions if you set TestMode to concurrency_mode. If you do not specify this parameter, you must configure **relationLoadConfig**.
        self.all_concurrency_limit = all_concurrency_limit
        # The starting RPS for all APIs.
        # 
        # The value is evenly distributed among all APIs if you set TestMode to RPS. If you do not specify this parameter, you must specify **apiLoadConfig**.
        self.all_rps_begin = all_rps_begin
        # The maximum RPS for all APIs.
        # 
        # The value is evenly distributed among all APIs if you set TestMode to RPS. If you do not specify this parameter, you must specify **apiLoadConfig**.
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


class SavePtsSceneRequestSceneLoadConfigRelationLoadConfigList(TeaModel):
    def __init__(
        self,
        concurrency_begin: int = None,
        concurrency_limit: int = None,
        relation_id: str = None,
    ):
        # The starting number of concurrent virtual users.
        # 
        # This parameter is required.
        self.concurrency_begin = concurrency_begin
        # The maximum number of concurrent virtual users.
        # 
        # This parameter is required.
        self.concurrency_limit = concurrency_limit
        # The ID of the session.
        self.relation_id = relation_id

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
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyBegin') is not None:
            self.concurrency_begin = m.get('ConcurrencyBegin')
        if m.get('ConcurrencyLimit') is not None:
            self.concurrency_limit = m.get('ConcurrencyLimit')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        return self


class SavePtsSceneRequestSceneLoadConfigVpcLoadConfig(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The ID of the vSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class SavePtsSceneRequestSceneLoadConfig(TeaModel):
    def __init__(
        self,
        agent_count: int = None,
        api_load_config_list: List[SavePtsSceneRequestSceneLoadConfigApiLoadConfigList] = None,
        auto_step: bool = None,
        configuration: SavePtsSceneRequestSceneLoadConfigConfiguration = None,
        increment: int = None,
        keep_time: int = None,
        max_running_time: int = None,
        relation_load_config_list: List[SavePtsSceneRequestSceneLoadConfigRelationLoadConfigList] = None,
        test_mode: str = None,
        vpc_load_config: SavePtsSceneRequestSceneLoadConfigVpcLoadConfig = None,
    ):
        # The number of load generators. If the number of concurrent virtual users exceeds 250 or the RPS exceeds 2,000, you can use multiple load generators. The maximum number of load generators is limited to the total number of concurrent virtual users divided by 250 or the total RPS divided by 200.
        self.agent_count = agent_count
        # The API request load settings.
        self.api_load_config_list = api_load_config_list
        # Specifies whether the load is automatically incremented. This parameter takes effect only if you set `TestMode=concurrency_mode`.
        self.auto_step = auto_step
        # The load level settings of the scenario.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The increment percentage. Valid values: 10 to 100, in increments of 10.
        # 
        # This parameter takes effect only if you set `testMode=concurrency_mode`and `autoStep=true`.
        self.increment = increment
        # The duration of a specific load level. Unit: minutes. The value must be less than the value of **maxRunningTime**.
        self.keep_time = keep_time
        # The duration of load application. Unit: minutes. Valid values: 1 to 1440.
        # 
        # This parameter is required.
        self.max_running_time = max_running_time
        # The session settings.
        self.relation_load_config_list = relation_load_config_list
        # The load application mode. Valid values:
        # 
        # *   concurrency_mode: concurrency mode
        # *   tps_mode: RPS mode.
        # 
        # This parameter is required.
        self.test_mode = test_mode
        # The VPC settings.
        self.vpc_load_config = vpc_load_config

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
        if self.vpc_load_config:
            self.vpc_load_config.validate()

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
        if self.auto_step is not None:
            result['AutoStep'] = self.auto_step
        if self.configuration is not None:
            result['Configuration'] = self.configuration.to_map()
        if self.increment is not None:
            result['Increment'] = self.increment
        if self.keep_time is not None:
            result['KeepTime'] = self.keep_time
        if self.max_running_time is not None:
            result['MaxRunningTime'] = self.max_running_time
        result['RelationLoadConfigList'] = []
        if self.relation_load_config_list is not None:
            for k in self.relation_load_config_list:
                result['RelationLoadConfigList'].append(k.to_map() if k else None)
        if self.test_mode is not None:
            result['TestMode'] = self.test_mode
        if self.vpc_load_config is not None:
            result['VpcLoadConfig'] = self.vpc_load_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCount') is not None:
            self.agent_count = m.get('AgentCount')
        self.api_load_config_list = []
        if m.get('ApiLoadConfigList') is not None:
            for k in m.get('ApiLoadConfigList'):
                temp_model = SavePtsSceneRequestSceneLoadConfigApiLoadConfigList()
                self.api_load_config_list.append(temp_model.from_map(k))
        if m.get('AutoStep') is not None:
            self.auto_step = m.get('AutoStep')
        if m.get('Configuration') is not None:
            temp_model = SavePtsSceneRequestSceneLoadConfigConfiguration()
            self.configuration = temp_model.from_map(m['Configuration'])
        if m.get('Increment') is not None:
            self.increment = m.get('Increment')
        if m.get('KeepTime') is not None:
            self.keep_time = m.get('KeepTime')
        if m.get('MaxRunningTime') is not None:
            self.max_running_time = m.get('MaxRunningTime')
        self.relation_load_config_list = []
        if m.get('RelationLoadConfigList') is not None:
            for k in m.get('RelationLoadConfigList'):
                temp_model = SavePtsSceneRequestSceneLoadConfigRelationLoadConfigList()
                self.relation_load_config_list.append(temp_model.from_map(k))
        if m.get('TestMode') is not None:
            self.test_mode = m.get('TestMode')
        if m.get('VpcLoadConfig') is not None:
            temp_model = SavePtsSceneRequestSceneLoadConfigVpcLoadConfig()
            self.vpc_load_config = temp_model.from_map(m['VpcLoadConfig'])
        return self


class SavePtsSceneRequestSceneRelationListApiListBody(TeaModel):
    def __init__(
        self,
        body_value: str = None,
        content_type: str = None,
    ):
        # The data in the body. For example, {"key1":"value2","key2":"value2"}.
        self.body_value = body_value
        # The body type. Default: `application/x-www-form-urlencoded`.
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


class SavePtsSceneRequestSceneRelationListApiListCheckPointList(TeaModel):
    def __init__(
        self,
        check_point: str = None,
        check_type: str = None,
        expect_value: str = None,
        operator: str = None,
    ):
        # The checked item.
        # 
        # This parameter specifies the fields in the header if you specify `CheckType=HEADER` or the name of the export parameter if you specify `CheckType=EXPORTED_PARAM`.
        self.check_point = check_point
        # The type of check. Valid values:
        # 
        # *   BODY_TEXT: the response body
        # *   HEADER: the response headers
        # *   STATUS_CODE: the HTTP status code returned by the API
        # *   EXPORTED_PARAM: a specific export parameter
        self.check_type = check_type
        # The expected value.
        self.expect_value = expect_value
        # The operation or condition that is checked against the expected value.
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


class SavePtsSceneRequestSceneRelationListApiListExportList(TeaModel):
    def __init__(
        self,
        count: str = None,
        export_name: str = None,
        export_type: str = None,
        export_value: str = None,
    ):
        # The index of the matched item. You can specify a number or "Random". If you set ExportType to BODY_TEXT, you must specify this parameter.
        self.count = count
        # The name of the export parameter.
        self.export_name = export_name
        # The source of the export parameter. Valid values:
        # 
        # *   BODY_TEXT: the request body in the BODY_TEXT format
        # *   BODY_JSON: the request body in the BODY_JSON format.
        # *   HEADER: the request header
        # *   STATUS_CODE: the HTTP status code returned by the API
        self.export_type = export_type
        # The actual path from which you want to extract the export parameter values.
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


class SavePtsSceneRequestSceneRelationListApiListHeaderList(TeaModel):
    def __init__(
        self,
        header_name: str = None,
        header_value: str = None,
    ):
        # The name of the header.
        self.header_name = header_name
        # The value of the header.
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


class SavePtsSceneRequestSceneRelationListApiList(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        body: SavePtsSceneRequestSceneRelationListApiListBody = None,
        check_point_list: List[SavePtsSceneRequestSceneRelationListApiListCheckPointList] = None,
        export_list: List[SavePtsSceneRequestSceneRelationListApiListExportList] = None,
        header_list: List[SavePtsSceneRequestSceneRelationListApiListHeaderList] = None,
        method: str = None,
        redirect_count_limit: int = None,
        timeout_in_second: int = None,
        url: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API operation.
        # 
        # This parameter is required.
        self.api_name = api_name
        # The request body.
        self.body = body
        # The checkpoints.
        self.check_point_list = check_point_list
        # The export parameters.
        self.export_list = export_list
        # The headers.
        self.header_list = header_list
        # The request method.
        # 
        # This parameter is required.
        self.method = method
        # The number of redirections. The value can be 0, which specifies that redirection is allowed, or 10, which specifies that redirection is not allowed. You can specify a value based on your business requirements.
        # 
        # This parameter is required.
        self.redirect_count_limit = redirect_count_limit
        # The timeout period of the API operation. Unit: seconds. Default: 5. Valid values: 1 to 60.
        self.timeout_in_second = timeout_in_second
        # The URL to which the API request is sent.
        # 
        # This parameter is required.
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
            temp_model = SavePtsSceneRequestSceneRelationListApiListBody()
            self.body = temp_model.from_map(m['Body'])
        self.check_point_list = []
        if m.get('CheckPointList') is not None:
            for k in m.get('CheckPointList'):
                temp_model = SavePtsSceneRequestSceneRelationListApiListCheckPointList()
                self.check_point_list.append(temp_model.from_map(k))
        self.export_list = []
        if m.get('ExportList') is not None:
            for k in m.get('ExportList'):
                temp_model = SavePtsSceneRequestSceneRelationListApiListExportList()
                self.export_list.append(temp_model.from_map(k))
        self.header_list = []
        if m.get('HeaderList') is not None:
            for k in m.get('HeaderList'):
                temp_model = SavePtsSceneRequestSceneRelationListApiListHeaderList()
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


class SavePtsSceneRequestSceneRelationListFileParameterExplainList(TeaModel):
    def __init__(
        self,
        base_file: bool = None,
        cycle_once: bool = None,
        file_name: str = None,
        file_param_name: str = None,
    ):
        # Specifies whether the file is used as the baseline file.
        self.base_file = base_file
        # Specifies whether the file is used for a single execution of the test.
        self.cycle_once = cycle_once
        # The name of the file.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The parameter names in the file.
        # 
        # This parameter is required.
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


class SavePtsSceneRequestSceneRelationList(TeaModel):
    def __init__(
        self,
        api_list: List[SavePtsSceneRequestSceneRelationListApiList] = None,
        file_parameter_explain_list: List[SavePtsSceneRequestSceneRelationListFileParameterExplainList] = None,
        relation_id: str = None,
        relation_name: str = None,
    ):
        # The API operations on the session.
        # 
        # This parameter is required.
        self.api_list = api_list
        # The file parameters of the session.
        self.file_parameter_explain_list = file_parameter_explain_list
        # The ID of the session.
        self.relation_id = relation_id
        # The name of the session.
        # 
        # This parameter is required.
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
                temp_model = SavePtsSceneRequestSceneRelationListApiList()
                self.api_list.append(temp_model.from_map(k))
        self.file_parameter_explain_list = []
        if m.get('FileParameterExplainList') is not None:
            for k in m.get('FileParameterExplainList'):
                temp_model = SavePtsSceneRequestSceneRelationListFileParameterExplainList()
                self.file_parameter_explain_list.append(temp_model.from_map(k))
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        if m.get('RelationName') is not None:
            self.relation_name = m.get('RelationName')
        return self


class SavePtsSceneRequestScene(TeaModel):
    def __init__(
        self,
        advance_setting: SavePtsSceneRequestSceneAdvanceSetting = None,
        file_parameter_list: List[SavePtsSceneRequestSceneFileParameterList] = None,
        global_parameter_list: List[SavePtsSceneRequestSceneGlobalParameterList] = None,
        load_config: SavePtsSceneRequestSceneLoadConfig = None,
        relation_list: List[SavePtsSceneRequestSceneRelationList] = None,
        scene_id: str = None,
        scene_name: str = None,
    ):
        # The advanced settings.
        self.advance_setting = advance_setting
        # The file parameters.
        self.file_parameter_list = file_parameter_list
        # The global customization parameters.
        self.global_parameter_list = global_parameter_list
        # The load settings.
        # 
        # This parameter is required.
        self.load_config = load_config
        # The sessions.
        # 
        # This parameter is required.
        self.relation_list = relation_list
        # The ID of the scenario. To save a new scenario, leave this parameter empty. To update an existing scenario, specify the ID of the scenario.
        self.scene_id = scene_id
        # The name of the scenario.
        # 
        # This parameter is required.
        self.scene_name = scene_name

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
        result['RelationList'] = []
        if self.relation_list is not None:
            for k in self.relation_list:
                result['RelationList'].append(k.to_map() if k else None)
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvanceSetting') is not None:
            temp_model = SavePtsSceneRequestSceneAdvanceSetting()
            self.advance_setting = temp_model.from_map(m['AdvanceSetting'])
        self.file_parameter_list = []
        if m.get('FileParameterList') is not None:
            for k in m.get('FileParameterList'):
                temp_model = SavePtsSceneRequestSceneFileParameterList()
                self.file_parameter_list.append(temp_model.from_map(k))
        self.global_parameter_list = []
        if m.get('GlobalParameterList') is not None:
            for k in m.get('GlobalParameterList'):
                temp_model = SavePtsSceneRequestSceneGlobalParameterList()
                self.global_parameter_list.append(temp_model.from_map(k))
        if m.get('LoadConfig') is not None:
            temp_model = SavePtsSceneRequestSceneLoadConfig()
            self.load_config = temp_model.from_map(m['LoadConfig'])
        self.relation_list = []
        if m.get('RelationList') is not None:
            for k in m.get('RelationList'):
                temp_model = SavePtsSceneRequestSceneRelationList()
                self.relation_list.append(temp_model.from_map(k))
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class SavePtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene: SavePtsSceneRequestScene = None,
    ):
        # The information about the scenario.
        # 
        # This parameter is required.
        self.scene = scene

    def validate(self):
        if self.scene:
            self.scene.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene is not None:
            result['Scene'] = self.scene.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scene') is not None:
            temp_model = SavePtsSceneRequestScene()
            self.scene = temp_model.from_map(m['Scene'])
        return self


class SavePtsSceneShrinkRequest(TeaModel):
    def __init__(
        self,
        scene_shrink: str = None,
    ):
        # The information about the scenario.
        # 
        # This parameter is required.
        self.scene_shrink = scene_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_shrink is not None:
            result['Scene'] = self.scene_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Scene') is not None:
            self.scene_shrink = m.get('Scene')
        return self


class SavePtsSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        scene_id: str = None,
        success: bool = None,
    ):
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # If the operation is successful, this parameter is not returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The ID of the scenario.
        self.scene_id = scene_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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


class SavePtsSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SavePtsSceneResponseBody = None,
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
            temp_model = SavePtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDebugPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The scenario ID.
        # 
        # This parameter is required.
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is left empty.
        self.message = message
        # The ID of the stress testing task.
        self.plan_id = plan_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: StartDebugPtsSceneResponseBody = None,
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
            temp_model = StartDebugPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDebuggingJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario that you want to debug.
        # 
        # This parameter is required.
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
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the debugging report.
        self.report_id = report_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: StartDebuggingJMeterSceneResponseBody = None,
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
            temp_model = StartDebuggingJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario that you want to start, which is the ID that is returned after the scenario is created. You can view scenario IDs on the scenario list page.
        # 
        # This parameter is required.
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The performance testing plan ID. If the scenario is successfully started, this parameter is returned.
        self.plan_id = plan_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: StartPtsSceneResponseBody = None,
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
            temp_model = StartPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTestingJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario.
        # 
        # This parameter is required.
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
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the report.
        self.report_id = report_id
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: StartTestingJMeterSceneResponseBody = None,
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
            temp_model = StartTestingJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDebugPtsSceneRequest(TeaModel):
    def __init__(
        self,
        plan_id: str = None,
        scene_id: str = None,
    ):
        # The ID of the stress testing task.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The scenario ID.
        # 
        # This parameter is required.
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message. If the request was successful, this parameter is left empty.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: StopDebugPtsSceneResponseBody = None,
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
            temp_model = StopDebugPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDebuggingJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario that you want to stop debugging.
        # 
        # This parameter is required.
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
        # The system status code. If the request was returned, this parameter is left empty.
        self.code = code
        # The HTTP status code. If the request was returned, this parameter is not returned.
        self.http_status_code = http_status_code
        # The returned message. If the request was returned, this parameter is not returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: StopDebuggingJMeterSceneResponseBody = None,
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
            temp_model = StopDebuggingJMeterSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopPtsSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the scenario that you want to stop, which is the ID that is returned after the scenario is created. You can view scenario IDs on the scenario list page in the PTS console.
        # 
        # This parameter is required.
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: StopPtsSceneResponseBody = None,
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
            temp_model = StopPtsSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTestingJMeterSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # The ID of the JMeter scenario.
        # 
        # This parameter is required.
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
        # The system status code. If the operation is successful, this parameter is not returned.
        self.code = code
        # The HTTP status code. If the operation is successful, this parameter is not returned.
        self.http_status_code = http_status_code
        # The error message. If the operation is successful, this parameter is not returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   true
        # *   false
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
        status_code: int = None,
        body: StopTestingJMeterSceneResponseBody = None,
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
        # null null
        self.api_baselines = api_baselines
        # null null
        self.scene_baseline = scene_baseline
        # The ID of the scene. For more information, see the [table](https://help.aliyun.com/document_detail/201321.html) provided in this topic.
        # 
        # This parameter is required.
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
        # null null
        self.api_baselines_shrink = api_baselines_shrink
        # null null
        self.scene_baseline_shrink = scene_baseline_shrink
        # The ID of the scene. For more information, see the [table](https://help.aliyun.com/document_detail/201321.html) provided in this topic.
        # 
        # This parameter is required.
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
        # The system status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # null
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # *   true
        # *   false:
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
        status_code: int = None,
        body: UpdatePtsSceneBaseLineResponseBody = None,
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
            temp_model = UpdatePtsSceneBaseLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


