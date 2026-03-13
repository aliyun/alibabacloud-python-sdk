# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightModifyOtaSearchV2Request(DaraModel):
    def __init__(
        self,
        cabin_class: List[int] = None,
        dep_date: List[str] = None,
        isv_name: str = None,
        order_id: int = None,
        out_order_id: str = None,
        passenger_segment_relations: List[main_models.FlightModifyOtaSearchV2RequestPassengerSegmentRelations] = None,
        selected_segments: List[main_models.FlightModifyOtaSearchV2RequestSelectedSegments] = None,
        session_id: str = None,
        voluntary: bool = None,
    ):
        self.cabin_class = cabin_class
        self.dep_date = dep_date
        self.isv_name = isv_name
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.passenger_segment_relations = passenger_segment_relations
        self.selected_segments = selected_segments
        self.session_id = session_id
        self.voluntary = voluntary

    def validate(self):
        if self.passenger_segment_relations:
            for v1 in self.passenger_segment_relations:
                 if v1:
                    v1.validate()
        if self.selected_segments:
            for v1 in self.selected_segments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        result['passenger_segment_relations'] = []
        if self.passenger_segment_relations is not None:
            for k1 in self.passenger_segment_relations:
                result['passenger_segment_relations'].append(k1.to_map() if k1 else None)

        result['selected_segments'] = []
        if self.selected_segments is not None:
            for k1 in self.selected_segments:
                result['selected_segments'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['session_id'] = self.session_id

        if self.voluntary is not None:
            result['voluntary'] = self.voluntary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        self.passenger_segment_relations = []
        if m.get('passenger_segment_relations') is not None:
            for k1 in m.get('passenger_segment_relations'):
                temp_model = main_models.FlightModifyOtaSearchV2RequestPassengerSegmentRelations()
                self.passenger_segment_relations.append(temp_model.from_map(k1))

        self.selected_segments = []
        if m.get('selected_segments') is not None:
            for k1 in m.get('selected_segments'):
                temp_model = main_models.FlightModifyOtaSearchV2RequestSelectedSegments()
                self.selected_segments.append(temp_model.from_map(k1))

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        if m.get('voluntary') is not None:
            self.voluntary = m.get('voluntary')

        return self

class FlightModifyOtaSearchV2RequestSelectedSegments(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        dep_city_code: str = None,
        dep_date_time: str = None,
        journey_seq: int = None,
        marketing_flight_no: str = None,
        operating_flight_no: str = None,
        segment_seq: int = None,
    ):
        self.arr_city_code = arr_city_code
        self.dep_city_code = dep_city_code
        self.dep_date_time = dep_date_time
        self.journey_seq = journey_seq
        self.marketing_flight_no = marketing_flight_no
        self.operating_flight_no = operating_flight_no
        self.segment_seq = segment_seq

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date_time is not None:
            result['dep_date_time'] = self.dep_date_time

        if self.journey_seq is not None:
            result['journey_seq'] = self.journey_seq

        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        if self.segment_seq is not None:
            result['segment_seq'] = self.segment_seq

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date_time') is not None:
            self.dep_date_time = m.get('dep_date_time')

        if m.get('journey_seq') is not None:
            self.journey_seq = m.get('journey_seq')

        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        if m.get('segment_seq') is not None:
            self.segment_seq = m.get('segment_seq')

        return self

class FlightModifyOtaSearchV2RequestPassengerSegmentRelations(DaraModel):
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

