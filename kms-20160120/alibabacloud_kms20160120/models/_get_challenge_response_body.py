# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChallengeResponseBody(DaraModel):
    def __init__(
        self,
        challenge_token: str = None,
        nonce: str = None,
        request_id: str = None,
    ):
        self.challenge_token = challenge_token
        self.nonce = nonce
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.challenge_token is not None:
            result['ChallengeToken'] = self.challenge_token

        if self.nonce is not None:
            result['Nonce'] = self.nonce

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChallengeToken') is not None:
            self.challenge_token = m.get('ChallengeToken')

        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

