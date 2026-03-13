# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainNoListSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TrainNoListSearchResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
        self.module = module
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.TrainNoListSearchResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainNoListSearchResponseBodyModule(DaraModel):
    def __init__(
        self,
        train_station_search_vos: List[main_models.TrainNoListSearchResponseBodyModuleTrainStationSearchVOS] = None,
        train_transfer_station_search_vos: List[main_models.TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOs] = None,
    ):
        self.train_station_search_vos = train_station_search_vos
        self.train_transfer_station_search_vos = train_transfer_station_search_vos

    def validate(self):
        if self.train_station_search_vos:
            for v1 in self.train_station_search_vos:
                 if v1:
                    v1.validate()
        if self.train_transfer_station_search_vos:
            for v1 in self.train_transfer_station_search_vos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['train_station_search_v_o_s'] = []
        if self.train_station_search_vos is not None:
            for k1 in self.train_station_search_vos:
                result['train_station_search_v_o_s'].append(k1.to_map() if k1 else None)

        result['train_transfer_station_search_v_os'] = []
        if self.train_transfer_station_search_vos is not None:
            for k1 in self.train_transfer_station_search_vos:
                result['train_transfer_station_search_v_os'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.train_station_search_vos = []
        if m.get('train_station_search_v_o_s') is not None:
            for k1 in m.get('train_station_search_v_o_s'):
                temp_model = main_models.TrainNoListSearchResponseBodyModuleTrainStationSearchVOS()
                self.train_station_search_vos.append(temp_model.from_map(k1))

        self.train_transfer_station_search_vos = []
        if m.get('train_transfer_station_search_v_os') is not None:
            for k1 in m.get('train_transfer_station_search_v_os'):
                temp_model = main_models.TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOs()
                self.train_transfer_station_search_vos.append(temp_model.from_map(k1))

        return self

class TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOs(DaraModel):
    def __init__(
        self,
        arr_station: str = None,
        dep_station: str = None,
        line_key: str = None,
        middle_station: str = None,
        transfer_detail_list: List[main_models.TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOsTransferDetailList] = None,
        transfer_type: str = None,
    ):
        self.arr_station = arr_station
        self.dep_station = dep_station
        self.line_key = line_key
        self.middle_station = middle_station
        self.transfer_detail_list = transfer_detail_list
        self.transfer_type = transfer_type

    def validate(self):
        if self.transfer_detail_list:
            for v1 in self.transfer_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station is not None:
            result['arr_station'] = self.arr_station

        if self.dep_station is not None:
            result['dep_station'] = self.dep_station

        if self.line_key is not None:
            result['line_key'] = self.line_key

        if self.middle_station is not None:
            result['middle_station'] = self.middle_station

        result['transfer_detail_list'] = []
        if self.transfer_detail_list is not None:
            for k1 in self.transfer_detail_list:
                result['transfer_detail_list'].append(k1.to_map() if k1 else None)

        if self.transfer_type is not None:
            result['transfer_type'] = self.transfer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')

        if m.get('dep_station') is not None:
            self.dep_station = m.get('dep_station')

        if m.get('line_key') is not None:
            self.line_key = m.get('line_key')

        if m.get('middle_station') is not None:
            self.middle_station = m.get('middle_station')

        self.transfer_detail_list = []
        if m.get('transfer_detail_list') is not None:
            for k1 in m.get('transfer_detail_list'):
                temp_model = main_models.TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOsTransferDetailList()
                self.transfer_detail_list.append(temp_model.from_map(k1))

        if m.get('transfer_type') is not None:
            self.transfer_type = m.get('transfer_type')

        return self

class TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOsTransferDetailList(DaraModel):
    def __init__(
        self,
        arr_day_tag: str = None,
        arr_station_code: str = None,
        arr_station_name: str = None,
        arr_time: str = None,
        cost_time: str = None,
        dep_station_code: str = None,
        dep_station_name: str = None,
        dep_time: str = None,
        is_end_station: int = None,
        is_start_station: int = None,
        price: str = None,
        sale_flag: str = None,
        sale_flag_msg: str = None,
        seat_infos: List[main_models.TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOsTransferDetailListSeatInfos] = None,
        segment_index: str = None,
        train_no: str = None,
        train_type: str = None,
    ):
        self.arr_day_tag = arr_day_tag
        self.arr_station_code = arr_station_code
        self.arr_station_name = arr_station_name
        self.arr_time = arr_time
        self.cost_time = cost_time
        self.dep_station_code = dep_station_code
        self.dep_station_name = dep_station_name
        self.dep_time = dep_time
        self.is_end_station = is_end_station
        self.is_start_station = is_start_station
        self.price = price
        self.sale_flag = sale_flag
        self.sale_flag_msg = sale_flag_msg
        self.seat_infos = seat_infos
        self.segment_index = segment_index
        self.train_no = train_no
        self.train_type = train_type

    def validate(self):
        if self.seat_infos:
            for v1 in self.seat_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_day_tag is not None:
            result['arr_day_tag'] = self.arr_day_tag

        if self.arr_station_code is not None:
            result['arr_station_code'] = self.arr_station_code

        if self.arr_station_name is not None:
            result['arr_station_name'] = self.arr_station_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cost_time is not None:
            result['cost_time'] = self.cost_time

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_station_name is not None:
            result['dep_station_name'] = self.dep_station_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.is_end_station is not None:
            result['is_end_station'] = self.is_end_station

        if self.is_start_station is not None:
            result['is_start_station'] = self.is_start_station

        if self.price is not None:
            result['price'] = self.price

        if self.sale_flag is not None:
            result['sale_flag'] = self.sale_flag

        if self.sale_flag_msg is not None:
            result['sale_flag_msg'] = self.sale_flag_msg

        result['seat_infos'] = []
        if self.seat_infos is not None:
            for k1 in self.seat_infos:
                result['seat_infos'].append(k1.to_map() if k1 else None)

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.train_no is not None:
            result['train_no'] = self.train_no

        if self.train_type is not None:
            result['train_type'] = self.train_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_day_tag') is not None:
            self.arr_day_tag = m.get('arr_day_tag')

        if m.get('arr_station_code') is not None:
            self.arr_station_code = m.get('arr_station_code')

        if m.get('arr_station_name') is not None:
            self.arr_station_name = m.get('arr_station_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cost_time') is not None:
            self.cost_time = m.get('cost_time')

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_station_name') is not None:
            self.dep_station_name = m.get('dep_station_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('is_end_station') is not None:
            self.is_end_station = m.get('is_end_station')

        if m.get('is_start_station') is not None:
            self.is_start_station = m.get('is_start_station')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('sale_flag') is not None:
            self.sale_flag = m.get('sale_flag')

        if m.get('sale_flag_msg') is not None:
            self.sale_flag_msg = m.get('sale_flag_msg')

        self.seat_infos = []
        if m.get('seat_infos') is not None:
            for k1 in m.get('seat_infos'):
                temp_model = main_models.TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOsTransferDetailListSeatInfos()
                self.seat_infos.append(temp_model.from_map(k1))

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        if m.get('train_type') is not None:
            self.train_type = m.get('train_type')

        return self

class TrainNoListSearchResponseBodyModuleTrainTransferStationSearchVOsTransferDetailListSeatInfos(DaraModel):
    def __init__(
        self,
        price: int = None,
        seat_name: str = None,
        seat_type: str = None,
        stock: str = None,
    ):
        self.price = price
        self.seat_name = seat_name
        self.seat_type = seat_type
        self.stock = stock

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['price'] = self.price

        if self.seat_name is not None:
            result['seat_name'] = self.seat_name

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

        if self.stock is not None:
            result['stock'] = self.stock

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('seat_name') is not None:
            self.seat_name = m.get('seat_name')

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

        if m.get('stock') is not None:
            self.stock = m.get('stock')

        return self

class TrainNoListSearchResponseBodyModuleTrainStationSearchVOS(DaraModel):
    def __init__(
        self,
        arr_day_tag: str = None,
        arr_station_code: str = None,
        arr_station_name: str = None,
        arr_time: str = None,
        cost_time: str = None,
        dep_station_code: str = None,
        dep_station_name: str = None,
        dep_time: str = None,
        is_end_station: int = None,
        is_start_station: int = None,
        price: str = None,
        sale_flag: str = None,
        sale_flag_msg: str = None,
        seagment_index: str = None,
        seat_infos: List[main_models.TrainNoListSearchResponseBodyModuleTrainStationSearchVOSSeatInfos] = None,
        train_no: str = None,
        train_type: str = None,
    ):
        self.arr_day_tag = arr_day_tag
        self.arr_station_code = arr_station_code
        self.arr_station_name = arr_station_name
        self.arr_time = arr_time
        self.cost_time = cost_time
        self.dep_station_code = dep_station_code
        self.dep_station_name = dep_station_name
        self.dep_time = dep_time
        self.is_end_station = is_end_station
        self.is_start_station = is_start_station
        self.price = price
        self.sale_flag = sale_flag
        self.sale_flag_msg = sale_flag_msg
        self.seagment_index = seagment_index
        self.seat_infos = seat_infos
        self.train_no = train_no
        self.train_type = train_type

    def validate(self):
        if self.seat_infos:
            for v1 in self.seat_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_day_tag is not None:
            result['arr_day_tag'] = self.arr_day_tag

        if self.arr_station_code is not None:
            result['arr_station_code'] = self.arr_station_code

        if self.arr_station_name is not None:
            result['arr_station_name'] = self.arr_station_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cost_time is not None:
            result['cost_time'] = self.cost_time

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_station_name is not None:
            result['dep_station_name'] = self.dep_station_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.is_end_station is not None:
            result['is_end_station'] = self.is_end_station

        if self.is_start_station is not None:
            result['is_start_station'] = self.is_start_station

        if self.price is not None:
            result['price'] = self.price

        if self.sale_flag is not None:
            result['sale_flag'] = self.sale_flag

        if self.sale_flag_msg is not None:
            result['sale_flag_msg'] = self.sale_flag_msg

        if self.seagment_index is not None:
            result['seagment_index'] = self.seagment_index

        result['seat_infos'] = []
        if self.seat_infos is not None:
            for k1 in self.seat_infos:
                result['seat_infos'].append(k1.to_map() if k1 else None)

        if self.train_no is not None:
            result['train_no'] = self.train_no

        if self.train_type is not None:
            result['train_type'] = self.train_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_day_tag') is not None:
            self.arr_day_tag = m.get('arr_day_tag')

        if m.get('arr_station_code') is not None:
            self.arr_station_code = m.get('arr_station_code')

        if m.get('arr_station_name') is not None:
            self.arr_station_name = m.get('arr_station_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cost_time') is not None:
            self.cost_time = m.get('cost_time')

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_station_name') is not None:
            self.dep_station_name = m.get('dep_station_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('is_end_station') is not None:
            self.is_end_station = m.get('is_end_station')

        if m.get('is_start_station') is not None:
            self.is_start_station = m.get('is_start_station')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('sale_flag') is not None:
            self.sale_flag = m.get('sale_flag')

        if m.get('sale_flag_msg') is not None:
            self.sale_flag_msg = m.get('sale_flag_msg')

        if m.get('seagment_index') is not None:
            self.seagment_index = m.get('seagment_index')

        self.seat_infos = []
        if m.get('seat_infos') is not None:
            for k1 in m.get('seat_infos'):
                temp_model = main_models.TrainNoListSearchResponseBodyModuleTrainStationSearchVOSSeatInfos()
                self.seat_infos.append(temp_model.from_map(k1))

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        if m.get('train_type') is not None:
            self.train_type = m.get('train_type')

        return self

class TrainNoListSearchResponseBodyModuleTrainStationSearchVOSSeatInfos(DaraModel):
    def __init__(
        self,
        price: int = None,
        seat_name: str = None,
        seat_type: str = None,
        stock: str = None,
    ):
        self.price = price
        self.seat_name = seat_name
        self.seat_type = seat_type
        self.stock = stock

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['price'] = self.price

        if self.seat_name is not None:
            result['seat_name'] = self.seat_name

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

        if self.stock is not None:
            result['stock'] = self.stock

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('seat_name') is not None:
            self.seat_name = m.get('seat_name')

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

        if m.get('stock') is not None:
            self.stock = m.get('stock')

        return self

