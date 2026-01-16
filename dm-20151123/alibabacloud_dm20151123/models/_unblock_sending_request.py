# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnblockSendingRequest(DaraModel):
    def __init__(
        self,
        block_email: str = None,
        block_type: str = None,
        sender_email: str = None,
    ):
        # Blacklisted recipient\\"s email address
        # 
        # This parameter is required.
        self.block_email = block_email
        # Blacklist type
        # - UNSUB: Unsubscribe
        # - REPORT: Report
        # 
        # This parameter is required.
        self.block_type = block_type
        # Sender\\"s email address
        # 
        # This parameter is required.
        self.sender_email = sender_email

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_email is not None:
            result['BlockEmail'] = self.block_email

        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.sender_email is not None:
            result['SenderEmail'] = self.sender_email

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockEmail') is not None:
            self.block_email = m.get('BlockEmail')

        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('SenderEmail') is not None:
            self.sender_email = m.get('SenderEmail')

        return self

