# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationBackupRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        job_mode: str = None,
        region_id: str = None,
    ):
        # The ID of the application to back up.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The application type, such as polarclaw.
        self.application_type = application_type
        # The backup mode. Automated indicates an automatic backup, and Manual indicates a manual backup.
        # 
        # This parameter is required.
        self.job_mode = job_mode
        # The ID of the region where the application resides. The server uses the actual region of the application.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.job_mode is not None:
            result['JobMode'] = self.job_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('JobMode') is not None:
            self.job_mode = m.get('JobMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

