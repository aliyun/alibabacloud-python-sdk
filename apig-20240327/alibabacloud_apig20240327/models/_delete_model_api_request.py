# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteModelApiRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
    ):
        # The idempotency token. Using the original clientToken for the same tenant, model API, and parameters allows you to retry the deletion if a background deletion fails. A conflict is returned if an active operation is still in progress or if the configuration has been replaced by a newer operation. A replay of a fully completed deletion returns a successful response with empty content, but using the same token for a different target is still rejected.
        self.client_token = client_token
        # Specifies whether to perform only a dry run. If you set this parameter to true, the system performs the same synchronous validation checks as a real deletion, but does not create a deletion execution or idempotent record, stop the service, or delete the API or associated configurations. If you set this parameter to false or leave it empty, the actual deletion is accepted.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

