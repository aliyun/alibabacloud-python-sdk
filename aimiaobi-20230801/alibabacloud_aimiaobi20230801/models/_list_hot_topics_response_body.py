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
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
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
        create_user: str = None,
        hot_value: int = None,
        id: str = None,
        status: str = None,
        structure_summary: List[main_models.ListHotTopicsResponseBodyDataStructureSummary] = None,
        summary: str = None,
        task_error_message: str = None,
        task_status: int = None,
        topic: str = None,
        topic_source: str = None,
        version: str = None,
    ):
        self.async_task_id = async_task_id
        self.create_user = create_user
        self.hot_value = hot_value
        self.id = id
        self.status = status
        self.structure_summary = structure_summary
        self.summary = summary
        self.task_error_message = task_error_message
        self.task_status = task_status
        self.topic = topic
        self.topic_source = topic_source
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

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

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

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

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

