# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSemanticJobRunsRequest(DaraModel):
    def __init__(
        self,
        job_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The job name. Use the Data.Name value from the CreateSemanticJob response or the Name value from a ListSemanticJobs list item.
        # 
        # This parameter is required.
        self.job_name = job_name
        # The page number, starting from 1. If this parameter is omitted or set to a value less than or equal to 0, page 1 is returned.
        self.page_number = page_number
        # The number of run records per page. If this parameter is omitted or set to a value less than or equal to 0, the default value 50 is used. Maximum value: 200.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

