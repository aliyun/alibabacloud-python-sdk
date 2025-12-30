# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class BatchQueryPushStatusResponseBody(DaraModel):
    def __init__(
        self,
        allow_retry: bool = None,
        http_status_code: int = None,
        max_results: int = None,
        module: main_models.BatchQueryPushStatusResponseBodyModule = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.allow_retry = allow_retry
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.module = module
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Module') is not None:
            temp_model = main_models.BatchQueryPushStatusResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BatchQueryPushStatusResponseBodyModule(DaraModel):
    def __init__(
        self,
        push_results: List[main_models.BatchQueryPushStatusResponseBodyModulePushResults] = None,
    ):
        self.push_results = push_results

    def validate(self):
        if self.push_results:
            for v1 in self.push_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PushResults'] = []
        if self.push_results is not None:
            for k1 in self.push_results:
                result['PushResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_results = []
        if m.get('PushResults') is not None:
            for k1 in m.get('PushResults'):
                temp_model = main_models.BatchQueryPushStatusResponseBodyModulePushResults()
                self.push_results.append(temp_model.from_map(k1))

        return self

class BatchQueryPushStatusResponseBodyModulePushResults(DaraModel):
    def __init__(
        self,
        out_biz_id: str = None,
        push_no: str = None,
        status: str = None,
        status_desc: str = None,
    ):
        self.out_biz_id = out_biz_id
        self.push_no = push_no
        self.status = status
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.push_no is not None:
            result['PushNo'] = self.push_no

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('PushNo') is not None:
            self.push_no = m.get('PushNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        return self

