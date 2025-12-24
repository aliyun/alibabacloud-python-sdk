# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterComponentsResponseBody(DaraModel):
    def __init__(
        self,
        components: main_models.DescribeCasterComponentsResponseBodyComponents = None,
        request_id: str = None,
        total: int = None,
    ):
        # The components.
        self.components = components
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.components:
            self.components.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.components is not None:
            result['Components'] = self.components.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Components') is not None:
            temp_model = main_models.DescribeCasterComponentsResponseBodyComponents()
            self.components = temp_model.from_map(m.get('Components'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeCasterComponentsResponseBodyComponents(DaraModel):
    def __init__(
        self,
        component: List[main_models.DescribeCasterComponentsResponseBodyComponentsComponent] = None,
    ):
        self.component = component

    def validate(self):
        if self.component:
            for v1 in self.component:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Component'] = []
        if self.component is not None:
            for k1 in self.component:
                result['Component'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component = []
        if m.get('Component') is not None:
            for k1 in m.get('Component'):
                temp_model = main_models.DescribeCasterComponentsResponseBodyComponentsComponent()
                self.component.append(temp_model.from_map(k1))

        return self

class DescribeCasterComponentsResponseBodyComponentsComponent(DaraModel):
    def __init__(
        self,
        caption_layer_content: main_models.DescribeCasterComponentsResponseBodyComponentsComponentCaptionLayerContent = None,
        component_id: str = None,
        component_layer: main_models.DescribeCasterComponentsResponseBodyComponentsComponentComponentLayer = None,
        component_name: str = None,
        component_type: str = None,
        effect: str = None,
        image_layer_content: main_models.DescribeCasterComponentsResponseBodyComponentsComponentImageLayerContent = None,
        location_id: str = None,
        text_layer_content: main_models.DescribeCasterComponentsResponseBodyComponentsComponentTextLayerContent = None,
    ):
        # The information about the subtitle component.
        self.caption_layer_content = caption_layer_content
        # The component ID.
        self.component_id = component_id
        # The information about the component layer, such as the size and layout.
        self.component_layer = component_layer
        # The name of the component. By default, the name is the ID of the component.
        self.component_name = component_name
        # The type of the component. Valid values:
        # 
        # *   **text**: a text component
        # *   **image**: an image component
        # *   **caption**: a caption component
        self.component_type = component_type
        # The display effect for the component. Valid values:
        # 
        # *   **none**
        # *   **animateH**: horizontal scrolling
        # *   **animateV**: vertical scrolling
        self.effect = effect
        # The information about the image component. This parameter is returned only for image components.
        self.image_layer_content = image_layer_content
        # The location ID of the component.
        # 
        # Each location ID can be assigned to only one component and must be in the RC[Number] format. The values of this parameter are in ascending order, for example, from RC01 to RC12.
        self.location_id = location_id
        # The information about the text component. This parameter is returned only for text components.
        self.text_layer_content = text_layer_content

    def validate(self):
        if self.caption_layer_content:
            self.caption_layer_content.validate()
        if self.component_layer:
            self.component_layer.validate()
        if self.image_layer_content:
            self.image_layer_content.validate()
        if self.text_layer_content:
            self.text_layer_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption_layer_content is not None:
            result['CaptionLayerContent'] = self.caption_layer_content.to_map()

        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_layer is not None:
            result['ComponentLayer'] = self.component_layer.to_map()

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.effect is not None:
            result['Effect'] = self.effect

        if self.image_layer_content is not None:
            result['ImageLayerContent'] = self.image_layer_content.to_map()

        if self.location_id is not None:
            result['LocationId'] = self.location_id

        if self.text_layer_content is not None:
            result['TextLayerContent'] = self.text_layer_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptionLayerContent') is not None:
            temp_model = main_models.DescribeCasterComponentsResponseBodyComponentsComponentCaptionLayerContent()
            self.caption_layer_content = temp_model.from_map(m.get('CaptionLayerContent'))

        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentLayer') is not None:
            temp_model = main_models.DescribeCasterComponentsResponseBodyComponentsComponentComponentLayer()
            self.component_layer = temp_model.from_map(m.get('ComponentLayer'))

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('Effect') is not None:
            self.effect = m.get('Effect')

        if m.get('ImageLayerContent') is not None:
            temp_model = main_models.DescribeCasterComponentsResponseBodyComponentsComponentImageLayerContent()
            self.image_layer_content = temp_model.from_map(m.get('ImageLayerContent'))

        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

        if m.get('TextLayerContent') is not None:
            temp_model = main_models.DescribeCasterComponentsResponseBodyComponentsComponentTextLayerContent()
            self.text_layer_content = temp_model.from_map(m.get('TextLayerContent'))

        return self

class DescribeCasterComponentsResponseBodyComponentsComponentTextLayerContent(DaraModel):
    def __init__(
        self,
        border_color: str = None,
        border_width_normalized: float = None,
        color: str = None,
        font_name: str = None,
        size_normalized: float = None,
        text: str = None,
    ):
        # The color of the text border. Valid values: **0x000000 to 0xffffff**. If the value of this parameter is **""**, this parameter does not take effect.
        self.border_color = border_color
        # The normalized value of the width of the text border. The value of this parameter equals the border width divided by the font size.****
        # 
        # The maximum width of the text border is **16**, even if the border width calculated based on this parameter is greater than **16**.
        self.border_width_normalized = border_width_normalized
        # The color of the text. Valid values: **0x000000 to 0xffffff**.
        self.color = color
        # The font of the text, which is specified by the system. Valid values:
        # 
        # *   **KaiTi**
        # *   **AlibabaPuHuiTi-Regular**
        # *   **AlibabaPuHuiTi-Bold**
        # *   **NAlibabaPuHuiTi-Light**
        # *   **NotoSansHans-Regular**
        # *   **NotoSansHans-Bold**
        # *   **NotoSansHans-Light**
        # 
        # ****
        self.font_name = font_name
        # The normalized value of the font size of the text.
        # 
        # The value of this parameter equals the font size divided by the output height.**** The maximum font size of the text is **1,024**, even if the font size calculated based on this parameter is greater than **1,024**. If the value of this parameter is **-1**, this parameter does not take effect.
        self.size_normalized = size_normalized
        # The content of the text.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width_normalized is not None:
            result['BorderWidthNormalized'] = self.border_width_normalized

        if self.color is not None:
            result['Color'] = self.color

        if self.font_name is not None:
            result['FontName'] = self.font_name

        if self.size_normalized is not None:
            result['SizeNormalized'] = self.size_normalized

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidthNormalized') is not None:
            self.border_width_normalized = m.get('BorderWidthNormalized')

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')

        if m.get('SizeNormalized') is not None:
            self.size_normalized = m.get('SizeNormalized')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class DescribeCasterComponentsResponseBodyComponentsComponentImageLayerContent(DaraModel):
    def __init__(
        self,
        material_id: str = None,
    ):
        # The ID of the material from the media library.
        self.material_id = material_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.material_id is not None:
            result['MaterialId'] = self.material_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialId') is not None:
            self.material_id = m.get('MaterialId')

        return self

class DescribeCasterComponentsResponseBodyComponentsComponentComponentLayer(DaraModel):
    def __init__(
        self,
        height_normalized: float = None,
        position_normalizeds: main_models.DescribeCasterComponentsResponseBodyComponentsComponentComponentLayerPositionNormalizeds = None,
        position_refer: str = None,
        transparency: int = None,
        width_normalized: float = None,
    ):
        # The normalized value for heights of the elements in the layer. The widths of the elements are proportionally scaled based on this parameter.
        # 
        # If the value of this parameter is **0**, the elements in the layer are not scaled.
        self.height_normalized = height_normalized
        # The normalized value of the position of the layer, in the format of `[x,y]`. Example: `[0,0]`.
        # 
        # >  The values of x and y need to be normalized.
        self.position_normalizeds = position_normalizeds
        # The reference coordinates of the layer. Valid values:
        # 
        # *   **topLeft**: the upper-left corner
        # *   **topRight**: the upper-right corner
        # *   **bottomLeft**: the lower-left corner
        # *   **bottomRight**: the lower-right corner
        self.position_refer = position_refer
        # The transparency of the layer. Valid values: 0 to 255.
        # 
        # A value of **0** indicates that the layer is completely transparent. A value of **255** indicates that the layer is completely opaque.
        self.transparency = transparency
        # The normalized value for widths of the elements in the layer. The heights of the elements are proportionally scaled based on this parameter. If the value of this parameter is **0**, the elements in the layer are not scaled.
        # 
        # >  This parameter conflicts with the HeightNormalized parameter. If both of them are specified, only the HeightNormalized parameter takes effect. If only one of them is specified, the latest specified value is used.
        self.width_normalized = width_normalized

    def validate(self):
        if self.position_normalizeds:
            self.position_normalizeds.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height_normalized is not None:
            result['HeightNormalized'] = self.height_normalized

        if self.position_normalizeds is not None:
            result['PositionNormalizeds'] = self.position_normalizeds.to_map()

        if self.position_refer is not None:
            result['PositionRefer'] = self.position_refer

        if self.transparency is not None:
            result['Transparency'] = self.transparency

        if self.width_normalized is not None:
            result['WidthNormalized'] = self.width_normalized

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HeightNormalized') is not None:
            self.height_normalized = m.get('HeightNormalized')

        if m.get('PositionNormalizeds') is not None:
            temp_model = main_models.DescribeCasterComponentsResponseBodyComponentsComponentComponentLayerPositionNormalizeds()
            self.position_normalizeds = temp_model.from_map(m.get('PositionNormalizeds'))

        if m.get('PositionRefer') is not None:
            self.position_refer = m.get('PositionRefer')

        if m.get('Transparency') is not None:
            self.transparency = m.get('Transparency')

        if m.get('WidthNormalized') is not None:
            self.width_normalized = m.get('WidthNormalized')

        return self

class DescribeCasterComponentsResponseBodyComponentsComponentComponentLayerPositionNormalizeds(DaraModel):
    def __init__(
        self,
        position: List[float] = None,
    ):
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class DescribeCasterComponentsResponseBodyComponentsComponentCaptionLayerContent(DaraModel):
    def __init__(
        self,
        border_color: str = None,
        border_width_normalized: float = None,
        color: str = None,
        font_name: str = None,
        line_space_normalized: float = None,
        location_id: str = None,
        pts_offset: int = None,
        show_source_lan: bool = None,
        size_normalized: float = None,
        source_lan: str = None,
        target_lan: str = None,
        word_count_per_line: int = None,
        word_space_normalized: float = None,
        words_count: int = None,
    ):
        # The color of the text border.
        # 
        # Valid values: **0x000000 to 0xffffff**. If the value of this parameter is "", this parameter does not take effect.
        self.border_color = border_color
        # The normalized value of the width of the text border. The value of this parameter equals the border width divided by the font size.
        # 
        # The maximum width of the text border is **16**, even if the border width calculated based on this parameter is greater than **16**.
        self.border_width_normalized = border_width_normalized
        # The color of the text. Valid values: **0x000000 to 0xffffff**.
        self.color = color
        # The font of the text, which is specified by the system. Valid values:
        # 
        # *   **KaiTi**
        # *   **AlibabaPuHuiTi-Regular**
        # *   **AlibabaPuHuiTi-Bold**
        # *   **NAlibabaPuHuiTi-Light**
        # *   **NotoSansHans-Regular**
        # *   **NotoSansHans-Bold**
        # *   **NotoSansHans-Light**
        # 
        # ****
        self.font_name = font_name
        # The line spacing, which indicates the interval between every two lines.
        self.line_space_normalized = line_space_normalized
        # The location ID of the component. If the value of the ComponentType parameter is caption, the LocationId parameter indicates the channel ID of the video source that is referenced by the component.
        self.location_id = location_id
        # The offset between the presentation timestamps (PTS) of the subtitles and the audio.
        # 
        # Valid values: **-10000 to 10000**. Default value: **0**.
        self.pts_offset = pts_offset
        # Indicates whether the source language of the subtitles is displayed. Valid values:
        # 
        # *   **true**: The source language is displayed.
        # *   **false**: The source language is not displayed.
        self.show_source_lan = show_source_lan
        # The normalized value of the font size of the subtitles. The value of this parameter equals the font size divided by the output height.``
        # 
        # The maximum font size of the subtitles is **1,024**, even if the font size calculated based on this parameter is greater than **1,024**. If the value of this parameter is **-1**, this parameter does not take effect.
        self.size_normalized = size_normalized
        # The source language of the audio in the video source. Valid values:
        # 
        # *   **en**: English
        # *   **cn**: Chinese
        # *   **es**: Spanish
        # *   **ru**: Russian
        self.source_lan = source_lan
        # The target language of the audio in the video source. Valid values:
        # 
        # *   **en**: English
        # *   **cn**: Chinese
        # *   **es**: Spanish
        # *   **ru**: Russian
        self.target_lan = target_lan
        # The maximum number of words displayed in each line.
        self.word_count_per_line = word_count_per_line
        # The word spacing, which indicates the interval between every two words.
        self.word_space_normalized = word_space_normalized
        # The number of words displayed on the component. The value of this parameter can be specified based on the font size.
        # 
        # Valid values: **10 to 50**.
        self.words_count = words_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.border_color is not None:
            result['BorderColor'] = self.border_color

        if self.border_width_normalized is not None:
            result['BorderWidthNormalized'] = self.border_width_normalized

        if self.color is not None:
            result['Color'] = self.color

        if self.font_name is not None:
            result['FontName'] = self.font_name

        if self.line_space_normalized is not None:
            result['LineSpaceNormalized'] = self.line_space_normalized

        if self.location_id is not None:
            result['LocationId'] = self.location_id

        if self.pts_offset is not None:
            result['PtsOffset'] = self.pts_offset

        if self.show_source_lan is not None:
            result['ShowSourceLan'] = self.show_source_lan

        if self.size_normalized is not None:
            result['SizeNormalized'] = self.size_normalized

        if self.source_lan is not None:
            result['SourceLan'] = self.source_lan

        if self.target_lan is not None:
            result['TargetLan'] = self.target_lan

        if self.word_count_per_line is not None:
            result['WordCountPerLine'] = self.word_count_per_line

        if self.word_space_normalized is not None:
            result['WordSpaceNormalized'] = self.word_space_normalized

        if self.words_count is not None:
            result['WordsCount'] = self.words_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BorderColor') is not None:
            self.border_color = m.get('BorderColor')

        if m.get('BorderWidthNormalized') is not None:
            self.border_width_normalized = m.get('BorderWidthNormalized')

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')

        if m.get('LineSpaceNormalized') is not None:
            self.line_space_normalized = m.get('LineSpaceNormalized')

        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

        if m.get('PtsOffset') is not None:
            self.pts_offset = m.get('PtsOffset')

        if m.get('ShowSourceLan') is not None:
            self.show_source_lan = m.get('ShowSourceLan')

        if m.get('SizeNormalized') is not None:
            self.size_normalized = m.get('SizeNormalized')

        if m.get('SourceLan') is not None:
            self.source_lan = m.get('SourceLan')

        if m.get('TargetLan') is not None:
            self.target_lan = m.get('TargetLan')

        if m.get('WordCountPerLine') is not None:
            self.word_count_per_line = m.get('WordCountPerLine')

        if m.get('WordSpaceNormalized') is not None:
            self.word_space_normalized = m.get('WordSpaceNormalized')

        if m.get('WordsCount') is not None:
            self.words_count = m.get('WordsCount')

        return self

