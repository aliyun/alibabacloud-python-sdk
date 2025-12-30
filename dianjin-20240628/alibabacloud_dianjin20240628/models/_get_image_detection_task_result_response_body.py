# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetImageDetectionTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetImageDetectionTaskResultResponseBodyData = None,
        message: str = None,
        retry_able: bool = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.retry_able = retry_able
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.retry_able is not None:
            result['retryAble'] = self.retry_able

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('retryAble') is not None:
            self.retry_able = m.get('retryAble')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetImageDetectionTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        detection_conclusion: str = None,
        detection_result: main_models.GetImageDetectionTaskResultResponseBodyDataDetectionResult = None,
        file_info: main_models.GetImageDetectionTaskResultResponseBodyDataFileInfo = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.detection_conclusion = detection_conclusion
        self.detection_result = detection_result
        self.file_info = file_info
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        if self.detection_result:
            self.detection_result.validate()
        if self.file_info:
            self.file_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detection_conclusion is not None:
            result['detectionConclusion'] = self.detection_conclusion

        if self.detection_result is not None:
            result['detectionResult'] = self.detection_result.to_map()

        if self.file_info is not None:
            result['fileInfo'] = self.file_info.to_map()

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detectionConclusion') is not None:
            self.detection_conclusion = m.get('detectionConclusion')

        if m.get('detectionResult') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyDataDetectionResult()
            self.detection_result = temp_model.from_map(m.get('detectionResult'))

        if m.get('fileInfo') is not None:
            temp_model = main_models.GetImageDetectionTaskResultResponseBodyDataFileInfo()
            self.file_info = temp_model.from_map(m.get('fileInfo'))

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        return self

class GetImageDetectionTaskResultResponseBodyDataFileInfo(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        file_trace_id: str = None,
        oss_key: str = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.file_trace_id = file_trace_id
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['fileId'] = self.file_id

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.file_trace_id is not None:
            result['fileTraceId'] = self.file_trace_id

        if self.oss_key is not None:
            result['ossKey'] = self.oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('fileTraceId') is not None:
            self.file_trace_id = m.get('fileTraceId')

        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')

        return self

class GetImageDetectionTaskResultResponseBodyDataDetectionResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        detection_details: List[main_models.GetImageDetectionTaskResultResponseBodyDataDetectionResultDetectionDetails] = None,
        portrait_type: str = None,
        suggestions: List[str] = None,
    ):
        self.description = description
        self.detection_details = detection_details
        self.portrait_type = portrait_type
        self.suggestions = suggestions

    def validate(self):
        if self.detection_details:
            for v1 in self.detection_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        result['detectionDetails'] = []
        if self.detection_details is not None:
            for k1 in self.detection_details:
                result['detectionDetails'].append(k1.to_map() if k1 else None)

        if self.portrait_type is not None:
            result['portraitType'] = self.portrait_type

        if self.suggestions is not None:
            result['suggestions'] = self.suggestions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        self.detection_details = []
        if m.get('detectionDetails') is not None:
            for k1 in m.get('detectionDetails'):
                temp_model = main_models.GetImageDetectionTaskResultResponseBodyDataDetectionResultDetectionDetails()
                self.detection_details.append(temp_model.from_map(k1))

        if m.get('portraitType') is not None:
            self.portrait_type = m.get('portraitType')

        if m.get('suggestions') is not None:
            self.suggestions = m.get('suggestions')

        return self

class GetImageDetectionTaskResultResponseBodyDataDetectionResultDetectionDetails(DaraModel):
    def __init__(
        self,
        code: str = None,
        confidence: float = None,
        pass_: bool = None,
        reason: str = None,
    ):
        self.code = code
        self.confidence = confidence
        self.pass_ = pass_
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.confidence is not None:
            result['confidence'] = self.confidence

        if self.pass_ is not None:
            result['pass'] = self.pass_

        if self.reason is not None:
            result['reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')

        if m.get('pass') is not None:
            self.pass_ = m.get('pass')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        return self

