# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListOpaClusterStrategyNewRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        image_name: List[str] = None,
        label: List[str] = None,
        page_size: int = None,
        strategy_name: List[str] = None,
    ):
        # The page number.
        self.current_page = current_page
        # The image names.
        self.image_name = image_name
        # The tags that are added to the container.
        self.label = label
        # The number of entries per page.
        self.page_size = page_size
        # The rule names.
        self.strategy_name = strategy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.label is not None:
            result['Label'] = self.label

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        return self

