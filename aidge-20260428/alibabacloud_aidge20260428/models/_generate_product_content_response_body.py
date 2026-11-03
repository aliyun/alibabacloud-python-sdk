# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class GenerateProductContentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GenerateProductContentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is not returned for successful calls.
        self.code = code
        # The processing result. Contains copy data upon success. Returns null upon business failure.
        self.data = data
        # The error message. This parameter is not returned for successful calls.
        self.message = message
        # The request ID, which is used for troubleshooting. This parameter may be empty in extreme exception scenarios.
        self.request_id = request_id
        # Indicates whether the business processing is successful. Valid values: true (the output passes verification) and false (the business processing fails).
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
            temp_model = main_models.GenerateProductContentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GenerateProductContentResponseBodyData(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        length: int = None,
        output_language: str = None,
        point_lengths: List[int] = None,
        points: List[str] = None,
        text: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The actual copy type processed.
        self.content_type = content_type
        # The total number of characters in data.text, including formatting characters such as spaces, punctuation marks, and line breaks.
        self.length = length
        # The code of the actual output language.
        self.output_language = output_language
        # The number of characters for each selling point, which corresponds to data.points one by one. This parameter is returned only when bullet points are successfully processed.
        self.point_lengths = point_lengths
        # The selling point texts arranged in output order. This parameter is returned only when bullet points are successfully processed.
        self.points = points
        # The final copy. Generated keywords are separated by commas and spaces. Rewritten keywords are separated by spaces. Bullet points are separated by line breaks.
        self.text = text
        # The usage information.
        self.usage_map = usage_map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.length is not None:
            result['Length'] = self.length

        if self.output_language is not None:
            result['OutputLanguage'] = self.output_language

        if self.point_lengths is not None:
            result['PointLengths'] = self.point_lengths

        if self.points is not None:
            result['Points'] = self.points

        if self.text is not None:
            result['Text'] = self.text

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('OutputLanguage') is not None:
            self.output_language = m.get('OutputLanguage')

        if m.get('PointLengths') is not None:
            self.point_lengths = m.get('PointLengths')

        if m.get('Points') is not None:
            self.points = m.get('Points')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

