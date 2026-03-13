# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainOrderQueryV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TrainOrderQueryV2ResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        # requestId
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
            temp_model = main_models.TrainOrderQueryV2ResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainOrderQueryV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        change_ticket_info_list: List[main_models.TrainOrderQueryV2ResponseBodyModuleChangeTicketInfoList] = None,
        invoice_info: main_models.TrainOrderQueryV2ResponseBodyModuleInvoiceInfo = None,
        order_base_info: main_models.TrainOrderQueryV2ResponseBodyModuleOrderBaseInfo = None,
        passenger_info_list: List[main_models.TrainOrderQueryV2ResponseBodyModulePassengerInfoList] = None,
        price_info_list: List[main_models.TrainOrderQueryV2ResponseBodyModulePriceInfoList] = None,
        refund_ticket_info_list: List[main_models.TrainOrderQueryV2ResponseBodyModuleRefundTicketInfoList] = None,
        train_order_info: main_models.TrainOrderQueryV2ResponseBodyModuleTrainOrderInfo = None,
    ):
        self.change_ticket_info_list = change_ticket_info_list
        self.invoice_info = invoice_info
        self.order_base_info = order_base_info
        self.passenger_info_list = passenger_info_list
        self.price_info_list = price_info_list
        self.refund_ticket_info_list = refund_ticket_info_list
        self.train_order_info = train_order_info

    def validate(self):
        if self.change_ticket_info_list:
            for v1 in self.change_ticket_info_list:
                 if v1:
                    v1.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.order_base_info:
            self.order_base_info.validate()
        if self.passenger_info_list:
            for v1 in self.passenger_info_list:
                 if v1:
                    v1.validate()
        if self.price_info_list:
            for v1 in self.price_info_list:
                 if v1:
                    v1.validate()
        if self.refund_ticket_info_list:
            for v1 in self.refund_ticket_info_list:
                 if v1:
                    v1.validate()
        if self.train_order_info:
            self.train_order_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['change_ticket_info_list'] = []
        if self.change_ticket_info_list is not None:
            for k1 in self.change_ticket_info_list:
                result['change_ticket_info_list'].append(k1.to_map() if k1 else None)

        if self.invoice_info is not None:
            result['invoice_info'] = self.invoice_info.to_map()

        if self.order_base_info is not None:
            result['order_base_info'] = self.order_base_info.to_map()

        result['passenger_info_list'] = []
        if self.passenger_info_list is not None:
            for k1 in self.passenger_info_list:
                result['passenger_info_list'].append(k1.to_map() if k1 else None)

        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k1 in self.price_info_list:
                result['price_info_list'].append(k1.to_map() if k1 else None)

        result['refund_ticket_info_list'] = []
        if self.refund_ticket_info_list is not None:
            for k1 in self.refund_ticket_info_list:
                result['refund_ticket_info_list'].append(k1.to_map() if k1 else None)

        if self.train_order_info is not None:
            result['train_order_info'] = self.train_order_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_ticket_info_list = []
        if m.get('change_ticket_info_list') is not None:
            for k1 in m.get('change_ticket_info_list'):
                temp_model = main_models.TrainOrderQueryV2ResponseBodyModuleChangeTicketInfoList()
                self.change_ticket_info_list.append(temp_model.from_map(k1))

        if m.get('invoice_info') is not None:
            temp_model = main_models.TrainOrderQueryV2ResponseBodyModuleInvoiceInfo()
            self.invoice_info = temp_model.from_map(m.get('invoice_info'))

        if m.get('order_base_info') is not None:
            temp_model = main_models.TrainOrderQueryV2ResponseBodyModuleOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m.get('order_base_info'))

        self.passenger_info_list = []
        if m.get('passenger_info_list') is not None:
            for k1 in m.get('passenger_info_list'):
                temp_model = main_models.TrainOrderQueryV2ResponseBodyModulePassengerInfoList()
                self.passenger_info_list.append(temp_model.from_map(k1))

        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k1 in m.get('price_info_list'):
                temp_model = main_models.TrainOrderQueryV2ResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k1))

        self.refund_ticket_info_list = []
        if m.get('refund_ticket_info_list') is not None:
            for k1 in m.get('refund_ticket_info_list'):
                temp_model = main_models.TrainOrderQueryV2ResponseBodyModuleRefundTicketInfoList()
                self.refund_ticket_info_list.append(temp_model.from_map(k1))

        if m.get('train_order_info') is not None:
            temp_model = main_models.TrainOrderQueryV2ResponseBodyModuleTrainOrderInfo()
            self.train_order_info = temp_model.from_map(m.get('train_order_info'))

        return self

