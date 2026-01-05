# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataSourceSharedRulesResponseBody(DaraModel):
    def __init__(
        self,
        data_source_shared_rules: List[main_models.ListDataSourceSharedRulesResponseBodyDataSourceSharedRules] = None,
        request_id: str = None,
    ):
        # The sharing rules of the data source.
        self.data_source_shared_rules = data_source_shared_rules
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_source_shared_rules:
            for v1 in self.data_source_shared_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSourceSharedRules'] = []
        if self.data_source_shared_rules is not None:
            for k1 in self.data_source_shared_rules:
                result['DataSourceSharedRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_shared_rules = []
        if m.get('DataSourceSharedRules') is not None:
            for k1 in m.get('DataSourceSharedRules'):
                temp_model = main_models.ListDataSourceSharedRulesResponseBodyDataSourceSharedRules()
                self.data_source_shared_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataSourceSharedRulesResponseBodyDataSourceSharedRules(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        data_source_id: int = None,
        env_type: str = None,
        id: int = None,
        shared_data_source_name: str = None,
        shared_user: str = None,
        source_project_id: int = None,
        target_project_id: int = None,
    ):
        # The time when the rule was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the user who creates the rule.
        self.create_user = create_user
        # The data source ID. You can call the [ListDataSources](https://help.aliyun.com/document_detail/211431.html) operation to query the ID.
        self.data_source_id = data_source_id
        # The environment to which the target data source belongs. The values are as follows:
        # - Dev: the development environment.
        # - Prod: the production environment.
        self.env_type = env_type
        # The rule ID.
        self.id = id
        # The name of the data source in the destination workspace.
        self.shared_data_source_name = shared_data_source_name
        # The user in the workspace to which the data source is shared. If the data source is shared to the entire workspace, this parameter is left empty.
        self.shared_user = shared_user
        # The ID of the workspace with which the data source is associated.
        self.source_project_id = source_project_id
        # The ID of the workspace to which the data source is shared.
        self.target_project_id = target_project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.id is not None:
            result['Id'] = self.id

        if self.shared_data_source_name is not None:
            result['SharedDataSourceName'] = self.shared_data_source_name

        if self.shared_user is not None:
            result['SharedUser'] = self.shared_user

        if self.source_project_id is not None:
            result['SourceProjectId'] = self.source_project_id

        if self.target_project_id is not None:
            result['TargetProjectId'] = self.target_project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('SharedDataSourceName') is not None:
            self.shared_data_source_name = m.get('SharedDataSourceName')

        if m.get('SharedUser') is not None:
            self.shared_user = m.get('SharedUser')

        if m.get('SourceProjectId') is not None:
            self.source_project_id = m.get('SourceProjectId')

        if m.get('TargetProjectId') is not None:
            self.target_project_id = m.get('TargetProjectId')

        return self

