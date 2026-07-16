# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServiceEndpointsRequest(DaraModel):
    def __init__(
        self,
        component: str = None,
        domain_type: str = None,
        instance_id: str = None,
        max_results: int = None,
        network_type: str = None,
        next_token: str = None,
        resource_name: str = None,
        skip: str = None,
    ):
        self.component = component
        self.domain_type = domain_type
        # This parameter is required.
        self.instance_id = instance_id
        self.max_results = max_results
        self.network_type = network_type
        self.next_token = next_token
        self.resource_name = resource_name
        self.skip = skip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component is not None:
            result['Component'] = self.component

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.skip is not None:
            result['Skip'] = self.skip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Component') is not None:
            self.component = m.get('Component')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        return self

