# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class DiduiAreaDeductionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DiduiAreaDeductionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The floor display area inference result.
        self.data = data
        # The error message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful.
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
            temp_model = main_models.DiduiAreaDeductionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DiduiAreaDeductionResponseBodyData(DaraModel):
    def __init__(
        self,
        attempts: int = None,
        code: str = None,
        http_status: int = None,
        latency_ms: int = None,
        message: str = None,
        model_request_id: str = None,
        req_id: str = None,
        result: main_models.DiduiAreaDeductionResponseBodyDataResult = None,
        status: str = None,
        success: bool = None,
        usage_map: Dict[str, int] = None,
    ):
        # The number of downstream call attempts.
        self.attempts = attempts
        # The workflow error code.
        self.code = code
        # The downstream HTTP status code.
        self.http_status = http_status
        # The downstream call latency, in milliseconds.
        self.latency_ms = latency_ms
        # The workflow description.
        self.message = message
        # The model request ID.
        self.model_request_id = model_request_id
        # The business request ID.
        self.req_id = req_id
        # The area calculation result.
        self.result = result
        # The workflow status.
        self.status = status
        # The workflow business status.
        self.success = success
        # The usage information.
        self.usage_map = usage_map

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempts is not None:
            result['Attempts'] = self.attempts

        if self.code is not None:
            result['Code'] = self.code

        if self.http_status is not None:
            result['HttpStatus'] = self.http_status

        if self.latency_ms is not None:
            result['LatencyMs'] = self.latency_ms

        if self.message is not None:
            result['Message'] = self.message

        if self.model_request_id is not None:
            result['ModelRequestId'] = self.model_request_id

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attempts') is not None:
            self.attempts = m.get('Attempts')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatus') is not None:
            self.http_status = m.get('HttpStatus')

        if m.get('LatencyMs') is not None:
            self.latency_ms = m.get('LatencyMs')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModelRequestId') is not None:
            self.model_request_id = m.get('ModelRequestId')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('Result') is not None:
            temp_model = main_models.DiduiAreaDeductionResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class DiduiAreaDeductionResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        stage_4area_label: main_models.DiduiAreaDeductionResponseBodyDataResultStage4AreaLabel = None,
    ):
        # The stage 4 area label.
        self.stage_4area_label = stage_4area_label

    def validate(self):
        if self.stage_4area_label:
            self.stage_4area_label.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stage_4area_label is not None:
            result['Stage4AreaLabel'] = self.stage_4area_label.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stage4AreaLabel') is not None:
            temp_model = main_models.DiduiAreaDeductionResponseBodyDataResultStage4AreaLabel()
            self.stage_4area_label = temp_model.from_map(m.get('Stage4AreaLabel'))

        return self

class DiduiAreaDeductionResponseBodyDataResultStage4AreaLabel(DaraModel):
    def __init__(
        self,
        area_m2: float = None,
        left_edge_m: float = None,
        right_edge_m: float = None,
    ):
        # The floor display area, in square meters.
        self.area_m2 = area_m2
        # The left edge length, in meters.
        self.left_edge_m = left_edge_m
        # The right edge length, in meters.
        self.right_edge_m = right_edge_m

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_m2 is not None:
            result['AreaM2'] = self.area_m2

        if self.left_edge_m is not None:
            result['LeftEdgeM'] = self.left_edge_m

        if self.right_edge_m is not None:
            result['RightEdgeM'] = self.right_edge_m

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaM2') is not None:
            self.area_m2 = m.get('AreaM2')

        if m.get('LeftEdgeM') is not None:
            self.left_edge_m = m.get('LeftEdgeM')

        if m.get('RightEdgeM') is not None:
            self.right_edge_m = m.get('RightEdgeM')

        return self

