# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQuotaUsageShrinkRequest(DaraModel):
    def __init__(
        self,
        agg_method: str = None,
        from_: int = None,
        plot_types_shrink: str = None,
        product_id: str = None,
        region: str = None,
        sub_quota_nickname: str = None,
        tenant_id: str = None,
        to: int = None,
        y_axis_types_shrink: str = None,
    ):
        # The aggregation algorithm. For a better page experience, up to 60 points can be displayed for each metric. If you select a time range longer than 1 hour, the chart uses the average value within the range (minutes of the selected time range/60) to aggregate data by default. You can change the aggregation algorithm based on your business requirements.
        self.agg_method = agg_method
        # The time when the query starts. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you set the **from** and **to** parameters to the same value, the time range is invalid and an error message is returned.
        # *   This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # The types of the charts.
        self.plot_types_shrink = plot_types_shrink
        # The quota type. Default value: ODPS.
        # 
        # *   ODPS: computing quota
        # *   TUNNEL: Tunnel quota
        self.product_id = product_id
        # The region ID.
        self.region = region
        # The alias of the level-2 quota.
        self.sub_quota_nickname = sub_quota_nickname
        # The ID of the tenant. You can log on to the MaxCompute console, and choose Tenants > Tenant Property from the left-side navigation pane to view the tenant ID.
        self.tenant_id = tenant_id
        # The time when the query ends. The value is the log time that is specified when log data is written.
        # 
        # *   The time range that is specified in this operation is a left-closed, right-open interval. The interval includes the start time specified by the **from** parameter, but does not include the end time specified by the **to** parameter. If you set the **from** and **to** parameters to the same value, the time range is invalid and an error message is returned.
        # *   This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to
        # The data metric fields.
        self.y_axis_types_shrink = y_axis_types_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agg_method is not None:
            result['aggMethod'] = self.agg_method

        if self.from_ is not None:
            result['from'] = self.from_

        if self.plot_types_shrink is not None:
            result['plotTypes'] = self.plot_types_shrink

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.region is not None:
            result['region'] = self.region

        if self.sub_quota_nickname is not None:
            result['subQuotaNickname'] = self.sub_quota_nickname

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.to is not None:
            result['to'] = self.to

        if self.y_axis_types_shrink is not None:
            result['yAxisTypes'] = self.y_axis_types_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggMethod') is not None:
            self.agg_method = m.get('aggMethod')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('plotTypes') is not None:
            self.plot_types_shrink = m.get('plotTypes')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('subQuotaNickname') is not None:
            self.sub_quota_nickname = m.get('subQuotaNickname')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('yAxisTypes') is not None:
            self.y_axis_types_shrink = m.get('yAxisTypes')

        return self

