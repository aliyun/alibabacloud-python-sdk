# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class UpsertUmodelDataRequest(DaraModel):
    def __init__(
        self,
        elements: List[Any] = None,
        dry_run: bool = None,
        method: str = None,
    ):
        # The content of the elements.
        self.elements = elements
        # Specifies whether to perform a dry run for this request. Valid values:
        # - true: sends a check request without performing actual changes.
        # - false: sends a normal request.
        # Default value: false.
        self.dry_run = dry_run
        # The method.
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elements is not None:
            result['elements'] = self.elements

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.method is not None:
            result['method'] = self.method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elements') is not None:
            self.elements = m.get('elements')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('method') is not None:
            self.method = m.get('method')

        return self

