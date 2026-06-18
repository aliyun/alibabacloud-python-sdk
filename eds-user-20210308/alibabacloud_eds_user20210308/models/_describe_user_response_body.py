# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.DescribeUserResponseBodyUser = None,
    ):
        # Request ID.
        self.request_id = request_id
        # User information.
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user is not None:
            result['User'] = self.user.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('User') is not None:
            temp_model = main_models.DescribeUserResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class DescribeUserResponseBodyUser(DaraModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        external_info: main_models.DescribeUserResponseBodyUserExternalInfo = None,
        extras: Dict[str, str] = None,
        gmt_create: int = None,
        nick_name: str = None,
        org_ids: List[str] = None,
        org_paths: List[str] = None,
        phone: str = None,
        properties: List[main_models.DescribeUserResponseBodyUserProperties] = None,
        remark: str = None,
        status: int = None,
        wy_id: str = None,
    ):
        # Mailbox.
        self.email = email
        # Username.
        self.end_user_id = end_user_id
        # Associated external user information.
        self.external_info = external_info
        # Extension information.
        self.extras = extras
        # Creation Time.
        self.gmt_create = gmt_create
        self.nick_name = nick_name
        # List of organization IDs.
        self.org_ids = org_ids
        # List of organizations.
        self.org_paths = org_paths
        # Phone number.
        self.phone = phone
        # User attributes.
        self.properties = properties
        # Remarks.
        self.remark = remark
        # User status.
        self.status = status
        # Unique ID of the Wuying user.
        self.wy_id = wy_id

    def validate(self):
        if self.external_info:
            self.external_info.validate()
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info.to_map()

        if self.extras is not None:
            result['Extras'] = self.extras

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.org_ids is not None:
            result['OrgIds'] = self.org_ids

        if self.org_paths is not None:
            result['OrgPaths'] = self.org_paths

        if self.phone is not None:
            result['Phone'] = self.phone

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.status is not None:
            result['Status'] = self.status

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExternalInfo') is not None:
            temp_model = main_models.DescribeUserResponseBodyUserExternalInfo()
            self.external_info = temp_model.from_map(m.get('ExternalInfo'))

        if m.get('Extras') is not None:
            self.extras = m.get('Extras')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('OrgIds') is not None:
            self.org_ids = m.get('OrgIds')

        if m.get('OrgPaths') is not None:
            self.org_paths = m.get('OrgPaths')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.DescribeUserResponseBodyUserProperties()
                self.properties.append(temp_model.from_map(k1))

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

class DescribeUserResponseBodyUserProperties(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Attribute key.
        self.key = key
        # Attribute value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeUserResponseBodyUserExternalInfo(DaraModel):
    def __init__(
        self,
        external_id: str = None,
        external_name: str = None,
        job_number: str = None,
        sso_type: str = None,
    ):
        # External User ID.
        self.external_id = external_id
        # External information name.
        self.external_name = external_name
        # Employee ID.
        self.job_number = job_number
        # SSO logon type.
        self.sso_type = sso_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_id is not None:
            result['ExternalId'] = self.external_id

        if self.external_name is not None:
            result['ExternalName'] = self.external_name

        if self.job_number is not None:
            result['JobNumber'] = self.job_number

        if self.sso_type is not None:
            result['SsoType'] = self.sso_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')

        if m.get('ExternalName') is not None:
            self.external_name = m.get('ExternalName')

        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')

        if m.get('SsoType') is not None:
            self.sso_type = m.get('SsoType')

        return self

