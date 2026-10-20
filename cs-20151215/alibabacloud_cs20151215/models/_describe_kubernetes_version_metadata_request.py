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
        # The cluster type. Valid values:
        # 
        # - `Kubernetes`: ACK dedicated cluster.
        # - `ManagedKubernetes`: ACK managed cluster, including ACK Pro clusters, ACK basic clusters, ACK Serverless Pro clusters, ACK Serverless basic clusters, ACK Edge Pro clusters, and ACK Edge basic clusters.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The Kubernetes version of the cluster. This version is consistent with the Kubernetes community baseline version. We recommend that you select the latest version. If you do not specify this parameter, the latest version is used by default.
        # 
        # For more information about the Kubernetes versions supported by ACK, see [Overview of Kubernetes versions](https://help.aliyun.com/document_detail/185269.html).
        self.kubernetes_version = kubernetes_version
        # The query mode. Valid values:
        # 
        # - `supported`: Supported versions.
        # - `creatable`: Versions available for cluster creation.
        # 
        # If you specify KubernetesVersion, the system ignores the query mode.
        # 
        # If you do not specify a query mode, the system returns versions available for cluster creation by default.
        self.mode = mode
        # The cluster profile. Valid values:
        # 
        # - `Default`: cluster for non-edge scenarios.
        # - `Edge`: cluster for edge scenarios.
        # - `Serverless`: ASK cluster.
        # 
        # Default value: `Default`.
        self.profile = profile
        # Specifies whether to query the upgradable versions of the cluster version. This parameter takes effect only when the KubernetesVersion parameter is specified. Valid values:
        # 
        # - true: Queries upgradable versions.
        # - false: Does not query upgradable versions.
        self.query_upgradable_version = query_upgradable_version
        # The ID of the region where the cluster is deployed.
        # 
        # This parameter is required.
        self.region = region
        # The runtime type. You can specify a runtime type to filter system images supported by the runtime. Valid values:
        # 
        # - `docker`: Docker runtime.
        # - `containerd`: containerd runtime.
        # - `Sandboxed-Container.runv`: sandboxed container.
        # 
        # If you specify a runtime type, the system returns the image versions supported by the specified runtime.
        # 
        # If you do not specify a runtime type, the system returns all images by default.
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

