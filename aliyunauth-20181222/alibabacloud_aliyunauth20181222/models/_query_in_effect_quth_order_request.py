# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryInEffectQuthOrderRequest(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        channel: str = None,
        language: str = None,
        operator_type_enum: str = None,
        request_from_app: str = None,
        request_id: str = None,
        request_way: str = None,
        user_no: str = None,
    ):
        self.biz_code = biz_code
        self.channel = channel
        self.language = language
        self.operator_type_enum = operator_type_enum
        self.request_from_app = request_from_app
        self.request_id = request_id
        self.request_way = request_way
        self.user_no = user_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.language is not None:
            result['Language'] = self.language

        if self.operator_type_enum is not None:
            result['OperatorTypeEnum'] = self.operator_type_enum

        if self.request_from_app is not None:
            result['RequestFromApp'] = self.request_from_app

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_way is not None:
            result['RequestWay'] = self.request_way

        if self.user_no is not None:
            result['UserNo'] = self.user_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OperatorTypeEnum') is not None:
            self.operator_type_enum = m.get('OperatorTypeEnum')

        if m.get('RequestFromApp') is not None:
            self.request_from_app = m.get('RequestFromApp')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestWay') is not None:
            self.request_way = m.get('RequestWay')

        if m.get('UserNo') is not None:
            self.user_no = m.get('UserNo')

        return self

