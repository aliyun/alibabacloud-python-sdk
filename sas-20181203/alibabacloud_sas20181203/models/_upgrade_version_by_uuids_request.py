# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpgradeVersionByUuidsRequest(DaraModel):
    def __init__(
        self,
        upgrade_version: str = None,
        uuid_list: List[str] = None,
    ):
        # The version to which you want to upgrade the client.
        # 
        # This parameter is required.
        self.upgrade_version = upgrade_version
        # The UUIDs of the assets on which you want to run the detection task.
        # 
        # This parameter is required.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

