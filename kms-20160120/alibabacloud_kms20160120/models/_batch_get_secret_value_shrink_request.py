# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetSecretValueShrinkRequest(DaraModel):
    def __init__(
        self,
        secrets_list_shrink: str = None,
    ):
        # The list of secret information. You can query up to 20 different secrets at a time.
        self.secrets_list_shrink = secrets_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secrets_list_shrink is not None:
            result['SecretsList'] = self.secrets_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretsList') is not None:
            self.secrets_list_shrink = m.get('SecretsList')

        return self

