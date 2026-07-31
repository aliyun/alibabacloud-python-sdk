# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterListSubscriptionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ModelRouterListSubscriptionsResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The subscription information.
        self.data = data
        # The fault error message encoding.
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
            temp_model = main_models.ModelRouterListSubscriptionsResponseBodyData()
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

class ModelRouterListSubscriptionsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.SubscriptionDTO] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The list of subscription information.
        self.list = list
        # The maximum number of results per page. Default value: 20.
        self.max_results = max_results
        # The pagination token. Do not specify this parameter for the first query. For subsequent queries, specify the value returned from the previous query. Set to "" when no more data is available. Set to "5" when there is a next page.
        self.next_token = next_token

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.SubscriptionDTO()
                self.list.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

