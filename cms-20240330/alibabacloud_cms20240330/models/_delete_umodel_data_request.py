# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUmodelDataRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        dry_run: bool = None,
        kind: str = None,
        name: str = None,
    ):
        # The name of the specific Umodel data. If you do not specify this parameter, all Umodel data is included.
        self.domain = domain
        # Specifies whether to perform a dry run of the request. Valid values:
        # - true: sends a check request and does not perform actual changes.
        # - false: sends a normal request.
        # Default value: false.
        self.dry_run = dry_run
        # The kind of the specific Umodel data. If you do not specify this parameter, all kinds are included.
        self.kind = kind
        # The name of the specific Umodel data. If you do not specify this parameter, all Umodel data is included.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['domain'] = self.domain

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.kind is not None:
            result['kind'] = self.kind

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

