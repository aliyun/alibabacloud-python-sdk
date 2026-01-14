# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ModifyGovernanceKubernetesClusterRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        namespace_infos: List[main_models.ModifyGovernanceKubernetesClusterRequestNamespaceInfos] = None,
        region_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The information about the namespace for which Microservices Engine(MSE) Microservices Governance is enabled.
        self.namespace_infos = namespace_infos
        # The ID of the region in which the instance resides. The region is supported by MSE.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.namespace_infos:
            for v1 in self.namespace_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        result['NamespaceInfos'] = []
        if self.namespace_infos is not None:
            for k1 in self.namespace_infos:
                result['NamespaceInfos'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        self.namespace_infos = []
        if m.get('NamespaceInfos') is not None:
            for k1 in m.get('NamespaceInfos'):
                temp_model = main_models.ModifyGovernanceKubernetesClusterRequestNamespaceInfos()
                self.namespace_infos.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyGovernanceKubernetesClusterRequestNamespaceInfos(DaraModel):
    def __init__(
        self,
        mse_namespace: str = None,
        name: str = None,
    ):
        # The microservice namespace. If you do not specify this parameter, Microservice Governance is not enabled for the namespace.
        self.mse_namespace = mse_namespace
        # The name of the Kubernetes namespace.
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

