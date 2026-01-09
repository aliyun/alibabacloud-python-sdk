# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class CreateLoggingRequest(DaraModel):
    def __init__(
        self,
        logging_details: List[main_models.CreateLoggingRequestLoggingDetails] = None,
        logging_project: str = None,
    ):
        # The configurations of service logs.
        # 
        # This parameter is required.
        self.logging_details = logging_details
        # The name of the project to which service logs are stored.
        # 
        # This parameter is required.
        self.logging_project = logging_project

    def validate(self):
        if self.logging_details:
            for v1 in self.logging_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['loggingDetails'] = []
        if self.logging_details is not None:
            for k1 in self.logging_details:
                result['loggingDetails'].append(k1.to_map() if k1 else None)

        if self.logging_project is not None:
            result['loggingProject'] = self.logging_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logging_details = []
        if m.get('loggingDetails') is not None:
            for k1 in m.get('loggingDetails'):
                temp_model = main_models.CreateLoggingRequestLoggingDetails()
                self.logging_details.append(temp_model.from_map(k1))

        if m.get('loggingProject') is not None:
            self.logging_project = m.get('loggingProject')

        return self

class CreateLoggingRequestLoggingDetails(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        type: str = None,
    ):
        # The name of the Logstore to which service logs of the type are stored.
        # 
        # This parameter is required.
        self.logstore = logstore
        # The type of service logs. Valid values:
        # 
        # *   consumergroup_log: the consumption delay logs of consumer groups.
        # *   logtail_alarm: the alert logs of Logtail.
        # *   operation_log: the operation logs.
        # *   logtail_profile: the collection logs of Logtail.
        # *   metering: the metering logs.
        # *   logtail_status: the status logs of Logtail.
        # *   scheduledsqlalert: the run logs of Scheduled SQL jobs.
        # *   etl_alert: the run logs of data transformation jobs.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

