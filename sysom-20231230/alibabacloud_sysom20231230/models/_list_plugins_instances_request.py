# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPluginsInstancesRequest(DaraModel):
    def __init__(
        self,
        current: int = None,
        instance_id_name: str = None,
        instance_tag: str = None,
        operation_type: str = None,
        page_size: int = None,
        plugin_id: str = None,
        region: str = None,
    ):
        # The current page number. This field is present when pagination is used.
        self.current = current
        # Filters instances by instance ID or instance name. Fuzzy match is supported.
        self.instance_id_name = instance_id_name
        # Filters instances by instance tag.
        self.instance_tag = instance_tag
        # Filters instances by plug-in installation status.
        # 
        # This parameter is required.
        self.operation_type = operation_type
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # Filters the instance list by the specified agent. If this parameter is specified, only instances associated with the specified agent are returned.
        # 
        # This parameter is required.
        self.plugin_id = plugin_id
        # Filters instances by region.
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
        if self.current is not None:
            result['current'] = self.current

        if self.instance_id_name is not None:
            result['instance_id_name'] = self.instance_id_name

        if self.instance_tag is not None:
            result['instance_tag'] = self.instance_tag

        if self.operation_type is not None:
            result['operation_type'] = self.operation_type

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id

        if self.region is not None:
            result['region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('instance_id_name') is not None:
            self.instance_id_name = m.get('instance_id_name')

        if m.get('instance_tag') is not None:
            self.instance_tag = m.get('instance_tag')

        if m.get('operation_type') is not None:
            self.operation_type = m.get('operation_type')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')

        if m.get('region') is not None:
            self.region = m.get('region')

        return self

