# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class ListK8sConfigMapsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        condition: Dict[str, Any] = None,
        namespace: str = None,
        page_no: int = None,
        page_size: int = None,
        region_id: str = None,
        show_related_apps: bool = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The filter conditions. Set this parameter to a JSON string in the format of {"field":"Name", "pattern":"configmap-"}.
        self.condition = condition
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace
        # The number of the page to return. Pages start from Page 0.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the region.
        self.region_id = region_id
        # Specifies whether to return a list of applications that use a ConfigMap. Valid values: true and false.
        self.show_related_apps = show_related_apps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.condition is not None:
            result['Condition'] = self.condition

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_related_apps is not None:
            result['ShowRelatedApps'] = self.show_related_apps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowRelatedApps') is not None:
            self.show_related_apps = m.get('ShowRelatedApps')

        return self

