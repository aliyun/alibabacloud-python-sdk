# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class BatchDeployHttpApiRoutesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BatchDeployHttpApiRoutesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code of the API call. For the acceptance or publishing results of each route, see data.results.
        self.code = code
        # The per-route results of the batch publishing operation. Synchronous publishing also returns the numbers of successful and failed routes, whereas asynchronous publishing returns only the per-route acceptance results.
        self.data = data
        # The response message of the API call. If a route fails or is rejected, see the errorMessage of the corresponding route for the cause.
        self.message = message
        # The request ID of the API call. You can use the ID to locate the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.BatchDeployHttpApiRoutesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class BatchDeployHttpApiRoutesResponseBodyData(DaraModel):
    def __init__(
        self,
        failed_count: int = None,
        results: Dict[str, main_models.DataResultsValue] = None,
        success_count: int = None,
    ):
        # The number of routes that failed to be published in the batch. This parameter is returned only for synchronous publishing and can be 0.
        self.failed_count = failed_count
        # A result map with route IDs as keys. If some routes in the same batch fail, the routes that have been successfully published remain valid.
        self.results = results
        # The number of routes successfully published in the batch. This parameter is returned only for synchronous publishing and can be 0.
        self.success_count = success_count

    def validate(self):
        if self.results:
            for v1 in self.results.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count is not None:
            result['failedCount'] = self.failed_count

        result['results'] = {}
        if self.results is not None:
            for k1, v1 in self.results.items():
                result['results'][k1] = v1.to_map() if v1 else None

        if self.success_count is not None:
            result['successCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedCount') is not None:
            self.failed_count = m.get('failedCount')

        self.results = {}
        if m.get('results') is not None:
            for k1, v1 in m.get('results').items():
                temp_model = main_models.DataResultsValue()
                self.results[k1] = temp_model.from_map(v1)

        if m.get('successCount') is not None:
            self.success_count = m.get('successCount')

        return self

