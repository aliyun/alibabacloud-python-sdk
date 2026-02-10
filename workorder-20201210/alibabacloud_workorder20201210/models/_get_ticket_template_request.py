# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTicketTemplateRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        cna: str = None,
        distribution_channel: str = None,
        referrer: str = None,
        sub_distribution_channel: str = None,
        xgateway_extend_info: str = None,
    ):
        # This parameter is required.
        self.category_id = category_id
        self.cna = cna
        self.distribution_channel = distribution_channel
        self.referrer = referrer
        self.sub_distribution_channel = sub_distribution_channel
        self.xgateway_extend_info = xgateway_extend_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.cna is not None:
            result['Cna'] = self.cna

        if self.distribution_channel is not None:
            result['DistributionChannel'] = self.distribution_channel

        if self.referrer is not None:
            result['Referrer'] = self.referrer

        if self.sub_distribution_channel is not None:
            result['SubDistributionChannel'] = self.sub_distribution_channel

        if self.xgateway_extend_info is not None:
            result['XGatewayExtendInfo'] = self.xgateway_extend_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Cna') is not None:
            self.cna = m.get('Cna')

        if m.get('DistributionChannel') is not None:
            self.distribution_channel = m.get('DistributionChannel')

        if m.get('Referrer') is not None:
            self.referrer = m.get('Referrer')

        if m.get('SubDistributionChannel') is not None:
            self.sub_distribution_channel = m.get('SubDistributionChannel')

        if m.get('XGatewayExtendInfo') is not None:
            self.xgateway_extend_info = m.get('XGatewayExtendInfo')

        return self

