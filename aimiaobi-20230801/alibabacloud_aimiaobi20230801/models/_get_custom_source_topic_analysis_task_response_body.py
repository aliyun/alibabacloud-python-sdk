# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetCustomSourceTopicAnalysisTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCustomSourceTopicAnalysisTaskResponseBodyData = None,
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
            temp_model = main_models.GetCustomSourceTopicAnalysisTaskResponseBodyData()
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

class GetCustomSourceTopicAnalysisTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_count: int = None,
        cluster_results: List[main_models.GetCustomSourceTopicAnalysisTaskResponseBodyDataClusterResults] = None,
        error_message: str = None,
        max_clustered_topic_news_size: int = None,
        parsed_news_size: int = None,
        status: str = None,
        rt: int = None,
        usages: Dict[str, int] = None,
    ):
        self.cluster_count = cluster_count
        self.cluster_results = cluster_results
        self.error_message = error_message
        self.max_clustered_topic_news_size = max_clustered_topic_news_size
        self.parsed_news_size = parsed_news_size
        self.status = status
        self.rt = rt
        self.usages = usages

    def validate(self):
        if self.cluster_results:
            for v1 in self.cluster_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count

        result['ClusterResults'] = []
        if self.cluster_results is not None:
            for k1 in self.cluster_results:
                result['ClusterResults'].append(k1.to_map() if k1 else None)

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.max_clustered_topic_news_size is not None:
            result['MaxClusteredTopicNewsSize'] = self.max_clustered_topic_news_size

        if self.parsed_news_size is not None:
            result['ParsedNewsSize'] = self.parsed_news_size

        if self.status is not None:
            result['Status'] = self.status

        if self.rt is not None:
            result['rt'] = self.rt

        if self.usages is not None:
            result['usages'] = self.usages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')

        self.cluster_results = []
        if m.get('ClusterResults') is not None:
            for k1 in m.get('ClusterResults'):
                temp_model = main_models.GetCustomSourceTopicAnalysisTaskResponseBodyDataClusterResults()
                self.cluster_results.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MaxClusteredTopicNewsSize') is not None:
            self.max_clustered_topic_news_size = m.get('MaxClusteredTopicNewsSize')

        if m.get('ParsedNewsSize') is not None:
            self.parsed_news_size = m.get('ParsedNewsSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('rt') is not None:
            self.rt = m.get('rt')

        if m.get('usages') is not None:
            self.usages = m.get('usages')

        return self

class GetCustomSourceTopicAnalysisTaskResponseBodyDataClusterResults(DaraModel):
    def __init__(
        self,
        cluster_news: List[main_models.GetCustomSourceTopicAnalysisTaskResponseBodyDataClusterResultsClusterNews] = None,
        topic: str = None,
    ):
        self.cluster_news = cluster_news
        self.topic = topic

    def validate(self):
        if self.cluster_news:
            for v1 in self.cluster_news:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterNews'] = []
        if self.cluster_news is not None:
            for k1 in self.cluster_news:
                result['ClusterNews'].append(k1.to_map() if k1 else None)

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_news = []
        if m.get('ClusterNews') is not None:
            for k1 in m.get('ClusterNews'):
                temp_model = main_models.GetCustomSourceTopicAnalysisTaskResponseBodyDataClusterResultsClusterNews()
                self.cluster_news.append(temp_model.from_map(k1))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class GetCustomSourceTopicAnalysisTaskResponseBodyDataClusterResultsClusterNews(DaraModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

