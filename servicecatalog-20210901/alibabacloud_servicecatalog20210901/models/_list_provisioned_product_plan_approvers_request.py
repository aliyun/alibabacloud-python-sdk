# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_servicecatalog20210901 import models as main_models
from darabonba.model import DaraModel

class ListProvisionedProductPlanApproversRequest(DaraModel):
    def __init__(
        self,
        access_level_filter: str = None,
        approval_filter: str = None,
        filters: List[main_models.ListProvisionedProductPlanApproversRequestFilters] = None,
    ):
        # The access filter. Valid values:
        # 
        # *   User (default): queries the plans that are created by the current requester.
        # *   Account: queries the plans that belong to the current Alibaba Cloud account.
        # *   ResourceDirectory: queries the plans that belong to the current resource directory.
        # 
        # >  You must specify one of the `ApprovalFilter` and `AccessLevelFilter` parameters, but not both.
        self.access_level_filter = access_level_filter
        # The access filter of the review dimension. Valid values:
        # 
        # *   AccountRequests: queries all reviewed plans that belong to the current Alibaba Cloud account.
        # *   ResourceDirectoryRequests: queries all plans that belong to the current resource directory.
        # 
        # >  You must specify one of the `ApprovalFilter` and `AccessLevelFilter` parameters, but not both.
        self.approval_filter = approval_filter
        # An array that consists of filter conditions.
        self.filters = filters

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
                temp_model = main_models.ListProvisionedProductPlanApproversRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        return self

class ListProvisionedProductPlanApproversRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the filter condition. Valid values:
        # 
        # *   ProvisionedProductPlanApproverName: performs fuzzy match by reviewer name.
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

