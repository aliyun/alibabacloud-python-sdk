# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebootRCInstanceRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        force_stop: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and insufficient inventory errors. If the request passes the dry run, the DryRunOperation error code is returned. Otherwise, an error message is returned.
        # *   **false**: performs a dry run and performs the actual request. If the request passes the dry run, the instance is restarted.
        # 
        # Default value: false
        self.dry_run = dry_run
        # Specifies whether to forcefully stop the instance before you restart the instance Valid values:
        # 
        # *   **true**: forcefully stops the instance. This operation is equivalent to the typical power-off operation. Cache data that is not written to storage devices on the instance is lost.
        # *   **false** (default): normally stops the instance.
        self.force_stop = force_stop
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

