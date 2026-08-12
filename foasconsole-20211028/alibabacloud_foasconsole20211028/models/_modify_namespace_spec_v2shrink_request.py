# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNamespaceSpecV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        elastic_resource_spec_shrink: str = None,
        guaranteed_resource_spec_shrink: str = None,
        ha: bool = None,
        instance_id: str = None,
        namespace: str = None,
        region: str = None,
    ):
        # The upper limit of pay-as-you-go resources allocated to the project namespace.
        self.elastic_resource_spec_shrink = elastic_resource_spec_shrink
        # The size of subscription resources allocated to the project namespace.
        self.guaranteed_resource_spec_shrink = guaranteed_resource_spec_shrink
        # Specifies whether the project namespace uses zone-disaster recovery.
        # 
        # This parameter is required.
        self.ha = ha
        # The order instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The project namespace name.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The region.
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_resource_spec_shrink is not None:
            result['ElasticResourceSpec'] = self.elastic_resource_spec_shrink

        if self.guaranteed_resource_spec_shrink is not None:
            result['GuaranteedResourceSpec'] = self.guaranteed_resource_spec_shrink

        if self.ha is not None:
            result['Ha'] = self.ha

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticResourceSpec') is not None:
            self.elastic_resource_spec_shrink = m.get('ElasticResourceSpec')

        if m.get('GuaranteedResourceSpec') is not None:
            self.guaranteed_resource_spec_shrink = m.get('GuaranteedResourceSpec')

        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

