# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckPushReceiverRequest(DaraModel):
    def __init__(
        self,
        receiver_account: str = None,
    ):
        # This parameter is required.
        self.receiver_account = receiver_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.receiver_account is not None:
            result['ReceiverAccount'] = self.receiver_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverAccount') is not None:
            self.receiver_account = m.get('ReceiverAccount')

        return self

