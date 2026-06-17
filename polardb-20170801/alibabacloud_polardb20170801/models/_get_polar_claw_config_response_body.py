# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetPolarClawConfigResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        config: Dict[str, Any] = None,
        hash: str = None,
        message: str = None,
        openclaw_version: str = None,
        request_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The configuration object.
        self.config = config
        # The configuration hash.
        self.hash = hash
        # The response message.
        self.message = message
        # The version of OpenClaw.
        self.openclaw_version = openclaw_version
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.config is not None:
            result['Config'] = self.config

        if self.hash is not None:
            result['Hash'] = self.hash

        if self.message is not None:
            result['Message'] = self.message

        if self.openclaw_version is not None:
            result['OpenclawVersion'] = self.openclaw_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Hash') is not None:
            self.hash = m.get('Hash')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OpenclawVersion') is not None:
            self.openclaw_version = m.get('OpenclawVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

