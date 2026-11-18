# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AuthorizeConsumerModelCardGrantsRequest(DaraModel):
    def __init__(
        self,
        model_card_ids: List[str] = None,
        model_group_ids: List[str] = None,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # The collection of selected model card IDs for this API. This parameter can be empty or omitted, but at least one of modelCardIds and modelGroupIds must be non-empty.
        self.model_card_ids = model_card_ids
        # The actual model group IDs of the current instance. The modelCardIds parameter can be empty only when group licenses are granted. Group licenses allow zero intersection with the current API, but principal relationships with both target types empty cannot be saved.
        self.model_group_ids = model_group_ids
        # The immutable ID of the authorization principal, not the name.
        # 
        # This parameter is required.
        self.principal_id = principal_id
        # The type of the authorization principal. Valid values: Consumer and ConsumerGroup.
        # 
        # This parameter is required.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_ids is not None:
            result['modelCardIds'] = self.model_card_ids

        if self.model_group_ids is not None:
            result['modelGroupIds'] = self.model_group_ids

        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardIds') is not None:
            self.model_card_ids = m.get('modelCardIds')

        if m.get('modelGroupIds') is not None:
            self.model_group_ids = m.get('modelGroupIds')

        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        return self

