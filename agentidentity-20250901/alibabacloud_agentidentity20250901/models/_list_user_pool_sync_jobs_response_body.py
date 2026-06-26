# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListUserPoolSyncJobsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        synchronization_jobs: List[main_models.ListUserPoolSyncJobsResponseBodySynchronizationJobs] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.synchronization_jobs = synchronization_jobs
        self.total_count = total_count

    def validate(self):
        if self.synchronization_jobs:
            for v1 in self.synchronization_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SynchronizationJobs'] = []
        if self.synchronization_jobs is not None:
            for k1 in self.synchronization_jobs:
                result['SynchronizationJobs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.synchronization_jobs = []
        if m.get('SynchronizationJobs') is not None:
            for k1 in m.get('SynchronizationJobs'):
                temp_model = main_models.ListUserPoolSyncJobsResponseBodySynchronizationJobs()
                self.synchronization_jobs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserPoolSyncJobsResponseBodySynchronizationJobs(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        error_message: str = None,
        identity_provider_type: str = None,
        job_summary: main_models.ListUserPoolSyncJobsResponseBodySynchronizationJobsJobSummary = None,
        start_time: str = None,
        status: str = None,
        synchronization_job_id: str = None,
        trigger_type: str = None,
    ):
        self.end_time = end_time
        self.error_message = error_message
        self.identity_provider_type = identity_provider_type
        self.job_summary = job_summary
        self.start_time = start_time
        self.status = status
        self.synchronization_job_id = synchronization_job_id
        self.trigger_type = trigger_type

    def validate(self):
        if self.job_summary:
            self.job_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.job_summary is not None:
            result['JobSummary'] = self.job_summary.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('JobSummary') is not None:
            temp_model = main_models.ListUserPoolSyncJobsResponseBodySynchronizationJobsJobSummary()
            self.job_summary = temp_model.from_map(m.get('JobSummary'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class ListUserPoolSyncJobsResponseBodySynchronizationJobsJobSummary(DaraModel):
    def __init__(
        self,
        created: str = None,
        deleted: str = None,
        same: str = None,
        updated: str = None,
    ):
        self.created = created
        self.deleted = deleted
        self.same = same
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['Created'] = self.created

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.same is not None:
            result['Same'] = self.same

        if self.updated is not None:
            result['Updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('Same') is not None:
            self.same = m.get('Same')

        if m.get('Updated') is not None:
            self.updated = m.get('Updated')

        return self

