# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListNacosHistoryConfigsResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        history_items: List[main_models.ListNacosHistoryConfigsResponseBodyHistoryItems] = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The configuration items.
        self.history_items = history_items
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.history_items:
            for v1 in self.history_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        result['HistoryItems'] = []
        if self.history_items is not None:
            for k1 in self.history_items:
                result['HistoryItems'].append(k1.to_map() if k1 else None)

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        self.history_items = []
        if m.get('HistoryItems') is not None:
            for k1 in m.get('HistoryItems'):
                temp_model = main_models.ListNacosHistoryConfigsResponseBodyHistoryItems()
                self.history_items.append(temp_model.from_map(k1))

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNacosHistoryConfigsResponseBodyHistoryItems(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        data_id: str = None,
        group: str = None,
        id: int = None,
        last_modified_time: int = None,
        op_type: str = None,
        src_user: str = None,
    ):
        # The application tag.
        self.app_name = app_name
        # The ID of the data.
        self.data_id = data_id
        # The name of the group.
        self.group = group
        # The ID of the configuration.
        self.id = id
        # The timestamp when the configuration was last modified.
        self.last_modified_time = last_modified_time
        # The format of the configuration file.
        self.op_type = op_type
        self.src_user = src_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.group is not None:
            result['Group'] = self.group

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.src_user is not None:
            result['SrcUser'] = self.src_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('SrcUser') is not None:
            self.src_user = m.get('SrcUser')

        return self

