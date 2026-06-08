# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyResourceAccessPermissionShrinkRequest(DaraModel):
    def __init__(
        self,
        apply_contents_shrink: str = None,
        client_token: str = None,
        reason: str = None,
    ):
        # This parameter is required.
        self.apply_contents_shrink = apply_contents_shrink
        self.client_token = client_token
        # This parameter is required.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_contents_shrink is not None:
            result['ApplyContents'] = self.apply_contents_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyContents') is not None:
            self.apply_contents_shrink = m.get('ApplyContents')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

