# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublicTemplateStatusReason(DaraModel):
    def __init__(
        self,
        message: str = None,
        step: str = None,
    ):
        # The details of the failure reason.
        self.message = message
        # The identity of the failed step.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.step is not None:
            result['step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('step') is not None:
            self.step = m.get('step')

        return self

