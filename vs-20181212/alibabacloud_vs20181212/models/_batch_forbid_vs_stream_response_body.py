# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class BatchForbidVsStreamResponseBody(DaraModel):
    def __init__(
        self,
        forbid_result: main_models.BatchForbidVsStreamResponseBodyForbidResult = None,
        request_id: str = None,
    ):
        self.forbid_result = forbid_result
        self.request_id = request_id

    def validate(self):
        if self.forbid_result:
            self.forbid_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forbid_result is not None:
            result['ForbidResult'] = self.forbid_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForbidResult') is not None:
            temp_model = main_models.BatchForbidVsStreamResponseBodyForbidResult()
            self.forbid_result = temp_model.from_map(m.get('ForbidResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchForbidVsStreamResponseBodyForbidResult(DaraModel):
    def __init__(
        self,
        forbid_result_info: List[main_models.BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo] = None,
    ):
        self.forbid_result_info = forbid_result_info

    def validate(self):
        if self.forbid_result_info:
            for v1 in self.forbid_result_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ForbidResultInfo'] = []
        if self.forbid_result_info is not None:
            for k1 in self.forbid_result_info:
                result['ForbidResultInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.forbid_result_info = []
        if m.get('ForbidResultInfo') is not None:
            for k1 in m.get('ForbidResultInfo'):
                temp_model = main_models.BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo()
                self.forbid_result_info.append(temp_model.from_map(k1))

        return self

class BatchForbidVsStreamResponseBodyForbidResultForbidResultInfo(DaraModel):
    def __init__(
        self,
        channels: main_models.BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels = None,
        count: int = None,
        detail: str = None,
        result: str = None,
    ):
        self.channels = channels
        self.count = count
        self.detail = detail
        self.result = result

    def validate(self):
        if self.channels:
            self.channels.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()

        if self.count is not None:
            result['Count'] = self.count

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            temp_model = main_models.BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels()
            self.channels = temp_model.from_map(m.get('Channels'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class BatchForbidVsStreamResponseBodyForbidResultForbidResultInfoChannels(DaraModel):
    def __init__(
        self,
        channel: List[str] = None,
    ):
        self.channel = channel

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        return self

