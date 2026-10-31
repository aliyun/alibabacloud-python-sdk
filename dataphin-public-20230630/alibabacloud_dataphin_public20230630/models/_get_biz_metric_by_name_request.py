# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetBizMetricByNameRequest(DaraModel):
    def __init__(
        self,
        biz_metric_by_name_query: main_models.GetBizMetricByNameRequestBizMetricByNameQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query request.
        # 
        # This parameter is required.
        self.biz_metric_by_name_query = biz_metric_by_name_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id

    def validate(self):
        if self.biz_metric_by_name_query:
            self.biz_metric_by_name_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_metric_by_name_query is not None:
            result['BizMetricByNameQuery'] = self.biz_metric_by_name_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizMetricByNameQuery') is not None:
            temp_model = main_models.GetBizMetricByNameRequestBizMetricByNameQuery()
            self.biz_metric_by_name_query = temp_model.from_map(m.get('BizMetricByNameQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class GetBizMetricByNameRequestBizMetricByNameQuery(DaraModel):
    def __init__(
        self,
        draft: bool = None,
        name: str = None,
    ):
        # Specifies whether to query the details of a draft or published asset. Valid values:
        # - True: Draft.
        # - False: Published.
        # 
        # This parameter is required.
        self.draft = draft
        # The name of the business metric.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft is not None:
            result['Draft'] = self.draft

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Draft') is not None:
            self.draft = m.get('Draft')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

