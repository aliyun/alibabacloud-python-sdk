# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCashCouponsRequest(DaraModel):
    def __init__(
        self,
        effective_or_not: bool = None,
        expiry_time_end: str = None,
        expiry_time_start: str = None,
    ):
        # Specifies whether the voucher takes effect. Valid values:
        # 
        # *   true: The voucher takes effect.
        # *   false: The voucher does not take effect.
        self.effective_or_not = effective_or_not
        # The end time of the validity period of the voucher. Specify the parameter in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2018-08-01T00:00:00Z.
        self.expiry_time_end = expiry_time_end
        # The start time of the validity period of the voucher. Specify the parameter in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2018-08-01T00:00:00Z.
        self.expiry_time_start = expiry_time_start

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveOrNot') is not None:
            self.effective_or_not = m.get('EffectiveOrNot')

        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')

        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')

        return self

