# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIdentityProvidersRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The direction of the identity provider.
        self.direction = direction
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Page number.
        self.page_number = page_number
        # Page size.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

