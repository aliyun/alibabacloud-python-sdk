# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateCapabilityRequest(DaraModel):
    def __init__(
        self,
        item_desc: str = None,
        item_name: str = None,
        item_value: Dict[str, Any] = None,
        dry_run: bool = None,
    ):
        # The configuration description.
        self.item_desc = item_desc
        # The configuration name.
        self.item_name = item_name
        # The configuration item.
        self.item_value = item_value
        # Specifies whether to check the validity of the request parameters without performing the actual operation. Default value: false.
        # 
        # Valid values:
        # 
        # - **true**
        # 
        # - **false**.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_desc is not None:
            result['itemDesc'] = self.item_desc

        if self.item_name is not None:
            result['itemName'] = self.item_name

        if self.item_value is not None:
            result['itemValue'] = self.item_value

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemDesc') is not None:
            self.item_desc = m.get('itemDesc')

        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')

        if m.get('itemValue') is not None:
            self.item_value = m.get('itemValue')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

