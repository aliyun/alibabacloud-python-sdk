# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetRectifyFlowRequest(DaraModel):
    def __init__(
        self,
        get_query: main_models.GetRectifyFlowRequestGetQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The business request parameters.
        # 
        # This parameter is required.
        self.get_query = get_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The operator ID.
        self.op_user_id = op_user_id

    def validate(self):
        if self.get_query:
            self.get_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_query is not None:
            result['GetQuery'] = self.get_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetQuery') is not None:
            temp_model = main_models.GetRectifyFlowRequestGetQuery()
            self.get_query = temp_model.from_map(m.get('GetQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class GetRectifyFlowRequestGetQuery(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        rectify_id: int = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of items per page. Default value: 20.
        self.page_size = page_size
        # The ID of the rectification process.
        # 
        # This parameter is required.
        self.rectify_id = rectify_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rectify_id is not None:
            result['RectifyId'] = self.rectify_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RectifyId') is not None:
            self.rectify_id = m.get('RectifyId')

        return self

