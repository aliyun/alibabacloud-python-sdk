# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetLiveEditingJobResponseBody(DaraModel):
    def __init__(
        self,
        live_editing_job: main_models.GetLiveEditingJobResponseBodyLiveEditingJob = None,
        request_id: str = None,
    ):
        # The information about the live editing job.
        self.live_editing_job = live_editing_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_editing_job:
            self.live_editing_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_editing_job is not None:
            result['LiveEditingJob'] = self.live_editing_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveEditingJob') is not None:
            temp_model = main_models.GetLiveEditingJobResponseBodyLiveEditingJob()
            self.live_editing_job = temp_model.from_map(m.get('LiveEditingJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLiveEditingJobResponseBodyLiveEditingJob(DaraModel):
    def __init__(
        self,
        clips: str = None,
        code: str = None,
        complete_time: str = None,
        creation_time: str = None,
        job_id: str = None,
        live_stream_config: main_models.GetLiveEditingJobResponseBodyLiveEditingJobLiveStreamConfig = None,
        media_id: str = None,
        media_produce_config: main_models.GetLiveEditingJobResponseBodyLiveEditingJobMediaProduceConfig = None,
        media_url: str = None,
        message: str = None,
        modified_time: str = None,
        output_media_config: main_models.GetLiveEditingJobResponseBodyLiveEditingJobOutputMediaConfig = None,
        project_id: str = None,
        status: str = None,
        user_data: str = None,
    ):
        # The clips.
        self.clips = clips
        # The response code. Note: Pay attention to this parameter if the job failed.
        self.code = code
        # The time when the live editing job was completed. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.complete_time = complete_time
        # The time when the live editing job was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The ID of the live editing job.
        self.job_id = job_id
        # The live editing configurations.
        self.live_stream_config = live_stream_config
        # The media asset ID of the output file.
        self.media_id = media_id
        # The production configurations.
        self.media_produce_config = media_produce_config
        # The URL of the output file.
        self.media_url = media_url
        # The returned message. Note: Pay attention to this parameter if the job failed.
        self.message = message
        # The time when the live editing job was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The storage configurations of the output file.
        self.output_media_config = output_media_config
        # The ID of the live editing project.
        self.project_id = project_id
        # The state of the live editing job. Valid values: Init, Queuing, Processing, Success, and Failed.
        self.status = status
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.live_stream_config:
            self.live_stream_config.validate()
        if self.media_produce_config:
            self.media_produce_config.validate()
        if self.output_media_config:
            self.output_media_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clips is not None:
            result['Clips'] = self.clips

        if self.code is not None:
            result['Code'] = self.code

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.live_stream_config is not None:
            result['LiveStreamConfig'] = self.live_stream_config.to_map()

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_produce_config is not None:
            result['MediaProduceConfig'] = self.media_produce_config.to_map()

        if self.media_url is not None:
            result['MediaURL'] = self.media_url

        if self.message is not None:
            result['Message'] = self.message

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config.to_map()

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clips') is not None:
            self.clips = m.get('Clips')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('LiveStreamConfig') is not None:
            temp_model = main_models.GetLiveEditingJobResponseBodyLiveEditingJobLiveStreamConfig()
            self.live_stream_config = temp_model.from_map(m.get('LiveStreamConfig'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaProduceConfig') is not None:
            temp_model = main_models.GetLiveEditingJobResponseBodyLiveEditingJobMediaProduceConfig()
            self.media_produce_config = temp_model.from_map(m.get('MediaProduceConfig'))

        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('OutputMediaConfig') is not None:
            temp_model = main_models.GetLiveEditingJobResponseBodyLiveEditingJobOutputMediaConfig()
            self.output_media_config = temp_model.from_map(m.get('OutputMediaConfig'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetLiveEditingJobResponseBodyLiveEditingJobOutputMediaConfig(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        file_name: str = None,
        height: int = None,
        media_url: str = None,
        storage_location: str = None,
        vod_template_group_id: str = None,
        width: int = None,
    ):
        # The bitrate of the output file. Unit: Kbit/s. You can leave this parameter empty. The default value is the maximum bitrate of the input materials.
        self.bitrate = bitrate
        # If OutputMediaTarget is set to vod-media, this parameter indicates the file name of the output file. The value contains the file name extension but not the path.
        self.file_name = file_name
        # The height of the output file. You can leave this parameter empty. The default value is the maximum height of the input materials.
        self.height = height
        # The URL of the output file.
        self.media_url = media_url
        # If OutputMediaTarget is set to vod-media, this parameter indicates the storage location of the media asset in ApsaraVideo VOD. The storage location is the path of the file in ApsaraVideo VOD, excluding the prefix http://. Example: outin-xxxxxx.oss-cn-shanghai.aliyuncs.com.
        self.storage_location = storage_location
        # The ID of the VOD transcoding template group. If VOD transcoding is not required, set the value to VOD_NO_TRANSCODE.
        self.vod_template_group_id = vod_template_group_id
        # The width of the output file. You can leave this parameter empty. The default value is the maximum width of the input materials.
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

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.height is not None:
            result['Height'] = self.height

        if self.media_url is not None:
            result['MediaURL'] = self.media_url

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.vod_template_group_id is not None:
            result['VodTemplateGroupId'] = self.vod_template_group_id

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MediaURL') is not None:
            self.media_url = m.get('MediaURL')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('VodTemplateGroupId') is not None:
            self.vod_template_group_id = m.get('VodTemplateGroupId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetLiveEditingJobResponseBodyLiveEditingJobMediaProduceConfig(DaraModel):
    def __init__(
        self,
        mode: str = None,
    ):
        # The editing mode. Default value: Accurate.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class GetLiveEditingJobResponseBodyLiveEditingJobLiveStreamConfig(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The domain name of the live stream.
        self.domain_name = domain_name
        # The name of the live stream.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

