# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveFormRemarkRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        at_user_id: str = None,
        content: str = None,
        form_instance_id: str = None,
        language: str = None,
        reply_id: int = None,
        system_token: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        self.at_user_id = at_user_id
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.form_instance_id = form_instance_id
        self.language = language
        self.reply_id = reply_id
        # This parameter is required.
        self.system_token = system_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.at_user_id is not None:
            result['AtUserId'] = self.at_user_id

        if self.content is not None:
            result['Content'] = self.content

        if self.form_instance_id is not None:
            result['FormInstanceId'] = self.form_instance_id

        if self.language is not None:
            result['Language'] = self.language

        if self.reply_id is not None:
            result['ReplyId'] = self.reply_id

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('AtUserId') is not None:
            self.at_user_id = m.get('AtUserId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FormInstanceId') is not None:
            self.form_instance_id = m.get('FormInstanceId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ReplyId') is not None:
            self.reply_id = m.get('ReplyId')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

