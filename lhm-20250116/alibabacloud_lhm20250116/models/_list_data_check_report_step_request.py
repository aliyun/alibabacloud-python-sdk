# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataCheckReportStepRequest(DaraModel):
    def __init__(
        self,
        check_result: int = None,
        job_id: int = None,
        job_status: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # The verification result filter. Valid values:
        # 
        # - 0: no record.
        # - 1: passed.
        # - 2: failed.
        self.check_result = check_result
        # The job database ID (integer) that identifies a verification sub-job. This parameter differs in format from the UUID-format sub-job ID (string) used in the operation that queries step details by UUID. The two are not interchangeable.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The step status filter. Valid values:
        # 
        # - 0: INIT.
        # - 1: RUNNING.
        # - 2: FINISHED.
        # - 3: STOPPED.
        # - 4: FAIL.
        # - 6: READY.
        # - 7: SKIPPED.
        self.job_status = job_status
        # The page number. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_result is not None:
            result['checkResult'] = self.check_result

        if self.job_id is not None:
            result['jobId'] = self.job_id

        if self.job_status is not None:
            result['jobStatus'] = self.job_status

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkResult') is not None:
            self.check_result = m.get('checkResult')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        if m.get('jobStatus') is not None:
            self.job_status = m.get('jobStatus')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

