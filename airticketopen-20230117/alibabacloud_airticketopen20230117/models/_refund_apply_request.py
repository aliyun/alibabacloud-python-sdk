# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class RefundApplyRequest(DaraModel):
    def __init__(
        self,
        order_num: int = None,
        refund_journeys: List[main_models.RefundApplyRequestRefundJourneys] = None,
        refund_passenger_list: List[main_models.RefundApplyRequestRefundPassengerList] = None,
        refund_type: main_models.RefundApplyRequestRefundType = None,
    ):
        # The order number.
        # 
        # This parameter is required.
        self.order_num = order_num
        # The journeys for the refund application.
        # 
        # This parameter is required.
        self.refund_journeys = refund_journeys
        # The list of passengers for the refund application.
        # 
        # This parameter is required.
        self.refund_passenger_list = refund_passenger_list
        # The refund type. Attachments are required for involuntary refund applications.
        # 
        # This parameter is required.
        self.refund_type = refund_type

    def validate(self):
        if self.refund_journeys:
            for v1 in self.refund_journeys:
                 if v1:
                    v1.validate()
        if self.refund_passenger_list:
            for v1 in self.refund_passenger_list:
                 if v1:
                    v1.validate()
        if self.refund_type:
            self.refund_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_num is not None:
            result['order_num'] = self.order_num

        result['refund_journeys'] = []
        if self.refund_journeys is not None:
            for k1 in self.refund_journeys:
                result['refund_journeys'].append(k1.to_map() if k1 else None)

        result['refund_passenger_list'] = []
        if self.refund_passenger_list is not None:
            for k1 in self.refund_passenger_list:
                result['refund_passenger_list'].append(k1.to_map() if k1 else None)

        if self.refund_type is not None:
            result['refund_type'] = self.refund_type.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        self.refund_journeys = []
        if m.get('refund_journeys') is not None:
            for k1 in m.get('refund_journeys'):
                temp_model = main_models.RefundApplyRequestRefundJourneys()
                self.refund_journeys.append(temp_model.from_map(k1))

        self.refund_passenger_list = []
        if m.get('refund_passenger_list') is not None:
            for k1 in m.get('refund_passenger_list'):
                temp_model = main_models.RefundApplyRequestRefundPassengerList()
                self.refund_passenger_list.append(temp_model.from_map(k1))

        if m.get('refund_type') is not None:
            temp_model = main_models.RefundApplyRequestRefundType()
            self.refund_type = temp_model.from_map(m.get('refund_type'))

        return self

class RefundApplyRequestRefundType(DaraModel):
    def __init__(
        self,
        file: List[str] = None,
        refund_type_id: int = None,
        remark: str = None,
    ):
        # The array of attachment file URLs. Upload files first by using the dedicated file upload operation to obtain the file URLs.
        self.file = file
        # The refund type. Valid values:
        # - 2: Voluntary refund (change of travel plans or decision not to fly).
        # - 5: Involuntary refund due to airline reasons such as flight delay, cancellation, or schedule change.
        # - 6: Involuntary refund due to medical reasons with a certificate from a Grade II Class A hospital or above.
        # 
        # Note: Attachments are not mandatory, but providing attachments for involuntary refunds can improve the success rate of the refund application.
        # 
        # This parameter is required.
        self.refund_type_id = refund_type_id
        # The remarks.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file is not None:
            result['file'] = self.file

        if self.refund_type_id is not None:
            result['refund_type_id'] = self.refund_type_id

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file') is not None:
            self.file = m.get('file')

        if m.get('refund_type_id') is not None:
            self.refund_type_id = m.get('refund_type_id')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

class RefundApplyRequestRefundPassengerList(DaraModel):
    def __init__(
        self,
        document: str = None,
        first_name: str = None,
        last_name: str = None,
    ):
        # The document number of the passenger.
        self.document = document
        # The first name of the passenger.
        # 
        # This parameter is required.
        self.first_name = first_name
        # The last name of the passenger.
        # 
        # This parameter is required.
        self.last_name = last_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.last_name is not None:
            result['last_name'] = self.last_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        return self

class RefundApplyRequestRefundJourneys(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.RefundApplyRequestRefundJourneysSegmentList] = None,
    ):
        # The segment information.
        # 
        # This parameter is required.
        self.segment_list = segment_list

    def validate(self):
        if self.segment_list:
            for v1 in self.segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['segment_list'] = []
        if self.segment_list is not None:
            for k1 in self.segment_list:
                result['segment_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k1 in m.get('segment_list'):
                temp_model = main_models.RefundApplyRequestRefundJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        return self

class RefundApplyRequestRefundJourneysSegmentList(DaraModel):
    def __init__(
        self,
        arrival_airport: str = None,
        arrival_city: str = None,
        departure_airport: str = None,
        departure_city: str = None,
    ):
        # The three-letter IATA code of the arrival airport (uppercase).
        # 
        # This parameter is required.
        self.arrival_airport = arrival_airport
        # The three-letter IATA code of the arrival city (uppercase).
        # 
        # This parameter is required.
        self.arrival_city = arrival_city
        # The three-letter IATA code of the departure airport (uppercase).
        # 
        # This parameter is required.
        self.departure_airport = departure_airport
        # The three-letter IATA code of the departure city (uppercase).
        # 
        # This parameter is required.
        self.departure_city = departure_city

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport

        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city

        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport

        if self.departure_city is not None:
            result['departure_city'] = self.departure_city

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')

        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')

        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')

        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')

        return self

