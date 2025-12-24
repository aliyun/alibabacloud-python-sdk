# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePlaylistItemsRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        program_id: str = None,
        program_item_ids: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        # The ID of the episode list. If the episode list was created by calling the [AddPlaylistItems](https://help.aliyun.com/document_detail/2848078.html) operation, check the value of the response parameter ProgramId to obtain the ID.
        # 
        # This parameter is required.
        self.program_id = program_id
        # The IDs of the episodes that you want to remove.
        # 
        # This parameter is required.
        self.program_item_ids = program_item_ids
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

