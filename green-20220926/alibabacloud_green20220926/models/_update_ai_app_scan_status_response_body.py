# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateAiAppScanStatusResponseBody(DaraModel):
    def __init__(
        self,
        failed_app_ids: List[str] = None,
        request_id: str = None,
        status: str = None,
        success_app_ids: List[str] = None,
    ):
        # The list of application IDs that failed.
        self.failed_app_ids = failed_app_ids
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The status. Valid values:
        # 
        # - SUCCESS: Succeeded.
        # 
        # - PARTIAL_SUCCESS: Partially succeeded.
        # 
        # - FAILED: Failed.
        self.status = status
        # The list of application IDs that succeeded.
        self.success_app_ids = success_app_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_app_ids is not None:
            result['FailedAppIds'] = self.failed_app_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success_app_ids is not None:
            result['SuccessAppIds'] = self.success_app_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedAppIds') is not None:
            self.failed_app_ids = m.get('FailedAppIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuccessAppIds') is not None:
            self.success_app_ids = m.get('SuccessAppIds')

        return self

