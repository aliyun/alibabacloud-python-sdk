# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightInventoryPriceCheckResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IntlFlightInventoryPriceCheckResponseBodyModule = None,
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
            temp_model = main_models.IntlFlightInventoryPriceCheckResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightInventoryPriceCheckResponseBodyModule(DaraModel):
    def __init__(
        self,
        check_success: bool = None,
        fail_type: int = None,
        passenger_changed_price_info_list: List[main_models.IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoList] = None,
        render_key: str = None,
    ):
        self.check_success = check_success
        self.fail_type = fail_type
        self.passenger_changed_price_info_list = passenger_changed_price_info_list
        self.render_key = render_key

    def validate(self):
        if self.passenger_changed_price_info_list:
            for v1 in self.passenger_changed_price_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_success is not None:
            result['check_success'] = self.check_success

        if self.fail_type is not None:
            result['fail_type'] = self.fail_type

        result['passenger_changed_price_info_list'] = []
        if self.passenger_changed_price_info_list is not None:
            for k1 in self.passenger_changed_price_info_list:
                result['passenger_changed_price_info_list'].append(k1.to_map() if k1 else None)

        if self.render_key is not None:
            result['render_key'] = self.render_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_success') is not None:
            self.check_success = m.get('check_success')

        if m.get('fail_type') is not None:
            self.fail_type = m.get('fail_type')

        self.passenger_changed_price_info_list = []
        if m.get('passenger_changed_price_info_list') is not None:
            for k1 in m.get('passenger_changed_price_info_list'):
                temp_model = main_models.IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoList()
                self.passenger_changed_price_info_list.append(temp_model.from_map(k1))

        if m.get('render_key') is not None:
            self.render_key = m.get('render_key')

        return self

class IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoList(DaraModel):
    def __init__(
        self,
        changed: bool = None,
        changed_price: main_models.IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoListChangedPrice = None,
        original_price: main_models.IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoListOriginalPrice = None,
        passenger_type: int = None,
    ):
        self.changed = changed
        self.changed_price = changed_price
        self.original_price = original_price
        self.passenger_type = passenger_type

    def validate(self):
        if self.changed_price:
            self.changed_price.validate()
        if self.original_price:
            self.original_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changed is not None:
            result['changed'] = self.changed

        if self.changed_price is not None:
            result['changed_price'] = self.changed_price.to_map()

        if self.original_price is not None:
            result['original_price'] = self.original_price.to_map()

        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changed') is not None:
            self.changed = m.get('changed')

        if m.get('changed_price') is not None:
            temp_model = main_models.IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoListChangedPrice()
            self.changed_price = temp_model.from_map(m.get('changed_price'))

        if m.get('original_price') is not None:
            temp_model = main_models.IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoListOriginalPrice()
            self.original_price = temp_model.from_map(m.get('original_price'))

        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        return self

class IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoListOriginalPrice(DaraModel):
    def __init__(
        self,
        tax_price: int = None,
        ticket_price: int = None,
    ):
        self.tax_price = tax_price
        self.ticket_price = ticket_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tax_price is not None:
            result['tax_price'] = self.tax_price

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tax_price') is not None:
            self.tax_price = m.get('tax_price')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        return self

class IntlFlightInventoryPriceCheckResponseBodyModulePassengerChangedPriceInfoListChangedPrice(DaraModel):
    def __init__(
        self,
        tax_price: int = None,
        ticket_price: int = None,
    ):
        self.tax_price = tax_price
        self.ticket_price = ticket_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tax_price is not None:
            result['tax_price'] = self.tax_price

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tax_price') is not None:
            self.tax_price = m.get('tax_price')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        return self

