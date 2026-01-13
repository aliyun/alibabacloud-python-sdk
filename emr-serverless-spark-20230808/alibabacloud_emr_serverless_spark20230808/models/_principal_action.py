# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrincipalAction(DaraModel):
    def __init__(
        self,
        action_arn: str = None,
        principal_arn: str = None,
    ):
        self.action_arn = action_arn
        self.principal_arn = principal_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_arn is not None:
            result['actionArn'] = self.action_arn

        if self.principal_arn is not None:
            result['principalArn'] = self.principal_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionArn') is not None:
            self.action_arn = m.get('actionArn')

        if m.get('principalArn') is not None:
            self.principal_arn = m.get('principalArn')

        return self

