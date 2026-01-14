# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTemplateAllRulesRequest(DaraModel):
    def __init__(
        self,
        feature_type: int = None,
        lang: str = None,
        template_id: int = None,
    ):
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language type for the request and response, default is **zh_cn**. Values:
        # - **zh_cn**: Chinese.
        # - **en_us**: English.
        self.lang = lang
        # Industry template ID.
        # 
        # > You can obtain the industry template ID by calling [DescribeCategoryTemplateList](https://help.aliyun.com/document_detail/2399296.html). If this parameter is not provided, the model list of the primary template will be returned by default.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

