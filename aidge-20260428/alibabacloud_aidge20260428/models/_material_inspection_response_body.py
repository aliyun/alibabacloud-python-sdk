# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class MaterialInspectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MaterialInspectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is not returned for successful calls.
        self.code = code
        # The material display detection result.
        self.data = data
        # The error message. This parameter is not returned for successful calls.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed.
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
            temp_model = main_models.MaterialInspectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MaterialInspectionResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.MaterialInspectionResponseBodyDataResult = None,
        usage_map: Dict[str, int] = None,
    ):
        # The inspection result.
        self.result = result
        # The usage information. The key is the usage metric name and the value is the count.
        self.usage_map = usage_map

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = main_models.MaterialInspectionResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class MaterialInspectionResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        evidence: str = None,
        overall_result: str = None,
        req_id: str = None,
        steps: List[main_models.MaterialInspectionResponseBodyDataResultSteps] = None,
        type: str = None,
    ):
        # The natural language summary, such as "1 rule: 1 PASS, all inspection items are compliant."
        self.evidence = evidence
        # The overall result. Valid values: PASS and FAIL.
        self.overall_result = overall_result
        # The request ID returned as-is from the input.
        self.req_id = req_id
        # The list of detection steps.
        self.steps = steps
        # The detection type.
        self.type = type

    def validate(self):
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evidence is not None:
            result['Evidence'] = self.evidence

        if self.overall_result is not None:
            result['OverallResult'] = self.overall_result

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        result['Steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['Steps'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Evidence') is not None:
            self.evidence = m.get('Evidence')

        if m.get('OverallResult') is not None:
            self.overall_result = m.get('OverallResult')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        self.steps = []
        if m.get('Steps') is not None:
            for k1 in m.get('Steps'):
                temp_model = main_models.MaterialInspectionResponseBodyDataResultSteps()
                self.steps.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MaterialInspectionResponseBodyDataResultSteps(DaraModel):
    def __init__(
        self,
        result: str = None,
        step_id: str = None,
    ):
        # The step result. Valid values: PASS, FAIL, and UNABLE_TO_JUDGE.
        self.result = result
        # The step ID.
        self.step_id = step_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result

        if self.step_id is not None:
            result['StepId'] = self.step_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('StepId') is not None:
            self.step_id = m.get('StepId')

        return self

