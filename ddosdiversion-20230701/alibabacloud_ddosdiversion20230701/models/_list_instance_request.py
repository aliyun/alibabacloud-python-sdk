# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        num: int = None,
        page: int = None,
        sale_id: str = None,
        status: str = None,
    ):
        # The name of the instance.
        self.name = name
        # The number of entries per page. Default value: 100.
        self.num = num
        # The page number. Default value: 1.
        self.page = page
        # The ID of the diversion instance.
        self.sale_id = sale_id
        # The instance status. Valid values:
        # - normal: The instance is running normally.
        # - expired: The instance has expired.
        # - deleting: The instance is being deleted.
        # - stopped: The instance is stopped.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.num is not None:
            result['Num'] = self.num

        if self.page is not None:
            result['Page'] = self.page

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

