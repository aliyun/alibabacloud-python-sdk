# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListParamsRequest(DaraModel):
    def __init__(
        self,
        encrypted: bool = None,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        scene_id: str = None,
    ):
        self.encrypted = encrypted
        self.environment = environment
        # This parameter is required.
        self.instance_id = instance_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

