# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAccessConfigurationRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        new_description: str = None,
        new_relay_state: str = None,
        new_session_duration: int = None,
    ):
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The new description of the access configuration.
        # 
        # The description can be up to 1,024 characters in length.
        self.new_description = new_description
        # The new initial web page
        # 
        # that is displayed after a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # The web page must be a page of the Alibaba Cloud Management Console.
        self.new_relay_state = new_relay_state
        # The new duration of a session
        # 
        # in which a CloudSSO user accesses an account in your resource directory by using the access configuration.
        # 
        # Unit: seconds.
        # 
        # Valid values: 900 to 43200. The value 900 indicates 15 minutes. The value 43200 indicates 12 hours.
        self.new_session_duration = new_session_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.new_description is not None:
            result['NewDescription'] = self.new_description

        if self.new_relay_state is not None:
            result['NewRelayState'] = self.new_relay_state

        if self.new_session_duration is not None:
            result['NewSessionDuration'] = self.new_session_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')

        if m.get('NewRelayState') is not None:
            self.new_relay_state = m.get('NewRelayState')

        if m.get('NewSessionDuration') is not None:
            self.new_session_duration = m.get('NewSessionDuration')

        return self

