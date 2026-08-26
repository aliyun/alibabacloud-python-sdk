# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPlaylistItemsRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        program_id: str = None,
        program_item_ids: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        # The ID of the playlist. You can obtain the ID from the ProgramId parameter in the response of the [AddPlaylistItems](https://help.aliyun.com/document_detail/2848078.html) operation.
        # 
        # This parameter is required.
        self.program_id = program_id
        # The IDs of the playlist items. Separate multiple IDs with commas (,). If you specify this parameter, only the information about the specified items is returned. If you leave this parameter empty, the information about all items in the playlist is returned.
        self.program_item_ids = program_item_ids
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.program_item_ids is not None:
            result['ProgramItemIds'] = self.program_item_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('ProgramItemIds') is not None:
            self.program_item_ids = m.get('ProgramItemIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

