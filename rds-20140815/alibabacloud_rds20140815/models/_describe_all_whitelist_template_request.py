# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAllWhitelistTemplateRequest(DaraModel):
    def __init__(
        self,
        fuzzy_search: bool = None,
        max_records_per_page: int = None,
        page_numbers: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_name: str = None,
    ):
        # Specifies whether to enable fuzzy search. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fuzzy_search = fuzzy_search
        # The number of entries to return on each page. Enumerated valid values: 10, 30, and 50.
        # 
        # This parameter is required.
        self.max_records_per_page = max_records_per_page
        # The page number.
        # 
        # This parameter is required.
        self.page_numbers = page_numbers
        # The region ID.
        self.region_id = region_id
        # The resource group ID. For more information about resource groups, see related documentation.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the IP whitelist template. If you specify this parameter when you perform a fuzzy search, you can call the DescribeWhitelistTemplate operation to query the name of the whitelist template during the fuzzy search.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fuzzy_search is not None:
            result['FuzzySearch'] = self.fuzzy_search

        if self.max_records_per_page is not None:
            result['MaxRecordsPerPage'] = self.max_records_per_page

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FuzzySearch') is not None:
            self.fuzzy_search = m.get('FuzzySearch')

        if m.get('MaxRecordsPerPage') is not None:
            self.max_records_per_page = m.get('MaxRecordsPerPage')

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

