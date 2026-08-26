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
        # The start offset of the video file. Unit: milliseconds.
        # 
        # >Notice: 
        # 
        # This parameter is valid only if the video source is a video file.
        # 
        # 
        # 
        # > A value greater than 0 specifies the start time to read the file. The time is an offset from the first frame.
        self.begin_offset = begin_offset
        # The ID of the production studio.
        # 
        # - If you create a production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId returned in the response.
        # 
        # - If you create a production studio in the console, find the ID on the **Cloud Production Studio** page. To go to this page, choose **LIVE Console** > **Production Studio**.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is its ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # This parameter is valid only for video files. Unit: milliseconds.
        # 
        # - If the value is greater than **0**, it specifies the end time to read the file. The time is an offset from the first frame.
        # 
        # - If the value is less than **0**, it specifies the end time to read the file. The time is an offset from the last frame.
        self.end_offset = end_offset
        # The ID of the image material in the media asset library.
        # 
        # > This parameter is required only if the video source is an image.
        self.image_id = image_id
        # The URL of the image material.
        # 
        # > This parameter is available only if the video source is an image that has not been imported to the material library. The image must be in JPG or PNG format, and its size cannot exceed 10 MB.
        self.image_url = image_url
        # The URL of the live stream.
        # 
        # >Notice: 
        # 
        # This parameter is required only if the video source is a live stream.
        self.live_stream_url = live_stream_url
        # The material ID.
        self.material_id = material_id
        self.owner_id = owner_id
        # The Presentation Time Stamp (PTS) callback interval. Unit: milliseconds. This parameter is valid only for VOD materials.
        self.pts_callback_interval = pts_callback_interval
        # The region ID.
        self.region_id = region_id
        # This parameter is valid only for video files. It specifies the number of times to loop the video after playback is complete.
        # 
        # - **0** (default): The video does not loop.
        # 
        # - **-1**: The video loops indefinitely.
        self.repeat_num = repeat_num
        # The resource ID. If you add a video source to the production studio by calling the [AddCasterVideoResource](https://help.aliyun.com/document_detail/2848020.html) operation, use the ResourceId returned in the response.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The name of the video source.
        self.resource_name = resource_name
        # The URL of the video on demand (VOD) file.
        # 
        # >Notice: 
        # 
        # This parameter is available only if the video source is a video file that has not been imported to the material library.
        # 
        # 
        # 
        # > VOD files must be in MP4, FLV, or TS format.
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

