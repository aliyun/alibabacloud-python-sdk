# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCollectionResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        metadata: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The returned message.
        self.message = message
        # The metadata of the vector data, which is a JSON string in the MAP format. The key specifies the field name, and the value specifies the data type.
        # 
        # > 
        # 
        # *   For information about the supported data types, see [Data types](https://help.aliyun.com/document_detail/424383.html).
        # 
        # *   The money data type is not supported.
        self.metadata = metadata
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

