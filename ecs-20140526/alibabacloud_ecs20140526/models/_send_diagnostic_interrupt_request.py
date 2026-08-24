# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendDiagnosticInterruptRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        instance_id: str = None,
    ):
        # Specifies whether to perform only a dry run. Valid values: ● true: Sends a check request without sending the NMI command. ● false (default): Sends a normal NMI request to trigger a crash dump.
        self.dry_run = dry_run
        # The instance ID of the instance to which you want to send a diagnostic break.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

