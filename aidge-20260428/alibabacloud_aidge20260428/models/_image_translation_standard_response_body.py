# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class ImageTranslationStandardResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ImageTranslationStandardResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of 200 indicates a successful call. For other response codes, refer to the error code information.
        self.code = code
        # The translation result data, including the translated image URL and usage information.
        self.data = data
        # The error message. "Success" is returned for successful calls, and a specific error message is returned for failed calls.
        self.message = message
        # The request ID, used to uniquely identify a request.
        self.request_id = request_id
        # Indicates whether the call is successful. A value of true indicates success, and a value of false indicates failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ImageTranslationStandardResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImageTranslationStandardResponseBodyData(DaraModel):
    def __init__(
        self,
        edit_info: main_models.ImageTranslationStandardResponseBodyDataEditInfo = None,
        image_url: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # The edit information.
        self.edit_info = edit_info
        # The URL of the image generated from the image translation result.
        self.image_url = image_url
        # The usage information, including the number of processed images.
        self.usage_map = usage_map

    def validate(self):
        if self.edit_info:
            self.edit_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edit_info is not None:
            result['EditInfo'] = self.edit_info.to_map()

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditInfo') is not None:
            temp_model = main_models.ImageTranslationStandardResponseBodyDataEditInfo()
            self.edit_info = temp_model.from_map(m.get('EditInfo'))

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class ImageTranslationStandardResponseBodyDataEditInfo(DaraModel):
    def __init__(
        self,
        font: List[str] = None,
        goods_rects: main_models.ImageTranslationStandardResponseBodyDataEditInfoGoodsRects = None,
        goods_url: str = None,
        languages: List[str] = None,
        pict_url: str = None,
        repaired_url: str = None,
        repaired_urls: List[str] = None,
        result_image_ids: List[str] = None,
        result_urls: List[str] = None,
        text_areas: List[main_models.ImageTranslationStandardResponseBodyDataEditInfoTextAreas] = None,
    ):
        # The list of fonts used.
        self.font = font
        # The product area rectangle.
        self.goods_rects = goods_rects
        # The product image URL.
        self.goods_url = goods_url
        # The list of target languages.
        self.languages = languages
        # The URL of the original image.
        self.pict_url = pict_url
        # The URL of the repaired image.
        self.repaired_url = repaired_url
        # The list of repaired image URLs.
        self.repaired_urls = repaired_urls
        # The list of result image IDs.
        self.result_image_ids = result_image_ids
        # The list of result image URLs.
        self.result_urls = result_urls
        # The list of text areas.
        self.text_areas = text_areas

    def validate(self):
        if self.goods_rects:
            self.goods_rects.validate()
        if self.text_areas:
            for v1 in self.text_areas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.font is not None:
            result['Font'] = self.font

        if self.goods_rects is not None:
            result['GoodsRects'] = self.goods_rects.to_map()

        if self.goods_url is not None:
            result['GoodsUrl'] = self.goods_url

        if self.languages is not None:
            result['Languages'] = self.languages

        if self.pict_url is not None:
            result['PictUrl'] = self.pict_url

        if self.repaired_url is not None:
            result['RepairedUrl'] = self.repaired_url

        if self.repaired_urls is not None:
            result['RepairedUrls'] = self.repaired_urls

        if self.result_image_ids is not None:
            result['ResultImageIds'] = self.result_image_ids

        if self.result_urls is not None:
            result['ResultUrls'] = self.result_urls

        result['TextAreas'] = []
        if self.text_areas is not None:
            for k1 in self.text_areas:
                result['TextAreas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Font') is not None:
            self.font = m.get('Font')

        if m.get('GoodsRects') is not None:
            temp_model = main_models.ImageTranslationStandardResponseBodyDataEditInfoGoodsRects()
            self.goods_rects = temp_model.from_map(m.get('GoodsRects'))

        if m.get('GoodsUrl') is not None:
            self.goods_url = m.get('GoodsUrl')

        if m.get('Languages') is not None:
            self.languages = m.get('Languages')

        if m.get('PictUrl') is not None:
            self.pict_url = m.get('PictUrl')

        if m.get('RepairedUrl') is not None:
            self.repaired_url = m.get('RepairedUrl')

        if m.get('RepairedUrls') is not None:
            self.repaired_urls = m.get('RepairedUrls')

        if m.get('ResultImageIds') is not None:
            self.result_image_ids = m.get('ResultImageIds')

        if m.get('ResultUrls') is not None:
            self.result_urls = m.get('ResultUrls')

        self.text_areas = []
        if m.get('TextAreas') is not None:
            for k1 in m.get('TextAreas'):
                temp_model = main_models.ImageTranslationStandardResponseBodyDataEditInfoTextAreas()
                self.text_areas.append(temp_model.from_map(k1))

        return self

class ImageTranslationStandardResponseBodyDataEditInfoTextAreas(DaraModel):
    def __init__(
        self,
        color: str = None,
        content: str = None,
        fontsize: int = None,
        horizontal_layout: str = None,
        line_count: int = None,
        texts: List[main_models.ImageTranslationStandardResponseBodyDataEditInfoTextAreasTexts] = None,
        vertical_layout: str = None,
    ):
        # The color.
        self.color = color
        # The content.
        self.content = content
        # The font size.
        self.fontsize = fontsize
        # The horizontal layout.
        self.horizontal_layout = horizontal_layout
        # The line count.
        self.line_count = line_count
        # The list of texts.
        self.texts = texts
        # The vertical layout.
        self.vertical_layout = vertical_layout

    def validate(self):
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color is not None:
            result['Color'] = self.color

        if self.content is not None:
            result['Content'] = self.content

        if self.fontsize is not None:
            result['Fontsize'] = self.fontsize

        if self.horizontal_layout is not None:
            result['HorizontalLayout'] = self.horizontal_layout

        if self.line_count is not None:
            result['LineCount'] = self.line_count

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        if self.vertical_layout is not None:
            result['VerticalLayout'] = self.vertical_layout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Fontsize') is not None:
            self.fontsize = m.get('Fontsize')

        if m.get('HorizontalLayout') is not None:
            self.horizontal_layout = m.get('HorizontalLayout')

        if m.get('LineCount') is not None:
            self.line_count = m.get('LineCount')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.ImageTranslationStandardResponseBodyDataEditInfoTextAreasTexts()
                self.texts.append(temp_model.from_map(k1))

        if m.get('VerticalLayout') is not None:
            self.vertical_layout = m.get('VerticalLayout')

        return self

class ImageTranslationStandardResponseBodyDataEditInfoTextAreasTexts(DaraModel):
    def __init__(
        self,
        color: str = None,
        fontsize: int = None,
        horizontal_layout: str = None,
        image_rect: main_models.ImageTranslationStandardResponseBodyDataEditInfoTextAreasTextsImageRect = None,
        language: str = None,
        line_count: int = None,
        text_rect: main_models.ImageTranslationStandardResponseBodyDataEditInfoTextAreasTextsTextRect = None,
        valid: bool = None,
        value: str = None,
        vertical_layout: str = None,
    ):
        # The color.
        self.color = color
        # The font size.
        self.fontsize = fontsize
        # The horizontal layout.
        self.horizontal_layout = horizontal_layout
        # The image area.
        self.image_rect = image_rect
        # The language.
        self.language = language
        # The line count.
        self.line_count = line_count
        # The text area.
        self.text_rect = text_rect
        # Indicates whether the text is valid.
        self.valid = valid
        # The text value.
        self.value = value
        # The vertical layout.
        self.vertical_layout = vertical_layout

    def validate(self):
        if self.image_rect:
            self.image_rect.validate()
        if self.text_rect:
            self.text_rect.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color is not None:
            result['Color'] = self.color

        if self.fontsize is not None:
            result['Fontsize'] = self.fontsize

        if self.horizontal_layout is not None:
            result['HorizontalLayout'] = self.horizontal_layout

        if self.image_rect is not None:
            result['ImageRect'] = self.image_rect.to_map()

        if self.language is not None:
            result['Language'] = self.language

        if self.line_count is not None:
            result['LineCount'] = self.line_count

        if self.text_rect is not None:
            result['TextRect'] = self.text_rect.to_map()

        if self.valid is not None:
            result['Valid'] = self.valid

        if self.value is not None:
            result['Value'] = self.value

        if self.vertical_layout is not None:
            result['VerticalLayout'] = self.vertical_layout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('Fontsize') is not None:
            self.fontsize = m.get('Fontsize')

        if m.get('HorizontalLayout') is not None:
            self.horizontal_layout = m.get('HorizontalLayout')

        if m.get('ImageRect') is not None:
            temp_model = main_models.ImageTranslationStandardResponseBodyDataEditInfoTextAreasTextsImageRect()
            self.image_rect = temp_model.from_map(m.get('ImageRect'))

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LineCount') is not None:
            self.line_count = m.get('LineCount')

        if m.get('TextRect') is not None:
            temp_model = main_models.ImageTranslationStandardResponseBodyDataEditInfoTextAreasTextsTextRect()
            self.text_rect = temp_model.from_map(m.get('TextRect'))

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('VerticalLayout') is not None:
            self.vertical_layout = m.get('VerticalLayout')

        return self

class ImageTranslationStandardResponseBodyDataEditInfoTextAreasTextsTextRect(DaraModel):
    def __init__(
        self,
        degree: int = None,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # The rotation angle.
        self.degree = degree
        # The height.
        self.height = height
        # The left coordinate.
        self.left = left
        # The top coordinate.
        self.top = top
        # The width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.degree is not None:
            result['Degree'] = self.degree

        if self.height is not None:
            result['Height'] = self.height

        if self.left is not None:
            result['Left'] = self.left

        if self.top is not None:
            result['Top'] = self.top

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class ImageTranslationStandardResponseBodyDataEditInfoTextAreasTextsImageRect(DaraModel):
    def __init__(
        self,
        degree: int = None,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # The rotation angle.
        self.degree = degree
        # The height.
        self.height = height
        # The left coordinate.
        self.left = left
        # The top coordinate.
        self.top = top
        # The width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.degree is not None:
            result['Degree'] = self.degree

        if self.height is not None:
            result['Height'] = self.height

        if self.left is not None:
            result['Left'] = self.left

        if self.top is not None:
            result['Top'] = self.top

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class ImageTranslationStandardResponseBodyDataEditInfoGoodsRects(DaraModel):
    def __init__(
        self,
        degree: int = None,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # The rotation angle.
        self.degree = degree
        # The height.
        self.height = height
        # The left coordinate.
        self.left = left
        # The top coordinate.
        self.top = top
        # The width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.degree is not None:
            result['Degree'] = self.degree

        if self.height is not None:
            result['Height'] = self.height

        if self.left is not None:
            result['Left'] = self.left

        if self.top is not None:
            result['Top'] = self.top

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Degree') is not None:
            self.degree = m.get('Degree')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

