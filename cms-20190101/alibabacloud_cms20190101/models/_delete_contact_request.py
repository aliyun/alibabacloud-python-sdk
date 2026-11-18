# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContactRequest(DaraModel):
    def __init__(
        self,
        contact_name: str = None,
        dry_run: bool = None,
    ):
        # The name of the alert contact.
        # 
        # This parameter is required.
        self.contact_name = contact_name
        # Specifies whether to perform only a dry run for this request.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        return self

