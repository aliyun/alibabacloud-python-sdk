# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class ListModelLimitsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        limits: List[main_models.ListModelLimitsResponseBodyLimits] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response status code.
        self.code = code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The model throttling information.
        self.limits = limits
        # The maximum number of records returned in a single request.
        self.max_results = max_results
        # The token for the next request.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # Indicates whether the API call was successful.
        self.success = success
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.limits:
            for v1 in self.limits:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['limits'] = []
        if self.limits is not None:
            for k1 in self.limits:
                result['limits'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.limits = []
        if m.get('limits') is not None:
            for k1 in m.get('limits'):
                temp_model = main_models.ListModelLimitsResponseBodyLimits()
                self.limits.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListModelLimitsResponseBodyLimits(DaraModel):
    def __init__(
        self,
        model: str = None,
        model_limit: main_models.ListModelLimitsResponseBodyLimitsModelLimit = None,
        name: str = None,
        workspace_limit: main_models.ListModelLimitsResponseBodyLimitsWorkspaceLimit = None,
    ):
        # The model.
        self.model = model
        # The model throttling configuration for the current user account.
        self.model_limit = model_limit
        # The model name.
        self.name = name
        # The custom model throttling configuration for the current workspace.
        self.workspace_limit = workspace_limit

    def validate(self):
        if self.model_limit:
            self.model_limit.validate()
        if self.workspace_limit:
            self.workspace_limit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['model'] = self.model

        if self.model_limit is not None:
            result['modelLimit'] = self.model_limit.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.workspace_limit is not None:
            result['workspaceLimit'] = self.workspace_limit.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('modelLimit') is not None:
            temp_model = main_models.ListModelLimitsResponseBodyLimitsModelLimit()
            self.model_limit = temp_model.from_map(m.get('modelLimit'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('workspaceLimit') is not None:
            temp_model = main_models.ListModelLimitsResponseBodyLimitsWorkspaceLimit()
            self.workspace_limit = temp_model.from_map(m.get('workspaceLimit'))

        return self

class ListModelLimitsResponseBodyLimitsWorkspaceLimit(DaraModel):
    def __init__(
        self,
        async_user_concurrency_limit: int = None,
        async_user_queue_limit: int = None,
        request_limit: int = None,
        request_limit_period: int = None,
        usage_limit: int = None,
        usage_limit_field: str = None,
        usage_limit_period: int = None,
    ):
        # The maximum concurrency.
        self.async_user_concurrency_limit = async_user_concurrency_limit
        # The queue size.
        self.async_user_queue_limit = async_user_queue_limit
        # The request throttling value.
        self.request_limit = request_limit
        # The time period for request throttling, in seconds.
        self.request_limit_period = request_limit_period
        # The usage throttling value.
        self.usage_limit = usage_limit
        # The usage throttling unit.
        self.usage_limit_field = usage_limit_field
        # The time period for usage throttling, in seconds.
        self.usage_limit_period = usage_limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_user_concurrency_limit is not None:
            result['asyncUserConcurrencyLimit'] = self.async_user_concurrency_limit

        if self.async_user_queue_limit is not None:
            result['asyncUserQueueLimit'] = self.async_user_queue_limit

        if self.request_limit is not None:
            result['requestLimit'] = self.request_limit

        if self.request_limit_period is not None:
            result['requestLimitPeriod'] = self.request_limit_period

        if self.usage_limit is not None:
            result['usageLimit'] = self.usage_limit

        if self.usage_limit_field is not None:
            result['usageLimitField'] = self.usage_limit_field

        if self.usage_limit_period is not None:
            result['usageLimitPeriod'] = self.usage_limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncUserConcurrencyLimit') is not None:
            self.async_user_concurrency_limit = m.get('asyncUserConcurrencyLimit')

        if m.get('asyncUserQueueLimit') is not None:
            self.async_user_queue_limit = m.get('asyncUserQueueLimit')

        if m.get('requestLimit') is not None:
            self.request_limit = m.get('requestLimit')

        if m.get('requestLimitPeriod') is not None:
            self.request_limit_period = m.get('requestLimitPeriod')

        if m.get('usageLimit') is not None:
            self.usage_limit = m.get('usageLimit')

        if m.get('usageLimitField') is not None:
            self.usage_limit_field = m.get('usageLimitField')

        if m.get('usageLimitPeriod') is not None:
            self.usage_limit_period = m.get('usageLimitPeriod')

        return self

class ListModelLimitsResponseBodyLimitsModelLimit(DaraModel):
    def __init__(
        self,
        async_user_concurrency_limit: int = None,
        async_user_queue_limit: int = None,
        request_limit: int = None,
        request_limit_period: int = None,
        usage_limit: int = None,
        usage_limit_field: str = None,
        usage_limit_period: int = None,
    ):
        # The maximum concurrency.
        self.async_user_concurrency_limit = async_user_concurrency_limit
        # The queue size.
        self.async_user_queue_limit = async_user_queue_limit
        # The request throttling value.
        self.request_limit = request_limit
        # The time period for request throttling, in seconds.
        self.request_limit_period = request_limit_period
        # The usage throttling value.
        self.usage_limit = usage_limit
        # The usage throttling unit.
        self.usage_limit_field = usage_limit_field
        # The time period for usage throttling, in seconds.
        self.usage_limit_period = usage_limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_user_concurrency_limit is not None:
            result['asyncUserConcurrencyLimit'] = self.async_user_concurrency_limit

        if self.async_user_queue_limit is not None:
            result['asyncUserQueueLimit'] = self.async_user_queue_limit

        if self.request_limit is not None:
            result['requestLimit'] = self.request_limit

        if self.request_limit_period is not None:
            result['requestLimitPeriod'] = self.request_limit_period

        if self.usage_limit is not None:
            result['usageLimit'] = self.usage_limit

        if self.usage_limit_field is not None:
            result['usageLimitField'] = self.usage_limit_field

        if self.usage_limit_period is not None:
            result['usageLimitPeriod'] = self.usage_limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asyncUserConcurrencyLimit') is not None:
            self.async_user_concurrency_limit = m.get('asyncUserConcurrencyLimit')

        if m.get('asyncUserQueueLimit') is not None:
            self.async_user_queue_limit = m.get('asyncUserQueueLimit')

        if m.get('requestLimit') is not None:
            self.request_limit = m.get('requestLimit')

        if m.get('requestLimitPeriod') is not None:
            self.request_limit_period = m.get('requestLimitPeriod')

        if m.get('usageLimit') is not None:
            self.usage_limit = m.get('usageLimit')

        if m.get('usageLimitField') is not None:
            self.usage_limit_field = m.get('usageLimitField')

        if m.get('usageLimitPeriod') is not None:
            self.usage_limit_period = m.get('usageLimitPeriod')

        return self

