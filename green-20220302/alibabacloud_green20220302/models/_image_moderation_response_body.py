# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class ImageModerationResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ImageModerationResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The moderation results.
        self.data = data
        # The message that is returned in response to the request.
        self.msg = msg
        # The request ID, which is used to locate and troubleshoot issues.
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
            temp_model = main_models.ImageModerationResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ImageModerationResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        data_id: str = None,
        ext: main_models.ImageModerationResponseBodyDataExt = None,
        manual_task_id: str = None,
        result: List[main_models.ImageModerationResponseBodyDataResult] = None,
        risk_level: str = None,
    ):
        self.account_id = account_id
        # The ID of the moderated object.
        # 
        # >  If you specify the dataId parameter in the request, the value of the dataId parameter is returned in the response.
        self.data_id = data_id
        # Auxiliary reference information.
        self.ext = ext
        self.manual_task_id = manual_task_id
        # The results of image moderation parameters such as the label parameter and the confidence parameter, which are an array structure.
        self.result = result
        # Risk Level.
        self.risk_level = risk_level

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
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.ext is not None:
            result['Ext'] = self.ext.to_map()

        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Ext') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExt()
            self.ext = temp_model.from_map(m.get('Ext'))

        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ImageModerationResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class ImageModerationResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
        risk_level: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places. Some labels do not have scores of confidence levels.
        self.confidence = confidence
        # The description of the result.
        self.description = description
        # The labels returned after the image moderation. Multiple risk labels and the corresponding scores of confidence levels may be returned for an image.
        self.label = label
        # Risk Level
        self.risk_level = risk_level

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

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class ImageModerationResponseBodyDataExt(DaraModel):
    def __init__(
        self,
        aigc_data: main_models.ImageModerationResponseBodyDataExtAigcData = None,
        custom_image: List[main_models.ImageModerationResponseBodyDataExtCustomImage] = None,
        face_data: List[main_models.ImageModerationResponseBodyDataExtFaceData] = None,
        logo_data: List[main_models.ImageModerationResponseBodyDataExtLogoData] = None,
        ocr_result: List[main_models.ImageModerationResponseBodyDataExtOcrResult] = None,
        public_figure: List[main_models.ImageModerationResponseBodyDataExtPublicFigure] = None,
        recognition: List[main_models.ImageModerationResponseBodyDataExtRecognition] = None,
        text_in_image: main_models.ImageModerationResponseBodyDataExtTextInImage = None,
        vl_content: main_models.ImageModerationResponseBodyDataExtVlContent = None,
    ):
        self.aigc_data = aigc_data
        # If a custom image library is hit, information about the hit custom image library is returned.
        self.custom_image = custom_image
        # The returned face attribute information
        self.face_data = face_data
        # Logo information.
        self.logo_data = logo_data
        # Returns the text information in the recognized image.
        self.ocr_result = ocr_result
        # Person information list.
        self.public_figure = public_figure
        # The result of image recognition.
        self.recognition = recognition
        # Returns the text information in the hit image.
        self.text_in_image = text_in_image
        # the vl output content
        self.vl_content = vl_content

    def validate(self):
        if self.aigc_data:
            self.aigc_data.validate()
        if self.custom_image:
            for v1 in self.custom_image:
                 if v1:
                    v1.validate()
        if self.face_data:
            for v1 in self.face_data:
                 if v1:
                    v1.validate()
        if self.logo_data:
            for v1 in self.logo_data:
                 if v1:
                    v1.validate()
        if self.ocr_result:
            for v1 in self.ocr_result:
                 if v1:
                    v1.validate()
        if self.public_figure:
            for v1 in self.public_figure:
                 if v1:
                    v1.validate()
        if self.recognition:
            for v1 in self.recognition:
                 if v1:
                    v1.validate()
        if self.text_in_image:
            self.text_in_image.validate()
        if self.vl_content:
            self.vl_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aigc_data is not None:
            result['AigcData'] = self.aigc_data.to_map()

        result['CustomImage'] = []
        if self.custom_image is not None:
            for k1 in self.custom_image:
                result['CustomImage'].append(k1.to_map() if k1 else None)

        result['FaceData'] = []
        if self.face_data is not None:
            for k1 in self.face_data:
                result['FaceData'].append(k1.to_map() if k1 else None)

        result['LogoData'] = []
        if self.logo_data is not None:
            for k1 in self.logo_data:
                result['LogoData'].append(k1.to_map() if k1 else None)

        result['OcrResult'] = []
        if self.ocr_result is not None:
            for k1 in self.ocr_result:
                result['OcrResult'].append(k1.to_map() if k1 else None)

        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k1 in self.public_figure:
                result['PublicFigure'].append(k1.to_map() if k1 else None)

        result['Recognition'] = []
        if self.recognition is not None:
            for k1 in self.recognition:
                result['Recognition'].append(k1.to_map() if k1 else None)

        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image.to_map()

        if self.vl_content is not None:
            result['VlContent'] = self.vl_content.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AigcData') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtAigcData()
            self.aigc_data = temp_model.from_map(m.get('AigcData'))

        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k1 in m.get('CustomImage'):
                temp_model = main_models.ImageModerationResponseBodyDataExtCustomImage()
                self.custom_image.append(temp_model.from_map(k1))

        self.face_data = []
        if m.get('FaceData') is not None:
            for k1 in m.get('FaceData'):
                temp_model = main_models.ImageModerationResponseBodyDataExtFaceData()
                self.face_data.append(temp_model.from_map(k1))

        self.logo_data = []
        if m.get('LogoData') is not None:
            for k1 in m.get('LogoData'):
                temp_model = main_models.ImageModerationResponseBodyDataExtLogoData()
                self.logo_data.append(temp_model.from_map(k1))

        self.ocr_result = []
        if m.get('OcrResult') is not None:
            for k1 in m.get('OcrResult'):
                temp_model = main_models.ImageModerationResponseBodyDataExtOcrResult()
                self.ocr_result.append(temp_model.from_map(k1))

        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k1 in m.get('PublicFigure'):
                temp_model = main_models.ImageModerationResponseBodyDataExtPublicFigure()
                self.public_figure.append(temp_model.from_map(k1))

        self.recognition = []
        if m.get('Recognition') is not None:
            for k1 in m.get('Recognition'):
                temp_model = main_models.ImageModerationResponseBodyDataExtRecognition()
                self.recognition.append(temp_model.from_map(k1))

        if m.get('TextInImage') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtTextInImage()
            self.text_in_image = temp_model.from_map(m.get('TextInImage'))

        if m.get('VlContent') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtVlContent()
            self.vl_content = temp_model.from_map(m.get('VlContent'))

        return self

