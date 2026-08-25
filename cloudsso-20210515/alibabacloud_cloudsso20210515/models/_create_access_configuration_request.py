# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class CreateAccessConfigurationRequest(DaraModel):
    def __init__(
        self,
        access_configuration_name: str = None,
        description: str = None,
        directory_id: str = None,
        relay_state: str = None,
        session_duration: int = None,
        tags: List[main_models.CreateAccessConfigurationRequestTags] = None,
    ):
        # The name of the access configuration.
        # 
        # Format: contains letters, digits, or hyphens (-).
        # 
        # Length: up to 32 characters.
        self.access_configuration_name = access_configuration_name
        # The description of the access configuration.
        # 
        # Length: up to 1024 characters.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The initial access page.
        # 
        # The page address that a CloudSSO user initially accesses when using the access configuration to access an account in a resource directory.
        # 
        # The page must be an Alibaba Cloud Management Console page. Default value: empty, which indicates that the user is redirected to the homepage of the Alibaba Cloud Management Console.
        self.relay_state = relay_state
        # The session duration.
        # 
        # The maximum duration of a session when a CloudSSO user uses the access configuration to access an account in a resource directory.
        # 
        # Unit: seconds.
        # 
        # Valid values: 900 to 43200 (15 minutes to 12 hours).
        # 
        # Default value: 3600 (1 hour).
        self.session_duration = session_duration
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_name is not None:
            result['AccessConfigurationName'] = self.access_configuration_name

        if self.description is not None:
            result['Description'] = self.description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.relay_state is not None:
            result['RelayState'] = self.relay_state

        if self.session_duration is not None:
            result['SessionDuration'] = self.session_duration

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationName') is not None:
            self.access_configuration_name = m.get('AccessConfigurationName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('RelayState') is not None:
            self.relay_state = m.get('RelayState')

        if m.get('SessionDuration') is not None:
            self.session_duration = m.get('SessionDuration')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateAccessConfigurationRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateAccessConfigurationRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

