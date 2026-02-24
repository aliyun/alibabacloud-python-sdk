# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListCompliancePacksRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        risk_level: int = None,
        status: str = None,
        tag: List[main_models.ListCompliancePacksRequestTag] = None,
    ):
        # The page number.
        # 
        # Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The risk level of the compliance pack. Valid values:
        # 
        # - 1: high risk.
        # 
        # - 2: medium risk.
        # 
        # - 3: low risk.
        self.risk_level = risk_level
        # The status of the compliance pack. Valid values:
        # 
        # - ACTIVE: The compliance pack is active.
        # 
        # - CREATING: The compliance pack is being created.
        self.status = status
        # The tags of the resource.
        # 
        # You can attach up to 20 tags to a resource.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListCompliancePacksRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListCompliancePacksRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # You can attach up to 20 tag keys to a resource.
        self.key = key
        # The tag value of the resource.
        # 
        # You can attach up to 20 tag values to a resource.
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

