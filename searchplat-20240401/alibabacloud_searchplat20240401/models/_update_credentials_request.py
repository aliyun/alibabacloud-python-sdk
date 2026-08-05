# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCredentialsRequest(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        dry_run: bool = None,
    ):
        # Specifies whether the credential is enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.enabled = enabled
        # Specifies whether to perform a dry run.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

