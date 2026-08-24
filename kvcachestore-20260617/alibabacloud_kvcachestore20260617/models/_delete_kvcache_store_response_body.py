# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteKVCacheStoreResponseBody(DaraModel):
    def __init__(
        self,
        kvcs_id: str = None,
        request_id: str = None,
    ):
        # KVCacheStore KvcsId
        self.kvcs_id = kvcs_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kvcs_id is not None:
            result['KvcsId'] = self.kvcs_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KvcsId') is not None:
            self.kvcs_id = m.get('KvcsId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

