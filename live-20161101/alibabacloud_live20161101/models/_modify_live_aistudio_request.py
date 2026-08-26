# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ModifyLiveAIStudioRequest(DaraModel):
    def __init__(
        self,
        background_resource_id: str = None,
        background_resource_url: str = None,
        background_type: str = None,
        description: str = None,
        height: int = None,
        matting_layout: main_models.ModifyLiveAIStudioRequestMattingLayout = None,
        matting_type: str = None,
        media_layout: main_models.ModifyLiveAIStudioRequestMediaLayout = None,
        media_resource_id: str = None,
        media_resource_url: str = None,
        media_type: str = None,
        owner_id: int = None,
        region_id: str = None,
        studio_name: str = None,
        width: int = None,
    ):
        # VOD resource ID of the background material, obtained from the VOD console.
        self.background_resource_id = background_resource_id
        # Resource access URL of the background material.
        self.background_resource_url = background_resource_url
        # Background material type:
        # - VOD: Video on demand
        # - PIC: Image
        # - LIVE: Live stream
        self.background_type = background_type
        # Custom description.
        self.description = description
        # Preview screen height, unit: px.
        # 
        # The preview screen width x height only supports the following specifications:
        # 
        # - Landscape Smooth 360P 640x360
        # - Portrait Smooth 360P 360x640
        # - Landscape Standard Definition 480P 854x480
        # - Portrait Standard Definition 480P 480x854
        # - Landscape HD 720P 1280x720
        # - Portrait HD 720P 720x1280
        # - Landscape Full HD 1080P 1920x1080
        # - Portrait Full HD 1080P 1080x1920
        self.height = height
        # Layout position information of the source stream after matting.
        # 
        # This parameter is required.
        self.matting_layout = matting_layout
        # Matting type:
        # - green: Green screen matting
        # - blue: Blue screen matting
        # - complex: Real-scene matting
        # 
        # This parameter is required.
        self.matting_type = matting_type
        # Layout position information of the multimedia material.
        self.media_layout = media_layout
        # VOD resource ID of the multimedia material, obtained from the VOD console.
        self.media_resource_id = media_resource_id
        # Resource access URL of the multimedia material. Either this or the resource ID should be provided.
        self.media_resource_url = media_resource_url
        # Multimedia material type:
        # - VOD: Video on demand
        # - PIC: Image
        # - LIVE: Live stream
        self.media_type = media_type
        self.owner_id = owner_id
        # Region ID.
        self.region_id = region_id
        # Virtual studio template name, same as the StudioName parameter in the create API.
        # 
        # This parameter is required.
        self.studio_name = studio_name
        # Preview screen width, unit: px.
        self.width = width

    def validate(self):
        if self.matting_layout:
            self.matting_layout.validate()
        if self.media_layout:
            self.media_layout.validate()

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

        if self.matting_layout is not None:
            result['MattingLayout'] = self.matting_layout.to_map()

        if self.matting_type is not None:
            result['MattingType'] = self.matting_type

        if self.media_layout is not None:
            result['MediaLayout'] = self.media_layout.to_map()

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
            temp_model = main_models.ModifyLiveAIStudioRequestMattingLayout()
            self.matting_layout = temp_model.from_map(m.get('MattingLayout'))

        if m.get('MattingType') is not None:
            self.matting_type = m.get('MattingType')

        if m.get('MediaLayout') is not None:
            temp_model = main_models.ModifyLiveAIStudioRequestMediaLayout()
            self.media_layout = temp_model.from_map(m.get('MediaLayout'))

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

class ModifyLiveAIStudioRequestMediaLayout(DaraModel):
    def __init__(
        self,
        height_normalized: float = None,
        position_x: float = None,
        position_y: float = None,
    ):
        # Normalized height value of the material, which is the height ratio of the material to the background. Value range: **0~1**.
        self.height_normalized = height_normalized
        # Position parameter, X coordinate. Value range: **0~1**. The material position uses the upper-left corner as the reference point.
        self.position_x = position_x
        # Position parameter, Y coordinate. Value range: **0~1**. The material position uses the upper-left corner as the reference point.
        self.position_y = position_y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height_normalized is not None:
            result['HeightNormalized'] = self.height_normalized

        if self.position_x is not None:
            result['PositionX'] = self.position_x

        if self.position_y is not None:
            result['PositionY'] = self.position_y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeightNormalized') is not None:
            self.height_normalized = m.get('HeightNormalized')

        if m.get('PositionX') is not None:
            self.position_x = m.get('PositionX')

        if m.get('PositionY') is not None:
            self.position_y = m.get('PositionY')

        return self

class ModifyLiveAIStudioRequestMattingLayout(DaraModel):
    def __init__(
        self,
        height_normalized: float = None,
        position_x: float = None,
        position_y: float = None,
    ):
        # Normalized height value, which is the height ratio of the matted portrait to the background. Value range: **0~1**.
        self.height_normalized = height_normalized
        # Position parameter, X coordinate. Value range: **0~1**. The material position uses the upper-left corner as the reference point.
        self.position_x = position_x
        # Position parameter, Y coordinate. Value range: **0~1**. The material position uses the upper-left corner as the reference point.
        self.position_y = position_y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height_normalized is not None:
            result['HeightNormalized'] = self.height_normalized

        if self.position_x is not None:
            result['PositionX'] = self.position_x

        if self.position_y is not None:
            result['PositionY'] = self.position_y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeightNormalized') is not None:
            self.height_normalized = m.get('HeightNormalized')

        if m.get('PositionX') is not None:
            self.position_x = m.get('PositionX')

        if m.get('PositionY') is not None:
            self.position_y = m.get('PositionY')

        return self

