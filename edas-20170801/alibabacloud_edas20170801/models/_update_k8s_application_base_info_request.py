# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateK8sApplicationBaseInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        description: str = None,
        email: str = None,
        owner: str = None,
        phone_number: str = None,
    ):
        # The ID of the application that you want to modify.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The description of the application. The description can be up to 256 characters in length.
        self.description = description
        # The email address of the application owner.
        self.email = email
        # The owner of the application. The value can be up to 128 characters in length.
        self.owner = owner
        # The phone number of the application owner.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.description is not None:
            result['Description'] = self.description

        if self.email is not None:
            result['Email'] = self.email

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        return self

