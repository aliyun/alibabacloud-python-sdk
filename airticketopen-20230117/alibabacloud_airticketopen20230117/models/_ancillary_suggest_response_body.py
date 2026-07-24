# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class AncillarySuggestResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.AncillarySuggestResponseBodyData = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned with the error.
        self.error_data = error_data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. The value is always 200 for successful requests.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_data is not None:
            result['error_data'] = self.error_data

        if self.error_msg is not None:
            result['error_msg'] = self.error_msg

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            temp_model = main_models.AncillarySuggestResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')

        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class AncillarySuggestResponseBodyData(DaraModel):
    def __init__(
        self,
        seg_ancillary_map_list: List[main_models.AncillarySuggestResponseBodyDataSegAncillaryMapList] = None,
        solution_id: str = None,
    ):
        # The mapping between flights and ancillary products.
        self.seg_ancillary_map_list = seg_ancillary_map_list
        # The solution_id of the flight.
        self.solution_id = solution_id

    def validate(self):
        if self.seg_ancillary_map_list:
            for v1 in self.seg_ancillary_map_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['seg_ancillary_map_list'] = []
        if self.seg_ancillary_map_list is not None:
            for k1 in self.seg_ancillary_map_list:
                result['seg_ancillary_map_list'].append(k1.to_map() if k1 else None)

        if self.solution_id is not None:
            result['solution_id'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.seg_ancillary_map_list = []
        if m.get('seg_ancillary_map_list') is not None:
            for k1 in m.get('seg_ancillary_map_list'):
                temp_model = main_models.AncillarySuggestResponseBodyDataSegAncillaryMapList()
                self.seg_ancillary_map_list.append(temp_model.from_map(k1))

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

class AncillarySuggestResponseBodyDataSegAncillaryMapList(DaraModel):
    def __init__(
        self,
        ancillary: main_models.AncillarySuggestResponseBodyDataSegAncillaryMapListAncillary = None,
        segment_id_list: List[str] = None,
    ):
        # The ancillary product.
        self.ancillary = ancillary
        # The list of segment IDs. These segments share the same ancillary product.
        self.segment_id_list = segment_id_list

    def validate(self):
        if self.ancillary:
            self.ancillary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ancillary is not None:
            result['ancillary'] = self.ancillary.to_map()

        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ancillary') is not None:
            temp_model = main_models.AncillarySuggestResponseBodyDataSegAncillaryMapListAncillary()
            self.ancillary = temp_model.from_map(m.get('ancillary'))

        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')

        return self

class AncillarySuggestResponseBodyDataSegAncillaryMapListAncillary(DaraModel):
    def __init__(
        self,
        ancillary_id: str = None,
        ancillary_type: int = None,
        baggage_ancillary: main_models.AncillarySuggestResponseBodyDataSegAncillaryMapListAncillaryBaggageAncillary = None,
    ):
        # The ancillary product ID.
        self.ancillary_id = ancillary_id
        # The ancillary product type. Currently supported value: 4 (paid baggage).
        self.ancillary_type = ancillary_type
        # The baggage ancillary details.
        self.baggage_ancillary = baggage_ancillary

    def validate(self):
        if self.baggage_ancillary:
            self.baggage_ancillary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ancillary_id is not None:
            result['ancillary_id'] = self.ancillary_id

        if self.ancillary_type is not None:
            result['ancillary_type'] = self.ancillary_type

        if self.baggage_ancillary is not None:
            result['baggage_ancillary'] = self.baggage_ancillary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ancillary_id') is not None:
            self.ancillary_id = m.get('ancillary_id')

        if m.get('ancillary_type') is not None:
            self.ancillary_type = m.get('ancillary_type')

        if m.get('baggage_ancillary') is not None:
            temp_model = main_models.AncillarySuggestResponseBodyDataSegAncillaryMapListAncillaryBaggageAncillary()
            self.baggage_ancillary = temp_model.from_map(m.get('baggage_ancillary'))

        return self

class AncillarySuggestResponseBodyDataSegAncillaryMapListAncillaryBaggageAncillary(DaraModel):
    def __init__(
        self,
        baggage_amount: int = None,
        baggage_weight: int = None,
        baggage_weight_unit: str = None,
        is_all_weight: bool = None,
        price: float = None,
    ):
        # The number of baggage pieces. Valid values: 3, 2, 1, 0, and -2. A value of -2 indicates weight-based calculation.
        self.baggage_amount = baggage_amount
        # The baggage weight, ranging from 0 to 50. If isAllWeight is set to true, this value represents the total weight of all pieces.
        self.baggage_weight = baggage_weight
        # The unit of baggage weight.
        self.baggage_weight_unit = baggage_weight_unit
        # Indicates whether the weight represents the total weight of all baggage pieces.
        self.is_all_weight = is_all_weight
        # The total price.
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_amount is not None:
            result['baggage_amount'] = self.baggage_amount

        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight

        if self.baggage_weight_unit is not None:
            result['baggage_weight_unit'] = self.baggage_weight_unit

        if self.is_all_weight is not None:
            result['is_all_weight'] = self.is_all_weight

        if self.price is not None:
            result['price'] = self.price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_amount') is not None:
            self.baggage_amount = m.get('baggage_amount')

        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')

        if m.get('baggage_weight_unit') is not None:
            self.baggage_weight_unit = m.get('baggage_weight_unit')

        if m.get('is_all_weight') is not None:
            self.is_all_weight = m.get('is_all_weight')

        if m.get('price') is not None:
            self.price = m.get('price')

        return self

