# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddVodStorageForAppResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        storage_location: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The address of the VOD bucket.
        self.storage_location = storage_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        return self

