# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableAutoGroupCreationRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Specify whether to enable the flexible group creation feature. Valid values:
        # 
        # *   **true**: enables the flexible group creation feature.
        # *   **false**: disabled the flexible group creation feature.
        # 
        # This parameter is required.
        self.enable = enable
        # The instance ID.
        # 
        # You can call the [GetInstanceList](https://help.aliyun.com/document_detail/437663.html) operation to query instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

