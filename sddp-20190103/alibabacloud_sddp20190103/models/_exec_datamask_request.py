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
        # The data that you want to mask. The data must be a string in JSON format and include the following fields:
        # 
        # - **dataHeaderList**: The column names of the data. The order of the column names must correspond to the order of the data that you want to mask.
        # 
        # - **dataList**: The data that you want to mask.
        # 
        # - **ruleList**: A list of sensitive data type IDs. The order of the IDs must correspond to the order of the data that you want to mask. Each ID is a number that represents a sensitive data type. You can call the [DescribeRules](https://help.aliyun.com/document_detail/410141.html) operation to obtain the IDs.
        # 
        # This parameter is required.
        self.data = data
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Simplified Chinese
        # 
        # - **en_us**: English (US)
        self.lang = lang
        # The ID of the data masking template. A template ID is generated after you create a template in the [Data Security Center console](https://yundun.console.aliyun.com/?p=sddp#/dm/dmConfig/cn-zhangjiakou). You can find the **Template ID** on the **Data Masking** > **Masking Configuration** > **Masking Template** page.
        # 
        # - If the matching type of the data masking template is **Field Name**, the system matches the data against **dataHeaderList** in **Data**.
        # 
        # - If the matching type of the data masking template is **Sensitive Data Type**, the system matches the data against **ruleList** in **Data**.
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

