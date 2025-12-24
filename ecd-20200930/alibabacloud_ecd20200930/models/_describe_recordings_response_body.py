# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeRecordingsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        recordings: List[main_models.DescribeRecordingsResponseBodyRecordings] = None,
        request_id: str = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The screen recording files.
        self.recordings = recordings
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.recordings:
            for v1 in self.recordings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Recordings'] = []
        if self.recordings is not None:
            for k1 in self.recordings:
                result['Recordings'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.recordings = []
        if m.get('Recordings') is not None:
            for k1 in m.get('Recordings'):
                temp_model = main_models.DescribeRecordingsResponseBodyRecordings()
                self.recordings.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRecordingsResponseBodyRecordings(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
        end_time: str = None,
        end_user_ids: List[str] = None,
        file_path: str = None,
        policy_group_id: str = None,
        recording_size: int = None,
        recording_type: str = None,
        signed_url: str = None,
        start_time: str = None,
    ):
        # The cloud computer ID.
        self.desktop_id = desktop_id
        # The cloud computer name.
        self.desktop_name = desktop_name
        # The end time of the recording.
        self.end_time = end_time
        # The end user IDs.
        self.end_user_ids = end_user_ids
        # The file path.
        self.file_path = file_path
        # The policy ID.
        self.policy_group_id = policy_group_id
        # The size of the screen recording file. Unit: bytes.
        self.recording_size = recording_size
        # The type of event that triggers the recording.
        # 
        # Valid values:
        # 
        # *   byaction_cmd_ft: triggered by copy-paste or file transfer events.
        # *   period: triggered at scheduled intervals.
        # *   session: triggered by session lifecycle monitoring.
        # *   byaction_commands: triggered by copy-paste only.
        # *   alltime: continuous recording.
        # *   byaction_file_transfer: triggered by file transfer only.
        self.recording_type = recording_type
        # The download URL of the screen recording file.
        self.signed_url = signed_url
        # The start time of the recording.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.recording_size is not None:
            result['RecordingSize'] = self.recording_size

        if self.recording_type is not None:
            result['RecordingType'] = self.recording_type

        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('RecordingSize') is not None:
            self.recording_size = m.get('RecordingSize')

        if m.get('RecordingType') is not None:
            self.recording_type = m.get('RecordingType')

        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

