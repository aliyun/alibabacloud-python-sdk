# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class DevicePageResponseBody(DaraModel):
    def __init__(
        self,
        device_list: List[main_models.DevicePageResponseBodyDeviceList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.device_list = device_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.device_list:
            for v1 in self.device_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeviceList'] = []
        if self.device_list is not None:
            for k1 in self.device_list:
                result['DeviceList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_list = []
        if m.get('DeviceList') is not None:
            for k1 in m.get('DeviceList'):
                temp_model = main_models.DevicePageResponseBodyDeviceList()
                self.device_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DevicePageResponseBodyDeviceList(DaraModel):
    def __init__(
        self,
        active_time: str = None,
        aliyun_uid: str = None,
        app_id: str = None,
        daily_count: int = None,
        device_name: str = None,
        order_type: int = None,
        status: int = None,
        sub_aliyun_uid: str = None,
        total_count: int = None,
        user_active_time: str = None,
        workspace_id: str = None,
    ):
        self.active_time = active_time
        self.aliyun_uid = aliyun_uid
        self.app_id = app_id
        self.daily_count = daily_count
        self.device_name = device_name
        self.order_type = order_type
        self.status = status
        self.sub_aliyun_uid = sub_aliyun_uid
        self.total_count = total_count
        self.user_active_time = user_active_time
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.daily_count is not None:
            result['DailyCount'] = self.daily_count

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_aliyun_uid is not None:
            result['SubAliyunUid'] = self.sub_aliyun_uid

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_active_time is not None:
            result['UserActiveTime'] = self.user_active_time

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DailyCount') is not None:
            self.daily_count = m.get('DailyCount')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubAliyunUid') is not None:
            self.sub_aliyun_uid = m.get('SubAliyunUid')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserActiveTime') is not None:
            self.user_active_time = m.get('UserActiveTime')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

