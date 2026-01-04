# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The type of the resource.
        # 
        # Valid values:
        # 
        # *   instance
        # *   eip
        # *   disk
        # *   network
        # *   natgateway
        # *   vswitch
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

