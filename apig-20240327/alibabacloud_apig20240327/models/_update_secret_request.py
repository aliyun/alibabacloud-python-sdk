# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSecretRequest(DaraModel):
    def __init__(
        self,
        secret_data: str = None,
    ):
        self.secret_data = secret_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secret_data is not None:
            result['secretData'] = self.secret_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('secretData') is not None:
            self.secret_data = m.get('secretData')

        return self

