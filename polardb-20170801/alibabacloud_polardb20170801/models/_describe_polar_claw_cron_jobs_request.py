# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePolarClawCronJobsRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        include_disabled: bool = None,
        include_runs: bool = None,
        job_id_list: List[str] = None,
        run_limit: int = None,
    ):
        # Application ID
        # 
        # This parameter is required.
        self.application_id = application_id
        # Include disabled tasks. Default is true.
        self.include_disabled = include_disabled
        # Include run history. Default is false.
        self.include_runs = include_runs
        # Filter by Job ID list
        self.job_id_list = job_id_list
        # Maximum number of run history entries per task. Default is 10.
        self.run_limit = run_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.include_disabled is not None:
            result['IncludeDisabled'] = self.include_disabled

        if self.include_runs is not None:
            result['IncludeRuns'] = self.include_runs

        if self.job_id_list is not None:
            result['JobIdList'] = self.job_id_list

        if self.run_limit is not None:
            result['RunLimit'] = self.run_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('IncludeDisabled') is not None:
            self.include_disabled = m.get('IncludeDisabled')

        if m.get('IncludeRuns') is not None:
            self.include_runs = m.get('IncludeRuns')

        if m.get('JobIdList') is not None:
            self.job_id_list = m.get('JobIdList')

        if m.get('RunLimit') is not None:
            self.run_limit = m.get('RunLimit')

        return self

