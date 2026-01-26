# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GrafanaWorkspaceIntegration(DaraModel):
    def __init__(
        self,
        datasource_amount: int = None,
        integration_id: str = None,
        integration_name: str = None,
        previews: List[main_models.GrafanaWorkspaceIntegrationPreview] = None,
        status: str = None,
        support_regions: List[str] = None,
    ):
        self.datasource_amount = datasource_amount
        self.integration_id = integration_id
        self.integration_name = integration_name
        self.previews = previews
        self.status = status
        self.support_regions = support_regions

    def validate(self):
        if self.previews:
            for v1 in self.previews:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_amount is not None:
            result['datasourceAmount'] = self.datasource_amount

        if self.integration_id is not None:
            result['integrationId'] = self.integration_id

        if self.integration_name is not None:
            result['integrationName'] = self.integration_name

        result['previews'] = []
        if self.previews is not None:
            for k1 in self.previews:
                result['previews'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.support_regions is not None:
            result['supportRegions'] = self.support_regions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasourceAmount') is not None:
            self.datasource_amount = m.get('datasourceAmount')

        if m.get('integrationId') is not None:
            self.integration_id = m.get('integrationId')

        if m.get('integrationName') is not None:
            self.integration_name = m.get('integrationName')

        self.previews = []
        if m.get('previews') is not None:
            for k1 in m.get('previews'):
                temp_model = main_models.GrafanaWorkspaceIntegrationPreview()
                self.previews.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('supportRegions') is not None:
            self.support_regions = m.get('supportRegions')

        return self

