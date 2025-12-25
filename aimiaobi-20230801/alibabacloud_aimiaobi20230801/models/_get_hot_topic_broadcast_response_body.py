# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetHotTopicBroadcastResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHotTopicBroadcastResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetHotTopicBroadcastResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHotTopicBroadcastResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetHotTopicBroadcastResponseBodyDataData] = None,
        total_count: int = None,
        total_token_info: main_models.GetHotTopicBroadcastResponseBodyDataTotalTokenInfo = None,
    ):
        self.data = data
        self.total_count = total_count
        self.total_token_info = total_token_info

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.total_token_info:
            self.total_token_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_token_info is not None:
            result['TotalTokenInfo'] = self.total_token_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetHotTopicBroadcastResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalTokenInfo') is not None:
            temp_model = main_models.GetHotTopicBroadcastResponseBodyDataTotalTokenInfo()
            self.total_token_info = temp_model.from_map(m.get('TotalTokenInfo'))

        return self

class GetHotTopicBroadcastResponseBodyDataTotalTokenInfo(DaraModel):
    def __init__(
        self,
        hot_topic_count: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        word_count: int = None,
    ):
        self.hot_topic_count = hot_topic_count
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.word_count = word_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hot_topic_count is not None:
            result['HotTopicCount'] = self.hot_topic_count

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.word_count is not None:
            result['WordCount'] = self.word_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotTopicCount') is not None:
            self.hot_topic_count = m.get('HotTopicCount')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')

        return self

class GetHotTopicBroadcastResponseBodyDataData(DaraModel):
    def __init__(
        self,
        category: str = None,
        create_time: str = None,
        custom_hot_value: float = None,
        custom_text_summary: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        hot_value: float = None,
        id: str = None,
        images: List[main_models.GetHotTopicBroadcastResponseBodyDataDataImages] = None,
        input_token: int = None,
        locations: List[str] = None,
        news: List[main_models.GetHotTopicBroadcastResponseBodyDataDataNews] = None,
        output_token: int = None,
        pub_time: str = None,
        summary: main_models.GetHotTopicBroadcastResponseBodyDataDataSummary = None,
        text_summary: str = None,
        url: str = None,
    ):
        self.category = category
        self.create_time = create_time
        self.custom_hot_value = custom_hot_value
        self.custom_text_summary = custom_text_summary
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.hot_value = hot_value
        self.id = id
        self.images = images
        self.input_token = input_token
        self.locations = locations
        self.news = news
        self.output_token = output_token
        self.pub_time = pub_time
        self.summary = summary
        self.text_summary = text_summary
        self.url = url

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.news:
            for v1 in self.news:
                 if v1:
                    v1.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_hot_value is not None:
            result['CustomHotValue'] = self.custom_hot_value

        if self.custom_text_summary is not None:
            result['CustomTextSummary'] = self.custom_text_summary

        if self.hot_topic is not None:
            result['HotTopic'] = self.hot_topic

        if self.hot_topic_version is not None:
            result['HotTopicVersion'] = self.hot_topic_version

        if self.hot_value is not None:
            result['HotValue'] = self.hot_value

        if self.id is not None:
            result['Id'] = self.id

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.input_token is not None:
            result['InputToken'] = self.input_token

        if self.locations is not None:
            result['Locations'] = self.locations

        result['News'] = []
        if self.news is not None:
            for k1 in self.news:
                result['News'].append(k1.to_map() if k1 else None)

        if self.output_token is not None:
            result['OutputToken'] = self.output_token

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        if self.text_summary is not None:
            result['TextSummary'] = self.text_summary

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomHotValue') is not None:
            self.custom_hot_value = m.get('CustomHotValue')

        if m.get('CustomTextSummary') is not None:
            self.custom_text_summary = m.get('CustomTextSummary')

        if m.get('HotTopic') is not None:
            self.hot_topic = m.get('HotTopic')

        if m.get('HotTopicVersion') is not None:
            self.hot_topic_version = m.get('HotTopicVersion')

        if m.get('HotValue') is not None:
            self.hot_value = m.get('HotValue')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.GetHotTopicBroadcastResponseBodyDataDataImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('InputToken') is not None:
            self.input_token = m.get('InputToken')

        if m.get('Locations') is not None:
            self.locations = m.get('Locations')

        self.news = []
        if m.get('News') is not None:
            for k1 in m.get('News'):
                temp_model = main_models.GetHotTopicBroadcastResponseBodyDataDataNews()
                self.news.append(temp_model.from_map(k1))

        if m.get('OutputToken') is not None:
            self.output_token = m.get('OutputToken')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Summary') is not None:
            temp_model = main_models.GetHotTopicBroadcastResponseBodyDataDataSummary()
            self.summary = temp_model.from_map(m.get('Summary'))

        if m.get('TextSummary') is not None:
            self.text_summary = m.get('TextSummary')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetHotTopicBroadcastResponseBodyDataDataSummary(DaraModel):
    def __init__(
        self,
        input_token: int = None,
        output_token: int = None,
        summaries: List[main_models.GetHotTopicBroadcastResponseBodyDataDataSummarySummaries] = None,
    ):
        self.input_token = input_token
        self.output_token = output_token
        self.summaries = summaries

    def validate(self):
        if self.summaries:
            for v1 in self.summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_token is not None:
            result['InputToken'] = self.input_token

        if self.output_token is not None:
            result['OutputToken'] = self.output_token

        result['Summaries'] = []
        if self.summaries is not None:
            for k1 in self.summaries:
                result['Summaries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputToken') is not None:
            self.input_token = m.get('InputToken')

        if m.get('OutputToken') is not None:
            self.output_token = m.get('OutputToken')

        self.summaries = []
        if m.get('Summaries') is not None:
            for k1 in m.get('Summaries'):
                temp_model = main_models.GetHotTopicBroadcastResponseBodyDataDataSummarySummaries()
                self.summaries.append(temp_model.from_map(k1))

        return self

