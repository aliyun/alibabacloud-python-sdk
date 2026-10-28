# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class CreateQuotaApplicationRequest(DaraModel):
    def __init__(
        self,
        audit_mode: str = None,
        desire_value: float = None,
        dimensions: List[main_models.CreateQuotaApplicationRequestDimensions] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        reason: str = None,
    ):
        # >Notice: This parameter is deprecated and is not recommended.
        # 
        # The quota review mode.
        self.audit_mode = audit_mode
        # The requested quota value.
        # 
        # > - Set the requested quota value based on the `TotalUsage` (quota usage) and `ApplicableRange` (applicable range of the quota) of the target quota in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # > - Quota increase requests are reviewed by the technical support of each cloud service. To increase the chances of approval, provide a reasonable requested value and a detailed reason when you submit the request.
        # 
        # This parameter is required.
        self.desire_value = desire_value
        # The quota dimensions.
        # The dimensions are attributes of the quota. The combination of dimensions (Dimensions) and quota ID (QuotaActionCode) uniquely identifies a quota.
        # > Some cloud services require dimensions. You can call [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) to query the quota dimensions supported by a cloud service. The `Requisite` response parameter indicates whether a dimension is required.
        self.dimensions = dimensions
        # The UTC time when the quota takes effect.
        # This parameter is applicable only to privileges (WhiteListLabel). 
        # 
        # > If you do not specify an effective period, the default value is 99 years from the start time of the current quota.
        self.effective_time = effective_time
        # The language of the quota alert notification.
        self.env_language = env_language
        # The UTC time when the quota expires.
        # This parameter is applicable only to privileges (WhiteListLabel). 
        # 
        # > If you do not specify an expiration time, the default value is the submission time.
        self.expire_time = expire_time
        # Specifies whether to send a notification about the request result. Valid values:
        # 
        # - 0 (default): does not send a notification.
        # - 3: sends a notification.
        self.notice_type = notice_type
        # The abbreviation of the cloud service name.
        # 
        # > For information about how to obtain the abbreviation of a cloud service name, see `ProductCode` in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # 
        # This parameter is required.
        self.product_code = product_code
        # The quota ID.
        # 
        # > For information about how to obtain the quota ID of a cloud service, see `QuotaActionCode` in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # 
        # This parameter is required.
        self.quota_action_code = quota_action_code
        # The quota type.
        # 
        # Default value: CommonQuota.
        self.quota_category = quota_category
        # The reason for the quota increase request.
        # 
        # > Quota increase requests are reviewed by the technical support of each cloud service. To increase the chances of approval, provide a reasonable requested value and a detailed reason when you submit the request.
        # 
        # This parameter is required.
        self.reason = reason

    def validate(self):
        if self.dimensions:
            for v1 in self.dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_mode is not None:
            result['AuditMode'] = self.audit_mode

        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value

        result['Dimensions'] = []
        if self.dimensions is not None:
            for k1 in self.dimensions:
                result['Dimensions'].append(k1.to_map() if k1 else None)

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type

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
        if m.get('AuditMode') is not None:
            self.audit_mode = m.get('AuditMode')

        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.CreateQuotaApplicationRequestDimensions()
                self.dimensions.append(temp_model.from_map(k1))

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

class CreateQuotaApplicationRequestDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # > `Dimensions.N.Key` and `Dimensions.N.Value` must be specified together. The valid values of N depend on the number of dimensions supported by the cloud service. You can call [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) to query the quota dimensions supported by a cloud service. The length of the returned array is the value of N.
        self.key = key
        # The value of the quota dimension.
        # 
        # > `Dimensions.N.Key` and `Dimensions.N.Value` must be specified together. The valid values of N depend on the number of dimensions supported by the cloud service. You can call [ListProductQuotaDimensions](~~ListProductQuotaDimensions~~) to query the quota dimensions supported by a cloud service. The length of the returned array is the value of N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

