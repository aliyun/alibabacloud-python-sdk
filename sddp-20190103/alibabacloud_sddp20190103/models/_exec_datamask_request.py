# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecDatamaskRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        feature_type: int = None,
        lang: str = None,
        template_id: int = None,
    ):
        # The sensitive data to be de-identified. The value is a JSON string that contains the following parameters:
        # 
        # *   **dataHeaderList**: the names of the columns in which data needs to be de-identified. Specify the column names in accordance with the order of data that needs to be de-identified.
        # *   **dataList**: the data that needs to be de-identified.
        # *   **ruleList**: the IDs of sensitive data detection rules used to detect data that needs to be de-identified. Specify the rule IDs in accordance with the order of data that needs to be de-identified. Each ID identifies a sensitive data detection rule that is used to detect a type of sensitive data. You can call the [DescribeRules](~~DescribeRules~~) operation to query the IDs of sensitive data detection rules.
        # 
        # This parameter is required.
        self.data = data
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang
        # The ID of the de-identification template. The ID is generated after you create the de-identification template in the [Data Security Center (DSC) console](https://yundun.console.aliyun.com/?\\&p=sddpnext#/sddp/dm/template). You can choose **Data desensitization** > **Desensitization Template** in the left-side navigation pane and obtain the ID of the de-identification template from the **Desensitization Template** page.
        # 
        # *   If you select **Field name** as the matching mode of the template, DSC matches data based on the columns specified by the **dataHeaderList** parameter in the **Data** parameter.
        # *   If you select **Sensitive type** as the matching mode of the template, DSC matches data based on the sensitive data detection rules specified by the **ruleList** parameter in the **Data** parameter.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

