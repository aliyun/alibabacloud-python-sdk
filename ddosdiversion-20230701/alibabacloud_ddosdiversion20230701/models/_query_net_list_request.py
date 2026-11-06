# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryNetListRequest(DaraModel):
    def __init__(
        self,
        main_net: str = None,
        mode: str = None,
        net: str = None,
        num: int = None,
        page: int = None,
        sale_id: str = None,
    ):
        # The primary CIDR block of the anti-DDoS diversion instance for which an extended CIDR block is configured. If no extended CIDR blocks are configured for the anti-DDoS diversion instance, leave this parameter empty.
        self.main_net = main_net
        # The scheduling mode. Valid values:
        # 
        # - manual: manual scheduling.
        # 
        # - netflow-auto: automatic scheduling.
        self.mode = mode
        # The CIDR block of the anti-DDoS diversion instance.
        # 
        # > If no extended CIDR blocks are configured for the anti-DDoS diversion instance, this parameter specifies the CIDR block of the instance. If an extended CIDR block is configured for the anti-DDoS diversion instance, this parameter specifies the extended CIDR block that is configured for the instance. If this parameter is specified, the MainNet parameter is required.
        self.net = net
        # The number of entries per page. Default value: 100.
        self.num = num
        # The page number. Default value: 1.
        self.page = page
        # The ID of the anti-DDoS diversion instance.
        self.sale_id = sale_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.main_net is not None:
            result['MainNet'] = self.main_net

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.net is not None:
            result['Net'] = self.net

        if self.num is not None:
            result['Num'] = self.num

        if self.page is not None:
            result['Page'] = self.page

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MainNet') is not None:
            self.main_net = m.get('MainNet')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Net') is not None:
            self.net = m.get('Net')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        return self

