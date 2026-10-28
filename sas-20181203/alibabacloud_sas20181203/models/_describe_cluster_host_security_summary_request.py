# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterHostSecuritySummaryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
        target_type: str = None,
    ):
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # The container search field. Valid values:
        # 
        # - **instanceId**: The instance ID.
        # - **appName**: The application name.
        # - **clusterId**: The cluster ID.
        # - **regionId**: The region ID.
        # - **nodeName**: The node name.
        # - **namespace**: The namespace.
        # - **clusterName**: The cluster name.
        # - **image**: The image name.
        # - **imageRepoName**: The image repository name.
        # - **imageRepoNamespace**: The image repository namespace.
        # - **imageRepoTag**: The image tag.
        # - **imageDigest**: The image digest.
        self.container_field_name = container_field_name
        # The value of the container search field.
        self.container_field_value = container_field_value
        self.resource_owner_id = resource_owner_id
        # The source IP address.
        self.source_ip = source_ip
        # The query type. Valid values:
        # 
        # - **containerId**: The container ID.
        # - **uuid**: The asset ID.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name

        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')

        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

