# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecretBlacklistRequest(DaraModel):
    def __init__(
        self,
        black_no: str = None,
        black_type: str = None,
        pool_key: str = None,
        remark: str = None,
        way_control: str = None,
    ):
        # The blacklisted number. The value type is determined by the **BlackType** parameter:
        # 
        # - **Point-to-point blacklist**: a pair of numbers separated by a colon (:)
        # - **Number pool blacklist**: a single number
        # 
        # This parameter is required.
        self.black_no = black_no
        # The type of the blacklist. Valid values:
        # 
        # - **POINT_TO_POINT_BLACK**: point-to-point blacklist
        # - **PARTNER_GLOBAL_NUMBER_BLACK**: number pool blacklist
        # 
        # This parameter is required.
        self.black_type = black_type
        # The key of the number pool.
        # 
        # You can obtain the **number pool key** on the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool) page in the Phone Number Privacy Protection console.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        # The remark for the blacklist.
        self.remark = remark
        # The call direction control. Valid values:
        # 
        # - **PHONEA_REJECT**: The first number in BlackNo can call the second number, but the second number cannot call the first number.
        # 
        # - **PHONEB_REJECT**: The first number in BlackNo cannot call the second number, but the second number can call the first number.
        # 
        # - **Leave empty**: The two numbers in BlackNo cannot call each other.
        self.way_control = way_control

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_no is not None:
            result['BlackNo'] = self.black_no

        if self.black_type is not None:
            result['BlackType'] = self.black_type

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.way_control is not None:
            result['WayControl'] = self.way_control

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')

        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('WayControl') is not None:
            self.way_control = m.get('WayControl')

        return self

