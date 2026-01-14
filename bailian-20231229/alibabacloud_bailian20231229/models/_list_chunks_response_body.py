# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListChunksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListChunksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The HTTP status code returned.
        self.status = status
        # Indications whether the API call is successful. Valid values:
        # 
        # *   true
        # *   false
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

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListChunksResponseBodyData(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.ListChunksResponseBodyDataNodes] = None,
        total: int = None,
    ):
        # The list of chunks.
        self.nodes = nodes
        # The total number of chunks returned.
        self.total = total

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ListChunksResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListChunksResponseBodyDataNodes(DaraModel):
    def __init__(
        self,
        metadata: Any = None,
        score: float = None,
        text: str = None,
    ):
        # The metadata map of the chunk.
        self.metadata = metadata
        # The similarity score of the chunk.
        self.score = score
        # The text of the chunk.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.score is not None:
            result['Score'] = self.score

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

