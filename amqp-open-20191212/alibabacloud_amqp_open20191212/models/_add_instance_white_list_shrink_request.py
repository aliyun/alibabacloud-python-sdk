# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddInstanceWhiteListShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        white_list_item_shrink: str = None,
        white_list_type: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.white_list_item_shrink = white_list_item_shrink
        # This parameter is required.
        self.white_list_type = white_list_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.white_list_item_shrink is not None:
            result['WhiteListItem'] = self.white_list_item_shrink

        if self.white_list_type is not None:
            result['WhiteListType'] = self.white_list_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('WhiteListItem') is not None:
            self.white_list_item_shrink = m.get('WhiteListItem')

        if m.get('WhiteListType') is not None:
            self.white_list_type = m.get('WhiteListType')

        return self

