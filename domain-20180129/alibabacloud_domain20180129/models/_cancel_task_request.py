# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelTaskRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        task_no: str = None,
        user_client_ip: str = None,
    ):
        # Language of the error message returned by the API. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # Job number.
        # 
        # >You can query the job number by using the [QueryTaskList](https://help.aliyun.com/document_detail/67709.html) API.
        # 
        # This parameter is required.
        self.task_no = task_no
        # User IP address.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

