# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendRCSRequest(DaraModel):
    def __init__(
        self,
        out_id: str = None,
        phone_numbers: str = None,
        sign_name: str = None,
        template_code: str = None,
        template_param: str = None,
    ):
        self.out_id = out_id
        # This parameter is required.
        self.phone_numbers = phone_numbers
        # This parameter is required.
        self.sign_name = sign_name
        # This parameter is required.
        self.template_code = template_code
        self.template_param = template_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_param is not None:
            result['TemplateParam'] = self.template_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')

        return self

