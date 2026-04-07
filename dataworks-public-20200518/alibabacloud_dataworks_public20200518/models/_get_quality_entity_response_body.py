# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetQualityEntityResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetQualityEntityResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the partition filter expression.
        self.data = data
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetQualityEntityResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityEntityResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        entity_level: int = None,
        env_type: str = None,
        followers: str = None,
        has_relative_node: bool = None,
        id: int = None,
        match_expression: str = None,
        modify_time: int = None,
        modify_user: str = None,
        on_duty: str = None,
        on_duty_account_name: str = None,
        project_name: str = None,
        relative_node: str = None,
        sql: int = None,
        table_name: str = None,
        task: int = None,
    ):
        # The time when the partition filter expression was created.
        self.create_time = create_time
        # The level of the partition filter expression. Valid values:
        # 
        # *   0: The partition filter expression is at the SQL level. This indicates that the system checks data quality after each SQL statement is executed.
        # *   1: The partition filter expression is at the node level. This indicates that the system checks data quality after all the SQL statements for a node are executed.
        self.entity_level = entity_level
        # The type of the compute engine instance or data source.
        self.env_type = env_type
        # The ID of the Alibaba Cloud account that is used to receive alert notifications.
        self.followers = followers
        # Indicates whether the partition filter expression is associated with a node. Valid values:
        # 
        # *   true: The partition filter expression is associated with a node.
        # *   false: The partition filter expression is not associated with a node.
        self.has_relative_node = has_relative_node
        # The ID of the partition filter expression.
        self.id = id
        # The partition filter expression.
        self.match_expression = match_expression
        # The time when the partition filter expression was modified.
        self.modify_time = modify_time
        # The ID of the Alibaba Cloud account that is used to modify the partition filter expression.
        self.modify_user = modify_user
        # The ID of the Alibaba Cloud account that is used to configure the partition filter expression.
        self.on_duty = on_duty
        # The name of the Alibaba Cloud account that is used to configure the partition filter expression.
        self.on_duty_account_name = on_duty_account_name
        # The name of the compute engine instance or data source.
        self.project_name = project_name
        # The information about the node with which the partition filter expression is associated. The information includes the following items:
        # 
        # *   ProjectName: the name of the workspace to which the node belongs.
        # *   NodeID: the ID of the node.
        self.relative_node = relative_node
        # Indicates that the partition filter expression is at the SQL level.
        self.sql = sql
        # The name of the partitioned table.
        self.table_name = table_name
        # The node.
        self.task = task

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.entity_level is not None:
            result['EntityLevel'] = self.entity_level

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.followers is not None:
            result['Followers'] = self.followers

        if self.has_relative_node is not None:
            result['HasRelativeNode'] = self.has_relative_node

        if self.id is not None:
            result['Id'] = self.id

        if self.match_expression is not None:
            result['MatchExpression'] = self.match_expression

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.on_duty is not None:
            result['OnDuty'] = self.on_duty

        if self.on_duty_account_name is not None:
            result['OnDutyAccountName'] = self.on_duty_account_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.relative_node is not None:
            result['RelativeNode'] = self.relative_node

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.task is not None:
            result['Task'] = self.task

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EntityLevel') is not None:
            self.entity_level = m.get('EntityLevel')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Followers') is not None:
            self.followers = m.get('Followers')

        if m.get('HasRelativeNode') is not None:
            self.has_relative_node = m.get('HasRelativeNode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchExpression') is not None:
            self.match_expression = m.get('MatchExpression')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('OnDuty') is not None:
            self.on_duty = m.get('OnDuty')

        if m.get('OnDutyAccountName') is not None:
            self.on_duty_account_name = m.get('OnDutyAccountName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RelativeNode') is not None:
            self.relative_node = m.get('RelativeNode')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('Task') is not None:
            self.task = m.get('Task')

        return self

