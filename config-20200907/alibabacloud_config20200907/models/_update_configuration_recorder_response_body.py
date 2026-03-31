# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class UpdateConfigurationRecorderResponseBody(DaraModel):
    def __init__(
        self,
        configuration_recorder: main_models.UpdateConfigurationRecorderResponseBodyConfigurationRecorder = None,
        request_id: str = None,
    ):
        # The details of the configuration recorder.
        self.configuration_recorder = configuration_recorder
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.configuration_recorder:
            self.configuration_recorder.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_recorder is not None:
            result['ConfigurationRecorder'] = self.configuration_recorder.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationRecorder') is not None:
            temp_model = main_models.UpdateConfigurationRecorderResponseBodyConfigurationRecorder()
            self.configuration_recorder = temp_model.from_map(m.get('ConfigurationRecorder'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateConfigurationRecorderResponseBodyConfigurationRecorder(DaraModel):
    def __init__(
        self,
        configuration_recorder_status: str = None,
        resource_types: List[str] = None,
    ):
        # The status of the configuration recorder. Valid values:
        # 
        # *   REGISTRABLE: The configuration recorder has not been registered.
        # *   BUILDING: The configuration recorder is being deployed.
        # *   REGISTERED: The configuration recorder has been registered.
        # *   REBUILDING: The configuration recorder is being redeployed.
        self.configuration_recorder_status = configuration_recorder_status
        # The types of the resources that are monitored by Cloud Config.
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_recorder_status is not None:
            result['ConfigurationRecorderStatus'] = self.configuration_recorder_status

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigurationRecorderStatus') is not None:
            self.configuration_recorder_status = m.get('ConfigurationRecorderStatus')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        return self

