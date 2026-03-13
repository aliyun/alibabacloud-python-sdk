# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ElectronicItineraryGetApplyResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: main_models.ElectronicItineraryGetApplyResultResponseBodyModule = None,
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
            temp_model = main_models.ElectronicItineraryGetApplyResultResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class ElectronicItineraryGetApplyResultResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_ticket_list: List[main_models.ElectronicItineraryGetApplyResultResponseBodyModuleApplyTicketList] = None,
        batch_apply_no: str = None,
    ):
        self.apply_ticket_list = apply_ticket_list
        self.batch_apply_no = batch_apply_no

    def validate(self):
        if self.apply_ticket_list:
            for v1 in self.apply_ticket_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apply_ticket_list'] = []
        if self.apply_ticket_list is not None:
            for k1 in self.apply_ticket_list:
                result['apply_ticket_list'].append(k1.to_map() if k1 else None)

        if self.batch_apply_no is not None:
            result['batch_apply_no'] = self.batch_apply_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_ticket_list = []
        if m.get('apply_ticket_list') is not None:
            for k1 in m.get('apply_ticket_list'):
                temp_model = main_models.ElectronicItineraryGetApplyResultResponseBodyModuleApplyTicketList()
                self.apply_ticket_list.append(temp_model.from_map(k1))

        if m.get('batch_apply_no') is not None:
            self.batch_apply_no = m.get('batch_apply_no')

        return self

class ElectronicItineraryGetApplyResultResponseBodyModuleApplyTicketList(DaraModel):
    def __init__(
        self,
        failed_code: int = None,
        failed_reason: str = None,
        itinerary_status: int = None,
        remark: str = None,
        ticket_no: str = None,
    ):
        self.failed_code = failed_code
        self.failed_reason = failed_reason
        self.itinerary_status = itinerary_status
        self.remark = remark
        self.ticket_no = ticket_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_code is not None:
            result['failed_code'] = self.failed_code

        if self.failed_reason is not None:
            result['failed_reason'] = self.failed_reason

        if self.itinerary_status is not None:
            result['itinerary_status'] = self.itinerary_status

        if self.remark is not None:
            result['remark'] = self.remark

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failed_code') is not None:
            self.failed_code = m.get('failed_code')

        if m.get('failed_reason') is not None:
            self.failed_reason = m.get('failed_reason')

        if m.get('itinerary_status') is not None:
            self.itinerary_status = m.get('itinerary_status')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        return self

