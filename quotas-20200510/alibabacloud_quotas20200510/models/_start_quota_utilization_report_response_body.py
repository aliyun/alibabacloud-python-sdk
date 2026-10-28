# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartQuotaUtilizationReportResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        message: str = None,
        next_refresh_time: str = None,
        refresh_success: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.message = message
        self.next_refresh_time = next_refresh_time
        self.refresh_success = refresh_success
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.message is not None:
            result['Message'] = self.message

        if self.next_refresh_time is not None:
            result['NextRefreshTime'] = self.next_refresh_time

        if self.refresh_success is not None:
            result['RefreshSuccess'] = self.refresh_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextRefreshTime') is not None:
            self.next_refresh_time = m.get('NextRefreshTime')

        if m.get('RefreshSuccess') is not None:
            self.refresh_success = m.get('RefreshSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

