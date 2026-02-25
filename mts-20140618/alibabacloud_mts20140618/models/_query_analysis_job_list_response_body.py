# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryAnalysisJobListResponseBody(DaraModel):
    def __init__(
        self,
        analysis_job_list: main_models.QueryAnalysisJobListResponseBodyAnalysisJobList = None,
        non_exist_analysis_job_ids: main_models.QueryAnalysisJobListResponseBodyNonExistAnalysisJobIds = None,
        request_id: str = None,
    ):
        self.analysis_job_list = analysis_job_list
        self.non_exist_analysis_job_ids = non_exist_analysis_job_ids
        # The status of the job. Valid values:
        # 
        # *   **Submitted**: The job has been submitted.
        # *   **Analyzing**: The job is being run.
        # *   **Success**: The job is successful.
        # *   **Fail**: The job fails.
        self.request_id = request_id

    def validate(self):
        if self.analysis_job_list:
            self.analysis_job_list.validate()
        if self.non_exist_analysis_job_ids:
            self.non_exist_analysis_job_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_job_list is not None:
            result['AnalysisJobList'] = self.analysis_job_list.to_map()

        if self.non_exist_analysis_job_ids is not None:
            result['NonExistAnalysisJobIds'] = self.non_exist_analysis_job_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisJobList') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobList()
            self.analysis_job_list = temp_model.from_map(m.get('AnalysisJobList'))

        if m.get('NonExistAnalysisJobIds') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyNonExistAnalysisJobIds()
            self.non_exist_analysis_job_ids = temp_model.from_map(m.get('NonExistAnalysisJobIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryAnalysisJobListResponseBodyNonExistAnalysisJobIds(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobList(DaraModel):
    def __init__(
        self,
        analysis_job: List[main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJob] = None,
    ):
        self.analysis_job = analysis_job

    def validate(self):
        if self.analysis_job:
            for v1 in self.analysis_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnalysisJob'] = []
        if self.analysis_job is not None:
            for k1 in self.analysis_job:
                result['AnalysisJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.analysis_job = []
        if m.get('AnalysisJob') is not None:
            for k1 in m.get('AnalysisJob'):
                temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJob()
                self.analysis_job.append(temp_model.from_map(k1))

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJob(DaraModel):
    def __init__(
        self,
        analysis_config: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfig = None,
        code: str = None,
        creation_time: str = None,
        id: str = None,
        input_file: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobInputFile = None,
        mnsmessage_result: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobMNSMessageResult = None,
        message: str = None,
        percent: int = None,
        pipeline_id: str = None,
        priority: str = None,
        state: str = None,
        template_list: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateList = None,
        user_data: str = None,
    ):
        self.analysis_config = analysis_config
        self.code = code
        self.creation_time = creation_time
        self.id = id
        self.input_file = input_file
        self.mnsmessage_result = mnsmessage_result
        self.message = message
        self.percent = percent
        self.pipeline_id = pipeline_id
        self.priority = priority
        self.state = state
        self.template_list = template_list
        self.user_data = user_data

    def validate(self):
        if self.analysis_config:
            self.analysis_config.validate()
        if self.input_file:
            self.input_file.validate()
        if self.mnsmessage_result:
            self.mnsmessage_result.validate()
        if self.template_list:
            self.template_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_config is not None:
            result['AnalysisConfig'] = self.analysis_config.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.id is not None:
            result['Id'] = self.id

        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.mnsmessage_result is not None:
            result['MNSMessageResult'] = self.mnsmessage_result.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.state is not None:
            result['State'] = self.state

        if self.template_list is not None:
            result['TemplateList'] = self.template_list.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalysisConfig') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfig()
            self.analysis_config = temp_model.from_map(m.get('AnalysisConfig'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InputFile') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobInputFile()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('MNSMessageResult') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobMNSMessageResult()
            self.mnsmessage_result = temp_model.from_map(m.get('MNSMessageResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TemplateList') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateList()
            self.template_list = temp_model.from_map(m.get('TemplateList'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateList(DaraModel):
    def __init__(
        self,
        template: List[main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for v1 in self.template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Template'] = []
        if self.template is not None:
            for k1 in self.template:
                result['Template'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('Template') is not None:
            for k1 in m.get('Template'):
                temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplate()
                self.template.append(temp_model.from_map(k1))

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplate(DaraModel):
    def __init__(
        self,
        audio: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateAudio = None,
        container: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateContainer = None,
        id: str = None,
        mux_config: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfig = None,
        name: str = None,
        state: str = None,
        trans_config: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateTransConfig = None,
        video: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateVideo = None,
    ):
        self.audio = audio
        self.container = container
        self.id = id
        self.mux_config = mux_config
        self.name = name
        self.state = state
        self.trans_config = trans_config
        self.video = video

    def validate(self):
        if self.audio:
            self.audio.validate()
        if self.container:
            self.container.validate()
        if self.mux_config:
            self.mux_config.validate()
        if self.trans_config:
            self.trans_config.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio.to_map()

        if self.container is not None:
            result['Container'] = self.container.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.mux_config is not None:
            result['MuxConfig'] = self.mux_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config.to_map()

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('Container') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MuxConfig') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TransConfig') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('Video') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateVideo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        bitrate_bnd: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateVideoBitrateBnd = None,
        bufsize: str = None,
        codec: str = None,
        crf: str = None,
        degrain: str = None,
        fps: str = None,
        gop: str = None,
        height: str = None,
        maxrate: str = None,
        pix_fmt: str = None,
        preset: str = None,
        profile: str = None,
        qscale: str = None,
        scan_mode: str = None,
        width: str = None,
    ):
        self.bitrate = bitrate
        self.bitrate_bnd = bitrate_bnd
        self.bufsize = bufsize
        self.codec = codec
        self.crf = crf
        self.degrain = degrain
        self.fps = fps
        self.gop = gop
        self.height = height
        self.maxrate = maxrate
        self.pix_fmt = pix_fmt
        self.preset = preset
        self.profile = profile
        self.qscale = qscale
        self.scan_mode = scan_mode
        self.width = width

    def validate(self):
        if self.bitrate_bnd:
            self.bitrate_bnd.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.bitrate_bnd is not None:
            result['BitrateBnd'] = self.bitrate_bnd.to_map()

        if self.bufsize is not None:
            result['Bufsize'] = self.bufsize

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.crf is not None:
            result['Crf'] = self.crf

        if self.degrain is not None:
            result['Degrain'] = self.degrain

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.height is not None:
            result['Height'] = self.height

        if self.maxrate is not None:
            result['Maxrate'] = self.maxrate

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.preset is not None:
            result['Preset'] = self.preset

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.qscale is not None:
            result['Qscale'] = self.qscale

        if self.scan_mode is not None:
            result['ScanMode'] = self.scan_mode

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('BitrateBnd') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateVideoBitrateBnd()
            self.bitrate_bnd = temp_model.from_map(m.get('BitrateBnd'))

        if m.get('Bufsize') is not None:
            self.bufsize = m.get('Bufsize')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Crf') is not None:
            self.crf = m.get('Crf')

        if m.get('Degrain') is not None:
            self.degrain = m.get('Degrain')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Maxrate') is not None:
            self.maxrate = m.get('Maxrate')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Preset') is not None:
            self.preset = m.get('Preset')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Qscale') is not None:
            self.qscale = m.get('Qscale')

        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateVideoBitrateBnd(DaraModel):
    def __init__(
        self,
        max: str = None,
        min: str = None,
    ):
        self.max = max
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateTransConfig(DaraModel):
    def __init__(
        self,
        trans_mode: str = None,
    ):
        self.trans_mode = trans_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trans_mode is not None:
            result['TransMode'] = self.trans_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransMode') is not None:
            self.trans_mode = m.get('TransMode')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfig(DaraModel):
    def __init__(
        self,
        gif: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfigGif = None,
        segment: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfigSegment = None,
    ):
        self.gif = gif
        self.segment = segment

    def validate(self):
        if self.gif:
            self.gif.validate()
        if self.segment:
            self.segment.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gif is not None:
            result['Gif'] = self.gif.to_map()

        if self.segment is not None:
            result['Segment'] = self.segment.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gif') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfigGif()
            self.gif = temp_model.from_map(m.get('Gif'))

        if m.get('Segment') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfigSegment(DaraModel):
    def __init__(
        self,
        duration: str = None,
    ):
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateMuxConfigGif(DaraModel):
    def __init__(
        self,
        final_delay: str = None,
        loop: str = None,
    ):
        self.final_delay = final_delay
        self.loop = loop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.final_delay is not None:
            result['FinalDelay'] = self.final_delay

        if self.loop is not None:
            result['Loop'] = self.loop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinalDelay') is not None:
            self.final_delay = m.get('FinalDelay')

        if m.get('Loop') is not None:
            self.loop = m.get('Loop')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateContainer(DaraModel):
    def __init__(
        self,
        format: str = None,
    ):
        self.format = format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobTemplateListTemplateAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        qscale: str = None,
        samplerate: str = None,
    ):
        self.bitrate = bitrate
        self.channels = channels
        self.codec = codec
        self.profile = profile
        self.qscale = qscale
        self.samplerate = samplerate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec is not None:
            result['Codec'] = self.codec

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.qscale is not None:
            result['Qscale'] = self.qscale

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Qscale') is not None:
            self.qscale = m.get('Qscale')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobMNSMessageResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        message_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobInputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfig(DaraModel):
    def __init__(
        self,
        properties_control: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigPropertiesControl = None,
        quality_control: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigQualityControl = None,
    ):
        self.properties_control = properties_control
        self.quality_control = quality_control

    def validate(self):
        if self.properties_control:
            self.properties_control.validate()
        if self.quality_control:
            self.quality_control.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.properties_control is not None:
            result['PropertiesControl'] = self.properties_control.to_map()

        if self.quality_control is not None:
            result['QualityControl'] = self.quality_control.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertiesControl') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigPropertiesControl()
            self.properties_control = temp_model.from_map(m.get('PropertiesControl'))

        if m.get('QualityControl') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigQualityControl()
            self.quality_control = temp_model.from_map(m.get('QualityControl'))

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigQualityControl(DaraModel):
    def __init__(
        self,
        method_streaming: str = None,
        rate_quality: str = None,
    ):
        self.method_streaming = method_streaming
        self.rate_quality = rate_quality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.method_streaming is not None:
            result['MethodStreaming'] = self.method_streaming

        if self.rate_quality is not None:
            result['RateQuality'] = self.rate_quality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MethodStreaming') is not None:
            self.method_streaming = m.get('MethodStreaming')

        if m.get('RateQuality') is not None:
            self.rate_quality = m.get('RateQuality')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigPropertiesControl(DaraModel):
    def __init__(
        self,
        crop: main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigPropertiesControlCrop = None,
        deinterlace: str = None,
    ):
        self.crop = crop
        self.deinterlace = deinterlace

    def validate(self):
        if self.crop:
            self.crop.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crop is not None:
            result['Crop'] = self.crop.to_map()

        if self.deinterlace is not None:
            result['Deinterlace'] = self.deinterlace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Crop') is not None:
            temp_model = main_models.QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigPropertiesControlCrop()
            self.crop = temp_model.from_map(m.get('Crop'))

        if m.get('Deinterlace') is not None:
            self.deinterlace = m.get('Deinterlace')

        return self

class QueryAnalysisJobListResponseBodyAnalysisJobListAnalysisJobAnalysisConfigPropertiesControlCrop(DaraModel):
    def __init__(
        self,
        height: str = None,
        left: str = None,
        mode: str = None,
        top: str = None,
        width: str = None,
    ):
        self.height = height
        self.left = left
        self.mode = mode
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.left is not None:
            result['Left'] = self.left

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.top is not None:
            result['Top'] = self.top

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Left') is not None:
            self.left = m.get('Left')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

