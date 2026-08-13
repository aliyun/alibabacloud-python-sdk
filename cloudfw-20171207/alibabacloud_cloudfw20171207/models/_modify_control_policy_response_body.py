# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyControlPolicyResponseBody(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        request_id: str = None,
    ):
        # Indicates whether this is a successful dry run response. A value of true indicates that only the dry run was completed and no actual modification was performed.
        self.dry_run = dry_run
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

