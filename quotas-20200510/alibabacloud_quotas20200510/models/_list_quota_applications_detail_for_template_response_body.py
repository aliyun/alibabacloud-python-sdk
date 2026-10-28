# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaApplicationsDetailForTemplateResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_applications: List[main_models.ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records returned for the current query.
        self.max_results = max_results
        # The token that marks the position from which the next query starts.
        self.next_token = next_token
        # A list of quota application details.
        self.quota_applications = quota_applications
        # The request ID.
        self.request_id = request_id
        # The total number of records returned for the request.
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
                temp_model = main_models.ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplications()
                self.quota_applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplications(DaraModel):
    def __init__(
        self,
        aliyun_uid: str = None,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        batch_quota_application_id: str = None,
        desire_value: float = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        notice_type: int = None,
        period: main_models.ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplicationsPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_dimension: Dict[str, str] = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        status: str = None,
    ):
        # The Alibaba Cloud account.
        self.aliyun_uid = aliyun_uid
        # The ID of the quota increase request.
        self.application_id = application_id
        # The UTC time when the quota increase request was submitted.
        self.apply_time = apply_time
        # The approved quota value.
        self.approve_value = approve_value
        # The reason for the approval.
        self.audit_reason = audit_reason
        # The ID of the quota application batch.
        self.batch_quota_application_id = batch_quota_application_id
        # The requested quota value.
        self.desire_value = desire_value
        # The UTC time when the new quota value takes effect.
        self.effective_time = effective_time
        # The language of the alert notification. Valid values:
        # 
        # - zh: Chinese.
        # 
        # - en: English.
        self.env_language = env_language
        # The UTC time when the new quota value expires.
        self.expire_time = expire_time
        # Indicates whether a notification is sent for the quota increase request. Valid values:
        # 
        # - 0: No.
        # 
        # - 3: Yes.
        self.notice_type = notice_type
        # The calculation cycle of the quota.
        self.period = period
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The quota type. Valid values:
        # 
        # - CommonQuota (default): General quota.
        # 
        # - WhiteListLabel: Privilege quota.
        # 
        # - FlowControl: API rate limit quota.
        self.quota_category = quota_category
        # The description of the quota.
        self.quota_description = quota_description
        # The quota dimensions.
        self.quota_dimension = quota_dimension
        # The name of the quota.
        self.quota_name = quota_name
        # The unit of the quota.
        self.quota_unit = quota_unit
        # The reason for the quota increase request.
        self.reason = reason
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
        if self.period:
            self.period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.approve_value is not None:
            result['ApproveValue'] = self.approve_value

        if self.audit_reason is not None:
            result['AuditReason'] = self.audit_reason

        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id

        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language

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

        if self.quota_dimension is not None:
            result['QuotaDimension'] = self.quota_dimension

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
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('ApproveValue') is not None:
            self.approve_value = m.get('ApproveValue')

        if m.get('AuditReason') is not None:
            self.audit_reason = m.get('AuditReason')

        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')

        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        if m.get('Period') is not None:
            temp_model = main_models.ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplicationsPeriod()
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

        if m.get('QuotaDimension') is not None:
            self.quota_dimension = m.get('QuotaDimension')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListQuotaApplicationsDetailForTemplateResponseBodyQuotaApplicationsPeriod(DaraModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the calculation cycle.
        self.period_unit = period_unit
        # The value of the calculation cycle.
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

