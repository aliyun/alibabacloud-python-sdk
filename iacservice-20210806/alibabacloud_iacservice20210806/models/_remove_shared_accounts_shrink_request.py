# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveSharedAccountsShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.account_ids_shrink = account_ids_shrink
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids_shrink is not None:
            result['accountIds'] = self.account_ids_shrink

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountIds') is not None:
            self.account_ids_shrink = m.get('accountIds')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

