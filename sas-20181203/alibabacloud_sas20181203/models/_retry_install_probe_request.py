# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryInstallProbeRequest(DaraModel):
    def __init__(
        self,
        probe_id: str = None,
    ):
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
        if self.probe_id is not None:
            result['ProbeId'] = self.probe_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProbeId') is not None:
            self.probe_id = m.get('ProbeId')

        return self

