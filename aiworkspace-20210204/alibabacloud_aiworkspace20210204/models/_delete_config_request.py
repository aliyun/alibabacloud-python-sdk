# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteConfigRequest(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        labels: str = None,
    ):
        # The classification of the configuration item. The following classifications are supported:
        # 
        # - DLCAutoRecycle: The DLC automatic release configuration.
        # 
        # - DLCPriorityConfig: The DLC priority settings.
        # 
        # - DSWPriorityConfig: The DSW priority settings.
        # 
        # - QuotaMaximumDuration: The maximum runtime configuration of a DLC task for a quota.
        # 
        # - CommonTagConfig: The tag settings.
        self.category_name = category_name
        # The filter conditions. Separate multiple conditions with commas. The conditions are combined with a logical AND.
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.labels is not None:
            result['Labels'] = self.labels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        return self

