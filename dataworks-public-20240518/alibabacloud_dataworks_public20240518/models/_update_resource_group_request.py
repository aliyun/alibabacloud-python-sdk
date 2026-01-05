# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResourceGroupRequest(DaraModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        id: str = None,
        name: str = None,
        remark: str = None,
    ):
        # The ID of the new Alibaba Cloud resource group.
        self.aliyun_resource_group_id = aliyun_resource_group_id
        # The ID of the resource group.
        # 
        # This parameter is required.
        self.id = id
        # The new name that you want to change for the resource group.
        self.name = name
        # The new remarks that you want to modify for the resource group.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

