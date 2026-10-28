# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQuotaApplicationsForTemplateRequest(DaraModel):
    def __init__(
        self,
        apply_end_time: str = None,
        apply_start_time: str = None,
        batch_quota_application_id: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
    ):
        # The end of the time range to query. The value is in UTC.
        # 
        # > The interval between `ApplyStartTime` and `ApplyEndTime` must be 7 days or less. If you do not set these two parameters, quota applications submitted within the last 7 days are queried.
        self.apply_end_time = apply_end_time
        # The beginning of the time range to query. The value is in UTC.
        # 
        # > The interval between `ApplyStartTime` and `ApplyEndTime` must be 7 days or less. If you do not set these two parameters, quota applications submitted within the last 7 days are queried.
        self.apply_start_time = apply_start_time
        # The ID of the batch quota application.
        self.batch_quota_application_id = batch_quota_application_id
        # The maximum number of results to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 30.
        self.max_results = max_results
        # The token that marks the start of the data to read.
        # 
        # > If you do not set this parameter, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service.
        # 
        # > For more information about how to obtain the abbreviation of an Alibaba Cloud service, see the `ProductCode` parameter in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The type of the quota. Valid values:
        # 
        # - CommonQuota: general quota.
        # 
        # - FlowControl: API rate limit.
        # 
        # - WhiteListLabel: privilege.
        self.quota_category = quota_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_end_time is not None:
            result['ApplyEndTime'] = self.apply_end_time

        if self.apply_start_time is not None:
            result['ApplyStartTime'] = self.apply_start_time

        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyEndTime') is not None:
            self.apply_end_time = m.get('ApplyEndTime')

        if m.get('ApplyStartTime') is not None:
            self.apply_start_time = m.get('ApplyStartTime')

        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        return self

