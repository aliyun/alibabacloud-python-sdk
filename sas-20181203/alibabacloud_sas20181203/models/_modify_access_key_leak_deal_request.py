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
        # The ID of the AccessKey pair leak.
        # 
        # > You can call the [DescribeAccesskeyLeakList](~~DescribeAccesskeyLeakList~~) operation to query the ID. You must specify at least one of the Id and **IdList** parameters.
        self.id = id
        # The IDs of AccessKey pair leaks.
        self.id_list = id_list
        # The remarks that are added.
        self.remark = remark
        # The method to handle the AccessKey pair leak. Valid values:
        # 
        # *   **manual**: manually handle
        # *   **disable**: disable
        # *   **add-whitelist**: add to the whitelist
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

