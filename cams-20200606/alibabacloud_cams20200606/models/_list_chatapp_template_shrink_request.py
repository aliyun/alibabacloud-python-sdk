# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListChatappTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        audit_status: str = None,
        category: str = None,
        code: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        isv_code: str = None,
        language: str = None,
        name: str = None,
        owner_id: int = None,
        page_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_type: str = None,
    ):
        # The review state of the template. Valid values:
        # 
        # *   **pass**: The template is approved.
        # *   **fail**: The template is rejected.
        # *   **auditing**: The template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the message template.
        self.category = category
        # The code of the message template.
        self.code = code
        # The space ID of the RAM user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business Account (WABA) ID of the RAM user within the independent software vendor (ISV) account.
        # 
        # >  CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The ISV verification code. This parameter is used to verify whether the RAM user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The name of the template.
        self.name = name
        self.owner_id = owner_id
        # The pagination settings.
        self.page_shrink = page_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the message template.
        # 
        # *   **WHATSAPP**
        # *   **VIBER**
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.category is not None:
            result['Category'] = self.category

        if self.code is not None:
            result['Code'] = self.code

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id

        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code

        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_shrink is not None:
            result['Page'] = self.page_shrink

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')

        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

