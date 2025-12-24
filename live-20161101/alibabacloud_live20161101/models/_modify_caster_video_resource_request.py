# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCasterVideoResourceRequest(DaraModel):
    def __init__(
        self,
        begin_offset: int = None,
        caster_id: str = None,
        end_offset: int = None,
        image_id: str = None,
        image_url: str = None,
        live_stream_url: str = None,
        material_id: str = None,
        owner_id: int = None,
        pts_callback_interval: int = None,
        region_id: str = None,
        repeat_num: int = None,
        resource_id: str = None,
        resource_name: str = None,
        vod_url: str = None,
    ):
        # The offset of the position where the system starts to read the video resource.
        # 
        # This parameter takes effect only when the video resource is a video file. Unit: milliseconds.
        # 
        # >  A value greater than 0 indicates an offset from the first frame.
        self.begin_offset = begin_offset
        # The ID of the production studio.
        # 
        # If you create a production studio through the [CreateCaster](~~69338#doc-api-live-CreateCaster~~ "Creates a production studio.") interface, check the value of the CasterId parameter in the response.
        # 
        # If you create a production studio through the ApsaraVideo Live Console, log in to the console, then check the ID of the production studio through the following path:
        # 
        # Production Studios > Production Studio Management
        # 
        # >  The CasterId is reflected in the Name column on the Production Studio Management page.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # This parameter takes effect only when the video resource is a video file. Unit: milliseconds.
        # 
        # *   A value greater than **0** indicates an offset from the first frame.
        # *   A value smaller than **0** indicates an offset from the last frame.
        self.end_offset = end_offset
        # ID of the media library image material.
        # > This parameter is only available and must be provided when the video source type is an image.
        self.image_id = image_id
        # Image material URL. 
        # >This parameter is only available when the video source type is an image and the image file has not been imported into the material library. Supports uploading images in jpg, png formats, with a maximum file size of 10MB.
        self.image_url = image_url
        # The URL of the live stream.
        # 
        # This parameter takes effect and is required only when the video resource is a live stream.
        self.live_stream_url = live_stream_url
        # The ID of the material.
        self.material_id = material_id
        self.owner_id = owner_id
        # The interval between presentation timestamp (PTS) callbacks. Unit: milliseconds. This parameter takes effect only when the video resource is a VOD file.
        self.pts_callback_interval = pts_callback_interval
        self.region_id = region_id
        # The number of playback times after the first playback is complete. This parameter takes effect only when the video resource is a file. Valid values:
        # 
        # *   **0**: indicates that the video is played only once. This is the default value.
        # *   **-1**: indicates that the video is played in loop mode.
        self.repeat_num = repeat_num
        # The ID of the video resource. It is reflected in the ResourceId parameter when you call the [AddCasterVideoResource](~~60250#doc-api-live-AddCasterVideoResource~~ "Adds a video resource to a production studio.") operation.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The name of the video resource.
        self.resource_name = resource_name
        # The URL of the video-on-demand (VOD) file. This parameter takes effect only when the video resource is a video file that is not from the media library.
        # 
        # >  The VOD file must be in the MP4, FLV, or TS format.
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_offset is not None:
            result['BeginOffset'] = self.begin_offset

        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.end_offset is not None:
            result['EndOffset'] = self.end_offset

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.live_stream_url is not None:
            result['LiveStreamUrl'] = self.live_stream_url

        if self.material_id is not None:
            result['MaterialId'] = self.material_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pts_callback_interval is not None:
            result['PtsCallbackInterval'] = self.pts_callback_interval

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repeat_num is not None:
            result['RepeatNum'] = self.repeat_num

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginOffset') is not None:
            self.begin_offset = m.get('BeginOffset')

        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('EndOffset') is not None:
            self.end_offset = m.get('EndOffset')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('LiveStreamUrl') is not None:
            self.live_stream_url = m.get('LiveStreamUrl')

        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PtsCallbackInterval') is not None:
            self.pts_callback_interval = m.get('PtsCallbackInterval')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepeatNum') is not None:
            self.repeat_num = m.get('RepeatNum')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')

        return self

