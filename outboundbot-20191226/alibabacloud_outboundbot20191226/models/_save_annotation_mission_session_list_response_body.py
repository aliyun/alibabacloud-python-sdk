# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class SaveAnnotationMissionSessionListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SaveAnnotationMissionSessionListResponseBodyData = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.SaveAnnotationMissionSessionListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SaveAnnotationMissionSessionListResponseBodyData(DaraModel):
    def __init__(
        self,
        message: str = None,
        message_list: List[str] = None,
        save_annotation_mission_session_list_request: main_models.SaveAnnotationMissionSessionListResponseBodyDataSaveAnnotationMissionSessionListRequest = None,
        success: bool = None,
    ):
        self.message = message
        self.message_list = message_list
        self.save_annotation_mission_session_list_request = save_annotation_mission_session_list_request
        self.success = success

    def validate(self):
        if self.save_annotation_mission_session_list_request:
            self.save_annotation_mission_session_list_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.message_list is not None:
            result['MessageList'] = self.message_list

        if self.save_annotation_mission_session_list_request is not None:
            result['SaveAnnotationMissionSessionListRequest'] = self.save_annotation_mission_session_list_request.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MessageList') is not None:
            self.message_list = m.get('MessageList')

        if m.get('SaveAnnotationMissionSessionListRequest') is not None:
            temp_model = main_models.SaveAnnotationMissionSessionListResponseBodyDataSaveAnnotationMissionSessionListRequest()
            self.save_annotation_mission_session_list_request = temp_model.from_map(m.get('SaveAnnotationMissionSessionListRequest'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SaveAnnotationMissionSessionListResponseBodyDataSaveAnnotationMissionSessionListRequest(DaraModel):
    def __init__(
        self,
        annotation_mission_session_list_json_string: str = None,
    ):
        self.annotation_mission_session_list_json_string = annotation_mission_session_list_json_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_session_list_json_string is not None:
            result['AnnotationMissionSessionListJsonString'] = self.annotation_mission_session_list_json_string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionSessionListJsonString') is not None:
            self.annotation_mission_session_list_json_string = m.get('AnnotationMissionSessionListJsonString')

        return self

