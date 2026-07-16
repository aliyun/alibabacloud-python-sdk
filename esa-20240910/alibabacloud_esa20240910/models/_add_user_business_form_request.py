# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserBusinessFormRequest(DaraModel):
    def __init__(
        self,
        company: str = None,
        email: str = None,
        phone_number: str = None,
        position: str = None,
        remark: str = None,
        user_name: str = None,
        website: str = None,
    ):
        # The company.
        # 
        # This parameter is required.
        self.company = company
        # The email address.
        # 
        # This parameter is required.
        self.email = email
        # The phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The job title.
        # 
        # This parameter is required.
        self.position = position
        # Additional remarks.
        self.remark = remark
        # The username.
        # 
        # This parameter is required.
        self.user_name = user_name
        # The company website.
        self.website = website

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company is not None:
            result['Company'] = self.company

        if self.email is not None:
            result['Email'] = self.email

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.position is not None:
            result['Position'] = self.position

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.website is not None:
            result['Website'] = self.website

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Company') is not None:
            self.company = m.get('Company')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Website') is not None:
            self.website = m.get('Website')

        return self

