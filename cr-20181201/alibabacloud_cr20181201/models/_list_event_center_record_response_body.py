# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListEventCenterRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        records: List[main_models.ListEventCenterRecordResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The list of historical events.
        self.records = records
        # The ID of the request.
        self.request_id = request_id
        # The total entries of historical events.
        self.total_count = total_count

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.ListEventCenterRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEventCenterRecordResponseBodyRecords(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        event_channel: str = None,
        event_notify_id: str = None,
        event_notify_method: str = None,
        event_type: str = None,
        instance_id: str = None,
        namespace: str = None,
        record_id: str = None,
        repo_name: str = None,
        rule_id: str = None,
        rule_name: str = None,
        tag: str = None,
        update_time: int = None,
    ):
        # The time when the event was created.
        self.create_time = create_time
        # The event notification channel.
        self.event_channel = event_channel
        # The ID of the event notification.
        self.event_notify_id = event_notify_id
        # The notification method. Valid values:
        # 
        # *   `http`: The notification is sent over HTTP.
        # *   `https`: The notification is sent over HTTPS.
        # *   `dingding`: The notification is sent by using DingTalk.
        self.event_notify_method = event_notify_method
        # The type of the event.
        self.event_type = event_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The namespace.
        self.namespace = namespace
        # The ID of the event record.
        self.record_id = record_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The ID of the event notification rule.
        self.rule_id = rule_id
        # The name of the event notification rule.
        self.rule_name = rule_name
        # The tags.
        self.tag = tag
        # The time when the event was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.event_channel is not None:
            result['EventChannel'] = self.event_channel

        if self.event_notify_id is not None:
            result['EventNotifyId'] = self.event_notify_id

        if self.event_notify_method is not None:
            result['EventNotifyMethod'] = self.event_notify_method

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EventChannel') is not None:
            self.event_channel = m.get('EventChannel')

        if m.get('EventNotifyId') is not None:
            self.event_notify_id = m.get('EventNotifyId')

        if m.get('EventNotifyMethod') is not None:
            self.event_notify_method = m.get('EventNotifyMethod')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

