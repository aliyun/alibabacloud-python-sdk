# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListExcessiveDeviceRegistrationApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # A list of excessive device registration applications.
        self.applications = applications
        # The request ID.
        self.request_id = request_id
        # The total number of excessive device registration applications.
        self.total_num = total_num

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListExcessiveDeviceRegistrationApplicationsResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        create_time: str = None,
        department: str = None,
        description: str = None,
        device_tag: str = None,
        device_type: str = None,
        full_department: List[str] = None,
        hostname: str = None,
        is_used: bool = None,
        mac: str = None,
        sase_user_id: str = None,
        status: str = None,
        username: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The creation time of the excessive device registration application.
        self.create_time = create_time
        # The user\\"s department.
        self.department = department
        # The reason for the excessive device registration application.
        self.description = description
        # The device ID.
        self.device_tag = device_tag
        # The operating system of the device. Valid values:
        # 
        # - **Windows**: The Windows operating system.
        # 
        # - **macOS**: The macOS operating system.
        # 
        # - **Linux**: The Linux operating system.
        # 
        # - **Android**: The Android operating system.
        # 
        # - **iOS**: The iOS operating system.
        # 
        # - **Windows_Wuying**: Wuying Workspace.
        self.device_type = device_type
        # A list of full department paths.
        self.full_department = full_department
        # The hostname of the device.
        self.hostname = hostname
        # Specifies whether the excessive device registration application has been used. Valid values:
        # 
        # - **true**: The application has been used.
        # 
        # - **false**: The application has not been used.
        self.is_used = is_used
        # The MAC address of the device.
        self.mac = mac
        # The user ID.
        self.sase_user_id = sase_user_id
        # The status of the excessive device registration application. Valid values:
        # 
        # - **Pending**
        # 
        # - **Approved**
        # 
        # - **Rejected**
        self.status = status
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.department is not None:
            result['Department'] = self.department

        if self.description is not None:
            result['Description'] = self.description

        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.full_department is not None:
            result['FullDepartment'] = self.full_department

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.is_used is not None:
            result['IsUsed'] = self.is_used

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        if self.status is not None:
            result['Status'] = self.status

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('FullDepartment') is not None:
            self.full_department = m.get('FullDepartment')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('IsUsed') is not None:
            self.is_used = m.get('IsUsed')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

