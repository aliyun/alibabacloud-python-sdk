# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHoneypotProbeBindRequest(DaraModel):
    def __init__(
        self,
        bind_id: str = None,
        lang: str = None,
        probe_id: str = None,
    ):
        # The unique ID of the bound service.
        self.bind_id = bind_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The probe ID.
        # 
        # >  You can call the [ListHoneypotProbe](~~ListHoneypotProbe~~) operation to query the IDs of probes.
        self.probe_id = probe_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_id is not None:
            result['BindId'] = self.bind_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        return self

