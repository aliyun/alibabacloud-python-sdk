# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEngineConfigsRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        scene_id: str = None,
        status: str = None,
        version: str = None,
    ):
        # The runtime environment. Valid values:
        # 
        # - Daily: Daily environment.
        # 
        # - Pre: Pre-release environment.
        # 
        # - Prod: Production environment.
        self.environment = environment
        # The instance ID. You can obtain the instance ID by calling the [ListInstances](https://help.aliyun.com/document_detail/2411819.html) operation.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The engine configuration name.
        self.name = name
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The scene ID.
        self.scene_id = scene_id
        # The status filter. Valid values:
        # 
        # - Released: Released.
        # 
        # - Unreleased: Not released.
        self.status = status
        # The version filter. Valid values:
        # 
        # latest: the most recently updated version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

