# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class QueryAlertRulesInput(DaraModel):
    def __init__(
        self,
        filter: main_models.QueryAlertRulesFilter = None,
        pagination: main_models.Pagination = None,
        workspace: str = None,
    ):
        self.filter = filter
        self.pagination = pagination
        self.workspace = workspace

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter.to_map()

        if self.pagination is not None:
            result['pagination'] = self.pagination.to_map()

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            temp_model = main_models.QueryAlertRulesFilter()
            self.filter = temp_model.from_map(m.get('filter'))

        if m.get('pagination') is not None:
            temp_model = main_models.Pagination()
            self.pagination = temp_model.from_map(m.get('pagination'))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

