# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatappTemplateDetailRequest(DaraModel):
    def __init__(
        self,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The SpaceId of the ISV sub-customer or the instance ID of a direct customer.
        self.cust_space_id = cust_space_id
        # The WabaId of the ISV customer.
        # 
        # > This parameter is deprecated. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The ISV verification code, which is used to verify whether the sub-account is authorized by the ISV.
        self.isv_code = isv_code
        # The language of the template. For detailed language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # The code of the template.
        self.template_code = template_code
        # The name of the template.
        self.template_name = template_name
        # The templatetype.
        # 
        # - **WHATSAPP**
        # 
        # - **VIBER**
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id

        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code

        if self.language is not None:
            result['Language'] = self.language

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')

        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

