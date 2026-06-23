# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetReportTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        out_request_no: str = None,
        task_status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.out_request_no = out_request_no
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.out_request_no is not None:
            result['outRequestNo'] = self.out_request_no

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('outRequestNo') is not None:
            self.out_request_no = m.get('outRequestNo')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        return self

