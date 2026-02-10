# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerFieldStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        container_grouped_fields: main_models.DescribeContainerFieldStatisticsResponseBodyContainerGroupedFields = None,
        request_id: str = None,
    ):
        # The statistical information about containers.
        self.container_grouped_fields = container_grouped_fields
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.container_grouped_fields:
            self.container_grouped_fields.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_grouped_fields is not None:
            result['ContainerGroupedFields'] = self.container_grouped_fields.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerGroupedFields') is not None:
            temp_model = main_models.DescribeContainerFieldStatisticsResponseBodyContainerGroupedFields()
            self.container_grouped_fields = temp_model.from_map(m.get('ContainerGroupedFields'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContainerFieldStatisticsResponseBodyContainerGroupedFields(DaraModel):
    def __init__(
        self,
        app_count: int = None,
        cluster_count: int = None,
        container_count: int = None,
        image_count: int = None,
        instance_count: int = None,
        namespace_count: int = None,
        pod_count: int = None,
        risk_app_count: int = None,
        risk_cluster_count: int = None,
        risk_container_count: int = None,
        risk_image_count: int = None,
        risk_instance_count: int = None,
        risk_pod_count: int = None,
    ):
        # The number of applications.
        self.app_count = app_count
        # The number of clusters.
        self.cluster_count = cluster_count
        # The number of containers.
        self.container_count = container_count
        # The number of images.
        self.image_count = image_count
        # The number of instances.
        self.instance_count = instance_count
        # The number of namespaces.
        self.namespace_count = namespace_count
        # The number of pods.
        self.pod_count = pod_count
        # The number of the applications on which risks are detected.
        self.risk_app_count = risk_app_count
        # The number of the clusters on which risks are detected.
        self.risk_cluster_count = risk_cluster_count
        # The number of the containers on which risks are detected.
        self.risk_container_count = risk_container_count
        # The number of the images on which risks are detected.
        self.risk_image_count = risk_image_count
        # The number of the instances on which risks are detected.
        self.risk_instance_count = risk_instance_count
        # The number of the pods on which risks are detected.
        self.risk_pod_count = risk_pod_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_count is not None:
            result['AppCount'] = self.app_count

        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count

        if self.container_count is not None:
            result['ContainerCount'] = self.container_count

        if self.image_count is not None:
            result['ImageCount'] = self.image_count

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.namespace_count is not None:
            result['NamespaceCount'] = self.namespace_count

        if self.pod_count is not None:
            result['PodCount'] = self.pod_count

        if self.risk_app_count is not None:
            result['RiskAppCount'] = self.risk_app_count

        if self.risk_cluster_count is not None:
            result['RiskClusterCount'] = self.risk_cluster_count

        if self.risk_container_count is not None:
            result['RiskContainerCount'] = self.risk_container_count

        if self.risk_image_count is not None:
            result['RiskImageCount'] = self.risk_image_count

        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count

        if self.risk_pod_count is not None:
            result['RiskPodCount'] = self.risk_pod_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')

        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')

        if m.get('ContainerCount') is not None:
            self.container_count = m.get('ContainerCount')

        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('NamespaceCount') is not None:
            self.namespace_count = m.get('NamespaceCount')

        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')

        if m.get('RiskAppCount') is not None:
            self.risk_app_count = m.get('RiskAppCount')

        if m.get('RiskClusterCount') is not None:
            self.risk_cluster_count = m.get('RiskClusterCount')

        if m.get('RiskContainerCount') is not None:
            self.risk_container_count = m.get('RiskContainerCount')

        if m.get('RiskImageCount') is not None:
            self.risk_image_count = m.get('RiskImageCount')

        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')

        if m.get('RiskPodCount') is not None:
            self.risk_pod_count = m.get('RiskPodCount')

        return self

