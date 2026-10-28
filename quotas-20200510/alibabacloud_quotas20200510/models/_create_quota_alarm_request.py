# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quotas20200510 import models as main_models
from darabonba.model import DaraModel

class CreateQuotaAlarmRequest(DaraModel):
    def __init__(
        self,
        alarm_name: str = None,
        original_context: str = None,
        product_code: str = None,
        quota_action_code: str = None,
        quota_dimensions: List[main_models.CreateQuotaAlarmRequestQuotaDimensions] = None,
        threshold: float = None,
        threshold_percent: float = None,
        threshold_type: str = None,
        web_hook: str = None,
    ):
        # The name of the quota alert rule.
        # 
        # This parameter is required.
        self.alarm_name = alarm_name
        # The original context information.
        self.original_context = original_context
        # The abbreviation of the cloud service.
        # 
        # > For more information about how to obtain the abbreviation of a cloud service, see ProductCode in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # 
        # This parameter is required.
        self.product_code = product_code
        # The quota ID.
        # 
        # > For more information about how to obtain the quota ID of a cloud service, see QuotaActionCode in [ListProductQuotas](https://help.aliyun.com/document_detail/440554.html).
        # 
        # This parameter is required.
        self.quota_action_code = quota_action_code
        # The quota dimensions.
        # The dimensions are properties of a quota item. A quota item is uniquely identified by Dimensions and QuotaActionCode.
        # > Some dimensions are required for specific cloud services. You can call the [ListProductQuotaDimensions](https://help.aliyun.com/document_detail/440553.html) operation to query the supported quota dimensions of a cloud service. The Requisite response parameter indicates whether a dimension is required.
        self.quota_dimensions = quota_dimensions
        # The numeric value of the quota alert threshold. Valid values:
        # 
        # - If ThresholdType is set to used, you receive an alert notification when the used quota is greater than or equal to the specified value. The quota alert threshold must be greater than the used quota.
        # 
        # - If ThresholdType is set to usable, you receive an alert notification when the available quota is less than or equal to the specified value. The quota alert threshold must be less than the available quota.
        # 
        # > You must specify either this parameter or ThresholdPercent.
        self.threshold = threshold
        # The percentage of the quota alert threshold. Valid values:
        # 
        # - If ThresholdType is set to used, you receive an alert notification when the used quota is greater than or equal to the specified percentage. Valid values: (50%, 100%].
        # 
        # - If ThresholdType is set to usable, you receive an alert notification when the available quota is less than or equal to the specified percentage. Valid values: (0%, 50%].
        # 
        # > You must specify either this parameter or Threshold.
        self.threshold_percent = threshold_percent
        # The quota alert type. Valid values:
        # 
        # - used: alerts on the used quota. This is the default value.
        # - usable: alerts on the remaining available quota.
        self.threshold_type = threshold_type
        # The public URL to which Quota Center sends alert notifications by using HTTP POST requests.
        self.web_hook = web_hook

    def validate(self):
        if self.quota_dimensions:
            for v1 in self.quota_dimensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_name is not None:
            result['AlarmName'] = self.alarm_name

        if self.original_context is not None:
            result['OriginalContext'] = self.original_context

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.quota_action_code is not None:
            result['QuotaActionCode'] = self.quota_action_code

        result['QuotaDimensions'] = []
        if self.quota_dimensions is not None:
            for k1 in self.quota_dimensions:
                result['QuotaDimensions'].append(k1.to_map() if k1 else None)

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent

        if self.threshold_type is not None:
            result['ThresholdType'] = self.threshold_type

        if self.web_hook is not None:
            result['WebHook'] = self.web_hook

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmName') is not None:
            self.alarm_name = m.get('AlarmName')

        if m.get('OriginalContext') is not None:
            self.original_context = m.get('OriginalContext')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('QuotaActionCode') is not None:
            self.quota_action_code = m.get('QuotaActionCode')

        self.quota_dimensions = []
        if m.get('QuotaDimensions') is not None:
            for k1 in m.get('QuotaDimensions'):
                temp_model = main_models.CreateQuotaAlarmRequestQuotaDimensions()
                self.quota_dimensions.append(temp_model.from_map(k1))

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        if m.get('ThresholdType') is not None:
            self.threshold_type = m.get('ThresholdType')

        if m.get('WebHook') is not None:
            self.web_hook = m.get('WebHook')

        return self



class CreateQuotaAlarmRequestQuotaDimensions(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the quota dimension.
        # 
        # > You must specify both Dimensions.N.Key and Dimensions.N.Value. The value range of N depends on the number of dimensions supported by the cloud service. You can call the [ListProductQuotaDimensions](https://help.aliyun.com/document_detail/440553.html) operation to query the supported quota dimensions. The length of the returned array is the maximum value of N.
        self.key = key
        # The value of the quota dimension.
        # 
        #  > You must specify both Dimensions.N.Key and Dimensions.N.Value. The value range of N depends on the number of dimensions supported by the cloud service. You can call the [ListProductQuotaDimensions](https://help.aliyun.com/document_detail/440553.html) operation to query the supported quota dimensions. The length of the returned array is the maximum value of N.
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

