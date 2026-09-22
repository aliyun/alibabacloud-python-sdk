# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetGuardStatusResponseBody(DaraModel):
    def __init__(
        self,
        log_scan_status: List[main_models.GetGuardStatusResponseBodyLogScanStatus] = None,
        protection_status: List[main_models.GetGuardStatusResponseBodyProtectionStatus] = None,
        real_time_status: List[main_models.GetGuardStatusResponseBodyRealTimeStatus] = None,
        request_id: str = None,
    ):
        # The list of log scan statistics.
        self.log_scan_status = log_scan_status
        # The list of protection status statistics.
        self.protection_status = protection_status
        # The list of real-time protection statistics.
        self.real_time_status = real_time_status
        # The ID assigned by the backend to uniquely identify a request. This ID can be used to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.log_scan_status:
            for v1 in self.log_scan_status:
                 if v1:
                    v1.validate()
        if self.protection_status:
            for v1 in self.protection_status:
                 if v1:
                    v1.validate()
        if self.real_time_status:
            for v1 in self.real_time_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogScanStatus'] = []
        if self.log_scan_status is not None:
            for k1 in self.log_scan_status:
                result['LogScanStatus'].append(k1.to_map() if k1 else None)

        result['ProtectionStatus'] = []
        if self.protection_status is not None:
            for k1 in self.protection_status:
                result['ProtectionStatus'].append(k1.to_map() if k1 else None)

        result['RealTimeStatus'] = []
        if self.real_time_status is not None:
            for k1 in self.real_time_status:
                result['RealTimeStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_scan_status = []
        if m.get('LogScanStatus') is not None:
            for k1 in m.get('LogScanStatus'):
                temp_model = main_models.GetGuardStatusResponseBodyLogScanStatus()
                self.log_scan_status.append(temp_model.from_map(k1))

        self.protection_status = []
        if m.get('ProtectionStatus') is not None:
            for k1 in m.get('ProtectionStatus'):
                temp_model = main_models.GetGuardStatusResponseBodyProtectionStatus()
                self.protection_status.append(temp_model.from_map(k1))

        self.real_time_status = []
        if m.get('RealTimeStatus') is not None:
            for k1 in m.get('RealTimeStatus'):
                temp_model = main_models.GetGuardStatusResponseBodyRealTimeStatus()
                self.real_time_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetGuardStatusResponseBodyRealTimeStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
    ):
        # The status. Valid values:
        # - enabled: Running.
        # - disabled: Not accessed.
        self.status = status
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetGuardStatusResponseBodyProtectionStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
    ):
        # The status. Valid values:
        # - enabled: Running.
        # - disabled: Not accessed.
        self.status = status
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetGuardStatusResponseBodyLogScanStatus(DaraModel):
    def __init__(
        self,
        status: str = None,
        type: str = None,
    ):
        # The status. Valid values:
        # - enabled: Running.
        # - disabled: Not accessed.
        self.status = status
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

