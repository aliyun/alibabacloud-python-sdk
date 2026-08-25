# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user: main_models.GetUserResponseBodyUser = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The user information.
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
            temp_model = main_models.GetUserResponseBodyUser()
            self.user = temp_model.from_map(m.get('User'))

        return self

class GetUserResponseBodyUser(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        email: str = None,
        external_id: main_models.GetUserResponseBodyUserExternalId = None,
        first_name: str = None,
        last_name: str = None,
        provision_type: str = None,
        status: str = None,
        tags: List[main_models.GetUserResponseBodyUserTags] = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The time when the user was created (in UTC).
        self.create_time = create_time
        # The description of the user.
        self.description = description
        # The display name of the user.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The user identifier information of the external identity provider.
        self.external_id = external_id
        # The first name of the user.
        self.first_name = first_name
        # The last name of the user.
        self.last_name = last_name
        # The type of the user. Valid values:
        # 
        # - Manual: Manually created.
        # - Synchronized: Synchronized from an external identity provider.
        self.provision_type = provision_type
        # The status of the user. Valid values:
        # 
        # - Enabled: Enabled.
        # - Disabled: Disabled.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The time when the user was last modified (in UTC).
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id
        # The username of the user.
        self.user_name = user_name

    def validate(self):
        if self.external_id:
            self.external_id.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.external_id is not None:
            result['ExternalId'] = self.external_id.to_map()

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.provision_type is not None:
            result['ProvisionType'] = self.provision_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ExternalId') is not None:
            temp_model = main_models.GetUserResponseBodyUserExternalId()
            self.external_id = temp_model.from_map(m.get('ExternalId'))

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('ProvisionType') is not None:
            self.provision_type = m.get('ProvisionType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetUserResponseBodyUserTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class GetUserResponseBodyUserTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class GetUserResponseBodyUserExternalId(DaraModel):
    def __init__(
        self,
        id: str = None,
        issuer: str = None,
    ):
        # The user identifier of the external identity provider.
        self.id = id
        # The external identity synchronization channel. Currently, only SCIM synchronization is supported.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        return self

