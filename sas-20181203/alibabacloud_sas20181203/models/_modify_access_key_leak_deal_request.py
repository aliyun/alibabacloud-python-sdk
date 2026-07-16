# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyAccessKeyLeakDealRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        id_list: List[int] = None,
        remark: str = None,
        type: str = None,
    ):
        # The ID of the AccessKey pair leak record.
        # >Call the [DescribeAccesskeyLeakList](~~DescribeAccesskeyLeakList~~) operation to obtain this parameter. This parameter and the **IdList** parameter cannot both be empty.
        self.id = id
        # The IDs of the AccessKey pair leak records.
        self.id_list = id_list
        # The remarks for handling the AccessKey pair leak record.
        self.remark = remark
        # The method to handle the AccessKey pair leak information. Valid values:
        # - **manual**: Manual handling.
        # - **disable**: Disable.
        # - **add-whitelist**: Add to whitelist.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.id_list is not None:
            result['IdList'] = self.id_list

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

