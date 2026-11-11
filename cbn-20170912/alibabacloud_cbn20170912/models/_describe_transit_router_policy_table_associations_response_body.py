# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouterPolicyTableAssociationsResponseBody(DaraModel):
    def __init__(
        self,
        associations: List[main_models.DescribeTransitRouterPolicyTableAssociationsResponseBodyAssociations] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The associate relationships between the policy routing table and network connectivity instances.
        self.associations = associations
        # The number of entries returned per page in a paginated query.
        self.max_results = max_results
        # The token for the next query in a paginated query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.associations:
            for v1 in self.associations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Associations'] = []
        if self.associations is not None:
            for k1 in self.associations:
                result['Associations'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associations = []
        if m.get('Associations') is not None:
            for k1 in m.get('Associations'):
                temp_model = main_models.DescribeTransitRouterPolicyTableAssociationsResponseBodyAssociations()
                self.associations.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTransitRouterPolicyTableAssociationsResponseBodyAssociations(DaraModel):
    def __init__(
        self,
        association_id: str = None,
        attachment_id: str = None,
        policy_table_id: str = None,
        status: str = None,
    ):
        # The ID of the association between the policy route table and the network instance connection.
        self.association_id = association_id
        # The ID of the network instance connection.
        self.attachment_id = attachment_id
        # The instance ID of the policy routing table.
        self.policy_table_id = policy_table_id
        # The status of the association. Valid values:
        # 
        # - **Active**: Active.
        # - **Associating**: Associating.
        # - **Dissociating**: Dissociating.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_id is not None:
            result['AssociationId'] = self.association_id

        if self.attachment_id is not None:
            result['AttachmentId'] = self.attachment_id

        if self.policy_table_id is not None:
            result['PolicyTableId'] = self.policy_table_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('AttachmentId') is not None:
            self.attachment_id = m.get('AttachmentId')

        if m.get('PolicyTableId') is not None:
            self.policy_table_id = m.get('PolicyTableId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

