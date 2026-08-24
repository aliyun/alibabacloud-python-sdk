# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class CreateDocParserJobAdvanceRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        asr_language: str = None,
        audio_clip_output: bool = None,
        audio_window_seconds: int = None,
        chunk_summary: bool = None,
        file_format: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        frame_output: bool = None,
        global_summary: bool = None,
        image_mode: str = None,
        image_understanding: str = None,
        media_chunk_interval_seconds: int = None,
        media_chunk_strategy: str = None,
        media_frames_per_minute: float = None,
        media_max_frame_budget: int = None,
        media_min_frame_budget: int = None,
        oss_file_url: str = None,
        output_format: str = None,
        parse_scene: str = None,
        region_id: str = None,
        response_mode: str = None,
        result_type: str = None,
        table_format: str = None,
    ):
        # The agent name.
        self.agent_name = agent_name
        # The language type for speech recognition.
        self.asr_language = asr_language
        # The audio clip output.
        self.audio_clip_output = audio_clip_output
        # The audio window duration in seconds.
        self.audio_window_seconds = audio_window_seconds
        # The chunk summary information.
        self.chunk_summary = chunk_summary
        # The format of the input file. Valid values:
        # 
        # - **pdf**: PDF file.
        # 
        # - **docx**: Word file in docx format.
        # 
        # - **doc**: Word file in doc format.
        # 
        # - **pptx**: PPT file in pptx format.
        # 
        # - **ppt**: PPT file in ppt format.
        # 
        # - **txt**: Plain text file.
        # 
        # - **md**: Markdown file.
        # 
        # - **png**: PNG image.
        # 
        # - **jpg**: JPG image.
        # 
        # - **jpeg**: JPEG image.
        # 
        # This parameter is required.
        self.file_format = file_format
        # The file name, which must include the file name extension.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The HTTP or HTTPS URL of the file to be parsed.
        # >SDKs for various programming languages additionally provide a `CreateDocParserJobAdvance` method that supports passing a local file stream directly (such as Java InputStream), without the need to upload the file to OSS and construct a FileUrl in advance. When using the Advance method, replace the `FileUrl` parameter (URL string) with the `FileUrlObject` parameter (file stream). All other request parameters remain unchanged. The SDK automatically performs the following operations:
        # >1. Obtains temporary OSS upload credentials.
        # >2. Uploads the file stream directly to OSS.
        # >3. Calls the CreateDocParserJob operation using the generated OSS URL.
        self.file_url_object = file_url_object
        # The frame output result.
        self.frame_output = frame_output
        # The global summary information.
        self.global_summary = global_summary
        # The image processing format.
        self.image_mode = image_mode
        # The image understanding and analysis setting.
        self.image_understanding = image_understanding
        # The media chunk interval in seconds.
        self.media_chunk_interval_seconds = media_chunk_interval_seconds
        # The media chunk strategy.
        self.media_chunk_strategy = media_chunk_strategy
        # The number of media frames per minute.
        self.media_frames_per_minute = media_frames_per_minute
        # The maximum frame budget for media.
        self.media_max_frame_budget = media_max_frame_budget
        # The minimum frame budget for media.
        self.media_min_frame_budget = media_min_frame_budget
        # The OSS file URL.
        self.oss_file_url = oss_file_url
        # The output format of the parsing result. Valid values:
        # 
        # - **markdown**: Markdown format.
        # 
        # This parameter is required.
        self.output_format = output_format
        # The parsing scene.
        self.parse_scene = parse_scene
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The response mode.
        self.response_mode = response_mode
        # The result type.
        self.result_type = result_type
        # The table processing format.
        self.table_format = table_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.asr_language is not None:
            result['AsrLanguage'] = self.asr_language

        if self.audio_clip_output is not None:
            result['AudioClipOutput'] = self.audio_clip_output

        if self.audio_window_seconds is not None:
            result['AudioWindowSeconds'] = self.audio_window_seconds

        if self.chunk_summary is not None:
            result['ChunkSummary'] = self.chunk_summary

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object

        if self.frame_output is not None:
            result['FrameOutput'] = self.frame_output

        if self.global_summary is not None:
            result['GlobalSummary'] = self.global_summary

        if self.image_mode is not None:
            result['ImageMode'] = self.image_mode

        if self.image_understanding is not None:
            result['ImageUnderstanding'] = self.image_understanding

        if self.media_chunk_interval_seconds is not None:
            result['MediaChunkIntervalSeconds'] = self.media_chunk_interval_seconds

        if self.media_chunk_strategy is not None:
            result['MediaChunkStrategy'] = self.media_chunk_strategy

        if self.media_frames_per_minute is not None:
            result['MediaFramesPerMinute'] = self.media_frames_per_minute

        if self.media_max_frame_budget is not None:
            result['MediaMaxFrameBudget'] = self.media_max_frame_budget

        if self.media_min_frame_budget is not None:
            result['MediaMinFrameBudget'] = self.media_min_frame_budget

        if self.oss_file_url is not None:
            result['OssFileUrl'] = self.oss_file_url

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.parse_scene is not None:
            result['ParseScene'] = self.parse_scene

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.response_mode is not None:
            result['ResponseMode'] = self.response_mode

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.table_format is not None:
            result['TableFormat'] = self.table_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('AsrLanguage') is not None:
            self.asr_language = m.get('AsrLanguage')

        if m.get('AudioClipOutput') is not None:
            self.audio_clip_output = m.get('AudioClipOutput')

        if m.get('AudioWindowSeconds') is not None:
            self.audio_window_seconds = m.get('AudioWindowSeconds')

        if m.get('ChunkSummary') is not None:
            self.chunk_summary = m.get('ChunkSummary')

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url_object = m.get('FileUrl')

        if m.get('FrameOutput') is not None:
            self.frame_output = m.get('FrameOutput')

        if m.get('GlobalSummary') is not None:
            self.global_summary = m.get('GlobalSummary')

        if m.get('ImageMode') is not None:
            self.image_mode = m.get('ImageMode')

        if m.get('ImageUnderstanding') is not None:
            self.image_understanding = m.get('ImageUnderstanding')

        if m.get('MediaChunkIntervalSeconds') is not None:
            self.media_chunk_interval_seconds = m.get('MediaChunkIntervalSeconds')

        if m.get('MediaChunkStrategy') is not None:
            self.media_chunk_strategy = m.get('MediaChunkStrategy')

        if m.get('MediaFramesPerMinute') is not None:
            self.media_frames_per_minute = m.get('MediaFramesPerMinute')

        if m.get('MediaMaxFrameBudget') is not None:
            self.media_max_frame_budget = m.get('MediaMaxFrameBudget')

        if m.get('MediaMinFrameBudget') is not None:
            self.media_min_frame_budget = m.get('MediaMinFrameBudget')

        if m.get('OssFileUrl') is not None:
            self.oss_file_url = m.get('OssFileUrl')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('ParseScene') is not None:
            self.parse_scene = m.get('ParseScene')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResponseMode') is not None:
            self.response_mode = m.get('ResponseMode')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('TableFormat') is not None:
            self.table_format = m.get('TableFormat')

        return self

