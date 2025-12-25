# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListAnalysisTagDetailByTaskIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAnalysisTagDetailByTaskIdResponseBodyData] = None,
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
                temp_model = main_models.ListAnalysisTagDetailByTaskIdResponseBodyData()
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

class ListAnalysisTagDetailByTaskIdResponseBodyData(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_tags: List[main_models.ListAnalysisTagDetailByTaskIdResponseBodyDataContentTags] = None,
        id: int = None,
        tag_task_type: str = None,
        task_id: str = None,
    ):
        self.content = content
        self.content_tags = content_tags
        self.id = id
        self.tag_task_type = tag_task_type
        self.task_id = task_id

    def validate(self):
        if self.content_tags:
            for v1 in self.content_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        result['ContentTags'] = []
        if self.content_tags is not None:
            for k1 in self.content_tags:
                result['ContentTags'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.tag_task_type is not None:
            result['TagTaskType'] = self.tag_task_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        self.content_tags = []
        if m.get('ContentTags') is not None:
            for k1 in m.get('ContentTags'):
                temp_model = main_models.ListAnalysisTagDetailByTaskIdResponseBodyDataContentTags()
                self.content_tags.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TagTaskType') is not None:
            self.tag_task_type = m.get('TagTaskType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class ListAnalysisTagDetailByTaskIdResponseBodyDataContentTags(DaraModel):
    def __init__(
        self,
        summary_overview: str = None,
        tag_name: str = None,
        tags: List[str] = None,
    ):
        self.summary_overview = summary_overview
        self.tag_name = tag_name
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.summary_overview is not None:
            result['SummaryOverview'] = self.summary_overview

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SummaryOverview') is not None:
            self.summary_overview = m.get('SummaryOverview')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

