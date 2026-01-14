# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryGovernanceKubernetesClusterResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryGovernanceKubernetesClusterResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.QueryGovernanceKubernetesClusterResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryGovernanceKubernetesClusterResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.QueryGovernanceKubernetesClusterResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The details of the data.
        self.result = result
        # The total number of clusters.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryGovernanceKubernetesClusterResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class QueryGovernanceKubernetesClusterResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        k_8s_version: str = None,
        namespace_infos: str = None,
        pilot_start_time: str = None,
        pilot_version: str = None,
        region: str = None,
        version_life_cycle: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The version of the cluster.
        self.k_8s_version = k_8s_version
        # The information about the namespace.
        self.namespace_infos = namespace_infos
        # The time when the pilot component was started.
        self.pilot_start_time = pilot_start_time
        self.pilot_version = pilot_version
        # The region where the cluster resides.
        self.region = region
        self.version_life_cycle = version_life_cycle

    def validate(self):
        pass

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

        if self.pilot_start_time is not None:
            result['PilotStartTime'] = self.pilot_start_time

        if self.pilot_version is not None:
            result['PilotVersion'] = self.pilot_version

        if self.region is not None:
            result['Region'] = self.region

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

        if m.get('PilotStartTime') is not None:
            self.pilot_start_time = m.get('PilotStartTime')

        if m.get('PilotVersion') is not None:
            self.pilot_version = m.get('PilotVersion')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('VersionLifeCycle') is not None:
            self.version_life_cycle = m.get('VersionLifeCycle')

        return self

