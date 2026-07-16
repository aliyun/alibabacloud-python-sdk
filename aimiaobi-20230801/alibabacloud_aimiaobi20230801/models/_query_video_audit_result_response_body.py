# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class QueryVideoAuditResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryVideoAuditResultResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Business status code
        self.code = code
        # Video audit result data
        self.data = data
        # HTTP status code
        self.http_status_code = http_status_code
        # Return message
        self.message = message
        # Request ID
        self.request_id = request_id
        # Is successful
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
            temp_model = main_models.QueryVideoAuditResultResponseBodyData()
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

class QueryVideoAuditResultResponseBodyData(DaraModel):
    def __init__(
        self,
        duration: float = None,
        error_message: str = None,
        fps: float = None,
        frame_audited: int = None,
        height: int = None,
        image_urls: List[main_models.QueryVideoAuditResultResponseBodyDataImageUrls] = None,
        results: List[main_models.QueryVideoAuditResultResponseBodyDataResults] = None,
        status: str = None,
        text: str = None,
        total_frame_audit: int = None,
        total_frames: int = None,
        total_shots: int = None,
        video_file_key: str = None,
        video_url: str = None,
        width: int = None,
    ):
        # Video duration
        self.duration = duration
        # Error message
        self.error_message = error_message
        # Video frame rate
        self.fps = fps
        # Frames audited
        self.frame_audited = frame_audited
        # Video height
        self.height = height
        # Image URL list
        self.image_urls = image_urls
        # Audit results list
        self.results = results
        # Task status (PENDING: Queued, RUNNING: In progress, SUCCESSED: Successful, FAILED: Failed, CANCELED: Task canceled)
        self.status = status
        # Reviewed text
        self.text = text
        # Frames to audit
        self.total_frame_audit = total_frame_audit
        # Total frames
        self.total_frames = total_frames
        # Total shots
        self.total_shots = total_shots
        # Video FileKey
        self.video_file_key = video_file_key
        # Video URL
        self.video_url = video_url
        # Video width
        self.width = width

    def validate(self):
        if self.image_urls:
            for v1 in self.image_urls:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.frame_audited is not None:
            result['FrameAudited'] = self.frame_audited

        if self.height is not None:
            result['Height'] = self.height

        result['ImageUrls'] = []
        if self.image_urls is not None:
            for k1 in self.image_urls:
                result['ImageUrls'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.text is not None:
            result['Text'] = self.text

        if self.total_frame_audit is not None:
            result['TotalFrameAudit'] = self.total_frame_audit

        if self.total_frames is not None:
            result['TotalFrames'] = self.total_frames

        if self.total_shots is not None:
            result['TotalShots'] = self.total_shots

        if self.video_file_key is not None:
            result['VideoFileKey'] = self.video_file_key

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('FrameAudited') is not None:
            self.frame_audited = m.get('FrameAudited')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        self.image_urls = []
        if m.get('ImageUrls') is not None:
            for k1 in m.get('ImageUrls'):
                temp_model = main_models.QueryVideoAuditResultResponseBodyDataImageUrls()
                self.image_urls.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.QueryVideoAuditResultResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('TotalFrameAudit') is not None:
            self.total_frame_audit = m.get('TotalFrameAudit')

        if m.get('TotalFrames') is not None:
            self.total_frames = m.get('TotalFrames')

        if m.get('TotalShots') is not None:
            self.total_shots = m.get('TotalShots')

        if m.get('VideoFileKey') is not None:
            self.video_file_key = m.get('VideoFileKey')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class QueryVideoAuditResultResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        req_id: str = None,
        result: List[main_models.QueryVideoAuditResultResponseBodyDataResultsResult] = None,
        risk_level: str = None,
    ):
        # Image ID (Associate with ImageUrls[].Id to get image information)
        self.data_id = data_id
        # Request ID
        self.req_id = req_id
        # Detection results
        self.result = result
        # Risk level
        # 
        # - high: High risk
        # 
        # - medium: Medium risk
        # 
        # - low: Low risk
        # 
        # - none: No risk
        self.risk_level = risk_level

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryVideoAuditResultResponseBodyDataResultsResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class QueryVideoAuditResultResponseBodyDataResultsResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # From 0 to 100, retained to 2 decimal places. Some labels do not have a confidence score.
        self.confidence = confidence
        # Explanation of the Label field
        self.description = description
        # Risk label
        # 
        # The label of the image content review result. For example: nonLabel (no risk detected).
        # 
        # The label can also be a risk level that is determined by the high-risk and low-risk thresholds that you set. Valid return values are:
        # ● high: high risk
        # ● medium: medium risk
        # ● low: low risk
        # ● none: no risk detected
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class QueryVideoAuditResultResponseBodyDataImageUrls(DaraModel):
    def __init__(
        self,
        id: str = None,
        timestamp: float = None,
        url: str = None,
    ):
        # Image ID (Associate with Results[].DataId to get audit result information)
        self.id = id
        # Timestamp (milliseconds)
        self.timestamp = timestamp
        # Image URL
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

