# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceGroupAdminSettingResponseBody(DaraModel):
    def __init__(
        self,
        creator_as_admin: bool = None,
        request_id: str = None,
    ):
        # Indicates whether enable the Use Creator as Administrator feature.
        self.creator_as_admin = creator_as_admin
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_as_admin is not None:
            result['CreatorAsAdmin'] = self.creator_as_admin

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorAsAdmin') is not None:
            self.creator_as_admin = m.get('CreatorAsAdmin')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

