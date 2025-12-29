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
        # Specifies whether to check the validity of input parameters. Default value: false.
        # 
        # Valid values:
        # 
        # *   **true**: checks only the validity of input parameters.
        # *   **false**: checks the validity of input parameters and creates an attribution configuration.
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

