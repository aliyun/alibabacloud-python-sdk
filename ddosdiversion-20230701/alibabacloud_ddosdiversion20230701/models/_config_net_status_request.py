# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfigNetStatusRequest(DaraModel):
    def __init__(
        self,
        net: str = None,
        regions: List[str] = None,
        sale_id: str = None,
        status: str = None,
        sub_nets: List[str] = None,
    ):
        # The CIDR block of the anti-DDoS diversion instance.
        # 
        # This parameter is required.
        self.net = net
        # The regions in which the CIDR block needs to be advertised or withdrawn from advertising. If you leave this parameter empty, the CIDR blocks in all regions are configured.
        # 
        # > You can call the [QueryNetList](https://help.aliyun.com/document_detail/2639086.html) operation to obtain the regions of the CIDR blocks.
        self.regions = regions
        # The ID of the anti-DDoS diversion instance.
        # 
        # This parameter is required.
        self.sale_id = sale_id
        # The status of the CIDR block. Valid values:
        # 
        # - enable: advertises the CIDR block.
        # 
        # - disable: withdraws the advertising of the CIDR block.
        # 
        # This parameter is required.
        self.status = status
        # The subnet CIDR blocks of the CIDR block.
        self.sub_nets = sub_nets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.net is not None:
            result['Net'] = self.net

        if self.regions is not None:
            result['Regions'] = self.regions

        if self.sale_id is not None:
            result['SaleId'] = self.sale_id

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_nets is not None:
            result['SubNets'] = self.sub_nets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Net') is not None:
            self.net = m.get('Net')

        if m.get('Regions') is not None:
            self.regions = m.get('Regions')

        if m.get('SaleId') is not None:
            self.sale_id = m.get('SaleId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubNets') is not None:
            self.sub_nets = m.get('SubNets')

        return self

