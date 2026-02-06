# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetTranscodeSummaryResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_video_ids: List[str] = None,
        request_id: str = None,
        transcode_summary_list: List[main_models.GetTranscodeSummaryResponseBodyTranscodeSummaryList] = None,
    ):
        # The IDs of the audio or video files that do not exist.
        self.non_exist_video_ids = non_exist_video_ids
        # The ID of the request.
        self.request_id = request_id
        # The transcoding summary of the file.
        self.transcode_summary_list = transcode_summary_list

    def validate(self):
        if self.transcode_summary_list:
            for v1 in self.transcode_summary_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TranscodeSummaryList'] = []
        if self.transcode_summary_list is not None:
            for k1 in self.transcode_summary_list:
                result['TranscodeSummaryList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.transcode_summary_list = []
        if m.get('TranscodeSummaryList') is not None:
            for k1 in m.get('TranscodeSummaryList'):
                temp_model = main_models.GetTranscodeSummaryResponseBodyTranscodeSummaryList()
                self.transcode_summary_list.append(temp_model.from_map(k1))

        return self

class GetTranscodeSummaryResponseBodyTranscodeSummaryList(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        creation_time: str = None,
        transcode_job_info_summary_list: List[main_models.GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList] = None,
        transcode_status: str = None,
        transcode_template_group_id: str = None,
        video_id: str = None,
    ):
        # The time when the transcoding task was complete. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.complete_time = complete_time
        # The time when the transcoding task was created. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The summaries of transcoding jobs.
        self.transcode_job_info_summary_list = transcode_job_info_summary_list
        # The status of the transcoding task. Valid values:
        # 
        # *   **Processing**: Transcoding is in process.
        # *   **Partial**: Some transcoding jobs were complete.
        # *   **CompleteAllSucc**: All transcoding jobs were successful.
        # *   **CompleteAllFail**: All transcoding jobs failed. If an exception occurs in the source file, no transcoding job is initiated and the transcoding task fails.
        # *   **CompletePartialSucc**: All transcoding jobs were complete but only some were successful.
        self.transcode_status = transcode_status
        # The ID of the transcoding template group.
        self.transcode_template_group_id = transcode_template_group_id
        # The ID of the audio or video file.
        self.video_id = video_id

    def validate(self):
        if self.transcode_job_info_summary_list:
            for v1 in self.transcode_job_info_summary_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        result['TranscodeJobInfoSummaryList'] = []
        if self.transcode_job_info_summary_list is not None:
            for k1 in self.transcode_job_info_summary_list:
                result['TranscodeJobInfoSummaryList'].append(k1.to_map() if k1 else None)

        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status

        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        self.transcode_job_info_summary_list = []
        if m.get('TranscodeJobInfoSummaryList') is not None:
            for k1 in m.get('TranscodeJobInfoSummaryList'):
                temp_model = main_models.GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList()
                self.transcode_job_info_summary_list.append(temp_model.from_map(k1))

        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')

        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

class GetTranscodeSummaryResponseBodyTranscodeSummaryListTranscodeJobInfoSummaryList(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        complete_time: str = None,
        creation_time: str = None,
        duration: str = None,
        error_code: str = None,
        error_message: str = None,
        filesize: int = None,
        format: str = None,
        fps: str = None,
        height: str = None,
        transcode_job_status: str = None,
        transcode_progress: int = None,
        transcode_template_id: str = None,
        watermark_id_list: List[str] = None,
        width: str = None,
    ):
        # The average bitrate of the output video. Unit: Kbit/s.
        self.bitrate = bitrate
        # The time when the transcoding job was complete. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.complete_time = complete_time
        # The time when the transcoding job was created. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The duration of the output video. Unit: seconds.
        self.duration = duration
        # The error code returned when the transcoding job failed.
        self.error_code = error_code
        # The error message returned when the transcoding job failed.
        self.error_message = error_message
        # The size of the output video. Unit: bytes.
        self.filesize = filesize
        # The container format of the output video.
        self.format = format
        # The frame rate of the output video. Unit: frames per second.
        self.fps = fps
        # The height of the output video. Unit: pixels.
        self.height = height
        # The status of the transcoding job. Valid values:
        # 
        # *   **Transcoding**: Transcoding is in process.
        # *   **TranscodeSuccess**: The job was successful.
        # *   **TranscodeFail**: The job failed.
        self.transcode_job_status = transcode_job_status
        # The transcoding progress. Valid values: `[0,100]`.
        self.transcode_progress = transcode_progress
        # The ID of the transcoding template.
        self.transcode_template_id = transcode_template_id
        # The IDs of the watermarks that are applied to the output video.
        self.watermark_id_list = watermark_id_list
        # The width of the output video. Unit: pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.filesize is not None:
            result['Filesize'] = self.filesize

        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.transcode_job_status is not None:
            result['TranscodeJobStatus'] = self.transcode_job_status

        if self.transcode_progress is not None:
            result['TranscodeProgress'] = self.transcode_progress

        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id

        if self.watermark_id_list is not None:
            result['WatermarkIdList'] = self.watermark_id_list

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('TranscodeJobStatus') is not None:
            self.transcode_job_status = m.get('TranscodeJobStatus')

        if m.get('TranscodeProgress') is not None:
            self.transcode_progress = m.get('TranscodeProgress')

        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')

        if m.get('WatermarkIdList') is not None:
            self.watermark_id_list = m.get('WatermarkIdList')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

