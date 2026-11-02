# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DecodeDiagnosticMessageRequest(DaraModel):
    def __init__(
        self,
        encoded_diagnostic_message: str = None,
    ):
        # The encoded diagnostic information obtained from the `AccessDeniedDetail.EncodedDiagnosticMessage` field in the response body when an API request is denied due to insufficient permissions. This parameter is used to decode the access denied diagnostic information and is required when you call this operation.
        self.encoded_diagnostic_message = encoded_diagnostic_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        return self

