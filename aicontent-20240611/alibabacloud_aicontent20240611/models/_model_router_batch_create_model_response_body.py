# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterBatchCreateModelResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ModelRouterBatchCreateModelResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data object.
        self.data = data
        # The fault code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ModelRouterBatchCreateModelResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ModelRouterBatchCreateModelResponseBodyData(DaraModel):
    def __init__(
        self,
        created: List[main_models.ModelDTO] = None,
        fail_count: int = None,
        failures: List[main_models.BatchModelErrorDTO] = None,
        success_count: int = None,
    ):
        # The list of models that were successfully created.
        self.created = created
        # The number of models that failed or were skipped.
        self.fail_count = fail_count
        # The list of models that failed or were skipped.
        self.failures = failures
        # The number of models that were successfully created.
        self.success_count = success_count

    def validate(self):
        if self.created:
            for v1 in self.created:
                 if v1:
                    v1.validate()
        if self.failures:
            for v1 in self.failures:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['created'] = []
        if self.created is not None:
            for k1 in self.created:
                result['created'].append(k1.to_map() if k1 else None)

        if self.fail_count is not None:
            result['failCount'] = self.fail_count

        result['failures'] = []
        if self.failures is not None:
            for k1 in self.failures:
                result['failures'].append(k1.to_map() if k1 else None)

        if self.success_count is not None:
            result['successCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.created = []
        if m.get('created') is not None:
            for k1 in m.get('created'):
                temp_model = main_models.ModelDTO()
                self.created.append(temp_model.from_map(k1))

        if m.get('failCount') is not None:
            self.fail_count = m.get('failCount')

        self.failures = []
        if m.get('failures') is not None:
            for k1 in m.get('failures'):
                temp_model = main_models.BatchModelErrorDTO()
                self.failures.append(temp_model.from_map(k1))

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        return self

