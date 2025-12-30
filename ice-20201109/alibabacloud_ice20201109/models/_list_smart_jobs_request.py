# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSmartJobsRequest(DaraModel):
    def __init__(
        self,
        job_state: str = None,
        job_type: str = None,
        max_results: int = None,
        next_token: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        # The job state.
        # 
        # Valid values:
        # 
        # *   Finished: The job is complete.
        # *   Failed: The job failed.
        # *   Executing: The job is in progress.
        # *   Created: The job is created.
        self.job_state = job_state
        # The job type.
        # 
        # Valid values:
        # 
        # *   ASR: automatic speech recognition(job) job.
        # *   DynamicChart: dynamic chart job.
        # *   VideoTranslation: video translation job.
        # *   TextToSpeech: intelligent audio production job.
        self.job_type = job_type
        # The maximum number of entries to return.
        # 
        # Default value: 10. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Valid values: 1 to 100.
        self.page_size = page_size
        # The sorting parameter. By default, the query results are sorted by creation time in descending order.
        # 
        # Valid values:
        # 
        # *   CreationTime:Asc: sorted by creation time in ascending order.
        # *   CreationTime:Desc: sorted by creation time in descending order.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_state is not None:
            result['JobState'] = self.job_state

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobState') is not None:
            self.job_state = m.get('JobState')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

