# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListPipelineIdsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListPipelineIdsResponseBodyResult] = None,
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
                temp_model = main_models.ListPipelineIdsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListPipelineIdsResponseBodyResult(DaraModel):
    def __init__(
        self,
        available: bool = None,
        code: str = None,
        message: str = None,
        pipeline_id: str = None,
    ):
        self.available = available
        self.code = code
        self.message = message
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['available'] = self.available

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.pipeline_id is not None:
            result['pipelineId'] = self.pipeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('available') is not None:
            self.available = m.get('available')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('pipelineId') is not None:
            self.pipeline_id = m.get('pipelineId')

        return self