class ImageModerationResponseBodyDataExtVlContent(DaraModel):
    def __init__(
        self,
        output_text: str = None,
    ):
        # the vl output content
        self.output_text = output_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_text is not None:
            result['OutputText'] = self.output_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputText') is not None:
            self.output_text = m.get('OutputText')

        return self

class ImageModerationResponseBodyDataExtTextInImage(DaraModel):
    def __init__(
        self,
        custom_text: List[main_models.ImageModerationResponseBodyDataExtTextInImageCustomText] = None,
        ocr_result: List[main_models.ImageModerationResponseBodyDataExtTextInImageOcrResult] = None,
        risk_word: List[str] = None,
    ):
        # When a custom text library is hit, the custom library ID, custom library name, and custom word are returned.
        self.custom_text = custom_text
        # Returns the text information in the recognized image.
        self.ocr_result = ocr_result
        # The risk words that are hit. Multiple words are separated by commas (,).
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
                temp_model = main_models.ImageModerationResponseBodyDataExtTextInImageCustomText()
                self.custom_text.append(temp_model.from_map(k1))

        self.ocr_result = []
        if m.get('OcrResult') is not None:
            for k1 in m.get('OcrResult'):
                temp_model = main_models.ImageModerationResponseBodyDataExtTextInImageOcrResult()
                self.ocr_result.append(temp_model.from_map(k1))

        if m.get('RiskWord') is not None:
            self.risk_word = m.get('RiskWord')

        return self

class ImageModerationResponseBodyDataExtTextInImageOcrResult(DaraModel):
    def __init__(
        self,
        location: main_models.ImageModerationResponseBodyDataExtTextInImageOcrResultLocation = None,
        text: str = None,
    ):
        # Location information.
        self.location = location
        # The text information in the recognized image.
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
            temp_model = main_models.ImageModerationResponseBodyDataExtTextInImageOcrResultLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class ImageModerationResponseBodyDataExtTextInImageOcrResultLocation(DaraModel):
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
        # The distance between the upper-left corner of the text area and the y-axis, using the upper-left corner of the image as the coordinate origin, in pixels.
        self.x = x
        # The distance between the upper left corner of the text area and the x-axis, with the upper left corner of the image as the coordinate origin, in pixels.
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

