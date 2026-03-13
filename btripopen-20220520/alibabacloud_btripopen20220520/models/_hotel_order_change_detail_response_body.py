# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderChangeDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelOrderChangeDetailResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
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
            temp_model = main_models.HotelOrderChangeDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelOrderChangeDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        change_order_id: str = None,
        change_type: int = None,
        corp_id: str = None,
        dis_order_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        reason: str = None,
        remarks: str = None,
        room_info_list: List[main_models.HotelOrderChangeDetailResponseBodyModuleRoomInfoList] = None,
        sale_order_id: str = None,
        source: int = None,
        status: int = None,
        work_order_id: str = None,
    ):
        self.change_order_id = change_order_id
        self.change_type = change_type
        self.corp_id = corp_id
        self.dis_order_id = dis_order_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.reason = reason
        self.remarks = remarks
        self.room_info_list = room_info_list
        self.sale_order_id = sale_order_id
        self.source = source
        self.status = status
        self.work_order_id = work_order_id

    def validate(self):
        if self.room_info_list:
            for v1 in self.room_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_id is not None:
            result['change_order_id'] = self.change_order_id

        if self.change_type is not None:
            result['change_type'] = self.change_type

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.reason is not None:
            result['reason'] = self.reason

        if self.remarks is not None:
            result['remarks'] = self.remarks

        result['room_info_list'] = []
        if self.room_info_list is not None:
            for k1 in self.room_info_list:
                result['room_info_list'].append(k1.to_map() if k1 else None)

        if self.sale_order_id is not None:
            result['sale_order_id'] = self.sale_order_id

        if self.source is not None:
            result['source'] = self.source

        if self.status is not None:
            result['status'] = self.status

        if self.work_order_id is not None:
            result['work_order_id'] = self.work_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_order_id') is not None:
            self.change_order_id = m.get('change_order_id')

        if m.get('change_type') is not None:
            self.change_type = m.get('change_type')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')

        self.room_info_list = []
        if m.get('room_info_list') is not None:
            for k1 in m.get('room_info_list'):
                temp_model = main_models.HotelOrderChangeDetailResponseBodyModuleRoomInfoList()
                self.room_info_list.append(temp_model.from_map(k1))

        if m.get('sale_order_id') is not None:
            self.sale_order_id = m.get('sale_order_id')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('work_order_id') is not None:
            self.work_order_id = m.get('work_order_id')

        return self

class HotelOrderChangeDetailResponseBodyModuleRoomInfoList(DaraModel):
    def __init__(
        self,
        cancel_date: List[str] = None,
        room_daily_refund_infos: List[main_models.HotelOrderChangeDetailResponseBodyModuleRoomInfoListRoomDailyRefundInfos] = None,
        room_no: int = None,
    ):
        self.cancel_date = cancel_date
        self.room_daily_refund_infos = room_daily_refund_infos
        self.room_no = room_no

    def validate(self):
        if self.room_daily_refund_infos:
            for v1 in self.room_daily_refund_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_date is not None:
            result['cancel_date'] = self.cancel_date

        result['room_daily_refund_infos'] = []
        if self.room_daily_refund_infos is not None:
            for k1 in self.room_daily_refund_infos:
                result['room_daily_refund_infos'].append(k1.to_map() if k1 else None)

        if self.room_no is not None:
            result['room_no'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancel_date') is not None:
            self.cancel_date = m.get('cancel_date')

        self.room_daily_refund_infos = []
        if m.get('room_daily_refund_infos') is not None:
            for k1 in m.get('room_daily_refund_infos'):
                temp_model = main_models.HotelOrderChangeDetailResponseBodyModuleRoomInfoListRoomDailyRefundInfos()
                self.room_daily_refund_infos.append(temp_model.from_map(k1))

        if m.get('room_no') is not None:
            self.room_no = m.get('room_no')

        return self

class HotelOrderChangeDetailResponseBodyModuleRoomInfoListRoomDailyRefundInfos(DaraModel):
    def __init__(
        self,
        check_in_date: str = None,
        penalty_price: int = None,
        price: int = None,
        refund_price: int = None,
    ):
        self.check_in_date = check_in_date
        self.penalty_price = penalty_price
        self.price = price
        self.refund_price = refund_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_in_date is not None:
            result['check_in_date'] = self.check_in_date

        if self.penalty_price is not None:
            result['penalty_price'] = self.penalty_price

        if self.price is not None:
            result['price'] = self.price

        if self.refund_price is not None:
            result['refund_price'] = self.refund_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_in_date') is not None:
            self.check_in_date = m.get('check_in_date')

        if m.get('penalty_price') is not None:
            self.penalty_price = m.get('penalty_price')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('refund_price') is not None:
            self.refund_price = m.get('refund_price')

        return self

