# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveGroupRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        group_id: str = None,
        group_ids: List[str] = None,
    ):
        self.business_channel = business_channel
        # The ID of the user group to be deleted.
        self.group_id = group_id
        # The IDs of the user groups to be deleted.
        self.group_ids = group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        return self

