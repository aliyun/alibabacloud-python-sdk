# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_videorecog20200320 import models as main_models
from darabonba.model import DaraModel

class GenerateVideoCoverResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GenerateVideoCoverResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GenerateVideoCoverResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GenerateVideoCoverResponseBodyData(DaraModel):
    def __init__(
        self,
        outputs: List[main_models.GenerateVideoCoverResponseBodyDataOutputs] = None,
    ):
        self.outputs = outputs

    def validate(self):
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['Outputs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outputs = []
        if m.get('Outputs') is not None:
            for k1 in m.get('Outputs'):
                temp_model = main_models.GenerateVideoCoverResponseBodyDataOutputs()
                self.outputs.append(temp_model.from_map(k1))

        return self

class GenerateVideoCoverResponseBodyDataOutputs(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        image_url: str = None,
    ):
        self.confidence = confidence
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.image_url is not None:
            result['ImageURL'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')

        return self

