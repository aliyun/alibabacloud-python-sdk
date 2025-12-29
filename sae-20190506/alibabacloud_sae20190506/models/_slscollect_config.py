# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SLSCollectConfig(DaraModel):
    def __init__(
        self,
        log_path: str = None,
        log_type: str = None,
        logstore_name: str = None,
        logtail_name: str = None,
        machine_group: str = None,
        project_name: str = None,
    ):
        self.log_path = log_path
        self.log_type = log_type
        self.logstore_name = logstore_name
        self.logtail_name = logtail_name
        self.machine_group = machine_group
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_path is not None:
            result['LogPath'] = self.log_path

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.logstore_name is not None:
            result['LogstoreName'] = self.logstore_name

        if self.logtail_name is not None:
            result['LogtailName'] = self.logtail_name

        if self.machine_group is not None:
            result['MachineGroup'] = self.machine_group

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogPath') is not None:
            self.log_path = m.get('LogPath')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('LogstoreName') is not None:
            self.logstore_name = m.get('LogstoreName')

        if m.get('LogtailName') is not None:
            self.logtail_name = m.get('LogtailName')

        if m.get('MachineGroup') is not None:
            self.machine_group = m.get('MachineGroup')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

