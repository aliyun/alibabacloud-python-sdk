# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRedeemRequest(DaraModel):
    def __init__(
        self,
        effective_or_not: bool = None,
        expiry_time_end: str = None,
        expiry_time_start: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # Specifies whether the redemption coupon takes effect. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.effective_or_not = effective_or_not
        # The end time when the redemption coupon expires. The value must be in the yyyy-MM-ddTHH:mm:ssZ format.
        self.expiry_time_end = expiry_time_end
        # The start time when the redemption coupon expires. The value must be in the yyyy-MM-ddTHH:mm:ssZ format.
        self.expiry_time_start = expiry_time_start
        # The number of the page to return.
        self.page_num = page_num
        # The number of entries to return on each page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_or_not is not None:
            result['EffectiveOrNot'] = self.effective_or_not

        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end

        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveOrNot') is not None:
            self.effective_or_not = m.get('EffectiveOrNot')

        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')

        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

