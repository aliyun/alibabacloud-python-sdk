# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListAccessConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        access_configurations: List[main_models.ListAccessConfigurationsResponseBodyAccessConfigurations] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # The list of access configurations.
        self.access_configurations = access_configurations
        # Indicates whether the results are truncated. Valid values:
        # 
        # - true: The results are truncated.
        # - false: The results are not truncated.
        self.is_truncated = is_truncated
        # The maximum number of entries per page.
        self.max_results = max_results
        # The token for the next page of results.
        # 
        # > This parameter is returned only when `IsTruncated` is `true`.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries that match the request parameters.
        self.total_counts = total_counts

    def validate(self):
        if self.access_configurations:
            for v1 in self.access_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessConfigurations'] = []
        if self.access_configurations is not None:
            for k1 in self.access_configurations:
                result['AccessConfigurations'].append(k1.to_map() if k1 else None)

        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_configurations = []
        if m.get('AccessConfigurations') is not None:
            for k1 in m.get('AccessConfigurations'):
                temp_model = main_models.ListAccessConfigurationsResponseBodyAccessConfigurations()
                self.access_configurations.append(temp_model.from_map(k1))

        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListAccessConfigurationsResponseBodyAccessConfigurations(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        access_configuration_name: str = None,
        create_time: str = None,
        description: str = None,
        relay_state: str = None,
        session_duration: int = None,
        status_notifications: List[str] = None,
        tags: List[main_models.ListAccessConfigurationsResponseBodyAccessConfigurationsTags] = None,
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
        # The initial access page.
        # 
        # The URL of the initial page that is displayed when a CloudSSO user uses the access configuration to access an account in a resource directory.
        self.relay_state = relay_state
        # The session duration.
        # 
        # The maximum duration of a session when a CloudSSO user uses the access configuration to access an account in a resource directory.
        # 
        # Unit: seconds.
        self.session_duration = session_duration
        # The status notification information.
        self.status_notifications = status_notifications
        # The list of tags.
        self.tags = tags
        # The time when the access configuration was last modified.
        self.update_time = update_time

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListAccessConfigurationsResponseBodyAccessConfigurationsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListAccessConfigurationsResponseBodyAccessConfigurationsTags(DaraModel):
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

