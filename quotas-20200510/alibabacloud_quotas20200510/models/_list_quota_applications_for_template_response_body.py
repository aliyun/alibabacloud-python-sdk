# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaApplicationsForTemplateResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_batch_applications: List[main_models.ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplications] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records returned for the query.
        self.max_results = max_results
        # The token that marks the start of the data to read.
        self.next_token = next_token
        # The list of historical quota applications.
        self.quota_batch_applications = quota_batch_applications
        # The request ID.
        self.request_id = request_id
        # The total number of records returned for the request.
        self.total_count = total_count

    def validate(self):
        if self.quota_batch_applications:
            for v1 in self.quota_batch_applications:
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

        result['QuotaBatchApplications'] = []
        if self.quota_batch_applications is not None:
            for k1 in self.quota_batch_applications:
                result['QuotaBatchApplications'].append(k1.to_map() if k1 else None)

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

        self.quota_batch_applications = []
        if m.get('QuotaBatchApplications') is not None:
            for k1 in m.get('QuotaBatchApplications'):
                temp_model = main_models.ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplications()
                self.quota_batch_applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplications(DaraModel):
    def __init__(
        self,
        aliyun_uids: List[str] = None,
        apply_time: str = None,
        audit_status_vos: List[main_models.ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplicationsAuditStatusVos] = None,
        batch_quota_application_id: str = None,
        desire_value: float = None,
        dimensions: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        reason: str = None,
    ):
        # The list of Alibaba Cloud accounts of the members in a resource directory for which the quota applications are submitted.
        self.aliyun_uids = aliyun_uids
        # The UTC time when the quota increase application was submitted.
        self.apply_time = apply_time
        # The number of applications in different approval states.
        self.audit_status_vos = audit_status_vos
        # The ID of the batch quota application.
        self.batch_quota_application_id = batch_quota_application_id
        # The requested quota value.
        self.desire_value = desire_value
        # The quota dimensions.
        # 
        # Format: {"regionId":"cn-hangzhou"}.
        self.dimensions = dimensions
        # The UTC time when the quota takes effect.
        self.effective_time = effective_time
        # The UTC time when the quota expires.
        self.expire_time = expire_time
        # The abbreviation of the Alibaba Cloud service.
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
        # The reason for the quota increase application.
        self.reason = reason

    def validate(self):
        if self.audit_status_vos:
            for v1 in self.audit_status_vos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_uids is not None:
            result['AliyunUids'] = self.aliyun_uids

        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        result['AuditStatusVos'] = []
        if self.audit_status_vos is not None:
            for k1 in self.audit_status_vos:
                result['AuditStatusVos'].append(k1.to_map() if k1 else None)

        if self.batch_quota_application_id is not None:
            result['BatchQuotaApplicationId'] = self.batch_quota_application_id

        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUids') is not None:
            self.aliyun_uids = m.get('AliyunUids')

        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        self.audit_status_vos = []
        if m.get('AuditStatusVos') is not None:
            for k1 in m.get('AuditStatusVos'):
                temp_model = main_models.ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplicationsAuditStatusVos()
                self.audit_status_vos.append(temp_model.from_map(k1))

        if m.get('BatchQuotaApplicationId') is not None:
            self.batch_quota_application_id = m.get('BatchQuotaApplicationId')

        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

class ListQuotaApplicationsForTemplateResponseBodyQuotaBatchApplicationsAuditStatusVos(DaraModel):
    def __init__(
        self,
        count: int = None,
        status: str = None,
    ):
        # The number of applications.
        self.count = count
        # The approval status of the quota increase application. Valid values:
        # 
        # - Disagree: denied.
        # 
        # - Agree: approved.
        # 
        # - Process: pending approval.
        # 
        # - Cancel: closed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

