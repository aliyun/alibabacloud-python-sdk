# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRCSMobileCapableTaskRequest(DaraModel):
    def __init__(
        self,
        phone_numbers_file: str = None,
        sign_name: str = None,
        template_code: str = None,
    ):
        # This parameter is required.
        self.phone_numbers_file = phone_numbers_file
        # This parameter is required.
        self.sign_name = sign_name
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_numbers_file is not None:
            result['PhoneNumbersFile'] = self.phone_numbers_file

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumbersFile') is not None:
            self.phone_numbers_file = m.get('PhoneNumbersFile')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

