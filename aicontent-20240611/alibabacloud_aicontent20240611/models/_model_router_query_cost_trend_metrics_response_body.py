# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterQueryCostTrendMetricsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CostQueryTrendDTO = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data object containing the cost trend metrics.
        self.data = data
        # The error code returned when the request fails.
        self.err_code = err_code
        # The error message returned when the request fails.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of results returned per page.
        self.max_results = max_results
        # A token to retrieve the next page of results. If no token is returned, all results have been retrieved.
        self.next_token = next_token
        # The unique request ID. If you encounter a problem, provide this ID to technical support for troubleshooting.
        self.request_id = request_id
        # Indicates whether the request was successful. A value of `true` indicates success, and `false` indicates failure.
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

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.CostQueryTrendDTO()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

