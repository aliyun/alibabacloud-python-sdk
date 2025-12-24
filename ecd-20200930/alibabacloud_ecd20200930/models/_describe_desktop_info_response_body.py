# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopInfoResponseBody(DaraModel):
    def __init__(
        self,
        desktops: List[main_models.DescribeDesktopInfoResponseBodyDesktops] = None,
        request_id: str = None,
    ):
        # The basic information about cloud computers.
        self.desktops = desktops
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.desktops:
            for v1 in self.desktops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Desktops'] = []
        if self.desktops is not None:
            for k1 in self.desktops:
                result['Desktops'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktops = []
        if m.get('Desktops') is not None:
            for k1 in m.get('Desktops'):
                temp_model = main_models.DescribeDesktopInfoResponseBodyDesktops()
                self.desktops.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDesktopInfoResponseBodyDesktops(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        current_app_version: str = None,
        desktop_group_id: str = None,
        desktop_id: str = None,
        desktop_status: str = None,
        management_flag: List[str] = None,
        new_app_size: int = None,
        new_app_version: str = None,
        release_note: str = None,
        start_time: str = None,
    ):
        # The connection status of the user.
        # 
        # Valid values:
        # 
        # *   Connected
        # *   Disconnected
        self.connection_status = connection_status
        # The version of the cloud computer image.
        self.current_app_version = current_app_version
        # The ID of the cloud computer pool.
        self.desktop_group_id = desktop_group_id
        # The ID of the cloud computer.
        self.desktop_id = desktop_id
        # The status of the cloud computer.
        # 
        # Valid values:
        # 
        # *   Stopped
        # *   Failed
        # *   Starting
        # *   Running
        # *   Stopping
        # *   Expired
        # *   Deleted
        # *   Pending
        self.desktop_status = desktop_status
        # The information about flags that are used to manage cloud computers.
        self.management_flag = management_flag
        # The size of the update package. Unit: KB.
        self.new_app_size = new_app_size
        # The version number of the image that can be updated on the cloud computer.
        self.new_app_version = new_app_version
        # The description of the image version that can be updated.
        self.release_note = release_note
        # The time when the cloud computer was first started.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.current_app_version is not None:
            result['CurrentAppVersion'] = self.current_app_version

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_status is not None:
            result['DesktopStatus'] = self.desktop_status

        if self.management_flag is not None:
            result['ManagementFlag'] = self.management_flag

        if self.new_app_size is not None:
            result['NewAppSize'] = self.new_app_size

        if self.new_app_version is not None:
            result['NewAppVersion'] = self.new_app_version

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('CurrentAppVersion') is not None:
            self.current_app_version = m.get('CurrentAppVersion')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopStatus') is not None:
            self.desktop_status = m.get('DesktopStatus')

        if m.get('ManagementFlag') is not None:
            self.management_flag = m.get('ManagementFlag')

        if m.get('NewAppSize') is not None:
            self.new_app_size = m.get('NewAppSize')

        if m.get('NewAppVersion') is not None:
            self.new_app_version = m.get('NewAppVersion')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

