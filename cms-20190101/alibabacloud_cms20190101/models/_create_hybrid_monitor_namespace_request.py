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
        # The description of the namespace.
        self.description = description
        # The name of the namespace.
        # 
        # The name can contain lowercase letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The region where the metric data is stored.
        self.namespace_region = namespace_region
        # The storage scheme of metric data. Valid values:
        # 
        # *   m_prom_user: The metric data is stored in Simple Log Service.
        # *   m_prom_pool: The metric data is stored in the private storage space provided by CloudMonitor.
        # 
        # >  For more information about the storage schemes of metric data, see [Data storage schemes for Hybrid Cloud Monitoring](https://help.aliyun.com/document_detail/2594921.html).
        self.namespace_type = namespace_type
        self.region_id = region_id
        # The data retention period. Valid values:
        # 
        # *   cms.s1.large (Retention Period 15 Days)
        # *   cms.s1.xlarge (Retention Period 32 Days)
        # *   cms.s1.2xlarge (Retention Period 63 Days)
        # *   cms.s1.3xlarge (Retention Period 93 Days) (default)
        # *   cms.s1.6xlarge (Retention Period 185 Days)
        # *   cms.s1.12xlarge (Retention Period 367 Days)
        # 
        # For information about the pricing for different retention periods, see the **Pricing** section in [Billing of the dashboard feature](https://help.aliyun.com/document_detail/223532.html).
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

