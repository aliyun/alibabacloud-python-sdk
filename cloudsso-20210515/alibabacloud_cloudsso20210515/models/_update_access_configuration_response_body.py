# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class UpdateAccessConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        access_configuration: main_models.UpdateAccessConfigurationResponseBodyAccessConfiguration = None,
        request_id: str = None,
    ):
        # The information about the access configuration.
        self.access_configuration = access_configuration
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_configuration:
            self.access_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration is not None:
            result['AccessConfiguration'] = self.access_configuration.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfiguration') is not None:
            temp_model = main_models.UpdateAccessConfigurationResponseBodyAccessConfiguration()
            self.access_configuration = temp_model.from_map(m.get('AccessConfiguration'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateAccessConfigurationResponseBodyAccessConfiguration(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        description: str = None,
        relay_state: str = None,
        session_duration: int = None,
        status_notifications: List[str] = None,
        update_time: str = None,
    ):
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The name of the access configuration.
        self.access_configuration_name = access_configuration_name
        # The time when the access configuration was created.
        self.create_time = create_time
        # The description of the access configuration.
        self.description = description
        # The initial web page
        # 
        # that is displayed after a CloudSSO user accesses an account in your resource directory by using the access configuration.
        self.relay_state = relay_state
        # The duration of a session
        # 
        # in which a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # Unit: seconds.
        self.session_duration = session_duration
        # The status notifications.
        self.status_notifications = status_notifications
        # The time when the information about the access configuration was modified.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.relay_state is not None:
            result['RelayState'] = self.relay_state

        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration

        if self.status_notifications is not None:
            result['StatusNotifications'] = self.status_notifications

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RelayState') is not None:
            self.relay_state = m.get('RelayState')

        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')

        if m.get('StatusNotifications') is not None:
            self.status_notifications = m.get('StatusNotifications')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

