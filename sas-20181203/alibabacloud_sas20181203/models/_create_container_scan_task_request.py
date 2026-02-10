# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContainerScanTaskRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_ids: str = None,
        lang: str = None,
    ):
        # The ID of the cluster to which the container belongs.
        # 
        # > You can call the [DescribeGroupedContainerInstances](https://help.aliyun.com/document_detail/182997.html) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The ID of the container.
        self.container_ids = container_ids
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.container_ids is not None:
            result['ContainerIds'] = self.container_ids

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainerIds') is not None:
            self.container_ids = m.get('ContainerIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

