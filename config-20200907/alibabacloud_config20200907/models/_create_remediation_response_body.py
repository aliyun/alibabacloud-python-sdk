# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRemediationResponseBody(DaraModel):
    def __init__(
        self,
        remediation_id: str = None,
        request_id: str = None,
    ):
        # The ID of the remediation template.
        self.remediation_id = remediation_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

