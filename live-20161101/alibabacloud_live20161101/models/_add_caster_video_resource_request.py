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
        # The start offset of the video file. Unit: milliseconds.
        # >Notice: This parameter takes effect only when the video source type is file video.
        # 
        # 
        # > A value greater than **0** indicates that reading starts from the offset time relative to the first frame.
        self.begin_offset = begin_offset
        # The production studio ID.
        # 
        # - If you created the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the CasterId parameter value returned by the CreateCaster operation.
        # 
        # - If you created the production studio in the ApsaraVideo Live console, navigate to **ApsaraVideo Live console** > **Production Studios** > **Cloud Production Studio** to view the production studio name.
        # 
        # > The production studio name in the production studio list on the Cloud Production Studio page of the ApsaraVideo Live console is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The end offset of the video file. Unit: milliseconds.
        # >Notice: This parameter takes effect only when the video source type is file video.
        # 
        #         
        # - A value greater than **0**: reading ends at the offset time relative to the first frame.
        # - A value less than **0**: reading ends at the offset time relative to the last frame.
        self.end_offset = end_offset
        # The fixed delay for the video, which can be used for subtitle synchronization. Unit: ms. Default value: 0. Value range: `[0-5000]`.
        self.fixed_delay_duration = fixed_delay_duration
        # The media asset library image material ID.
        # > This parameter is available and required only when the video source type is image.
        self.image_id = image_id
        # The image material URL.
        # >This parameter is available only when the video source type is image and the image file has not been imported to the media asset library. JPG and PNG formats are supported. The maximum file size is 10 MB.
        self.image_url = image_url
        # The ApsaraVideo Live streaming URL.
        # 
        # >Notice:  
        #  
        # -  This parameter is required when the video source type is live stream.
        #  
        # -  Do not include this parameter in the request when the video source type is not live stream.
        self.live_stream_url = live_stream_url
        # The location identifier of the video source. This parameter is required. 
        # 
        # Defines the reference number of a scene in the layout. Each location can be associated with at most one resource. The format must match "RV01~RV12", which is RV + a number in the range of `[01~99]`.
        self.location_id = location_id
        # The media asset library material ID.
        # >Notice: This parameter is available and required only when the video source type is material.
        # 
        # 
        # If you call the [DescribeCasterConfig](https://help.aliyun.com/document_detail/2848011.html) operation to query the production studio configuration, check the UrgentMaterialId parameter value returned by the DescribeCasterConfig operation.
        # 
        # > The UrgentMaterialId value is the media asset library material ID.
        self.material_id = material_id
        self.owner_id = owner_id
        # The PTS callback interval. Unit: milliseconds.
        self.pts_callback_interval = pts_callback_interval
        # The region ID.
        self.region_id = region_id
        # The number of times the video repeats after playback completes. Valid values:
        # >Notice: This parameter takes effect only when the video source type is file video.
        # 
        # 
        # - **0** (default): no repeat.
        # - **-1**: loops indefinitely.
        self.repeat_num = repeat_num
        # The name of the video source.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The video-on-demand file URL.
        # >Notice: This parameter is available only when the video source type is file video and the video file has not been imported to the media asset library.
        # 
        # 
        # >Video-on-demand files are limited to MP4, FLV, and TS formats.
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

