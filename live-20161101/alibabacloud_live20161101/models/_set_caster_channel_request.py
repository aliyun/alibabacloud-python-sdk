# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetCasterChannelRequest(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        channel_id: str = None,
        face_beauty: str = None,
        owner_id: int = None,
        play_status: int = None,
        region_id: str = None,
        resource_id: str = None,
        seek_offset: int = None,
    ):
        # The ID of the production studio.
        # 
        # - If you create a production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value returned in the response.
        # 
        # - If you create a production studio in the ApsaraVideo Live console, go to the **Production Studio** > **Cloud Production Studio** page to view the ID.
        # 
        # > The production studio name in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The channel ID.
        # 
        # The reference ID for the layout scene. You can set a maximum of one resource for each channel. The total number of channels is determined when you create the production studio. The format is \\`RV01\\` to \\`RV12\\`.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The facial retouching settings. Valid values: 0 (whole), 1 (skin smoothing), 2 (skin whitening), 3 (dark circle removal), and 4 (nasolabial fold removal).
        self.face_beauty = face_beauty
        self.owner_id = owner_id
        # The playback status. This parameter applies only to video files, not live streams. Valid values:
        # 
        # - **1** (default): Playback.
        # 
        # - **0**: Pause.
        self.play_status = play_status
        # The region ID.
        self.region_id = region_id
        # The ID of the video source.
        self.resource_id = resource_id
        # This parameter applies only to video files, not live streams. The value must be greater than or equal to 0. It specifies the offset from the first frame at which to start reading the file. Unit: milliseconds (ms).
        self.seek_offset = seek_offset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.face_beauty is not None:
            result['FaceBeauty'] = self.face_beauty

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.play_status is not None:
            result['PlayStatus'] = self.play_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.seek_offset is not None:
            result['SeekOffset'] = self.seek_offset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('FaceBeauty') is not None:
            self.face_beauty = m.get('FaceBeauty')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlayStatus') is not None:
            self.play_status = m.get('PlayStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('SeekOffset') is not None:
            self.seek_offset = m.get('SeekOffset')

        return self

