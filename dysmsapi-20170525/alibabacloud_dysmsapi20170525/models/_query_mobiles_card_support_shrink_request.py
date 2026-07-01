# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMobilesCardSupportShrinkRequest(DaraModel):
    def __init__(
        self,
        encrypt_type: str = None,
        mobiles_shrink: str = None,
        template_code: str = None,
    ):
        # The encryption method for the phone number. Valid values:
        # - SHA1: SHA1 encryption.
        # - NORMAL: no encryption. The phone number is transmitted in plaintext.
        self.encrypt_type = encrypt_type
        # The list of phone numbers.
        # 
        # This parameter is required.
        self.mobiles_shrink = mobiles_shrink
        # The code of the card SMS template. To view the code, log on to the console and choose **Domestic Messages** > [Template Management](https://dysms.console.aliyun.com/domestic/text/template).
        # 
        # >The template must be added and approved.
        # 
        # This parameter is required.
        self.template_code = template_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.mobiles_shrink is not None:
            result['Mobiles'] = self.mobiles_shrink

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('Mobiles') is not None:
            self.mobiles_shrink = m.get('Mobiles')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        return self

