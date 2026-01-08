# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class DescribeImageModerationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeImageModerationResultResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code.
        self.code = code
        # The image moderation results.
        self.data = data
        # The message that is returned in response to the request.
        self.msg = msg
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id

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

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeImageModerationResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageModerationResultResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        data_id: str = None,
        frame: str = None,
        frame_num: int = None,
        manual_task_id: str = None,
        req_id: str = None,
        result: List[main_models.DescribeImageModerationResultResponseBodyDataResult] = None,
        risk_level: str = None,
    ):
        self.account_id = account_id
        # The value of dataId that is specified in the API request. If this parameter is not specified in the API request, this field is not available in the response.
        self.data_id = data_id
        # The information about the captured frames.
        self.frame = frame
        # The number of frames.
        self.frame_num = frame_num
        self.manual_task_id = manual_task_id
        # The reqId field returned by the Image Async Moderation API.
        self.req_id = req_id
        # The results of image moderation parameters such as the label parameter and the confidence parameter.
        self.result = result
        # Risk Level.
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
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.frame is not None:
            result['Frame'] = self.frame

        if self.frame_num is not None:
            result['FrameNum'] = self.frame_num

        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id

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
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Frame') is not None:
            self.frame = m.get('Frame')

        if m.get('FrameNum') is not None:
            self.frame_num = m.get('FrameNum')

        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeImageModerationResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class DescribeImageModerationResultResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
        risk_level: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The description of the result.
        self.description = description
        # The labels returned after the image moderation.
        self.label = label
        # Risk Level
        self.risk_level = risk_level

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

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

