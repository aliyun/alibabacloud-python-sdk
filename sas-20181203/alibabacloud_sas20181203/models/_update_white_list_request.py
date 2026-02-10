# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateWhiteListRequest(DaraModel):
    def __init__(
        self,
        registry_id: int = None,
        white_list: str = None,
    ):
        # The ID of the image repository.
        # 
        # >  You can call the [PageImageRegistry](~~PageImageRegistry~~) operation to obtain the ID.
        # 
        # This parameter is required.
        self.registry_id = registry_id
        # The IP address whitelist. Separate multiple IP addresses with commas (,).
        # 
        # This parameter is required.
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registry_id is not None:
            result['RegistryId'] = self.registry_id

        if self.white_list is not None:
            result['WhiteList'] = self.white_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistryId') is not None:
            self.registry_id = m.get('RegistryId')

        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')

        return self

