# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SkipPreCheckResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        migration_job_id: str = None,
        request_id: str = None,
        schedule_job_id: str = None,
        skip_items: str = None,
        skip_names: str = None,
        success: bool = None,
    ):
        # The error code. This parameter will be deprecated.
        self.code = code
        # The dynamic error message used to replace the %s variable in the ErrMessage parameter.
        # 
        # > For example, if ErrMessage returns The Value of Input Parameter %s is not valid and DynamicMessage returns JobId, the JobId request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the precheck task.
        self.migration_job_id = migration_job_id
        # The request ID.
        self.request_id = request_id
        # The ID of the precheck task.
        self.schedule_job_id = schedule_job_id
        # The abbreviated names of the precheck items to suppress or unsuppress.
        self.skip_items = skip_items
        # The full names of the precheck items to suppress or unsuppress.
        self.skip_names = skip_names
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schedule_job_id is not None:
            result['ScheduleJobId'] = self.schedule_job_id

        if self.skip_items is not None:
            result['SkipItems'] = self.skip_items

        if self.skip_names is not None:
            result['SkipNames'] = self.skip_names

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScheduleJobId') is not None:
            self.schedule_job_id = m.get('ScheduleJobId')

        if m.get('SkipItems') is not None:
            self.skip_items = m.get('SkipItems')

        if m.get('SkipNames') is not None:
            self.skip_names = m.get('SkipNames')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

