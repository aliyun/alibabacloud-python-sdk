# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyPhoneBusinessProfileRequest(DaraModel):
    def __init__(
        self,
        about: str = None,
        address: str = None,
        cust_space_id: str = None,
        description: str = None,
        email: str = None,
        owner_id: int = None,
        phone_number: str = None,
        profile_picture_url: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vertical: str = None,
        websites: List[str] = None,
    ):
        # The business information.
        self.about = about
        # The address.
        self.address = address
        # The space ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # This parameter is required.
        self.cust_space_id = cust_space_id
        # The description of the phone number.
        self.description = description
        # The email address.
        self.email = email
        self.owner_id = owner_id
        # The mobile phone number.
        # 
        # This parameter is required.
        self.phone_number = phone_number
        # The URL of the profile picture.
        self.profile_picture_url = profile_picture_url
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The industry.
        # 
        # >  Valid values: OTHER, AUTO, BEAUTY, APPAREL, EDU, ENTERTAIN, EVENT_PLAN, FINANCE, GROCERY, GOVT, HOTEL, HEALTH, NONPROFIT, PROF_SERVICES, RETAIL, TRAVEL, and RESTAURANT.
        self.vertical = vertical
        # The URLs of the websites.
        self.websites = websites

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.about is not None:
            result['About'] = self.about

        if self.address is not None:
            result['Address'] = self.address

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.description is not None:
            result['Description'] = self.description

        if self.email is not None:
            result['Email'] = self.email

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.vertical is not None:
            result['Vertical'] = self.vertical

        if self.websites is not None:
            result['Websites'] = self.websites

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')

        if m.get('Websites') is not None:
            self.websites = m.get('Websites')

        return self

