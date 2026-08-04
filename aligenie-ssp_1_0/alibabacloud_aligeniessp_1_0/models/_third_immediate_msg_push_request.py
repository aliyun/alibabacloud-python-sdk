# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ThirdImmediateMsgPushRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        change_detail: str = None,
        order_id: str = None,
        psg_ids: str = None,
        source: str = None,
        traffic_change_type: str = None,
        traffic_change_type_desc: str = None,
        traffic_journey_ids: str = None,
        traffic_sub_order_ids: str = None,
        user_id: str = None,
    ):
        # Business type (FLIGHT: flight, TRAIN: train)
        self.biz_type = biz_type
        # Change details (JSON-formatted change data)
        self.change_detail = change_detail
        # Order ID
        self.order_id = order_id
        # Passenger IDs to change
        self.psg_ids = psg_ids
        # Request source
        self.source = source
        # change type (TRAIN_ISSUED, FLIGHT_CHANGED)
        self.traffic_change_type = traffic_change_type
        # change type description (ticket issued, rebooked)
        self.traffic_change_type_desc = traffic_change_type_desc
        # Journey IDs to change
        self.traffic_journey_ids = traffic_journey_ids
        # sub-order ID of the changed train request
        self.traffic_sub_order_ids = traffic_sub_order_ids
        # user ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.change_detail is not None:
            result['ChangeDetail'] = self.change_detail

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.psg_ids is not None:
            result['PsgIds'] = self.psg_ids

        if self.source is not None:
            result['Source'] = self.source

        if self.traffic_change_type is not None:
            result['TrafficChangeType'] = self.traffic_change_type

        if self.traffic_change_type_desc is not None:
            result['TrafficChangeTypeDesc'] = self.traffic_change_type_desc

        if self.traffic_journey_ids is not None:
            result['TrafficJourneyIds'] = self.traffic_journey_ids

        if self.traffic_sub_order_ids is not None:
            result['TrafficSubOrderIds'] = self.traffic_sub_order_ids

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ChangeDetail') is not None:
            self.change_detail = m.get('ChangeDetail')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PsgIds') is not None:
            self.psg_ids = m.get('PsgIds')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TrafficChangeType') is not None:
            self.traffic_change_type = m.get('TrafficChangeType')

        if m.get('TrafficChangeTypeDesc') is not None:
            self.traffic_change_type_desc = m.get('TrafficChangeTypeDesc')

        if m.get('TrafficJourneyIds') is not None:
            self.traffic_journey_ids = m.get('TrafficJourneyIds')

        if m.get('TrafficSubOrderIds') is not None:
            self.traffic_sub_order_ids = m.get('TrafficSubOrderIds')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

