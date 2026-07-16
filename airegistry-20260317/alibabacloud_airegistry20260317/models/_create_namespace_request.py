# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNamespaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        scan_policy: str = None,
        tags: str = None,
    ):
        self.description = description
        self.name = name
        self.scan_policy = scan_policy
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.scan_policy is not None:
            result['ScanPolicy'] = self.scan_policy

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ScanPolicy') is not None:
            self.scan_policy = m.get('ScanPolicy')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

