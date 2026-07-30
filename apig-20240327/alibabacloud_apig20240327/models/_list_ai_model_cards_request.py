# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAiModelCardsRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the AI gateway instance. The target instance must exist, belong to the current account, and be of the AI gateway type.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # The fuzzy match keyword for the model provider identifier or model name. If left empty, all model cards under the current gateway are queried.
        self.keyword = keyword
        # The page number. Default value: 1. The value must be greater than or equal to 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Valid values: 1 to 500.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

