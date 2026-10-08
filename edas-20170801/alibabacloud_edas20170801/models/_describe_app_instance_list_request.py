# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppInstanceListRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        with_node_info: bool = None,
    ):
        # The ID of the application. You can call the ListApplication operation to query the ID of the application. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to return the information about the node in which the pod resides.
        # 
        # - `true`: returns the information about the node in which the pod resides
        # 
        # - `false`: does not return the information about the node in which the pod resides
        self.with_node_info = with_node_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.with_node_info is not None:
            result['WithNodeInfo'] = self.with_node_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('WithNodeInfo') is not None:
            self.with_node_info = m.get('WithNodeInfo')

        return self

