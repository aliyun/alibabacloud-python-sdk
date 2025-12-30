# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveDomainResourceGroupRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        new_resource_group_id: str = None,
        resource_id: str = None,
    ):
        # The language of the values of specific response parameters. Default value: en. Valid values: en, zh, and ja.
        self.lang = lang
        # The ID of the new resource group.
        # 
        # You can view the resource group ID in the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups?).
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The domain name.
        # 
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

