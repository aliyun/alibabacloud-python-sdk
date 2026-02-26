# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetPromptTestResultResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.GetPromptTestResultResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetPromptTestResultResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class GetPromptTestResultResponseBodyResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        label_details: List[main_models.GetPromptTestResultResponseBodyResultLabelDetails] = None,
        risk_level: str = None,
    ):
        self.content = content
        self.label_details = label_details
        self.risk_level = risk_level

    def validate(self):
        if self.label_details:
            for v1 in self.label_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        result['LabelDetails'] = []
        if self.label_details is not None:
            for k1 in self.label_details:
                result['LabelDetails'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.label_details = []
        if m.get('LabelDetails') is not None:
            for k1 in m.get('LabelDetails'):
                temp_model = main_models.GetPromptTestResultResponseBodyResultLabelDetails()
                self.label_details.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class GetPromptTestResultResponseBodyResultLabelDetails(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
    ):
        self.description = description
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

