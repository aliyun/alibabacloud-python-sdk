# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListPrivateK8sResponseBody(DaraModel):
    def __init__(
        self,
        private_k8s_infos: List[main_models.ListPrivateK8sResponseBodyPrivateK8sInfos] = None,
        request_id: str = None,
    ):
        # The information about the self-managed Kubernetes clusters.
        self.private_k8s_infos = private_k8s_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.private_k8s_infos:
            for v1 in self.private_k8s_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrivateK8sInfos'] = []
        if self.private_k8s_infos is not None:
            for k1 in self.private_k8s_infos:
                result['PrivateK8sInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.private_k8s_infos = []
        if m.get('PrivateK8sInfos') is not None:
            for k1 in m.get('PrivateK8sInfos'):
                temp_model = main_models.ListPrivateK8sResponseBodyPrivateK8sInfos()
                self.private_k8s_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrivateK8sResponseBodyPrivateK8sInfos(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        api_server_ip: str = None,
        cluster_name: str = None,
        id: int = None,
        k_8s_version: str = None,
        kube_config: str = None,
        net_type: int = None,
        region_id: str = None,
        vpc_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The IP address of the API server.
        self.api_server_ip = api_server_ip
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The ID of the policy.
        self.id = id
        # The version of Kubernetes.
        self.k_8s_version = k_8s_version
        # The server configuration of Kubernetes.
        self.kube_config = kube_config
        # The network type. Valid values:
        # 
        # *   **1**: Internet.
        # *   **2**: VPC.
        self.net_type = net_type
        # The ID of the region.
        self.region_id = region_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.api_server_ip is not None:
            result['ApiServerIp'] = self.api_server_ip

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.id is not None:
            result['Id'] = self.id

        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version

        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ApiServerIp') is not None:
            self.api_server_ip = m.get('ApiServerIp')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')

        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

