# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class SendRCSResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.SendRCSResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.SendRCSResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SendRCSResponseBodyData(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        bdcust: str = None,
        code: str = None,
        debug: Dict[str, Any] = None,
        e: str = None,
        extend_map: Dict[str, Any] = None,
        gate_fail_msg: str = None,
        key_string: str = None,
        message: str = None,
        module: Dict[str, Any] = None,
        partner_id: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.bdcust = bdcust
        self.code = code
        self.debug = debug
        self.e = e
        self.extend_map = extend_map
        self.gate_fail_msg = gate_fail_msg
        self.key_string = key_string
        self.message = message
        self.module = module
        self.partner_id = partner_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.bdcust is not None:
            result['Bdcust'] = self.bdcust

        if self.code is not None:
            result['Code'] = self.code

        if self.debug is not None:
            result['Debug'] = self.debug

        if self.e is not None:
            result['E'] = self.e

        if self.extend_map is not None:
            result['ExtendMap'] = self.extend_map

        if self.gate_fail_msg is not None:
            result['GateFailMsg'] = self.gate_fail_msg

        if self.key_string is not None:
            result['KeyString'] = self.key_string

        if self.message is not None:
            result['Message'] = self.message

        if self.module is not None:
            result['Module'] = self.module

        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Bdcust') is not None:
            self.bdcust = m.get('Bdcust')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Debug') is not None:
            self.debug = m.get('Debug')

        if m.get('E') is not None:
            self.e = m.get('E')

        if m.get('ExtendMap') is not None:
            self.extend_map = m.get('ExtendMap')

        if m.get('GateFailMsg') is not None:
            self.gate_fail_msg = m.get('GateFailMsg')

        if m.get('KeyString') is not None:
            self.key_string = m.get('KeyString')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

