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
        # The information about the subtitle component. The value must be a JSON string. This parameter contains the following fields:
        # 
        # >  This parameter is required if you set ComponentType to caption.
        # 
        # *   **SizeNormalized**: the normalized value of the font size. The value of this field equals the font size divided by the output height. Valid values: `0 to 1`. The maximum font size is 1,024, even if the font size calculated based on this field is greater than 1,024.
        # *   **BorderWidthNormalized**: the normalized value of the border width. The value of this field equals the border width divided by the font size. Valid values: `0 to 1`. Default value: 0. The maximum border width is 16, even if the border width calculated based on this field is greater than 16.
        # *   **FontName**: the font name. Default value: KaiTi. For more information about the valid values, see **Fonts used in a production studio**.
        # *   **BorderColor**: the color of the text border. Valid values: 0x000000 to 0xffffff. By default, this parameter is left empty. In this case, the color of the text border is transparent.
        # *   **LocationId**: the channel ID of the source subtitles.
        # *   **SourceLan**: the source language of the subtitles in the video. Valid values: en (English), cn (Chinese), es (Spanish), and ru (Russian). Default value: cn.
        # *   **TargetLan**: the target language of the subtitles in the video. If you do not specify this field, speech recognition is used. If you specify this field, translation is used. Valid values: en (English), cn (Chinese), es (Spanish), and ru (Russian).
        # *   **ShowSourceLan**: specifies whether to display the source language. A value of true specifies that the source language is displayed. A value of false specifies that the source language is not displayed. Default value: false.
        # *   **Truncation**: specifies whether to allow subtitle truncation. A value of true specifies that the subtitles can be truncated. A value of false specifies that the subtitles cannot be truncated. Default value: false.
        # *   **SourceLanPerLineWordCount**: the number of words displayed in each line of the source language. This field takes effect only if you set Truncation to true. Default value: 20.
        # *   **TargetLanPerLineWordCount**: the number of words displayed in each line of the target language. This field takes effect only if you set Truncation to true. Default value: 20.
        self.caption_layer_content = caption_layer_content
        # The ID of the production studio.
        # 
        # *   If the production studio was created by calling the [CreateCaster](https://help.aliyun.com/document_detail/2848009.html) operation, check the value of the response parameter CasterId to obtain the ID.
        # *   If the production studio was created by using the ApsaraVideo Live console, obtain the ID on the **Production Studio Management** page. To go to the page, log on to the **ApsaraVideo Live console** and click **Production Studios** in the left-side navigation pane.
        # 
        # >  You can find the ID of the production studio in the Instance ID/Name column.
        # 
        # This parameter is required.
        self.caster_id = caster_id
        # The ID of the component. If the component was added by calling the [AddCasterComponent](https://help.aliyun.com/document_detail/2848030.html) operation, check the value of the response parameter ComponentId to obtain the ID.
        # 
        # This parameter is required.
        self.component_id = component_id
        # The information about the component layer, such as the size and layout, The value must be a JSON string. This parameter contains the following fields:
        # 
        # *   **HeightNormalized**: the normalized value of the height of the component layer.
        # *   **WidthNormalized**: the normalized value of the width of the component layer.
        # *   **PositionNormalized**: the normalized value of the position of the component layer.
        # *   **PositionRefer**: the reference coordinates of the component layer.
        self.component_layer = component_layer
        # The name of the component. By default, the name is the ID of the component.
        self.component_name = component_name
        # The type of the component. Valid values:
        # 
        # *   **text**: text component. The TextLayerContent parameter is required if you set ComponentType to text.
        # *   **image**: image component. The ImageLayerContent parameter is required if you set ComponentType to image.
        # *   **caption**: subtitle component. The CaptionLayerContent parameter is required if you set ComponentType to caption.
        self.component_type = component_type
        # The display effect for the component. Valid values:
        # 
        # *   **none** (default)
        # *   **animateH**: horizontal scrolling
        # *   **animateV**: vertical scrolling
        self.effect = effect
        # The information about the image component. The value must be a JSON string.
        # 
        # >  This parameter is required if you set ComponentType to image.
        # 
        # The MaterialId field specifies the ID of the material from the media asset library.
        self.image_layer_content = image_layer_content
        self.owner_id = owner_id
        self.region_id = region_id
        # The information about the text component. The value must be a JSON string. This parameter contains the following fields:
        # 
        # >  This parameter is required if you set ComponentType to text.
        # 
        # *   **SizeNormalized**: the normalized value of the font size. The value of this field equals the font size divided by the output height. Valid values: `0 to 1`. The maximum font size is 1,024, even if the font size calculated based on this field is greater than 1,024.
        # *   **BorderWidthNormalized**: the normalized value of the border width. The value of this field equals the border width divided by the font size. Valid values: `0 to 1`. Default value: 0. The maximum border width is 16, even if the border width calculated based on this field is greater than 16.
        # *   **FontName**: the font name. Default value: KaiTi. For more information about the valid values, see **Fonts used in a production studio**.
        # *   **BorderColor**: the color of the text border. Valid values: 0x000000 to 0xffffff. By default, this parameter is left empty. In this case, the color of the text border is transparent.
        # *   **Text**: the content of the text. By default, this parameter is left empty. In this case, the text contains no content.
        # *   **Color**: the color of the text. The default value is 0xff0000, which indicates that the text is in red.
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

