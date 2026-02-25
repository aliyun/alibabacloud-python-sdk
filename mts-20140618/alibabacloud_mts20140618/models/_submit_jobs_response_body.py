# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class SubmitJobsResponseBody(DaraModel):
    def __init__(
        self,
        job_result_list: main_models.SubmitJobsResponseBodyJobResultList = None,
        request_id: str = None,
    ):
        self.job_result_list = job_result_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job_result_list:
            self.job_result_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_result_list is not None:
            result['JobResultList'] = self.job_result_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobResultList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultList()
            self.job_result_list = temp_model.from_map(m.get('JobResultList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SubmitJobsResponseBodyJobResultList(DaraModel):
    def __init__(
        self,
        job_result: List[main_models.SubmitJobsResponseBodyJobResultListJobResult] = None,
    ):
        self.job_result = job_result

    def validate(self):
        if self.job_result:
            for v1 in self.job_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobResult'] = []
        if self.job_result is not None:
            for k1 in self.job_result:
                result['JobResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_result = []
        if m.get('JobResult') is not None:
            for k1 in m.get('JobResult'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResult()
                self.job_result.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        job: main_models.SubmitJobsResponseBodyJobResultListJobResultJob = None,
        message: str = None,
        success: bool = None,
    ):
        self.code = code
        self.job = job
        self.message = message
        self.success = success

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.job is not None:
            result['Job'] = self.job.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Job') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        creation_time: str = None,
        finish_time: str = None,
        input: main_models.SubmitJobsResponseBodyJobResultListJobResultJobInput = None,
        job_id: str = None,
        mnsmessage_result: main_models.SubmitJobsResponseBodyJobResultListJobResultJobMNSMessageResult = None,
        message: str = None,
        output: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutput = None,
        percent: int = None,
        pipeline_id: str = None,
        state: str = None,
    ):
        self.code = code
        self.creation_time = creation_time
        self.finish_time = finish_time
        self.input = input
        self.job_id = job_id
        self.mnsmessage_result = mnsmessage_result
        self.message = message
        self.output = output
        self.percent = percent
        self.pipeline_id = pipeline_id
        self.state = state

    def validate(self):
        if self.input:
            self.input.validate()
        if self.mnsmessage_result:
            self.mnsmessage_result.validate()
        if self.output:
            self.output.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.mnsmessage_result is not None:
            result['MNSMessageResult'] = self.mnsmessage_result.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Input') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MNSMessageResult') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobMNSMessageResult()
            self.mnsmessage_result = temp_model.from_map(m.get('MNSMessageResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Output') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutput(DaraModel):
    def __init__(
        self,
        amix_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputAmixList = None,
        audio: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputAudio = None,
        audio_stream_map: str = None,
        clip: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputClip = None,
        container: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputContainer = None,
        de_watermark: str = None,
        digi_water_mark: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputDigiWaterMark = None,
        encryption: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputEncryption = None,
        m_3u8non_standard_support: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputM3U8NonStandardSupport = None,
        merge_config_url: str = None,
        merge_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMergeList = None,
        mux_config: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfig = None,
        opening_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOpeningList = None,
        out_subtitle_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleList = None,
        output_file: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOutputFile = None,
        priority: str = None,
        properties: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputProperties = None,
        rotate: str = None,
        subtitle_config: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfig = None,
        super_reso: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSuperReso = None,
        tail_slate_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputTailSlateList = None,
        template_id: str = None,
        trans_config: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputTransConfig = None,
        user_data: str = None,
        video: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputVideo = None,
        video_stream_map: str = None,
        water_mark_config_url: str = None,
        water_mark_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkList = None,
    ):
        self.amix_list = amix_list
        self.audio = audio
        self.audio_stream_map = audio_stream_map
        self.clip = clip
        self.container = container
        self.de_watermark = de_watermark
        self.digi_water_mark = digi_water_mark
        self.encryption = encryption
        self.m_3u8non_standard_support = m_3u8non_standard_support
        self.merge_config_url = merge_config_url
        self.merge_list = merge_list
        self.mux_config = mux_config
        self.opening_list = opening_list
        self.out_subtitle_list = out_subtitle_list
        self.output_file = output_file
        self.priority = priority
        self.properties = properties
        self.rotate = rotate
        self.subtitle_config = subtitle_config
        self.super_reso = super_reso
        self.tail_slate_list = tail_slate_list
        self.template_id = template_id
        self.trans_config = trans_config
        self.user_data = user_data
        self.video = video
        self.video_stream_map = video_stream_map
        self.water_mark_config_url = water_mark_config_url
        self.water_mark_list = water_mark_list

    def validate(self):
        if self.amix_list:
            self.amix_list.validate()
        if self.audio:
            self.audio.validate()
        if self.clip:
            self.clip.validate()
        if self.container:
            self.container.validate()
        if self.digi_water_mark:
            self.digi_water_mark.validate()
        if self.encryption:
            self.encryption.validate()
        if self.m_3u8non_standard_support:
            self.m_3u8non_standard_support.validate()
        if self.merge_list:
            self.merge_list.validate()
        if self.mux_config:
            self.mux_config.validate()
        if self.opening_list:
            self.opening_list.validate()
        if self.out_subtitle_list:
            self.out_subtitle_list.validate()
        if self.output_file:
            self.output_file.validate()
        if self.properties:
            self.properties.validate()
        if self.subtitle_config:
            self.subtitle_config.validate()
        if self.super_reso:
            self.super_reso.validate()
        if self.tail_slate_list:
            self.tail_slate_list.validate()
        if self.trans_config:
            self.trans_config.validate()
        if self.video:
            self.video.validate()
        if self.water_mark_list:
            self.water_mark_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amix_list is not None:
            result['AmixList'] = self.amix_list.to_map()

        if self.audio is not None:
            result['Audio'] = self.audio.to_map()

        if self.audio_stream_map is not None:
            result['AudioStreamMap'] = self.audio_stream_map

        if self.clip is not None:
            result['Clip'] = self.clip.to_map()

        if self.container is not None:
            result['Container'] = self.container.to_map()

        if self.de_watermark is not None:
            result['DeWatermark'] = self.de_watermark

        if self.digi_water_mark is not None:
            result['DigiWaterMark'] = self.digi_water_mark.to_map()

        if self.encryption is not None:
            result['Encryption'] = self.encryption.to_map()

        if self.m_3u8non_standard_support is not None:
            result['M3U8NonStandardSupport'] = self.m_3u8non_standard_support.to_map()

        if self.merge_config_url is not None:
            result['MergeConfigUrl'] = self.merge_config_url

        if self.merge_list is not None:
            result['MergeList'] = self.merge_list.to_map()

        if self.mux_config is not None:
            result['MuxConfig'] = self.mux_config.to_map()

        if self.opening_list is not None:
            result['OpeningList'] = self.opening_list.to_map()

        if self.out_subtitle_list is not None:
            result['OutSubtitleList'] = self.out_subtitle_list.to_map()

        if self.output_file is not None:
            result['OutputFile'] = self.output_file.to_map()

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.subtitle_config is not None:
            result['SubtitleConfig'] = self.subtitle_config.to_map()

        if self.super_reso is not None:
            result['SuperReso'] = self.super_reso.to_map()

        if self.tail_slate_list is not None:
            result['TailSlateList'] = self.tail_slate_list.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.trans_config is not None:
            result['TransConfig'] = self.trans_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video is not None:
            result['Video'] = self.video.to_map()

        if self.video_stream_map is not None:
            result['VideoStreamMap'] = self.video_stream_map

        if self.water_mark_config_url is not None:
            result['WaterMarkConfigUrl'] = self.water_mark_config_url

        if self.water_mark_list is not None:
            result['WaterMarkList'] = self.water_mark_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmixList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputAmixList()
            self.amix_list = temp_model.from_map(m.get('AmixList'))

        if m.get('Audio') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('AudioStreamMap') is not None:
            self.audio_stream_map = m.get('AudioStreamMap')

        if m.get('Clip') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputClip()
            self.clip = temp_model.from_map(m.get('Clip'))

        if m.get('Container') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('DeWatermark') is not None:
            self.de_watermark = m.get('DeWatermark')

        if m.get('DigiWaterMark') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputDigiWaterMark()
            self.digi_water_mark = temp_model.from_map(m.get('DigiWaterMark'))

        if m.get('Encryption') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputEncryption()
            self.encryption = temp_model.from_map(m.get('Encryption'))

        if m.get('M3U8NonStandardSupport') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputM3U8NonStandardSupport()
            self.m_3u8non_standard_support = temp_model.from_map(m.get('M3U8NonStandardSupport'))

        if m.get('MergeConfigUrl') is not None:
            self.merge_config_url = m.get('MergeConfigUrl')

        if m.get('MergeList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMergeList()
            self.merge_list = temp_model.from_map(m.get('MergeList'))

        if m.get('MuxConfig') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfig()
            self.mux_config = temp_model.from_map(m.get('MuxConfig'))

        if m.get('OpeningList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOpeningList()
            self.opening_list = temp_model.from_map(m.get('OpeningList'))

        if m.get('OutSubtitleList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleList()
            self.out_subtitle_list = temp_model.from_map(m.get('OutSubtitleList'))

        if m.get('OutputFile') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOutputFile()
            self.output_file = temp_model.from_map(m.get('OutputFile'))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Properties') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('SubtitleConfig') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfig()
            self.subtitle_config = temp_model.from_map(m.get('SubtitleConfig'))

        if m.get('SuperReso') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSuperReso()
            self.super_reso = temp_model.from_map(m.get('SuperReso'))

        if m.get('TailSlateList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputTailSlateList()
            self.tail_slate_list = temp_model.from_map(m.get('TailSlateList'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TransConfig') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputTransConfig()
            self.trans_config = temp_model.from_map(m.get('TransConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('Video') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputVideo()
            self.video = temp_model.from_map(m.get('Video'))

        if m.get('VideoStreamMap') is not None:
            self.video_stream_map = m.get('VideoStreamMap')

        if m.get('WaterMarkConfigUrl') is not None:
            self.water_mark_config_url = m.get('WaterMarkConfigUrl')

        if m.get('WaterMarkList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkList()
            self.water_mark_list = temp_model.from_map(m.get('WaterMarkList'))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkList(DaraModel):
    def __init__(
        self,
        water_mark: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkListWaterMark] = None,
    ):
        self.water_mark = water_mark

    def validate(self):
        if self.water_mark:
            for v1 in self.water_mark:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WaterMark'] = []
        if self.water_mark is not None:
            for k1 in self.water_mark:
                result['WaterMark'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.water_mark = []
        if m.get('WaterMark') is not None:
            for k1 in m.get('WaterMark'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkListWaterMark()
                self.water_mark.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkListWaterMark(DaraModel):
    def __init__(
        self,
        dx: str = None,
        dy: str = None,
        height: str = None,
        input_file: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkListWaterMarkInputFile = None,
        refer_pos: str = None,
        type: str = None,
        water_mark_template_id: str = None,
        width: str = None,
    ):
        self.dx = dx
        self.dy = dy
        self.height = height
        self.input_file = input_file
        self.refer_pos = refer_pos
        self.type = type
        self.water_mark_template_id = water_mark_template_id
        self.width = width

    def validate(self):
        if self.input_file:
            self.input_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dx is not None:
            result['Dx'] = self.dx

        if self.dy is not None:
            result['Dy'] = self.dy

        if self.height is not None:
            result['Height'] = self.height

        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.refer_pos is not None:
            result['ReferPos'] = self.refer_pos

        if self.type is not None:
            result['Type'] = self.type

        if self.water_mark_template_id is not None:
            result['WaterMarkTemplateId'] = self.water_mark_template_id

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dx') is not None:
            self.dx = m.get('Dx')

        if m.get('Dy') is not None:
            self.dy = m.get('Dy')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('InputFile') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkListWaterMarkInputFile()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('ReferPos') is not None:
            self.refer_pos = m.get('ReferPos')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WaterMarkTemplateId') is not None:
            self.water_mark_template_id = m.get('WaterMarkTemplateId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputWaterMarkListWaterMarkInputFile(DaraModel):
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

class SubmitJobsResponseBodyJobResultListJobResultJobOutputVideo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        bitrate_bnd: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputVideoBitrateBnd = None,
        bufsize: str = None,
        codec: str = None,
        crf: str = None,
        crop: str = None,
        degrain: str = None,
        fps: str = None,
        gop: str = None,
        height: str = None,
        max_fps: str = None,
        maxrate: str = None,
        pad: str = None,
        pix_fmt: str = None,
        preset: str = None,
        profile: str = None,
        qscale: str = None,
        reso_priority: str = None,
        scan_mode: str = None,
        width: str = None,
    ):
        self.bitrate = bitrate
        self.bitrate_bnd = bitrate_bnd
        self.bufsize = bufsize
        self.codec = codec
        self.crf = crf
        self.crop = crop
        self.degrain = degrain
        self.fps = fps
        self.gop = gop
        self.height = height
        self.max_fps = max_fps
        self.maxrate = maxrate
        self.pad = pad
        self.pix_fmt = pix_fmt
        self.preset = preset
        self.profile = profile
        self.qscale = qscale
        self.reso_priority = reso_priority
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

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.degrain is not None:
            result['Degrain'] = self.degrain

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.gop is not None:
            result['Gop'] = self.gop

        if self.height is not None:
            result['Height'] = self.height

        if self.max_fps is not None:
            result['MaxFps'] = self.max_fps

        if self.maxrate is not None:
            result['Maxrate'] = self.maxrate

        if self.pad is not None:
            result['Pad'] = self.pad

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.preset is not None:
            result['Preset'] = self.preset

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.qscale is not None:
            result['Qscale'] = self.qscale

        if self.reso_priority is not None:
            result['ResoPriority'] = self.reso_priority

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
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputVideoBitrateBnd()
            self.bitrate_bnd = temp_model.from_map(m.get('BitrateBnd'))

        if m.get('Bufsize') is not None:
            self.bufsize = m.get('Bufsize')

        if m.get('Codec') is not None:
            self.codec = m.get('Codec')

        if m.get('Crf') is not None:
            self.crf = m.get('Crf')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('Degrain') is not None:
            self.degrain = m.get('Degrain')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Gop') is not None:
            self.gop = m.get('Gop')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MaxFps') is not None:
            self.max_fps = m.get('MaxFps')

        if m.get('Maxrate') is not None:
            self.maxrate = m.get('Maxrate')

        if m.get('Pad') is not None:
            self.pad = m.get('Pad')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Preset') is not None:
            self.preset = m.get('Preset')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Qscale') is not None:
            self.qscale = m.get('Qscale')

        if m.get('ResoPriority') is not None:
            self.reso_priority = m.get('ResoPriority')

        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputVideoBitrateBnd(DaraModel):
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

class SubmitJobsResponseBodyJobResultListJobResultJobOutputTransConfig(DaraModel):
    def __init__(
        self,
        adj_dar_method: str = None,
        is_check_audio_bitrate: str = None,
        is_check_audio_bitrate_fail: str = None,
        is_check_reso: str = None,
        is_check_reso_fail: str = None,
        is_check_video_bitrate: str = None,
        is_check_video_bitrate_fail: str = None,
        trans_mode: str = None,
    ):
        self.adj_dar_method = adj_dar_method
        self.is_check_audio_bitrate = is_check_audio_bitrate
        self.is_check_audio_bitrate_fail = is_check_audio_bitrate_fail
        self.is_check_reso = is_check_reso
        self.is_check_reso_fail = is_check_reso_fail
        self.is_check_video_bitrate = is_check_video_bitrate
        self.is_check_video_bitrate_fail = is_check_video_bitrate_fail
        self.trans_mode = trans_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adj_dar_method is not None:
            result['AdjDarMethod'] = self.adj_dar_method

        if self.is_check_audio_bitrate is not None:
            result['IsCheckAudioBitrate'] = self.is_check_audio_bitrate

        if self.is_check_audio_bitrate_fail is not None:
            result['IsCheckAudioBitrateFail'] = self.is_check_audio_bitrate_fail

        if self.is_check_reso is not None:
            result['IsCheckReso'] = self.is_check_reso

        if self.is_check_reso_fail is not None:
            result['IsCheckResoFail'] = self.is_check_reso_fail

        if self.is_check_video_bitrate is not None:
            result['IsCheckVideoBitrate'] = self.is_check_video_bitrate

        if self.is_check_video_bitrate_fail is not None:
            result['IsCheckVideoBitrateFail'] = self.is_check_video_bitrate_fail

        if self.trans_mode is not None:
            result['TransMode'] = self.trans_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjDarMethod') is not None:
            self.adj_dar_method = m.get('AdjDarMethod')

        if m.get('IsCheckAudioBitrate') is not None:
            self.is_check_audio_bitrate = m.get('IsCheckAudioBitrate')

        if m.get('IsCheckAudioBitrateFail') is not None:
            self.is_check_audio_bitrate_fail = m.get('IsCheckAudioBitrateFail')

        if m.get('IsCheckReso') is not None:
            self.is_check_reso = m.get('IsCheckReso')

        if m.get('IsCheckResoFail') is not None:
            self.is_check_reso_fail = m.get('IsCheckResoFail')

        if m.get('IsCheckVideoBitrate') is not None:
            self.is_check_video_bitrate = m.get('IsCheckVideoBitrate')

        if m.get('IsCheckVideoBitrateFail') is not None:
            self.is_check_video_bitrate_fail = m.get('IsCheckVideoBitrateFail')

        if m.get('TransMode') is not None:
            self.trans_mode = m.get('TransMode')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputTailSlateList(DaraModel):
    def __init__(
        self,
        tail_slate: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputTailSlateListTailSlate] = None,
    ):
        self.tail_slate = tail_slate

    def validate(self):
        if self.tail_slate:
            for v1 in self.tail_slate:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TailSlate'] = []
        if self.tail_slate is not None:
            for k1 in self.tail_slate:
                result['TailSlate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tail_slate = []
        if m.get('TailSlate') is not None:
            for k1 in m.get('TailSlate'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputTailSlateListTailSlate()
                self.tail_slate.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputTailSlateListTailSlate(DaraModel):
    def __init__(
        self,
        bg_color: str = None,
        blend_duration: str = None,
        height: str = None,
        is_merge_audio: bool = None,
        start: str = None,
        tail_url: str = None,
        width: str = None,
    ):
        self.bg_color = bg_color
        self.blend_duration = blend_duration
        self.height = height
        self.is_merge_audio = is_merge_audio
        self.start = start
        self.tail_url = tail_url
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bg_color is not None:
            result['BgColor'] = self.bg_color

        if self.blend_duration is not None:
            result['BlendDuration'] = self.blend_duration

        if self.height is not None:
            result['Height'] = self.height

        if self.is_merge_audio is not None:
            result['IsMergeAudio'] = self.is_merge_audio

        if self.start is not None:
            result['Start'] = self.start

        if self.tail_url is not None:
            result['TailUrl'] = self.tail_url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BgColor') is not None:
            self.bg_color = m.get('BgColor')

        if m.get('BlendDuration') is not None:
            self.blend_duration = m.get('BlendDuration')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('IsMergeAudio') is not None:
            self.is_merge_audio = m.get('IsMergeAudio')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('TailUrl') is not None:
            self.tail_url = m.get('TailUrl')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputSuperReso(DaraModel):
    def __init__(
        self,
        is_half_sample: str = None,
    ):
        self.is_half_sample = is_half_sample

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_half_sample is not None:
            result['IsHalfSample'] = self.is_half_sample

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsHalfSample') is not None:
            self.is_half_sample = m.get('IsHalfSample')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfig(DaraModel):
    def __init__(
        self,
        ext_subtitle_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleList = None,
        subtitle_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigSubtitleList = None,
    ):
        self.ext_subtitle_list = ext_subtitle_list
        self.subtitle_list = subtitle_list

    def validate(self):
        if self.ext_subtitle_list:
            self.ext_subtitle_list.validate()
        if self.subtitle_list:
            self.subtitle_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_subtitle_list is not None:
            result['ExtSubtitleList'] = self.ext_subtitle_list.to_map()

        if self.subtitle_list is not None:
            result['SubtitleList'] = self.subtitle_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtSubtitleList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleList()
            self.ext_subtitle_list = temp_model.from_map(m.get('ExtSubtitleList'))

        if m.get('SubtitleList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigSubtitleList()
            self.subtitle_list = temp_model.from_map(m.get('SubtitleList'))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigSubtitleList(DaraModel):
    def __init__(
        self,
        subtitle: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigSubtitleListSubtitle] = None,
    ):
        self.subtitle = subtitle

    def validate(self):
        if self.subtitle:
            for v1 in self.subtitle:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Subtitle'] = []
        if self.subtitle is not None:
            for k1 in self.subtitle:
                result['Subtitle'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subtitle = []
        if m.get('Subtitle') is not None:
            for k1 in m.get('Subtitle'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigSubtitleListSubtitle()
                self.subtitle.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigSubtitleListSubtitle(DaraModel):
    def __init__(
        self,
        map: str = None,
    ):
        self.map = map

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.map is not None:
            result['Map'] = self.map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Map') is not None:
            self.map = m.get('Map')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleList(DaraModel):
    def __init__(
        self,
        ext_subtitle: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleListExtSubtitle] = None,
    ):
        self.ext_subtitle = ext_subtitle

    def validate(self):
        if self.ext_subtitle:
            for v1 in self.ext_subtitle:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExtSubtitle'] = []
        if self.ext_subtitle is not None:
            for k1 in self.ext_subtitle:
                result['ExtSubtitle'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ext_subtitle = []
        if m.get('ExtSubtitle') is not None:
            for k1 in m.get('ExtSubtitle'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleListExtSubtitle()
                self.ext_subtitle.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleListExtSubtitle(DaraModel):
    def __init__(
        self,
        char_enc: str = None,
        font_name: str = None,
        input: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleListExtSubtitleInput = None,
    ):
        self.char_enc = char_enc
        self.font_name = font_name
        self.input = input

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.char_enc is not None:
            result['CharEnc'] = self.char_enc

        if self.font_name is not None:
            result['FontName'] = self.font_name

        if self.input is not None:
            result['Input'] = self.input.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharEnc') is not None:
            self.char_enc = m.get('CharEnc')

        if m.get('FontName') is not None:
            self.font_name = m.get('FontName')

        if m.get('Input') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleListExtSubtitleInput()
            self.input = temp_model.from_map(m.get('Input'))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputSubtitleConfigExtSubtitleListExtSubtitleInput(DaraModel):
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

class SubmitJobsResponseBodyJobResultListJobResultJobOutputProperties(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        duration: str = None,
        file_format: str = None,
        file_size: str = None,
        format: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesFormat = None,
        fps: str = None,
        height: str = None,
        streams: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreams = None,
        width: str = None,
    ):
        self.bitrate = bitrate
        self.duration = duration
        self.file_format = file_format
        self.file_size = file_size
        self.format = format
        self.fps = fps
        self.height = height
        self.streams = streams
        self.width = width

    def validate(self):
        if self.format:
            self.format.validate()
        if self.streams:
            self.streams.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.format is not None:
            result['Format'] = self.format.to_map()

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.streams is not None:
            result['Streams'] = self.streams.to_map()

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Format') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesFormat()
            self.format = temp_model.from_map(m.get('Format'))

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Streams') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreams()
            self.streams = temp_model.from_map(m.get('Streams'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreams(DaraModel):
    def __init__(
        self,
        audio_stream_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsAudioStreamList = None,
        subtitle_stream_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsSubtitleStreamList = None,
        video_stream_list: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamList = None,
    ):
        self.audio_stream_list = audio_stream_list
        self.subtitle_stream_list = subtitle_stream_list
        self.video_stream_list = video_stream_list

    def validate(self):
        if self.audio_stream_list:
            self.audio_stream_list.validate()
        if self.subtitle_stream_list:
            self.subtitle_stream_list.validate()
        if self.video_stream_list:
            self.video_stream_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_stream_list is not None:
            result['AudioStreamList'] = self.audio_stream_list.to_map()

        if self.subtitle_stream_list is not None:
            result['SubtitleStreamList'] = self.subtitle_stream_list.to_map()

        if self.video_stream_list is not None:
            result['VideoStreamList'] = self.video_stream_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioStreamList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsAudioStreamList()
            self.audio_stream_list = temp_model.from_map(m.get('AudioStreamList'))

        if m.get('SubtitleStreamList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsSubtitleStreamList()
            self.subtitle_stream_list = temp_model.from_map(m.get('SubtitleStreamList'))

        if m.get('VideoStreamList') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamList()
            self.video_stream_list = temp_model.from_map(m.get('VideoStreamList'))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamList(DaraModel):
    def __init__(
        self,
        video_stream: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamListVideoStream] = None,
    ):
        self.video_stream = video_stream

    def validate(self):
        if self.video_stream:
            for v1 in self.video_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoStream'] = []
        if self.video_stream is not None:
            for k1 in self.video_stream:
                result['VideoStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_stream = []
        if m.get('VideoStream') is not None:
            for k1 in m.get('VideoStream'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamListVideoStream()
                self.video_stream.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamListVideoStream(DaraModel):
    def __init__(
        self,
        avg_fps: str = None,
        bitrate: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        dar: str = None,
        duration: str = None,
        fps: str = None,
        has_bframes: str = None,
        height: str = None,
        index: str = None,
        lang: str = None,
        level: str = None,
        network_cost: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamListVideoStreamNetworkCost = None,
        num_frames: str = None,
        pix_fmt: str = None,
        profile: str = None,
        sar: str = None,
        start_time: str = None,
        timebase: str = None,
        width: str = None,
    ):
        self.avg_fps = avg_fps
        self.bitrate = bitrate
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.dar = dar
        self.duration = duration
        self.fps = fps
        self.has_bframes = has_bframes
        self.height = height
        self.index = index
        self.lang = lang
        self.level = level
        self.network_cost = network_cost
        self.num_frames = num_frames
        self.pix_fmt = pix_fmt
        self.profile = profile
        self.sar = sar
        self.start_time = start_time
        self.timebase = timebase
        self.width = width

    def validate(self):
        if self.network_cost:
            self.network_cost.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.dar is not None:
            result['Dar'] = self.dar

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes

        if self.height is not None:
            result['Height'] = self.height

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.network_cost is not None:
            result['NetworkCost'] = self.network_cost.to_map()

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.sar is not None:
            result['Sar'] = self.sar

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('Dar') is not None:
            self.dar = m.get('Dar')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('NetworkCost') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamListVideoStreamNetworkCost()
            self.network_cost = temp_model.from_map(m.get('NetworkCost'))

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Sar') is not None:
            self.sar = m.get('Sar')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsVideoStreamListVideoStreamNetworkCost(DaraModel):
    def __init__(
        self,
        avg_bitrate: str = None,
        cost_bandwidth: str = None,
        preload_time: str = None,
    ):
        self.avg_bitrate = avg_bitrate
        self.cost_bandwidth = cost_bandwidth
        self.preload_time = preload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_bitrate is not None:
            result['AvgBitrate'] = self.avg_bitrate

        if self.cost_bandwidth is not None:
            result['CostBandwidth'] = self.cost_bandwidth

        if self.preload_time is not None:
            result['PreloadTime'] = self.preload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgBitrate') is not None:
            self.avg_bitrate = m.get('AvgBitrate')

        if m.get('CostBandwidth') is not None:
            self.cost_bandwidth = m.get('CostBandwidth')

        if m.get('PreloadTime') is not None:
            self.preload_time = m.get('PreloadTime')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsSubtitleStreamList(DaraModel):
    def __init__(
        self,
        subtitle_stream: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsSubtitleStreamListSubtitleStream] = None,
    ):
        self.subtitle_stream = subtitle_stream

    def validate(self):
        if self.subtitle_stream:
            for v1 in self.subtitle_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubtitleStream'] = []
        if self.subtitle_stream is not None:
            for k1 in self.subtitle_stream:
                result['SubtitleStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subtitle_stream = []
        if m.get('SubtitleStream') is not None:
            for k1 in m.get('SubtitleStream'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsSubtitleStreamListSubtitleStream()
                self.subtitle_stream.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsSubtitleStreamListSubtitleStream(DaraModel):
    def __init__(
        self,
        index: str = None,
        lang: str = None,
    ):
        self.index = index
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsAudioStreamList(DaraModel):
    def __init__(
        self,
        audio_stream: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsAudioStreamListAudioStream] = None,
    ):
        self.audio_stream = audio_stream

    def validate(self):
        if self.audio_stream:
            for v1 in self.audio_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioStream'] = []
        if self.audio_stream is not None:
            for k1 in self.audio_stream:
                result['AudioStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_stream = []
        if m.get('AudioStream') is not None:
            for k1 in m.get('AudioStream'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsAudioStreamListAudioStream()
                self.audio_stream.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesStreamsAudioStreamListAudioStream(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channel_layout: str = None,
        channels: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: str = None,
        index: str = None,
        lang: str = None,
        num_frames: str = None,
        sample_fmt: str = None,
        samplerate: str = None,
        start_time: str = None,
        timebase: str = None,
    ):
        self.bitrate = bitrate
        self.channel_layout = channel_layout
        self.channels = channels
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.duration = duration
        self.index = index
        self.lang = lang
        self.num_frames = num_frames
        self.sample_fmt = sample_fmt
        self.samplerate = samplerate
        self.start_time = start_time
        self.timebase = timebase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputPropertiesFormat(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        duration: str = None,
        format_long_name: str = None,
        format_name: str = None,
        num_programs: str = None,
        num_streams: str = None,
        size: str = None,
        start_time: str = None,
    ):
        self.bitrate = bitrate
        self.duration = duration
        self.format_long_name = format_long_name
        self.format_name = format_name
        self.num_programs = num_programs
        self.num_streams = num_streams
        self.size = size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name

        if self.format_name is not None:
            result['FormatName'] = self.format_name

        if self.num_programs is not None:
            result['NumPrograms'] = self.num_programs

        if self.num_streams is not None:
            result['NumStreams'] = self.num_streams

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')

        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')

        if m.get('NumPrograms') is not None:
            self.num_programs = m.get('NumPrograms')

        if m.get('NumStreams') is not None:
            self.num_streams = m.get('NumStreams')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputOutputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        role_arn: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object
        self.role_arn = role_arn

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

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleList(DaraModel):
    def __init__(
        self,
        out_subtitle: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleListOutSubtitle] = None,
    ):
        self.out_subtitle = out_subtitle

    def validate(self):
        if self.out_subtitle:
            for v1 in self.out_subtitle:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OutSubtitle'] = []
        if self.out_subtitle is not None:
            for k1 in self.out_subtitle:
                result['OutSubtitle'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.out_subtitle = []
        if m.get('OutSubtitle') is not None:
            for k1 in m.get('OutSubtitle'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleListOutSubtitle()
                self.out_subtitle.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleListOutSubtitle(DaraModel):
    def __init__(
        self,
        map: str = None,
        message: str = None,
        out_subtitle_file: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleListOutSubtitleOutSubtitleFile = None,
        success: bool = None,
    ):
        self.map = map
        self.message = message
        self.out_subtitle_file = out_subtitle_file
        self.success = success

    def validate(self):
        if self.out_subtitle_file:
            self.out_subtitle_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.map is not None:
            result['Map'] = self.map

        if self.message is not None:
            result['Message'] = self.message

        if self.out_subtitle_file is not None:
            result['OutSubtitleFile'] = self.out_subtitle_file.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Map') is not None:
            self.map = m.get('Map')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OutSubtitleFile') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleListOutSubtitleOutSubtitleFile()
            self.out_subtitle_file = temp_model.from_map(m.get('OutSubtitleFile'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputOutSubtitleListOutSubtitleOutSubtitleFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        role_arn: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object
        self.role_arn = role_arn

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

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputOpeningList(DaraModel):
    def __init__(
        self,
        opening: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOpeningListOpening] = None,
    ):
        self.opening = opening

    def validate(self):
        if self.opening:
            for v1 in self.opening:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Opening'] = []
        if self.opening is not None:
            for k1 in self.opening:
                result['Opening'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.opening = []
        if m.get('Opening') is not None:
            for k1 in m.get('Opening'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputOpeningListOpening()
                self.opening.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputOpeningListOpening(DaraModel):
    def __init__(
        self,
        height: str = None,
        start: str = None,
        width: str = None,
        open_url: str = None,
    ):
        self.height = height
        self.start = start
        self.width = width
        self.open_url = open_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.start is not None:
            result['Start'] = self.start

        if self.width is not None:
            result['Width'] = self.width

        if self.open_url is not None:
            result['openUrl'] = self.open_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('openUrl') is not None:
            self.open_url = m.get('openUrl')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfig(DaraModel):
    def __init__(
        self,
        gif: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigGif = None,
        segment: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigSegment = None,
        webp: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigWebp = None,
    ):
        self.gif = gif
        self.segment = segment
        self.webp = webp

    def validate(self):
        if self.gif:
            self.gif.validate()
        if self.segment:
            self.segment.validate()
        if self.webp:
            self.webp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gif is not None:
            result['Gif'] = self.gif.to_map()

        if self.segment is not None:
            result['Segment'] = self.segment.to_map()

        if self.webp is not None:
            result['Webp'] = self.webp.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gif') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigGif()
            self.gif = temp_model.from_map(m.get('Gif'))

        if m.get('Segment') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigSegment()
            self.segment = temp_model.from_map(m.get('Segment'))

        if m.get('Webp') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigWebp()
            self.webp = temp_model.from_map(m.get('Webp'))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigWebp(DaraModel):
    def __init__(
        self,
        loop: str = None,
    ):
        self.loop = loop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.loop is not None:
            result['Loop'] = self.loop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Loop') is not None:
            self.loop = m.get('Loop')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigSegment(DaraModel):
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

class SubmitJobsResponseBodyJobResultListJobResultJobOutputMuxConfigGif(DaraModel):
    def __init__(
        self,
        dither_mode: str = None,
        final_delay: str = None,
        is_custom_palette: str = None,
        loop: str = None,
    ):
        self.dither_mode = dither_mode
        self.final_delay = final_delay
        self.is_custom_palette = is_custom_palette
        self.loop = loop

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dither_mode is not None:
            result['DitherMode'] = self.dither_mode

        if self.final_delay is not None:
            result['FinalDelay'] = self.final_delay

        if self.is_custom_palette is not None:
            result['IsCustomPalette'] = self.is_custom_palette

        if self.loop is not None:
            result['Loop'] = self.loop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DitherMode') is not None:
            self.dither_mode = m.get('DitherMode')

        if m.get('FinalDelay') is not None:
            self.final_delay = m.get('FinalDelay')

        if m.get('IsCustomPalette') is not None:
            self.is_custom_palette = m.get('IsCustomPalette')

        if m.get('Loop') is not None:
            self.loop = m.get('Loop')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputMergeList(DaraModel):
    def __init__(
        self,
        merge: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMergeListMerge] = None,
    ):
        self.merge = merge

    def validate(self):
        if self.merge:
            for v1 in self.merge:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Merge'] = []
        if self.merge is not None:
            for k1 in self.merge:
                result['Merge'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.merge = []
        if m.get('Merge') is not None:
            for k1 in m.get('Merge'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputMergeListMerge()
                self.merge.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputMergeListMerge(DaraModel):
    def __init__(
        self,
        duration: str = None,
        merge_url: str = None,
        role_arn: str = None,
        start: str = None,
    ):
        self.duration = duration
        self.merge_url = merge_url
        self.role_arn = role_arn
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.merge_url is not None:
            result['MergeURL'] = self.merge_url

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MergeURL') is not None:
            self.merge_url = m.get('MergeURL')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputM3U8NonStandardSupport(DaraModel):
    def __init__(
        self,
        ts: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputM3U8NonStandardSupportTS = None,
    ):
        self.ts = ts

    def validate(self):
        if self.ts:
            self.ts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ts is not None:
            result['TS'] = self.ts.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TS') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputM3U8NonStandardSupportTS()
            self.ts = temp_model.from_map(m.get('TS'))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputM3U8NonStandardSupportTS(DaraModel):
    def __init__(
        self,
        md_5support: bool = None,
        size_support: bool = None,
    ):
        self.md_5support = md_5support
        self.size_support = size_support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.md_5support is not None:
            result['Md5Support'] = self.md_5support

        if self.size_support is not None:
            result['SizeSupport'] = self.size_support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Md5Support') is not None:
            self.md_5support = m.get('Md5Support')

        if m.get('SizeSupport') is not None:
            self.size_support = m.get('SizeSupport')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputEncryption(DaraModel):
    def __init__(
        self,
        id: str = None,
        key: str = None,
        key_type: str = None,
        key_uri: str = None,
        skip_cnt: str = None,
        type: str = None,
    ):
        self.id = id
        self.key = key
        self.key_type = key_type
        self.key_uri = key_uri
        self.skip_cnt = skip_cnt
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.key is not None:
            result['Key'] = self.key

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.key_uri is not None:
            result['KeyUri'] = self.key_uri

        if self.skip_cnt is not None:
            result['SkipCnt'] = self.skip_cnt

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('KeyUri') is not None:
            self.key_uri = m.get('KeyUri')

        if m.get('SkipCnt') is not None:
            self.skip_cnt = m.get('SkipCnt')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputDigiWaterMark(DaraModel):
    def __init__(
        self,
        alpha: str = None,
        input_file: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputDigiWaterMarkInputFile = None,
        type: str = None,
    ):
        self.alpha = alpha
        self.input_file = input_file
        self.type = type

    def validate(self):
        if self.input_file:
            self.input_file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alpha is not None:
            result['Alpha'] = self.alpha

        if self.input_file is not None:
            result['InputFile'] = self.input_file.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alpha') is not None:
            self.alpha = m.get('Alpha')

        if m.get('InputFile') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputDigiWaterMarkInputFile()
            self.input_file = temp_model.from_map(m.get('InputFile'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputDigiWaterMarkInputFile(DaraModel):
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

class SubmitJobsResponseBodyJobResultListJobResultJobOutputContainer(DaraModel):
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

class SubmitJobsResponseBodyJobResultListJobResultJobOutputClip(DaraModel):
    def __init__(
        self,
        time_span: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputClipTimeSpan = None,
    ):
        self.time_span = time_span

    def validate(self):
        if self.time_span:
            self.time_span.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_span is not None:
            result['TimeSpan'] = self.time_span.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeSpan') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputClipTimeSpan()
            self.time_span = temp_model.from_map(m.get('TimeSpan'))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputClipTimeSpan(DaraModel):
    def __init__(
        self,
        duration: str = None,
        seek: str = None,
    ):
        self.duration = duration
        self.seek = seek

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.seek is not None:
            result['Seek'] = self.seek

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Seek') is not None:
            self.seek = m.get('Seek')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputAudio(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channels: str = None,
        codec: str = None,
        profile: str = None,
        qscale: str = None,
        samplerate: str = None,
        volume: main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputAudioVolume = None,
    ):
        self.bitrate = bitrate
        self.channels = channels
        self.codec = codec
        self.profile = profile
        self.qscale = qscale
        self.samplerate = samplerate
        self.volume = volume

    def validate(self):
        if self.volume:
            self.volume.validate()

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

        if self.volume is not None:
            result['Volume'] = self.volume.to_map()

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

        if m.get('Volume') is not None:
            temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputAudioVolume()
            self.volume = temp_model.from_map(m.get('Volume'))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputAudioVolume(DaraModel):
    def __init__(
        self,
        level: str = None,
        method: str = None,
    ):
        self.level = level
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.method is not None:
            result['Method'] = self.method

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputAmixList(DaraModel):
    def __init__(
        self,
        amix: List[main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputAmixListAmix] = None,
    ):
        self.amix = amix

    def validate(self):
        if self.amix:
            for v1 in self.amix:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Amix'] = []
        if self.amix is not None:
            for k1 in self.amix:
                result['Amix'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.amix = []
        if m.get('Amix') is not None:
            for k1 in m.get('Amix'):
                temp_model = main_models.SubmitJobsResponseBodyJobResultListJobResultJobOutputAmixListAmix()
                self.amix.append(temp_model.from_map(k1))

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobOutputAmixListAmix(DaraModel):
    def __init__(
        self,
        amix_url: str = None,
        duration: str = None,
        map: str = None,
        mix_dur_mode: str = None,
        start: str = None,
    ):
        self.amix_url = amix_url
        self.duration = duration
        self.map = map
        self.mix_dur_mode = mix_dur_mode
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amix_url is not None:
            result['AmixURL'] = self.amix_url

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.map is not None:
            result['Map'] = self.map

        if self.mix_dur_mode is not None:
            result['MixDurMode'] = self.mix_dur_mode

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AmixURL') is not None:
            self.amix_url = m.get('AmixURL')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Map') is not None:
            self.map = m.get('Map')

        if m.get('MixDurMode') is not None:
            self.mix_dur_mode = m.get('MixDurMode')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class SubmitJobsResponseBodyJobResultListJobResultJobMNSMessageResult(DaraModel):
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

class SubmitJobsResponseBodyJobResultListJobResultJobInput(DaraModel):
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

