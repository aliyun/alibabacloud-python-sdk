# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConfigRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        feature_type: int = None,
        lang: str = None,
        source_ip: str = None,
        value: str = None,
    ):
        # The code of the common configuration item. Valid values:
        # 
        # *   **access_failed_cnt**: the maximum number of access attempts allowed when Data Security Center (DSC) fails to access an unauthorized resource.
        # *   **access_permission_exprie_max_days**: the maximum idle period allowed for access permissions before an alert is triggered.
        # *   **log_datasize_avg_days**: the minimum percentage of the volume of logs of a specific type generated on the current day to the average volume of logs generated in the previous 10 days before an alert is triggered.
        self.code = code
        # The description of the common configuration item.
        self.description = description
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang
        # This parameter is deprecated.
        self.source_ip = source_ip
        # The value of the common configuration item. The meaning of this parameter varies with the value of the Code parameter.
        # 
        # *   If you set the Code parameter to **access_failed_cnt**, the Value parameter specifies the maximum number of access attempts allowed when DSC fails to access an unauthorized resource.
        # *   If you set the Code parameter to **access_permission_exprie_max_days**, the Value parameter specifies the maximum idle period allowed for access permissions before an alert is triggered.
        # *   If you set the Code parameter to **log_datasize_avg_days**, the Value parameter specifies the minimum percentage of the volume of logs of a specific type generated on the current day to the average amount of logs generated in the previous 10 days before an alert is triggered.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

