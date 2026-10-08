# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckDomainSunriseClaimResponseBody(DaraModel):
    def __init__(
        self,
        claim_key: str = None,
        request_id: str = None,
        result: int = None,
    ):
        # The trademark keyword key provided by the TMDB database.
        self.claim_key = claim_key
        # Unique request access token.
        self.request_id = request_id
        # Result. Valid values:
        # - **0**: Not a trademark keyword or not in the claim domain lifecycle.
        # - **1**: In the sunrise domain lifecycle.
        # - **2**: In the claim domain lifecycle.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.claim_key is not None:
            result['ClaimKey'] = self.claim_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClaimKey') is not None:
            self.claim_key = m.get('ClaimKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

