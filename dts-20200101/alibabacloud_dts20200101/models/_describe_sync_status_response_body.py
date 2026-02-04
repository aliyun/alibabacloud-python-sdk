# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSyncStatusResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        page_number: int = None,
        request_id: str = None,
        success: bool = None,
        sync_status_list: List[main_models.DescribeSyncStatusResponseBodySyncStatusList] = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.page_number = page_number
        self.request_id = request_id
        self.success = success
        self.sync_status_list = sync_status_list

    def validate(self):
        if self.sync_status_list:
            for v1 in self.sync_status_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['SyncStatusList'] = []
        if self.sync_status_list is not None:
            for k1 in self.sync_status_list:
                result['SyncStatusList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.sync_status_list = []
        if m.get('SyncStatusList') is not None:
            for k1 in m.get('SyncStatusList'):
                temp_model = main_models.DescribeSyncStatusResponseBodySyncStatusList()
                self.sync_status_list.append(temp_model.from_map(k1))

        return self

class DescribeSyncStatusResponseBodySyncStatusList(DaraModel):
    def __init__(
        self,
        checkpoint: int = None,
        code: str = None,
        delay: int = None,
        job_id: str = None,
        rate: str = None,
        status: str = None,
    ):
        self.checkpoint = checkpoint
        self.code = code
        self.delay = delay
        self.job_id = job_id
        self.rate = rate
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.code is not None:
            result['Code'] = self.code

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

