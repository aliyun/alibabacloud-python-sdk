# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class DescribeImageResultExtResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeImageResultExtResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
        self.msg = msg
        # The request ID.
        self.request_id = request_id

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

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeImageResultExtResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageResultExtResponseBodyData(DaraModel):
    def __init__(
        self,
        custom_image: List[main_models.DescribeImageResultExtResponseBodyDataCustomImage] = None,
        public_figure: List[main_models.DescribeImageResultExtResponseBodyDataPublicFigure] = None,
        text_in_image: main_models.DescribeImageResultExtResponseBodyDataTextInImage = None,
    ):
        # If a custom image library is hit, information about the hit custom image library is returned.
        self.custom_image = custom_image
        # Person information list.
        self.public_figure = public_figure
        # Returns the text information in the hit image.
        self.text_in_image = text_in_image

    def validate(self):
        if self.custom_image:
            for v1 in self.custom_image:
                 if v1:
                    v1.validate()
        if self.public_figure:
            for v1 in self.public_figure:
                 if v1:
                    v1.validate()
        if self.text_in_image:
            self.text_in_image.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k1 in self.custom_image:
                result['CustomImage'].append(k1.to_map() if k1 else None)

        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k1 in self.public_figure:
                result['PublicFigure'].append(k1.to_map() if k1 else None)

        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k1 in m.get('CustomImage'):
                temp_model = main_models.DescribeImageResultExtResponseBodyDataCustomImage()
                self.custom_image.append(temp_model.from_map(k1))

        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k1 in m.get('PublicFigure'):
                temp_model = main_models.DescribeImageResultExtResponseBodyDataPublicFigure()
                self.public_figure.append(temp_model.from_map(k1))

        if m.get('TextInImage') is not None:
            temp_model = main_models.DescribeImageResultExtResponseBodyDataTextInImage()
            self.text_in_image = temp_model.from_map(m.get('TextInImage'))

        return self

class DescribeImageResultExtResponseBodyDataTextInImage(DaraModel):
    def __init__(
        self,
        custom_texts: List[main_models.DescribeImageResultExtResponseBodyDataTextInImageCustomTexts] = None,
        ocr_datas: List[str] = None,
        risk_words: List[str] = None,
    ):
        # When a custom text library is hit, the custom library ID, custom library name, and custom word are returned.
        self.custom_texts = custom_texts
        # Returns the text information in the recognized image.
        self.ocr_datas = ocr_datas
        # The risk words that are hit. Multiple words are separated by commas (,).
        self.risk_words = risk_words

    def validate(self):
        if self.custom_texts:
            for v1 in self.custom_texts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomTexts'] = []
        if self.custom_texts is not None:
            for k1 in self.custom_texts:
                result['CustomTexts'].append(k1.to_map() if k1 else None)

        if self.ocr_datas is not None:
            result['OcrDatas'] = self.ocr_datas

        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_texts = []
        if m.get('CustomTexts') is not None:
            for k1 in m.get('CustomTexts'):
                temp_model = main_models.DescribeImageResultExtResponseBodyDataTextInImageCustomTexts()
                self.custom_texts.append(temp_model.from_map(k1))

        if m.get('OcrDatas') is not None:
            self.ocr_datas = m.get('OcrDatas')

        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')

        return self

class DescribeImageResultExtResponseBodyDataTextInImageCustomTexts(DaraModel):
    def __init__(
        self,
        key_words: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        # Custom words, multiple words separated by commas.
        self.key_words = key_words
        # Custom library ID.
        self.lib_id = lib_id
        # Custom library name.
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_words is not None:
            result['KeyWords'] = self.key_words

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        return self

class DescribeImageResultExtResponseBodyDataPublicFigure(DaraModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        # Identified person coding information.
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')

        return self

class DescribeImageResultExtResponseBodyDataCustomImage(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The image library ID.
        self.lib_id = lib_id
        # The image library name.
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.lib_name is not None:
            result['LibName'] = self.lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')

        return self

