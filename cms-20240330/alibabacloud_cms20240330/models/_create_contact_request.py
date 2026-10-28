# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateContactRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        email: str = None,
        im_user_ids: Dict[str, str] = None,
        lang: str = None,
        name: str = None,
        phone: str = None,
        workspace: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The email address.
        self.email = email
        # The instant messaging (IM) user ID mapping, which supports multi-platform integration. The key is the IM type (such as DING or WEIXIN), and the value is the corresponding user ID.
        self.im_user_ids = im_user_ids
        # The language.
        self.lang = lang
        # The name of the contact.
        self.name = name
        # The mobile phone number. Currently, only mobile phone numbers in the Chinese mainland are supported.
        self.phone = phone
        # The name of the workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        if self.email is not None:
            result['email'] = self.email

        if self.im_user_ids is not None:
            result['imUserIds'] = self.im_user_ids

        if self.lang is not None:
            result['lang'] = self.lang

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('imUserIds') is not None:
            self.im_user_ids = m.get('imUserIds')

        if m.get('lang') is not None:
            self.lang = m.get('lang')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

