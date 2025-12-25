# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncInstanceMetaRequest(DaraModel):
    def __init__(
        self,
        ignore_table: bool = None,
        instance_id: str = None,
        tid: int = None,
    ):
        # Specifies whether to skip synchronization for the metadata of table dictionaries. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ignore_table = ignore_table
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the Manage DMS tenants topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_table is not None:
            result['IgnoreTable'] = self.ignore_table

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreTable') is not None:
            self.ignore_table = m.get('IgnoreTable')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

