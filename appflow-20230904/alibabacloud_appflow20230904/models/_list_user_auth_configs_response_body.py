# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appflow20230904 import models as main_models
from darabonba.model import DaraModel

class ListUserAuthConfigsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        user_auth_configs: List[main_models.ListUserAuthConfigsResponseBodyUserAuthConfigs] = None,
    ):
        # The page size.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The user authentication credentials.
        self.user_auth_configs = user_auth_configs

    def validate(self):
        if self.user_auth_configs:
            for v1 in self.user_auth_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserAuthConfigs'] = []
        if self.user_auth_configs is not None:
            for k1 in self.user_auth_configs:
                result['UserAuthConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_auth_configs = []
        if m.get('UserAuthConfigs') is not None:
            for k1 in m.get('UserAuthConfigs'):
                temp_model = main_models.ListUserAuthConfigsResponseBodyUserAuthConfigs()
                self.user_auth_configs.append(temp_model.from_map(k1))

        return self

class ListUserAuthConfigsResponseBodyUserAuthConfigs(DaraModel):
    def __init__(
        self,
        auth_config_id: str = None,
        auth_config_name: str = None,
        auth_type: str = None,
        connector_id: str = None,
        connector_version: str = None,
        flow_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        # The credential ID.
        self.auth_config_id = auth_config_id
        # The credential name.
        self.auth_config_name = auth_config_name
        # The authentication type.
        self.auth_type = auth_type
        # The ID of the connector.
        self.connector_id = connector_id
        # The version of the connector.
        self.connector_version = connector_version
        # The number of connection flows that use this credential.
        self.flow_count = flow_count
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config_id is not None:
            result['AuthConfigId'] = self.auth_config_id

        if self.auth_config_name is not None:
            result['AuthConfigName'] = self.auth_config_name

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.connector_version is not None:
            result['ConnectorVersion'] = self.connector_version

        if self.flow_count is not None:
            result['FlowCount'] = self.flow_count

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConfigId') is not None:
            self.auth_config_id = m.get('AuthConfigId')

        if m.get('AuthConfigName') is not None:
            self.auth_config_name = m.get('AuthConfigName')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('ConnectorVersion') is not None:
            self.connector_version = m.get('ConnectorVersion')

        if m.get('FlowCount') is not None:
            self.flow_count = m.get('FlowCount')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        return self

