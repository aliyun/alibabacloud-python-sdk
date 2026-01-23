# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNamespaceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespace name.
        self.namespace_name = namespace_name
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`
        # *   `DELETING`
        self.namespace_status = namespace_status
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name

        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')

        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

