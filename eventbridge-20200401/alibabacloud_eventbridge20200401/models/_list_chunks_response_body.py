# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListChunksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListChunksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of Success indicates that the call is successful. If the call fails, a specific error code is returned.
        self.code = code
        # The query result of the chunk list, which includes chunk entries and pagination information.
        self.data = data
        # The prompt message returned by the API. If the call is successful, the value is Operation success. If the call fails, a specific error description is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates that the call is successful.
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
            temp_model = main_models.ListChunksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListChunksResponseBodyData(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.KnowledgeBaseChunk] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The list of chunk entries.
        self.chunks = chunks
        # The actual maximum number of results per page that takes effect for the current request.
        self.max_results = max_results
        # The pagination token for the next page, which is an opaque string. Pass this value to the NextToken parameter of the next request to obtain the next page. An empty value indicates that no more data is available.
        self.next_token = next_token
        # The total number of chunks in the specified document. This parameter is returned only when DocumentId is specified. In full-base mode (when DocumentId is not specified), this parameter is not returned, and pagination ends when NextToken is empty.
        self.total_count = total_count

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('Chunks') is not None:
            for k1 in m.get('Chunks'):
                temp_model = main_models.KnowledgeBaseChunk()
                self.chunks.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

