# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_applications: List[main_models.ListQuotaApplicationsResponseBodyQuotaApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records returned in this query.
        self.max_results = max_results
        # The token that marks the position of the returned data. An empty value indicates that all data has been returned.
        self.next_token = next_token
        # The details of the quota increase applications.
        self.quota_applications = quota_applications
        # The request ID.
        self.request_id = request_id
        # The total number of quota increase applications.
        self.total_count = total_count

    def validate(self):
        if self.quota_applications:
            for v1 in self.quota_applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['QuotaApplications'] = []
        if self.quota_applications is not None:
            for k1 in self.quota_applications:
                result['QuotaApplications'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.quota_applications = []
        if m.get('QuotaApplications') is not None:
            for k1 in m.get('QuotaApplications'):
                temp_model = main_models.ListQuotaApplicationsResponseBodyQuotaApplications()
                self.quota_applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQuotaApplicationsResponseBodyQuotaApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        comment: str = None,
        desire_value: float = None,
        dimension: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        notice_type: int = None,
        period: main_models.ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The ID of the quota increase application.
        self.application_id = application_id
        # The time when the quota increase application was submitted. The value is in ISO 8601 format, in UTC, and ends with Z.
        self.apply_time = apply_time
        # The approved quota value of the quota increase application.
        self.approve_value = approve_value
        # The approval comment for the quota increase application.
        self.audit_reason = audit_reason
        # The remarks of the quota increase application.
        self.comment = comment
        # The requested quota value of the quota increase application.
        self.desire_value = desire_value
        # The quota dimensions of the quota increase application.
        self.dimension = dimension
        # The effective period of the quota increase application. The value is in ISO 8601 format, in UTC, and ends with Z.
        self.effective_time = effective_time
        # The expiration time of the quota increase application. The value is in ISO 8601 format, in UTC, and ends with Z.
        self.expire_time = expire_time
        # Indicates whether a notification is sent for the quota increase application result. Valid values:
        # 
        # - 0: No.
        # - 3: Yes.
        self.notice_type = notice_type
        # The quota calculation period.
        self.period = period
        # The abbreviation of the cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The quota category. Valid values:
        # - CommonQuota (default): general quota.
        # - WhiteListLabel: privilege.
        # - FlowControl: API rate limit.
        self.quota_category = quota_category
        # The description of the quota.
        self.quota_description = quota_description
        # The name of the quota.
        self.quota_name = quota_name
        # The unit of the quota.
        self.quota_unit = quota_unit
        # The reason for the quota increase application.
        self.reason = reason
        # The approval status of the quota increase application. Valid values:
        # 
        # - Disagree: Rejected.
        # 
        # - Agree: Approved.
        # 
        # - Process: Under review.
        # 
        # - Cancel: Closed.
        self.status = status

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value

        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type

        if self.period is not None:
            result['Period'] = self.period.to_map()

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn

        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')

        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        if m.get('Period') is not None:
            temp_model = main_models.ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListQuotaApplicationsResponseBodyQuotaApplicationsPeriod(DaraModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the quota calculation period. Valid values:
        # - second: seconds.
        # - minute: minutes.
        # - hour: hours.
        # - day: days.
        # - week: weeks.
        self.period_unit = period_unit
        # The value of the quota calculation period.
        self.period_value = period_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.period_value is not None:
            result['PeriodValue'] = self.period_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PeriodValue') is not None:
            self.period_value = m.get('PeriodValue')

        return self

