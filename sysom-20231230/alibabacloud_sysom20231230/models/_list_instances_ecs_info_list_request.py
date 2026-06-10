# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstancesEcsInfoListRequest(DaraModel):
    def __init__(
        self,
        info_type: str = None,
        instance_id: str = None,
        managed_type: str = None,
        plugin_id: str = None,
        region: str = None,
    ):
        # Type of information to retrieve
        # 
        # This parameter is required.
        self.info_type = info_type
        # If this field is specified, the response filters and returns the Agent installation status for the specified instance.
        self.instance_id = instance_id
        # Management status of the instance
        self.managed_type = managed_type
        # If this parameter is specified, the response filters and returns the instance information list for the corresponding widget.
        self.plugin_id = plugin_id
        # Filter instances by area
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_type is not None:
            result['info_type'] = self.info_type

        if self.instance_id is not None:
            result['instance_id'] = self.instance_id

        if self.managed_type is not None:
            result['managed_type'] = self.managed_type

        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('info_type') is not None:
            self.info_type = m.get('info_type')

        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')

        if m.get('managed_type') is not None:
            self.managed_type = m.get('managed_type')

        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

