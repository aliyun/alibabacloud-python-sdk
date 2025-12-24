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
        # The information about the caption layer. This parameter contains the following fields:
        # 
        # >  This parameter is required when the ComponentType parameter is set to caption.
        # 
        # *   **SizeNormalized**: the normalized font size. The font size is set to font_size/output_height. The value range is `[0,1]` and accurate to two decimal places. If the font size calculated by the system based on the normalization method is greater than **1024**, **1024** is used.
        # *   **BorderWidthNormalized**: the normalized value of the text border width, which is calculated based on the size of the text, namely "BorderWidth/FontSize". The value range is `[0,1]` and accurate to two decimal places. If the value calculated according to the normalization method exceeds **16**, **16** is used. The default value is **0**.
        # *   **FontName**: the font name. For more information about the value, see **Font description**. The default font name is KaiTi.
        # *   **BorderColor**: the color of the text border. Valid values: 0x000000 to 0xffffff. By default, this parameter is not set. In this case, the color of the text border is transparent.
        # *   **LocationId**: the channel ID of the source subtitle.
        # *   **SourceLan**: the source language of the audio in the source video. Valid values: en, cn, es, and ru, which indicate English, Chinese, Spanish, and Russian respectively. Default value: cn.
        # *   **TargetLan**: the target audio language in the source video. If you do not specify this field, speech recognition is used. If you specify this field, translation is used. Valid values: en, cn, es, and ru, which indicate English, Chinese, Spanish, and Russian respectively. Default value: cn.
        # *   **ShowSourceLan**: specifies whether to display the source language. Valid values: true: displays the source language. false: hides the source language. Default value: false.
        # *   **Truncation**: specifies whether to allow caption truncation. Valid values: true: specifies that the caption can be truncated. false: specifies that the caption cannot be truncated. Default value: false.
        # *   **SourceLanPerLineWordCount**: the number of words displayed in each line when the subtitle is in the source language. Default value: 20.
        # *   **TargetLanPerLineWordCount**: the number of words displayed in each line when the subtitle is in the destination language. Default value: 20.
        # *   **SourceLanReservePages**: the number of lines reserved when the subtitle is in the source language. This field takes effect only when the Truncation field is set to true. Default value: 2.
        # *   **TargetLanReservePages**: the number of lines reserved when the subtitle is in the destination language. This field takes effect only when the Truncation field is set to true. Default value: 2.
        # 
        # The value is a JSON string. Use upper camel case for field names.
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
        # The information about the component layer, such as the size and layout. This parameter contains the following fields:
        # 
        # *   **HeightNormalized**: the normalized value of heights for the elements in the component layer
        # *   **WidthNormalized**: the normalized value of widths for the elements in the component layer
        # *   **PositionNormalized**: the normalized value of the coordinates of the component layer
        # *   **PositionRefer**: the reference coordinates of the component layer.
        # 
        # The value is a JSON string. Use upper camel case for field names.
        # 
        # This parameter is required.
        self.component_layer = component_layer
        # The component name. By default, the component name is the component ID.
        self.component_name = component_name
        # The component type. Valid values:
        # 
        # *   **text**: a text component. If you set ComponentType to text, you must also specify TextLayerContent.
        # *   **image**: an image component. If you set ComponentType to image, you must also specify ImageLayerContent.
        # *   **caption**: a caption component. If you set ComponentType to caption, you must also specify CaptionLayerContent.
        # 
        # This parameter is required.
        self.component_type = component_type
        # The effect of the component. Valid values:
        # 
        # *   **none (default)**
        # *   **animateH**: horizontal scrolling
        # *   **animateV**: vertical scrolling
        self.effect = effect
        # The information about the HTML5 layer.
        self.html_layer_content = html_layer_content
        # The information about the image layer. This parameter contains the following fields:
        # 
        # >  This parameter is required when the ComponentType parameter is set to image.
        # 
        # MaterialId: the ID of the asset from the media asset library. The name that you set when you upload an asset is the ID of the asset.
        # 
        # The value is a JSON string. Use upper camel case for field names.
        self.image_layer_content = image_layer_content
        # The layer stacking order of the component. Valid values:
        # 
        # *   cover
        # *   background
        self.layer_order = layer_order
        # The location ID of the component. Each location ID can be assigned to only one component and must be in the RC[Number] format. The values specified by this parameter must be in ascending order, such as RC01 to RC99.
        # 
        # >  If the ComponentType parameter is set to caption, the LocationId parameter specifies the location ID of the video source referenced by the component.
        # 
        # This parameter is required.
        self.location_id = location_id
        self.owner_id = owner_id
        self.region_id = region_id
        # The information about the text layer. This parameter contains the following fields:
        # 
        # >  This parameter is available and required only when the ComponentType parameter is set to text.
        # 
        # *   **SizeNormalized**: the normalized font size. The font size is set to font_size/output_height. The value range is `[0,1]`. If the font size calculated by the system based on the normalization method is greater than 1024, 1024 is used.
        # *   **BorderWidthNormalized**: the normalized value of the text border width. The normalized value is calculated based on the size of the text, that is, "BorderWidth/FontSize". The value range is `[0,1]`. If the value calculated based on the normalization method exceeds 16, 16 is used. The default value is 0.
        # *   **FontName**: the font name. For more information about the value, see **Font description**. The default value is KaiTi.
        # *   **BorderColor**: the color of the text border. Valid values: 0x000000 to 0xffffff. By default, this parameter is not set. In this case, the color of the text border is transparent.
        # *   **Text**: the content of the text. By default, this parameter is not set. In this case, the text contains no content.
        # *   **Color**: the color of the text. The default value is 0xff0000, which indicates that the text is in red.
        # 
        # The value is a JSON string. Use upper camel case for field names.
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

