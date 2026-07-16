# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aideepsign20260511 import models as main_models
from darabonba.model import DaraModel

class DetectAigcImageResponseBody(DaraModel):
    def __init__(
        self,
        body: List[main_models.DetectAigcImageResponseBodyBody] = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of AIGC detection result labels.
        self.body = body
        # The business error code. The value `OK` is returned if the request was successful.
        self.code = code
        # The HTTP status code. The value `200` is returned if the request was successful.
        self.http_status_code = http_status_code
        # The additional information. The value `success` is returned if the request was successful.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['Body'].append(k1.to_map() if k1 else None)

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
        self.body = []
        if m.get('Body') is not None:
            for k1 in m.get('Body'):
                temp_model = main_models.DetectAigcImageResponseBodyBody()
                self.body.append(temp_model.from_map(k1))

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



class DetectAigcImageResponseBodyBody(DaraModel):
    def __init__(
        self,
        confidence: str = None,
        label: str = None,
    ):
        # The confidence level. Value range: 0 to 1. A higher value indicates a higher probability.
        self.confidence = confidence
        # The detection label. Valid values:
        # - `ai_generated`: AI-generated.
        # - `non_ai_generated`: Not AI-generated.
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

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

