# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppSupabaseSecretRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        secret_key: str = None,
        secret_name: str = None,
        secret_type: str = None,
        secret_value: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Key value
        self.secret_key = secret_key
        # Key name
        self.secret_name = secret_name
        # Key Type
        self.secret_type = secret_type
        # Key Value
        self.secret_value = secret_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.secret_type is not None:
            result['SecretType'] = self.secret_type

        if self.secret_value is not None:
            result['SecretValue'] = self.secret_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')

        if m.get('SecretValue') is not None:
            self.secret_value = m.get('SecretValue')

        return self

