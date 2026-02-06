# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveAppResourceRequest(DaraModel):
    def __init__(
        self,
        resource_ids: str = None,
        resource_type: str = None,
        target_app_id: str = None,
    ):
        # The resource ID. You can specify a maximum of 20 IDs at a time. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The resource type. Valid values:
        # 
        # *   **video**: video files.
        # *   **image**: image files.
        # *   **attached**: auxiliary media assets.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The ID of the application to which resources are migrated. Default value: **app-1000000**. For more information, see [Use the multi-application service](https://help.aliyun.com/document_detail/113600.html).
        # 
        # This parameter is required.
        self.target_app_id = target_app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.target_app_id is not None:
            result['TargetAppId'] = self.target_app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TargetAppId') is not None:
            self.target_app_id = m.get('TargetAppId')

        return self

