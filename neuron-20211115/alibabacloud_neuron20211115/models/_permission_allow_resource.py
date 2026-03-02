# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PermissionAllowResource(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_list: List[str] = None,
    ):
        self.request_id = request_id
        self.resource_list = resource_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_list is not None:
            result['resourceList'] = self.resource_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceList') is not None:
            self.resource_list = m.get('resourceList')

        return self