class TrainOrderQueryV2ResponseBodyModuleTrainOrderInfo(DaraModel):
    def __init__(
        self,
        train_info_list: List[main_models.TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainInfoList] = None,
        train_transfer_info: main_models.TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainTransferInfo = None,
    ):
        self.train_info_list = train_info_list
        self.train_transfer_info = train_transfer_info

    def validate(self):
        if self.train_info_list:
            for v1 in self.train_info_list:
                 if v1:
                    v1.validate()
        if self.train_transfer_info:
            self.train_transfer_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['train_info_list'] = []
        if self.train_info_list is not None:
            for k1 in self.train_info_list:
                result['train_info_list'].append(k1.to_map() if k1 else None)

        if self.train_transfer_info is not None:
            result['train_transfer_info'] = self.train_transfer_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.train_info_list = []
        if m.get('train_info_list') is not None:
            for k1 in m.get('train_info_list'):
                temp_model = main_models.TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainInfoList()
                self.train_info_list.append(temp_model.from_map(k1))

        if m.get('train_transfer_info') is not None:
            temp_model = main_models.TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainTransferInfo()
            self.train_transfer_info = temp_model.from_map(m.get('train_transfer_info'))

        return self

class TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainTransferInfo(DaraModel):
    def __init__(
        self,
        cost_time: str = None,
        end_time: str = None,
        from_city_ad_code: str = None,
        from_city_name: str = None,
        from_station_name: str = None,
        middle_city: str = None,
        middle_city_ad_code: str = None,
        middle_date: str = None,
        middle_station: str = None,
        middle_type: str = None,
        start_time: str = None,
        sub_from_city_ad_code: str = None,
        sub_from_city_ad_name: str = None,
        sub_middle_city_code: str = None,
        sub_middle_city_name: str = None,
        sub_to_city_code: str = None,
        sub_to_city_name: str = None,
        to_city_ad_code: str = None,
        to_city_name: str = None,
        to_station_name: str = None,
        wait_time: str = None,
    ):
        self.cost_time = cost_time
        self.end_time = end_time
        self.from_city_ad_code = from_city_ad_code
        self.from_city_name = from_city_name
        self.from_station_name = from_station_name
        self.middle_city = middle_city
        self.middle_city_ad_code = middle_city_ad_code
        self.middle_date = middle_date
        self.middle_station = middle_station
        self.middle_type = middle_type
        self.start_time = start_time
        self.sub_from_city_ad_code = sub_from_city_ad_code
        self.sub_from_city_ad_name = sub_from_city_ad_name
        self.sub_middle_city_code = sub_middle_city_code
        self.sub_middle_city_name = sub_middle_city_name
        self.sub_to_city_code = sub_to_city_code
        self.sub_to_city_name = sub_to_city_name
        self.to_city_ad_code = to_city_ad_code
        self.to_city_name = to_city_name
        self.to_station_name = to_station_name
        self.wait_time = wait_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_time is not None:
            result['cost_time'] = self.cost_time

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.from_city_ad_code is not None:
            result['from_city_ad_code'] = self.from_city_ad_code

        if self.from_city_name is not None:
            result['from_city_name'] = self.from_city_name

        if self.from_station_name is not None:
            result['from_station_name'] = self.from_station_name

        if self.middle_city is not None:
            result['middle_city'] = self.middle_city

        if self.middle_city_ad_code is not None:
            result['middle_city_ad_code'] = self.middle_city_ad_code

        if self.middle_date is not None:
            result['middle_date'] = self.middle_date

        if self.middle_station is not None:
            result['middle_station'] = self.middle_station

        if self.middle_type is not None:
            result['middle_type'] = self.middle_type

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.sub_from_city_ad_code is not None:
            result['sub_from_city_ad_code'] = self.sub_from_city_ad_code

        if self.sub_from_city_ad_name is not None:
            result['sub_from_city_ad_name'] = self.sub_from_city_ad_name

        if self.sub_middle_city_code is not None:
            result['sub_middle_city_code'] = self.sub_middle_city_code

        if self.sub_middle_city_name is not None:
            result['sub_middle_city_name'] = self.sub_middle_city_name

        if self.sub_to_city_code is not None:
            result['sub_to_city_code'] = self.sub_to_city_code

        if self.sub_to_city_name is not None:
            result['sub_to_city_name'] = self.sub_to_city_name

        if self.to_city_ad_code is not None:
            result['to_city_ad_code'] = self.to_city_ad_code

        if self.to_city_name is not None:
            result['to_city_name'] = self.to_city_name

        if self.to_station_name is not None:
            result['to_station_name'] = self.to_station_name

        if self.wait_time is not None:
            result['wait_time'] = self.wait_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_time') is not None:
            self.cost_time = m.get('cost_time')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('from_city_ad_code') is not None:
            self.from_city_ad_code = m.get('from_city_ad_code')

        if m.get('from_city_name') is not None:
            self.from_city_name = m.get('from_city_name')

        if m.get('from_station_name') is not None:
            self.from_station_name = m.get('from_station_name')

        if m.get('middle_city') is not None:
            self.middle_city = m.get('middle_city')

        if m.get('middle_city_ad_code') is not None:
            self.middle_city_ad_code = m.get('middle_city_ad_code')

        if m.get('middle_date') is not None:
            self.middle_date = m.get('middle_date')

        if m.get('middle_station') is not None:
            self.middle_station = m.get('middle_station')

        if m.get('middle_type') is not None:
            self.middle_type = m.get('middle_type')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('sub_from_city_ad_code') is not None:
            self.sub_from_city_ad_code = m.get('sub_from_city_ad_code')

        if m.get('sub_from_city_ad_name') is not None:
            self.sub_from_city_ad_name = m.get('sub_from_city_ad_name')

        if m.get('sub_middle_city_code') is not None:
            self.sub_middle_city_code = m.get('sub_middle_city_code')

        if m.get('sub_middle_city_name') is not None:
            self.sub_middle_city_name = m.get('sub_middle_city_name')

        if m.get('sub_to_city_code') is not None:
            self.sub_to_city_code = m.get('sub_to_city_code')

        if m.get('sub_to_city_name') is not None:
            self.sub_to_city_name = m.get('sub_to_city_name')

        if m.get('to_city_ad_code') is not None:
            self.to_city_ad_code = m.get('to_city_ad_code')

        if m.get('to_city_name') is not None:
            self.to_city_name = m.get('to_city_name')

        if m.get('to_station_name') is not None:
            self.to_station_name = m.get('to_station_name')

        if m.get('wait_time') is not None:
            self.wait_time = m.get('wait_time')

        return self

class TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainInfoList(DaraModel):
    def __init__(
        self,
        arr_time: str = None,
        dep_time: str = None,
        from_city_ad_code: str = None,
        from_city_name: str = None,
        from_station_name: str = None,
        item_id: int = None,
        run_time: int = None,
        sub_from_city_ad_code: str = None,
        sub_from_city_ad_name: str = None,
        sub_to_city_code: str = None,
        sub_to_city_name: str = None,
        to_city_ad_code: str = None,
        to_city_name: str = None,
        to_station_name: str = None,
        train_no: str = None,
        train_ticket_infos: List[main_models.TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainInfoListTrainTicketInfos] = None,
    ):
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.from_city_ad_code = from_city_ad_code
        self.from_city_name = from_city_name
        self.from_station_name = from_station_name
        # itemId
        self.item_id = item_id
        self.run_time = run_time
        self.sub_from_city_ad_code = sub_from_city_ad_code
        self.sub_from_city_ad_name = sub_from_city_ad_name
        self.sub_to_city_code = sub_to_city_code
        self.sub_to_city_name = sub_to_city_name
        self.to_city_ad_code = to_city_ad_code
        self.to_city_name = to_city_name
        self.to_station_name = to_station_name
        self.train_no = train_no
        self.train_ticket_infos = train_ticket_infos

    def validate(self):
        if self.train_ticket_infos:
            for v1 in self.train_ticket_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.from_city_ad_code is not None:
            result['from_city_ad_code'] = self.from_city_ad_code

        if self.from_city_name is not None:
            result['from_city_name'] = self.from_city_name

        if self.from_station_name is not None:
            result['from_station_name'] = self.from_station_name

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.run_time is not None:
            result['run_time'] = self.run_time

        if self.sub_from_city_ad_code is not None:
            result['sub_from_city_ad_code'] = self.sub_from_city_ad_code

        if self.sub_from_city_ad_name is not None:
            result['sub_from_city_ad_name'] = self.sub_from_city_ad_name

        if self.sub_to_city_code is not None:
            result['sub_to_city_code'] = self.sub_to_city_code

        if self.sub_to_city_name is not None:
            result['sub_to_city_name'] = self.sub_to_city_name

        if self.to_city_ad_code is not None:
            result['to_city_ad_code'] = self.to_city_ad_code

        if self.to_city_name is not None:
            result['to_city_name'] = self.to_city_name

        if self.to_station_name is not None:
            result['to_station_name'] = self.to_station_name

        if self.train_no is not None:
            result['train_no'] = self.train_no

        result['train_ticket_infos'] = []
        if self.train_ticket_infos is not None:
            for k1 in self.train_ticket_infos:
                result['train_ticket_infos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('from_city_ad_code') is not None:
            self.from_city_ad_code = m.get('from_city_ad_code')

        if m.get('from_city_name') is not None:
            self.from_city_name = m.get('from_city_name')

        if m.get('from_station_name') is not None:
            self.from_station_name = m.get('from_station_name')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('run_time') is not None:
            self.run_time = m.get('run_time')

        if m.get('sub_from_city_ad_code') is not None:
            self.sub_from_city_ad_code = m.get('sub_from_city_ad_code')

        if m.get('sub_from_city_ad_name') is not None:
            self.sub_from_city_ad_name = m.get('sub_from_city_ad_name')

        if m.get('sub_to_city_code') is not None:
            self.sub_to_city_code = m.get('sub_to_city_code')

        if m.get('sub_to_city_name') is not None:
            self.sub_to_city_name = m.get('sub_to_city_name')

        if m.get('to_city_ad_code') is not None:
            self.to_city_ad_code = m.get('to_city_ad_code')

        if m.get('to_city_name') is not None:
            self.to_city_name = m.get('to_city_name')

        if m.get('to_station_name') is not None:
            self.to_station_name = m.get('to_station_name')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        self.train_ticket_infos = []
        if m.get('train_ticket_infos') is not None:
            for k1 in m.get('train_ticket_infos'):
                temp_model = main_models.TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainInfoListTrainTicketInfos()
                self.train_ticket_infos.append(temp_model.from_map(k1))

        return self

class TrainOrderQueryV2ResponseBodyModuleTrainOrderInfoTrainInfoListTrainTicketInfos(DaraModel):
    def __init__(
        self,
        changed: bool = None,
        check_in_time: str = None,
        check_out_time: str = None,
        coach_no: str = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        out_ticket_status: str = None,
        pay_type: int = None,
        seat_no: str = None,
        seat_type_name: str = None,
        segment_index: int = None,
        service_fee: float = None,
        short_ticket_no: str = None,
        start_time: str = None,
        ticket_entrance: str = None,
        ticket_no: str = None,
        ticket_price: float = None,
        ticket_status: int = None,
        train_type_name: str = None,
        use_ticket: str = None,
        user_id: str = None,
    ):
        self.changed = changed
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.coach_no = coach_no
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.out_ticket_status = out_ticket_status
        self.pay_type = pay_type
        self.seat_no = seat_no
        self.seat_type_name = seat_type_name
        self.segment_index = segment_index
        self.service_fee = service_fee
        self.short_ticket_no = short_ticket_no
        self.start_time = start_time
        self.ticket_entrance = ticket_entrance
        self.ticket_no = ticket_no
        self.ticket_price = ticket_price
        self.ticket_status = ticket_status
        self.train_type_name = train_type_name
        self.use_ticket = use_ticket
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changed is not None:
            result['changed'] = self.changed

        if self.check_in_time is not None:
            result['check_in_time'] = self.check_in_time

        if self.check_out_time is not None:
            result['check_out_time'] = self.check_out_time

        if self.coach_no is not None:
            result['coach_no'] = self.coach_no

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify

        if self.out_ticket_status is not None:
            result['out_ticket_status'] = self.out_ticket_status

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.seat_no is not None:
            result['seat_no'] = self.seat_no

        if self.seat_type_name is not None:
            result['seat_type_name'] = self.seat_type_name

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        if self.short_ticket_no is not None:
            result['short_ticket_no'] = self.short_ticket_no

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.ticket_entrance is not None:
            result['ticket_entrance'] = self.ticket_entrance

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status

        if self.train_type_name is not None:
            result['train_type_name'] = self.train_type_name

        if self.use_ticket is not None:
            result['use_ticket'] = self.use_ticket

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changed') is not None:
            self.changed = m.get('changed')

        if m.get('check_in_time') is not None:
            self.check_in_time = m.get('check_in_time')

        if m.get('check_out_time') is not None:
            self.check_out_time = m.get('check_out_time')

        if m.get('coach_no') is not None:
            self.coach_no = m.get('coach_no')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')

        if m.get('out_ticket_status') is not None:
            self.out_ticket_status = m.get('out_ticket_status')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('seat_no') is not None:
            self.seat_no = m.get('seat_no')

        if m.get('seat_type_name') is not None:
            self.seat_type_name = m.get('seat_type_name')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        if m.get('short_ticket_no') is not None:
            self.short_ticket_no = m.get('short_ticket_no')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('ticket_entrance') is not None:
            self.ticket_entrance = m.get('ticket_entrance')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')

        if m.get('train_type_name') is not None:
            self.train_type_name = m.get('train_type_name')

        if m.get('use_ticket') is not None:
            self.use_ticket = m.get('use_ticket')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class TrainOrderQueryV2ResponseBodyModuleRefundTicketInfoList(DaraModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modify: str = None,
        refund_apply_id: str = None,
        refund_fee: float = None,
        refund_service_fee: float = None,
        ticket_no: str = None,
        user_id: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.refund_apply_id = refund_apply_id
        self.refund_fee = refund_fee
        self.refund_service_fee = refund_service_fee
        self.ticket_no = ticket_no
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify

        if self.refund_apply_id is not None:
            result['refund_apply_id'] = self.refund_apply_id

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        if self.refund_service_fee is not None:
            result['refund_service_fee'] = self.refund_service_fee

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')

        if m.get('refund_apply_id') is not None:
            self.refund_apply_id = m.get('refund_apply_id')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        if m.get('refund_service_fee') is not None:
            self.refund_service_fee = m.get('refund_service_fee')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class TrainOrderQueryV2ResponseBodyModulePriceInfoList(DaraModel):
    def __init__(
        self,
        category_code: int = None,
        gmt_create: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.gmt_create = gmt_create
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.price = price
        self.trade_id = trade_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['category_code'] = self.category_code

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.price is not None:
            result['price'] = self.price

        if self.trade_id is not None:
            result['trade_id'] = self.trade_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class TrainOrderQueryV2ResponseBodyModulePassengerInfoList(DaraModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        thirdpart_cost_center_id: str = None,
        thirdpart_project_id: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_number = cost_center_number
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.thirdpart_project_id = thirdpart_project_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.thirdpart_project_id is not None:
            result['thirdpart_project_id'] = self.thirdpart_project_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('thirdpart_project_id') is not None:
            self.thirdpart_project_id = m.get('thirdpart_project_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class TrainOrderQueryV2ResponseBodyModuleOrderBaseInfo(DaraModel):
    def __init__(
        self,
        apply_id: str = None,
        btrip_title: str = None,
        contact_name: str = None,
        contact_phone: str = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        exceed_apply_id: str = None,
        exceed_thirdpart_apply_id: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        itinerary_id: str = None,
        order_id: int = None,
        order_status: int = None,
        replenish_order_ids: str = None,
        replenish_original_order_id: str = None,
        third_part_business_id: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_depart_id: str = None,
        thirdpart_itinerary_id: str = None,
        trip_type: int = None,
        user_id: str = None,
        user_nick: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_title = btrip_title
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.exceed_apply_id = exceed_apply_id
        self.exceed_thirdpart_apply_id = exceed_thirdpart_apply_id
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.itinerary_id = itinerary_id
        self.order_id = order_id
        self.order_status = order_status
        self.replenish_order_ids = replenish_order_ids
        self.replenish_original_order_id = replenish_original_order_id
        self.third_part_business_id = third_part_business_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_depart_id = thirdpart_depart_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.trip_type = trip_type
        self.user_id = user_id
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title

        if self.contact_name is not None:
            result['contact_name'] = self.contact_name

        if self.contact_phone is not None:
            result['contact_phone'] = self.contact_phone

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.exceed_apply_id is not None:
            result['exceed_apply_id'] = self.exceed_apply_id

        if self.exceed_thirdpart_apply_id is not None:
            result['exceed_thirdpart_apply_id'] = self.exceed_thirdpart_apply_id

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.replenish_order_ids is not None:
            result['replenish_order_ids'] = self.replenish_order_ids

        if self.replenish_original_order_id is not None:
            result['replenish_original_order_id'] = self.replenish_original_order_id

        if self.third_part_business_id is not None:
            result['thirdPart_business_id'] = self.third_part_business_id

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_depart_id is not None:
            result['thirdpart_depart_id'] = self.thirdpart_depart_id

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_nick is not None:
            result['user_nick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')

        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')

        if m.get('contact_phone') is not None:
            self.contact_phone = m.get('contact_phone')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('exceed_apply_id') is not None:
            self.exceed_apply_id = m.get('exceed_apply_id')

        if m.get('exceed_thirdpart_apply_id') is not None:
            self.exceed_thirdpart_apply_id = m.get('exceed_thirdpart_apply_id')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('replenish_order_ids') is not None:
            self.replenish_order_ids = m.get('replenish_order_ids')

        if m.get('replenish_original_order_id') is not None:
            self.replenish_original_order_id = m.get('replenish_original_order_id')

        if m.get('thirdPart_business_id') is not None:
            self.third_part_business_id = m.get('thirdPart_business_id')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_depart_id') is not None:
            self.thirdpart_depart_id = m.get('thirdpart_depart_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_nick') is not None:
            self.user_nick = m.get('user_nick')

        return self

class TrainOrderQueryV2ResponseBodyModuleInvoiceInfo(DaraModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class TrainOrderQueryV2ResponseBodyModuleChangeTicketInfoList(DaraModel):
    def __init__(
        self,
        change_coach_no: str = None,
        change_gap_fee: float = None,
        change_handling_fee: float = None,
        change_order_id: str = None,
        change_seat_no: str = None,
        change_seat_type_name: str = None,
        change_service_fee: float = None,
        change_train_no: str = None,
        change_train_type_name: str = None,
        check_in_time: str = None,
        check_out_time: str = None,
        end_time: str = None,
        from_city_name: str = None,
        from_station_name: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        origin_ticket_no: str = None,
        out_ticket_status: str = None,
        segment_index: int = None,
        short_ticket_no: str = None,
        start_time: str = None,
        ticket_entrance: str = None,
        ticket_no: str = None,
        ticket_status: int = None,
        to_city_name: str = None,
        to_station_name: str = None,
        use_ticket: str = None,
        user_id: str = None,
    ):
        self.change_coach_no = change_coach_no
        self.change_gap_fee = change_gap_fee
        self.change_handling_fee = change_handling_fee
        self.change_order_id = change_order_id
        self.change_seat_no = change_seat_no
        self.change_seat_type_name = change_seat_type_name
        self.change_service_fee = change_service_fee
        self.change_train_no = change_train_no
        self.change_train_type_name = change_train_type_name
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.end_time = end_time
        self.from_city_name = from_city_name
        self.from_station_name = from_station_name
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.origin_ticket_no = origin_ticket_no
        self.out_ticket_status = out_ticket_status
        self.segment_index = segment_index
        self.short_ticket_no = short_ticket_no
        self.start_time = start_time
        self.ticket_entrance = ticket_entrance
        self.ticket_no = ticket_no
        self.ticket_status = ticket_status
        self.to_city_name = to_city_name
        self.to_station_name = to_station_name
        self.use_ticket = use_ticket
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_coach_no is not None:
            result['change_coach_no'] = self.change_coach_no

        if self.change_gap_fee is not None:
            result['change_gap_fee'] = self.change_gap_fee

        if self.change_handling_fee is not None:
            result['change_handling_fee'] = self.change_handling_fee

        if self.change_order_id is not None:
            result['change_order_id'] = self.change_order_id

        if self.change_seat_no is not None:
            result['change_seat_no'] = self.change_seat_no

        if self.change_seat_type_name is not None:
            result['change_seat_type_name'] = self.change_seat_type_name

        if self.change_service_fee is not None:
            result['change_service_fee'] = self.change_service_fee

        if self.change_train_no is not None:
            result['change_train_no'] = self.change_train_no

        if self.change_train_type_name is not None:
            result['change_train_type_name'] = self.change_train_type_name

        if self.check_in_time is not None:
            result['check_in_time'] = self.check_in_time

        if self.check_out_time is not None:
            result['check_out_time'] = self.check_out_time

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.from_city_name is not None:
            result['from_city_name'] = self.from_city_name

        if self.from_station_name is not None:
            result['from_station_name'] = self.from_station_name

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify

        if self.origin_ticket_no is not None:
            result['origin_ticket_no'] = self.origin_ticket_no

        if self.out_ticket_status is not None:
            result['out_ticket_status'] = self.out_ticket_status

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.short_ticket_no is not None:
            result['short_ticket_no'] = self.short_ticket_no

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.ticket_entrance is not None:
            result['ticket_entrance'] = self.ticket_entrance

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status

        if self.to_city_name is not None:
            result['to_city_name'] = self.to_city_name

        if self.to_station_name is not None:
            result['to_station_name'] = self.to_station_name

        if self.use_ticket is not None:
            result['use_ticket'] = self.use_ticket

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_coach_no') is not None:
            self.change_coach_no = m.get('change_coach_no')

        if m.get('change_gap_fee') is not None:
            self.change_gap_fee = m.get('change_gap_fee')

        if m.get('change_handling_fee') is not None:
            self.change_handling_fee = m.get('change_handling_fee')

        if m.get('change_order_id') is not None:
            self.change_order_id = m.get('change_order_id')

        if m.get('change_seat_no') is not None:
            self.change_seat_no = m.get('change_seat_no')

        if m.get('change_seat_type_name') is not None:
            self.change_seat_type_name = m.get('change_seat_type_name')

        if m.get('change_service_fee') is not None:
            self.change_service_fee = m.get('change_service_fee')

        if m.get('change_train_no') is not None:
            self.change_train_no = m.get('change_train_no')

        if m.get('change_train_type_name') is not None:
            self.change_train_type_name = m.get('change_train_type_name')

        if m.get('check_in_time') is not None:
            self.check_in_time = m.get('check_in_time')

        if m.get('check_out_time') is not None:
            self.check_out_time = m.get('check_out_time')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('from_city_name') is not None:
            self.from_city_name = m.get('from_city_name')

        if m.get('from_station_name') is not None:
            self.from_station_name = m.get('from_station_name')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')

        if m.get('origin_ticket_no') is not None:
            self.origin_ticket_no = m.get('origin_ticket_no')

        if m.get('out_ticket_status') is not None:
            self.out_ticket_status = m.get('out_ticket_status')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('short_ticket_no') is not None:
            self.short_ticket_no = m.get('short_ticket_no')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('ticket_entrance') is not None:
            self.ticket_entrance = m.get('ticket_entrance')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')

        if m.get('to_city_name') is not None:
            self.to_city_name = m.get('to_city_name')

        if m.get('to_station_name') is not None:
            self.to_station_name = m.get('to_station_name')

        if m.get('use_ticket') is not None:
            self.use_ticket = m.get('use_ticket')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

