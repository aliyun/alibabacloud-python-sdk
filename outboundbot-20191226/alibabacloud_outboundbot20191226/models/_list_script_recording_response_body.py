# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListScriptRecordingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        script_recordings: List[main_models.ListScriptRecordingResponseBodyScriptRecordings] = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.script_recordings = script_recordings
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.script_recordings:
            for v1 in self.script_recordings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScriptRecordings'] = []
        if self.script_recordings is not None:
            for k1 in self.script_recordings:
                result['ScriptRecordings'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.script_recordings = []
        if m.get('ScriptRecordings') is not None:
            for k1 in m.get('ScriptRecordings'):
                temp_model = main_models.ListScriptRecordingResponseBodyScriptRecordings()
                self.script_recordings.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScriptRecordingResponseBodyScriptRecordings(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        gmt_upload: int = None,
        inner_id: str = None,
        instance_id: str = None,
        recording_content: str = None,
        recording_duration: int = None,
        recording_name: str = None,
        ref_id: str = None,
        script_id: str = None,
        state: int = None,
        state_extend: str = None,
        storage_uuid: str = None,
        uuid: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.gmt_upload = gmt_upload
        self.inner_id = inner_id
        self.instance_id = instance_id
        self.recording_content = recording_content
        self.recording_duration = recording_duration
        self.recording_name = recording_name
        self.ref_id = ref_id
        self.script_id = script_id
        self.state = state
        self.state_extend = state_extend
        self.storage_uuid = storage_uuid
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.gmt_upload is not None:
            result['GmtUpload'] = self.gmt_upload

        if self.inner_id is not None:
            result['InnerId'] = self.inner_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.recording_content is not None:
            result['RecordingContent'] = self.recording_content

        if self.recording_duration is not None:
            result['RecordingDuration'] = self.recording_duration

        if self.recording_name is not None:
            result['RecordingName'] = self.recording_name

        if self.ref_id is not None:
            result['RefId'] = self.ref_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.state is not None:
            result['State'] = self.state

        if self.state_extend is not None:
            result['StateExtend'] = self.state_extend

        if self.storage_uuid is not None:
            result['StorageUuid'] = self.storage_uuid

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GmtUpload') is not None:
            self.gmt_upload = m.get('GmtUpload')

        if m.get('InnerId') is not None:
            self.inner_id = m.get('InnerId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RecordingContent') is not None:
            self.recording_content = m.get('RecordingContent')

        if m.get('RecordingDuration') is not None:
            self.recording_duration = m.get('RecordingDuration')

        if m.get('RecordingName') is not None:
            self.recording_name = m.get('RecordingName')

        if m.get('RefId') is not None:
            self.ref_id = m.get('RefId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StateExtend') is not None:
            self.state_extend = m.get('StateExtend')

        if m.get('StorageUuid') is not None:
            self.storage_uuid = m.get('StorageUuid')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

