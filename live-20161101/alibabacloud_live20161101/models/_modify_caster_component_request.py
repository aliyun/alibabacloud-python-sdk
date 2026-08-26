# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCasterComponentRequest(DaraModel):
    def __init__(
        self,
        caption_layer_content: str = None,
        caster_id: str = None,
        component_id: str = None,
        component_layer: str = None,
        component_name: str = None,
        component_type: str = None,
        effect: str = None,
        image_layer_content: str = None,
        owner_id: int = None,
        region_id: str = None,
        text_layer_content: str = None,
    ):
        # The properties of the caption layer. The value is a JSON string. The following properties are supported:
        # 
        # >Notice: 
        # 
        # This parameter is required if you set ComponentType to caption.
        # 
        # 
        # 
        # - **SizeNormalized**: The normalized font size. The font size is calculated using the formula: font_size/output_height. The value must be in the range of `[0,1]`. If the calculated font size is greater than 1024, the value 1024 is used.
        # 
        # - **BorderWidthNormalized**: The normalized width of the text border. The normalized width is calculated based on the font size using the formula: BorderWidth/FontSize. The value must be in the range of `[0,1]`. If the calculated value is greater than 16, the value 16 is used. Default value: 0.
        # 
        # - **FontName**: The font name. For more information about valid values, see **Production studio fonts**. Default value: KaiTi.
        # 
        # - **BorderColor**: The color of the text border. Valid values are from 0x000000 to 0xffffff. The default value is an empty string, which indicates that this parameter is not used.
        # 
        # - **LocationId**: The channel ID of the translation source.
        # 
        # - **SourceLan**: The source language of the audio in the video source. Valid values are en (English), cn (Chinese), es (Spanish), and ru (Russian). Default value: cn.
        # 
        # - **TargetLan**: The target language for translation. If you do not set this parameter, only speech recognition is performed. If you set this parameter, translation is also performed. Valid values are en (English), cn (Chinese), es (Spanish), and ru (Russian).
        # 
        # - **ShowSourceLan**: Specifies whether to display the source language. Valid values are true (display) and false (do not display). Default value: false.
        # 
        # - **Truncation**: Specifies whether to truncate the caption. Valid values are true (truncate) and false (do not truncate). Default value: false.
        # 
        # - **SourceLanPerLineWordCount**: The number of words per line for the source language. This parameter takes effect only if Truncation is set to true. Default value: 20.
        # 
        # - **TargetLanPerLineWordCount**: The number of words per line for the target language. This parameter takes effect only if Truncation is set to true. Default value: 20.
        self.caption_layer_content = caption_layer_content
        # The ID of the production studio.
        # 
        # - The ID is returned after you call the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation.
        # 
        # - If you create a production studio in the LIVE console, go to the **LIVE** > **Production Studio** > **Cloud Production Studio** page to find the ID.
        # 
        # > The name of the production studio in the list on the Cloud Production Studio page is the production studio ID.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The component ID. The ID is returned after you call the [AddCasterComponent](https://help.aliyun.com/document_detail/2848030.html) operation.
        # 
        # This parameter is required.
        self.component_id = component_id
        # The size and layout of the layer. The value is a JSON string. The following properties are supported:
        # 
        # - **HeightNormalized**: The normalized height.
        # 
        # - **WidthNormalized**: The normalized width.
        # 
        # - **PositionNormalized**: The normalized position of the layer.
        # 
        # - **PositionRefer**: The reference point for the position of the layer.
        self.component_layer = component_layer
        # The name of the component. The default value is the component ID.
        self.component_name = component_name
        # The type of the component. Valid values:
        # 
        # - **text**: A text component. The TextLayerContent parameter is required only if you set ComponentType to text.
        # 
        # - **image**: An image component. The ImageLayerContent parameter is required only if you set ComponentType to image.
        # 
        # - **caption**: A translation caption component. The CaptionLayerContent parameter is required only if you set ComponentType to caption.
        self.component_type = component_type
        # The display effect of the component. Valid values:
        # 
        # - **none** (default): no effect.
        # 
        # - **animateH**: horizontal scroll.
        # 
        # - **animateV**: vertical scroll.
        self.effect = effect
        # The properties of the image layer. The value is a JSON string.
        # 
        # >Notice: 
        # 
        # This parameter is required if you set ComponentType to image.
        # 
        # 
        # 
        # MaterialId is the ID of the material in the media asset library.
        self.image_layer_content = image_layer_content
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The properties of the text layer. The value is a JSON string. The following properties are supported:
        # 
        # >Notice: 
        # 
        # This parameter is required if you set ComponentType to text.
        # 
        # 
        # 
        # - **SizeNormalized**: The normalized font size. The font size is calculated using the formula: font_size/output_height. The value must be in the range of `[0,1]`. If the calculated font size is greater than 1024, the value 1024 is used.
        # 
        # - **BorderWidthNormalized**: The normalized width of the text border. The normalized width is calculated based on the font size using the formula: BorderWidth/FontSize. The value must be in the range of `[0,1]`. If the calculated value is greater than 16, the value 16 is used. Default value: 0.
        # 
        # - **FontName**: The font name. For more information about valid values, see **Production studio fonts**. Default value: KaiTi.
        # 
        # - **BorderColor**: The color of the text border. Valid values are from 0x000000 to 0xffffff. The default value is an empty string, which indicates that this parameter is not used.
        # 
        # - **Text**: The text content. The default value is an empty string.
        # 
        # - **Color**: The color of the text. Default value: 0xff0000, which is red.
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

        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_layer is not None:
            result['ComponentLayer'] = self.component_layer

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.effect is not None:
            result['Effect'] = self.effect

        if self.image_layer_content is not None:
            result['ImageLayerContent'] = self.image_layer_content

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

        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentLayer') is not None:
            self.component_layer = m.get('ComponentLayer')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('ImageLayerContent') is not None:
            self.image_layer_content = m.get('ImageLayerContent')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TextLayerContent') is not None:
            self.text_layer_content = m.get('TextLayerContent')

        return self

