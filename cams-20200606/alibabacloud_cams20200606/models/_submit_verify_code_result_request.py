# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVerifyCodeResultRequest(DaraModel):
    def __init__(
        self,
        message_id: str = None,
        result: bool = None,
        to: str = None,
    ):
        # The message ID.
        # 
        # This parameter is required.
        self.message_id = message_id
        # The verification result.
        # 
        # This parameter is required.
        self.result = result
        # The recipient number.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.result is not None:
            result['Result'] = self.result

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

