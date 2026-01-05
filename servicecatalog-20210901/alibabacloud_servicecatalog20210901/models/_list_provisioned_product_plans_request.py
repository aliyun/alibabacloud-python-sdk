# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListProvisionedProductPlansRequest(DaraModel):
    def __init__(
        self,
        access_level_filter: str = None,
        approval_filter: str = None,
        filters: List[main_models.ListProvisionedProductPlansRequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        provisioned_product_id: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # The access filter. Valid values:
        # 
        # *   User (default): queries the plans that are created by the current requester.
        # *   Account: queries the plans that belong to the current Alibaba Cloud account.
        # *   ResourceDirectory: queries the plans that belong to the current resource directory.
        self.access_level_filter = access_level_filter
        # The access filter of the review dimension. Valid values:
        # 
        # *   ReceivedRequests: queries plans that are pending for review.
        # *   ApprovalHistory: queries review history.
        # *   AccountRequests: queries all plans that belong to the current Alibaba Cloud account.
        # *   AccountRequests: queries all plans that belong to the current Alibaba Cloud account.
        self.approval_filter = approval_filter
        # An array that consists of filter conditions.
        self.filters = filters
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size
        # The ID of the product instance.
        self.provisioned_product_id = provisioned_product_id
        # The information based on which you want to sort the query results.
        # 
        # Set the value to CreateTime, which specifies the creation time of plans.
        self.sort_by = sort_by
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   Asc: the ascending order
        # *   Desc (default): the descending order.
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_level_filter is not None:
            result['AccessLevelFilter'] = self.access_level_filter

        if self.approval_filter is not None:
            result['ApprovalFilter'] = self.approval_filter

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLevelFilter') is not None:
            self.access_level_filter = m.get('AccessLevelFilter')

        if m.get('ApprovalFilter') is not None:
            self.approval_filter = m.get('ApprovalFilter')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ListProvisionedProductPlansRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class ListProvisionedProductPlansRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter condition. Valid values:
        # 
        # *   ProvisionedProductPlanName: performs exact matches by plan name. Plan names are not case-sensitive.
        # *   ProvisionedProductPlanApprover: performs exact matches by reviewer. You must specify a reviewer in the `RamUser/RamRole:<Name of the reviewer>` format. You can specify multiple reviewers.
        # *   ProvisionedProductPlanApproverName: performs matches by reviewer name. You must specify the Resource Access Management (RAM) entity name of the reviewer. You can specify multiple reviewer names.
        # *   ProvisionedProductPlanStatus: performs matches by plan status. You must specify the state of the plan. You can specify multiple states.
        # *   ProvisionedProductPlanOwnerUid: performs exact matches by ID of Alibaba Cloud account to which a plan belongs.
        # *   FullTextSearch: performs fuzzy full-text searches by plan name.
        self.key = key
        # The value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

