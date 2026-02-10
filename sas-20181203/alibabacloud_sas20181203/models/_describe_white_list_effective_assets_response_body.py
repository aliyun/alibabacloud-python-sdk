# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWhiteListEffectiveAssetsResponseBody(DaraModel):
    def __init__(
        self,
        assets: List[main_models.DescribeWhiteListEffectiveAssetsResponseBodyAssets] = None,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The servers on which the policy takes effect.
        self.assets = assets
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of the servers on which the policy takes effect.
        self.total_count = total_count

    def validate(self):
        if self.assets:
            for v1 in self.assets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Assets'] = []
        if self.assets is not None:
            for k1 in self.assets:
                result['Assets'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assets = []
        if m.get('Assets') is not None:
            for k1 in m.get('Assets'):
                temp_model = main_models.DescribeWhiteListEffectiveAssetsResponseBodyAssets()
                self.assets.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWhiteListEffectiveAssetsResponseBodyAssets(DaraModel):
    def __init__(
        self,
        internet_ip: str = None,
        intranet_ip: str = None,
        machine_name: str = None,
        process_method: int = None,
        strategy_id: int = None,
        strategy_name: str = None,
        suspicious_event_count: int = None,
        uuid: str = None,
    ):
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address.
        self.intranet_ip = intranet_ip
        # The name of the server.
        self.machine_name = machine_name
        # The exception handling mode. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: alerted
        # *   **2**: blocked
        self.process_method = process_method
        # The ID of the policy.
        self.strategy_id = strategy_id
        # The name of the policy.
        self.strategy_name = strategy_name
        # The number of **untrusted programs** on the server.
        self.suspicious_event_count = suspicious_event_count
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.process_method is not None:
            result['ProcessMethod'] = self.process_method

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.suspicious_event_count is not None:
            result['SuspiciousEventCount'] = self.suspicious_event_count

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('ProcessMethod') is not None:
            self.process_method = m.get('ProcessMethod')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('SuspiciousEventCount') is not None:
            self.suspicious_event_count = m.get('SuspiciousEventCount')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

