# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyGovernanceKubernetesClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        namespace_infos_shrink: str = None,
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
        self.namespace_infos_shrink = namespace_infos_shrink
        # The ID of the region in which the instance resides. The region is supported by MSE.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespace_infos_shrink is not None:
            result['NamespaceInfos'] = self.namespace_infos_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NamespaceInfos') is not None:
            self.namespace_infos_shrink = m.get('NamespaceInfos')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

