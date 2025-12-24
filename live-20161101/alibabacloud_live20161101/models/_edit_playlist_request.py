# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditPlaylistRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        program_config: str = None,
        program_id: str = None,
        program_items: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        # The configurations of the episode list. For more information, see the **ProgramConfig** section of this topic.
        self.program_config = program_config
        # The ID of the episode list. If the episode list was created by calling the [AddPlaylistItems](https://help.aliyun.com/document_detail/2848078.html) operation, check the value of the response parameter ProgramId to obtain the ID.
        # 
        # This parameter is required.
        self.program_id = program_id
        # The episodes that you want to add to the production studio. The value is a JSON string. For more information, see the **InputProgramItem** section of this topic.
        # 
        # This parameter is required.
        self.program_items = program_items
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

        if self.program_config is not None:
            result['ProgramConfig'] = self.program_config

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.program_items is not None:
            result['ProgramItems'] = self.program_items

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProgramConfig') is not None:
            self.program_config = m.get('ProgramConfig')

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('ProgramItems') is not None:
            self.program_items = m.get('ProgramItems')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

