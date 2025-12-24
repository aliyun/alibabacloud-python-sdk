# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCasterVideoResourceRequest(DaraModel):
    def __init__(
        self,
        begin_offset: int = None,
        caster_id: str = None,
        end_offset: int = None,
        fixed_delay_duration: int = None,
        image_id: str = None,
        image_url: str = None,
        live_stream_url: str = None,
        location_id: str = None,
        material_id: str = None,
        owner_id: int = None,
        pts_callback_interval: int = None,
        region_id: str = None,
        repeat_num: int = None,
        resource_name: str = None,
        vod_url: str = None,
    ):
        # The offset of the position where the system starts to read the video source. Unit: milliseconds.
        # 
        # **
        # 
        # **Important** This parameter takes effect only if the video source is a file.
        # 
        # > A value greater than **0** specifies an offset from the first frame.
        self.begin_offset = begin_offset
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/69338.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # > You can find the ID of the production studio in the Instance Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The offset of the position where the system stops reading the video source. Unit: milliseconds.
        # 
        # **
        # 
        # **Important** This parameter takes effect only if the video source is a file.
        # 
        # *   A value greater than **0** specifies an offset from the first frame.
        # *   A value less than **0** specifies an offset from the last frame.
        self.end_offset = end_offset
        # The fixed delay of the video layer. This parameter is used to synchronize the video with subtitles. Unit: milliseconds. Default value: 0. Valid values: `0 to 5000`.
        self.fixed_delay_duration = fixed_delay_duration
        # ID of the media library image material. 
        # >This parameter is only available and must be provided when the video source type is an image.
        self.image_id = image_id
        # Image material URL. 
        # >This parameter is available only when the video source type is an image and the image file has not been imported into the material library. Supports uploading images in jpg, png formats, with a maximum file size of 10MB.
        self.image_url = image_url
        # The streaming URL.
        # 
        # **
        # 
        # **Important** This parameter is required if the video source is a live stream.
        # 
        # > Do not specify this parameter in the request if the video source is not a live stream.
        self.live_stream_url = live_stream_url
        # The ID that is used to identify the position of the video source.
        # 
        # Define the reference numbers in the layout. Each reference number is associated with only one resource. The value of this parameter must be in the RV[Number] format, where Number is `01 to 99`.
        self.location_id = location_id
        # The ID of the material from the media library.
        # 
        # **
        # 
        # **Important** This parameter takes effect and is required only if the video source is a material.
        # 
        # If you query the configurations of the production studio by calling the [DescribeCasterConfig](https://help.aliyun.com/document_detail/60259.html) operation, obtain the value of the response parameter UrgentMaterialId.
        # 
        # > The value of the UrgentMaterialId parameter is the ID of the material from the media library.
        self.material_id = material_id
        self.owner_id = owner_id
        # The interval between presentation timestamp (PTS) callbacks. Unit: milliseconds.
        self.pts_callback_interval = pts_callback_interval
        self.region_id = region_id
        # The number of playbacks after the first playback is complete. Valid values:
        # 
        # **
        # 
        # **Important** This parameter takes effect only if the video source is a file.
        # 
        # *   **0**: specifies that the video source is played only once. This is the default value.
        # *   **-1**: specifies that the video source is played in loop mode.
        self.repeat_num = repeat_num
        # The name of the video source.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The URL of the VOD file.
        # 
        # **
        # 
        # **Important** This parameter takes effect only if the video source is a file that is not from the media library.
        # 
        # > The VOD file must be in the MP4, FLV, or TS format.
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

        if self.fixed_delay_duration is not None:
            result['FixedDelayDuration'] = self.fixed_delay_duration

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.live_stream_url is not None:
            result['LiveStreamUrl'] = self.live_stream_url

        if self.location_id is not None:
            result['LocationId'] = self.location_id

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

        if m.get('FixedDelayDuration') is not None:
            self.fixed_delay_duration = m.get('FixedDelayDuration')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('LiveStreamUrl') is not None:
            self.live_stream_url = m.get('LiveStreamUrl')

        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

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

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')

        return self

