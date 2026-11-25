# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRepoTagScanStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        scan_service: str = None,
        status: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API call was successful. Valid values:
        # 
        # - `true`: The API call succeeded.
        # 
        # - `false`: The API call failed.
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The scan engine type. Valid values:
        # - `ACR_SCAN_SERVICE`: The ACR Trivy scan engine.
        # - `SAS_SCAN_SERVICE`: The cloud security scan engine.
        self.scan_service = scan_service
        # The scan status of the image version. Valid values:
        # 
        # - `SCANNING`: Scanning.
        # 
        # - `COMPLETE`: Completed.
        # 
        # - `FAILED`: Failed.
        # 
        # - `RETRYING`: Retrying.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scan_service is not None:
            result['ScanService'] = self.scan_service

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

