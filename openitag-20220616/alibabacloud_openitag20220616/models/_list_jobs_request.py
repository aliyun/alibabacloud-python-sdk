# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobsRequest(DaraModel):
    def __init__(
        self,
        job_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # Task Type. Currently, only DOWNLOWD_MARKRESULT_FLOW is available.
        self.job_type = job_type
        # The quantity of annotation results displayed per page in a paged query. The default value is 20.
        self.page_number = page_number
        # The page number of the annotation result list. The starting value is 1, and the default value is 1.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

