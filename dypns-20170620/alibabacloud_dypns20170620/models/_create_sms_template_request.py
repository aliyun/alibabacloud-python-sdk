# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsTemplateRequest(DaraModel):
    def __init__(
        self,
        biz_url: str = None,
        business_type: str = None,
        owner_id: int = None,
        prod_code: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sms_template_content: str = None,
        sms_template_name: str = None,
        sms_template_rule: str = None,
    ):
        # This parameter is required.
        self.biz_url = biz_url
        # This parameter is required.
        self.business_type = business_type
        self.owner_id = owner_id
        self.prod_code = prod_code
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.sms_template_content = sms_template_content
        # This parameter is required.
        self.sms_template_name = sms_template_name
        # This parameter is required.
        self.sms_template_rule = sms_template_rule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_url is not None:
            result['BizUrl'] = self.biz_url

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sms_template_content is not None:
            result['SmsTemplateContent'] = self.sms_template_content

        if self.sms_template_name is not None:
            result['SmsTemplateName'] = self.sms_template_name

        if self.sms_template_rule is not None:
            result['SmsTemplateRule'] = self.sms_template_rule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUrl') is not None:
            self.biz_url = m.get('BizUrl')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SmsTemplateContent') is not None:
            self.sms_template_content = m.get('SmsTemplateContent')

        if m.get('SmsTemplateName') is not None:
            self.sms_template_name = m.get('SmsTemplateName')

        if m.get('SmsTemplateRule') is not None:
            self.sms_template_rule = m.get('SmsTemplateRule')

        return self

