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
        # The log path.
        self.log_path = log_path
        # The log type. The following types of logs are supported:
        # 
        # *   File collection logs
        # *   Standard output logs
        self.log_type = log_type
        # The name of the Logstore. The name must meet the following requirements:
        # 
        # *   The name must be unique in a project.
        # *   The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # *   The name must start and end with a lowercase letter or a digit.
        # *   The name must be 3 to 63 characters in length.
        self.logstore_name = logstore_name
        # The name for the Logtail configuration.
        self.logtail_name = logtail_name
        # The name of the machine group of Simple Log Service.
        self.machine_group = machine_group
        # The name of the SLS project.
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

