# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetQualityFollowerResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetQualityFollowerResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the subscription relationship.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP return code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Whether the call is successful.
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
                temp_model = main_models.GetQualityFollowerResponseBodyData()
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

class GetQualityFollowerResponseBodyData(DaraModel):
    def __init__(
        self,
        alarm_mode: int = None,
        create_time: int = None,
        entity_id: str = None,
        follower: str = None,
        follower_account_name: str = None,
        id: int = None,
        modify_time: int = None,
        project_name: str = None,
        table_name: str = None,
    ):
        # The alert mode. The value is as follows:
        # 
        # - 1 (Mail)
        # - 2 (email and SMS)
        # - 4 (DingTalk groups of robots or hook)
        # - 5 (DingTalk groups of robots @ ALL)
        self.alarm_mode = alarm_mode
        # The time when the data quality rule subscription configuration was created.
        self.create_time = create_time
        # The ID of the partition expression.
        self.entity_id = entity_id
        # The subscriber to receive alert information.
        self.follower = follower
        # The Alibaba Cloud account name of the subscriber.
        self.follower_account_name = follower_account_name
        # The ID of the subscription relationship.
        self.id = id
        # The update time of the data quality rule subscription configuration.
        self.modify_time = modify_time
        # The name of the engine or data source.
        self.project_name = project_name
        # The name of the partitioned table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_mode is not None:
            result['AlarmMode'] = self.alarm_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.follower is not None:
            result['Follower'] = self.follower

        if self.follower_account_name is not None:
            result['FollowerAccountName'] = self.follower_account_name

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMode') is not None:
            self.alarm_mode = m.get('AlarmMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('Follower') is not None:
            self.follower = m.get('Follower')

        if m.get('FollowerAccountName') is not None:
            self.follower_account_name = m.get('FollowerAccountName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

