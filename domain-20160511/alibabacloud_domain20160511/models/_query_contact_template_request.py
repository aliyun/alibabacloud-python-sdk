# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryContactTemplateRequest(DaraModel):
    def __init__(
        self,
        audit_status: str = None,
        ccompany: str = None,
        contact_template_id: int = None,
        default_template: bool = None,
        ecompany: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        reg_type: str = None,
        user_client_ip: str = None,
    ):
        self.audit_status = audit_status
        self.ccompany = ccompany
        self.contact_template_id = contact_template_id
        self.default_template = default_template
        self.ecompany = ecompany
        self.lang = lang
        self.page_num = page_num
        self.page_size = page_size
        self.reg_type = reg_type
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.ccompany is not None:
            result['CCompany'] = self.ccompany

        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id

        if self.default_template is not None:
            result['DefaultTemplate'] = self.default_template

        if self.ecompany is not None:
            result['ECompany'] = self.ecompany

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reg_type is not None:
            result['RegType'] = self.reg_type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('CCompany') is not None:
            self.ccompany = m.get('CCompany')

        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')

        if m.get('DefaultTemplate') is not None:
            self.default_template = m.get('DefaultTemplate')

        if m.get('ECompany') is not None:
            self.ecompany = m.get('ECompany')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegType') is not None:
            self.reg_type = m.get('RegType')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

