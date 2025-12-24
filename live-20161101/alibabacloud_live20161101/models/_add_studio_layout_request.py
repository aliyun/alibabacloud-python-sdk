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
        # The background material configurations. The value is a JSON string. For more information, see **BgImageConfig**.
        # 
        # >  This parameter is required only if you set LayoutType to studio.
        self.bg_image_config = bg_image_config
        # The ID of the production studio.
        # 
        # >  The production studio must be a virtual studio that you create in advance. You can use the ApsaraVideo Live console or call the CreateCaster operation to create a virtual studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The common layout configurations. The value is a JSON string. For more information, see **CommonConfig**.
        # 
        # >  This parameter is required only if you set LayoutType to common.
        self.common_config = common_config
        # The layer sorting configurations. The value is a JSON string. For more information, see **layerOrderConfig**. You can sort layers of background and multimedia materials. The chroma key layer cannot be sorted. A layer that is in the front of the code is placed behind other layers in the layout.
        self.layer_order_config_list = layer_order_config_list
        # The name of the layout.
        # 
        # This parameter is required.
        self.layout_name = layout_name
        # The type of the layout. Valid values:
        # 
        # *   **common**: If you set this parameter to common, you must specify the CommonConfig parameter.
        # *   **studio**: If you set this parameter to studio, you must specify the BgImageConfig and ScreenInputConfigList parameters. The MediaInputConfigList parameter is optional.
        # 
        # This parameter is required.
        self.layout_type = layout_type
        # The multimedia input configurations. The value is a JSON string. For more information, see **MediaInputConfig**.
        # 
        # >  This parameter is optional and is valid only if you set LayoutType to studio.
        self.media_input_config_list = media_input_config_list
        self.owner_id = owner_id
        self.region_id = region_id
        # The input configurations for chroma key. The value is a JSON string. For more information, see **ScreenInputConfig**.
        # 
        # >  This parameter is required only if you set LayoutType to studio.
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

