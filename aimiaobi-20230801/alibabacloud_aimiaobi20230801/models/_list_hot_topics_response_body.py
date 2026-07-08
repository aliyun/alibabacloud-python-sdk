# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListHotTopicsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListHotTopicsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of results returned on this page.
        self.max_results = max_results
        # The result message for the request.
        self.message = message
        # The token to retrieve the next page of results.
        self.next_token = next_token
        # The unique ID for the request.
        self.request_id = request_id
        # Indicates whether the request was successful. A value of `true` indicates success; `false` indicates failure.
        self.success = success
        # The total number of topics found.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListHotTopicsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHotTopicsResponseBodyData(DaraModel):
    def __init__(
        self,
        async_task_id: str = None,
        create_time: str = None,
        create_user: str = None,
        custom_field: str = None,
        hot_value: int = None,
        id: str = None,
        status: str = None,
        structure_summary: List[main_models.ListHotTopicsResponseBodyDataStructureSummary] = None,
        summary: str = None,
        task_error_message: str = None,
        task_status: int = None,
        topic: str = None,
        topic_source: str = None,
        topic_url: str = None,
        version: str = None,
    ):
        # The asynchronous task ID. This parameter is returned only when `TopicSource` is `Custom`.
        self.async_task_id = async_task_id
        # The time the topic was created, in `yyyy-MM-dd HH:mm:ss` format.
        self.create_time = create_time
        # The ID of the user who created the topic. This parameter is returned only when `TopicSource` is `Custom`.
        self.create_user = create_user
        # A custom field for business-specific data, such as a keyword.
        self.custom_field = custom_field
        # The popularity score of the topic.
        self.hot_value = hot_value
        # The ID of the hot topic.
        self.id = id
        # The asynchronous task status. This parameter is returned only when `TopicSource` is `Custom`. Valid values: `PENDING`, `RUNNING`, `SUCCEEDED`, `SUSPENDED`, `FAILED`, and `CANCELED`.
        self.status = status
        # A list of structured topic summaries.
        self.structure_summary = structure_summary
        # The hot topic summary.
        self.summary = summary
        # The error message returned when the asynchronous task fails.
        self.task_error_message = task_error_message
        # The asynchronous task status. This parameter is returned only when `TopicSource` is `Custom`. Valid values: `0` (Pending), `1` (Running), `2` (Succeeded), `3` (Suspended, not currently in use), `4` (Failed), and `6` (Canceled).
        self.task_status = task_status
        # The unique topic name.
        self.topic = topic
        # The source of the hot topic. Valid values:
        # 
        # - `Toutiao`
        # 
        # - `Quark`
        # 
        # - `Baidu`
        # 
        # - `Sina`
        # 
        # - `Custom`
        # 
        # - `Aggregation`
        self.topic_source = topic_source
        # The URL of the original topic.
        self.topic_url = topic_url
        # The data version.
        self.version = version

    def validate(self):
        if self.structure_summary:
            for v1 in self.structure_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.custom_field is not None:
            result['CustomField'] = self.custom_field

        if self.hot_value is not None:
            result['HotValue'] = self.hot_value

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        result['StructureSummary'] = []
        if self.structure_summary is not None:
            for k1 in self.structure_summary:
                result['StructureSummary'].append(k1.to_map() if k1 else None)

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source

        if self.topic_url is not None:
            result['TopicUrl'] = self.topic_url

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('CustomField') is not None:
            self.custom_field = m.get('CustomField')

        if m.get('HotValue') is not None:
            self.hot_value = m.get('HotValue')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.structure_summary = []
        if m.get('StructureSummary') is not None:
            for k1 in m.get('StructureSummary'):
                temp_model = main_models.ListHotTopicsResponseBodyDataStructureSummary()
                self.structure_summary.append(temp_model.from_map(k1))

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')

        if m.get('TopicUrl') is not None:
            self.topic_url = m.get('TopicUrl')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListHotTopicsResponseBodyDataStructureSummary(DaraModel):
    def __init__(
        self,
        doc_list: List[main_models.ListHotTopicsResponseBodyDataStructureSummaryDocList] = None,
        summary: str = None,
        title: str = None,
    ):
        # A list of articles used to generate the title and summary.
        self.doc_list = doc_list
        # The generated summary.
        self.summary = summary
        # The generated title.
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
                temp_model = main_models.ListHotTopicsResponseBodyDataStructureSummaryDocList()
                self.doc_list.append(temp_model.from_map(k1))

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class ListHotTopicsResponseBodyDataStructureSummaryDocList(DaraModel):
    def __init__(
        self,
        source: str = None,
        title: str = None,
        url: str = None,
    ):
        # The source of the article.
        self.source = source
        # The article title.
        self.title = title
        # The article URL.
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

