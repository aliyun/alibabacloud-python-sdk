# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQuotaApplicationsDetailForTemplateRequest(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        batch_quota_application_id: str = None,
        max_results: int = None,
        next_token: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        status: str = None,
    ):
        # The Alibaba Cloud account for which the quota increase is requested.
        self.aliyun_uid = aliyun_uid
        # The ID of the quota application batch.
        self.batch_quota_application_id = batch_quota_application_id
        # The maximum number of records to return for the current query.
        # 
        # Valid values: 1 to 100. Default value: 30.
        self.max_results = max_results
        # The token that marks the position from which the query starts.
        # 
        # > If you do not specify this parameter, the query starts from the beginning.
        self.next_token = next_token
        # The abbreviation of the Alibaba Cloud service name.
        # 
        # > For more information about how to obtain the abbreviation of an Alibaba Cloud service name, see the `ProductCode` parameter in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The quota type. Valid values:
        # 
        # - CommonQuota: General quota.
        # 
        # - FlowControl: API rate limit quota.
        # 
        # - WhiteListLabel: Privilege quota.
        self.quota_category = quota_category
        # The approval status of the quota increase request. Valid values:
        # 
        # - Disagree: The request is rejected.
        # 
        # - Agree: The request is approved.
        # 
        # - Process: The request is in review.
        # 
        # - Cancel: The request is closed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

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

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

