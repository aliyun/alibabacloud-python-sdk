# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeDeviceInfoResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        device_info_list: main_models.DescribeDeviceInfoResponseBodyDeviceInfoList = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number being queried.
        self.current_page = current_page
        # Array of device information.
        self.device_info_list = device_info_list
        # Number of items per page.
        self.page_size = page_size
        # The ID of this request.
        self.request_id = request_id
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.device_info_list:
            self.device_info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.device_info_list is not None:
            result['DeviceInfoList'] = self.device_info_list.to_map()

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DeviceInfoList') is not None:
            temp_model = main_models.DescribeDeviceInfoResponseBodyDeviceInfoList()
            self.device_info_list = temp_model.from_map(m.get('DeviceInfoList'))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDeviceInfoResponseBodyDeviceInfoList(DaraModel):
    def __init__(
        self,
        device_info: List[main_models.DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo] = None,
    ):
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            for v1 in self.device_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeviceInfo'] = []
        if self.device_info is not None:
            for k1 in self.device_info:
                result['DeviceInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_info = []
        if m.get('DeviceInfo') is not None:
            for k1 in m.get('DeviceInfo'):
                temp_model = main_models.DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo()
                self.device_info.append(temp_model.from_map(k1))

        return self

class DescribeDeviceInfoResponseBodyDeviceInfoListDeviceInfo(DaraModel):
    def __init__(
        self,
        begin_day: str = None,
        biz_type: str = None,
        device_id: str = None,
        expired_day: str = None,
        user_device_id: str = None,
    ):
        # Authorization start date.
        self.begin_day = begin_day
        # Corresponds to the BizType in the request.
        self.biz_type = biz_type
        # Corresponds to the DeviceId in the request.
        self.device_id = device_id
        # Authorization expiration date.
        self.expired_day = expired_day
        # Corresponds to the UserDeviceId in the request.
        self.user_device_id = user_device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_day is not None:
            result['BeginDay'] = self.begin_day

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.expired_day is not None:
            result['ExpiredDay'] = self.expired_day

        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginDay') is not None:
            self.begin_day = m.get('BeginDay')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('ExpiredDay') is not None:
            self.expired_day = m.get('ExpiredDay')

        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')

        return self

