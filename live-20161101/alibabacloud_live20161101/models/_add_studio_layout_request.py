# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddStudioLayoutRequest(DaraModel):
    def __init__(
        self,
        bg_image_config: str = None,
        caster_id: str = None,
        common_config: str = None,
        layer_order_config_list: str = None,
        layout_name: str = None,
        layout_type: str = None,
        media_input_config_list: str = None,
        owner_id: int = None,
        region_id: str = None,
        screen_input_config_list: str = None,
    ):
        # The configuration of the background resource. The value is a JSON string. For more information, see **BgImageConfig**.
        # 
        # >Notice: 
        # 
        # This parameter is required only when you set LayoutType to studio.
        self.bg_image_config = bg_image_config
        # The ID of the production studio.
        # 
        # >Notice: 
        # 
        # Create a virtual production studio in advance. You can create a production studio in the console or by calling the [CreateCaster](https://help.aliyun.com/document_detail/69338.html) API operation. The production studio must be a virtual production studio.
        # 
        # 
        # 
        # - If you call the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) API operation to create a production studio, use the returned CasterId value.
        # 
        # - If you create a production studio in the ApsaraVideo Live console, go to the **ApsaraVideo Live console** > **Production Studio** > **Cloud Production Studio** page. The name of the production studio in the list is its ID.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The configuration of the common layout. The value is a JSON string. For more information, see **CommonConfig**.
        # 
        # >Notice: 
        # 
        # This parameter is required only when you set LayoutType to common.
        self.common_config = common_config
        # The layer order settings. The value is a JSON string. For more information, see **LayerOrderConfig**. You can sort background materials and multimedia materials. Chroma keying layers are not supported. The earlier a material appears in the list, the lower its layer.
        self.layer_order_config_list = layer_order_config_list
        # The name of the studio layout.
        # 
        # This parameter is required.
        self.layout_name = layout_name
        # The type of the studio layout. Valid values:
        # 
        # - **common**: A common layout. If you set LayoutType to common, you must also specify CommonConfig.
        # 
        # - **studio**: A studio layout. If you set LayoutType to studio, you must also specify BgImageConfig and ScreenInputConfigList. The MediaInputConfigList parameter is optional.
        # 
        # This parameter is required.
        self.layout_type = layout_type
        # The settings for the multimedia input resource. The value is a JSON string. For more information, see **MediaInputConfig**.
        # 
        # >Notice: 
        # 
        # This parameter is valid and optional only when you set LayoutType to studio.
        self.media_input_config_list = media_input_config_list
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The settings for the chroma keying input. The value is a JSON string. For more information, see **ScreenInputConfig**.
        # 
        # >Notice: 
        # 
        # This parameter is required only when you set LayoutType to studio.
        self.screen_input_config_list = screen_input_config_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bg_image_config is not None:
            result['BgImageConfig'] = self.bg_image_config

        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.common_config is not None:
            result['CommonConfig'] = self.common_config

        if self.layer_order_config_list is not None:
            result['LayerOrderConfigList'] = self.layer_order_config_list

        if self.layout_name is not None:
            result['LayoutName'] = self.layout_name

        if self.layout_type is not None:
            result['LayoutType'] = self.layout_type

        if self.media_input_config_list is not None:
            result['MediaInputConfigList'] = self.media_input_config_list

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.screen_input_config_list is not None:
            result['ScreenInputConfigList'] = self.screen_input_config_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgImageConfig') is not None:
            self.bg_image_config = m.get('BgImageConfig')

        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('CommonConfig') is not None:
            self.common_config = m.get('CommonConfig')

        if m.get('LayerOrderConfigList') is not None:
            self.layer_order_config_list = m.get('LayerOrderConfigList')

        if m.get('LayoutName') is not None:
            self.layout_name = m.get('LayoutName')

        if m.get('LayoutType') is not None:
            self.layout_type = m.get('LayoutType')

        if m.get('MediaInputConfigList') is not None:
            self.media_input_config_list = m.get('MediaInputConfigList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScreenInputConfigList') is not None:
            self.screen_input_config_list = m.get('ScreenInputConfigList')

        return self

