# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenStructIdpSyncRecord(DaraModel):
    def __init__(
        self,
        action: str = None,
        idp_raw_json: str = None,
        idp_resource_id: str = None,
        name: str = None,
        record_type: str = None,
        sase_raw_json: str = None,
        sase_resource_id: str = None,
        success: bool = None,
        sync_record_id: str = None,
        sync_task_id: str = None,
        time_unix: str = None,
    ):
        self.action = action
        self.idp_raw_json = idp_raw_json
        self.idp_resource_id = idp_resource_id
        self.name = name
        self.record_type = record_type
        self.sase_raw_json = sase_raw_json
        self.sase_resource_id = sase_resource_id
        self.success = success
        self.sync_record_id = sync_record_id
        self.sync_task_id = sync_task_id
        self.time_unix = time_unix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.idp_raw_json is not None:
            result['IdpRawJson'] = self.idp_raw_json

        if self.idp_resource_id is not None:
            result['IdpResourceId'] = self.idp_resource_id

        if self.name is not None:
            result['Name'] = self.name

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.sase_raw_json is not None:
            result['SaseRawJson'] = self.sase_raw_json

        if self.sase_resource_id is not None:
            result['SaseResourceId'] = self.sase_resource_id

        if self.success is not None:
            result['Success'] = self.success

        if self.sync_record_id is not None:
            result['SyncRecordId'] = self.sync_record_id

        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id

        if self.time_unix is not None:
            result['TimeUnix'] = self.time_unix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('IdpRawJson') is not None:
            self.idp_raw_json = m.get('IdpRawJson')

        if m.get('IdpResourceId') is not None:
            self.idp_resource_id = m.get('IdpResourceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('SaseRawJson') is not None:
            self.sase_raw_json = m.get('SaseRawJson')

        if m.get('SaseResourceId') is not None:
            self.sase_resource_id = m.get('SaseResourceId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('SyncRecordId') is not None:
            self.sync_record_id = m.get('SyncRecordId')

        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')

        if m.get('TimeUnix') is not None:
            self.time_unix = m.get('TimeUnix')

        return self

