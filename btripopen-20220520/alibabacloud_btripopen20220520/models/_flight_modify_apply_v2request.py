# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightModifyApplyV2Request(DaraModel):
    def __init__(
        self,
        cache_key: str = None,
        contact_phone: str = None,
        isv_name: str = None,
        item_id: str = None,
        order_id: int = None,
        out_order_id: str = None,
        out_sub_order_id: str = None,
        passenger_segment_relations: List[main_models.FlightModifyApplyV2RequestPassengerSegmentRelations] = None,
        reason: str = None,
        session_id: str = None,
        voluntary: bool = None,
    ):
        self.cache_key = cache_key
        self.contact_phone = contact_phone
        self.isv_name = isv_name
        self.item_id = item_id
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_sub_order_id = out_sub_order_id
        self.passenger_segment_relations = passenger_segment_relations
        self.reason = reason
        # sessionId
        self.session_id = session_id
        self.voluntary = voluntary

    def validate(self):
        if self.passenger_segment_relations:
            for v1 in self.passenger_segment_relations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_key is not None:
            result['cache_key'] = self.cache_key

        if self.contact_phone is not None:
            result['contact_phone'] = self.contact_phone

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_sub_order_id is not None:
            result['out_sub_order_id'] = self.out_sub_order_id

        result['passenger_segment_relations'] = []
        if self.passenger_segment_relations is not None:
            for k1 in self.passenger_segment_relations:
                result['passenger_segment_relations'].append(k1.to_map() if k1 else None)

        if self.reason is not None:
            result['reason'] = self.reason

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.voluntary is not None:
            result['voluntary'] = self.voluntary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cache_key') is not None:
            self.cache_key = m.get('cache_key')

        if m.get('contact_phone') is not None:
            self.contact_phone = m.get('contact_phone')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_sub_order_id') is not None:
            self.out_sub_order_id = m.get('out_sub_order_id')

        self.passenger_segment_relations = []
        if m.get('passenger_segment_relations') is not None:
            for k1 in m.get('passenger_segment_relations'):
                temp_model = main_models.FlightModifyApplyV2RequestPassengerSegmentRelations()
                self.passenger_segment_relations.append(temp_model.from_map(k1))

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('voluntary') is not None:
            self.voluntary = m.get('voluntary')

        return self

class FlightModifyApplyV2RequestPassengerSegmentRelations(DaraModel):
    def __init__(
        self,
        passenger_id: str = None,
        segment_id_list: List[str] = None,
    ):
        self.passenger_id = passenger_id
        self.segment_id_list = segment_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')

        return self

