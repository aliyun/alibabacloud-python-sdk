# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListPublishRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        list_result: main_models.ListPublishRecordsResponseBodyListResult = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.list_result = list_result
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.list_result:
            self.list_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.list_result is not None:
            result['ListResult'] = self.list_result.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('ListResult') is not None:
            temp_model = main_models.ListPublishRecordsResponseBodyListResult()
            self.list_result = temp_model.from_map(m.get('ListResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListPublishRecordsResponseBodyListResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListPublishRecordsResponseBodyListResultData] = None,
        total_count: int = None,
    ):
        self.data = data
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListPublishRecordsResponseBodyListResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublishRecordsResponseBodyListResultData(DaraModel):
    def __init__(
        self,
        change_type: int = None,
        error_message: str = None,
        finish_time: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        id: int = None,
        node_id: str = None,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
        object_version: str = None,
        project_id: str = None,
        publish_name: str = None,
        publish_status: int = None,
        publisher: str = None,
        publisher_name: str = None,
    ):
        self.change_type = change_type
        self.error_message = error_message
        self.finish_time = finish_time
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.id = id
        self.node_id = node_id
        self.object_id = object_id
        self.object_name = object_name
        self.object_type = object_type
        self.object_version = object_version
        self.project_id = project_id
        self.publish_name = publish_name
        self.publish_status = publish_status
        self.publisher = publisher
        self.publisher_name = publisher_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modify is not None:
            result['GmtModify'] = self.gmt_modify

        if self.id is not None:
            result['Id'] = self.id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.object_version is not None:
            result['ObjectVersion'] = self.object_version

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.publish_name is not None:
            result['PublishName'] = self.publish_name

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.publisher is not None:
            result['Publisher'] = self.publisher

        if self.publisher_name is not None:
            result['PublisherName'] = self.publisher_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModify') is not None:
            self.gmt_modify = m.get('GmtModify')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('ObjectVersion') is not None:
            self.object_version = m.get('ObjectVersion')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('PublishName') is not None:
            self.publish_name = m.get('PublishName')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('Publisher') is not None:
            self.publisher = m.get('Publisher')

        if m.get('PublisherName') is not None:
            self.publisher_name = m.get('PublisherName')

        return self

