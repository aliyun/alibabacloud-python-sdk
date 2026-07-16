# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHybridMonitorNamespaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        namespace: str = None,
        namespace_region: str = None,
        namespace_type: str = None,
        region_id: str = None,
        spec: str = None,
    ):
        # The description of the metric repository.
        self.description = description
        # The name of the metric repository.
        # 
        # Format: consists of lowercase letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The region in which monitoring data is stored.
        self.namespace_region = namespace_region
        # The storage solution for monitoring data. Valid values:
        # 
        # - aliyun_prometheus: monitoring data is stored in Managed Service for Prometheus.
        # 
        # > For more information about storage solutions for monitoring data, see [Storage solutions for Hybrid Cloud Monitoring data](https://help.aliyun.com/document_detail/2594921.html).
        self.namespace_type = namespace_type
        self.region_id = region_id
        # The data storage duration. Valid values:
        # 
        # - cms.s1.large: storage duration of 15 days.
        # - cms.s1.xlarge: storage duration of 32 days.
        # - cms.s1.2xlarge: storage duration of 63 days.
        # - cms.s1.3xlarge (default): storage duration of 93 days.
        # - cms.s1.6xlarge: storage duration of 185 days.
        # - cms.s1.12xlarge: storage duration of 376 days.
        # 
        # For the pricing of different storage duration specifications, see the **Pricing** section in [monitoring dashboard](https://help.aliyun.com/document_detail/223532.html).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_region is not None:
            result['NamespaceRegion'] = self.namespace_region

        if self.namespace_type is not None:
            result['NamespaceType'] = self.namespace_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespaceRegion') is not None:
            self.namespace_region = m.get('NamespaceRegion')

        if m.get('NamespaceType') is not None:
            self.namespace_type = m.get('NamespaceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

