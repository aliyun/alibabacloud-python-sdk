# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyStudioLayoutRequest(DaraModel):
    def __init__(
        self,
        bg_image_config: str = None,
        caster_id: str = None,
        common_config: str = None,
        layer_order_config_list: str = None,
        layout_id: str = None,
        layout_name: str = None,
        media_input_config_list: str = None,
        owner_id: int = None,
        region_id: str = None,
        screen_input_config_list: str = None,
    ):
        # The configuration of the background resource. This parameter is a JSON string. For more information, see **BgImageConfig**.
        # 
        # >Notice: 
        # 
        # This parameter is required only when LayoutType is set to studio.
        self.bg_image_config = bg_image_config
        # The ID of the production studio. >Notice: The production studio must be created in advance and must be of the virtual studio type.
        # 
        # - If you create a production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, use the CasterId value returned in the response.
        # 
        # - If you create a production studio in the ApsaraVideo Live console, go to the **ApsaraVideo Live console** > **Production Studio** > **Cloud Production Studio** page to view the ID.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The configuration of the common layout. This parameter is a JSON string. For more information, see **CommonConfig**. >Notice: This parameter is required only when LayoutType is set to common.
        self.common_config = common_config
        # The layer order settings. This parameter is a JSON string. For more information, see **layerOrderConfig**. You can sort background and multimedia materials. Chroma keying layers are not supported. The earlier an item appears in the list, the lower its layer.
        self.layer_order_config_list = layer_order_config_list
        # The ID of the layout. If you add a layout for a production studio by calling the [AddStudioLayout](https://help.aliyun.com/document_detail/2848062.html) operation, use the LayoutId value returned in the response.
        # 
        # This parameter is required.
        self.layout_id = layout_id
        # The name of the production studio layout.
        self.layout_name = layout_name
        # The settings for the multimedia input resource. This parameter is a JSON string. For more information, see **MediaInputConfig**.
        # 
        # >Notice: 
        # 
        # This parameter is valid and optional only when LayoutType is set to studio.
        self.media_input_config_list = media_input_config_list
        self.owner_id = owner_id
        # The ID of the region.
        self.region_id = region_id
        # The settings for the chroma keying input. This parameter is a JSON string. For more information, see **ScreenInputConfig**.
        # 
        # >Notice: 
        # 
        # This parameter is required only when LayoutType is set to studio.
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

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.layout_name is not None:
            result['LayoutName'] = self.layout_name

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

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('LayoutName') is not None:
            self.layout_name = m.get('LayoutName')

        if m.get('MediaInputConfigList') is not None:
            self.media_input_config_list = m.get('MediaInputConfigList')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScreenInputConfigList') is not None:
            self.screen_input_config_list = m.get('ScreenInputConfigList')

        return self

