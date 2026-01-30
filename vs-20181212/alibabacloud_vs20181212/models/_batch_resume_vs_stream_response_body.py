# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class BatchResumeVsStreamResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resume_result: main_models.BatchResumeVsStreamResponseBodyResumeResult = None,
    ):
        self.request_id = request_id
        self.resume_result = resume_result

    def validate(self):
        if self.resume_result:
            self.resume_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resume_result is not None:
            result['ResumeResult'] = self.resume_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResumeResult') is not None:
            temp_model = main_models.BatchResumeVsStreamResponseBodyResumeResult()
            self.resume_result = temp_model.from_map(m.get('ResumeResult'))

        return self

class BatchResumeVsStreamResponseBodyResumeResult(DaraModel):
    def __init__(
        self,
        resume_result_info: List[main_models.BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo] = None,
    ):
        self.resume_result_info = resume_result_info

    def validate(self):
        if self.resume_result_info:
            for v1 in self.resume_result_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResumeResultInfo'] = []
        if self.resume_result_info is not None:
            for k1 in self.resume_result_info:
                result['ResumeResultInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resume_result_info = []
        if m.get('ResumeResultInfo') is not None:
            for k1 in m.get('ResumeResultInfo'):
                temp_model = main_models.BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo()
                self.resume_result_info.append(temp_model.from_map(k1))

        return self

class BatchResumeVsStreamResponseBodyResumeResultResumeResultInfo(DaraModel):
    def __init__(
        self,
        channels: main_models.BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels = None,
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
            temp_model = main_models.BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels()
            self.channels = temp_model.from_map(m.get('Channels'))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class BatchResumeVsStreamResponseBodyResumeResultResumeResultInfoChannels(DaraModel):
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

