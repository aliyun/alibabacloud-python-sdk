# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SuggestCategoryRequest(DaraModel):
    def __init__(
        self,
        cna: str = None,
        content: str = None,
        distribution_channel: str = None,
        referrer: str = None,
        sub_distribution_channel: str = None,
        ticket_id: str = None,
        top_n: int = None,
        use_hot_suggest_catch_all: bool = None,
        xgateway_extend_info: str = None,
    ):
        self.cna = cna
        self.content = content
        self.distribution_channel = distribution_channel
        self.referrer = referrer
        self.sub_distribution_channel = sub_distribution_channel
        self.ticket_id = ticket_id
        self.top_n = top_n
        self.use_hot_suggest_catch_all = use_hot_suggest_catch_all
        self.xgateway_extend_info = xgateway_extend_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cna is not None:
            result['Cna'] = self.cna

        if self.content is not None:
            result['Content'] = self.content

        if self.distribution_channel is not None:
            result['DistributionChannel'] = self.distribution_channel

        if self.referrer is not None:
            result['Referrer'] = self.referrer

        if self.sub_distribution_channel is not None:
            result['SubDistributionChannel'] = self.sub_distribution_channel

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.top_n is not None:
            result['TopN'] = self.top_n

        if self.use_hot_suggest_catch_all is not None:
            result['UseHotSuggestCatchAll'] = self.use_hot_suggest_catch_all

        if self.xgateway_extend_info is not None:
            result['XGatewayExtendInfo'] = self.xgateway_extend_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cna') is not None:
            self.cna = m.get('Cna')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DistributionChannel') is not None:
            self.distribution_channel = m.get('DistributionChannel')

        if m.get('Referrer') is not None:
            self.referrer = m.get('Referrer')

        if m.get('SubDistributionChannel') is not None:
            self.sub_distribution_channel = m.get('SubDistributionChannel')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        if m.get('UseHotSuggestCatchAll') is not None:
            self.use_hot_suggest_catch_all = m.get('UseHotSuggestCatchAll')

        if m.get('XGatewayExtendInfo') is not None:
            self.xgateway_extend_info = m.get('XGatewayExtendInfo')

        return self

