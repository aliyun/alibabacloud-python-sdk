# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class GetUpgradeStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetUpgradeStatusResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetUpgradeStatusResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetUpgradeStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        details: str = None,
        from_version: str = None,
        prepare_finish_time: str = None,
        status: str = None,
        to_version: str = None,
    ):
        self.details = details
        self.from_version = from_version
        self.prepare_finish_time = prepare_finish_time
        self.status = status
        self.to_version = to_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.details is not None:
            result['Details'] = self.details

        if self.from_version is not None:
            result['FromVersion'] = self.from_version

        if self.prepare_finish_time is not None:
            result['PrepareFinishTime'] = self.prepare_finish_time

        if self.status is not None:
            result['Status'] = self.status

        if self.to_version is not None:
            result['ToVersion'] = self.to_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('FromVersion') is not None:
            self.from_version = m.get('FromVersion')

        if m.get('PrepareFinishTime') is not None:
            self.prepare_finish_time = m.get('PrepareFinishTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ToVersion') is not None:
            self.to_version = m.get('ToVersion')

        return self

