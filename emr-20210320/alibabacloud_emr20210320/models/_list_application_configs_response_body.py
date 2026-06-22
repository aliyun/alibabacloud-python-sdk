# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListApplicationConfigsResponseBody(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.ListApplicationConfigsResponseBodyApplicationConfigs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The application configurations.
        self.application_configs = application_configs
        # The number of entries per page.
        self.max_results = max_results
        # The page number of the next page returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of pages returned.
        self.total_count = total_count

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['ApplicationConfigs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k1 in m.get('ApplicationConfigs'):
                temp_model = main_models.ListApplicationConfigsResponseBodyApplicationConfigs()
                self.application_configs.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationConfigsResponseBodyApplicationConfigs(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        config_effect_state: str = None,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
        create_time: int = None,
        custom: bool = None,
        description: str = None,
        init_value: str = None,
        modifier: str = None,
        node_group_id: str = None,
        node_id: str = None,
        update_time: int = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The status of the configuration value.
        self.config_effect_state = config_effect_state
        # The name of the configuration file.
        self.config_file_name = config_file_name
        # The key of the configuration item.
        self.config_item_key = config_item_key
        # The value of the configuration item.
        self.config_item_value = config_item_value
        # The creation time.
        self.create_time = create_time
        # Indicates whether the configurations are custom.
        self.custom = custom
        # The description.
        self.description = description
        # The initial value.
        self.init_value = init_value
        # The person who modified the configurations.
        self.modifier = modifier
        # The node group ID.
        self.node_group_id = node_group_id
        # The node ID.
        self.node_id = node_id
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.config_effect_state is not None:
            result['ConfigEffectState'] = self.config_effect_state

        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom is not None:
            result['Custom'] = self.custom

        if self.description is not None:
            result['Description'] = self.description

        if self.init_value is not None:
            result['InitValue'] = self.init_value

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ConfigEffectState') is not None:
            self.config_effect_state = m.get('ConfigEffectState')

        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')

        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')

        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Custom') is not None:
            self.custom = m.get('Custom')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InitValue') is not None:
            self.init_value = m.get('InitValue')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

