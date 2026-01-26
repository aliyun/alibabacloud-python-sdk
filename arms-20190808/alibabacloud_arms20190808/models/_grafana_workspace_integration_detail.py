# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GrafanaWorkspaceIntegrationDetail(DaraModel):
    def __init__(
        self,
        data_sources: List[main_models.GrafanaWorkspaceIntegrationDataSource] = None,
        integration_id: str = None,
        status: str = None,
    ):
        self.data_sources = data_sources
        self.integration_id = integration_id
        self.status = status

    def validate(self):
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['dataSources'].append(k1.to_map() if k1 else None)

        if self.integration_id is not None:
            result['integrationId'] = self.integration_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k1 in m.get('dataSources'):
                temp_model = main_models.GrafanaWorkspaceIntegrationDataSource()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('integrationId') is not None:
            self.integration_id = m.get('integrationId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

