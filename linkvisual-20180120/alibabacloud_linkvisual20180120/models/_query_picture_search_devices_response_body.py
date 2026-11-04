# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryPictureSearchDevicesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryPictureSearchDevicesResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/145071.html).
        self.code = code
        # The response data.
        self.data = data
        # The error message returned if the call fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryPictureSearchDevicesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPictureSearchDevicesResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_count: int = None,
        page_data: List[main_models.QueryPictureSearchDevicesResponseBodyDataPageData] = None,
        page_size: int = None,
        total: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The total number of pages.
        self.page_count = page_count
        # The list of applications.
        self.page_data = page_data
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.page_data:
            for v1 in self.page_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        result['PageData'] = []
        if self.page_data is not None:
            for k1 in self.page_data:
                result['PageData'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        self.page_data = []
        if m.get('PageData') is not None:
            for k1 in m.get('PageData'):
                temp_model = main_models.QueryPictureSearchDevicesResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryPictureSearchDevicesResponseBodyDataPageData(DaraModel):
    def __init__(
        self,
        iot_id: str = None,
        nick_name: str = None,
    ):
        # The ID of the device.
        self.iot_id = iot_id
        # The alias of the device.
        # 
        # > This parameter is returned only for IPC devices.
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        return self

