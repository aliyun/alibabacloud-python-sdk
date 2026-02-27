# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDeviceSeatsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        serial_no: str = None,
        serial_no_list: List[str] = None,
        site_id: str = None,
        tenant_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.serial_no = serial_no
        self.serial_no_list = serial_no_list
        self.site_id = site_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no

        if self.serial_no_list is not None:
            result['SerialNoList'] = self.serial_no_list

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')

        if m.get('SerialNoList') is not None:
            self.serial_no_list = m.get('SerialNoList')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

