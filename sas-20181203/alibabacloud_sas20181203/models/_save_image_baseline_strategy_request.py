# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveImageBaselineStrategyRequest(DaraModel):
    def __init__(
        self,
        baseline_item_list: str = None,
        image_vul_clean: int = None,
        lang: str = None,
        source: str = None,
        strategy_id: int = None,
        strategy_name: str = None,
    ):
        # The baseline check items.
        # 
        # > You can call the [DescribeImageBaselineStrategy](~~DescribeImageBaselineStrategy~~) operation to query baseline check items.
        # 
        # This parameter is required.
        self.baseline_item_list = baseline_item_list
        self.image_vul_clean = image_vul_clean
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The data source. If this parameter is left empty, the baseline check policy for images is queried. Valid values:
        # 
        # *   **default**: the baseline check policy for images
        # *   **agentless**: agentless detection
        self.source = source
        # The ID of the baseline check policy.
        # 
        # > You can call the [DescribeImageBaselineStrategy](~~DescribeImageBaselineStrategy~~) operation to query the IDs of baseline check policies.
        self.strategy_id = strategy_id
        # The name of the baseline check policy.
        self.strategy_name = strategy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_item_list is not None:
            result['BaselineItemList'] = self.baseline_item_list

        if self.image_vul_clean is not None:
            result['ImageVulClean'] = self.image_vul_clean

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source is not None:
            result['Source'] = self.source

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineItemList') is not None:
            self.baseline_item_list = m.get('BaselineItemList')

        if m.get('ImageVulClean') is not None:
            self.image_vul_clean = m.get('ImageVulClean')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

