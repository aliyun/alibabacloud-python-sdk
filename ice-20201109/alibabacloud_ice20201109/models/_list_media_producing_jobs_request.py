# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMediaProducingJobsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        job_type: str = None,
        keyword: str = None,
        master_job_id: str = None,
        max_results: int = None,
        next_token: str = None,
        project_id: str = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
    ):
        # The end of the time range to query. The maximum time range between EndTime and StartTime cannot exceed 30 days. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The job type.
        # 
        # Valid values:
        # 
        # *   LiveEditingJob: live editing job.
        # *   EditingJob: regular template-based editing job
        # *   VETemplateJob: advanced template-based editing job.
        self.job_type = job_type
        # The search keyword. For example, you can use a job ID as the keyword to search for jobs.
        self.keyword = keyword
        # The ID of the quick video production job. If this parameter is specified, the subjobs of the quick video production job are queried.
        self.master_job_id = master_job_id
        # The maximum number of entries to return.
        # 
        # Default value: 10. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the online editing project.
        self.project_id = project_id
        # The sorting parameter. By default, the query results are sorted by creation time in descending order.
        # 
        # Valid values:
        # 
        # *   CreationTime:Asc: sorted by creation time in ascending order.
        # *   CreationTime:Desc: sorted by creation time in descending order.
        self.sort_by = sort_by
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time
        # The job state.
        # 
        # Valid values:
        # 
        # *   Init: The job is initialized.
        # *   Failed: The job failed.
        # *   Success: The job is successful.
        # *   Processing: The job is in progress.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.master_job_id is not None:
            result['MasterJobId'] = self.master_job_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MasterJobId') is not None:
            self.master_job_id = m.get('MasterJobId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

