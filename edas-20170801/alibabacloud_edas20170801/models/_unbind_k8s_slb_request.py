# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindK8sSlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cluster_id: str = None,
        slb_name: str = None,
        type: str = None,
    ):
        # The ID of the application. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/149390.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the cluster. You can call the GetK8sCluster operation to query the cluster ID. For more information, see [GetK8sCluster](https://help.aliyun.com/document_detail/181437.html).
        self.cluster_id = cluster_id
        # The name of the SLB instance.
        self.slb_name = slb_name
        # The type of the SLB instance. Valid values:
        # 
        # - **internet**: Internet-facing SLB instance
        # 
        # - **intranet**: internal-facing SLB instance
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.slb_name is not None:
            result['SlbName'] = self.slb_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

