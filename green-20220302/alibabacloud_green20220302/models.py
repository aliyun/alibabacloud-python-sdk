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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
        # 
        # *   taskId: required. The URL of the object that you want to moderate. Make sure that the URL can be accessed over the Internet.
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
        description: str = None,
        label: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The description.
        self.description = description
        # The details of the labels.
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


class DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation(TeaModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        # The H value of the coordinate point.
        self.h = h
        # The W value of the coordinate point.
        self.w = w
        # The X value of the coordinate point.
        self.x = x
        # The Y value of the coordinate point.
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
        risk_level: str = None,
        service: str = None,
    ):
        # The description.
        self.description = description
        # The label information.
        self.label_result = label_result
        # The location information
        self.location = location
        # Risk Level
        self.risk_level = risk_level
        # The moderation service.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class DescribeFileModerationResultResponseBodyDataPageResultTextResult(TeaModel):
    def __init__(
        self,
        description: str = None,
        labels: str = None,
        risk_level: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        service: str = None,
        text: str = None,
        text_segment: str = None,
    ):
        # The description.
        self.description = description
        # The details of the labels.
        self.labels = labels
        # Risk Level
        self.risk_level = risk_level
        # The risk details that are hit.
        self.risk_tips = risk_tips
        # The risk words that are hit.
        self.risk_words = risk_words
        # The moderation service.
        self.service = service
        # The text content.
        self.text = text
        # The text segmentation information.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
        # The image moderation results.
        self.image_result = image_result
        # The image URL.
        self.image_url = image_url
        # The page number.
        self.page_num = page_num
        # The text moderation results.
        self.text_result = text_result
        # The text URL.
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


class DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels(TeaModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        label_sum: int = None,
    ):
        # The description.
        self.description = description
        # The details of the labels.
        self.label = label
        # The number of times that the label is matched.
        self.label_sum = label_sum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelSum') is not None:
            self.label_sum = m.get('LabelSum')
        return self


class DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary(TeaModel):
    def __init__(
        self,
        image_labels: List[DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels] = None,
        risk_level: str = None,
    ):
        # Image Label
        self.image_labels = image_labels
        # Risk Level
        self.risk_level = risk_level

    def validate(self):
        if self.image_labels:
            for k in self.image_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageLabels'] = []
        if self.image_labels is not None:
            for k in self.image_labels:
                result['ImageLabels'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_labels = []
        if m.get('ImageLabels') is not None:
            for k in m.get('ImageLabels'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels()
                self.image_labels.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels(TeaModel):
    def __init__(
        self,
        label: str = None,
        label_sum: int = None,
    ):
        # The details of the labels.
        self.label = label
        # The number of times that the label is matched.
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


class DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary(TeaModel):
    def __init__(
        self,
        risk_level: str = None,
        text_labels: List[DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels] = None,
    ):
        # Risk Level
        self.risk_level = risk_level
        # Text Label
        self.text_labels = text_labels

    def validate(self):
        if self.text_labels:
            for k in self.text_labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        result['TextLabels'] = []
        if self.text_labels is not None:
            for k in self.text_labels:
                result['TextLabels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        self.text_labels = []
        if m.get('TextLabels') is not None:
            for k in m.get('TextLabels'):
                temp_model = DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels()
                self.text_labels.append(temp_model.from_map(k))
        return self


class DescribeFileModerationResultResponseBodyDataPageSummary(TeaModel):
    def __init__(
        self,
        image_summary: DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary = None,
        page_sum: int = None,
        text_summary: DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary = None,
    ):
        # Image Results Summary
        self.image_summary = image_summary
        # Number of pages
        self.page_sum = page_sum
        # Text Results Summary
        self.text_summary = text_summary

    def validate(self):
        if self.image_summary:
            self.image_summary.validate()
        if self.text_summary:
            self.text_summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_summary is not None:
            result['ImageSummary'] = self.image_summary.to_map()
        if self.page_sum is not None:
            result['PageSum'] = self.page_sum
        if self.text_summary is not None:
            result['TextSummary'] = self.text_summary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageSummary') is not None:
            temp_model = DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary()
            self.image_summary = temp_model.from_map(m['ImageSummary'])
        if m.get('PageSum') is not None:
            self.page_sum = m.get('PageSum')
        if m.get('TextSummary') is not None:
            temp_model = DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary()
            self.text_summary = temp_model.from_map(m['TextSummary'])
        return self


class DescribeFileModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        doc_type: str = None,
        page_result: List[DescribeFileModerationResultResponseBodyDataPageResult] = None,
        page_summary: DescribeFileModerationResultResponseBodyDataPageSummary = None,
        risk_level: str = None,
        url: str = None,
    ):
        # The ID of the moderated object.
        self.data_id = data_id
        # Optional. The document type.
        self.doc_type = doc_type
        # An array that consists of the moderation results.
        self.page_result = page_result
        # Summary of results
        self.page_summary = page_summary
        # Risk Level
        self.risk_level = risk_level
        # The URL of the moderated object.
        self.url = url

    def validate(self):
        if self.page_result:
            for k in self.page_result:
                if k:
                    k.validate()
        if self.page_summary:
            self.page_summary.validate()

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
        if self.page_summary is not None:
            result['PageSummary'] = self.page_summary.to_map()
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('PageSummary') is not None:
            temp_model = DescribeFileModerationResultResponseBodyDataPageSummary()
            self.page_summary = temp_model.from_map(m['PageSummary'])
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
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
        # The ReqId field returned by the asynchronous Image Moderation 2.0 API.
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
        description: str = None,
        label: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The description of the result.
        self.description = description
        # The labels returned after the image moderation.
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
        # The value of dataId that is specified in the API request. If this parameter is not specified in the API request, this field is not available in the response.
        self.data_id = data_id
        # The information about the captured frames.
        self.frame = frame
        # The number of frames.
        self.frame_num = frame_num
        # The reqId field returned by the Image Async Moderation API.
        self.req_id = req_id
        # The results of image moderation parameters such as the label parameter and the confidence parameter.
        self.result = result
        # Risk Level.
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
        # The returned HTTP status code.
        self.code = code
        # The image moderation results.
        self.data = data
        # The message that is returned in response to the request.
        self.msg = msg
        # The request ID, which is used to locate and troubleshoot issues.
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
        # The content of the information to be obtained. Multiple values are separated by commas.
        self.info_type = info_type
        # The reqId field returned by the Url Async Moderation API.
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
        # The image ID.
        self.image_id = image_id
        # The image library ID.
        self.lib_id = lib_id
        # The image library name.
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
        # Identified person coding information.
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
        # Custom words, multiple words separated by commas.
        self.key_words = key_words
        # Custom library ID.
        self.lib_id = lib_id
        # Custom library name.
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
        # When a custom text library is hit, the custom library ID, custom library name, and custom word are returned.
        self.custom_texts = custom_texts
        # Returns the text information in the recognized image.
        self.ocr_datas = ocr_datas
        # The risk words that are hit. Multiple words are separated by commas (,).
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
        # If a custom image library is hit, information about the hit custom image library is returned.
        self.custom_image = custom_image
        # Person information list.
        self.public_figure = public_figure
        # Returns the text information in the hit image.
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
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The AccessKey secret.
        self.access_key_secret = access_key_secret
        # The bucket name.
        self.bucket_name = bucket_name
        # The time when the file sharing link expires.
        self.expiration = expiration
        # The file prefix.
        self.file_name_prefix = file_name_prefix
        # the oss intranet point.
        self.oss_internal_end_point = oss_internal_end_point
        # the oss internet point.
        self.oss_internet_end_point = oss_internet_end_point
        # The security token.
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
        # The ReqId field returned by an asynchronous URL moderation operation.
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
        site_type: str = None,
    ):
        # The ICP number.
        self.icp_no = icp_no
        # The type of the ICP filing.
        self.icp_type = icp_type
        # The type of site
        self.site_type = site_type

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
        if self.site_type is not None:
            result['SiteType'] = self.site_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IcpNo') is not None:
            self.icp_no = m.get('IcpNo')
        if m.get('IcpType') is not None:
            self.icp_type = m.get('IcpType')
        if m.get('SiteType') is not None:
            self.site_type = m.get('SiteType')
        return self


class DescribeUrlModerationResultResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        label: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The labels returned after the asynchronous URL moderation.
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
        # The value of dataId that is specified in the API request. If this parameter is not specified in the API request, this field is not available in the response.
        self.data_id = data_id
        # The supplementary information.
        self.extra_info = extra_info
        # The ReqId field returned by an asynchronous URL moderation operation.
        self.req_id = req_id
        # The returned results.
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
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The task ID.
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
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
        self.message = message
        # The request ID.
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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The ID of the moderated object.
        self.data_id = data_id
        # The reqId field returned by the Image Async Moderation API. You can use this field to query the detection results.
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


class ImageBatchModerationRequest(TeaModel):
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


class ImageBatchModerationResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.description = description
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


class ImageBatchModerationResponseBodyDataResultsExtCustomImage(TeaModel):
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


class ImageBatchModerationResponseBodyDataResultsExtLogoDataLocation(TeaModel):
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


class ImageBatchModerationResponseBodyDataResultsExtLogoDataLogo(TeaModel):
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


class ImageBatchModerationResponseBodyDataResultsExtLogoData(TeaModel):
    def __init__(
        self,
        location: ImageBatchModerationResponseBodyDataResultsExtLogoDataLocation = None,
        logo: List[ImageBatchModerationResponseBodyDataResultsExtLogoDataLogo] = None,
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
            temp_model = ImageBatchModerationResponseBodyDataResultsExtLogoDataLocation()
            self.location = temp_model.from_map(m['Location'])
        self.logo = []
        if m.get('Logo') is not None:
            for k in m.get('Logo'):
                temp_model = ImageBatchModerationResponseBodyDataResultsExtLogoDataLogo()
                self.logo.append(temp_model.from_map(k))
        return self


class ImageBatchModerationResponseBodyDataResultsExtPublicFigureLocation(TeaModel):
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


class ImageBatchModerationResponseBodyDataResultsExtPublicFigure(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
        figure_name: str = None,
        location: List[ImageBatchModerationResponseBodyDataResultsExtPublicFigureLocation] = None,
    ):
        self.figure_id = figure_id
        self.figure_name = figure_name
        self.location = location

    def validate(self):
        if self.location:
            for k in self.location:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_name is not None:
            result['FigureName'] = self.figure_name
        result['Location'] = []
        if self.location is not None:
            for k in self.location:
                result['Location'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureName') is not None:
            self.figure_name = m.get('FigureName')
        self.location = []
        if m.get('Location') is not None:
            for k in m.get('Location'):
                temp_model = ImageBatchModerationResponseBodyDataResultsExtPublicFigureLocation()
                self.location.append(temp_model.from_map(k))
        return self


class ImageBatchModerationResponseBodyDataResultsExtTextInImageCustomText(TeaModel):
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


class ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResultLocation(TeaModel):
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


class ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResult(TeaModel):
    def __init__(
        self,
        location: ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResultLocation = None,
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
            temp_model = ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResultLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ImageBatchModerationResponseBodyDataResultsExtTextInImage(TeaModel):
    def __init__(
        self,
        custom_text: List[ImageBatchModerationResponseBodyDataResultsExtTextInImageCustomText] = None,
        ocr_result: List[ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResult] = None,
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
                temp_model = ImageBatchModerationResponseBodyDataResultsExtTextInImageCustomText()
                self.custom_text.append(temp_model.from_map(k))
        self.ocr_result = []
        if m.get('OcrResult') is not None:
            for k in m.get('OcrResult'):
                temp_model = ImageBatchModerationResponseBodyDataResultsExtTextInImageOcrResult()
                self.ocr_result.append(temp_model.from_map(k))
        if m.get('RiskWord') is not None:
            self.risk_word = m.get('RiskWord')
        return self


class ImageBatchModerationResponseBodyDataResultsExt(TeaModel):
    def __init__(
        self,
        custom_image: List[ImageBatchModerationResponseBodyDataResultsExtCustomImage] = None,
        logo_data: ImageBatchModerationResponseBodyDataResultsExtLogoData = None,
        public_figure: List[ImageBatchModerationResponseBodyDataResultsExtPublicFigure] = None,
        text_in_image: ImageBatchModerationResponseBodyDataResultsExtTextInImage = None,
    ):
        self.custom_image = custom_image
        self.logo_data = logo_data
        self.public_figure = public_figure
        self.text_in_image = text_in_image

    def validate(self):
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.logo_data:
            self.logo_data.validate()
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
        if self.logo_data is not None:
            result['LogoData'] = self.logo_data.to_map()
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
                temp_model = ImageBatchModerationResponseBodyDataResultsExtCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        if m.get('LogoData') is not None:
            temp_model = ImageBatchModerationResponseBodyDataResultsExtLogoData()
            self.logo_data = temp_model.from_map(m['LogoData'])
        self.public_figure = []
        if m.get('PublicFigure') is not None:
            for k in m.get('PublicFigure'):
                temp_model = ImageBatchModerationResponseBodyDataResultsExtPublicFigure()
                self.public_figure.append(temp_model.from_map(k))
        if m.get('TextInImage') is not None:
            temp_model = ImageBatchModerationResponseBodyDataResultsExtTextInImage()
            self.text_in_image = temp_model.from_map(m['TextInImage'])
        return self


class ImageBatchModerationResponseBodyDataResultsResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        self.confidence = confidence
        self.description = description
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


class ImageBatchModerationResponseBodyDataResults(TeaModel):
    def __init__(
        self,
        ext: ImageBatchModerationResponseBodyDataResultsExt = None,
        result: List[ImageBatchModerationResponseBodyDataResultsResult] = None,
        risk_level: str = None,
        service: str = None,
    ):
        self.ext = ext
        self.result = result
        self.risk_level = risk_level
        self.service = service

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
        if self.ext is not None:
            result['Ext'] = self.ext.to_map()
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.service is not None:
            result['Service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            temp_model = ImageBatchModerationResponseBodyDataResultsExt()
            self.ext = temp_model.from_map(m['Ext'])
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ImageBatchModerationResponseBodyDataResultsResult()
                self.result.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        return self


class ImageBatchModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        result: List[ImageBatchModerationResponseBodyDataResult] = None,
        results: List[ImageBatchModerationResponseBodyDataResults] = None,
        risk_level: str = None,
    ):
        self.data_id = data_id
        self.result = result
        self.results = results
        self.risk_level = risk_level

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ImageBatchModerationResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ImageBatchModerationResponseBodyDataResults()
                self.results.append(temp_model.from_map(k))
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class ImageBatchModerationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ImageBatchModerationResponseBodyData = None,
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
            temp_model = ImageBatchModerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImageBatchModerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImageBatchModerationResponseBody = None,
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
            temp_model = ImageBatchModerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImageModerationRequest(TeaModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        # The moderation services supported by Image Moderation 2.0. Valid values:
        # 
        # *   baselineCheck: common baseline moderation
        # *   baselineCheck_pro: common baseline moderation_Professional
        # *   baselineCheck_cb: common baseline moderation_For regions outside the Chinese mainland
        # *   tonalityImprove: content governance moderation
        # *   aigcCheck: AI-generated image identification
        # *   profilePhotoCheck: avatar image moderation
        # *   advertisingCheck: marketing material identification
        # *   liveStreamCheck: moderation of screenshots of videos and live streams
        # 
        # Valid values:
        # 
        # *   liveStreamCheck: moderation of screenshots of videos and live streams
        # *   baselineCheck: common baseline moderation
        # *   aigcCheck: AI-generated image identification
        # *   baselineCheck_pro: common baseline moderation_Professional
        # *   advertisingCheck: marketing material identification
        # *   baselineCheck_cb: common baseline moderation_For regions outside the Chinese mainland
        # *   tonalityImprove: content governance moderation
        # *   profilePhotoCheck: avatar image moderation
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
        # 
        # *   imageUrl: the URL of the object that you want to moderate. This parameter is required.
        # *   dataId: the ID of the object that you want to moderate. This parameter is optional.
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
        # The image ID.
        self.image_id = image_id
        # The image library ID.
        self.lib_id = lib_id
        # The image library name.
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


class ImageModerationResponseBodyDataExtFaceDataBang(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtFaceDataGender(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtFaceDataHairstyle(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtFaceDataHat(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtFaceDataLocation(TeaModel):
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


class ImageModerationResponseBodyDataExtFaceDataMask(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtFaceDataMustache(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtFaceDataQuality(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ImageModerationResponseBodyDataExtFaceData(TeaModel):
    def __init__(
        self,
        age: int = None,
        bang: ImageModerationResponseBodyDataExtFaceDataBang = None,
        gender: ImageModerationResponseBodyDataExtFaceDataGender = None,
        glasses: str = None,
        hairstyle: ImageModerationResponseBodyDataExtFaceDataHairstyle = None,
        hat: ImageModerationResponseBodyDataExtFaceDataHat = None,
        location: ImageModerationResponseBodyDataExtFaceDataLocation = None,
        mask: ImageModerationResponseBodyDataExtFaceDataMask = None,
        mustache: ImageModerationResponseBodyDataExtFaceDataMustache = None,
        quality: ImageModerationResponseBodyDataExtFaceDataQuality = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ImageModerationResponseBodyDataExtFaceDataBang()
            self.bang = temp_model.from_map(m['Bang'])
        if m.get('Gender') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataGender()
            self.gender = temp_model.from_map(m['Gender'])
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Hairstyle') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataHairstyle()
            self.hairstyle = temp_model.from_map(m['Hairstyle'])
        if m.get('Hat') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataHat()
            self.hat = temp_model.from_map(m['Hat'])
        if m.get('Location') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Mask') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataMask()
            self.mask = temp_model.from_map(m['Mask'])
        if m.get('Mustache') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataMustache()
            self.mustache = temp_model.from_map(m['Mustache'])
        if m.get('Quality') is not None:
            temp_model = ImageModerationResponseBodyDataExtFaceDataQuality()
            self.quality = temp_model.from_map(m['Quality'])
        if m.get('Smile') is not None:
            self.smile = m.get('Smile')
        return self


class ImageModerationResponseBodyDataExtLogoDataLocation(TeaModel):
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
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places. Some labels do not have scores of confidence levels.
        self.confidence = confidence
        # Logo category.
        self.label = label
        # Logo name.
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
        # Location information.
        self.location = location
        # Logo information.
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
        # Location information.
        self.location = location
        # The text information in the recognized image.
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


class ImageModerationResponseBodyDataExtPublicFigureLocation(TeaModel):
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


class ImageModerationResponseBodyDataExtPublicFigure(TeaModel):
    def __init__(
        self,
        figure_id: str = None,
        figure_name: str = None,
        location: List[ImageModerationResponseBodyDataExtPublicFigureLocation] = None,
    ):
        # Identified person coding information.
        self.figure_id = figure_id
        # Identified person name information.
        self.figure_name = figure_name
        # the data array of location info
        self.location = location

    def validate(self):
        if self.location:
            for k in self.location:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.figure_id is not None:
            result['FigureId'] = self.figure_id
        if self.figure_name is not None:
            result['FigureName'] = self.figure_name
        result['Location'] = []
        if self.location is not None:
            for k in self.location:
                result['Location'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FigureId') is not None:
            self.figure_id = m.get('FigureId')
        if m.get('FigureName') is not None:
            self.figure_name = m.get('FigureName')
        self.location = []
        if m.get('Location') is not None:
            for k in m.get('Location'):
                temp_model = ImageModerationResponseBodyDataExtPublicFigureLocation()
                self.location.append(temp_model.from_map(k))
        return self


class ImageModerationResponseBodyDataExtRecognition(TeaModel):
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
        # Custom words, multiple words separated by commas.
        self.key_words = key_words
        # Custom library ID.
        self.lib_id = lib_id
        # Custom library name.
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
        # Location information.
        self.location = location
        # The text information in the recognized image.
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
        # When a custom text library is hit, the custom library ID, custom library name, and custom word are returned.
        self.custom_text = custom_text
        # Returns the text information in the recognized image.
        self.ocr_result = ocr_result
        # The risk words that are hit. Multiple words are separated by commas (,).
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


class ImageModerationResponseBodyDataExtVlContent(TeaModel):
    def __init__(
        self,
        output_text: str = None,
    ):
        # the vl output content
        self.output_text = output_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output_text is not None:
            result['OutputText'] = self.output_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputText') is not None:
            self.output_text = m.get('OutputText')
        return self


class ImageModerationResponseBodyDataExt(TeaModel):
    def __init__(
        self,
        custom_image: List[ImageModerationResponseBodyDataExtCustomImage] = None,
        face_data: List[ImageModerationResponseBodyDataExtFaceData] = None,
        logo_data: List[ImageModerationResponseBodyDataExtLogoData] = None,
        ocr_result: List[ImageModerationResponseBodyDataExtOcrResult] = None,
        public_figure: List[ImageModerationResponseBodyDataExtPublicFigure] = None,
        recognition: List[ImageModerationResponseBodyDataExtRecognition] = None,
        text_in_image: ImageModerationResponseBodyDataExtTextInImage = None,
        vl_content: ImageModerationResponseBodyDataExtVlContent = None,
    ):
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
        if self.custom_image:
            for k in self.custom_image:
                if k:
                    k.validate()
        if self.face_data:
            for k in self.face_data:
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
        if self.vl_content:
            self.vl_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CustomImage'] = []
        if self.custom_image is not None:
            for k in self.custom_image:
                result['CustomImage'].append(k.to_map() if k else None)
        result['FaceData'] = []
        if self.face_data is not None:
            for k in self.face_data:
                result['FaceData'].append(k.to_map() if k else None)
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
        if self.vl_content is not None:
            result['VlContent'] = self.vl_content.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_image = []
        if m.get('CustomImage') is not None:
            for k in m.get('CustomImage'):
                temp_model = ImageModerationResponseBodyDataExtCustomImage()
                self.custom_image.append(temp_model.from_map(k))
        self.face_data = []
        if m.get('FaceData') is not None:
            for k in m.get('FaceData'):
                temp_model = ImageModerationResponseBodyDataExtFaceData()
                self.face_data.append(temp_model.from_map(k))
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
        if m.get('VlContent') is not None:
            temp_model = ImageModerationResponseBodyDataExtVlContent()
            self.vl_content = temp_model.from_map(m['VlContent'])
        return self


class ImageModerationResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        confidence: float = None,
        description: str = None,
        label: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places. Some labels do not have scores of confidence levels.
        self.confidence = confidence
        # The description of the result.
        self.description = description
        # The labels returned after the image moderation. Multiple risk labels and the corresponding scores of confidence levels may be returned for an image.
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


class ImageModerationResponseBodyData(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        ext: ImageModerationResponseBodyDataExt = None,
        result: List[ImageModerationResponseBodyDataResult] = None,
        risk_level: str = None,
    ):
        # The ID of the moderated object.
        # 
        # >  If you specify the dataId parameter in the request, the value of the dataId parameter is returned in the response.
        self.data_id = data_id
        # Auxiliary reference information.
        self.ext = ext
        # The results of image moderation parameters such as the label parameter and the confidence parameter, which are an array structure.
        self.result = result
        # Risk Level.
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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The device ID.
        self.device_id = device_id
        # Labels.
        self.labels = labels
        # The JSON string used to locate the cause.
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
        # The returned HTTP status code.
        self.code = code
        # The moderation results.
        self.data = data
        # The message that is returned in response to the request.
        self.message = message
        # The request ID.
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
        # The moderation service.
        # 
        # Valid values:
        # 
        # *   chat_detection_pro: moderation of interactive content of private chats_Professional
        # *   llm_response_moderation: moderation of text generated by LLMs
        # *   llm_query_moderation: moderation of input text of LLMs
        # *   nickname_detection_pro: moderation of user nicknames_Professional
        # *   comment_detection_pro: moderation of comment content of public chats_Professional
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The answer.
        self.answer = answer
        # Hit Label
        self.hit_label = hit_label
        # Hit Library Name
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
        # The terms that are hit. Multiple terms are separated by commas (,).
        self.key_words = key_words
        # The library name.
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
        description: str = None,
        label: str = None,
        risk_words: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The custom term hit by the moderated content.
        self.customized_hit = customized_hit
        # The description of the label.
        self.description = description
        # The label.
        self.label = label
        # The term hit by the moderated content.
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
        if self.description is not None:
            result['Description'] = self.description
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
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
        # The suggestion.
        self.advice = advice
        # The results.
        self.result = result
        # Risk Level
        self.risk_level = risk_level
        # The score.
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
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The moderation results.
        self.data = data
        # The message that is returned in response to the request.
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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The ID of the moderated object.
        self.data_id = data_id
        # The reqId field returned by the Url Async Moderation API.
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
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The ID of the moderated object.
        self.data_id = data_id
        # The task ID.
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
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
        self.message = message
        # The request ID.
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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The returned HTTP status code.
        self.code = code
        # The message that is returned in response to the request.
        self.message = message
        # The request ID.
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
        # The type of the moderation service.
        # 
        # Valid values:
        # 
        # *   liveStreamDetection: live stream moderation
        # *   videoDetection: video file moderation
        # *   liveStreamDetection_cb: live stream moderation_For regions outside the Chinese mainland
        # *   videoDetection_cb: video file moderation_For regions outside the Chinese mainland.
        self.service = service
        # The parameters required by the moderation service. The ID of the task that you want to query. You can specify one task ID at a time.
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
        # The voice label.
        self.label = label
        # The number of times that the label is matched.
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
        risk_level: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        score: float = None,
        start_time: int = None,
        start_timestamp: int = None,
        text: str = None,
        url: str = None,
    ):
        # The end time of the text after voice-to-text conversion. Unit: seconds.
        self.end_time = end_time
        # The end timestamp of the segment. Unit: milliseconds.
        self.end_timestamp = end_timestamp
        # A reserved parameter.
        self.extend = extend
        # The details of the labels.
        self.labels = labels
        # Risk Level.
        self.risk_level = risk_level
        # Subcategory labels. Multiple labels are separated by commas (,).
        self.risk_tips = risk_tips
        # The risk words that are hit. Multiple words are separated by commas (,).
        self.risk_words = risk_words
        # The risk score. Default range: 0 to 99.
        self.score = score
        # The start time of the text after voice-to-text conversion. Unit: seconds.
        self.start_time = start_time
        # The start timestamp of the segment. Unit: milliseconds.
        self.start_timestamp = start_timestamp
        # The text converted from voice.
        self.text = text
        # If the moderation object is a voice stream, this parameter indicates the temporary access URL of the voice stream to which the text entry corresponds. The validity period of the URL is 30 minutes. You must prepare another URL to store the voice stream at the earliest opportunity.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
        risk_level: str = None,
        slice_details: List[VideoModerationResultResponseBodyDataAudioResultSliceDetails] = None,
    ):
        # Summary of voice labels.
        self.audio_summarys = audio_summarys
        # Risk Level.
        self.risk_level = risk_level
        # The details about the text in the moderated voice. The value is a JSON array that contains one or more elements. Each element corresponds to a text entry.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        self.slice_details = []
        if m.get('SliceDetails') is not None:
            for k in m.get('SliceDetails'):
                temp_model = VideoModerationResultResponseBodyDataAudioResultSliceDetails()
                self.slice_details.append(temp_model.from_map(k))
        return self


class VideoModerationResultResponseBodyDataFrameResultFrameSummarys(TeaModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        label_sum: int = None,
    ):
        # The description of the result.
        self.description = description
        # The label against which a captured frame is matched.
        self.label = label
        # The number of times that the label is matched.
        self.label_sum = label_sum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.label is not None:
            result['Label'] = self.label
        if self.label_sum is not None:
            result['LabelSum'] = self.label_sum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
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
        # The ID of the custom image that is hit.
        self.image_id = image_id
        # The ID of the custom image library that is hit.
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
        # The information about the code of the identified figure.
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
        description: str = None,
        label: str = None,
    ):
        # The score of the confidence level. Valid values: 0 to 100. The value is accurate to two decimal places.
        self.confidence = confidence
        # The description of the result.
        self.description = description
        # The label returned after a frame is moderated. Multiple risk labels and the corresponding scores of confidence levels may be returned for a frame.
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


class VideoModerationResultResponseBodyDataFrameResultFramesResults(TeaModel):
    def __init__(
        self,
        custom_image: List[VideoModerationResultResponseBodyDataFrameResultFramesResultsCustomImage] = None,
        public_figure: List[VideoModerationResultResponseBodyDataFrameResultFramesResultsPublicFigure] = None,
        result: List[VideoModerationResultResponseBodyDataFrameResultFramesResultsResult] = None,
        service: str = None,
        text_in_image: Dict[str, Any] = None,
    ):
        # If a custom image library is hit, information about the custom image library is returned.
        self.custom_image = custom_image
        # If the video contains a specific figure, the code of the identified figure is returned.
        self.public_figure = public_figure
        # The results of frame moderation parameters such as the label parameter and the confidence parameter.
        self.result = result
        # The moderation service that is called.
        self.service = service
        # The information about the text hit in the image is returned.
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
        risk_level: str = None,
        temp_url: str = None,
        timestamp: int = None,
    ):
        # The interval between the start of the video file and the captured frame. Unit: seconds.
        self.offset = offset
        # The results of frame moderation parameters such as the label parameter and the confidence parameter.
        self.results = results
        # Risk Level.
        self.risk_level = risk_level
        # The temporary URL of a captured frame.
        self.temp_url = temp_url
        # The absolute timestamp. Unit: milliseconds.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
        risk_level: str = None,
    ):
        # The number of captured frames that are returned for the video file.
        self.frame_num = frame_num
        # The summary of the labels against which captured frames are matched.
        self.frame_summarys = frame_summarys
        # The information about the frames that match the labels.
        self.frames = frames
        # Risk Level.
        self.risk_level = risk_level

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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        return self


class VideoModerationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        audio_result: VideoModerationResultResponseBodyDataAudioResult = None,
        data_id: str = None,
        frame_result: VideoModerationResultResponseBodyDataFrameResult = None,
        live_id: str = None,
        risk_level: str = None,
        task_id: str = None,
    ):
        # The voice moderation results. The moderation results contain a structure.
        self.audio_result = audio_result
        # The value of dataId that is specified in the API request. If this parameter is not specified in the API request, the dataId field is not available in the response.
        self.data_id = data_id
        # The image moderation results. If the call is successful, the HTTP status code 200 and moderation results are returned. The moderation results contain a structure.
        self.frame_result = frame_result
        # The unique ID of the live stream.
        self.live_id = live_id
        # Risk Level.
        self.risk_level = risk_level
        # The task ID.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
        # The returned HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The moderation results.
        self.data = data
        # The message that is returned in response to the request.
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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The ID of the moderated object.
        self.data_id = data_id
        # The task ID.
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
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
        self.message = message
        # The request ID.
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
        # The type of the moderation service.
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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
        # The returned HTTP status code.
        self.code = code
        # The message that is returned in response to the request.
        self.message = message
        # The request ID.
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
        # The type of the moderation service. Valid values: nickname_detection: user nickname
        self.service = service
        # The parameters of API requests that are sent from API Gateway to the backend service.
        # 
        # For more information, see [ServiceParameter](https://help.aliyun.com/document_detail/43988.html).
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
        risk_level: str = None,
        risk_tips: str = None,
        risk_words: str = None,
        score: float = None,
        start_time: int = None,
        start_timestamp: int = None,
        text: str = None,
        url: str = None,
    ):
        # The end time of the audio segment in seconds.
        self.end_time = end_time
        # The end timestamp of the segment. Unit: milliseconds.
        self.end_timestamp = end_timestamp
        # Extended fields.
        self.extend = extend
        # The details of the labels.
        self.labels = labels
        # Reserved parameter.
        self.origin_algo_result = origin_algo_result
        # Risk Level.
        self.risk_level = risk_level
        # The details of the risky content.
        self.risk_tips = risk_tips
        # The term hit by the risky content.
        self.risk_words = risk_words
        # The risk score. Default range: 0 to 99.
        self.score = score
        # The start time of the audio segment in seconds.
        self.start_time = start_time
        # The start timestamp of the segment. Unit: milliseconds.
        self.start_timestamp = start_timestamp
        # The text converted from the audio segment.
        self.text = text
        # The temporary URL of the audio segment.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
        risk_level: str = None,
        slice_details: List[VoiceModerationResultResponseBodyDataSliceDetails] = None,
        task_id: str = None,
        url: str = None,
    ):
        # The ID of the moderated object.
        self.data_id = data_id
        # The unique ID of the live stream.
        self.live_id = live_id
        # Risk Level.
        self.risk_level = risk_level
        # The moderation results of audio segments.
        self.slice_details = slice_details
        # The task ID.
        self.task_id = task_id
        # The URL of the moderated content.
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
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
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
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
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
        # The returned HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message that is returned in response to the request.
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


