# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGovernanceKubernetesClusterResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetGovernanceKubernetesClusterResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetGovernanceKubernetesClusterResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetGovernanceKubernetesClusterResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        k_8s_version: str = None,
        namespace_infos: str = None,
        namespaces: List[main_models.GetGovernanceKubernetesClusterResponseBodyDataNamespaces] = None,
        pilot_start_time: str = None,
        pilot_version: str = None,
        region: str = None,
        update_time: str = None,
        version_life_cycle: str = None,
    ):
        # The ID of the instance.
        self.cluster_id = cluster_id
        # The name of the instance.
        self.cluster_name = cluster_name
        # The version of Kubernetes.
        self.k_8s_version = k_8s_version
        # The information of the namespace.
        self.namespace_infos = namespace_infos
        # The queried namespaces.
        self.namespaces = namespaces
        # The time when the pilot component was started.
        self.pilot_start_time = pilot_start_time
        self.pilot_version = pilot_version
        # The ID of the region in which the instance resides. The region is supported by MSE.
        self.region = region
        # The time of the last modification.
        self.update_time = update_time
        self.version_life_cycle = version_life_cycle

    def validate(self):
        if self.namespaces:
            for v1 in self.namespaces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.k_8s_version is not None:
            result['K8sVersion'] = self.k_8s_version

        if self.namespace_infos is not None:
            result['NamespaceInfos'] = self.namespace_infos

        result['Namespaces'] = []
        if self.namespaces is not None:
            for k1 in self.namespaces:
                result['Namespaces'].append(k1.to_map() if k1 else None)

        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time

        if self.pilot_version is not None:
            result['PilotVersion'] = self.pilot_version

        if self.region is not None:
            result['Region'] = self.region

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.version_life_cycle is not None:
            result['VersionLifeCycle'] = self.version_life_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('K8sVersion') is not None:
            self.k_8s_version = m.get('K8sVersion')

        if m.get('NamespaceInfos') is not None:
            self.namespace_infos = m.get('NamespaceInfos')

        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k1 in m.get('Namespaces'):
                temp_model = main_models.GetGovernanceKubernetesClusterResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k1))

        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')

        if m.get('PilotVersion') is not None:
            self.pilot_version = m.get('PilotVersion')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VersionLifeCycle') is not None:
            self.version_life_cycle = m.get('VersionLifeCycle')

        return self

class GetGovernanceKubernetesClusterResponseBodyDataNamespaces(DaraModel):
    def __init__(
        self,
        mse_namespace: str = None,
        name: str = None,
    ):
        # The name of the MSE namespace that you want to access.
        self.mse_namespace = mse_namespace
        # The name of the namespace in the ACK cluster.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mse_namespace is not None:
            result['MseNamespace'] = self.mse_namespace

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MseNamespace') is not None:
            self.mse_namespace = m.get('MseNamespace')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

