# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterVideoResourcesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total: int = None,
        video_resources: main_models.DescribeCasterVideoResourcesResponseBodyVideoResources = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total = total
        # The input sources.
        self.video_resources = video_resources

    def validate(self):
        if self.video_resources:
            self.video_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        if self.video_resources is not None:
            result['VideoResources'] = self.video_resources.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('VideoResources') is not None:
            temp_model = main_models.DescribeCasterVideoResourcesResponseBodyVideoResources()
            self.video_resources = temp_model.from_map(m.get('VideoResources'))

        return self

class DescribeCasterVideoResourcesResponseBodyVideoResources(DaraModel):
    def __init__(
        self,
        video_resource: List[main_models.DescribeCasterVideoResourcesResponseBodyVideoResourcesVideoResource] = None,
    ):
        self.video_resource = video_resource

    def validate(self):
        if self.video_resource:
            for v1 in self.video_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoResource'] = []
        if self.video_resource is not None:
            for k1 in self.video_resource:
                result['VideoResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_resource = []
        if m.get('VideoResource') is not None:
            for k1 in m.get('VideoResource'):
                temp_model = main_models.DescribeCasterVideoResourcesResponseBodyVideoResourcesVideoResource()
                self.video_resource.append(temp_model.from_map(k1))

        return self

class DescribeCasterVideoResourcesResponseBodyVideoResourcesVideoResource(DaraModel):
    def __init__(
        self,
        begin_offset: int = None,
        end_offset: int = None,
        flv_url: str = None,
        image_id: str = None,
        image_url: str = None,
        live_stream_url: str = None,
        location_id: str = None,
        material_id: str = None,
        pts_callback_interval: int = None,
        repeat_num: int = None,
        resource_id: str = None,
        resource_name: str = None,
        vod_url: str = None,
    ):
        # The offset of the position where the system starts to read the video resource. This parameter takes effect only if the input source is a video file. Unit: milliseconds.
        # 
        # A value **greater than 0** indicates an offset from the first frame.
        self.begin_offset = begin_offset
        # The offset of the position where the system stops reading the video file. This parameter takes effect only if the input source is a video file. Unit: milliseconds.
        # 
        # *   A value greater than **0** indicates an offset from the first frame.
        # *   A value smaller than **0** indicates an offset from the last frame.
        self.end_offset = end_offset
        # The source URL.
        self.flv_url = flv_url
        # The image ID.
        self.image_id = image_id
        # The image URL.
        self.image_url = image_url
        # The URL of the live stream.
        self.live_stream_url = live_stream_url
        # The position of the video resource.
        self.location_id = location_id
        # The material ID.
        self.material_id = material_id
        # The interval between presentation timestamp (PTS) callbacks. If you set the value to 0, the PTS callback is disabled. This parameter is returned only when the video resource is a video-on-demand (VOD) file.
        self.pts_callback_interval = pts_callback_interval
        # The number of playback times after the first playback is complete. This parameter takes effect only when the input source is a video file. Valid values:
        # 
        # *   **0** (default): The video file is played only once.
        # *   **-1**: The video file is played in loop mode.
        self.repeat_num = repeat_num
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The URL of the VOD file.
        # 
        # This parameter is returned only when the video resource is an MP4, FLV, or TS file that is not from the media library.
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

        if self.end_offset is not None:
            result['EndOffset'] = self.end_offset

        if self.flv_url is not None:
            result['FlvUrl'] = self.flv_url

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

        if self.pts_callback_interval is not None:
            result['PtsCallbackInterval'] = self.pts_callback_interval

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

        if m.get('EndOffset') is not None:
            self.end_offset = m.get('EndOffset')

        if m.get('FlvUrl') is not None:
            self.flv_url = m.get('FlvUrl')

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

        if m.get('PtsCallbackInterval') is not None:
            self.pts_callback_interval = m.get('PtsCallbackInterval')

        if m.get('RepeatNum') is not None:
            self.repeat_num = m.get('RepeatNum')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')

        return self

