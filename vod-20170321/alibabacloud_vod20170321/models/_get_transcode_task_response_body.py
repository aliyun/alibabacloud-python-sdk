# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetTranscodeTaskResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_job_ids: List[str] = None,
        request_id: str = None,
        transcode_job_info_list: List[main_models.GetTranscodeTaskResponseBodyTranscodeJobInfoList] = None,
        transcode_task: main_models.GetTranscodeTaskResponseBodyTranscodeTask = None,
    ):
        # The IDs of transcoding jobs that do not exist.
        self.non_exist_job_ids = non_exist_job_ids
        # The request ID.
        self.request_id = request_id
        # The transcoding job information.
        self.transcode_job_info_list = transcode_job_info_list
        # The transcoding task information.
        self.transcode_task = transcode_task

    def validate(self):
        if self.transcode_job_info_list:
            for v1 in self.transcode_job_info_list:
                 if v1:
                    v1.validate()
        if self.transcode_task:
            self.transcode_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_job_ids is not None:
            result['NonExistJobIds'] = self.non_exist_job_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TranscodeJobInfoList'] = []
        if self.transcode_job_info_list is not None:
            for k1 in self.transcode_job_info_list:
                result['TranscodeJobInfoList'].append(k1.to_map() if k1 else None)

        if self.transcode_task is not None:
            result['TranscodeTask'] = self.transcode_task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistJobIds') is not None:
            self.non_exist_job_ids = m.get('NonExistJobIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.transcode_job_info_list = []
        if m.get('TranscodeJobInfoList') is not None:
            for k1 in m.get('TranscodeJobInfoList'):
                temp_model = main_models.GetTranscodeTaskResponseBodyTranscodeJobInfoList()
                self.transcode_job_info_list.append(temp_model.from_map(k1))

        if m.get('TranscodeTask') is not None:
            temp_model = main_models.GetTranscodeTaskResponseBodyTranscodeTask()
            self.transcode_task = temp_model.from_map(m.get('TranscodeTask'))

        return self

class GetTranscodeTaskResponseBodyTranscodeTask(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        creation_time: str = None,
        task_status: str = None,
        transcode_job_info_list: List[main_models.GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList] = None,
        transcode_task_id: str = None,
        transcode_template_group_id: str = None,
        trigger: str = None,
        video_id: str = None,
    ):
        # The time when the transcoding task was completed. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.complete_time = complete_time
        # The time when the transcoding task was created. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.creation_time = creation_time
        # The status of the transcoding task. Valid values:
        # 
        # - **Processing**: processing in progress.
        # - **Partial**: partially completed.
        # - **CompleteAllSucc**: all transcoding jobs are completed and succeeded.
        # - **CompleteAllFail**: all transcoding jobs are completed but failed. If the source file has issues, no transcoding jobs are initiated and the entire transcoding task fails.
        # - **CompletePartialSucc**: all transcoding jobs are completed but only some succeeded.
        self.task_status = task_status
        # The transcoding job information.
        self.transcode_job_info_list = transcode_job_info_list
        # The transcoding task ID.
        self.transcode_task_id = transcode_task_id
        # The ID of the transcoding template group used for transcoding.
        self.transcode_template_group_id = transcode_template_group_id
        # The trigger type. Valid values:
        # 
        # - **Auto**: automatically triggered after a video is uploaded.
        # - **Manual**: triggered by calling the SubmitTranscodeJobs operation.
        self.trigger = trigger
        # The audio or video ID.
        self.video_id = video_id

    def validate(self):
        if self.transcode_job_info_list:
            for v1 in self.transcode_job_info_list:
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

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        result['TranscodeJobInfoList'] = []
        if self.transcode_job_info_list is not None:
            for k1 in self.transcode_job_info_list:
                result['TranscodeJobInfoList'].append(k1.to_map() if k1 else None)

        if self.transcode_task_id is not None:
            result['TranscodeTaskId'] = self.transcode_task_id

        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id

        if self.trigger is not None:
            result['Trigger'] = self.trigger

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        self.transcode_job_info_list = []
        if m.get('TranscodeJobInfoList') is not None:
            for k1 in m.get('TranscodeJobInfoList'):
                temp_model = main_models.GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList()
                self.transcode_job_info_list.append(temp_model.from_map(k1))

        if m.get('TranscodeTaskId') is not None:
            self.transcode_task_id = m.get('TranscodeTaskId')

        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')

        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

class GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoList(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        creation_time: str = None,
        definition: str = None,
        error_code: str = None,
        error_message: str = None,
        input_file_url: str = None,
        output_file: main_models.GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile = None,
        priority: str = None,
        transcode_job_id: str = None,
        transcode_job_status: str = None,
        transcode_progress: int = None,
        transcode_template_id: str = None,
    ):
        # The time when the transcoding job was completed. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.complete_time = complete_time
        # The time when the transcoding job was created. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.creation_time = creation_time
        # The video definition. Valid values:
        # 
        # - **LD**: fluent.
        # - **SD**: standard definition.
        # - **HD**: high definition.
        # - **FHD**: ultra high definition.
        # - **OD**: original quality.
        # - **2K**: 2K.
        # - **4K**: 4K.
        # - **SQ**: standard sound quality.
        # - **HQ**: high sound quality.
        # - **AUTO**: adaptive bitrate streaming. This definition is available only when packaging is configured in the transcoding template. For more information, see [Transcoding template configuration - PackageSetting](https://help.aliyun.com/document_detail/52839.html).
        # 
        # > This value is the definition label configured in the transcoding template and does not indicate the actual resolution range of the transcoded output file.
        self.definition = definition
        # The error code returned when the transcoding job failed.
        self.error_code = error_code
        # The error message returned when the transcoding job failed.
        self.error_message = error_message
        # The OSS URL of the transcoding source file.
        self.input_file_url = input_file_url
        # The information about the transcoding output file.
        self.output_file = output_file
        # The priority of the transcoding task.
        self.priority = priority
        # The transcoding job ID.
        self.transcode_job_id = transcode_job_id
        # The status of the transcoding job. Valid values:
        # - **Transcoding**: transcoding in progress.
        # - **TranscodeSuccess**: transcoding succeeded.
        # - **TranscodeFail**: transcoding failed.
        self.transcode_job_status = transcode_job_status
        # The transcoding job progress. Value range: `[0,100]`.
        self.transcode_progress = transcode_progress
        # The ID of the transcoding template used for transcoding.
        self.transcode_template_id = transcode_template_id

    def validate(self):
        if self.output_file:
            self.output_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url

        if self.output_file is not None:
            result['OutputFile'] = self.output_file.to_map()

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.transcode_job_id is not None:
            result['TranscodeJobId'] = self.transcode_job_id

        if self.transcode_job_status is not None:
            result['TranscodeJobStatus'] = self.transcode_job_status

        if self.transcode_progress is not None:
            result['TranscodeProgress'] = self.transcode_progress

        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')

        if m.get('OutputFile') is not None:
            temp_model = main_models.GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile()
            self.output_file = temp_model.from_map(m.get('OutputFile'))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TranscodeJobId') is not None:
            self.transcode_job_id = m.get('TranscodeJobId')

        if m.get('TranscodeJobStatus') is not None:
            self.transcode_job_status = m.get('TranscodeJobStatus')

        if m.get('TranscodeProgress') is not None:
            self.transcode_progress = m.get('TranscodeProgress')

        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')

        return self

class GetTranscodeTaskResponseBodyTranscodeTaskTranscodeJobInfoListOutputFile(DaraModel):
    def __init__(
        self,
        audio_stream_list: str = None,
        bitrate: str = None,
        duration: str = None,
        encryption: str = None,
        filesize: int = None,
        format: str = None,
        fps: str = None,
        height: str = None,
        output_file_url: str = None,
        subtitle_stream_list: str = None,
        video_stream_list: str = None,
        watermark_id_list: List[str] = None,
        width: str = None,
    ):
        # The list of audio streams.
        self.audio_stream_list = audio_stream_list
        # The average bitrate of the transcoding output file. Unit: Kbps.
        self.bitrate = bitrate
        # The duration of the transcoding output file. Unit: seconds.
        self.duration = duration
        # The encryption configuration used for the transcoding output file. Valid values:
        # 
        # - **AliyunVoDEncryption**: Alibaba Cloud video encryption (proprietary encryption).
        # - **HLSEncryption**: HLS encryption.
        self.encryption = encryption
        # The size of the transcoding output file. Unit: bytes.
        self.filesize = filesize
        # The container format of the transcoding output file.
        self.format = format
        # The frame rate of the transcoding output file. Unit: frames per second.
        self.fps = fps
        # The height of the transcoding output video. Unit: px.
        self.height = height
        # The OSS URL of the transcoding output file.
        self.output_file_url = output_file_url
        # The list of subtitle streams.
        self.subtitle_stream_list = subtitle_stream_list
        # The list of video streams.
        self.video_stream_list = video_stream_list
        # The list of watermark IDs used for the transcoding output file.
        self.watermark_id_list = watermark_id_list
        # The width of the transcoding output video. Unit: px.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_stream_list is not None:
            result['AudioStreamList'] = self.audio_stream_list

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.encryption is not None:
            result['Encryption'] = self.encryption

        if self.filesize is not None:
            result['Filesize'] = self.filesize

        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.output_file_url is not None:
            result['OutputFileUrl'] = self.output_file_url

        if self.subtitle_stream_list is not None:
            result['SubtitleStreamList'] = self.subtitle_stream_list

        if self.video_stream_list is not None:
            result['VideoStreamList'] = self.video_stream_list

        if self.watermark_id_list is not None:
            result['WatermarkIdList'] = self.watermark_id_list

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioStreamList') is not None:
            self.audio_stream_list = m.get('AudioStreamList')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')

        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('OutputFileUrl') is not None:
            self.output_file_url = m.get('OutputFileUrl')

        if m.get('SubtitleStreamList') is not None:
            self.subtitle_stream_list = m.get('SubtitleStreamList')

        if m.get('VideoStreamList') is not None:
            self.video_stream_list = m.get('VideoStreamList')

        if m.get('WatermarkIdList') is not None:
            self.watermark_id_list = m.get('WatermarkIdList')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetTranscodeTaskResponseBodyTranscodeJobInfoList(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        creation_time: str = None,
        definition: str = None,
        error_code: str = None,
        error_message: str = None,
        input_file_url: str = None,
        output_file: main_models.GetTranscodeTaskResponseBodyTranscodeJobInfoListOutputFile = None,
        priority: str = None,
        transcode_job_id: str = None,
        transcode_job_status: str = None,
        transcode_progress: int = None,
        transcode_template_id: str = None,
    ):
        # The time when the transcoding job was completed. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.complete_time = complete_time
        # The time when the transcoding job was created. The time is in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.creation_time = creation_time
        # The video definition. Valid values:
        # 
        # - **LD**: fluent.
        # - **SD**: standard definition.
        # - **HD**: high definition.
        # - **FHD**: ultra high definition.
        # - **OD**: original quality.
        # - **2K**: 2K.
        # - **4K**: 4K.
        # - **SQ**: standard sound quality.
        # - **HQ**: high sound quality.
        # - **AUTO**: adaptive bitrate streaming. This definition is available only when packaging is configured in the transcoding template. For more information, see [Transcoding template configuration - PackageSetting](https://help.aliyun.com/document_detail/52839.html).
        # 
        # > This value is the definition label configured in the transcoding template and does not indicate the actual resolution range of the transcoded output file.
        self.definition = definition
        # The error code returned when the transcoding job failed.
        self.error_code = error_code
        # The error message returned when the transcoding job failed.
        self.error_message = error_message
        # The OSS URL of the transcoding source file.
        self.input_file_url = input_file_url
        # The information about the transcoding output file.
        self.output_file = output_file
        # The priority of the transcoding task.
        self.priority = priority
        # The transcoding job ID.
        self.transcode_job_id = transcode_job_id
        # The status of the transcoding job. Valid values:
        # - **Transcoding**: transcoding in progress.
        # - **TranscodeSuccess**: transcoding succeeded.
        # - **TranscodeFail**: transcoding failed.
        self.transcode_job_status = transcode_job_status
        # The transcoding job progress. Value range: `[0,100]`.
        self.transcode_progress = transcode_progress
        # The ID of the transcoding template used for transcoding.
        self.transcode_template_id = transcode_template_id

    def validate(self):
        if self.output_file:
            self.output_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.input_file_url is not None:
            result['InputFileUrl'] = self.input_file_url

        if self.output_file is not None:
            result['OutputFile'] = self.output_file.to_map()

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.transcode_job_id is not None:
            result['TranscodeJobId'] = self.transcode_job_id

        if self.transcode_job_status is not None:
            result['TranscodeJobStatus'] = self.transcode_job_status

        if self.transcode_progress is not None:
            result['TranscodeProgress'] = self.transcode_progress

        if self.transcode_template_id is not None:
            result['TranscodeTemplateId'] = self.transcode_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InputFileUrl') is not None:
            self.input_file_url = m.get('InputFileUrl')

        if m.get('OutputFile') is not None:
            temp_model = main_models.GetTranscodeTaskResponseBodyTranscodeJobInfoListOutputFile()
            self.output_file = temp_model.from_map(m.get('OutputFile'))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TranscodeJobId') is not None:
            self.transcode_job_id = m.get('TranscodeJobId')

        if m.get('TranscodeJobStatus') is not None:
            self.transcode_job_status = m.get('TranscodeJobStatus')

        if m.get('TranscodeProgress') is not None:
            self.transcode_progress = m.get('TranscodeProgress')

        if m.get('TranscodeTemplateId') is not None:
            self.transcode_template_id = m.get('TranscodeTemplateId')

        return self

class GetTranscodeTaskResponseBodyTranscodeJobInfoListOutputFile(DaraModel):
    def __init__(
        self,
        audio_stream_list: str = None,
        bitrate: str = None,
        duration: str = None,
        encryption: str = None,
        filesize: int = None,
        format: str = None,
        fps: str = None,
        height: str = None,
        output_file_url: str = None,
        subtitle_stream_list: str = None,
        video_stream_list: str = None,
        watermark_id_list: List[str] = None,
        width: str = None,
    ):
        # The list of audio streams.
        self.audio_stream_list = audio_stream_list
        # The average bitrate of the transcoding output file. Unit: Kbps.
        self.bitrate = bitrate
        # The duration of the transcoding output file. Unit: seconds.
        self.duration = duration
        # The encryption configuration used for the transcoding output file. Valid values:
        # 
        # - **AliyunVoDEncryption**: Alibaba Cloud video encryption (proprietary encryption).
        # - **HLSEncryption**: HLS encryption.
        self.encryption = encryption
        # The size of the transcoding output file. Unit: bytes.
        self.filesize = filesize
        # The container format of the transcoding output file.
        self.format = format
        # The frame rate of the transcoding output file. Unit: frames per second.
        self.fps = fps
        # The height of the transcoding output video. Unit: px.
        self.height = height
        # The OSS URL of the transcoding output file.
        self.output_file_url = output_file_url
        # The list of subtitle streams.
        self.subtitle_stream_list = subtitle_stream_list
        # The list of video streams.
        self.video_stream_list = video_stream_list
        # The list of watermarks used for transcoding.
        self.watermark_id_list = watermark_id_list
        # The width of the transcoding output video. Unit: px.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_stream_list is not None:
            result['AudioStreamList'] = self.audio_stream_list

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.encryption is not None:
            result['Encryption'] = self.encryption

        if self.filesize is not None:
            result['Filesize'] = self.filesize

        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.output_file_url is not None:
            result['OutputFileUrl'] = self.output_file_url

        if self.subtitle_stream_list is not None:
            result['SubtitleStreamList'] = self.subtitle_stream_list

        if self.video_stream_list is not None:
            result['VideoStreamList'] = self.video_stream_list

        if self.watermark_id_list is not None:
            result['WatermarkIdList'] = self.watermark_id_list

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioStreamList') is not None:
            self.audio_stream_list = m.get('AudioStreamList')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')

        if m.get('Filesize') is not None:
            self.filesize = m.get('Filesize')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('OutputFileUrl') is not None:
            self.output_file_url = m.get('OutputFileUrl')

        if m.get('SubtitleStreamList') is not None:
            self.subtitle_stream_list = m.get('SubtitleStreamList')

        if m.get('VideoStreamList') is not None:
            self.video_stream_list = m.get('VideoStreamList')

        if m.get('WatermarkIdList') is not None:
            self.watermark_id_list = m.get('WatermarkIdList')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

