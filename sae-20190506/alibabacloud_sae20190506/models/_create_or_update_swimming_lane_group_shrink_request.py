# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        app_ids_shrink: str = None,
        entry_app_id: str = None,
        entry_app_type: str = None,
        group_id: int = None,
        group_name: str = None,
        namespace_id: str = None,
        swim_version: str = None,
    ):
        # The ID of the baseline application.
        self.app_ids_shrink = app_ids_shrink
        # The unique ID of the corresponding gateway.
        self.entry_app_id = entry_app_id
        # The application entry type (gateway type).
        # 
        # *   **apig:** cloud-native API Gateway
        # *   **mse:** Java Services Gateway
        # *   **mse-gw:** MSE cloud-native Gateway
        self.entry_app_type = entry_app_type
        # The ID of the lane group. This is required when you update a lane group.
        self.group_id = group_id
        # The name of the lane group.
        self.group_name = group_name
        # The ID of a namespace.
        self.namespace_id = namespace_id
        # The end-to-end grayscale version. Valid values: 0 and 2 (recommended).
        self.swim_version = swim_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_ids_shrink is not None:
            result['AppIds'] = self.app_ids_shrink

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
            self.app_ids_shrink = m.get('AppIds')

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

