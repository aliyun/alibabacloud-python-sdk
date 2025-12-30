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
    ):
        # This parameter is required.
        self.biz_metric_by_name_query = biz_metric_by_name_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizMetricByNameQuery') is not None:
            temp_model = main_models.GetBizMetricByNameRequestBizMetricByNameQuery()
            self.biz_metric_by_name_query = temp_model.from_map(m.get('BizMetricByNameQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetBizMetricByNameRequestBizMetricByNameQuery(DaraModel):
    def __init__(
        self,
        draft: bool = None,
        name: str = None,
    ):
        # This parameter is required.
        self.draft = draft
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

