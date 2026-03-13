# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExternalUserAddShrinkRequest(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        cert_request_list_shrink: str = None,
        email: str = None,
        external_user_id: str = None,
        phone: str = None,
        real_name: str = None,
        real_name_en: str = None,
        user_type: int = None,
    ):
        self.birthday = birthday
        self.cert_request_list_shrink = cert_request_list_shrink
        self.email = email
        # This parameter is required.
        self.external_user_id = external_user_id
        self.phone = phone
        self.real_name = real_name
        self.real_name_en = real_name_en
        # This parameter is required.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.cert_request_list_shrink is not None:
            result['cert_request_list'] = self.cert_request_list_shrink

        if self.email is not None:
            result['email'] = self.email

        if self.external_user_id is not None:
            result['external_user_id'] = self.external_user_id

        if self.phone is not None:
            result['phone'] = self.phone

        if self.real_name is not None:
            result['real_name'] = self.real_name

        if self.real_name_en is not None:
            result['real_name_en'] = self.real_name_en

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('cert_request_list') is not None:
            self.cert_request_list_shrink = m.get('cert_request_list')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('external_user_id') is not None:
            self.external_user_id = m.get('external_user_id')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('real_name') is not None:
            self.real_name = m.get('real_name')

        if m.get('real_name_en') is not None:
            self.real_name_en = m.get('real_name_en')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

