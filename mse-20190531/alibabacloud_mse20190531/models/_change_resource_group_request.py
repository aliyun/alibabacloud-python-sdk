# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResourceGroupRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The language in which the response is displayed. Values: zh (default): Chinese, en: English
        self.accept_language = accept_language
        # Target resource group
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # Resource ID, which is the ID of the registration and configuration center instance or the unique ID of the gateway
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Region ID
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # Resource type, such as a registration and configuration center cluster or gateway instance
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

