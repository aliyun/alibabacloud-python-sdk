# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightRefundConsultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IntlFlightRefundConsultResponseBodyModule = None,
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
            temp_model = main_models.IntlFlightRefundConsultResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightRefundConsultResponseBodyModule(DaraModel):
    def __init__(
        self,
        passenger_journey_group_info_list: List[main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoList] = None,
    ):
        self.passenger_journey_group_info_list = passenger_journey_group_info_list

    def validate(self):
        if self.passenger_journey_group_info_list:
            for v1 in self.passenger_journey_group_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['passenger_journey_group_info_list'] = []
        if self.passenger_journey_group_info_list is not None:
            for k1 in self.passenger_journey_group_info_list:
                result['passenger_journey_group_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.passenger_journey_group_info_list = []
        if m.get('passenger_journey_group_info_list') is not None:
            for k1 in m.get('passenger_journey_group_info_list'):
                temp_model = main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoList()
                self.passenger_journey_group_info_list.append(temp_model.from_map(k1))

        return self

class IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoList(DaraModel):
    def __init__(
        self,
        passenger_journey_group_key: str = None,
        passenger_list: List[main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListPassengerList] = None,
        passenger_segment_status_info_list: List[main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListPassengerSegmentStatusInfoList] = None,
        refund_reason_info_list: List[main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListRefundReasonInfoList] = None,
        segment_list: List[main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListSegmentList] = None,
    ):
        self.passenger_journey_group_key = passenger_journey_group_key
        self.passenger_list = passenger_list
        self.passenger_segment_status_info_list = passenger_segment_status_info_list
        self.refund_reason_info_list = refund_reason_info_list
        self.segment_list = segment_list

    def validate(self):
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()
        if self.passenger_segment_status_info_list:
            for v1 in self.passenger_segment_status_info_list:
                 if v1:
                    v1.validate()
        if self.refund_reason_info_list:
            for v1 in self.refund_reason_info_list:
                 if v1:
                    v1.validate()
        if self.segment_list:
            for v1 in self.segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_journey_group_key is not None:
            result['passenger_journey_group_key'] = self.passenger_journey_group_key

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        result['passenger_segment_status_info_list'] = []
        if self.passenger_segment_status_info_list is not None:
            for k1 in self.passenger_segment_status_info_list:
                result['passenger_segment_status_info_list'].append(k1.to_map() if k1 else None)

        result['refund_reason_info_list'] = []
        if self.refund_reason_info_list is not None:
            for k1 in self.refund_reason_info_list:
                result['refund_reason_info_list'].append(k1.to_map() if k1 else None)

        result['segment_list'] = []
        if self.segment_list is not None:
            for k1 in self.segment_list:
                result['segment_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_journey_group_key') is not None:
            self.passenger_journey_group_key = m.get('passenger_journey_group_key')

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListPassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        self.passenger_segment_status_info_list = []
        if m.get('passenger_segment_status_info_list') is not None:
            for k1 in m.get('passenger_segment_status_info_list'):
                temp_model = main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListPassengerSegmentStatusInfoList()
                self.passenger_segment_status_info_list.append(temp_model.from_map(k1))

        self.refund_reason_info_list = []
        if m.get('refund_reason_info_list') is not None:
            for k1 in m.get('refund_reason_info_list'):
                temp_model = main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListRefundReasonInfoList()
                self.refund_reason_info_list.append(temp_model.from_map(k1))

        self.segment_list = []
        if m.get('segment_list') is not None:
            for k1 in m.get('segment_list'):
                temp_model = main_models.IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        return self

class IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListSegmentList(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        dep_city_code: str = None,
        dep_time: str = None,
        flight_no: str = None,
        journey_index: int = None,
        segment_index: int = None,
        segment_key: str = None,
    ):
        self.arr_city_code = arr_city_code
        self.dep_city_code = dep_city_code
        self.dep_time = dep_time
        self.flight_no = flight_no
        self.journey_index = journey_index
        self.segment_index = segment_index
        self.segment_key = segment_key

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

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.segment_key is not None:
            result['segment_key'] = self.segment_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('segment_key') is not None:
            self.segment_key = m.get('segment_key')

        return self

class IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListRefundReasonInfoList(DaraModel):
    def __init__(
        self,
        reason_code: str = None,
        reason_desc: str = None,
        voluntary: bool = None,
    ):
        self.reason_code = reason_code
        self.reason_desc = reason_desc
        self.voluntary = voluntary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason_code is not None:
            result['reason_code'] = self.reason_code

        if self.reason_desc is not None:
            result['reason_desc'] = self.reason_desc

        if self.voluntary is not None:
            result['voluntary'] = self.voluntary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reason_code') is not None:
            self.reason_code = m.get('reason_code')

        if m.get('reason_desc') is not None:
            self.reason_desc = m.get('reason_desc')

        if m.get('voluntary') is not None:
            self.voluntary = m.get('voluntary')

        return self

class IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListPassengerSegmentStatusInfoList(DaraModel):
    def __init__(
        self,
        can_refund: bool = None,
        passenger_id: int = None,
        segment_key: str = None,
        un_refund_reason: str = None,
        un_refund_reason_code: str = None,
    ):
        self.can_refund = can_refund
        self.passenger_id = passenger_id
        self.segment_key = segment_key
        self.un_refund_reason = un_refund_reason
        self.un_refund_reason_code = un_refund_reason_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_refund is not None:
            result['can_refund'] = self.can_refund

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.segment_key is not None:
            result['segment_key'] = self.segment_key

        if self.un_refund_reason is not None:
            result['un_refund_reason'] = self.un_refund_reason

        if self.un_refund_reason_code is not None:
            result['un_refund_reason_code'] = self.un_refund_reason_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('can_refund') is not None:
            self.can_refund = m.get('can_refund')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('segment_key') is not None:
            self.segment_key = m.get('segment_key')

        if m.get('un_refund_reason') is not None:
            self.un_refund_reason = m.get('un_refund_reason')

        if m.get('un_refund_reason_code') is not None:
            self.un_refund_reason_code = m.get('un_refund_reason_code')

        return self

class IntlFlightRefundConsultResponseBodyModulePassengerJourneyGroupInfoListPassengerList(DaraModel):
    def __init__(
        self,
        full_name: str = None,
        passenger_id: int = None,
    ):
        self.full_name = full_name
        self.passenger_id = passenger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_name is not None:
            result['full_name'] = self.full_name

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('full_name') is not None:
            self.full_name = m.get('full_name')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        return self

