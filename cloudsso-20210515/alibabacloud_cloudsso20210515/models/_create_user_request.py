# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class CreateUserRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        display_name: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        status: str = None,
        tags: List[main_models.CreateUserRequestTags] = None,
        user_name: str = None,
    ):
        # The description of the user.
        # 
        # Maximum length: 1024 characters.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The display name of the user.
        # 
        # Maximum length: 256 characters.
        self.display_name = display_name
        # The email address of the user. The email address must be unique within the directory.
        # 
        # Maximum length: 128 characters.
        self.email = email
        # The first name of the user.
        # 
        # Maximum length: 64 characters.
        self.first_name = first_name
        # The last name of the user.
        # 
        # Maximum length: 64 characters.
        self.last_name = last_name
        # The status of the user. Valid values:
        # 
        # - Enabled (default): Enabled.
        # - Disabled: Disabled.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The username. The username must be unique within the directory and cannot be modified.
        # 
        # Format: Can contain digits, letters, and the following special characters: `@_-.`
        # 
        # Maximum length: 64 characters.
        self.user_name = user_name

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateUserRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class CreateUserRequestTags(DaraModel):
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

