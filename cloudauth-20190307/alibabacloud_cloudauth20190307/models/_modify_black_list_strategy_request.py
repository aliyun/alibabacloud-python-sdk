# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class ModifyBlackListStrategyRequest(DaraModel):
    def __init__(
        self,
        black_list_strategy: main_models.ModifyBlackListStrategyRequestBlackListStrategy = None,
        region_id: str = None,
    ):
        # The blacklist rule.
        self.black_list_strategy = black_list_strategy
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.black_list_strategy:
            self.black_list_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_list_strategy is not None:
            result['BlackListStrategy'] = self.black_list_strategy.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackListStrategy') is not None:
            temp_model = main_models.ModifyBlackListStrategyRequestBlackListStrategy()
            self.black_list_strategy = temp_model.from_map(m.get('BlackListStrategy'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyBlackListStrategyRequestBlackListStrategy(DaraModel):
    def __init__(
        self,
        biz_content: str = None,
        biz_key: str = None,
        id: int = None,
        product_name: str = None,
        status: str = None,
    ):
        # The blacklist string. Separate multiple entries with commas (,).
        self.biz_content = biz_content
        # The blacklist type. Valid values:
        # - **mobile**: mobile number blacklist.
        # - **ip**: IP blacklist.
        # - **identifyNum**: ID card blacklist.
        # - **bankCard**: bank card blacklist.
        self.biz_key = biz_key
        # The rule ID. Valid values:
        # - **Empty**: creates a rule.
        # - **Not empty**: modifies a rule.
        self.id = id
        # The product name. Valid values:
        # - **id2meta**: ID card two-element verification.
        # - **mobile3Meta**: mobile number element verification.
        # - **bankcardMeta**: bank card element verification.
        self.product_name = product_name
        # The authentication status. Valid values:
        # - **1**: Authentication passed.
        # - **2**: Authentication failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_content is not None:
            result['BizContent'] = self.biz_content

        if self.biz_key is not None:
            result['BizKey'] = self.biz_key

        if self.id is not None:
            result['Id'] = self.id

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizContent') is not None:
            self.biz_content = m.get('BizContent')

        if m.get('BizKey') is not None:
            self.biz_key = m.get('BizKey')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

