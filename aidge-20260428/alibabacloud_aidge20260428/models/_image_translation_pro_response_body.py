# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class ImageTranslationProResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ImageTranslationProResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Response code. 200 indicates a successful call. For other response codes, refer to the error code documentation.
        self.code = code
        # Translation result data. ResultList contains the URL of the translation result, and GenFiles contains EditInfo with recognized text information.
        self.data = data
        # Error message. Returns "Success" during normal calls. Returns specific error information during exceptions, such as "Content contains sensitive data, please try other input".
        self.message = message
        # Request ID, used to identify a unique request call.
        self.request_id = request_id
        # Whether the call was successful. true indicates success, false indicates failure.
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
            temp_model = main_models.ImageTranslationProResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ImageTranslationProResponseBodyData(DaraModel):
    def __init__(
        self,
        gen_files: List[main_models.ImageTranslationProResponseBodyDataGenFiles] = None,
        result_list: List[main_models.ImageTranslationProResponseBodyDataResultList] = None,
        task_id: str = None,
        usage_map: Dict[str, int] = None,
    ):
        # Editor protocol, containing translation result files and editing information
        self.gen_files = gen_files
        # Image translation result list
        self.result_list = result_list
        # Asynchronous task ID, not returned during synchronous calls.
        self.task_id = task_id
        # Usage information, including the number of processed images, etc.
        self.usage_map = usage_map

    def validate(self):
        if self.gen_files:
            for v1 in self.gen_files:
                 if v1:
                    v1.validate()
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GenFiles'] = []
        if self.gen_files is not None:
            for k1 in self.gen_files:
                result['GenFiles'].append(k1.to_map() if k1 else None)

        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gen_files = []
        if m.get('GenFiles') is not None:
            for k1 in m.get('GenFiles'):
                temp_model = main_models.ImageTranslationProResponseBodyDataGenFiles()
                self.gen_files.append(temp_model.from_map(k1))

        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.ImageTranslationProResponseBodyDataResultList()
                self.result_list.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class ImageTranslationProResponseBodyDataResultList(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        language: str = None,
    ):
        # Image translation result image URL
        self.file_url = file_url
        # Image translation target language
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

class ImageTranslationProResponseBodyDataGenFiles(DaraModel):
    def __init__(
        self,
        edit_info: main_models.ImageTranslationProResponseBodyDataGenFilesEditInfo = None,
        result_list: List[main_models.ImageTranslationProResponseBodyDataGenFilesResultList] = None,
        src_image: str = None,
    ):
        # Editor information, containing recognized information such as text areas, product areas, and fonts
        self.edit_info = edit_info
        # Translation result collection
        self.result_list = result_list
        # Original image URL
        self.src_image = src_image

    def validate(self):
        if self.edit_info:
            self.edit_info.validate()
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edit_info is not None:
            result['EditInfo'] = self.edit_info.to_map()

        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        if self.src_image is not None:
            result['SrcImage'] = self.src_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditInfo') is not None:
            temp_model = main_models.ImageTranslationProResponseBodyDataGenFilesEditInfo()
            self.edit_info = temp_model.from_map(m.get('EditInfo'))

        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.ImageTranslationProResponseBodyDataGenFilesResultList()
                self.result_list.append(temp_model.from_map(k1))

        if m.get('SrcImage') is not None:
            self.src_image = m.get('SrcImage')

        return self

class ImageTranslationProResponseBodyDataGenFilesResultList(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        language: str = None,
    ):
        # Translated image file URL
        self.file_url = file_url
        # Translation target language
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

class ImageTranslationProResponseBodyDataGenFilesEditInfo(DaraModel):
    def __init__(
        self,
        font: List[str] = None,
        goods_rects: main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoGoodsRects = None,
        languages: List[str] = None,
        repaired_url: str = None,
        result_image_ids: List[str] = None,
        text_areas: List[main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreas] = None,
    ):
        # Font type list
        self.font = font
        # Product bounding box area coordinate information
        self.goods_rects = goods_rects
        # Translation target language list
        self.languages = languages
        # Image URL after all text has been inpainted
        self.repaired_url = repaired_url
        # Collection of translated image global IDs
        self.result_image_ids = result_image_ids
        # Text box list, containing information about all recognized text areas
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

        if self.languages is not None:
            result['Languages'] = self.languages

        if self.repaired_url is not None:
            result['RepairedUrl'] = self.repaired_url

        if self.result_image_ids is not None:
            result['ResultImageIds'] = self.result_image_ids

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
            temp_model = main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoGoodsRects()
            self.goods_rects = temp_model.from_map(m.get('GoodsRects'))

        if m.get('Languages') is not None:
            self.languages = m.get('Languages')

        if m.get('RepairedUrl') is not None:
            self.repaired_url = m.get('RepairedUrl')

        if m.get('ResultImageIds') is not None:
            self.result_image_ids = m.get('ResultImageIds')

        self.text_areas = []
        if m.get('TextAreas') is not None:
            for k1 in m.get('TextAreas'):
                temp_model = main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreas()
                self.text_areas.append(temp_model.from_map(k1))

        return self

class ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreas(DaraModel):
    def __init__(
        self,
        color: str = None,
        content: str = None,
        fontsize: int = None,
        horizontal_layout: str = None,
        line_count: int = None,
        texts: List[main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTexts] = None,
        vertical_layout: str = None,
    ):
        # Text color, e.g., #ffffff
        self.color = color
        # Original text before translation
        self.content = content
        # Font size
        self.fontsize = fontsize
        # Horizontal layout mode. Available values: center, left, right
        self.horizontal_layout = horizontal_layout
        # Number of lines in the text box
        self.line_count = line_count
        # Translated text list, where each element corresponds to the translation result for one target language
        self.texts = texts
        # Vertical layout mode. Available values: center, top, down
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
                temp_model = main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTexts()
                self.texts.append(temp_model.from_map(k1))

        if m.get('VerticalLayout') is not None:
            self.vertical_layout = m.get('VerticalLayout')

        return self

class ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTexts(DaraModel):
    def __init__(
        self,
        color: str = None,
        fontsize: int = None,
        horizontal_layout: str = None,
        image_rect: main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTextsImageRect = None,
        language: str = None,
        line_count: int = None,
        ovis_err_msg: str = None,
        text_rect: main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTextsTextRect = None,
        valid: bool = None,
        value: str = None,
        vertical_layout: str = None,
    ):
        # Translated text color
        self.color = color
        # Font size of the translated text
        self.fontsize = fontsize
        # Horizontal layout mode. Available values: center, left, right
        self.horizontal_layout = horizontal_layout
        # Image repair area coordinates
        self.image_rect = image_rect
        # Translation target language code
        self.language = language
        # Number of lines in the text box
        self.line_count = line_count
        # Ovis model error message and execution time
        self.ovis_err_msg = ovis_err_msg
        # Text box area coordinates
        self.text_rect = text_rect
        # Whether the TextItem is valid. It is invalid when this value does not exist or is false.
        self.valid = valid
        # Translated text content
        self.value = value
        # Vertical layout mode. Available values: center, top, down
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

        if self.ovis_err_msg is not None:
            result['OvisErrMsg'] = self.ovis_err_msg

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
            temp_model = main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTextsImageRect()
            self.image_rect = temp_model.from_map(m.get('ImageRect'))

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LineCount') is not None:
            self.line_count = m.get('LineCount')

        if m.get('OvisErrMsg') is not None:
            self.ovis_err_msg = m.get('OvisErrMsg')

        if m.get('TextRect') is not None:
            temp_model = main_models.ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTextsTextRect()
            self.text_rect = temp_model.from_map(m.get('TextRect'))

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('VerticalLayout') is not None:
            self.vertical_layout = m.get('VerticalLayout')

        return self

class ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTextsTextRect(DaraModel):
    def __init__(
        self,
        degree: int = None,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # Text box rotation angle in degrees. Values less than 1 indicate a horizontal text box
        self.degree = degree
        # Height
        self.height = height
        # Left coordinate
        self.left = left
        # Top coordinate
        self.top = top
        # Width
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

class ImageTranslationProResponseBodyDataGenFilesEditInfoTextAreasTextsImageRect(DaraModel):
    def __init__(
        self,
        degree: int = None,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # Text box rotation angle in degrees. Values less than 1 indicate a horizontal text box
        self.degree = degree
        # Height
        self.height = height
        # Left coordinate
        self.left = left
        # Top coordinate
        self.top = top
        # Width
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

class ImageTranslationProResponseBodyDataGenFilesEditInfoGoodsRects(DaraModel):
    def __init__(
        self,
        degree: int = None,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        # Text box rotation angle in degrees. Values less than 1 indicate a horizontal text box
        self.degree = degree
        # Height
        self.height = height
        # Left coordinate
        self.left = left
        # Top coordinate
        self.top = top
        # Width
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

