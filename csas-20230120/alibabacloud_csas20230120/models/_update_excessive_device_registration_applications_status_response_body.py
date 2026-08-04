# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications] = None,
        request_id: str = None,
    ):
        # List of device registration applications that exceed your quota.
        self.applications = applications
        # ID of the request.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateExcessiveDeviceRegistrationApplicationsStatusResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        create_time: str = None,
        department: str = None,
        description: str = None,
        device_tag: str = None,
        device_type: str = None,
        hostname: str = None,
        is_used: bool = None,
        mac: str = None,
        sase_user_id: str = None,
        status: str = None,
        username: str = None,
    ):
        # ID of the device registration application.
        self.application_id = application_id
        # Time when the device registration application was created.
        self.create_time = create_time
        # Department to which the user belongs.
        self.department = department
        # This field indicates the reason for the excessive device registration request.
        self.description = description
        # ID of the endpoint device.
        self.device_tag = device_tag
        # Operating system of the endpoint device. Valid values:
        # 
        # - **Windows**: Windows operating system.
        # 
        # - **macOS**: macOS operating system.
        # 
        # - **Linux**: Linux operating system.
        # 
        # - **Android**: Android operating system.
        # 
        # - **iOS**: iOS operating system.
        # 
        # - **Windows_Wuying**: Alibaba Cloud Cloud Desktop operating system.
        self.device_type = device_type
        # Name of the endpoint device.
        self.hostname = hostname
        # Indicates whether the device registration application has been used. Valid values:
        # 
        # - **true**: Used.
        # 
        # - **false**: Not used.
        self.is_used = is_used
        # MAC address of the endpoint device.
        self.mac = mac
        # User ID.
        self.sase_user_id = sase_user_id
        # Status of the device registration application. Valid values:
        # 
        # - **Pending**: Pending review.
        # 
        # - **Approved**: Approved.
        # 
        # - **Rejected**: Rejected.
        self.status = status
        # Username.
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

