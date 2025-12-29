# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKubernetesVersionMetadataRequest(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        kubernetes_version: str = None,
        mode: str = None,
        profile: str = None,
        query_upgradable_version: bool = None,
        region: str = None,
        runtime: str = None,
    ):
        # The cluster type that you want to use. Valid values:
        # 
        # *   `Kubernetes`: ACK dedicated cluster.
        # *   `ManagedKubernetes`: ACK managed cluster. ACK managed clusters include ACK Pro clusters, ACK Basic clusters, ACK Serverless Pro clusters, ACK Serverless Basic clusters, ACK Edge Pro clusters, and ACK Edge Basic clusters.
        # *   `ExternalKubernetes`: registered cluster.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The Kubernetes version of the cluster. The Kubernetes versions supported by ACK are the same as the Kubernetes versions supported by open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not configure this parameter, the latest Kubernetes version is used.
        # 
        # For more information about the Kubernetes versions supported by ACK, see [Release notes for Kubernetes versions](https://help.aliyun.com/document_detail/185269.html).
        self.kubernetes_version = kubernetes_version
        # The query mode. Valid values:
        # 
        # *   `supported`: queries all supported Kubernetes versions.
        # *   `creatable`: queries only Kubernetes versions of clusters that you can create.
        # 
        # If you specify `KubernetesVersion`, this parameter does not take effect.
        # 
        # If you do not specify a query mode, Kubernetes versions of clusters that you can create are returned.
        self.mode = mode
        # The scenario where clusters are used. Valid values:
        # 
        # *   `Default`: non-edge computing scenarios
        # *   `Edge`: edge computing scenarios
        # *   `Serverless`: serverless scenarios.
        # 
        # Default value: `Default`.
        self.profile = profile
        # Specifies whether to query the Kubernetes versions available for updates. This parameter takes effect only when the KubernetesVersion parameter is specified.
        # 
        # *   true: queries the Kubernetes versions available for updates.
        # *   false: does not query the Kubernetes versions available for updates.
        self.query_upgradable_version = query_upgradable_version
        # The region ID of the cluster.
        # 
        # This parameter is required.
        self.region = region
        # The container runtime type that you want to use. You can specify a runtime type to query only OS images that support the runtime type. Valid values:
        # 
        # *   `docker`: Docker
        # *   `containerd`: containerd
        # *   `Sandboxed-Container.runv`: Sandboxed-Container
        # 
        # If you specify a runtime type, only the OS images that support the specified runtime type are returned.
        # 
        # Otherwise, all OS images are returned.
        self.runtime = runtime

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.query_upgradable_version is not None:
            result['QueryUpgradableVersion'] = self.query_upgradable_version

        if self.region is not None:
            result['Region'] = self.region

        if self.runtime is not None:
            result['runtime'] = self.runtime

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('QueryUpgradableVersion') is not None:
            self.query_upgradable_version = m.get('QueryUpgradableVersion')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        return self

