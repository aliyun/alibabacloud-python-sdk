# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DryRunViolation(DaraModel):
    def __init__(
        self,
        field: str = None,
        message: str = None,
        suggestion: str = None,
    ):
        # The path of the violated field, such as schedule.intervalSecs.
        self.field = field
        # The violation description.
        self.message = message
        # The remediation suggestion.
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field

        if self.message is not None:
            result['message'] = self.message

        if self.suggestion is not None:
            result['suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')

        return self

