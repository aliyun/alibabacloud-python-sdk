# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightSegmentAvailableCertResponseBody(DaraModel):
    def __init__(
        self,
        module: main_models.IntlFlightSegmentAvailableCertResponseBodyModule = None,
        request_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.module = module
        self.request_id = request_id
        self.result_code = result_code
        self.result_msg = result_msg
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
        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_code is not None:
            result['result_code'] = self.result_code

        if self.result_msg is not None:
            result['result_msg'] = self.result_msg

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = main_models.IntlFlightSegmentAvailableCertResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')

        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightSegmentAvailableCertResponseBodyModule(DaraModel):
    def __init__(
        self,
        segment_available_cert_list: List[main_models.IntlFlightSegmentAvailableCertResponseBodyModuleSegmentAvailableCertList] = None,
    ):
        self.segment_available_cert_list = segment_available_cert_list

    def validate(self):
        if self.segment_available_cert_list:
            for v1 in self.segment_available_cert_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['segment_available_cert_list'] = []
        if self.segment_available_cert_list is not None:
            for k1 in self.segment_available_cert_list:
                result['segment_available_cert_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.segment_available_cert_list = []
        if m.get('segment_available_cert_list') is not None:
            for k1 in m.get('segment_available_cert_list'):
                temp_model = main_models.IntlFlightSegmentAvailableCertResponseBodyModuleSegmentAvailableCertList()
                self.segment_available_cert_list.append(temp_model.from_map(k1))

        return self

class IntlFlightSegmentAvailableCertResponseBodyModuleSegmentAvailableCertList(DaraModel):
    def __init__(
        self,
        cert_types: List[int] = None,
        segment_position: main_models.IntlFlightSegmentAvailableCertResponseBodyModuleSegmentAvailableCertListSegmentPosition = None,
    ):
        self.cert_types = cert_types
        self.segment_position = segment_position

    def validate(self):
        if self.segment_position:
            self.segment_position.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_types is not None:
            result['cert_types'] = self.cert_types

        if self.segment_position is not None:
            result['segment_position'] = self.segment_position.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_types') is not None:
            self.cert_types = m.get('cert_types')

        if m.get('segment_position') is not None:
            temp_model = main_models.IntlFlightSegmentAvailableCertResponseBodyModuleSegmentAvailableCertListSegmentPosition()
            self.segment_position = temp_model.from_map(m.get('segment_position'))

        return self

class IntlFlightSegmentAvailableCertResponseBodyModuleSegmentAvailableCertListSegmentPosition(DaraModel):
    def __init__(
        self,
        journey_index: int = None,
        segment_index: int = None,
    ):
        self.journey_index = journey_index
        self.segment_index = segment_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        return self

