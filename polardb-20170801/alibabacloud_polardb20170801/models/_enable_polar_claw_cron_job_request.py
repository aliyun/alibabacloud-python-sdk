# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnablePolarClawCronJobRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        job_id: str = None,
        restart: bool = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The ID of the cron job to enable.
        # 
        # This parameter is required.
        self.job_id = job_id
        # Specifies whether to restart the gateway after the job is enabled. The default value is `true`.
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

