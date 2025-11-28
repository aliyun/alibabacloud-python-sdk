# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeIndexResponseBody(DaraModel):
    def __init__(
        self,
        collection: str = None,
        index_def: str = None,
        index_name: str = None,
        message: str = None,
        namespace: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The name of the collection.
        self.collection = collection
        # The definition of the index.
        self.index_def = index_def
        # The name of the index.
        self.index_name = index_name
        # The returned message.
        self.message = message
        # The namespace.
        self.namespace = namespace
        # The unique ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **false**: The operation fails.
        # *   **true**: The operation is successful.
        self.status = status

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

        if self.message is not None:
            result['Message'] = self.message

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('IndexDef') is not None:
            self.index_def = m.get('IndexDef')

        if m.get('IndexName') is not None:
            self.index_name = m.get('IndexName')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

