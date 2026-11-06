# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataIngestionResponseBody(DaraModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
        request_id: str = None,
    ):
        self.data_ingestion_id = data_ingestion_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

