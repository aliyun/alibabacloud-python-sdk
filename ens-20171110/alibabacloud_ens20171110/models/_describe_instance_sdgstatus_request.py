# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInstanceSDGStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        sdgids: List[str] = None,
        status: str = None,
    ):
        # The ID of the AIC instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The IDs of SDGs that you want to query. By default, all SDGs are queried.
        self.sdgids = sdgids
        # The deployment status of the SDG.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sdgids is not None:
            result['SDGIds'] = self.sdgids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SDGIds') is not None:
            self.sdgids = m.get('SDGIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

