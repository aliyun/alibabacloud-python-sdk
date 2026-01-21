# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHybridMonitorNamespaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        namespace: str = None,
        region_id: str = None,
        spec: str = None,
    ):
        # The description of the namespace.
        self.description = description
        # The name of the namespace.
        # 
        # The name can contain letters, digits, and hyphens (-).
        # 
        # For information about how to obtain the name of a namespace, see [DescribeHybridMonitorNamespaceList](https://help.aliyun.com/document_detail/428880.html).
        # 
        # This parameter is required.
        self.namespace = namespace
        self.region_id = region_id
        # The data retention period. Valid values:
        # 
        # *   cms.s1.large: Data is stored for 15 days.
        # *   cms.s1.xlarge: Data is stored for 32 days.
        # *   cms.s1.2xlarge: Data is stored for 63 days.
        # *   cms.s1.3xlarge: Data is stored for 93 days.
        # *   cms.s1.6xlarge: Data is stored for 185 days.
        # *   cms.s1.12xlarge: Data is stored for 376 days.
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

