# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudAgentUnlinkRequest(DaraModel):
    def __init__(
        self,
        cno: str = None,
        enterprise_id: int = None,
        request_unique_id: str = None,
        side: int = None,
        unique_id: str = None,
    ):
        # 座席工号；取值3-10位正整数，参数cno,uniqueId和requestUniqueId三选一
        self.cno = cno
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 请求唯一标识；参数cno,uniqueId和requestUniqueId三选一。注意：requestUniqueId挂机功能只在呼叫类型为webcall时生效，且需提前在管理后台将功能开启
        self.request_unique_id = request_unique_id
        # 是否座席侧挂机；取值范围：1,2（数字含义，座席侧，非座席侧)，默认座席侧
        self.side = side
        # 通话唯一标识；参数cno,uniqueId和requestUniqueId三选一
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cno is not None:
            result['Cno'] = self.cno

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.request_unique_id is not None:
            result['RequestUniqueId'] = self.request_unique_id

        if self.side is not None:
            result['Side'] = self.side

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('RequestUniqueId') is not None:
            self.request_unique_id = m.get('RequestUniqueId')

        if m.get('Side') is not None:
            self.side = m.get('Side')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        return self

