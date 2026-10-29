# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteRequestSGRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        service: str = None,
        service_parameters: str = None,
    ):
        # The language.
        self.lang = lang
        # The service product code. For custom events, set this parameter to saf_de.
        # 
        # This parameter is required.
        self.service = service
        # The service input parameters in JSON format. For custom events, you must include the eventCode property in the JSON string.
        # 
        # This parameter is required.
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.service is not None:
            result['Service'] = self.service

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        return self

