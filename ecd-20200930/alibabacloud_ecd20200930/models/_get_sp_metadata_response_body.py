# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSpMetadataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sp_metadata: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The metadata of the SP.
        self.sp_metadata = sp_metadata

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sp_metadata is not None:
            result['SpMetadata'] = self.sp_metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SpMetadata') is not None:
            self.sp_metadata = m.get('SpMetadata')

        return self

