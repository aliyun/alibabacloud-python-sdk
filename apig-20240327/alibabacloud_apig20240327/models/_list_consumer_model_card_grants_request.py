# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConsumerModelCardGrantsRequest(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
        page_number: int = None,
        page_size: int = None,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # Filters results by model card ID.
        self.model_card_id = model_card_id
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # Filters results by principal ID. This parameter must be specified together with principalType.
        self.principal_id = principal_id
        # Filters results by principal type. Valid values: Consumer and ConsumerGroup. This parameter must be specified together with principalId.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.principal_id is not None:
            result['principalId'] = self.principal_id

        if self.principal_type is not None:
            result['principalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('principalId') is not None:
            self.principal_id = m.get('principalId')

        if m.get('principalType') is not None:
            self.principal_type = m.get('principalType')

        return self

