# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPodRiskRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        current_page: int = None,
        namespace: str = None,
        page_size: int = None,
        pod_name: str = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The ID of the container cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](https://help.aliyun.com/document_detail/182997.html) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The number of the page to return.
        self.current_page = current_page
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The name of the pod.
        self.pod_name = pod_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        return self

