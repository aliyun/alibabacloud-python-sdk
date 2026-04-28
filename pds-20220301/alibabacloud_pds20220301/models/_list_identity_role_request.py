# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ListIdentityRoleRequest(DaraModel):
    def __init__(
        self,
        identity: main_models.Identity = None,
    ):
        # This parameter is required.
        self.identity = identity

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity is not None:
            result['identity'] = self.identity.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity') is not None:
            temp_model = main_models.Identity()
            self.identity = temp_model.from_map(m.get('identity'))

        return self

