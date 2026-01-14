# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManualRunMailTaskRequest(DaraModel):
    def __init__(
        self,
        mail_id: str = None,
    ):
        # The ID of the email task in the subscription management interface.
        # 
        # This parameter is required.
        self.mail_id = mail_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mail_id is not None:
            result['MailId'] = self.mail_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MailId') is not None:
            self.mail_id = m.get('MailId')

        return self

