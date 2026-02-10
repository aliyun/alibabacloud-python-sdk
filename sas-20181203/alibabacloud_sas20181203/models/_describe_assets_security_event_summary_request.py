# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAssetsSecurityEventSummaryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        container_field_name: str = None,
        container_field_value: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
    ):
        # The ID of the cluster to which the container belongs.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of clusters.
        self.cluster_id = cluster_id
        # The key of the condition that is used to query on containers. Valid values:
        # 
        # *   **instanceId**: the ID of the container instance
        # *   **clusterId**: the ID of the cluster
        # *   **regionId**: the region ID of the container
        # *   **clusterName**: the name of the cluster
        # *   **image**: the name of the image
        # *   **imageRepoName**: the name of the image repository
        # *   **imageRepoNamespace**: the namespace to which the image repository belongs
        # *   **imageRepoTag**: the tag that is added to the image repository
        # *   **imageDigest**: the digest of the image
        # *   **ClusterType**: the type of the cluster
        # *   **hostIp**: the public IP address
        # *   **pod**: the pod
        # *   **podIp**: the IP address of the pod
        # *   **containerId**: the ID of the container
        # *   **vulStatus**: whether vulnerabilities are detected on the container
        # *   **alarmStatus**: whether alerts are generated for the container
        # *   **riskStatus**: whether risks are detected on the container
        # *   **riskLevel**: the risk level of the container
        # *   **containerScope**: the type of the container
        self.container_field_name = container_field_name
        # The value of the condition that is used to query on containers.
        self.container_field_value = container_field_value
        self.resource_owner_id = resource_owner_id
        # The source IP address of the request.
        self.source_ip = source_ip

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

        return self

