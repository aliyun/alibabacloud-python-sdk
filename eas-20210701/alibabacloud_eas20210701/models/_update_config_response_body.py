# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConfigResponseBody(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        key: str = None,
        updated_at: str = None,
        value: str = None,
    ):
        # The time the configuration was created.
        self.created_at = created_at
        # The dynamic parameter name.
        self.key = key
        # The time the configuration was last updated.
        self.updated_at = updated_at
        # The dynamic parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.key is not None:
            result['Key'] = self.key

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

