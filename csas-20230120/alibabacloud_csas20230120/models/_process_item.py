# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProcessItem(DaraModel):
    def __init__(
        self,
        bundle_id: str = None,
        dev_type: str = None,
        directory: str = None,
        process: str = None,
    ):
        self.bundle_id = bundle_id
        self.dev_type = dev_type
        self.directory = directory
        self.process = process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.dev_type is not None:
            result['DevType'] = self.dev_type

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.process is not None:
            result['Process'] = self.process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('DevType') is not None:
            self.dev_type = m.get('DevType')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        return self

