# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateUninstallApplicationsStatusResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.UpdateUninstallApplicationsStatusResponseBodyApplications] = None,
        request_id: str = None,
    ):
        self.applications = applications
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
                temp_model = main_models.UpdateUninstallApplicationsStatusResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateUninstallApplicationsStatusResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        create_time: str = None,
        department: str = None,
        dev_tag: str = None,
        dev_type: str = None,
        hostname: str = None,
        idp_name: str = None,
        is_uninstall: bool = None,
        mac: str = None,
        reason: str = None,
        sase_user_id: str = None,
        status: str = None,
        username: str = None,
    ):
        self.application_id = application_id
        self.create_time = create_time
        self.department = department
        self.dev_tag = dev_tag
        self.dev_type = dev_type
        self.hostname = hostname
        self.idp_name = idp_name
        self.is_uninstall = is_uninstall
        self.mac = mac
        self.reason = reason
        self.sase_user_id = sase_user_id
        self.status = status
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

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.idp_name is not None:
            result['IdpName'] = self.idp_name

        if self.is_uninstall is not None:
            result['IsUninstall'] = self.is_uninstall

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.reason is not None:
            result['Reason'] = self.reason

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

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('IdpName') is not None:
            self.idp_name = m.get('IdpName')

        if m.get('IsUninstall') is not None:
            self.is_uninstall = m.get('IsUninstall')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