class ImageModerationResponseBodyDataExtTextInImageCustomText(DaraModel):
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

class ImageModerationResponseBodyDataExtRecognition(DaraModel):
    def __init__(
        self,
        classification: str = None,
        confidence: float = None,
    ):
        # The category of image recognition.
        self.classification = classification
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places. Some labels do not have scores of confidence levels.
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classification is not None:
            result['Classification'] = self.classification

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        return self

class ImageModerationResponseBodyDataExtPublicFigure(DaraModel):
    def __init__(
        self,
        figure_id: str = None,
        figure_name: str = None,
        location: List[main_models.ImageModerationResponseBodyDataExtPublicFigureLocation] = None,
    ):
        # Identified person coding information.
        self.figure_id = figure_id
        # Identified person name information.
        self.figure_name = figure_name
        # the data array of location info
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
                temp_model = main_models.ImageModerationResponseBodyDataExtPublicFigureLocation()
                self.location.append(temp_model.from_map(k1))

        return self

class ImageModerationResponseBodyDataExtPublicFigureLocation(DaraModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        # The height
        self.h = h
        # The weight
        self.w = w
        # X coordinate
        self.x = x
        # Y coordinate
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

class ImageModerationResponseBodyDataExtOcrResult(DaraModel):
    def __init__(
        self,
        location: main_models.ImageModerationResponseBodyDataExtOcrResultLocation = None,
        text: str = None,
    ):
        # Location information.
        self.location = location
        # The text information in the recognized image.
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
            temp_model = main_models.ImageModerationResponseBodyDataExtOcrResultLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class ImageModerationResponseBodyDataExtOcrResultLocation(DaraModel):
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
        # The distance between the upper-left corner of the text area and the y-axis, using the upper-left corner of the image as the coordinate origin, in pixels.
        self.x = x
        # The distance between the upper left corner of the text area and the x-axis, with the upper left corner of the image as the coordinate origin, in pixels.
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

class ImageModerationResponseBodyDataExtLogoData(DaraModel):
    def __init__(
        self,
        location: main_models.ImageModerationResponseBodyDataExtLogoDataLocation = None,
        logo: List[main_models.ImageModerationResponseBodyDataExtLogoDataLogo] = None,
    ):
        # Location information.
        self.location = location
        # Logo information.
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
            temp_model = main_models.ImageModerationResponseBodyDataExtLogoDataLocation()
            self.location = temp_model.from_map(m.get('Location'))

        self.logo = []
        if m.get('Logo') is not None:
            for k1 in m.get('Logo'):
                temp_model = main_models.ImageModerationResponseBodyDataExtLogoDataLogo()
                self.logo.append(temp_model.from_map(k1))

        return self

class ImageModerationResponseBodyDataExtLogoDataLogo(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
        name: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places. Some labels do not have scores of confidence levels.
        self.confidence = confidence
        # Logo category.
        self.label = label
        # Logo name.
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

class ImageModerationResponseBodyDataExtLogoDataLocation(DaraModel):
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
        # The distance between the upper-left corner of the text area and the y-axis, using the upper-left corner of the image as the coordinate origin, in pixels.
        self.x = x
        # The distance between the upper left corner of the text area and the x-axis, with the upper left corner of the image as the coordinate origin, in pixels.
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

class ImageModerationResponseBodyDataExtFaceData(DaraModel):
    def __init__(
        self,
        age: int = None,
        bang: main_models.ImageModerationResponseBodyDataExtFaceDataBang = None,
        gender: main_models.ImageModerationResponseBodyDataExtFaceDataGender = None,
        glasses: str = None,
        hairstyle: main_models.ImageModerationResponseBodyDataExtFaceDataHairstyle = None,
        hat: main_models.ImageModerationResponseBodyDataExtFaceDataHat = None,
        location: main_models.ImageModerationResponseBodyDataExtFaceDataLocation = None,
        mask: main_models.ImageModerationResponseBodyDataExtFaceDataMask = None,
        mustache: main_models.ImageModerationResponseBodyDataExtFaceDataMustache = None,
        quality: main_models.ImageModerationResponseBodyDataExtFaceDataQuality = None,
        smile: float = None,
    ):
        # The age recognition result.
        self.age = age
        # Indicates whether the recognition result of bangs is available.
        self.bang = bang
        # The gender recognition result.
        self.gender = gender
        # The recognition result of whether to wear glasses.
        # 
        # - None: No glasses.
        # 
        # - Wear: Wear glasses.
        # 
        # - Sunglass: Wear sunglasses.
        self.glasses = glasses
        # The hairstyle recognition result.
        self.hairstyle = hairstyle
        # The recognition result of whether to wear a hat.
        self.hat = hat
        # The location of the face.
        self.location = location
        # The recognition result of whether to wear a mask.
        self.mask = mask
        # The identification result of whether there is a beard.
        self.mustache = mustache
        # The quality information of the face image.
        self.quality = quality
        # The smiling degree of the face.
        self.smile = smile

    def validate(self):
        if self.bang:
            self.bang.validate()
        if self.gender:
            self.gender.validate()
        if self.hairstyle:
            self.hairstyle.validate()
        if self.hat:
            self.hat.validate()
        if self.location:
            self.location.validate()
        if self.mask:
            self.mask.validate()
        if self.mustache:
            self.mustache.validate()
        if self.quality:
            self.quality.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.age is not None:
            result['Age'] = self.age

        if self.bang is not None:
            result['Bang'] = self.bang.to_map()

        if self.gender is not None:
            result['Gender'] = self.gender.to_map()

        if self.glasses is not None:
            result['Glasses'] = self.glasses

        if self.hairstyle is not None:
            result['Hairstyle'] = self.hairstyle.to_map()

        if self.hat is not None:
            result['Hat'] = self.hat.to_map()

        if self.location is not None:
            result['Location'] = self.location.to_map()

        if self.mask is not None:
            result['Mask'] = self.mask.to_map()

        if self.mustache is not None:
            result['Mustache'] = self.mustache.to_map()

        if self.quality is not None:
            result['Quality'] = self.quality.to_map()

        if self.smile is not None:
            result['Smile'] = self.smile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')

        if m.get('Bang') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtFaceDataBang()
            self.bang = temp_model.from_map(m.get('Bang'))

        if m.get('Gender') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtFaceDataGender()
            self.gender = temp_model.from_map(m.get('Gender'))

        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')

        if m.get('Hairstyle') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtFaceDataHairstyle()
            self.hairstyle = temp_model.from_map(m.get('Hairstyle'))

        if m.get('Hat') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtFaceDataHat()
            self.hat = temp_model.from_map(m.get('Hat'))

        if m.get('Location') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtFaceDataLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('Mask') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtFaceDataMask()
            self.mask = temp_model.from_map(m.get('Mask'))

        if m.get('Mustache') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtFaceDataMustache()
            self.mustache = temp_model.from_map(m.get('Mustache'))

        if m.get('Quality') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtFaceDataQuality()
            self.quality = temp_model.from_map(m.get('Quality'))

        if m.get('Smile') is not None:
            self.smile = m.get('Smile')

        return self

class ImageModerationResponseBodyDataExtFaceDataQuality(DaraModel):
    def __init__(
        self,
        blur: float = None,
        integrity: float = None,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        # The blur of the face image. Valid values: 0 to 100. The higher the score, the more fuzzy it is.
        # Recommended values: 0 to 25.
        self.blur = blur
        # The integrity of the human face. Recommended values:80 to 100.
        self.integrity = integrity
        # The head-up or head-down angle of the face.
        # Recommended values:-30 to 30.
        self.pitch = pitch
        # The plane rotation angle of the face.
        # Recommended values:-30 to 30.
        self.roll = roll
        # The left and right shaking angle of the human face.
        # Recommended values:-30 to 30.
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blur is not None:
            result['Blur'] = self.blur

        if self.integrity is not None:
            result['Integrity'] = self.integrity

        if self.pitch is not None:
            result['Pitch'] = self.pitch

        if self.roll is not None:
            result['Roll'] = self.roll

        if self.yaw is not None:
            result['Yaw'] = self.yaw

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')

        if m.get('Integrity') is not None:
            self.integrity = m.get('Integrity')

        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')

        if m.get('Roll') is not None:
            self.roll = m.get('Roll')

        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')

        return self

class ImageModerationResponseBodyDataExtFaceDataMustache(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        # The confidence level of the result of the beard. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence
        # The identification result of whether there is a beard.Valid values:
        # 
        # - Has:have a beard.
        # 
        # - None:No beard.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ImageModerationResponseBodyDataExtFaceDataMask(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        # The confidence level of the result of wearing the mask. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence
        # The recognition result of whether to wear a mask. Valid values:
        # 
        # - Wear a mask.
        # 
        #  - None: No mask.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ImageModerationResponseBodyDataExtFaceDataLocation(DaraModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        # The height of the face area. Unit: pixels.
        self.h = h
        # The width of the face area. Unit: pixels.
        self.w = w
        # The distance from the upper-left corner of the face area to the y-axis with the upper-left corner of the image as the coordinate origin. Unit: pixels.
        self.x = x
        # The distance from the upper-left corner of the face area to the x-axis with the upper-left corner of the image as the coordinate origin. Unit: pixels.
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

class ImageModerationResponseBodyDataExtFaceDataHat(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        # The confidence level of the result of wearing the hat. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence
        # The recognition result of whether to wear the hat. Valid values:
        # 
        # - Wear: Wear a hat.
        # 
        # - None: No hat.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ImageModerationResponseBodyDataExtFaceDataHairstyle(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        # The confidence level of the hairstyle recognition result. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence
        # The hairstyle recognition result. Valid values:
        # 
        # - Bald: bald head.
        # 
        # - Long: Long hair.
        # 
        # - Short: Short hair.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ImageModerationResponseBodyDataExtFaceDataGender(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        # The confidence level of the gender recognition result. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence
        # The gender recognition result. Valid values:
        # 
        # - Male
        # 
        # - FeMale
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ImageModerationResponseBodyDataExtFaceDataBang(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        value: str = None,
    ):
        # The confidence level of the bang recognition result. Valid values: 0 to 100. A higher value indicates a more credible result.
        self.confidence = confidence
        # Indicates whether the recognition result of bangs is available.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ImageModerationResponseBodyDataExtCustomImage(DaraModel):
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

class ImageModerationResponseBodyDataExtAigcData(DaraModel):
    def __init__(
        self,
        aigc: main_models.ImageModerationResponseBodyDataExtAigcDataAIGC = None,
    ):
        self.aigc = aigc

    def validate(self):
        if self.aigc:
            self.aigc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aigc is not None:
            result['AIGC'] = self.aigc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIGC') is not None:
            temp_model = main_models.ImageModerationResponseBodyDataExtAigcDataAIGC()
            self.aigc = temp_model.from_map(m.get('AIGC'))

        return self

class ImageModerationResponseBodyDataExtAigcDataAIGC(DaraModel):
    def __init__(
        self,
        content_producer: str = None,
        content_propagator: str = None,
        label: str = None,
        produce_id: str = None,
        propagate_id: str = None,
        reserved_code_1: str = None,
        reserved_code_2: str = None,
    ):
        self.content_producer = content_producer
        self.content_propagator = content_propagator
        self.label = label
        self.produce_id = produce_id
        self.propagate_id = propagate_id
        self.reserved_code_1 = reserved_code_1
        self.reserved_code_2 = reserved_code_2

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_producer is not None:
            result['ContentProducer'] = self.content_producer

        if self.content_propagator is not None:
            result['ContentPropagator'] = self.content_propagator

        if self.label is not None:
            result['Label'] = self.label

        if self.produce_id is not None:
            result['ProduceID'] = self.produce_id

        if self.propagate_id is not None:
            result['PropagateID'] = self.propagate_id

        if self.reserved_code_1 is not None:
            result['ReservedCode1'] = self.reserved_code_1

        if self.reserved_code_2 is not None:
            result['ReservedCode2'] = self.reserved_code_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentProducer') is not None:
            self.content_producer = m.get('ContentProducer')

        if m.get('ContentPropagator') is not None:
            self.content_propagator = m.get('ContentPropagator')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('ProduceID') is not None:
            self.produce_id = m.get('ProduceID')

        if m.get('PropagateID') is not None:
            self.propagate_id = m.get('PropagateID')

        if m.get('ReservedCode1') is not None:
            self.reserved_code_1 = m.get('ReservedCode1')

        if m.get('ReservedCode2') is not None:
            self.reserved_code_2 = m.get('ReservedCode2')

        return self

