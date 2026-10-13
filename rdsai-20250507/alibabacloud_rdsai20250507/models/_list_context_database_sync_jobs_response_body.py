# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ListContextDatabaseSyncJobsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListContextDatabaseSyncJobsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.ListContextDatabaseSyncJobsResponseBodyData()
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

class ListContextDatabaseSyncJobsResponseBodyData(DaraModel):
    def __init__(
        self,
        jobs: List[main_models.ListContextDatabaseSyncJobsResponseBodyDataJobs] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The list of import tasks.
        self.jobs = jobs
        # The page number. The value starts from 1.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.jobs:
            for v1 in self.jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Jobs'] = []
        if self.jobs is not None:
            for k1 in self.jobs:
                result['Jobs'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('Jobs') is not None:
            for k1 in m.get('Jobs'):
                temp_model = main_models.ListContextDatabaseSyncJobsResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListContextDatabaseSyncJobsResponseBodyDataJobs(DaraModel):
    def __init__(
        self,
        auto_pause_reason: str = None,
        auto_paused: bool = None,
        config_version: int = None,
        enabled: bool = None,
        filters: main_models.ListContextDatabaseSyncJobsResponseBodyDataJobsFilters = None,
        id: str = None,
        knowledge_base_id: str = None,
        name: str = None,
        next_run_at: str = None,
        schedule_type: str = None,
        source_id: str = None,
        target_id: str = None,
    ):
        # The reason for automatic pause.
        self.auto_pause_reason = auto_pause_reason
        # Indicates whether the task is automatically paused.
        self.auto_paused = auto_paused
        # The configuration version number.
        self.config_version = config_version
        # Indicates whether the task is enabled.
        self.enabled = enabled
        # The filter conditions.
        self.filters = filters
        # The task ID, which is a system-generated UUID.
        self.id = id
        # The ID of the target knowledge base.
        self.knowledge_base_id = knowledge_base_id
        # The name.
        self.name = name
        # The time of the next run.
        self.next_run_at = next_run_at
        # The scheduling type. Valid values: interval, daily-times.
        self.schedule_type = schedule_type
        # The data source ID, which is a system-generated UUID.
        self.source_id = source_id
        # The target ID, which is a system-generated UUID.
        self.target_id = target_id

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pause_reason is not None:
            result['AutoPauseReason'] = self.auto_pause_reason

        if self.auto_paused is not None:
            result['AutoPaused'] = self.auto_paused

        if self.config_version is not None:
            result['ConfigVersion'] = self.config_version

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.filters is not None:
            result['Filters'] = self.filters.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.name is not None:
            result['Name'] = self.name

        if self.next_run_at is not None:
            result['NextRunAt'] = self.next_run_at

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPauseReason') is not None:
            self.auto_pause_reason = m.get('AutoPauseReason')

        if m.get('AutoPaused') is not None:
            self.auto_paused = m.get('AutoPaused')

        if m.get('ConfigVersion') is not None:
            self.config_version = m.get('ConfigVersion')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Filters') is not None:
            temp_model = main_models.ListContextDatabaseSyncJobsResponseBodyDataJobsFilters()
            self.filters = temp_model.from_map(m.get('Filters'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextRunAt') is not None:
            self.next_run_at = m.get('NextRunAt')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        return self

class ListContextDatabaseSyncJobsResponseBodyDataJobsFilters(DaraModel):
    def __init__(
        self,
        exclude: List[str] = None,
        excluded_document_ids: List[str] = None,
        include: List[str] = None,
        size_limit: int = None,
        type_allowlist: List[str] = None,
    ):
        # The list of exclusion rules.
        self.exclude = exclude
        # The list of excluded document IDs.
        self.excluded_document_ids = excluded_document_ids
        # The list of inclusion rules.
        self.include = include
        # The size limit in bytes.
        self.size_limit = size_limit
        # The list of allowed document types.
        self.type_allowlist = type_allowlist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.excluded_document_ids is not None:
            result['ExcludedDocumentIds'] = self.excluded_document_ids

        if self.include is not None:
            result['Include'] = self.include

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        if self.type_allowlist is not None:
            result['TypeAllowlist'] = self.type_allowlist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('ExcludedDocumentIds') is not None:
            self.excluded_document_ids = m.get('ExcludedDocumentIds')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        if m.get('TypeAllowlist') is not None:
            self.type_allowlist = m.get('TypeAllowlist')

        return self

