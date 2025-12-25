# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetTopicSelectionPerspectiveAnalysisTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyData = None,
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
            temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyData()
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

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        fresh_view_points_result: main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResult = None,
        hot_view_points_result: main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResult = None,
        status: str = None,
        timed_view_points_result: main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResult = None,
        topic: str = None,
        topic_summary_result: main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResult = None,
        web_review_points_result: main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResult = None,
    ):
        self.error_message = error_message
        self.fresh_view_points_result = fresh_view_points_result
        self.hot_view_points_result = hot_view_points_result
        self.status = status
        self.timed_view_points_result = timed_view_points_result
        self.topic = topic
        self.topic_summary_result = topic_summary_result
        self.web_review_points_result = web_review_points_result

    def validate(self):
        if self.fresh_view_points_result:
            self.fresh_view_points_result.validate()
        if self.hot_view_points_result:
            self.hot_view_points_result.validate()
        if self.timed_view_points_result:
            self.timed_view_points_result.validate()
        if self.topic_summary_result:
            self.topic_summary_result.validate()
        if self.web_review_points_result:
            self.web_review_points_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.fresh_view_points_result is not None:
            result['FreshViewPointsResult'] = self.fresh_view_points_result.to_map()

        if self.hot_view_points_result is not None:
            result['HotViewPointsResult'] = self.hot_view_points_result.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.timed_view_points_result is not None:
            result['TimedViewPointsResult'] = self.timed_view_points_result.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.topic_summary_result is not None:
            result['TopicSummaryResult'] = self.topic_summary_result.to_map()

        if self.web_review_points_result is not None:
            result['WebReviewPointsResult'] = self.web_review_points_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FreshViewPointsResult') is not None:
            temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResult()
            self.fresh_view_points_result = temp_model.from_map(m.get('FreshViewPointsResult'))

        if m.get('HotViewPointsResult') is not None:
            temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResult()
            self.hot_view_points_result = temp_model.from_map(m.get('HotViewPointsResult'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimedViewPointsResult') is not None:
            temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResult()
            self.timed_view_points_result = temp_model.from_map(m.get('TimedViewPointsResult'))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TopicSummaryResult') is not None:
            temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResult()
            self.topic_summary_result = temp_model.from_map(m.get('TopicSummaryResult'))

        if m.get('WebReviewPointsResult') is not None:
            temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResult()
            self.web_review_points_result = temp_model.from_map(m.get('WebReviewPointsResult'))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResult(DaraModel):
    def __init__(
        self,
        attitudes: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudes] = None,
    ):
        self.attitudes = attitudes

    def validate(self):
        if self.attitudes:
            for v1 in self.attitudes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k1 in self.attitudes:
                result['Attitudes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k1 in m.get('Attitudes'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudes(DaraModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        comments: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesComments] = None,
        ratio: str = None,
        view_points: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.comments = comments
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.comments:
            for v1 in self.comments:
                 if v1:
                    v1.validate()
        if self.view_points:
            for v1 in self.view_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type

        result['Comments'] = []
        if self.comments is not None:
            for k1 in self.comments:
                result['Comments'].append(k1.to_map() if k1 else None)

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        result['ViewPoints'] = []
        if self.view_points is not None:
            for k1 in self.view_points:
                result['ViewPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')

        self.comments = []
        if m.get('Comments') is not None:
            for k1 in m.get('Comments'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesComments()
                self.comments.append(temp_model.from_map(k1))

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k1 in m.get('ViewPoints'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPoints(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.point is not None:
            result['Point'] = self.point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPointsOutlines(DaraModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outline is not None:
            result['Outline'] = self.outline

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesComments(DaraModel):
    def __init__(
        self,
        source: str = None,
        text: str = None,
        title: str = None,
        url: str = None,
        username: str = None,
    ):
        self.source = source
        self.text = text
        self.title = title
        self.url = url
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['Source'] = self.source

        if self.text is not None:
            result['Text'] = self.text

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResult(DaraModel):
    def __init__(
        self,
        summaries: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummaries] = None,
    ):
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
        result['Summaries'] = []
        if self.summaries is not None:
            for k1 in self.summaries:
                result['Summaries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summaries = []
        if m.get('Summaries') is not None:
            for k1 in m.get('Summaries'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummaries()
                self.summaries.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummaries(DaraModel):
    def __init__(
        self,
        doc_list: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummariesDocList] = None,
        summary: str = None,
        title: str = None,
    ):
        self.doc_list = doc_list
        self.summary = summary
        self.title = title

    def validate(self):
        if self.doc_list:
            for v1 in self.doc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DocList'] = []
        if self.doc_list is not None:
            for k1 in self.doc_list:
                result['DocList'].append(k1.to_map() if k1 else None)

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_list = []
        if m.get('DocList') is not None:
            for k1 in m.get('DocList'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummariesDocList()
                self.doc_list.append(temp_model.from_map(k1))

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummariesDocList(DaraModel):
    def __init__(
        self,
        source: str = None,
        title: str = None,
        url: str = None,
    ):
        self.source = source
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResult(DaraModel):
    def __init__(
        self,
        attitudes: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudes] = None,
    ):
        self.attitudes = attitudes

    def validate(self):
        if self.attitudes:
            for v1 in self.attitudes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k1 in self.attitudes:
                result['Attitudes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k1 in m.get('Attitudes'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudes(DaraModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        pub_time: str = None,
        ratio: str = None,
        source: str = None,
        title: str = None,
        url: str = None,
        view_points: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.pub_time = pub_time
        self.ratio = ratio
        self.source = source
        self.title = title
        self.url = url
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for v1 in self.view_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.source is not None:
            result['Source'] = self.source

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        result['ViewPoints'] = []
        if self.view_points is not None:
            for k1 in self.view_points:
                result['ViewPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k1 in m.get('ViewPoints'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPoints(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.point is not None:
            result['Point'] = self.point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPointsOutlines(DaraModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outline is not None:
            result['Outline'] = self.outline

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResult(DaraModel):
    def __init__(
        self,
        attitudes: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudes] = None,
    ):
        self.attitudes = attitudes

    def validate(self):
        if self.attitudes:
            for v1 in self.attitudes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k1 in self.attitudes:
                result['Attitudes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k1 in m.get('Attitudes'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudes(DaraModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        news: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesNews] = None,
        ratio: str = None,
        view_points: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.news = news
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.news:
            for v1 in self.news:
                 if v1:
                    v1.validate()
        if self.view_points:
            for v1 in self.view_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type

        result['News'] = []
        if self.news is not None:
            for k1 in self.news:
                result['News'].append(k1.to_map() if k1 else None)

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        result['ViewPoints'] = []
        if self.view_points is not None:
            for k1 in self.view_points:
                result['ViewPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')

        self.news = []
        if m.get('News') is not None:
            for k1 in m.get('News'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesNews()
                self.news.append(temp_model.from_map(k1))

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k1 in m.get('ViewPoints'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPoints(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.point is not None:
            result['Point'] = self.point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPointsOutlines(DaraModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outline is not None:
            result['Outline'] = self.outline

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesNews(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        image_urls: List[str] = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tags: List[str] = None,
        title: str = None,
        topic: str = None,
        url: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.image_urls = image_urls
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tags = tags
        self.title = title
        self.topic = topic
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResult(DaraModel):
    def __init__(
        self,
        attitudes: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudes] = None,
    ):
        self.attitudes = attitudes

    def validate(self):
        if self.attitudes:
            for v1 in self.attitudes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k1 in self.attitudes:
                result['Attitudes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k1 in m.get('Attitudes'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudes(DaraModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        ratio: str = None,
        view_points: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for v1 in self.view_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        result['ViewPoints'] = []
        if self.view_points is not None:
            for k1 in self.view_points:
                result['ViewPoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k1 in m.get('ViewPoints'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k1))

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPoints(DaraModel):
    def __init__(
        self,
        outlines: List[main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for v1 in self.outlines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Outlines'] = []
        if self.outlines is not None:
            for k1 in self.outlines:
                result['Outlines'].append(k1.to_map() if k1 else None)

        if self.point is not None:
            result['Point'] = self.point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k1 in m.get('Outlines'):
                temp_model = main_models.GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k1))

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPointsOutlines(DaraModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.outline is not None:
            result['Outline'] = self.outline

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

