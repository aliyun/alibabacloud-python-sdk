# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthenticateRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        language: str = None,
        operate_code: str = None,
        operator_type_enum: str = None,
        product_code: str = None,
        request_from_app: str = None,
        request_way: str = None,
        user_no: str = None,
    ):
        self.instance_id = instance_id
        self.language = language
        self.operate_code = operate_code
        self.operator_type_enum = operator_type_enum
        self.product_code = product_code
        self.request_from_app = request_from_app
        self.request_way = request_way
        self.user_no = user_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.language is not None:
            result['Language'] = self.language

        if self.operate_code is not None:
            result['OperateCode'] = self.operate_code

        if self.operator_type_enum is not None:
            result['OperatorTypeEnum'] = self.operator_type_enum

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.request_from_app is not None:
            result['RequestFromApp'] = self.request_from_app

        if self.request_way is not None:
            result['RequestWay'] = self.request_way

        if self.user_no is not None:
            result['UserNo'] = self.user_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OperateCode') is not None:
            self.operate_code = m.get('OperateCode')

        if m.get('OperatorTypeEnum') is not None:
            self.operator_type_enum = m.get('OperatorTypeEnum')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RequestFromApp') is not None:
            self.request_from_app = m.get('RequestFromApp')

        if m.get('RequestWay') is not None:
            self.request_way = m.get('RequestWay')

        if m.get('UserNo') is not None:
            self.user_no = m.get('UserNo')

        return self

