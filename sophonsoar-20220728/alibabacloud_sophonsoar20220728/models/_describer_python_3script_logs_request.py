# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescriberPython3ScriptLogsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        request_uuid: str = None,
    ):
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The UUID that is returned when the Python3 script is run.
        # 
        # >  You can call the [RunPython3Script](~~RunPython3Script~~) operation to query the UUID.
        # 
        # This parameter is required.
        self.request_uuid = request_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')

        return self

