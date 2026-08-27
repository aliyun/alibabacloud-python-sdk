# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SaveGroupOutputFileToPersonalResourceRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        group_id: str = None,
        item_ids: List[str] = None,
        mode: str = None,
        tenant_id: str = None,
    ):
        # The enterprise knowledge base directory ID.
        self.directory_id = directory_id
        # The project group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # itemIds
        # 
        # This parameter is required.
        self.item_ids = item_ids
        # The save mode. Valid values:
        # - link: creates a link (1:1 idempotent, editing the output synchronizes the resource).
        # - copy: creates a copy (unlimited times, snapshot).
        # 
        # This parameter is required.
        self.mode = mode
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.item_ids is not None:
            result['itemIds'] = self.item_ids

        if self.mode is not None:
            result['mode'] = self.mode

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('itemIds') is not None:
            self.item_ids = m.get('itemIds')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

