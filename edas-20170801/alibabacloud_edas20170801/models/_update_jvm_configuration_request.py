# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateJvmConfigurationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        group_id: str = None,
        max_heap_size: int = None,
        max_perm_size: int = None,
        min_heap_size: int = None,
        options: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the instance group where the application is deployed. You can call the ListDeployGroup operation to query the group ID. For more information, see [ListDeployGroup](https://help.aliyun.com/document_detail/62077.html).
        # 
        # >
        # 
        # - To configure the JVM parameters for an instance group, set this parameter to a specific ID.
        # 
        # - To configure the JVM parameters for an application, leave this parameter empty.
        self.group_id = group_id
        # The maximum size of the heap memory. Unit: MB.
        # 
        # >
        # 
        # - If this parameter is not specified in the group configuration, the value specified in the application configuration is used.
        # 
        # - If this parameter is not specified in the application configuration, the default value is used.
        self.max_heap_size = max_heap_size
        # The size of the permanent generation heap memory. Unit: MB.
        # 
        # >
        # 
        # - If this parameter is not specified in the group configuration, the value specified in the application configuration is used.
        # 
        # - If this parameter is not specified in the application configuration, the default value is used.
        self.max_perm_size = max_perm_size
        # The initial size of the heap memory. Unit: MB.
        # 
        # >
        # 
        # - If this parameter is not specified in the group configuration, the value specified in the application configuration is used.
        # 
        # - If this parameter is not specified in the application configuration, the default value is used.
        self.min_heap_size = min_heap_size
        # The custom JVM parameters.
        # 
        # >
        # 
        # - If this parameter is not specified in the group configuration, the value specified in the application configuration is used.
        # 
        # - If this parameter is not specified in the application configuration, the default value is used.
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_heap_size is not None:
            result['MaxHeapSize'] = self.max_heap_size

        if self.max_perm_size is not None:
            result['MaxPermSize'] = self.max_perm_size

        if self.min_heap_size is not None:
            result['MinHeapSize'] = self.min_heap_size

        if self.options is not None:
            result['Options'] = self.options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxHeapSize') is not None:
            self.max_heap_size = m.get('MaxHeapSize')

        if m.get('MaxPermSize') is not None:
            self.max_perm_size = m.get('MaxPermSize')

        if m.get('MinHeapSize') is not None:
            self.min_heap_size = m.get('MinHeapSize')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        return self

