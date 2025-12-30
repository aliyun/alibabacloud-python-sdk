# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLiveEditingIndexFileResponseBody(DaraModel):
    def __init__(
        self,
        index_file: str = None,
        request_id: str = None,
    ):
        # The URL of the index file.
        self.index_file = index_file
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_file is not None:
            result['IndexFile'] = self.index_file

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexFile') is not None:
            self.index_file = m.get('IndexFile')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

