# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class ListQuotaApplicationTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        quota_application_templates: List[main_models.ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of records returned for the query.
        self.max_results = max_results
        # The token that marks the position at which the query ends.
        # 
        # > An empty value indicates that all data is returned.
        self.next_token = next_token
        # The information about quota templates.
        self.quota_application_templates = quota_application_templates
        # The request ID.
        self.request_id = request_id
        # The total number of records returned for the query.
        self.total_count = total_count

    def validate(self):
        if self.quota_application_templates:
            for v1 in self.quota_application_templates:
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

        result['QuotaApplicationTemplates'] = []
        if self.quota_application_templates is not None:
            for k1 in self.quota_application_templates:
                result['QuotaApplicationTemplates'].append(k1.to_map() if k1 else None)

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

        self.quota_application_templates = []
        if m.get('QuotaApplicationTemplates') is not None:
            for k1 in m.get('QuotaApplicationTemplates'):
                temp_model = main_models.ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates()
                self.quota_application_templates.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplates(DaraModel):
    def __init__(
        self,
        applicable_range: List[float] = None,
        applicable_type: str = None,
        desire_value: float = None,
        dimensions: Dict[str, Any] = None,
        effective_time: str = None,
        env_language: str = None,
        expire_time: str = None,
        id: str = None,
        notice_type: int = None,
        period: main_models.ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplatesPeriod = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_category: str = None,
        quota_description: str = None,
        quota_name: str = None,
    ):
        # None.
        self.applicable_range = applicable_range
        # The type of the adjustable value. Valid values:
        # 
        # - continuous
        # 
        # - discontinuous
        self.applicable_type = applicable_type
        # The requested value of the quota.
        self.desire_value = desire_value
        # The quota dimensions.
        # 
        # Format: {"regionId":"Region"}.
        self.dimensions = dimensions
        # The start time of the validity period of the quota. The value is displayed in UTC.
        self.effective_time = effective_time
        # The language of the quota alert notification. Valid values:
        # 
        # - zh: Chinese
        # 
        # - en: English
        self.env_language = env_language
        # The end time of the validity period of the quota. The value is displayed in UTC.
        self.expire_time = expire_time
        # The ID of the quota template.
        self.id = id
        # Indicates whether Quota Center sends a notification about the application result. Valid values:
        # 
        # - 0: no
        # 
        # - 3: yes
        self.notice_type = notice_type
        # The calculation cycle of the quota.
        self.period = period
        # The abbreviation of the Alibaba Cloud service name.
        self.product_code = product_code
        # The ID of the quota.
        self.quota_action_code = quota_action_code
        # The type of the quota. Valid values:
        # 
        # - CommonQuota: general quota
        # 
        # - FlowControl: API rate limit
        # 
        # - WhiteListLabel: privilege
        self.quota_category = quota_category
        # The description of the quota.
        self.quota_description = quota_description
        # The name of the quota.
        self.quota_name = quota_name

    def validate(self):
        if self.period:
            self.period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable_range is not None:
            result['ApplicableRange'] = self.applicable_range

        if self.applicable_type is not None:
            result['ApplicableType'] = self.applicable_type

        if self.desire_value is not None:
            result['DesireValue'] = self.desire_value

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.env_language is not None:
            result['EnvLanguage'] = self.env_language

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.id is not None:
            result['Id'] = self.id

        if self.notice_type is not None:
            result['NoticeType'] = self.notice_type

        if self.period is not None:
            result['Period'] = self.period.to_map()

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        if self.quota_category is not None:
            result['QuotaCategory'] = self.quota_category

        if self.quota_description is not None:
            result['QuotaDescription'] = self.quota_description

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableRange') is not None:
            self.applicable_range = m.get('ApplicableRange')

        if m.get('ApplicableType') is not None:
            self.applicable_type = m.get('ApplicableType')

        if m.get('DesireValue') is not None:
            self.desire_value = m.get('DesireValue')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('EnvLanguage') is not None:
            self.env_language = m.get('EnvLanguage')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NoticeType') is not None:
            self.notice_type = m.get('NoticeType')

        if m.get('Period') is not None:
            temp_model = main_models.ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplatesPeriod()
            self.period = temp_model.from_map(m.get('Period'))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        if m.get('QuotaCategory') is not None:
            self.quota_category = m.get('QuotaCategory')

        if m.get('QuotaDescription') is not None:
            self.quota_description = m.get('QuotaDescription')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        return self

class ListQuotaApplicationTemplatesResponseBodyQuotaApplicationTemplatesPeriod(DaraModel):
    def __init__(
        self,
        period_unit: str = None,
        period_value: int = None,
    ):
        # The unit of the calculation cycle. Valid values:
        # 
        # - second
        # 
        # - minute
        # 
        # - hour
        # 
        # - day
        # 
        # - week
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

