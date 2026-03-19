# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyStorageStrategyResponseBody(DaraModel):
    def __init__(
        self,
        backup_plan_id: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        need_precheck: bool = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Backup plan ID.
        self.backup_plan_id = backup_plan_id
        # Error code.
        self.err_code = err_code
        # Error message.
        self.err_message = err_message
        # HTTP status code.
        self.http_status_code = http_status_code
        # Indicates whether this modification triggers a precheck. Return values:
        # 
        # - **true**: A precheck is triggered. Manually call the [StartBackupPlan](https://help.aliyun.com/document_detail/2869818.html) API to start the backup plan.
        # 
        # - **false**: No precheck is triggered.
        self.need_precheck = need_precheck
        # Request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Return values:
        # 
        # - **true**: The request was successful.
        # 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_id is not None:
            result['BackupPlanId'] = self.backup_plan_id

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.need_precheck is not None:
            result['NeedPrecheck'] = self.need_precheck

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanId') is not None:
            self.backup_plan_id = m.get('BackupPlanId')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('NeedPrecheck') is not None:
            self.need_precheck = m.get('NeedPrecheck')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

