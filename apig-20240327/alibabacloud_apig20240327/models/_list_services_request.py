# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListServicesRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        source_type: str = None,
        source_types: str = None,
    ):
        # The ID of the Cloud-native API Gateway instance.
        self.gateway_id = gateway_id
        # The service name.
        self.name = name
        # The page number to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The service source. Valid values:
        # 
        # *   MSE_NACOS: a service in an MSE Nacos instance
        # *   K8S: a service in a Kubernetes (K8s) cluster in Container Service for Kubernetes (ACK)
        # *   FC3: a service in Function Compute
        # *   VIP: a fixed address
        # *   DNS: a domain name
        # 
        # Enumerated values:
        # 
        # *   K8S
        # *   FC3
        # *   DNS
        # *   VIP
        # *   MSE_NACOS
        self.source_type = source_type
        self.source_types = source_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.source_types is not None:
            result['sourceTypes'] = self.source_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('sourceTypes') is not None:
            self.source_types = m.get('sourceTypes')

        return self

