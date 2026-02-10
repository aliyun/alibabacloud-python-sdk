# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCriteriaStrategyRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        image_name: str = None,
        label: str = None,
        namespace: str = None,
        strategy_name: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The name of the image.
        # 
        # >  You can call the [GetOpaClusterImageList](~~GetOpaClusterImageList~~) operation to query the names of images.
        self.image_name = image_name
        # The tag that is added to the container.
        # 
        # >  You can call the [GetOpaClusterLabelList](~~GetOpaClusterLabelList~~) operation to query the tags that are added to containers.
        self.label = label
        # The namespace of the cluster.
        # 
        # >  You can call the [GetOpaClusterNamespaceList](~~GetOpaClusterNamespaceList~~) operation to query the namespaces of clusters.
        self.namespace = namespace
        # The name of the rule.
        self.strategy_name = strategy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.label is not None:
            result['Label'] = self.label

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

