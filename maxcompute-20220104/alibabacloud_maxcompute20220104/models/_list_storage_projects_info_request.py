# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStorageProjectsInfoRequest(DaraModel):
    def __init__(
        self,
        asc_order: bool = None,
        date: str = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        project_prefix: str = None,
        recent_days: int = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to sort the results in ascending order.
        self.asc_order = asc_order
        # The statistics collection date. The date is accurate to the day. The date must be in the `YYYYMMdd` format.
        # 
        # This parameter is required.
        self.date = date
        # The column to sort by. Valid values:
        # 
        # - totalStorage
        # 
        # - longTermStorage
        # 
        # - lowFreqStorage
        # 
        # - standardStorage
        # 
        # - recycleBinStorage
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The prefix of the MaxCompute project name.
        self.project_prefix = project_prefix
        # The number of days for year-over-year comparison.
        self.recent_days = recent_days
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
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order

        if self.date is not None:
            result['date'] = self.date

        if self.order_column is not None:
            result['orderColumn'] = self.order_column

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.project_prefix is not None:
            result['projectPrefix'] = self.project_prefix

        if self.recent_days is not None:
            result['recentDays'] = self.recent_days

        if self.region is not None:
            result['region'] = self.region

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('projectPrefix') is not None:
            self.project_prefix = m.get('projectPrefix')

        if m.get('recentDays') is not None:
            self.recent_days = m.get('recentDays')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

