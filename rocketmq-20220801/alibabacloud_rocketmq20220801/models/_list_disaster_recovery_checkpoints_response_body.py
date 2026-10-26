# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ListDisasterRecoveryCheckpointsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListDisasterRecoveryCheckpointsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The returned data.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListDisasterRecoveryCheckpointsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListDisasterRecoveryCheckpointsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListDisasterRecoveryCheckpointsResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The paginated data.
        self.list = list
        # The current page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ListDisasterRecoveryCheckpointsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListDisasterRecoveryCheckpointsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        checkpoint_id: int = None,
        item_id: int = None,
        last_sync_time: int = None,
        plan_id: int = None,
        source_progress: main_models.ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgress = None,
        target_progress: main_models.ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgress = None,
    ):
        # The consumer offset checkpoint ID.
        self.checkpoint_id = checkpoint_id
        # The ID of the backup mapping.
        self.item_id = item_id
        # The most recent synchronization time. The value is a UNIX timestamp in milliseconds.
        self.last_sync_time = last_sync_time
        # The ID of the backup plan.
        self.plan_id = plan_id
        # The source consumer offset.
        self.source_progress = source_progress
        # The target consumer offset.
        self.target_progress = target_progress

    def validate(self):
        if self.source_progress:
            self.source_progress.validate()
        if self.target_progress:
            self.target_progress.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint_id is not None:
            result['checkpointId'] = self.checkpoint_id

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.last_sync_time is not None:
            result['lastSyncTime'] = self.last_sync_time

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.source_progress is not None:
            result['sourceProgress'] = self.source_progress.to_map()

        if self.target_progress is not None:
            result['targetProgress'] = self.target_progress.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkpointId') is not None:
            self.checkpoint_id = m.get('checkpointId')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('lastSyncTime') is not None:
            self.last_sync_time = m.get('lastSyncTime')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('sourceProgress') is not None:
            temp_model = main_models.ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgress()
            self.source_progress = temp_model.from_map(m.get('sourceProgress'))

        if m.get('targetProgress') is not None:
            temp_model = main_models.ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgress()
            self.target_progress = temp_model.from_map(m.get('targetProgress'))

        return self

class ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgress(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        last_fetch_time: int = None,
        progress_data: main_models.ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgressProgressData = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The instance ID.
        self.instance_id = instance_id
        # The instance type. Valid values:
        # - ALIYUN_ROCKETMQ: Alibaba Cloud instance.
        # - EXTERNAL_ROCKETMQ: external instance, open source instance, or open source cluster.
        self.instance_type = instance_type
        # The latest fetch time. The value is a UNIX timestamp in milliseconds.
        self.last_fetch_time = last_fetch_time
        # The consumer offset data.
        self.progress_data = progress_data
        # The region ID.
        self.region_id = region_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        if self.progress_data:
            self.progress_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.last_fetch_time is not None:
            result['lastFetchTime'] = self.last_fetch_time

        if self.progress_data is not None:
            result['progressData'] = self.progress_data.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('lastFetchTime') is not None:
            self.last_fetch_time = m.get('lastFetchTime')

        if m.get('progressData') is not None:
            temp_model = main_models.ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgressProgressData()
            self.progress_data = temp_model.from_map(m.get('progressData'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

class ListDisasterRecoveryCheckpointsResponseBodyDataListTargetProgressProgressData(DaraModel):
    def __init__(
        self,
        consume_timestamp: int = None,
    ):
        # The latest consumption time.
        self.consume_timestamp = consume_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_timestamp is not None:
            result['consumeTimestamp'] = self.consume_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeTimestamp') is not None:
            self.consume_timestamp = m.get('consumeTimestamp')

        return self

class ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgress(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        last_fetch_time: int = None,
        progress_data: main_models.ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgressProgressData = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The instance ID.
        self.instance_id = instance_id
        # The instance type. Valid values:
        # - ALIYUN_ROCKETMQ: Alibaba Cloud instance.
        # - EXTERNAL_ROCKETMQ: external instance, open source instance, or open source cluster.
        self.instance_type = instance_type
        # The most recent fetch time. The value is a UNIX timestamp in milliseconds.
        self.last_fetch_time = last_fetch_time
        # The consumer offset data.
        self.progress_data = progress_data
        # The region ID.
        self.region_id = region_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        if self.progress_data:
            self.progress_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.last_fetch_time is not None:
            result['lastFetchTime'] = self.last_fetch_time

        if self.progress_data is not None:
            result['progressData'] = self.progress_data.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('lastFetchTime') is not None:
            self.last_fetch_time = m.get('lastFetchTime')

        if m.get('progressData') is not None:
            temp_model = main_models.ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgressProgressData()
            self.progress_data = temp_model.from_map(m.get('progressData'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

class ListDisasterRecoveryCheckpointsResponseBodyDataListSourceProgressProgressData(DaraModel):
    def __init__(
        self,
        consume_timestamp: int = None,
    ):
        # The latest consumption time.
        self.consume_timestamp = consume_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_timestamp is not None:
            result['consumeTimestamp'] = self.consume_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumeTimestamp') is not None:
            self.consume_timestamp = m.get('consumeTimestamp')

        return self

