# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class SearchLumaKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SearchLumaKnowledgeBaseResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of Success indicates a successful call. If the call fails, a specific error code is returned.
        self.code = code
        # The retrieval result from the knowledge base bound to the Agent.
        self.data = data
        # The message returned by the operation. The value is Operation success if the call succeeds, or a specific error description if the call fails.
        self.message = message
        # The unique identifier of the request, used for troubleshooting and ticket feedback.
        self.request_id = request_id
        # Indicates whether the call was successful. A value of true indicates success.
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
            temp_model = main_models.SearchLumaKnowledgeBaseResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchLumaKnowledgeBaseResponseBodyData(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.KnowledgeBaseSearchChunk] = None,
        time_spent: int = None,
    ):
        # The list of matched text chunks, sorted by relevance.
        self.chunks = chunks
        # The time spent on the retrieval, in milliseconds.
        self.time_spent = time_spent

    def validate(self):
        if self.chunks:
            for v1 in self.chunks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Chunks'] = []
        if self.chunks is not None:
            for k1 in self.chunks:
                result['Chunks'].append(k1.to_map() if k1 else None)

        if self.time_spent is not None:
            result['TimeSpent'] = self.time_spent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('Chunks') is not None:
            for k1 in m.get('Chunks'):
                temp_model = main_models.KnowledgeBaseSearchChunk()
                self.chunks.append(temp_model.from_map(k1))

        if m.get('TimeSpent') is not None:
            self.time_spent = m.get('TimeSpent')

        return self

