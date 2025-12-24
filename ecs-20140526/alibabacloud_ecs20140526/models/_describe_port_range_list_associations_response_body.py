# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribePortRangeListAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        port_range_list_associations: List[main_models.DescribePortRangeListAssociationsResponseBodyPortRangeListAssociations] = None,
        request_id: str = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If the return value is empty, no more data is returned.
        self.next_token = next_token
        # The resources that are associated with the port list.
        self.port_range_list_associations = port_range_list_associations
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.port_range_list_associations:
            for v1 in self.port_range_list_associations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PortRangeListAssociations'] = []
        if self.port_range_list_associations is not None:
            for k1 in self.port_range_list_associations:
                result['PortRangeListAssociations'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.port_range_list_associations = []
        if m.get('PortRangeListAssociations') is not None:
            for k1 in m.get('PortRangeListAssociations'):
                temp_model = main_models.DescribePortRangeListAssociationsResponseBodyPortRangeListAssociations()
                self.port_range_list_associations.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePortRangeListAssociationsResponseBodyPortRangeListAssociations(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource. Valid value: SecurityGroup.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

