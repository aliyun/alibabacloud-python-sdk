# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetEmonMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.GetEmonMonitorDataResponseBodyResult] = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetEmonMonitorDataResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEmonMonitorDataResponseBodyResult(DaraModel):
    def __init__(
        self,
        dps: Dict[str, Any] = None,
        integrity: float = None,
        message_watermark: int = None,
        metric: str = None,
        summary: float = None,
        tags: Dict[str, Any] = None,
    ):
        self.dps = dps
        self.integrity = integrity
        self.message_watermark = message_watermark
        self.metric = metric
        self.summary = summary
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dps is not None:
            result['dps'] = self.dps

        if self.integrity is not None:
            result['integrity'] = self.integrity

        if self.message_watermark is not None:
            result['messageWatermark'] = self.message_watermark

        if self.metric is not None:
            result['metric'] = self.metric

        if self.summary is not None:
            result['summary'] = self.summary

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dps') is not None:
            self.dps = m.get('dps')

        if m.get('integrity') is not None:
            self.integrity = m.get('integrity')

        if m.get('messageWatermark') is not None:
            self.message_watermark = m.get('messageWatermark')

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

