# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateQuotaApplicationResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        apply_time: str = None,
        approve_value: float = None,
        audit_reason: str = None,
        desire_value: int = None,
        dimension: Dict[str, Any] = None,
        effective_time: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_arn: str = None,
        quota_description: str = None,
        quota_name: str = None,
        quota_unit: str = None,
        reason: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the quota increase request.
        self.application_id = application_id
        # The time when the quota increase request was submitted. The time is in ISO 8601 format and in UTC. The value ends with Z.
        self.apply_time = apply_time
        # The approved quota value.
        self.approve_value = approve_value
        # The review comments on the quota increase request.
        self.audit_reason = audit_reason
        # The requested quota value.
        self.desire_value = desire_value
        # The quota dimensions.
        self.dimension = dimension
        # The effective period of the quota. The time is in ISO 8601 format and in UTC. The value ends with Z.
        self.effective_time = effective_time
        # The time when the quota expires. The time is in ISO 8601 format and in UTC. The value ends with Z.
        self.expire_time = expire_time
        # Indicates whether a notification is sent about the request result. Valid values:
        # 
        # - 0: no notification is sent.
        # 
        # - 3: a notification is sent.
        self.notice_type = notice_type
        # The abbreviation of the cloud service name.
        self.product_code = product_code
        # The quota ID.
        self.quota_action_code = quota_action_code
        # The Alibaba Cloud Resource Name (ARN) of the quota.
        self.quota_arn = quota_arn
        # The description of the quota.
        self.quota_description = quota_description
        # The name of the quota.
        self.quota_name = quota_name
        # The unit of the quota.
        self.quota_unit = quota_unit
        # The reason for the quota increase request.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The approval status of the quota increase request.
        self.status = status

    def validate(self):
        pass

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

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_arn is not None:
            result['QuotaArn'] = self.quota_arn

        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.quota_unit is not None:
            result['QuotaUnit'] = self.quota_unit

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaArn') is not None:
            self.quota_arn = m.get('QuotaArn')

        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('QuotaUnit') is not None:
            self.quota_unit = m.get('QuotaUnit')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

