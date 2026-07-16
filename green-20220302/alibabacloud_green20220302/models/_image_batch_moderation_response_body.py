# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class ImageBatchModerationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ImageBatchModerationResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        # The return code. A value of 200 indicates success.
        self.code = code
        # The results of the image content moderation.
        self.data = data
        # The response message for the request.
        self.msg = msg
        # The unique ID of the request. Alibaba Cloud generates this ID for each request. Use this ID to troubleshoot issues.
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
            temp_model = main_models.ImageBatchModerationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ImageBatchModerationResponseBodyData(DaraModel):
    def __init__(
        self,
        data_id: str = None,
        manual_task_id: str = None,
        result: List[main_models.ImageBatchModerationResponseBodyDataResult] = None,
        results: List[main_models.ImageBatchModerationResponseBodyDataResults] = None,
        risk_level: str = None,
    ):
        # The data ID of the moderated object.
        self.data_id = data_id
        # The ID of the manual review task.
        self.manual_task_id = manual_task_id
        # An array of results for the image moderation. The results contain parameters such as threat labels and confidence scores.
        self.result = result
        # The detailed moderation results for each detection service. This is an array.
        self.results = results
        # The risk level.
        self.risk_level = risk_level

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ImageBatchModerationResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.ImageBatchModerationResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class ImageBatchModerationResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        ext: main_models.ImageBatchModerationResponseBodyDataResultsExt = None,
        result: List[main_models.ImageBatchModerationResponseBodyDataResultsResult] = None,
        risk_level: str = None,
        service: str = None,
    ):
        # Additional reference information for the image.
        self.ext = ext
        # The results of the image detection, including threat labels and confidence scores. This is an array.
        self.result = result
        # The risk level.
        self.risk_level = risk_level
        # The detection service supported by Image Moderation Pro.
        self.service = service

    def validate(self):
        if self.ext:
            self.ext.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext.to_map()

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExt()
            self.ext = temp_model.from_map(m.get('Ext'))

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ImageBatchModerationResponseBodyDataResultsResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

class ImageBatchModerationResponseBodyDataResultsResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # The confidence score. The value ranges from 0 to 100, with two decimal places. Some labels do not have a confidence score.
        self.confidence = confidence
        # The description.
        self.description = description
        # The label returned after the image content moderation. An image may have multiple labels and scores.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class ImageBatchModerationResponseBodyDataResultsExt(DaraModel):
    def __init__(
        self,
        custom_image: List[main_models.ImageBatchModerationResponseBodyDataResultsExtCustomImage] = None,
        logo_data: main_models.ImageBatchModerationResponseBodyDataResultsExtLogoData = None,
        public_figure: List[main_models.ImageBatchModerationResponseBodyDataResultsExtPublicFigure] = None,
        text_in_image: main_models.ImageBatchModerationResponseBodyDataResultsExtTextInImage = None,
    ):
        # A list of hits in custom image libraries.
        self.custom_image = custom_image
        # Logo information.
        self.logo_data = logo_data
        # A list of public figures.
        self.public_figure = public_figure
        # The text detected in the image.
        self.text_in_image = text_in_image

    def validate(self):
        if self.custom_image:
            for v1 in self.custom_image:
                 if v1:
                    v1.validate()
        if self.logo_data:
            self.logo_data.validate()
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

        if self.logo_data is not None:
            result['LogoData'] = self.logo_data.to_map()

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
                temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtCustomImage()
                self.custom_image.append(temp_model.from_map(k1))

        if m.get('LogoData') is not None:
            temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtLogoData()
            self.logo_data = temp_model.from_map(m.get('LogoData'))

        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k1 in m.get('PublicFigure'):
                temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtPublicFigure()
                self.public_figure.append(temp_model.from_map(k1))

        if m.get('TextInImage') is not None:
            temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtTextInImage()
            self.text_in_image = temp_model.from_map(m.get('TextInImage'))

        return self

class ImageBatchModerationResponseBodyDataResultsExtTextInImage(DaraModel):
    def __init__(
        self,
        custom_text: List[main_models.ImageBatchModerationResponseBodyDataResultsExtTextInImageCustomText] = None,
        ocr_result: List[main_models.ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResult] = None,
        risk_word: List[str] = None,
    ):
        # If a custom text library is hit, the ID and name of the library, and the hit keywords are returned.
        self.custom_text = custom_text
        # The information for each line of text recognized in the image.
        self.ocr_result = ocr_result
        # The detected risk keywords.
        self.risk_word = risk_word

    def validate(self):
        if self.custom_text:
            for v1 in self.custom_text:
                 if v1:
                    v1.validate()
        if self.ocr_result:
            for v1 in self.ocr_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomText'] = []
        if self.custom_text is not None:
            for k1 in self.custom_text:
                result['CustomText'].append(k1.to_map() if k1 else None)

        result['OcrResult'] = []
        if self.ocr_result is not None:
            for k1 in self.ocr_result:
                result['OcrResult'].append(k1.to_map() if k1 else None)

        if self.risk_word is not None:
            result['RiskWord'] = self.risk_word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_text = []
        if m.get('CustomText') is not None:
            for k1 in m.get('CustomText'):
                temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtTextInImageCustomText()
                self.custom_text.append(temp_model.from_map(k1))

        self.ocr_result = []
        if m.get('OcrResult') is not None:
            for k1 in m.get('OcrResult'):
                temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResult()
                self.ocr_result.append(temp_model.from_map(k1))

        if m.get('RiskWord') is not None:
            self.risk_word = m.get('RiskWord')

        return self

class ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResult(DaraModel):
    def __init__(
        self,
        location: main_models.ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResultLocation = None,
        text: str = None,
    ):
        # The coordinates of the text line.
        self.location = location
        # The text.
        self.text = text

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location is not None:
            result['Location'] = self.location.to_map()

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResultLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResultLocation(DaraModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        # The height of the text area, in pixels.
        self.h = h
        # The width of the text area, in pixels.
        self.w = w
        # The x-coordinate of the upper-left corner of the text area, in pixels. The origin (0,0) is the upper-left corner of the image.
        self.x = x
        # The y-coordinate of the upper-left corner of the text area, in pixels. The origin (0,0) is the upper-left corner of the image.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h is not None:
            result['H'] = self.h

        if self.w is not None:
            result['W'] = self.w

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')

        if m.get('W') is not None:
            self.w = m.get('W')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class ImageBatchModerationResponseBodyDataResultsExtTextInImageCustomText(DaraModel):
    def __init__(
        self,
        key_words: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        # The custom keywords. Separate multiple keywords with a comma.
        self.key_words = key_words
        # The ID of the custom library.
        self.lib_id = lib_id
        # The name of the custom library.
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

class ImageBatchModerationResponseBodyDataResultsExtPublicFigure(DaraModel):
    def __init__(
        self,
        figure_id: str = None,
        figure_name: str = None,
        location: List[main_models.ImageBatchModerationResponseBodyDataResultsExtPublicFigureLocation] = None,
    ):
        # The ID of the recognized public figure.
        self.figure_id = figure_id
        # The name of the recognized public figure.
        self.figure_name = figure_name
        # The location of the recognized object.
        self.location = location

    def validate(self):
        if self.location:
            for v1 in self.location:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id

        if self.figure_name is not None:
            result['FigureName'] = self.figure_name

        result['Location'] = []
        if self.location is not None:
            for k1 in self.location:
                result['Location'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')

        if m.get('FigureName') is not None:
            self.figure_name = m.get('FigureName')

        self.location = []
        if m.get('Location') is not None:
            for k1 in m.get('Location'):
                temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtPublicFigureLocation()
                self.location.append(temp_model.from_map(k1))

        return self

class ImageBatchModerationResponseBodyDataResultsExtPublicFigureLocation(DaraModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        # The height of the area, in pixels.
        self.h = h
        # The width of the area, in pixels.
        self.w = w
        # The x-coordinate of the upper-left corner of the area, in pixels. The origin (0,0) is the upper-left corner of the image.
        self.x = x
        # The y-coordinate of the upper-left corner of the area, in pixels. The origin (0,0) is the upper-left corner of the image.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h is not None:
            result['H'] = self.h

        if self.w is not None:
            result['W'] = self.w

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')

        if m.get('W') is not None:
            self.w = m.get('W')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class ImageBatchModerationResponseBodyDataResultsExtLogoData(DaraModel):
    def __init__(
        self,
        location: main_models.ImageBatchModerationResponseBodyDataResultsExtLogoDataLocation = None,
        logo: List[main_models.ImageBatchModerationResponseBodyDataResultsExtLogoDataLogo] = None,
    ):
        # The location of the recognized object.
        self.location = location
        # Identity information.
        self.logo = logo

    def validate(self):
        if self.location:
            self.location.validate()
        if self.logo:
            for v1 in self.logo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.location is not None:
            result['Location'] = self.location.to_map()

        result['Logo'] = []
        if self.logo is not None:
            for k1 in self.logo:
                result['Logo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtLogoDataLocation()
            self.location = temp_model.from_map(m.get('Location'))

        self.logo = []
        if m.get('Logo') is not None:
            for k1 in m.get('Logo'):
                temp_model = main_models.ImageBatchModerationResponseBodyDataResultsExtLogoDataLogo()
                self.logo.append(temp_model.from_map(k1))

        return self

class ImageBatchModerationResponseBodyDataResultsExtLogoDataLogo(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
        name: str = None,
    ):
        # The confidence score. The value ranges from 0 to 100, with two decimal places.
        self.confidence = confidence
        # The category of the logo.
        self.label = label
        # The name of the logo.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ImageBatchModerationResponseBodyDataResultsExtLogoDataLocation(DaraModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        # The height of the logo area, in pixels.
        self.h = h
        # The width of the logo area, in pixels.
        self.w = w
        # The x-coordinate of the upper-left corner of the area, in pixels. The origin (0,0) is the upper-left corner of the image.
        self.x = x
        # The y-coordinate of the upper-left corner of the area, in pixels. The origin (0,0) is the upper-left corner of the image.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.h is not None:
            result['H'] = self.h

        if self.w is not None:
            result['W'] = self.w

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')

        if m.get('W') is not None:
            self.w = m.get('W')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class ImageBatchModerationResponseBodyDataResultsExtCustomImage(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        # The ID of the hit custom image.
        self.image_id = image_id
        # The ID of the custom library.
        self.lib_id = lib_id
        # The name of the hit custom image library.
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

class ImageBatchModerationResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # The confidence score. The value ranges from 0 to 100, with two decimal places. Some labels do not have a confidence score.
        self.confidence = confidence
        # The description.
        self.description = description
        # The label returned after the image content moderation. An image may have multiple labels and scores.
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

