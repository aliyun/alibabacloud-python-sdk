# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateModelGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        gateway_id: str = None,
        model_card_ids: List[str] = None,
        name: str = None,
    ):
        # The description of the model group. The description can be up to 1,024 UTF-16 code units in length and can be left empty.
        self.description = description
        # The ID of the AI gateway instance to which the resource belongs.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # The IDs of the actual or logical model cards within the same instance. The list can be empty and must not contain duplicate values. Model groups are not accepted as members.
        # 
        # This parameter is required.
        self.model_card_ids = model_card_ids
        # The unique name within the instance. The name must be 1 to 128 UTF-8 bytes in length after trimming.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.model_card_ids is not None:
            result['modelCardIds'] = self.model_card_ids

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('modelCardIds') is not None:
            self.model_card_ids = m.get('modelCardIds')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

