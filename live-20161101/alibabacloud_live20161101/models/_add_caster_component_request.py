# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCasterComponentRequest(DaraModel):
    def __init__(
        self,
        caption_layer_content: str = None,
        caster_id: str = None,
        component_layer: str = None,
        component_name: str = None,
        component_type: str = None,
        effect: str = None,
        html_layer_content: str = None,
        image_layer_content: str = None,
        layer_order: str = None,
        location_id: str = None,
        owner_id: int = None,
        region_id: str = None,
        text_layer_content: str = None,
    ):
        # The properties of the layer element. The properties are described as follows:
        # >Notice: This parameter is required when ComponentType is set to caption.
        # 
        # - **SizeNormalized**: The normalized font size. This value is calculated as font size / output height. The value must be in the `[0,1]` range and accurate to two decimal places. If the font size calculated from the normalized value is greater than **1024**, the font size is set to **1024**.
        # 
        # - **BorderWidthNormalized**: The normalized width of the text border. This value is calculated based on the font size: BorderWidth / FontSize. The value must be in the `[0,1]` range and accurate to two decimal places. If the width calculated from the normalized value is greater than **16**, the width is set to **16**. The default value is **0**.
        # 
        # - **FontName**: The font name. For valid values, see **Production studio fonts**. The default font is KaiTi.
        # 
        # - **BorderColor**: The color of the text border. The value must be a hexadecimal color code that ranges from 0x000000 to 0xffffff. The default value is an empty string (""), which indicates that no border color is set.
        # 
        # - **LocationId**: The channel ID of the translation source.
        # 
        # - **SourceLan**: The original audio language of the video source. Valid values: en (English), cn (Chinese), es (Spanish), and ru (Russian). The default value is cn.
        # 
        # - **TargetLan**: The target audio language for the video source. If you do not set this parameter, only speech recognition is performed. If you set this parameter, the audio is translated. Valid values: en (English), cn (Chinese), es (Spanish), and ru (Russian).
        # 
        # - **ShowSourceLan**: Specifies whether to display the source language. Valid values: true and false. The default value is false.
        # 
        # - **Truncation**: Specifies whether captions can be truncated. Valid values: true and false. The default value is false.
        # 
        # - **SourceLanPerLineWordCount**: The maximum number of words per line for the source language captions. The default value is 20.
        # 
        # - **TargetLanPerLineWordCount**: The maximum number of words per line for the target language captions. The default value is 20.
        # 
        # - **SourceLanReservePages**: The number of lines to reserve for the source language captions. This parameter takes effect only when Truncation is set to true. The default value is 2.
        # 
        # - **TargetLanReservePages**: The number of lines to reserve for the target language captions. This parameter takes effect only when Truncation is set to true. The default value is 2.
        # 
        # The value must be a JSON-formatted string. Parameter names must be in upper-camel case.
        self.caption_layer_content = caption_layer_content
        # The ID of the production studio.
        # 
        # - If you create the production studio by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, find the ID in the CasterId parameter of the response.
        # 
        # - If you create the production studio in the LIVE console, go to the **LIVE Console** > **Production Studio** > **Cloud Production Studio** page to view the ID.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The size, layout, and other information about the component layer. The elements are described as follows:
        # 
        # - **HeightNormalized**: The normalized height.
        # 
        # - **WidthNormalized**: The normalized width.
        # 
        # - **PositionNormalized**: The normalized position of the layer element.
        # 
        # - **PositionRefer**: The reference coordinates for the element\\"s position.
        # 
        # The value is a JSON-formatted string. Parameter names must be in upper-camel case.
        # 
        # This parameter is required.
        self.component_layer = component_layer
        # The name of the component. The default value is the component ID.
        self.component_name = component_name
        # The type of component. Valid values:
        # 
        # - **text**: A text component. If you set this parameter to text, you must also set the TextLayerContent parameter.
        # 
        # - **image**: An image component. If you set this parameter to image, you must also set the ImageLayerContent parameter.
        # 
        # - **caption**: A caption component. If you set this parameter to caption, you must also set the CaptionLayerContent parameter.
        # 
        # This parameter is required.
        self.component_type = component_type
        # The display effect of the component. Valid values:
        # 
        # - **none** (default): No effect.
        # 
        # - **animateH**: Scrolls horizontally.
        # 
        # - **animateV**: Scrolls vertically.
        self.effect = effect
        # The configuration of the H5 component.
        self.html_layer_content = html_layer_content
        # The properties of the layer element. The properties are described as follows:
        # 
        # >Notice: 
        # 
        # This parameter is required when ComponentType is set to image.
        # 
        # 
        # 
        # MaterialId: The ID of the media asset. The name that you specify when you upload a media asset is used as the ID of the media asset.
        # 
        # The value must be a JSON-formatted string. Parameter names must be in upper-camel case.
        self.image_layer_content = image_layer_content
        # The layer order of the component.
        # 
        # - cover: The component is in the foreground.
        # 
        # - background: The component is in the background.
        self.layer_order = layer_order
        # Specifies the position of the component. Each position can hold only one component. The format must be RC01 to RC99.
        # 
        # > If the component type is caption, this parameter specifies the location of the referenced video source.
        # 
        # This parameter is required.
        self.location_id = location_id
        self.owner_id = owner_id
        # The ID of the region.
        self.region_id = region_id
        # The properties of the layer element. The properties are described as follows:
        # >Notice: This parameter is required only when ComponentType is set to text.
        # 
        # - **SizeNormalized**: The normalized font size. This value is calculated as font size / output height. The value must be in the `[0,1]` range. If the font size calculated from the normalized value is greater than 1024, the font size is set to 1024.
        # 
        # - **BorderWidthNormalized**: The normalized width of the text border. This value is calculated based on the font size: BorderWidth / FontSize. The value must be in the `[0,1]` range. If the width calculated from the normalized value is greater than 16, the width is set to 16. The default value is 0.
        # 
        # - **FontName**: The font name. For valid values, see **Production studio fonts**. The default font is KaiTi.
        # 
        # - **BorderColor**: The color of the text border. The value must be a hexadecimal color code that ranges from 0x000000 to 0xffffff. The default value is an empty string (""), which indicates that no border color is set.
        # 
        # - **Text**: The text content. The default value is an empty string ("").
        # 
        # - **Color**: The text color. The default value is 0xff0000, which represents red.
        # 
        # The value must be a JSON-formatted string. Parameter names must be in upper-camel case.
        self.text_layer_content = text_layer_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption_layer_content is not None:
            result['CaptionLayerContent'] = self.caption_layer_content

        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.component_layer is not None:
            result['ComponentLayer'] = self.component_layer

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.effect is not None:
            result['Effect'] = self.effect

        if self.html_layer_content is not None:
            result['HtmlLayerContent'] = self.html_layer_content

        if self.image_layer_content is not None:
            result['ImageLayerContent'] = self.image_layer_content

        if self.layer_order is not None:
            result['LayerOrder'] = self.layer_order

        if self.location_id is not None:
            result['LocationId'] = self.location_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.text_layer_content is not None:
            result['TextLayerContent'] = self.text_layer_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptionLayerContent') is not None:
            self.caption_layer_content = m.get('CaptionLayerContent')

        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('ComponentLayer') is not None:
            self.component_layer = m.get('ComponentLayer')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('HtmlLayerContent') is not None:
            self.html_layer_content = m.get('HtmlLayerContent')

        if m.get('ImageLayerContent') is not None:
            self.image_layer_content = m.get('ImageLayerContent')

        if m.get('LayerOrder') is not None:
            self.layer_order = m.get('LayerOrder')

        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TextLayerContent') is not None:
            self.text_layer_content = m.get('TextLayerContent')

        return self

