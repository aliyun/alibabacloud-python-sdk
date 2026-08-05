# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateConfigRequest(DaraModel):
    def __init__(
        self,
        config_data: Dict[str, Any] = None,
        dry_run: bool = None,
    ):
        # The configuration content.
        self.config_data = config_data
        # Specifies whether this is a dry run request.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_data is not None:
            result['configData'] = self.config_data

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configData') is not None:
            self.config_data = m.get('configData')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

