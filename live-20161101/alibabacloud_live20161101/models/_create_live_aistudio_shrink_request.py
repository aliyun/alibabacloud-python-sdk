# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveAIStudioShrinkRequest(DaraModel):
    def __init__(
        self,
        background_resource_id: str = None,
        background_resource_url: str = None,
        background_type: str = None,
        description: str = None,
        height: int = None,
        matting_layout_shrink: str = None,
        matting_type: str = None,
        media_layout_shrink: str = None,
        media_resource_id: str = None,
        media_resource_url: str = None,
        media_type: str = None,
        owner_id: int = None,
        region_id: str = None,
        studio_name: str = None,
        width: int = None,
    ):
        # The video-on-demand resource ID of the background material. Obtain this value from the ApsaraVideo VOD console.
        self.background_resource_id = background_resource_id
        # The access URL of the background material. Specify either this parameter or the resource ID.
        self.background_resource_url = background_resource_url
        # The type of the background material. Valid values:
        # - VOD: video-on-demand video.
        # - PIC: image.
        # - LIVE: live stream.
        self.background_type = background_type
        # The custom description.
        self.description = description
        # The height of the preview screen. Unit: px.
        # 
        # The width × height of the preview screen supports only the following specifications:
        # 
        # - Landscape low definition 360P: 640 × 360
        # - Portrait low definition 360P: 360 × 640
        # - Landscape standard definition 480P: 854 × 480
        # - Portrait standard definition 480P: 480 × 854
        # - Landscape high definition 720P: 1280 × 720
        # - Portrait high definition 720P: 720 × 1280
        # - Landscape ultra-high definition 1080P: 1920 × 1080
        # - Portrait ultra-high definition 1080P: 1080 × 1920.
        self.height = height
        # The layout position information of the source stream after image matting.
        # 
        # This parameter is required.
        self.matting_layout_shrink = matting_layout_shrink
        # The image matting type. Valid values:
        # - green: green screen matting.
        # - blue: blue screen matting.
        # - complex: real-scene matting.
        # 
        # This parameter is required.
        self.matting_type = matting_type
        # The layout position information of the multimedia material.
        self.media_layout_shrink = media_layout_shrink
        # The video-on-demand resource ID of the multimedia material. Obtain this value from the ApsaraVideo VOD console.
        self.media_resource_id = media_resource_id
        # The access URL of the multimedia material. Specify either this parameter or the resource ID.
        self.media_resource_url = media_resource_url
        # The type of the multimedia material. Valid values:
        # - VOD: video-on-demand video.
        # - PIC: image.
        # - LIVE: live stream.
        self.media_type = media_type
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The name of the virtual studio template. The name must be unique.
        # 
        # This parameter is required.
        self.studio_name = studio_name
        # The width of the preview screen. Unit: px.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_resource_id is not None:
            result['BackgroundResourceId'] = self.background_resource_id

        if self.background_resource_url is not None:
            result['BackgroundResourceUrl'] = self.background_resource_url

        if self.background_type is not None:
            result['BackgroundType'] = self.background_type

        if self.description is not None:
            result['Description'] = self.description

        if self.height is not None:
            result['Height'] = self.height

        if self.matting_layout_shrink is not None:
            result['MattingLayout'] = self.matting_layout_shrink

        if self.matting_type is not None:
            result['MattingType'] = self.matting_type

        if self.media_layout_shrink is not None:
            result['MediaLayout'] = self.media_layout_shrink

        if self.media_resource_id is not None:
            result['MediaResourceId'] = self.media_resource_id

        if self.media_resource_url is not None:
            result['MediaResourceUrl'] = self.media_resource_url

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.studio_name is not None:
            result['StudioName'] = self.studio_name

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundResourceId') is not None:
            self.background_resource_id = m.get('BackgroundResourceId')

        if m.get('BackgroundResourceUrl') is not None:
            self.background_resource_url = m.get('BackgroundResourceUrl')

        if m.get('BackgroundType') is not None:
            self.background_type = m.get('BackgroundType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MattingLayout') is not None:
            self.matting_layout_shrink = m.get('MattingLayout')

        if m.get('MattingType') is not None:
            self.matting_type = m.get('MattingType')

        if m.get('MediaLayout') is not None:
            self.media_layout_shrink = m.get('MediaLayout')

        if m.get('MediaResourceId') is not None:
            self.media_resource_id = m.get('MediaResourceId')

        if m.get('MediaResourceUrl') is not None:
            self.media_resource_url = m.get('MediaResourceUrl')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StudioName') is not None:
            self.studio_name = m.get('StudioName')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

