# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartPlaylistRequest(DaraModel):
    def __init__(
        self,
        offset: int = None,
        owner_id: int = None,
        program_id: str = None,
        region_id: str = None,
        resume_mode: str = None,
        start_item_id: str = None,
    ):
        # The start offset for the video file. This parameter is valid only for video files. Unit: milliseconds.
        # 
        # A value greater than 0 specifies the start time relative to the first frame.
        self.offset = offset
        self.owner_id = owner_id
        # The ID of the playlist. If you add items to the playlist by calling the [AddPlaylistItems](https://help.aliyun.com/document_detail/2848078.html) operation, use the value of the ProgramId parameter that is returned.
        # 
        # This parameter is required.
        self.program_id = program_id
        # The region ID.
        self.region_id = region_id
        # The restart mode. Valid values:
        # 
        # - **Restart**: Starts from the beginning.
        # 
        # - **Continue**: Resumes playback from where it was stopped. The **StartItemId** parameter is required only when you set the **ResumeMode** parameter to **Custom**.
        # 
        # - **Custom**: Custom start point.
        self.resume_mode = resume_mode
        # The ID of the item to play first. When the carousel starts, this item is played.
        # 
        # >Notice: 
        # 
        # This parameter is required only when you set **ResumeMode** to **Custom**.
        self.start_item_id = start_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offset is not None:
            result['Offset'] = self.offset

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resume_mode is not None:
            result['ResumeMode'] = self.resume_mode

        if self.start_item_id is not None:
            result['StartItemId'] = self.start_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResumeMode') is not None:
            self.resume_mode = m.get('ResumeMode')

        if m.get('StartItemId') is not None:
            self.start_item_id = m.get('StartItemId')

        return self

