# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStorageSummaryComparedShrinkRequest(DaraModel):
    def __init__(
        self,
        begin_date: str = None,
        end_date: str = None,
        projects_shrink: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The start date.
        # 
        # This parameter is required.
        self.begin_date = begin_date
        # The end date.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The list of projects.
        self.projects_shrink = projects_shrink
        # The region ID.
        self.region = region
        # The tenant ID. You can log on to the MaxCompute console and choose **Tenant Property** in the navigation pane on the left to view the tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_date is not None:
            result['beginDate'] = self.begin_date

        if self.end_date is not None:
            result['endDate'] = self.end_date

        if self.projects_shrink is not None:
            result['projects'] = self.projects_shrink

        if self.region is not None:
            result['region'] = self.region

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beginDate') is not None:
            self.begin_date = m.get('beginDate')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        if m.get('projects') is not None:
            self.projects_shrink = m.get('projects')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

