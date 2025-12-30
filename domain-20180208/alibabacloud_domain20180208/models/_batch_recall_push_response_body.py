# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180208 import models as main_models
from darabonba.model import DaraModel

class BatchRecallPushResponseBody(DaraModel):
    def __init__(
        self,
        allow_retry: bool = None,
        http_status_code: int = None,
        module: main_models.BatchRecallPushResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.allow_retry = allow_retry
        self.http_status_code = http_status_code
        self.module = module
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

        if self.module is not None:
            result['Module'] = self.module.to_map()

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

        if m.get('Module') is not None:
            temp_model = main_models.BatchRecallPushResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BatchRecallPushResponseBodyModule(DaraModel):
    def __init__(
        self,
        recall_results: List[main_models.BatchRecallPushResponseBodyModuleRecallResults] = None,
    ):
        self.recall_results = recall_results

    def validate(self):
        if self.recall_results:
            for v1 in self.recall_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RecallResults'] = []
        if self.recall_results is not None:
            for k1 in self.recall_results:
                result['RecallResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recall_results = []
        if m.get('RecallResults') is not None:
            for k1 in m.get('RecallResults'):
                temp_model = main_models.BatchRecallPushResponseBodyModuleRecallResults()
                self.recall_results.append(temp_model.from_map(k1))

        return self

class BatchRecallPushResponseBodyModuleRecallResults(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        out_biz_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.out_biz_id = out_biz_id
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

        if self.message is not None:
            result['Message'] = self.message

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

