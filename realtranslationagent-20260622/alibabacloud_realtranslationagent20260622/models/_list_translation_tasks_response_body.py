# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_realtranslationagent20260622 import models as main_models
from darabonba.model import DaraModel

class ListTranslationTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListTranslationTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
            temp_model = main_models.ListTranslationTasksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTranslationTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListTranslationTasksResponseBodyDataList] = None,
        max_results: int = None,
        next_token: str = None,
        total: int = None,
    ):
        self.list = list
        self.max_results = max_results
        self.next_token = next_token
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListTranslationTasksResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListTranslationTasksResponseBodyDataList(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        cost_credits: float = None,
        cost_time: int = None,
        creator: str = None,
        creator_name: str = None,
        error_message: str = None,
        file_format: str = None,
        file_name: str = None,
        gmt_create: str = None,
        org_id: str = None,
        original_file_name: str = None,
        page_count: int = None,
        progress: int = None,
        source_language: str = None,
        start_time: str = None,
        status: str = None,
        target_language: str = None,
        task_id: str = None,
        task_type: str = None,
        template: str = None,
        word_count: int = None,
        work_space_id: str = None,
    ):
        self.complete_time = complete_time
        self.cost_credits = cost_credits
        self.cost_time = cost_time
        self.creator = creator
        self.creator_name = creator_name
        self.error_message = error_message
        self.file_format = file_format
        self.file_name = file_name
        self.gmt_create = gmt_create
        self.org_id = org_id
        self.original_file_name = original_file_name
        self.page_count = page_count
        self.progress = progress
        self.source_language = source_language
        self.start_time = start_time
        self.status = status
        self.target_language = target_language
        self.task_id = task_id
        self.task_type = task_type
        self.template = template
        self.word_count = word_count
        self.work_space_id = work_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.cost_credits is not None:
            result['CostCredits'] = self.cost_credits

        if self.cost_time is not None:
            result['CostTime'] = self.cost_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.template is not None:
            result['Template'] = self.template

        if self.word_count is not None:
            result['WordCount'] = self.word_count

        if self.work_space_id is not None:
            result['WorkSpaceId'] = self.work_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CostCredits') is not None:
            self.cost_credits = m.get('CostCredits')

        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('WordCount') is not None:
            self.word_count = m.get('WordCount')

        if m.get('WorkSpaceId') is not None:
            self.work_space_id = m.get('WorkSpaceId')

        return self

