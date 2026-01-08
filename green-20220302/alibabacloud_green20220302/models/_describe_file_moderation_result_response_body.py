# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class DescribeFileModerationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeFileModerationResultResponseBodyData = None,
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeFileModerationResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFileModerationResultResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        data_id: str = None,
        doc_type: str = None,
        page_result: List[main_models.DescribeFileModerationResultResponseBodyDataPageResult] = None,
        page_summary: main_models.DescribeFileModerationResultResponseBodyDataPageSummary = None,
        risk_level: str = None,
        url: str = None,
    ):
        self.account_id = account_id
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
            for v1 in self.page_result:
                 if v1:
                    v1.validate()
        if self.page_summary:
            self.page_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.doc_type is not None:
            result['DocType'] = self.doc_type

        result['PageResult'] = []
        if self.page_result is not None:
            for k1 in self.page_result:
                result['PageResult'].append(k1.to_map() if k1 else None)

        if self.page_summary is not None:
            result['PageSummary'] = self.page_summary.to_map()

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')

        self.page_result = []
        if m.get('PageResult') is not None:
            for k1 in m.get('PageResult'):
                temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageResult()
                self.page_result.append(temp_model.from_map(k1))

        if m.get('PageSummary') is not None:
            temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageSummary()
            self.page_summary = temp_model.from_map(m.get('PageSummary'))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeFileModerationResultResponseBodyDataPageSummary(DaraModel):
    def __init__(
        self,
        image_summary: main_models.DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary = None,
        page_sum: int = None,
        text_summary: main_models.DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary = None,
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary()
            self.image_summary = temp_model.from_map(m.get('ImageSummary'))

        if m.get('PageSum') is not None:
            self.page_sum = m.get('PageSum')

        if m.get('TextSummary') is not None:
            temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary()
            self.text_summary = temp_model.from_map(m.get('TextSummary'))

        return self

class DescribeFileModerationResultResponseBodyDataPageSummaryTextSummary(DaraModel):
    def __init__(
        self,
        risk_level: str = None,
        text_labels: List[main_models.DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels] = None,
    ):
        # Risk Level
        self.risk_level = risk_level
        # Text Label
        self.text_labels = text_labels

    def validate(self):
        if self.text_labels:
            for v1 in self.text_labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        result['TextLabels'] = []
        if self.text_labels is not None:
            for k1 in self.text_labels:
                result['TextLabels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        self.text_labels = []
        if m.get('TextLabels') is not None:
            for k1 in m.get('TextLabels'):
                temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels()
                self.text_labels.append(temp_model.from_map(k1))

        return self

class DescribeFileModerationResultResponseBodyDataPageSummaryTextSummaryTextLabels(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
        label_sum: int = None,
    ):
        # The description of the labels.
        self.description = description
        # The details of the labels.
        self.label = label
        # The number of times that the label is matched.
        self.label_sum = label_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeFileModerationResultResponseBodyDataPageSummaryImageSummary(DaraModel):
    def __init__(
        self,
        image_labels: List[main_models.DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels] = None,
        risk_level: str = None,
    ):
        # Image Label
        self.image_labels = image_labels
        # Risk Level
        self.risk_level = risk_level

    def validate(self):
        if self.image_labels:
            for v1 in self.image_labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageLabels'] = []
        if self.image_labels is not None:
            for k1 in self.image_labels:
                result['ImageLabels'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_labels = []
        if m.get('ImageLabels') is not None:
            for k1 in m.get('ImageLabels'):
                temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels()
                self.image_labels.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class DescribeFileModerationResultResponseBodyDataPageSummaryImageSummaryImageLabels(DaraModel):
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeFileModerationResultResponseBodyDataPageResult(DaraModel):
    def __init__(
        self,
        image_result: List[main_models.DescribeFileModerationResultResponseBodyDataPageResultImageResult] = None,
        image_url: str = None,
        page_num: int = None,
        text_result: List[main_models.DescribeFileModerationResultResponseBodyDataPageResultTextResult] = None,
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
            for v1 in self.image_result:
                 if v1:
                    v1.validate()
        if self.text_result:
            for v1 in self.text_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageResult'] = []
        if self.image_result is not None:
            for k1 in self.image_result:
                result['ImageResult'].append(k1.to_map() if k1 else None)

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        result['TextResult'] = []
        if self.text_result is not None:
            for k1 in self.text_result:
                result['TextResult'].append(k1.to_map() if k1 else None)

        if self.text_url is not None:
            result['TextUrl'] = self.text_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_result = []
        if m.get('ImageResult') is not None:
            for k1 in m.get('ImageResult'):
                temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageResultImageResult()
                self.image_result.append(temp_model.from_map(k1))

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        self.text_result = []
        if m.get('TextResult') is not None:
            for k1 in m.get('TextResult'):
                temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageResultTextResult()
                self.text_result.append(temp_model.from_map(k1))

        if m.get('TextUrl') is not None:
            self.text_url = m.get('TextUrl')

        return self

class DescribeFileModerationResultResponseBodyDataPageResultTextResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        descriptions: str = None,
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
        # The description of the labels.
        self.descriptions = descriptions
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.descriptions is not None:
            result['Descriptions'] = self.descriptions

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

        if m.get('Descriptions') is not None:
            self.descriptions = m.get('Descriptions')

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

class DescribeFileModerationResultResponseBodyDataPageResultImageResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        label_result: List[main_models.DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult] = None,
        location: main_models.DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation = None,
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
            for v1 in self.label_result:
                 if v1:
                    v1.validate()
        if self.location:
            self.location.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['LabelResult'] = []
        if self.label_result is not None:
            for k1 in self.label_result:
                result['LabelResult'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('LabelResult'):
                temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult()
                self.label_result.append(temp_model.from_map(k1))

        if m.get('Location') is not None:
            temp_model = main_models.DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

class DescribeFileModerationResultResponseBodyDataPageResultImageResultLocation(DaraModel):
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



class DescribeFileModerationResultResponseBodyDataPageResultImageResultLabelResult(DaraModel):
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

