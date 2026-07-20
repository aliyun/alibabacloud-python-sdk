# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainOrderDetailQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TrainOrderDetailQueryResponseBodyModule = None,
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
            temp_model = main_models.TrainOrderDetailQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainOrderDetailQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        book_infos: main_models.TrainOrderDetailQueryResponseBodyModuleBookInfos = None,
        change_infos: List[main_models.TrainOrderDetailQueryResponseBodyModuleChangeInfos] = None,
        offline_refund_details: List[main_models.TrainOrderDetailQueryResponseBodyModuleOfflineRefundDetails] = None,
        order_id: str = None,
        out_order_id: str = None,
        passenger_info_s: List[main_models.TrainOrderDetailQueryResponseBodyModulePassengerInfoS] = None,
        refund_infos: List[main_models.TrainOrderDetailQueryResponseBodyModuleRefundInfos] = None,
    ):
        self.book_infos = book_infos
        self.change_infos = change_infos
        self.offline_refund_details = offline_refund_details
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.passenger_info_s = passenger_info_s
        self.refund_infos = refund_infos

    def validate(self):
        if self.book_infos:
            self.book_infos.validate()
        if self.change_infos:
            for v1 in self.change_infos:
                 if v1:
                    v1.validate()
        if self.offline_refund_details:
            for v1 in self.offline_refund_details:
                 if v1:
                    v1.validate()
        if self.passenger_info_s:
            for v1 in self.passenger_info_s:
                 if v1:
                    v1.validate()
        if self.refund_infos:
            for v1 in self.refund_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.book_infos is not None:
            result['book_infos'] = self.book_infos.to_map()

        result['change_infos'] = []
        if self.change_infos is not None:
            for k1 in self.change_infos:
                result['change_infos'].append(k1.to_map() if k1 else None)

        result['offlineRefundDetails'] = []
        if self.offline_refund_details is not None:
            for k1 in self.offline_refund_details:
                result['offlineRefundDetails'].append(k1.to_map() if k1 else None)

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        result['passenger_info_s'] = []
        if self.passenger_info_s is not None:
            for k1 in self.passenger_info_s:
                result['passenger_info_s'].append(k1.to_map() if k1 else None)

        result['refund_infos'] = []
        if self.refund_infos is not None:
            for k1 in self.refund_infos:
                result['refund_infos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('book_infos') is not None:
            temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleBookInfos()
            self.book_infos = temp_model.from_map(m.get('book_infos'))

        self.change_infos = []
        if m.get('change_infos') is not None:
            for k1 in m.get('change_infos'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleChangeInfos()
                self.change_infos.append(temp_model.from_map(k1))

        self.offline_refund_details = []
        if m.get('offlineRefundDetails') is not None:
            for k1 in m.get('offlineRefundDetails'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleOfflineRefundDetails()
                self.offline_refund_details.append(temp_model.from_map(k1))

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        self.passenger_info_s = []
        if m.get('passenger_info_s') is not None:
            for k1 in m.get('passenger_info_s'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModulePassengerInfoS()
                self.passenger_info_s.append(temp_model.from_map(k1))

        self.refund_infos = []
        if m.get('refund_infos') is not None:
            for k1 in m.get('refund_infos'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleRefundInfos()
                self.refund_infos.append(temp_model.from_map(k1))

        return self

class TrainOrderDetailQueryResponseBodyModuleRefundInfos(DaraModel):
    def __init__(
        self,
        fail_code: str = None,
        fail_msg: str = None,
        out_refund_id: str = None,
        refund_id: str = None,
        refund_train_info: List[main_models.TrainOrderDetailQueryResponseBodyModuleRefundInfosRefundTrainInfo] = None,
        status: str = None,
    ):
        self.fail_code = fail_code
        self.fail_msg = fail_msg
        self.out_refund_id = out_refund_id
        # String
        self.refund_id = refund_id
        self.refund_train_info = refund_train_info
        self.status = status

    def validate(self):
        if self.refund_train_info:
            for v1 in self.refund_train_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_code is not None:
            result['fail_code'] = self.fail_code

        if self.fail_msg is not None:
            result['fail_msg'] = self.fail_msg

        if self.out_refund_id is not None:
            result['out_refund_id'] = self.out_refund_id

        if self.refund_id is not None:
            result['refund_id'] = self.refund_id

        result['refund_train_info'] = []
        if self.refund_train_info is not None:
            for k1 in self.refund_train_info:
                result['refund_train_info'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fail_code') is not None:
            self.fail_code = m.get('fail_code')

        if m.get('fail_msg') is not None:
            self.fail_msg = m.get('fail_msg')

        if m.get('out_refund_id') is not None:
            self.out_refund_id = m.get('out_refund_id')

        if m.get('refund_id') is not None:
            self.refund_id = m.get('refund_id')

        self.refund_train_info = []
        if m.get('refund_train_info') is not None:
            for k1 in m.get('refund_train_info'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleRefundInfosRefundTrainInfo()
                self.refund_train_info.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class TrainOrderDetailQueryResponseBodyModuleRefundInfosRefundTrainInfo(DaraModel):
    def __init__(
        self,
        arr_station_name: str = None,
        arr_time: str = None,
        dep_station_code: str = None,
        dep_station_name: str = None,
        dep_time: str = None,
        refund_ticket_infos: List[main_models.TrainOrderDetailQueryResponseBodyModuleRefundInfosRefundTrainInfoRefundTicketInfos] = None,
        train_no: str = None,
    ):
        self.arr_station_name = arr_station_name
        self.arr_time = arr_time
        self.dep_station_code = dep_station_code
        self.dep_station_name = dep_station_name
        self.dep_time = dep_time
        self.refund_ticket_infos = refund_ticket_infos
        self.train_no = train_no

    def validate(self):
        if self.refund_ticket_infos:
            for v1 in self.refund_ticket_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station_name is not None:
            result['arr_station_name'] = self.arr_station_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_station_name is not None:
            result['dep_station_name'] = self.dep_station_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        result['refund_ticket_infos'] = []
        if self.refund_ticket_infos is not None:
            for k1 in self.refund_ticket_infos:
                result['refund_ticket_infos'].append(k1.to_map() if k1 else None)

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station_name') is not None:
            self.arr_station_name = m.get('arr_station_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_station_name') is not None:
            self.dep_station_name = m.get('dep_station_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        self.refund_ticket_infos = []
        if m.get('refund_ticket_infos') is not None:
            for k1 in m.get('refund_ticket_infos'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleRefundInfosRefundTrainInfoRefundTicketInfos()
                self.refund_ticket_infos.append(temp_model.from_map(k1))

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainOrderDetailQueryResponseBodyModuleRefundInfosRefundTrainInfoRefundTicketInfos(DaraModel):
    def __init__(
        self,
        passenger_id: str = None,
        refund_cost: int = None,
        refund_price: int = None,
        ticket_price: int = None,
    ):
        self.passenger_id = passenger_id
        self.refund_cost = refund_cost
        self.refund_price = refund_price
        self.ticket_price = ticket_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.refund_cost is not None:
            result['refund_cost'] = self.refund_cost

        if self.refund_price is not None:
            result['refund_price'] = self.refund_price

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('refund_cost') is not None:
            self.refund_cost = m.get('refund_cost')

        if m.get('refund_price') is not None:
            self.refund_price = m.get('refund_price')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        return self

class TrainOrderDetailQueryResponseBodyModulePassengerInfoS(DaraModel):
    def __init__(
        self,
        cost_center_info: main_models.TrainOrderDetailQueryResponseBodyModulePassengerInfoSCostCenterInfo = None,
        country_code: str = None,
        passenger_cert_no: str = None,
        passenger_cert_type: str = None,
        passenger_id: str = None,
        passenger_mobile: str = None,
        passenger_name: str = None,
        valid_date_end: str = None,
    ):
        self.cost_center_info = cost_center_info
        self.country_code = country_code
        self.passenger_cert_no = passenger_cert_no
        self.passenger_cert_type = passenger_cert_type
        self.passenger_id = passenger_id
        self.passenger_mobile = passenger_mobile
        self.passenger_name = passenger_name
        self.valid_date_end = valid_date_end

    def validate(self):
        if self.cost_center_info:
            self.cost_center_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_info is not None:
            result['cost_center_info'] = self.cost_center_info.to_map()

        if self.country_code is not None:
            result['country_code'] = self.country_code

        if self.passenger_cert_no is not None:
            result['passenger_cert_no'] = self.passenger_cert_no

        if self.passenger_cert_type is not None:
            result['passenger_cert_type'] = self.passenger_cert_type

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.passenger_mobile is not None:
            result['passenger_mobile'] = self.passenger_mobile

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.valid_date_end is not None:
            result['valid_date_end'] = self.valid_date_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_info') is not None:
            temp_model = main_models.TrainOrderDetailQueryResponseBodyModulePassengerInfoSCostCenterInfo()
            self.cost_center_info = temp_model.from_map(m.get('cost_center_info'))

        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        if m.get('passenger_cert_no') is not None:
            self.passenger_cert_no = m.get('passenger_cert_no')

        if m.get('passenger_cert_type') is not None:
            self.passenger_cert_type = m.get('passenger_cert_type')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('passenger_mobile') is not None:
            self.passenger_mobile = m.get('passenger_mobile')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('valid_date_end') is not None:
            self.valid_date_end = m.get('valid_date_end')

        return self

class TrainOrderDetailQueryResponseBodyModulePassengerInfoSCostCenterInfo(DaraModel):
    def __init__(
        self,
        cascade_dept_name: str = None,
        cost_center_id: str = None,
        cost_center_name: str = None,
        cost_center_no: str = None,
        depart_id: str = None,
        depart_name: str = None,
        invoice_id: str = None,
        invoice_title: str = None,
        passenger_id: str = None,
        project_code: str = None,
        project_title: str = None,
    ):
        self.cascade_dept_name = cascade_dept_name
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_no = cost_center_no
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.invoice_id = invoice_id
        self.invoice_title = invoice_title
        self.passenger_id = passenger_id
        self.project_code = project_code
        self.project_title = project_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascade_dept_name is not None:
            result['cascade_dept_name'] = self.cascade_dept_name

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.cost_center_no is not None:
            result['cost_center_no'] = self.cost_center_no

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cascade_dept_name') is not None:
            self.cascade_dept_name = m.get('cascade_dept_name')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_no') is not None:
            self.cost_center_no = m.get('cost_center_no')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        return self

class TrainOrderDetailQueryResponseBodyModuleOfflineRefundDetails(DaraModel):
    def __init__(
        self,
        offline_refund_id: str = None,
        offline_refund_infos: List[main_models.TrainOrderDetailQueryResponseBodyModuleOfflineRefundDetailsOfflineRefundInfos] = None,
        offline_refund_type: str = None,
        refund_total_price: int = None,
    ):
        self.offline_refund_id = offline_refund_id
        self.offline_refund_infos = offline_refund_infos
        self.offline_refund_type = offline_refund_type
        self.refund_total_price = refund_total_price

    def validate(self):
        if self.offline_refund_infos:
            for v1 in self.offline_refund_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.offline_refund_id is not None:
            result['offline_refund_id'] = self.offline_refund_id

        result['offline_refund_infos'] = []
        if self.offline_refund_infos is not None:
            for k1 in self.offline_refund_infos:
                result['offline_refund_infos'].append(k1.to_map() if k1 else None)

        if self.offline_refund_type is not None:
            result['offline_refund_type'] = self.offline_refund_type

        if self.refund_total_price is not None:
            result['refund_total_price'] = self.refund_total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offline_refund_id') is not None:
            self.offline_refund_id = m.get('offline_refund_id')

        self.offline_refund_infos = []
        if m.get('offline_refund_infos') is not None:
            for k1 in m.get('offline_refund_infos'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleOfflineRefundDetailsOfflineRefundInfos()
                self.offline_refund_infos.append(temp_model.from_map(k1))

        if m.get('offline_refund_type') is not None:
            self.offline_refund_type = m.get('offline_refund_type')

        if m.get('refund_total_price') is not None:
            self.refund_total_price = m.get('refund_total_price')

        return self

class TrainOrderDetailQueryResponseBodyModuleOfflineRefundDetailsOfflineRefundInfos(DaraModel):
    def __init__(
        self,
        passenger_id: str = None,
        refund_price: int = None,
    ):
        self.passenger_id = passenger_id
        self.refund_price = refund_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.refund_price is not None:
            result['refund_price'] = self.refund_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('refund_price') is not None:
            self.refund_price = m.get('refund_price')

        return self

class TrainOrderDetailQueryResponseBodyModuleChangeInfos(DaraModel):
    def __init__(
        self,
        change_apply_id: str = None,
        change_train_infos: List[main_models.TrainOrderDetailQueryResponseBodyModuleChangeInfosChangeTrainInfos] = None,
        limit_pay_time: str = None,
        out_change_apply_id: str = None,
        status: str = None,
    ):
        self.change_apply_id = change_apply_id
        self.change_train_infos = change_train_infos
        self.limit_pay_time = limit_pay_time
        self.out_change_apply_id = out_change_apply_id
        self.status = status

    def validate(self):
        if self.change_train_infos:
            for v1 in self.change_train_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_apply_id is not None:
            result['change_apply_id'] = self.change_apply_id

        result['change_train_infos'] = []
        if self.change_train_infos is not None:
            for k1 in self.change_train_infos:
                result['change_train_infos'].append(k1.to_map() if k1 else None)

        if self.limit_pay_time is not None:
            result['limit_pay_time'] = self.limit_pay_time

        if self.out_change_apply_id is not None:
            result['out_change_apply_id'] = self.out_change_apply_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_apply_id') is not None:
            self.change_apply_id = m.get('change_apply_id')

        self.change_train_infos = []
        if m.get('change_train_infos') is not None:
            for k1 in m.get('change_train_infos'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleChangeInfosChangeTrainInfos()
                self.change_train_infos.append(temp_model.from_map(k1))

        if m.get('limit_pay_time') is not None:
            self.limit_pay_time = m.get('limit_pay_time')

        if m.get('out_change_apply_id') is not None:
            self.out_change_apply_id = m.get('out_change_apply_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class TrainOrderDetailQueryResponseBodyModuleChangeInfosChangeTrainInfos(DaraModel):
    def __init__(
        self,
        arr_station_code: str = None,
        arr_station_name: str = None,
        arrive_time: str = None,
        change_ticket_infos: List[main_models.TrainOrderDetailQueryResponseBodyModuleChangeInfosChangeTrainInfosChangeTicketInfos] = None,
        dep_station_code: str = None,
        dep_station_name: str = None,
        dep_time: str = None,
        train_no: str = None,
    ):
        self.arr_station_code = arr_station_code
        self.arr_station_name = arr_station_name
        self.arrive_time = arrive_time
        self.change_ticket_infos = change_ticket_infos
        self.dep_station_code = dep_station_code
        self.dep_station_name = dep_station_name
        self.dep_time = dep_time
        self.train_no = train_no

    def validate(self):
        if self.change_ticket_infos:
            for v1 in self.change_ticket_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station_code is not None:
            result['arr_station_code'] = self.arr_station_code

        if self.arr_station_name is not None:
            result['arr_station_name'] = self.arr_station_name

        if self.arrive_time is not None:
            result['arrive_time'] = self.arrive_time

        result['change_ticket_infos'] = []
        if self.change_ticket_infos is not None:
            for k1 in self.change_ticket_infos:
                result['change_ticket_infos'].append(k1.to_map() if k1 else None)

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_station_name is not None:
            result['dep_station_name'] = self.dep_station_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station_code') is not None:
            self.arr_station_code = m.get('arr_station_code')

        if m.get('arr_station_name') is not None:
            self.arr_station_name = m.get('arr_station_name')

        if m.get('arrive_time') is not None:
            self.arrive_time = m.get('arrive_time')

        self.change_ticket_infos = []
        if m.get('change_ticket_infos') is not None:
            for k1 in m.get('change_ticket_infos'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleChangeInfosChangeTrainInfosChangeTicketInfos()
                self.change_ticket_infos.append(temp_model.from_map(k1))

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_station_name') is not None:
            self.dep_station_name = m.get('dep_station_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainOrderDetailQueryResponseBodyModuleChangeInfosChangeTrainInfosChangeTicketInfos(DaraModel):
    def __init__(
        self,
        change_cost: int = None,
        change_diff: int = None,
        change_gap_handing_fee: int = None,
        change_min_ticket_amount_handing_fee: int = None,
        coach_no: str = None,
        fail_code: str = None,
        fail_reason: str = None,
        passenger_id: str = None,
        real_ticket_price: int = None,
        seat_no: str = None,
        seat_type: str = None,
        ticket_entrance: str = None,
        ticket_price: int = None,
        ticket_status: str = None,
    ):
        self.change_cost = change_cost
        self.change_diff = change_diff
        self.change_gap_handing_fee = change_gap_handing_fee
        self.change_min_ticket_amount_handing_fee = change_min_ticket_amount_handing_fee
        self.coach_no = coach_no
        self.fail_code = fail_code
        self.fail_reason = fail_reason
        self.passenger_id = passenger_id
        self.real_ticket_price = real_ticket_price
        self.seat_no = seat_no
        self.seat_type = seat_type
        self.ticket_entrance = ticket_entrance
        self.ticket_price = ticket_price
        self.ticket_status = ticket_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_cost is not None:
            result['change_cost'] = self.change_cost

        if self.change_diff is not None:
            result['change_diff'] = self.change_diff

        if self.change_gap_handing_fee is not None:
            result['change_gap_handing_fee'] = self.change_gap_handing_fee

        if self.change_min_ticket_amount_handing_fee is not None:
            result['change_min_ticket_amount_handing_fee'] = self.change_min_ticket_amount_handing_fee

        if self.coach_no is not None:
            result['coach_no'] = self.coach_no

        if self.fail_code is not None:
            result['fail_code'] = self.fail_code

        if self.fail_reason is not None:
            result['fail_reason'] = self.fail_reason

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.real_ticket_price is not None:
            result['real_ticket_price'] = self.real_ticket_price

        if self.seat_no is not None:
            result['seat_no'] = self.seat_no

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

        if self.ticket_entrance is not None:
            result['ticket_entrance'] = self.ticket_entrance

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_cost') is not None:
            self.change_cost = m.get('change_cost')

        if m.get('change_diff') is not None:
            self.change_diff = m.get('change_diff')

        if m.get('change_gap_handing_fee') is not None:
            self.change_gap_handing_fee = m.get('change_gap_handing_fee')

        if m.get('change_min_ticket_amount_handing_fee') is not None:
            self.change_min_ticket_amount_handing_fee = m.get('change_min_ticket_amount_handing_fee')

        if m.get('coach_no') is not None:
            self.coach_no = m.get('coach_no')

        if m.get('fail_code') is not None:
            self.fail_code = m.get('fail_code')

        if m.get('fail_reason') is not None:
            self.fail_reason = m.get('fail_reason')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('real_ticket_price') is not None:
            self.real_ticket_price = m.get('real_ticket_price')

        if m.get('seat_no') is not None:
            self.seat_no = m.get('seat_no')

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

        if m.get('ticket_entrance') is not None:
            self.ticket_entrance = m.get('ticket_entrance')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')

        return self

class TrainOrderDetailQueryResponseBodyModuleBookInfos(DaraModel):
    def __init__(
        self,
        book_train_infos: List[main_models.TrainOrderDetailQueryResponseBodyModuleBookInfosBookTrainInfos] = None,
        fail_code: str = None,
        fail_msg: str = None,
        last_pay_time: str = None,
        status: int = None,
        ticket_no: str = None,
    ):
        self.book_train_infos = book_train_infos
        self.fail_code = fail_code
        self.fail_msg = fail_msg
        self.last_pay_time = last_pay_time
        self.status = status
        self.ticket_no = ticket_no

    def validate(self):
        if self.book_train_infos:
            for v1 in self.book_train_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['book_train_infos'] = []
        if self.book_train_infos is not None:
            for k1 in self.book_train_infos:
                result['book_train_infos'].append(k1.to_map() if k1 else None)

        if self.fail_code is not None:
            result['fail_code'] = self.fail_code

        if self.fail_msg is not None:
            result['fail_msg'] = self.fail_msg

        if self.last_pay_time is not None:
            result['last_pay_time'] = self.last_pay_time

        if self.status is not None:
            result['status'] = self.status

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.book_train_infos = []
        if m.get('book_train_infos') is not None:
            for k1 in m.get('book_train_infos'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleBookInfosBookTrainInfos()
                self.book_train_infos.append(temp_model.from_map(k1))

        if m.get('fail_code') is not None:
            self.fail_code = m.get('fail_code')

        if m.get('fail_msg') is not None:
            self.fail_msg = m.get('fail_msg')

        if m.get('last_pay_time') is not None:
            self.last_pay_time = m.get('last_pay_time')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        return self

class TrainOrderDetailQueryResponseBodyModuleBookInfosBookTrainInfos(DaraModel):
    def __init__(
        self,
        arr_station_code: str = None,
        arr_station_name: str = None,
        arrive_time: str = None,
        book_ticket_infos: List[main_models.TrainOrderDetailQueryResponseBodyModuleBookInfosBookTrainInfosBookTicketInfos] = None,
        dep_station_code: str = None,
        dep_station_name: str = None,
        dep_time: str = None,
        train_no: str = None,
    ):
        self.arr_station_code = arr_station_code
        self.arr_station_name = arr_station_name
        self.arrive_time = arrive_time
        self.book_ticket_infos = book_ticket_infos
        self.dep_station_code = dep_station_code
        self.dep_station_name = dep_station_name
        self.dep_time = dep_time
        self.train_no = train_no

    def validate(self):
        if self.book_ticket_infos:
            for v1 in self.book_ticket_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station_code is not None:
            result['arr_station_code'] = self.arr_station_code

        if self.arr_station_name is not None:
            result['arr_station_name'] = self.arr_station_name

        if self.arrive_time is not None:
            result['arrive_time'] = self.arrive_time

        result['book_ticket_infos'] = []
        if self.book_ticket_infos is not None:
            for k1 in self.book_ticket_infos:
                result['book_ticket_infos'].append(k1.to_map() if k1 else None)

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_station_name is not None:
            result['dep_station_name'] = self.dep_station_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station_code') is not None:
            self.arr_station_code = m.get('arr_station_code')

        if m.get('arr_station_name') is not None:
            self.arr_station_name = m.get('arr_station_name')

        if m.get('arrive_time') is not None:
            self.arrive_time = m.get('arrive_time')

        self.book_ticket_infos = []
        if m.get('book_ticket_infos') is not None:
            for k1 in m.get('book_ticket_infos'):
                temp_model = main_models.TrainOrderDetailQueryResponseBodyModuleBookInfosBookTrainInfosBookTicketInfos()
                self.book_ticket_infos.append(temp_model.from_map(k1))

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_station_name') is not None:
            self.dep_station_name = m.get('dep_station_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainOrderDetailQueryResponseBodyModuleBookInfosBookTrainInfosBookTicketInfos(DaraModel):
    def __init__(
        self,
        coach_no: str = None,
        fail_code: str = None,
        fail_reason: str = None,
        passenger_id: str = None,
        real_ticket_price: int = None,
        seat_no: str = None,
        seat_type: str = None,
        ticket_entrance: str = None,
        ticket_price: int = None,
        ticket_status: int = None,
        ticket_type: str = None,
    ):
        self.coach_no = coach_no
        self.fail_code = fail_code
        self.fail_reason = fail_reason
        self.passenger_id = passenger_id
        self.real_ticket_price = real_ticket_price
        self.seat_no = seat_no
        self.seat_type = seat_type
        self.ticket_entrance = ticket_entrance
        self.ticket_price = ticket_price
        self.ticket_status = ticket_status
        self.ticket_type = ticket_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coach_no is not None:
            result['coach_no'] = self.coach_no

        if self.fail_code is not None:
            result['fail_code'] = self.fail_code

        if self.fail_reason is not None:
            result['fail_reason'] = self.fail_reason

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.real_ticket_price is not None:
            result['real_ticket_price'] = self.real_ticket_price

        if self.seat_no is not None:
            result['seat_no'] = self.seat_no

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

        if self.ticket_entrance is not None:
            result['ticket_entrance'] = self.ticket_entrance

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status

        if self.ticket_type is not None:
            result['ticket_type'] = self.ticket_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('coach_no') is not None:
            self.coach_no = m.get('coach_no')

        if m.get('fail_code') is not None:
            self.fail_code = m.get('fail_code')

        if m.get('fail_reason') is not None:
            self.fail_reason = m.get('fail_reason')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('real_ticket_price') is not None:
            self.real_ticket_price = m.get('real_ticket_price')

        if m.get('seat_no') is not None:
            self.seat_no = m.get('seat_no')

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

        if m.get('ticket_entrance') is not None:
            self.ticket_entrance = m.get('ticket_entrance')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')

        if m.get('ticket_type') is not None:
            self.ticket_type = m.get('ticket_type')

        return self

