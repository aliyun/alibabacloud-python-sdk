# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeRtcCloudRecordingFilesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_info: main_models.DescribeRtcCloudRecordingFilesResponseBodyTaskInfo = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task information.
        self.task_info = task_info

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_info is not None:
            result['TaskInfo'] = self.task_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskInfo') is not None:
            temp_model = main_models.DescribeRtcCloudRecordingFilesResponseBodyTaskInfo()
            self.task_info = temp_model.from_map(m.get('TaskInfo'))

        return self

class DescribeRtcCloudRecordingFilesResponseBodyTaskInfo(DaraModel):
    def __init__(
        self,
        record_file_list: main_models.DescribeRtcCloudRecordingFilesResponseBodyTaskInfoRecordFileList = None,
        status: str = None,
        task_id: str = None,
    ):
        # The list of recording files.
        self.record_file_list = record_file_list
        # The task status. Valid values:
        # - RUNNING
        # - RECOVERING
        # - STOPPING
        # - STOPPED.
        self.status = status
        # The task ID passed in the request.
        self.task_id = task_id

    def validate(self):
        if self.record_file_list:
            self.record_file_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_file_list is not None:
            result['RecordFileList'] = self.record_file_list.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordFileList') is not None:
            temp_model = main_models.DescribeRtcCloudRecordingFilesResponseBodyTaskInfoRecordFileList()
            self.record_file_list = temp_model.from_map(m.get('RecordFileList'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeRtcCloudRecordingFilesResponseBodyTaskInfoRecordFileList(DaraModel):
    def __init__(
        self,
        hls_file_list: List[str] = None,
        mp_3file_list: List[str] = None,
        mp_4file_list: List[str] = None,
        vod_media_list: List[main_models.DescribeRtcCloudRecordingFilesResponseBodyTaskInfoRecordFileListVodMediaList] = None,
    ):
        # The array of HLS recording file names.
        self.hls_file_list = hls_file_list
        # The array of MP3 recording file names.
        self.mp_3file_list = mp_3file_list
        # The array of MP4 recording file names.
        self.mp_4file_list = mp_4file_list
        # The array of VOD media resources. When recording to VOD, this is the collection of recording files for each subscribed stream, where each item corresponds to a subscribed stream.
        self.vod_media_list = vod_media_list

    def validate(self):
        if self.vod_media_list:
            for v1 in self.vod_media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hls_file_list is not None:
            result['HlsFileList'] = self.hls_file_list

        if self.mp_3file_list is not None:
            result['Mp3FileList'] = self.mp_3file_list

        if self.mp_4file_list is not None:
            result['Mp4FileList'] = self.mp_4file_list

        result['VodMediaList'] = []
        if self.vod_media_list is not None:
            for k1 in self.vod_media_list:
                result['VodMediaList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HlsFileList') is not None:
            self.hls_file_list = m.get('HlsFileList')

        if m.get('Mp3FileList') is not None:
            self.mp_3file_list = m.get('Mp3FileList')

        if m.get('Mp4FileList') is not None:
            self.mp_4file_list = m.get('Mp4FileList')

        self.vod_media_list = []
        if m.get('VodMediaList') is not None:
            for k1 in m.get('VodMediaList'):
                temp_model = main_models.DescribeRtcCloudRecordingFilesResponseBodyTaskInfoRecordFileListVodMediaList()
                self.vod_media_list.append(temp_model.from_map(k1))

        return self

class DescribeRtcCloudRecordingFilesResponseBodyTaskInfoRecordFileListVodMediaList(DaraModel):
    def __init__(
        self,
        media_ids: List[str] = None,
        merged_ids: List[str] = None,
        stream: str = None,
    ):
        # The array of media resource IDs generated during recording.
        self.media_ids = media_ids
        # The array of automatically merged media resource IDs generated after recording ends.
        self.merged_ids = merged_ids
        # The subscribed stream.
        #  - For stream mixing recording, the value is always Mix.
        #  - For single-stream recording, the value is Single::{UserId}::{Suffix}.
        #    - UserId is the UserId corresponding to this stream.
        #    - Suffix depends on the StreamType and SourceType specified during subscription.
        #      - When StreamType is 0: if SourceType is 0, Suffix is AV::C. If SourceType is 1, Suffix is AV::S.
        #      - When StreamType is 1: Suffix can only be A.
        #      - When StreamType is 2 (not supported for single-stream recording): if SourceType is 0, Suffix is V::C. If SourceType is 1, Suffix is V::S.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.merged_ids is not None:
            result['MergedIds'] = self.merged_ids

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('MergedIds') is not None:
            self.merged_ids = m.get('MergedIds')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

