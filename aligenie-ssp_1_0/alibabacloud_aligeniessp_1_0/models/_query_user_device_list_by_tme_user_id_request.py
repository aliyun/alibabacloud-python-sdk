# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryUserDeviceListByTmeUserIdRequest(DaraModel):
    def __init__(
        self,
        sp: str = None,
        tme_user_id: str = None,
    ):
        # "KG": KuGou  
        # "KW": Kuwo  
        # "QM": QQ Music
        # 
        # This parameter is required.
        self.sp = sp
        # TME User ID
        # 
        # This parameter is required.
        self.tme_user_id = tme_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sp is not None:
            result['Sp'] = self.sp

        if self.tme_user_id is not None:
            result['TmeUserId'] = self.tme_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')

        if m.get('TmeUserId') is not None:
            self.tme_user_id = m.get('TmeUserId')

        return self

