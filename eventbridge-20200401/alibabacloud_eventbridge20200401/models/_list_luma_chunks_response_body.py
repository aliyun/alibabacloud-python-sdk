# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ListLumaChunksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLumaChunksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of Success indicates that the call succeeded. If the call fails, a specific error code is returned.
        self.code = code
        # The chunk list result, which contains chunk entries and pagination information.
        self.data = data
        # The message returned by the operation. The value is Operation success if the call succeeds, or a specific error description if the call fails.
        self.message = message
        # The unique ID of the request. Use this ID for troubleshooting and when submitting a ticket.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success.
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
            temp_model = main_models.ListLumaChunksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListLumaChunksResponseBodyData(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.KnowledgeBaseChunk] = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The list of chunk entries.
        self.chunks = chunks
        # The pagination token for the next page (an opaque string). Pass this value as the NextToken parameter in the next request to retrieve the next page. An empty value indicates that no more data is available.
        self.next_token = next_token
        # The total number of chunks in the document.
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

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

