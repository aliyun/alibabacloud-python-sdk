# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListRectifyFlowRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListRectifyFlowRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The business request parameters.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListRectifyFlowRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListRectifyFlowRequestListQuery(DaraModel):
    def __init__(
        self,
        govern_item_type: str = None,
        page_number: int = None,
        page_size: int = None,
        priority_filters: List[str] = None,
        rectify_user_filters: List[str] = None,
        status_filters: List[str] = None,
        verify_user_filters: List[str] = None,
    ):
        # The governance object type. Valid values: TABLE, DATASOURCE_TABLE, DATASOURCE, INDEX, REALTIME_LOGICAL_TABLE, and QD_FEATURE.
        # 
        # This parameter is required.
        self.govern_item_type = govern_item_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The priority filters. Valid values: HIGH, MIDDLE, and LOW.
        self.priority_filters = priority_filters
        # The list of rectifier IDs.
        self.rectify_user_filters = rectify_user_filters
        # SUBMIT_RECTIFY, SUBMIT_VERIFY, FINISH_VERIFY, and REJECT_VERIFY.
        self.status_filters = status_filters
        # The list of verifier IDs.
        self.verify_user_filters = verify_user_filters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.govern_item_type is not None:
            result['GovernItemType'] = self.govern_item_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.priority_filters is not None:
            result['PriorityFilters'] = self.priority_filters

        if self.rectify_user_filters is not None:
            result['RectifyUserFilters'] = self.rectify_user_filters

        if self.status_filters is not None:
            result['StatusFilters'] = self.status_filters

        if self.verify_user_filters is not None:
            result['VerifyUserFilters'] = self.verify_user_filters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GovernItemType') is not None:
            self.govern_item_type = m.get('GovernItemType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PriorityFilters') is not None:
            self.priority_filters = m.get('PriorityFilters')

        if m.get('RectifyUserFilters') is not None:
            self.rectify_user_filters = m.get('RectifyUserFilters')

        if m.get('StatusFilters') is not None:
            self.status_filters = m.get('StatusFilters')

        if m.get('VerifyUserFilters') is not None:
            self.verify_user_filters = m.get('VerifyUserFilters')

        return self

