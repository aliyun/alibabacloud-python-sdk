# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListIndicesResponseBody(DaraModel):
    def __init__(
        self,
        indices: main_models.ListIndicesResponseBodyIndices = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The queried indexes.
        self.indices = indices
        # The returned message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # The status of the operation. Valid values:
        # 
        # *   **success**.
        # *   **fail**.
        self.status = status

    def validate(self):
        if self.indices:
            self.indices.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.indices is not None:
            result['Indices'] = self.indices.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Indices') is not None:
            temp_model = main_models.ListIndicesResponseBodyIndices()
            self.indices = temp_model.from_map(m.get('Indices'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListIndicesResponseBodyIndices(DaraModel):
    def __init__(
        self,
        indices: List[main_models.ListIndicesResponseBodyIndicesIndices] = None,
    ):
        self.indices = indices

    def validate(self):
        if self.indices:
            for v1 in self.indices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Indices'] = []
        if self.indices is not None:
            for k1 in self.indices:
                result['Indices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.indices = []
        if m.get('Indices') is not None:
            for k1 in m.get('Indices'):
                temp_model = main_models.ListIndicesResponseBodyIndicesIndices()
                self.indices.append(temp_model.from_map(k1))

        return self

class ListIndicesResponseBodyIndicesIndices(DaraModel):
    def __init__(
        self,
        collection: str = None,
        index_def: str = None,
        index_name: str = None,
        namespace: str = None,
    ):
        # The name of the collection.
        self.collection = collection
        # The definition of the index.
        self.index_def = index_def
        # The name of the index.
        self.index_name = index_name
        # The namespace to which the pod belongs.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        if self.index_def is not None:
            result['IndexDef'] = self.index_def

        if self.index_name is not None:
            result['IndexName'] = self.index_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('IndexDef') is not None:
            self.index_def = m.get('IndexDef')

        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

