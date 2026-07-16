# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AcknowledgeTaskResultRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        task_detail_no: List[str] = None,
        user_client_ip: str = None,
    ):
        self.lang = lang
        # This parameter is required.
        self.task_detail_no = task_detail_no
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

        if self.task_detail_no is not None:
            result['TaskDetailNo'] = self.task_detail_no

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TaskDetailNo') is not None:
            self.task_detail_no = m.get('TaskDetailNo')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

