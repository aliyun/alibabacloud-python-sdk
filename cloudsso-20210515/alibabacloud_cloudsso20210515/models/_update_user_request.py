# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        new_description: str = None,
        new_display_name: str = None,
        new_email: str = None,
        new_first_name: str = None,
        new_last_name: str = None,
        user_id: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The new description of the user.
        self.new_description = new_description
        # The new display name of the user.
        self.new_display_name = new_display_name
        # The new email address of the user.
        self.new_email = new_email
        # The new first name of the user.
        self.new_first_name = new_first_name
        # The new last name of the user.
        self.new_last_name = new_last_name
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.new_description is not None:
            result['NewDescription'] = self.new_description

        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name

        if self.new_email is not None:
            result['NewEmail'] = self.new_email

        if self.new_first_name is not None:
            result['NewFirstName'] = self.new_first_name

        if self.new_last_name is not None:
            result['NewLastName'] = self.new_last_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')

        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')

        if m.get('NewEmail') is not None:
            self.new_email = m.get('NewEmail')

        if m.get('NewFirstName') is not None:
            self.new_first_name = m.get('NewFirstName')

        if m.get('NewLastName') is not None:
            self.new_last_name = m.get('NewLastName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

