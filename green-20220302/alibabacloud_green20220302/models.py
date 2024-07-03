# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class DescribeFileModerationResultRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation(TeaModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeFileModerationResultResponseBodyDataPageResultImageResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        label_result: List[DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult] = None,
        location: DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation = None,
        service: str = None,
    ):
        self.description = description
        self.label_result = label_result
        self.location = location
        self.service = service

    def validate(self):
        if self.label_result:
            for k in self.label_result:
                if k:
                    k.validate()
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['LabelResult'] = []
        if self.label_result is not None:
            for k in self.label_result:
                result['LabelResult'].append(k.to_map() if k else None)
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.label_result = []
        if m.get('LabelResult') is not None:
            for k in m.get('LabelResult'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult()
                self.label_result.append(temp_model.from_map(k))
        if m.get('Location') is not None:
            temp_model = DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultTextResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        labels: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        service: str = None,
        text: str = None,
        text_segment: str = None,
    ):
        self.description = description
        self.labels = labels
        self.risk_tips = risk_tips
        self.risk_words = risk_words
        self.service = service
        self.text = text
        self.text_segment = text_segment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.service is not None:
            result['Service'] = self.service
        if self.text is not None:
            result['Text'] = self.text
        if self.text_segment is not None:
            result['TextSegment'] = self.text_segment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextSegment') is not None:
            self.text_segment = m.get('TextSegment')
        return self


