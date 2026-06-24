# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AcceptPushRequest(DaraModel):
    def __init__(
        self,
        contact_template_id: int = None,
        push_no: str = None,
    ):
        # 实名认证通过的模板，域名过户时用于WHOIS信息变更
        # 
        # This parameter is required.
        self.contact_template_id = contact_template_id
        # Push编号
        # 
        # This parameter is required.
        self.push_no = push_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id

        if self.push_no is not None:
            result['PushNo'] = self.push_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')

        if m.get('PushNo') is not None:
            self.push_no = m.get('PushNo')

        return self

