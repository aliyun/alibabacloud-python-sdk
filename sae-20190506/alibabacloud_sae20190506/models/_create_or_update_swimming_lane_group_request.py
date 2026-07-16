# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneGroupRequest(DaraModel):
    def __init__(
        self,
        app_ids: List[str] = None,
        entry_app_id: str = None,
        entry_app_type: str = None,
        group_id: int = None,
        group_name: str = None,
        namespace_id: str = None,
        swim_version: str = None,
    ):
        # The IDs of the baseline applications.
        self.app_ids = app_ids
        # The unique ID of the gateway.
        self.entry_app_id = entry_app_id
        # The type of the gateway that acts as the application\\"s entry point.
        # 
        # - **apig:** cloud-native API gateway
        # 
        # - **mse:** java service gateway
        # 
        # - **mse-gw:** MSE Cloud Native Gateway
        self.entry_app_type = entry_app_type
        # The ID of the swimming lane group. This parameter is required when you update a swimming lane group.
        self.group_id = group_id
        # The name of the swimming lane group.
        self.group_name = group_name
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The version of the end-to-end canary release. Valid values: 0 and 2. The value 2 is recommended.
        self.swim_version = swim_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.entry_app_id is not None:
            result['EntryAppId'] = self.entry_app_id

        if self.entry_app_type is not None:
            result['EntryAppType'] = self.entry_app_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.swim_version is not None:
            result['SwimVersion'] = self.swim_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('EntryAppId') is not None:
            self.entry_app_id = m.get('EntryAppId')

        if m.get('EntryAppType') is not None:
            self.entry_app_type = m.get('EntryAppType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SwimVersion') is not None:
            self.swim_version = m.get('SwimVersion')

        return self

