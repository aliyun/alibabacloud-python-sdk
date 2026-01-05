# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetSmsTemplateListRequest(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        owner_id: int = None,
        page_index: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        template_code: str = None,
        template_name: str = None,
        template_tag: str = None,
        template_type: int = None,
        usable_state_list: List[str] = None,
    ):
        # 模板审核状态
        self.audit_status = audit_status
        self.owner_id = owner_id
        # 页码, 默认1
        self.page_index = page_index
        # 每页数量，默认10
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名
        self.sign_name = sign_name
        # 模板code
        self.template_code = template_code
        # 模板名称
        self.template_name = template_name
        # 模板标签
        self.template_tag = template_tag
        # 模板类型
        self.template_type = template_type
        # 模板状态
        self.usable_state_list = usable_state_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_tag is not None:
            result['TemplateTag'] = self.template_tag

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.usable_state_list is not None:
            result['UsableStateList'] = self.usable_state_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateTag') is not None:
            self.template_tag = m.get('TemplateTag')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('UsableStateList') is not None:
            self.usable_state_list = m.get('UsableStateList')

        return self

