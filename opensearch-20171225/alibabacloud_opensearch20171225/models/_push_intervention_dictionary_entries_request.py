# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class PushInterventionDictionaryEntriesRequest(DaraModel):
    def __init__(
        self,
        body: List[Dict[str, Any]] = None,
        dry_run: bool = None,
    ):
        # The request body.
        self.body = body
        # Specifies whether to validate the request parameters without creating the attribution configuration. The default value is false.
        # 
        # Valid values:
        # 
        # - **true**: Validates the request parameters only.
        # 
        # - **false**: Validates the request parameters and creates the attribution configuration.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

