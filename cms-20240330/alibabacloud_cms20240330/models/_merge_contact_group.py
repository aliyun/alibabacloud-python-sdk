# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class MergeContactGroup(DaraModel):
    def __init__(
        self,
        contacts: List[str] = None,
        extend: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        identifier: str = None,
        name: str = None,
        source: str = None,
    ):
        self.contacts = contacts
        self.extend = extend
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.identifier = identifier
        self.name = name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contacts is not None:
            result['contacts'] = self.contacts

        if self.extend is not None:
            result['extend'] = self.extend

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')

        if m.get('extend') is not None:
            self.extend = m.get('extend')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