class DescribeFileModerationResultResponseBodyDataPageResult(TeaModel):
    def __init__(
        self,
        image_result: List[DescribeFileModerationResultResponseBodyDataPageResultImageResult] = None,
        image_url: str = None,
        page_num: int = None,
        text_result: List[DescribeFileModerationResultResponseBodyDataPageResultTextResult] = None,
        text_url: str = None,
    ):
        self.image_result = image_result
        self.image_url = image_url
        self.page_num = page_num
        self.text_result = text_result
        self.text_url = text_url

    def validate(self):
        if self.image_result:
            for k in self.image_result:
                if k:
                    k.validate()
        if self.text_result:
            for k in self.text_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageResult'] = []
        if self.image_result is not None:
            for k in self.image_result:
                result['ImageResult'].append(k.to_map() if k else None)
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        result['TextResult'] = []
        if self.text_result is not None:
            for k in self.text_result:
                result['TextResult'].append(k.to_map() if k else None)
        if self.text_url is not None:
            result['TextUrl'] = self.text_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_result = []
        if m.get('ImageResult') is not None:
            for k in m.get('ImageResult'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageResultImageResult()
                self.image_result.append(temp_model.from_map(k))
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        self.text_result = []
        if m.get('TextResult') is not None:
            for k in m.get('TextResult'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageResultTextResult()
                self.text_result.append(temp_model.from_map(k))
        if m.get('TextUrl') is not None:
            self.text_url = m.get('TextUrl')
        return self


class DescribeFileModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        doc_type: str = None,
        page_result: List[DescribeFileModerationResultResponseBodyDataPageResult] = None,
        url: str = None,
    ):
        self.data_id = data_id
        self.doc_type = doc_type
        self.page_result = page_result
        self.url = url

    def validate(self):
        if self.page_result:
            for k in self.page_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        result['PageResult'] = []
        if self.page_result is not None:
            for k in self.page_result:
                result['PageResult'].append(k.to_map() if k else None)
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        self.page_result = []
        if m.get('PageResult') is not None:
            for k in m.get('PageResult'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageResult()
                self.page_result.append(temp_model.from_map(k))
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeFileModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeFileModerationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeFileModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeFileModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeFileModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeFileModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageModerationResultRequest(TeaModel):
    def __init__(
        self,
        req_id: str = None,
    ):
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class DescribeImageModerationResultResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeImageModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        frame: str = None,
        frame_num: int = None,
        req_id: str = None,
        result: List[DescribeImageModerationResultResponseBodyDataResult] = None,
        risk_level: str = None,
    ):
        self.data_id = data_id
        self.frame = frame
        self.frame_num = frame_num
        self.req_id = req_id
        self.result = result
        self.risk_level = risk_level

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.frame is not None:
            result['Frame'] = self.frame
        if self.frame_num is not None:
            result['FrameNum'] = self.frame_num
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Frame') is not None:
            self.frame = m.get('Frame')
        if m.get('FrameNum') is not None:
            self.frame_num = m.get('FrameNum')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeImageModerationResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeImageModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeImageModerationResultResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeImageModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeImageModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageResultExtRequest(TeaModel):
    def __init__(
        self,
        info_type: str = None,
        req_id: str = None,
    ):
        self.info_type = info_type
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info_type is not None:
            result['InfoType'] = self.info_type
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoType') is not None:
            self.info_type = m.get('InfoType')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class DescribeImageResultExtResponseBodyDataCustomImage(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        # 图片ID。
        self.image_id = image_id
        # 图库ID。
        self.lib_id = lib_id
        # 图库名。
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeImageResultExtResponseBodyDataPublicFigure(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        # 人物ID。
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class DescribeImageResultExtResponseBodyDataTextInImageCustomTexts(TeaModel):
    def __init__(
        self,
        key_words: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        self.key_words = key_words
        self.lib_id = lib_id
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeImageResultExtResponseBodyDataTextInImage(TeaModel):
    def __init__(
        self,
        custom_texts: List[DescribeImageResultExtResponseBodyDataTextInImageCustomTexts] = None,
        ocr_datas: List[str] = None,
        risk_words: List[str] = None,
    ):
        self.custom_texts = custom_texts
        self.ocr_datas = ocr_datas
        self.risk_words = risk_words

    def validate(self):
        if self.custom_texts:
            for k in self.custom_texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomTexts'] = []
        if self.custom_texts is not None:
            for k in self.custom_texts:
                result['CustomTexts'].append(k.to_map() if k else None)
        if self.ocr_datas is not None:
            result['OcrDatas'] = self.ocr_datas
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_texts = []
        if m.get('CustomTexts') is not None:
            for k in m.get('CustomTexts'):
                temp_model = DescribeImageResultExtResponseBodyDataTextInImageCustomTexts()
                self.custom_texts.append(temp_model.from_map(k))
        if m.get('OcrDatas') is not None:
            self.ocr_datas = m.get('OcrDatas')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        return self


class DescribeImageResultExtResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_image: List[DescribeImageResultExtResponseBodyDataCustomImage] = None,
        public_figure: List[DescribeImageResultExtResponseBodyDataPublicFigure] = None,
        text_in_image: DescribeImageResultExtResponseBodyDataTextInImage = None,
    ):
        self.custom_image = custom_image
        self.public_figure = public_figure
        self.text_in_image = text_in_image

    def validate(self):
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.public_figure:
            for k in self.public_figure:
                if k:
                    k.validate()
        if self.text_in_image:
            self.text_in_image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k in self.custom_image:
                result['CustomImage'].append(k.to_map() if k else None)
        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k in self.public_figure:
                result['PublicFigure'].append(k.to_map() if k else None)
        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k in m.get('CustomImage'):
                temp_model = DescribeImageResultExtResponseBodyDataCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k in m.get('PublicFigure'):
                temp_model = DescribeImageResultExtResponseBodyDataPublicFigure()
                self.public_figure.append(temp_model.from_map(k))
        if m.get('TextInImage') is not None:
            temp_model = DescribeImageResultExtResponseBodyDataTextInImage()
            self.text_in_image = temp_model.from_map(m['TextInImage'])
        return self


class DescribeImageResultExtResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeImageResultExtResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeImageResultExtResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeImageResultExtResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageResultExtResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeImageResultExtResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket_name: str = None,
        expiration: int = None,
        file_name_prefix: str = None,
        oss_internal_end_point: str = None,
        oss_internet_end_point: str = None,
        security_token: str = None,
    ):
        self.access_key_id = access_key_id
        self.access_key_secret = access_key_secret
        self.bucket_name = bucket_name
        self.expiration = expiration
        self.file_name_prefix = file_name_prefix
        self.oss_internal_end_point = oss_internal_end_point
        self.oss_internet_end_point = oss_internet_end_point
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix
        if self.oss_internal_end_point is not None:
            result['OssInternalEndPoint'] = self.oss_internal_end_point
        if self.oss_internet_end_point is not None:
            result['OssInternetEndPoint'] = self.oss_internet_end_point
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')
        if m.get('OssInternalEndPoint') is not None:
            self.oss_internal_end_point = m.get('OssInternalEndPoint')
        if m.get('OssInternetEndPoint') is not None:
            self.oss_internet_end_point = m.get('OssInternetEndPoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeUploadTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeUploadTokenResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeUploadTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUploadTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUploadTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUrlModerationResultRequest(TeaModel):
    def __init__(
        self,
        req_id: str = None,
    ):
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class DescribeUrlModerationResultResponseBodyDataExtraInfo(TeaModel):
    def __init__(
        self,
        icp_no: str = None,
        icp_type: str = None,
    ):
        self.icp_no = icp_no
        self.icp_type = icp_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icp_no is not None:
            result['IcpNo'] = self.icp_no
        if self.icp_type is not None:
            result['IcpType'] = self.icp_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IcpNo') is not None:
            self.icp_no = m.get('IcpNo')
        if m.get('IcpType') is not None:
            self.icp_type = m.get('IcpType')
        return self


class DescribeUrlModerationResultResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class DescribeUrlModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        extra_info: DescribeUrlModerationResultResponseBodyDataExtraInfo = None,
        req_id: str = None,
        result: List[DescribeUrlModerationResultResponseBodyDataResult] = None,
    ):
        self.data_id = data_id
        self.extra_info = extra_info
        self.req_id = req_id
        self.result = result

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ExtraInfo') is not None:
            temp_model = DescribeUrlModerationResultResponseBodyDataExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeUrlModerationResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeUrlModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeUrlModerationResultResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeUrlModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUrlModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUrlModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUrlModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FileModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class FileModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FileModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FileModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = FileModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FileModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FileModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FileModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageAsyncModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ImageAsyncModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        req_id: str = None,
    ):
        self.data_id = data_id
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class ImageAsyncModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ImageAsyncModerationResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ImageAsyncModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageAsyncModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImageAsyncModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ImageAsyncModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ImageModerationResponseBodyDataExtCustomImage(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        self.image_id = image_id
        self.lib_id = lib_id
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtLogoDataLocation(TeaModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtLogoDataLogo(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
        name: str = None,
    ):
        self.confidence = confidence
        self.label = label
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtLogoData(TeaModel):
    def __init__(
        self,
        location: ImageModerationResponseBodyDataExtLogoDataLocation = None,
        logo: List[ImageModerationResponseBodyDataExtLogoDataLogo] = None,
    ):
        self.location = location
        self.logo = logo

    def validate(self):
        if self.location:
            self.location.validate()
        if self.logo:
            for k in self.logo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        result['Logo'] = []
        if self.logo is not None:
            for k in self.logo:
                result['Logo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = ImageModerationResponseBodyDataExtLogoDataLocation()
            self.location = temp_model.from_map(m['Location'])
        self.logo = []
        if m.get('Logo') is not None:
            for k in m.get('Logo'):
                temp_model = ImageModerationResponseBodyDataExtLogoDataLogo()
                self.logo.append(temp_model.from_map(k))
        return self


class ImageModerationResponseBodyDataExtOcrResultLocation(TeaModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtOcrResult(TeaModel):
    def __init__(
        self,
        location: ImageModerationResponseBodyDataExtOcrResultLocation = None,
        text: str = None,
    ):
        self.location = location
        self.text = text

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = ImageModerationResponseBodyDataExtOcrResultLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ImageModerationResponseBodyDataExtPublicFigure(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
        figure_name: str = None,
    ):
        self.figure_id = figure_id
        self.figure_name = figure_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_name is not None:
            result['FigureName'] = self.figure_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureName') is not None:
            self.figure_name = m.get('FigureName')
        return self


class ImageModerationResponseBodyDataExtRecognition(TeaModel):
    def __init__(
        self,
        classification: str = None,
        confidence: float = None,
    ):
        self.classification = classification
        self.confidence = confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtTextInImageCustomText(TeaModel):
    def __init__(
        self,
        key_words: str = None,
        lib_id: str = None,
        lib_name: str = None,
    ):
        self.key_words = key_words
        self.lib_id = lib_id
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtTextInImageOcrResultLocation(TeaModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtTextInImageOcrResult(TeaModel):
    def __init__(
        self,
        location: ImageModerationResponseBodyDataExtTextInImageOcrResultLocation = None,
        text: str = None,
    ):
        self.location = location
        self.text = text

    def validate(self):
        if self.location:
            self.location.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Location') is not None:
            temp_model = ImageModerationResponseBodyDataExtTextInImageOcrResultLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ImageModerationResponseBodyDataExtTextInImage(TeaModel):
    def __init__(
        self,
        custom_text: List[ImageModerationResponseBodyDataExtTextInImageCustomText] = None,
        ocr_result: List[ImageModerationResponseBodyDataExtTextInImageOcrResult] = None,
        risk_word: List[str] = None,
    ):
        self.custom_text = custom_text
        self.ocr_result = ocr_result
        self.risk_word = risk_word

    def validate(self):
        if self.custom_text:
            for k in self.custom_text:
                if k:
                    k.validate()
        if self.ocr_result:
            for k in self.ocr_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomText'] = []
        if self.custom_text is not None:
            for k in self.custom_text:
                result['CustomText'].append(k.to_map() if k else None)
        result['OcrResult'] = []
        if self.ocr_result is not None:
            for k in self.ocr_result:
                result['OcrResult'].append(k.to_map() if k else None)
        if self.risk_word is not None:
            result['RiskWord'] = self.risk_word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_text = []
        if m.get('CustomText') is not None:
            for k in m.get('CustomText'):
                temp_model = ImageModerationResponseBodyDataExtTextInImageCustomText()
                self.custom_text.append(temp_model.from_map(k))
        self.ocr_result = []
        if m.get('OcrResult') is not None:
            for k in m.get('OcrResult'):
                temp_model = ImageModerationResponseBodyDataExtTextInImageOcrResult()
                self.ocr_result.append(temp_model.from_map(k))
        if m.get('RiskWord') is not None:
            self.risk_word = m.get('RiskWord')
        return self


class ImageModerationResponseBodyDataExt(TeaModel):
    def __init__(
        self,
        custom_image: List[ImageModerationResponseBodyDataExtCustomImage] = None,
        logo_data: List[ImageModerationResponseBodyDataExtLogoData] = None,
        ocr_result: List[ImageModerationResponseBodyDataExtOcrResult] = None,
        public_figure: List[ImageModerationResponseBodyDataExtPublicFigure] = None,
        recognition: List[ImageModerationResponseBodyDataExtRecognition] = None,
        text_in_image: ImageModerationResponseBodyDataExtTextInImage = None,
    ):
        self.custom_image = custom_image
        self.logo_data = logo_data
        self.ocr_result = ocr_result
        self.public_figure = public_figure
        self.recognition = recognition
        self.text_in_image = text_in_image

    def validate(self):
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.logo_data:
            for k in self.logo_data:
                if k:
                    k.validate()
        if self.ocr_result:
            for k in self.ocr_result:
                if k:
                    k.validate()
        if self.public_figure:
            for k in self.public_figure:
                if k:
                    k.validate()
        if self.recognition:
            for k in self.recognition:
                if k:
                    k.validate()
        if self.text_in_image:
            self.text_in_image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k in self.custom_image:
                result['CustomImage'].append(k.to_map() if k else None)
        result['LogoData'] = []
        if self.logo_data is not None:
            for k in self.logo_data:
                result['LogoData'].append(k.to_map() if k else None)
        result['OcrResult'] = []
        if self.ocr_result is not None:
            for k in self.ocr_result:
                result['OcrResult'].append(k.to_map() if k else None)
        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k in self.public_figure:
                result['PublicFigure'].append(k.to_map() if k else None)
        result['Recognition'] = []
        if self.recognition is not None:
            for k in self.recognition:
                result['Recognition'].append(k.to_map() if k else None)
        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k in m.get('CustomImage'):
                temp_model = ImageModerationResponseBodyDataExtCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        self.logo_data = []
        if m.get('LogoData') is not None:
            for k in m.get('LogoData'):
                temp_model = ImageModerationResponseBodyDataExtLogoData()
                self.logo_data.append(temp_model.from_map(k))
        self.ocr_result = []
        if m.get('OcrResult') is not None:
            for k in m.get('OcrResult'):
                temp_model = ImageModerationResponseBodyDataExtOcrResult()
                self.ocr_result.append(temp_model.from_map(k))
        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k in m.get('PublicFigure'):
                temp_model = ImageModerationResponseBodyDataExtPublicFigure()
                self.public_figure.append(temp_model.from_map(k))
        self.recognition = []
        if m.get('Recognition') is not None:
            for k in m.get('Recognition'):
                temp_model = ImageModerationResponseBodyDataExtRecognition()
                self.recognition.append(temp_model.from_map(k))
        if m.get('TextInImage') is not None:
            temp_model = ImageModerationResponseBodyDataExtTextInImage()
            self.text_in_image = temp_model.from_map(m['TextInImage'])
        return self


class ImageModerationResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ImageModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        ext: ImageModerationResponseBodyDataExt = None,
        result: List[ImageModerationResponseBodyDataResult] = None,
        risk_level: str = None,
    ):
        self.data_id = data_id
        self.ext = ext
        self.result = result
        self.risk_level = risk_level

    def validate(self):
        if self.ext:
            self.ext.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.ext is not None:
            result['Ext'] = self.ext.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Ext') is not None:
            temp_model = ImageModerationResponseBodyDataExt()
            self.ext = temp_model.from_map(m['Ext'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ImageModerationResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ImageModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ImageModerationResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ImageModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImageModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ImageModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TextModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class TextModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        device_id: str = None,
        labels: str = None,
        reason: str = None,
    ):
        self.account_id = account_id
        self.device_id = device_id
        self.labels = labels
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.labels is not None:
            result['labels'] = self.labels
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class TextModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TextModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TextModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TextModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TextModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TextModerationPlusRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class TextModerationPlusResponseBodyDataAdvice(TeaModel):
    def __init__(
        self,
        answer: str = None,
        hit_label: str = None,
        hit_lib_name: str = None,
    ):
        self.answer = answer
        self.hit_label = hit_label
        self.hit_lib_name = hit_lib_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['Answer'] = self.answer
        if self.hit_label is not None:
            result['HitLabel'] = self.hit_label
        if self.hit_lib_name is not None:
            result['HitLibName'] = self.hit_lib_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')
        if m.get('HitLabel') is not None:
            self.hit_label = m.get('HitLabel')
        if m.get('HitLibName') is not None:
            self.hit_lib_name = m.get('HitLibName')
        return self


class TextModerationPlusResponseBodyDataResultCustomizedHit(TeaModel):
    def __init__(
        self,
        key_words: str = None,
        lib_name: str = None,
    ):
        self.key_words = key_words
        self.lib_name = lib_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_words is not None:
            result['KeyWords'] = self.key_words
        if self.lib_name is not None:
            result['LibName'] = self.lib_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')
        if m.get('LibName') is not None:
            self.lib_name = m.get('LibName')
        return self


class TextModerationPlusResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        customized_hit: List[TextModerationPlusResponseBodyDataResultCustomizedHit] = None,
        label: str = None,
        risk_words: str = None,
    ):
        self.confidence = confidence
        self.customized_hit = customized_hit
        self.label = label
        self.risk_words = risk_words

    def validate(self):
        if self.customized_hit:
            for k in self.customized_hit:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        result['CustomizedHit'] = []
        if self.customized_hit is not None:
            for k in self.customized_hit:
                result['CustomizedHit'].append(k.to_map() if k else None)
        if self.label is not None:
            result['Label'] = self.label
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        self.customized_hit = []
        if m.get('CustomizedHit') is not None:
            for k in m.get('CustomizedHit'):
                temp_model = TextModerationPlusResponseBodyDataResultCustomizedHit()
                self.customized_hit.append(temp_model.from_map(k))
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        return self


class TextModerationPlusResponseBodyData(TeaModel):
    def __init__(
        self,
        advice: List[TextModerationPlusResponseBodyDataAdvice] = None,
        result: List[TextModerationPlusResponseBodyDataResult] = None,
        risk_level: str = None,
        score: float = None,
    ):
        self.advice = advice
        self.result = result
        self.risk_level = risk_level
        self.score = score

    def validate(self):
        if self.advice:
            for k in self.advice:
                if k:
                    k.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Advice'] = []
        if self.advice is not None:
            for k in self.advice:
                result['Advice'].append(k.to_map() if k else None)
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advice = []
        if m.get('Advice') is not None:
            for k in m.get('Advice'):
                temp_model = TextModerationPlusResponseBodyDataAdvice()
                self.advice.append(temp_model.from_map(k))
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = TextModerationPlusResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class TextModerationPlusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: TextModerationPlusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TextModerationPlusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TextModerationPlusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TextModerationPlusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TextModerationPlusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UrlAsyncModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class UrlAsyncModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        req_id: str = None,
    ):
        self.data_id = data_id
        self.req_id = req_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.req_id is not None:
            result['ReqId'] = self.req_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')
        return self


class UrlAsyncModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: UrlAsyncModerationResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UrlAsyncModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UrlAsyncModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UrlAsyncModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UrlAsyncModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        task_id: str = None,
    ):
        self.data_id = data_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VideoModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: VideoModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VideoModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VideoModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VideoModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationCancelRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationCancelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationCancelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VideoModerationCancelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VideoModerationCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoModerationResultRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VideoModerationResultResponseBodyDataAudioResultAudioSummarys(TeaModel):
    def __init__(
        self,
        label: str = None,
        label_sum: int = None,
    ):
        self.label = label
        self.label_sum = label_sum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')
        return self


class VideoModerationResultResponseBodyDataAudioResultSliceDetails(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        end_timestamp: int = None,
        extend: str = None,
        labels: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        score: float = None,
        start_time: int = None,
        start_timestamp: int = None,
        text: str = None,
        url: str = None,
    ):
        self.end_time = end_time
        self.end_timestamp = end_timestamp
        self.extend = extend
        self.labels = labels
        self.risk_tips = risk_tips
        self.risk_words = risk_words
        self.score = score
        self.start_time = start_time
        self.start_timestamp = start_timestamp
        self.text = text
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.score is not None:
            result['Score'] = self.score
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.text is not None:
            result['Text'] = self.text
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VideoModerationResultResponseBodyDataAudioResult(TeaModel):
    def __init__(
        self,
        audio_summarys: List[VideoModerationResultResponseBodyDataAudioResultAudioSummarys] = None,
        slice_details: List[VideoModerationResultResponseBodyDataAudioResultSliceDetails] = None,
    ):
        self.audio_summarys = audio_summarys
        self.slice_details = slice_details

    def validate(self):
        if self.audio_summarys:
            for k in self.audio_summarys:
                if k:
                    k.validate()
        if self.slice_details:
            for k in self.slice_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AudioSummarys'] = []
        if self.audio_summarys is not None:
            for k in self.audio_summarys:
                result['AudioSummarys'].append(k.to_map() if k else None)
        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k in self.slice_details:
                result['SliceDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_summarys = []
        if m.get('AudioSummarys') is not None:
            for k in m.get('AudioSummarys'):
                temp_model = VideoModerationResultResponseBodyDataAudioResultAudioSummarys()
                self.audio_summarys.append(temp_model.from_map(k))
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k in m.get('SliceDetails'):
                temp_model = VideoModerationResultResponseBodyDataAudioResultSliceDetails()
                self.slice_details.append(temp_model.from_map(k))
        return self


class VideoModerationResultResponseBodyDataFrameResultFrameSummarys(TeaModel):
    def __init__(
        self,
        label: str = None,
        label_sum: int = None,
    ):
        self.label = label
        self.label_sum = label_sum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        lib_id: str = None,
    ):
        self.image_id = image_id
        self.lib_id = lib_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.lib_id is not None:
            result['LibId'] = self.lib_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
    ):
        self.figure_id = figure_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResultsResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class VideoModerationResultResponseBodyDataFrameResultFramesResults(TeaModel):
    def __init__(
        self,
        custom_image: List[VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage] = None,
        public_figure: List[VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure] = None,
        result: List[VideoModerationResultResponseBodyDataFrameResultFramesResultsResult] = None,
        service: str = None,
        text_in_image: Dict[str, Any] = None,
    ):
        self.custom_image = custom_image
        self.public_figure = public_figure
        self.result = result
        self.service = service
        self.text_in_image = text_in_image

    def validate(self):
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.public_figure:
            for k in self.public_figure:
                if k:
                    k.validate()
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k in self.custom_image:
                result['CustomImage'].append(k.to_map() if k else None)
        result['PublicFigure'] = []
        if self.public_figure is not None:
            for k in self.public_figure:
                result['PublicFigure'].append(k.to_map() if k else None)
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.service is not None:
            result['Service'] = self.service
        if self.text_in_image is not None:
            result['TextInImage'] = self.text_in_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k in m.get('CustomImage'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k in m.get('PublicFigure'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure()
                self.public_figure.append(temp_model.from_map(k))
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResultsResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('TextInImage') is not None:
            self.text_in_image = m.get('TextInImage')
        return self


class VideoModerationResultResponseBodyDataFrameResultFrames(TeaModel):
    def __init__(
        self,
        offset: float = None,
        results: List[VideoModerationResultResponseBodyDataFrameResultFramesResults] = None,
        temp_url: str = None,
        timestamp: int = None,
    ):
        self.offset = offset
        self.results = results
        self.temp_url = temp_url
        self.timestamp = timestamp

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.temp_url is not None:
            result['TempUrl'] = self.temp_url
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFramesResults()
                self.results.append(temp_model.from_map(k))
        if m.get('TempUrl') is not None:
            self.temp_url = m.get('TempUrl')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class VideoModerationResultResponseBodyDataFrameResult(TeaModel):
    def __init__(
        self,
        frame_num: int = None,
        frame_summarys: List[VideoModerationResultResponseBodyDataFrameResultFrameSummarys] = None,
        frames: List[VideoModerationResultResponseBodyDataFrameResultFrames] = None,
    ):
        self.frame_num = frame_num
        self.frame_summarys = frame_summarys
        self.frames = frames

    def validate(self):
        if self.frame_summarys:
            for k in self.frame_summarys:
                if k:
                    k.validate()
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.frame_num is not None:
            result['FrameNum'] = self.frame_num
        result['FrameSummarys'] = []
        if self.frame_summarys is not None:
            for k in self.frame_summarys:
                result['FrameSummarys'].append(k.to_map() if k else None)
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameNum') is not None:
            self.frame_num = m.get('FrameNum')
        self.frame_summarys = []
        if m.get('FrameSummarys') is not None:
            for k in m.get('FrameSummarys'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFrameSummarys()
                self.frame_summarys.append(temp_model.from_map(k))
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = VideoModerationResultResponseBodyDataFrameResultFrames()
                self.frames.append(temp_model.from_map(k))
        return self


class VideoModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        audio_result: VideoModerationResultResponseBodyDataAudioResult = None,
        data_id: str = None,
        frame_result: VideoModerationResultResponseBodyDataFrameResult = None,
        live_id: str = None,
        task_id: str = None,
    ):
        self.audio_result = audio_result
        self.data_id = data_id
        self.frame_result = frame_result
        self.live_id = live_id
        self.task_id = task_id

    def validate(self):
        if self.audio_result:
            self.audio_result.validate()
        if self.frame_result:
            self.frame_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_result is not None:
            result['AudioResult'] = self.audio_result.to_map()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.frame_result is not None:
            result['FrameResult'] = self.frame_result.to_map()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioResult') is not None:
            temp_model = VideoModerationResultResponseBodyDataAudioResult()
            self.audio_result = temp_model.from_map(m['AudioResult'])
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FrameResult') is not None:
            temp_model = VideoModerationResultResponseBodyDataFrameResult()
            self.frame_result = temp_model.from_map(m['FrameResult'])
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VideoModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: VideoModerationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VideoModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VideoModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VideoModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VideoModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        task_id: str = None,
    ):
        self.data_id = data_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class VoiceModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: VoiceModerationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VoiceModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VoiceModerationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VoiceModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationCancelRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationCancelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationCancelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VoiceModerationCancelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VoiceModerationCancelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoiceModerationResultRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        self.service = service
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class VoiceModerationResultResponseBodyDataSliceDetails(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        end_timestamp: int = None,
        extend: str = None,
        labels: str = None,
        origin_algo_result: Dict[str, Any] = None,
        risk_tips: str = None,
        risk_words: str = None,
        score: float = None,
        start_time: int = None,
        start_timestamp: int = None,
        text: str = None,
        url: str = None,
    ):
        self.end_time = end_time
        self.end_timestamp = end_timestamp
        self.extend = extend
        self.labels = labels
        self.origin_algo_result = origin_algo_result
        self.risk_tips = risk_tips
        self.risk_words = risk_words
        self.score = score
        self.start_time = start_time
        self.start_timestamp = start_timestamp
        self.text = text
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.origin_algo_result is not None:
            result['OriginAlgoResult'] = self.origin_algo_result
        if self.risk_tips is not None:
            result['RiskTips'] = self.risk_tips
        if self.risk_words is not None:
            result['RiskWords'] = self.risk_words
        if self.score is not None:
            result['Score'] = self.score
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.text is not None:
            result['Text'] = self.text
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('OriginAlgoResult') is not None:
            self.origin_algo_result = m.get('OriginAlgoResult')
        if m.get('RiskTips') is not None:
            self.risk_tips = m.get('RiskTips')
        if m.get('RiskWords') is not None:
            self.risk_words = m.get('RiskWords')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VoiceModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        live_id: str = None,
        slice_details: List[VoiceModerationResultResponseBodyDataSliceDetails] = None,
        task_id: str = None,
        url: str = None,
    ):
        self.data_id = data_id
        self.live_id = live_id
        self.slice_details = slice_details
        self.task_id = task_id
        self.url = url

    def validate(self):
        if self.slice_details:
            for k in self.slice_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        result['SliceDetails'] = []
        if self.slice_details is not None:
            for k in self.slice_details:
                result['SliceDetails'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k in m.get('SliceDetails'):
                temp_model = VoiceModerationResultResponseBodyDataSliceDetails()
                self.slice_details.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class VoiceModerationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: VoiceModerationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = VoiceModerationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoiceModerationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VoiceModerationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VoiceModerationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


