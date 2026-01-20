# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListResourceShareAssociationsRequest(DaraModel):
    def __init__(
        self,
        association_status: str = None,
        association_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_share_ids: List[str] = None,
        target: str = None,
    ):
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status = association_status
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        # 
        # This parameter is required.
        self.association_type = association_type
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The `token` that is used to initiate the next request if the response of the current request is truncated. You can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token
        self.resource_arn = resource_arn
        # The ID of the resource.
        # 
        # >  This parameter is unavailable if you set the `AssociationType` parameter to `Target`.
        self.resource_id = resource_id
        # The IDs of the resource shares.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five resource shares can be specified at a time.
        self.resource_share_ids = resource_share_ids
        # The ID of the principal.
        # 
        # >  This parameter is unavailable if you set the `AssociationType` parameter to `Resource`.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status

        if self.association_type is not None:
            result['AssociationType'] = self.association_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')

        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

