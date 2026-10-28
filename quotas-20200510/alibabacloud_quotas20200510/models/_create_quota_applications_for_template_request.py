# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class CreateQuotaApplicationsForTemplateRequest(DaraModel):
    def __init__(
        self,
        aliyun_uids: List[str] = None,
        desire_value: float = None,
        dimensions: List[main_models.CreateQuotaApplicationsForTemplateRequestDimensions] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        notice_type: int = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        reason: str = None,
    ):
        # The list of Alibaba Cloud accounts that belong to the resource directory members for which you want to apply for quotas.
        # 
        # > You can apply for quota increases for a maximum of 50 members at a time. For more information about the members of a resource directory, see [ListAccounts](https://help.aliyun.com/document_detail/604207.html).
        # 
        # This parameter is required.
        self.aliyun_uids = aliyun_uids
        # The requested quota value.
        # 
        # > - Set the requested quota value based on the `TotalUsage` (quota usage) and `ApplicableRange` (applicable range for quota application) of the target quota in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # > - Quota applications are reviewed and approved by the technical support team of each cloud service. To increase the approval rate, specify a reasonable requested value and provide a detailed reason when you submit a quota application.
        # 
        # This parameter is required.
        self.desire_value = desire_value
        # The quota dimensions.
        self.dimensions = dimensions
        # The UTC time when the quota takes effect. This parameter applies only to privileges (WhiteListLabel).
        #  
        # > If you do not specify an effective period for the current account, the commit time is used by default.
        self.effective_time = effective_time
        # The language of the notification for the quota application result. Valid values:
        # 
        # - zh (default): Chinese.
        # - en: English.
        self.env_language = env_language
        # The UTC time when the quota expires. This parameter applies only to privileges (WhiteListLabel). 
        # 
        # > If you do not specify an expiration time for the current account, the expiration time is set to 99 years after the effective period of the current quota.
        self.expire_time = expire_time
        # Specifies whether to send notifications for quota application results. Valid values:
        # 
        # - 0 (default): no.
        # - 3: yes.
        self.notice_type = notice_type
        # The abbreviated name of the cloud service.
        # 
        # > For more information about how to obtain the abbreviated name of a cloud service, see `ProductCode` in [ListProducts](https://help.aliyun.com/document_detail/440555.html).
        # 
        # This parameter is required.
        self.product_code = product_code
        # The quota ID.
        # 
        # > For more information about how to obtain the quota ID of a cloud service, see `QuotaActionCode` in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # 
        # This parameter is required.
        self.quota_action_code = quota_action_code
        # The quota type. Valid values:
        # - CommonQuota: general quota.
        # - FlowControl: API rate limit.
        # - WhiteListLabel: privilege.
        # 
        # This parameter is required.
        self.quota_category = quota_category
        # The reason for the quota application.
        # 
        # > Quota applications are reviewed and approved by the technical support team of each cloud service. To increase the approval rate, specify a reasonable requested value and provide a detailed reason when you submit a quota application.
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
        if self.aliyun_uids is not None:
            result['AliyunUids'] = self.aliyun_uids

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
        if m.get('AliyunUids') is not None:
            self.aliyun_uids = m.get('AliyunUids')

        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')

        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k1 in m.get('Dimensions'):
                temp_model = main_models.CreateQuotaApplicationsForTemplateRequestDimensions()
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

class CreateQuotaApplicationsForTemplateRequestDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # > - The value range of N depends on the number of dimensions supported by the cloud service.
        # > - When `ProductCode` is set to `ecs`, `ecs-spec`, `actiontrail`, or `ess`, you must specify both the key and the value of the quota dimension.
        self.key = key
        # The value of the quota dimension.
        # 
        # > - The value range of N depends on the number of dimensions supported by the cloud service.
        # > - When `ProductCode` is set to `ecs`, `ecs-spec`, `actiontrail`, or `ess`, you must specify both the key and the value of the quota dimension.
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

