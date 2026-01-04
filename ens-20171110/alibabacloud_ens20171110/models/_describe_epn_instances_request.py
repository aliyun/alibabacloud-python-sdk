# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEpnInstancesRequest(DaraModel):
    def __init__(
        self,
        epninstance_id: str = None,
        epninstance_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The version number.
        self.epninstance_id = epninstance_id
        # The name of the EPN instance.
        self.epninstance_name = epninstance_name
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 50**. Default value: **10**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id

        if self.epninstance_name is not None:
            result['EPNInstanceName'] = self.epninstance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')

        if m.get('EPNInstanceName') is not None:
            self.epninstance_name = m.get('EPNInstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

