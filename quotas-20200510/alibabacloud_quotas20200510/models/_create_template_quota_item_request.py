# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateQuotaItemRequest(DaraModel):
    def __init__(
        self,
        desire_value: float = None,
        dimensions: List[main_models.CreateTemplateQuotaItemRequestDimensions] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
    ):
        # The requested quota value.
        # 
        # > - Set the requested quota value based on the `TotalUsage` (quota usage) and `ApplicableRange` (applicable range for the quota item) of the target quota in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # > - Quota applications are reviewed by the technical support team of each cloud service. To increase the approval rate, specify a reasonable requested value and provide a detailed reason when you apply for a quota increase.
        # 
        # This parameter is required.
        self.desire_value = desire_value
        # The quota dimensions.
        self.dimensions = dimensions
        # The UTC time when the quota takes effect.
        # This parameter applies only to privileges (WhiteListLabel). 
        # 
        # > An empty value indicates that the quota takes effect immediately.
        self.effective_time = effective_time
        # The language of the quota alert notification. Valid values:
        # 
        # - zh (default): Chinese.
        # - en: English.
        self.env_language = env_language
        # The UTC time when the quota expires.
        # This parameter applies only to privileges (WhiteListLabel). 
        # 
        # > An empty value indicates that no UTC expiration time is specified.
        self.expire_time = expire_time
        # Specifies whether to send a notification for the quota application result. Valid values:
        # - 0 (default): No.
        # - 3: Yes.
        self.notice_type = notice_type
        # The abbreviation of the cloud service.
        # 
        # > For information about how to obtain the abbreviation of a cloud service, see `ProductCode` in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        # 
        # This parameter is required.
        self.product_code = product_code
        # The quota ID.
        # 
        # > For information about how to obtain the quota ID of a cloud service, see `QuotaActionCode` in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # 
        # This parameter is required.
        self.quota_action_code = quota_action_code
        # The quota category. Valid values:
        # - CommonQuota: general quota.
        # - WhiteListLabel: privilege.
        # - FlowControl: API rate limit.
        self.quota_category = quota_category

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.CreateTemplateQuotaItemRequestDimensions()
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

        return self

class CreateTemplateQuotaItemRequestDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # > - The value range of N depends on the number of dimensions supported by the cloud service.
        # > - If `ProductCode` is `ecs`, `ecs-spec`, `actiontrail`, or `ess`, you must specify both the key and the value of the quota dimension.
        self.key = key
        # The value of the quota dimension.
        # 
        # > - The value range of N depends on the number of dimensions supported by the cloud service.
        # > - If `ProductCode` is `ecs`, `ecs-spec`, `actiontrail`, or `ess`, you must specify both the key and the value of the quota dimension.
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

