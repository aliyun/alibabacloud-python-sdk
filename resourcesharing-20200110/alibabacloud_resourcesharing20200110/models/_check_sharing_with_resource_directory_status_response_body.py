# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckSharingWithResourceDirectoryStatusResponseBody(DaraModel):
    def __init__(
        self,
        enable_sharing_with_rd: bool = None,
        request_id: str = None,
    ):
        # Indicates whether resource sharing within a resource directory is enabled. Valid values:
        # 
        # *   false
        # *   true
        self.enable_sharing_with_rd = enable_sharing_with_rd
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_sharing_with_rd is not None:
            result['EnableSharingWithRd'] = self.enable_sharing_with_rd

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSharingWithRd') is not None:
            self.enable_sharing_with_rd = m.get('EnableSharingWithRd')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

