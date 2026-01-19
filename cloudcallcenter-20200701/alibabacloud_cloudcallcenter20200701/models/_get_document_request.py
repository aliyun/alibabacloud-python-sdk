# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDocumentRequest(DaraModel):
    def __init__(
        self,
        document_id: str = None,
        instance_id: str = None,
        request_id: str = None,
        schema_id: str = None,
    ):
        # This parameter is required.
        self.document_id = document_id
        # This parameter is required.
        self.instance_id = instance_id
        self.request_id = request_id
        # schema id
        # 
        # This parameter is required.
        self.schema_id = schema_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        return self