class GetHotTopicBroadcastResponseBodyDataDataSummarySummaries(DaraModel):
    def __init__(
        self,
        summary: str = None,
        title: str = None,
    ):
        self.summary = summary
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetHotTopicBroadcastResponseBodyDataDataNews(DaraModel):
    def __init__(
        self,
        analysis_category: str = None,
        analysis_topic: str = None,
        author: str = None,
        category: List[str] = None,
        comments: List[main_models.GetHotTopicBroadcastResponseBodyDataDataNewsComments] = None,
        content: str = None,
        create_time: str = None,
        domain: str = None,
        dt: str = None,
        hot_topic: str = None,
        img_list: List[str] = None,
        logo: str = None,
        pub_time: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
        uuid: str = None,
        website: str = None,
    ):
        self.analysis_category = analysis_category
        self.analysis_topic = analysis_topic
        self.author = author
        self.category = category
        self.comments = comments
        self.content = content
        self.create_time = create_time
        self.domain = domain
        self.dt = dt
        self.hot_topic = hot_topic
        self.img_list = img_list
        # logo
        self.logo = logo
        self.pub_time = pub_time
        self.summary = summary
        self.title = title
        self.url = url
        self.uuid = uuid
        self.website = website

    def validate(self):
        if self.comments:
            for v1 in self.comments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_category is not None:
            result['AnalysisCategory'] = self.analysis_category

        if self.analysis_topic is not None:
            result['AnalysisTopic'] = self.analysis_topic

        if self.author is not None:
            result['Author'] = self.author

        if self.category is not None:
            result['Category'] = self.category

        result['Comments'] = []
        if self.comments is not None:
            for k1 in self.comments:
                result['Comments'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.dt is not None:
            result['Dt'] = self.dt

        if self.hot_topic is not None:
            result['HotTopic'] = self.hot_topic

        if self.img_list is not None:
            result['ImgList'] = self.img_list

        if self.logo is not None:
            result['Logo'] = self.logo

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.website is not None:
            result['Website'] = self.website

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisCategory') is not None:
            self.analysis_category = m.get('AnalysisCategory')

        if m.get('AnalysisTopic') is not None:
            self.analysis_topic = m.get('AnalysisTopic')

        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        self.comments = []
        if m.get('Comments') is not None:
            for k1 in m.get('Comments'):
                temp_model = main_models.GetHotTopicBroadcastResponseBodyDataDataNewsComments()
                self.comments.append(temp_model.from_map(k1))

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Dt') is not None:
            self.dt = m.get('Dt')

        if m.get('HotTopic') is not None:
            self.hot_topic = m.get('HotTopic')

        if m.get('ImgList') is not None:
            self.img_list = m.get('ImgList')

        if m.get('Logo') is not None:
            self.logo = m.get('Logo')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Website') is not None:
            self.website = m.get('Website')

        return self

class GetHotTopicBroadcastResponseBodyDataDataNewsComments(DaraModel):
    def __init__(
        self,
        text: str = None,
        username: str = None,
    ):
        self.text = text
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetHotTopicBroadcastResponseBodyDataDataImages(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

