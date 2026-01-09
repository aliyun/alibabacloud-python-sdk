# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MobileRecycledMetaVerifyRequest(DaraModel):
    def __init__(
        self,
        mobile: str = None,
        param_type: str = None,
        register_date: str = None,
    ):
        # This parameter is required.
        self.mobile = mobile
        # This parameter is required.
        self.param_type = param_type
        # This parameter is required.
        self.register_date = register_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.register_date is not None:
            result['RegisterDate'] = self.register_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('RegisterDate') is not None:
            self.register_date = m.get('RegisterDate')

        return self

