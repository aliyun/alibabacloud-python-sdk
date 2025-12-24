# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopOversoldGroupResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        data: List[main_models.DescribeDesktopOversoldGroupResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.count = count
        self.data = data
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeDesktopOversoldGroupResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDesktopOversoldGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        concurrence_count: int = None,
        cur_concurrence_count: int = None,
        data_disk_size: int = None,
        description: str = None,
        desktop_type: str = None,
        directory_id: str = None,
        expire_time: str = None,
        idle_disconnect_duration: str = None,
        image_id: str = None,
        keep_duration: str = None,
        name: str = None,
        oversold_group_id: str = None,
        oversold_user_count: int = None,
        oversold_warn: int = None,
        policy_group_id: str = None,
        sale_status: str = None,
        status: str = None,
        stop_duration: int = None,
        system_disk_size: int = None,
    ):
        self.concurrence_count = concurrence_count
        self.cur_concurrence_count = cur_concurrence_count
        self.data_disk_size = data_disk_size
        self.description = description
        self.desktop_type = desktop_type
        self.directory_id = directory_id
        self.expire_time = expire_time
        self.idle_disconnect_duration = idle_disconnect_duration
        self.image_id = image_id
        self.keep_duration = keep_duration
        self.name = name
        self.oversold_group_id = oversold_group_id
        self.oversold_user_count = oversold_user_count
        self.oversold_warn = oversold_warn
        self.policy_group_id = policy_group_id
        self.sale_status = sale_status
        self.status = status
        self.stop_duration = stop_duration
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrence_count is not None:
            result['ConcurrenceCount'] = self.concurrence_count

        if self.cur_concurrence_count is not None:
            result['CurConcurrenceCount'] = self.cur_concurrence_count

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration

        if self.name is not None:
            result['Name'] = self.name

        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.oversold_user_count is not None:
            result['OversoldUserCount'] = self.oversold_user_count

        if self.oversold_warn is not None:
            result['OversoldWarn'] = self.oversold_warn

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.sale_status is not None:
            result['SaleStatus'] = self.sale_status

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrenceCount') is not None:
            self.concurrence_count = m.get('ConcurrenceCount')

        if m.get('CurConcurrenceCount') is not None:
            self.cur_concurrence_count = m.get('CurConcurrenceCount')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('OversoldUserCount') is not None:
            self.oversold_user_count = m.get('OversoldUserCount')

        if m.get('OversoldWarn') is not None:
            self.oversold_warn = m.get('OversoldWarn')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('SaleStatus') is not None:
            self.sale_status = m.get('SaleStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

