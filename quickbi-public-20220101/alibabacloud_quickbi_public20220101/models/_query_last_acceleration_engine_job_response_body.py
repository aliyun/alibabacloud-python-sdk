# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryLastAccelerationEngineJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryLastAccelerationEngineJobResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # The entity of the most recent acceleration task.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryLastAccelerationEngineJobResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryLastAccelerationEngineJobResponseBodyResult(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        job_history_id: str = None,
        status: str = None,
    ):
        # Execution time, in the format yyyy-MM-dd hh:mm:ss.
        self.gmt_create = gmt_create
        # Completion time, in the format yyyy-MM-dd hh:mm:ss.
        self.gmt_modified = gmt_modified
        # Acceleration task ID.
        self.job_history_id = job_history_id
        # Task status. Possible values:
        # 
        # - TODO -- To be run
        # - RUNNING -- Running
        # - SUCCESS -- Successfully completed
        # - FAILURE -- Abnormally terminated
        # - CANCELED -- Canceled
        # - CHECK_DEPENDENCY -- Checking dependencies
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.job_history_id is not None:
            result['JobHistoryId'] = self.job_history_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('JobHistoryId') is not None:
            self.job_history_id = m.get('JobHistoryId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

