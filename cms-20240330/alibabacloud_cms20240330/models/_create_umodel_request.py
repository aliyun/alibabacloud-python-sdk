# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUmodelRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        dry_run: bool = None,
    ):
        # The description of the Umodel.
        self.description = description
        # Specifies whether to perform a dry run on the request. Valid values:
        # - true: performs a dry run. The system checks the request but does not make actual changes.
        # - false: sends a normal request.
        # Default value: false.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

