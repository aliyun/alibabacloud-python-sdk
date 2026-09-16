# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAIDBClusterCustomModelResponseBody(DaraModel):
    def __init__(
        self,
        deleted: bool = None,
        model_id: int = None,
        model_name: str = None,
        request_id: str = None,
    ):
        # Indicates whether the deletion was successful.
        self.deleted = deleted
        # The ID of the deleted model registration.
        self.model_id = model_id
        # The key of the deleted custom model registration.
        self.model_name = model_name
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

