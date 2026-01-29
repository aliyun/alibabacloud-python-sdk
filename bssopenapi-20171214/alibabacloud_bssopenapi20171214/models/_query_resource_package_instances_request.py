# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryResourcePackageInstancesRequest(DaraModel):
    def __init__(
        self,
        expiry_time_end: str = None,
        expiry_time_start: str = None,
        include_partner: bool = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        product_code: str = None,
    ):
        # The end of the expiration time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.expiry_time_end = expiry_time_end
        # The beginning of the expiration time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.expiry_time_start = expiry_time_start
        # Specifies whether partners are involved.
        self.include_partner = include_partner
        self.owner_id = owner_id
        # The number of the page to return. Default value: 1.
        self.page_num = page_num
        # The number of entries to return on each page. Default value: 20. Maximum value: 300.
        self.page_size = page_size
        # The code of the service.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end

        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start

        if self.include_partner is not None:
            result['IncludePartner'] = self.include_partner

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')

        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')

        if m.get('IncludePartner') is not None:
            self.include_partner = m.get('IncludePartner')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        return self

