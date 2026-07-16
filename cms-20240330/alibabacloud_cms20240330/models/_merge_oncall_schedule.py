# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class MergeOncallSchedule(DaraModel):
    def __init__(
        self,
        detail: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        identifier: str = None,
        name: str = None,
        source: str = None,
        workspace: str = None,
    ):
        # Details of the on-call schedule.
        self.detail = detail
        # The UTC time when the on-call schedule was created.
        self.gmt_create = gmt_create
        # The UTC time when the on-call schedule was last modified.
        self.gmt_modified = gmt_modified
        # The unique identifier of the on-call schedule.
        self.identifier = identifier
        # The name of the on-call schedule.
        self.name = name
        # The creation source of the on-call schedule.
        self.source = source
        # The workspace that the on-call schedule belongs to.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['detail'] = self.detail

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

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')

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

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

