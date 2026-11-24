# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressConnectRouterAllowedPrefixHistoryResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allowed_prefix_history_list: List[main_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList] = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The list of historical prefix routes.
        self.allowed_prefix_history_list = allowed_prefix_history_list
        # Indicates whether the call was successful. A value of 200 indicates that the operation was successful. Other values indicate that the operation failed. For more information about the causes of failures, see error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace `%s` in the error message of the **ErrMessage** response parameter.
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message returned for the operation.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **True**: Successful.
        # - **False**: Failed.
        self.success = success

    def validate(self):
        if self.allowed_prefix_history_list:
            for v1 in self.allowed_prefix_history_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['AllowedPrefixHistoryList'] = []
        if self.allowed_prefix_history_list is not None:
            for k1 in self.allowed_prefix_history_list:
                result['AllowedPrefixHistoryList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.allowed_prefix_history_list = []
        if m.get('AllowedPrefixHistoryList') is not None:
            for k1 in m.get('AllowedPrefixHistoryList'):
                temp_model = main_models.DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList()
                self.allowed_prefix_history_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeExpressConnectRouterAllowedPrefixHistoryResponseBodyAllowedPrefixHistoryList(DaraModel):
    def __init__(
        self,
        allowed_prefix: List[str] = None,
        gmt_create: str = None,
    ):
        # The prefix route.
        self.allowed_prefix = allowed_prefix
        # The time when the historical route entry was created.
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_prefix is not None:
            result['AllowedPrefix'] = self.allowed_prefix

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedPrefix') is not None:
            self.allowed_prefix = m.get('AllowedPrefix')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        return self

