# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class RunVideoAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunVideoAnalysisResponseBodyHeader = None,
        payload: main_models.RunVideoAnalysisResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header is not None:
            result['header'] = self.header.to_map()

        if self.payload is not None:
            result['payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('payload') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('payload'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class RunVideoAnalysisResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunVideoAnalysisResponseBodyPayloadOutput = None,
        usage: main_models.RunVideoAnalysisResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['output'] = self.output.to_map()

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('usage') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunVideoAnalysisResponseBodyPayloadUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class RunVideoAnalysisResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        add_dataset_documents_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputAddDatasetDocumentsResult = None,
        result_json_file_url: str = None,
        video_analysis_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResult = None,
        video_calculator_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoCalculatorResult = None,
        video_caption_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResult = None,
        video_generate_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResult = None,
        video_generate_results: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResults] = None,
        video_mind_mapping_generate_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResult = None,
        video_role_recognition_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResult = None,
        video_shot_snapshot_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResult = None,
        video_title_generate_result: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResult = None,
    ):
        self.add_dataset_documents_result = add_dataset_documents_result
        self.result_json_file_url = result_json_file_url
        self.video_analysis_result = video_analysis_result
        self.video_calculator_result = video_calculator_result
        self.video_caption_result = video_caption_result
        self.video_generate_result = video_generate_result
        self.video_generate_results = video_generate_results
        self.video_mind_mapping_generate_result = video_mind_mapping_generate_result
        self.video_role_recognition_result = video_role_recognition_result
        self.video_shot_snapshot_result = video_shot_snapshot_result
        self.video_title_generate_result = video_title_generate_result

    def validate(self):
        if self.add_dataset_documents_result:
            self.add_dataset_documents_result.validate()
        if self.video_analysis_result:
            self.video_analysis_result.validate()
        if self.video_calculator_result:
            self.video_calculator_result.validate()
        if self.video_caption_result:
            self.video_caption_result.validate()
        if self.video_generate_result:
            self.video_generate_result.validate()
        if self.video_generate_results:
            for v1 in self.video_generate_results:
                 if v1:
                    v1.validate()
        if self.video_mind_mapping_generate_result:
            self.video_mind_mapping_generate_result.validate()
        if self.video_role_recognition_result:
            self.video_role_recognition_result.validate()
        if self.video_shot_snapshot_result:
            self.video_shot_snapshot_result.validate()
        if self.video_title_generate_result:
            self.video_title_generate_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_dataset_documents_result is not None:
            result['addDatasetDocumentsResult'] = self.add_dataset_documents_result.to_map()

        if self.result_json_file_url is not None:
            result['resultJsonFileUrl'] = self.result_json_file_url

        if self.video_analysis_result is not None:
            result['videoAnalysisResult'] = self.video_analysis_result.to_map()

        if self.video_calculator_result is not None:
            result['videoCalculatorResult'] = self.video_calculator_result.to_map()

        if self.video_caption_result is not None:
            result['videoCaptionResult'] = self.video_caption_result.to_map()

        if self.video_generate_result is not None:
            result['videoGenerateResult'] = self.video_generate_result.to_map()

        result['videoGenerateResults'] = []
        if self.video_generate_results is not None:
            for k1 in self.video_generate_results:
                result['videoGenerateResults'].append(k1.to_map() if k1 else None)

        if self.video_mind_mapping_generate_result is not None:
            result['videoMindMappingGenerateResult'] = self.video_mind_mapping_generate_result.to_map()

        if self.video_role_recognition_result is not None:
            result['videoRoleRecognitionResult'] = self.video_role_recognition_result.to_map()

        if self.video_shot_snapshot_result is not None:
            result['videoShotSnapshotResult'] = self.video_shot_snapshot_result.to_map()

        if self.video_title_generate_result is not None:
            result['videoTitleGenerateResult'] = self.video_title_generate_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addDatasetDocumentsResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputAddDatasetDocumentsResult()
            self.add_dataset_documents_result = temp_model.from_map(m.get('addDatasetDocumentsResult'))

        if m.get('resultJsonFileUrl') is not None:
            self.result_json_file_url = m.get('resultJsonFileUrl')

        if m.get('videoAnalysisResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResult()
            self.video_analysis_result = temp_model.from_map(m.get('videoAnalysisResult'))

        if m.get('videoCalculatorResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoCalculatorResult()
            self.video_calculator_result = temp_model.from_map(m.get('videoCalculatorResult'))

        if m.get('videoCaptionResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResult()
            self.video_caption_result = temp_model.from_map(m.get('videoCaptionResult'))

        if m.get('videoGenerateResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResult()
            self.video_generate_result = temp_model.from_map(m.get('videoGenerateResult'))

        self.video_generate_results = []
        if m.get('videoGenerateResults') is not None:
            for k1 in m.get('videoGenerateResults'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResults()
                self.video_generate_results.append(temp_model.from_map(k1))

        if m.get('videoMindMappingGenerateResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResult()
            self.video_mind_mapping_generate_result = temp_model.from_map(m.get('videoMindMappingGenerateResult'))

        if m.get('videoRoleRecognitionResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResult()
            self.video_role_recognition_result = temp_model.from_map(m.get('videoRoleRecognitionResult'))

        if m.get('videoShotSnapshotResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResult()
            self.video_shot_snapshot_result = temp_model.from_map(m.get('videoShotSnapshotResult'))

        if m.get('videoTitleGenerateResult') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResult()
            self.video_title_generate_result = temp_model.from_map(m.get('videoTitleGenerateResult'))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        model_id: str = None,
        model_reduce: bool = None,
        text: str = None,
        usage: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResultUsage = None,
    ):
        self.generate_finished = generate_finished
        self.model_id = model_id
        self.model_reduce = model_reduce
        self.text = text
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_reduce is not None:
            result['modelReduce'] = self.model_reduce

        if self.text is not None:
            result['text'] = self.text

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelReduce') is not None:
            self.model_reduce = m.get('modelReduce')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('usage') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResultUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoTitleGenerateResultUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResult(DaraModel):
    def __init__(
        self,
        video_shots: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShots] = None,
    ):
        self.video_shots = video_shots

    def validate(self):
        if self.video_shots:
            for v1 in self.video_shots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['videoShots'] = []
        if self.video_shots is not None:
            for k1 in self.video_shots:
                result['videoShots'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_shots = []
        if m.get('videoShots') is not None:
            for k1 in m.get('videoShots'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShots()
                self.video_shots.append(temp_model.from_map(k1))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShots(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        end_time_format: str = None,
        start_time: int = None,
        start_time_format: str = None,
        video_snapshots: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShotsVideoSnapshots] = None,
    ):
        self.end_time = end_time
        self.end_time_format = end_time_format
        self.start_time = start_time
        self.start_time_format = start_time_format
        self.video_snapshots = video_snapshots

    def validate(self):
        if self.video_snapshots:
            for v1 in self.video_snapshots:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.end_time_format is not None:
            result['endTimeFormat'] = self.end_time_format

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.start_time_format is not None:
            result['startTimeFormat'] = self.start_time_format

        result['videoSnapshots'] = []
        if self.video_snapshots is not None:
            for k1 in self.video_snapshots:
                result['videoSnapshots'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('endTimeFormat') is not None:
            self.end_time_format = m.get('endTimeFormat')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('startTimeFormat') is not None:
            self.start_time_format = m.get('startTimeFormat')

        self.video_snapshots = []
        if m.get('videoSnapshots') is not None:
            for k1 in m.get('videoSnapshots'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShotsVideoSnapshots()
                self.video_snapshots.append(temp_model.from_map(k1))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoShotSnapshotResultVideoShotsVideoSnapshots(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResult(DaraModel):
    def __init__(
        self,
        video_roles: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResultVideoRoles] = None,
    ):
        self.video_roles = video_roles

    def validate(self):
        if self.video_roles:
            for v1 in self.video_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['videoRoles'] = []
        if self.video_roles is not None:
            for k1 in self.video_roles:
                result['videoRoles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_roles = []
        if m.get('videoRoles') is not None:
            for k1 in m.get('videoRoles'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResultVideoRoles()
                self.video_roles.append(temp_model.from_map(k1))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResultVideoRoles(DaraModel):
    def __init__(
        self,
        is_auto_recognition: bool = None,
        ratio: float = None,
        role_info: str = None,
        role_name: str = None,
        time_intervals: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResultVideoRolesTimeIntervals] = None,
    ):
        self.is_auto_recognition = is_auto_recognition
        self.ratio = ratio
        self.role_info = role_info
        self.role_name = role_name
        self.time_intervals = time_intervals

    def validate(self):
        if self.time_intervals:
            for v1 in self.time_intervals:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_auto_recognition is not None:
            result['isAutoRecognition'] = self.is_auto_recognition

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.role_info is not None:
            result['roleInfo'] = self.role_info

        if self.role_name is not None:
            result['roleName'] = self.role_name

        result['timeIntervals'] = []
        if self.time_intervals is not None:
            for k1 in self.time_intervals:
                result['timeIntervals'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isAutoRecognition') is not None:
            self.is_auto_recognition = m.get('isAutoRecognition')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('roleInfo') is not None:
            self.role_info = m.get('roleInfo')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        self.time_intervals = []
        if m.get('timeIntervals') is not None:
            for k1 in m.get('timeIntervals'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResultVideoRolesTimeIntervals()
                self.time_intervals.append(temp_model.from_map(k1))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoRoleRecognitionResultVideoRolesTimeIntervals(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        timestamp: int = None,
        url: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.timestamp = timestamp
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        model_id: str = None,
        model_reduce: bool = None,
        text: str = None,
        usage: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultUsage = None,
        video_mind_mappings: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappings] = None,
    ):
        self.generate_finished = generate_finished
        self.model_id = model_id
        self.model_reduce = model_reduce
        self.text = text
        self.usage = usage
        self.video_mind_mappings = video_mind_mappings

    def validate(self):
        if self.usage:
            self.usage.validate()
        if self.video_mind_mappings:
            for v1 in self.video_mind_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_reduce is not None:
            result['modelReduce'] = self.model_reduce

        if self.text is not None:
            result['text'] = self.text

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        result['videoMindMappings'] = []
        if self.video_mind_mappings is not None:
            for k1 in self.video_mind_mappings:
                result['videoMindMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelReduce') is not None:
            self.model_reduce = m.get('modelReduce')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('usage') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        self.video_mind_mappings = []
        if m.get('videoMindMappings') is not None:
            for k1 in m.get('videoMindMappings'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappings()
                self.video_mind_mappings.append(temp_model.from_map(k1))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappings(DaraModel):
    def __init__(
        self,
        child_nodes: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes] = None,
        name: str = None,
    ):
        self.child_nodes = child_nodes
        self.name = name

    def validate(self):
        if self.child_nodes:
            for v1 in self.child_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['childNodes'] = []
        if self.child_nodes is not None:
            for k1 in self.child_nodes:
                result['childNodes'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_nodes = []
        if m.get('childNodes') is not None:
            for k1 in m.get('childNodes'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes()
                self.child_nodes.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodes(DaraModel):
    def __init__(
        self,
        child_nodes: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes] = None,
        name: str = None,
    ):
        self.child_nodes = child_nodes
        self.name = name

    def validate(self):
        if self.child_nodes:
            for v1 in self.child_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['childNodes'] = []
        if self.child_nodes is not None:
            for k1 in self.child_nodes:
                result['childNodes'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.child_nodes = []
        if m.get('childNodes') is not None:
            for k1 in m.get('childNodes'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes()
                self.child_nodes.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultVideoMindMappingsChildNodesChildNodes(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoMindMappingGenerateResultUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResults(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        index: int = None,
        model_id: str = None,
        reason_text: str = None,
        text: str = None,
        usage: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultsUsage = None,
    ):
        self.generate_finished = generate_finished
        self.index = index
        self.model_id = model_id
        self.reason_text = reason_text
        self.text = text
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished

        if self.index is not None:
            result['index'] = self.index

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.reason_text is not None:
            result['reasonText'] = self.reason_text

        if self.text is not None:
            result['text'] = self.text

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('reasonText') is not None:
            self.reason_text = m.get('reasonText')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('usage') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultsUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultsUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        index: int = None,
        model_id: str = None,
        model_reduce: bool = None,
        reason_text: str = None,
        text: str = None,
        usage: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultUsage = None,
    ):
        self.generate_finished = generate_finished
        self.index = index
        self.model_id = model_id
        self.model_reduce = model_reduce
        self.reason_text = reason_text
        self.text = text
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished

        if self.index is not None:
            result['index'] = self.index

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_reduce is not None:
            result['modelReduce'] = self.model_reduce

        if self.reason_text is not None:
            result['reasonText'] = self.reason_text

        if self.text is not None:
            result['text'] = self.text

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelReduce') is not None:
            self.model_reduce = m.get('modelReduce')

        if m.get('reasonText') is not None:
            self.reason_text = m.get('reasonText')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('usage') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoGenerateResultUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        video_captions: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResultVideoCaptions] = None,
    ):
        self.generate_finished = generate_finished
        self.video_captions = video_captions

    def validate(self):
        if self.video_captions:
            for v1 in self.video_captions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished

        result['videoCaptions'] = []
        if self.video_captions is not None:
            for k1 in self.video_captions:
                result['videoCaptions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')

        self.video_captions = []
        if m.get('videoCaptions') is not None:
            for k1 in m.get('videoCaptions'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResultVideoCaptions()
                self.video_captions.append(temp_model.from_map(k1))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoCaptionResultVideoCaptions(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        end_time_format: str = None,
        speaker: str = None,
        start_time: int = None,
        start_time_format: str = None,
        text: str = None,
    ):
        self.end_time = end_time
        self.end_time_format = end_time_format
        self.speaker = speaker
        self.start_time = start_time
        self.start_time_format = start_time_format
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.end_time_format is not None:
            result['endTimeFormat'] = self.end_time_format

        if self.speaker is not None:
            result['speaker'] = self.speaker

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.start_time_format is not None:
            result['startTimeFormat'] = self.start_time_format

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('endTimeFormat') is not None:
            self.end_time_format = m.get('endTimeFormat')

        if m.get('speaker') is not None:
            self.speaker = m.get('speaker')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('startTimeFormat') is not None:
            self.start_time_format = m.get('startTimeFormat')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoCalculatorResult(DaraModel):
    def __init__(
        self,
        items: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoCalculatorResultItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoCalculatorResultItems()
                self.items.append(temp_model.from_map(k1))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoCalculatorResultItems(DaraModel):
    def __init__(
        self,
        input_expense: float = None,
        input_token: int = None,
        name: str = None,
        output_expense: float = None,
        output_token: int = None,
        time: int = None,
        time_expense: float = None,
        total_expense: float = None,
        type: str = None,
    ):
        self.input_expense = input_expense
        self.input_token = input_token
        self.name = name
        self.output_expense = output_expense
        self.output_token = output_token
        self.time = time
        self.time_expense = time_expense
        self.total_expense = total_expense
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_expense is not None:
            result['inputExpense'] = self.input_expense

        if self.input_token is not None:
            result['inputToken'] = self.input_token

        if self.name is not None:
            result['name'] = self.name

        if self.output_expense is not None:
            result['outputExpense'] = self.output_expense

        if self.output_token is not None:
            result['outputToken'] = self.output_token

        if self.time is not None:
            result['time'] = self.time

        if self.time_expense is not None:
            result['timeExpense'] = self.time_expense

        if self.total_expense is not None:
            result['totalExpense'] = self.total_expense

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputExpense') is not None:
            self.input_expense = m.get('inputExpense')

        if m.get('inputToken') is not None:
            self.input_token = m.get('inputToken')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputExpense') is not None:
            self.output_expense = m.get('outputExpense')

        if m.get('outputToken') is not None:
            self.output_token = m.get('outputToken')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('timeExpense') is not None:
            self.time_expense = m.get('timeExpense')

        if m.get('totalExpense') is not None:
            self.total_expense = m.get('totalExpense')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        model_id: str = None,
        text: str = None,
        usage: main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultUsage = None,
        video_shot_analysis_results: List[main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultVideoShotAnalysisResults] = None,
    ):
        self.generate_finished = generate_finished
        self.model_id = model_id
        self.text = text
        self.usage = usage
        self.video_shot_analysis_results = video_shot_analysis_results

    def validate(self):
        if self.usage:
            self.usage.validate()
        if self.video_shot_analysis_results:
            for v1 in self.video_shot_analysis_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['generateFinished'] = self.generate_finished

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.text is not None:
            result['text'] = self.text

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        result['videoShotAnalysisResults'] = []
        if self.video_shot_analysis_results is not None:
            for k1 in self.video_shot_analysis_results:
                result['videoShotAnalysisResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('generateFinished') is not None:
            self.generate_finished = m.get('generateFinished')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('usage') is not None:
            temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        self.video_shot_analysis_results = []
        if m.get('videoShotAnalysisResults') is not None:
            for k1 in m.get('videoShotAnalysisResults'):
                temp_model = main_models.RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultVideoShotAnalysisResults()
                self.video_shot_analysis_results.append(temp_model.from_map(k1))

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultVideoShotAnalysisResults(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        text: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputVideoAnalysisResultUsage(DaraModel):
    def __init__(
        self,
        image_tokens: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.image_tokens = image_tokens
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_tokens is not None:
            result['imageTokens'] = self.image_tokens

        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageTokens') is not None:
            self.image_tokens = m.get('imageTokens')

        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class RunVideoAnalysisResponseBodyPayloadOutputAddDatasetDocumentsResult(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        error_message: str = None,
        status: int = None,
        title: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.error_message = error_message
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.doc_uuid is not None:
            result['docUuid'] = self.doc_uuid

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('docUuid') is not None:
            self.doc_uuid = m.get('docUuid')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class RunVideoAnalysisResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.event is not None:
            result['event'] = self.event

        if self.event_info is not None:
            result['eventInfo'] = self.event_info

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

