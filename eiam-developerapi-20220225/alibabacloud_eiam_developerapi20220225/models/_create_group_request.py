# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        group_external_id: str = None,
        group_name: str = None,
    ):
        # The external ID.
        self.group_external_id = group_external_id
        # The organization name.
        # 
        # This parameter is required.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_external_id is not None:
            result['groupExternalId'] = self.group_external_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupExternalId') is not None:
            self.group_external_id = m.get('groupExternalId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        return self

