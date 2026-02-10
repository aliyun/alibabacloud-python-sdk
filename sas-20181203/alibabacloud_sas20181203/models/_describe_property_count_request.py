# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePropertyCountRequest(DaraModel):
    def __init__(
        self,
        type: str = None,
        uuid_list: str = None,
    ):
        # The type of the asset fingerprints. Separate multiple types with commas (,). Valid values:
        # 
        # *   **port**: port
        # *   **process**: process
        # *   **software**: software
        # *   **user**: account
        # *   **cron**: scheduled task
        # *   **sca**: middleware
        # *   **web**: website
        # *   **database**: database
        # *   **lkm**: kernel module
        # *   **autorun**: startup item
        # *   **web_server**: web service
        self.type = type
        # The UUIDs of the assets. Separate multiple UUIDs with commas (,).
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

