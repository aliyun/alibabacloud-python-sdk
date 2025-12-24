# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCenterPolicyListRequest(DaraModel):
    def __init__(
        self,
        academic_proxy: str = None,
        business_type: int = None,
        model_library: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_group_id: List[str] = None,
        port_proxy: str = None,
        resource_type: str = None,
        scope: str = None,
    ):
        self.academic_proxy = academic_proxy
        # The business type.
        # 
        # Valid values:
        # 
        # *   1: public cloud
        # *   8: commercial edition.
        # 
        # This parameter is required.
        self.business_type = business_type
        self.model_library = model_library
        # The page number.\\
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The IDs of the cloud computer policies.
        self.policy_group_id = policy_group_id
        self.port_proxy = port_proxy
        # The resource type.
        # 
        # Valid values:
        # 
        # *   app: cloud applications.
        # *   desktop: cloud computers.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The effective scope of the cloud computer policy.
        # 
        # Valid values:
        # 
        # *   IP: The policy applies to specific IP addresses.
        # *   GLOBAL: The policy applies globally.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.academic_proxy is not None:
            result['AcademicProxy'] = self.academic_proxy

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.model_library is not None:
            result['ModelLibrary'] = self.model_library

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.port_proxy is not None:
            result['PortProxy'] = self.port_proxy

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcademicProxy') is not None:
            self.academic_proxy = m.get('AcademicProxy')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('ModelLibrary') is not None:
            self.model_library = m.get('ModelLibrary')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PortProxy') is not None:
            self.port_proxy = m.get('PortProxy')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

