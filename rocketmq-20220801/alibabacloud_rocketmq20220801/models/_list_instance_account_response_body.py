# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListInstanceAccountResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.ListInstanceAccountResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The ID of the request. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListInstanceAccountResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListInstanceAccountResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListInstanceAccountResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The pagination information.
        self.list = list
        # The page number.
        self.page_number = page_number
        # Number of items per page.
        self.page_size = page_size
        # The total number of returned entries.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListInstanceAccountResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListInstanceAccountResponseBodyDataList(DaraModel):
    def __init__(
        self,
        account_status: str = None,
        account_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        username: str = None,
    ):
        # The status of the account.
        # Valid values:
        #   - DISABLE
        #   - ENABLE
        self.account_status = account_status
        # The account type.
        #   - CUSTOMER
        #   - DEFAULT
        self.account_type = account_type
        # The instance ID.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The username of the account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_status is not None:
            result['accountStatus'] = self.account_status

        if self.account_type is not None:
            result['accountType'] = self.account_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')

        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

