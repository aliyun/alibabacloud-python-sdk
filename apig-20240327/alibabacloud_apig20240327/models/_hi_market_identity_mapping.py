# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HiMarketIdentityMapping(DaraModel):
    def __init__(
        self,
        email_field: str = None,
        user_id_field: str = None,
        user_name_field: str = None,
    ):
        self.email_field = email_field
        self.user_id_field = user_id_field
        self.user_name_field = user_name_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email_field is not None:
            result['emailField'] = self.email_field

        if self.user_id_field is not None:
            result['userIdField'] = self.user_id_field

        if self.user_name_field is not None:
            result['userNameField'] = self.user_name_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('emailField') is not None:
            self.email_field = m.get('emailField')

        if m.get('userIdField') is not None:
            self.user_id_field = m.get('userIdField')

        if m.get('userNameField') is not None:
            self.user_name_field = m.get('userNameField')

        return self

