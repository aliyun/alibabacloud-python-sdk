# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class SubmitVideoAnalysisTaskRequest(DaraModel):
    def __init__(
        self,
        add_document_param: main_models.SubmitVideoAnalysisTaskRequestAddDocumentParam = None,
        auto_role_recognition_video_url: str = None,
        deduplication_id: str = None,
        exclude_generate_options: List[str] = None,
        face_identity_similarity_min_score: float = None,
        frame_sample_method: main_models.SubmitVideoAnalysisTaskRequestFrameSampleMethod = None,
        generate_options: List[str] = None,
        language: str = None,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        snapshot_interval: float = None,
        split_interval: int = None,
        split_type: str = None,
        text_process_tasks: List[main_models.SubmitVideoAnalysisTaskRequestTextProcessTasks] = None,
        video_caption_info: main_models.SubmitVideoAnalysisTaskRequestVideoCaptionInfo = None,
        video_extra_info: str = None,
        video_model_custom_prompt_template: str = None,
        video_model_id: str = None,
        video_roles: List[main_models.SubmitVideoAnalysisTaskRequestVideoRoles] = None,
        video_shot_face_identity_count: int = None,
        video_url: str = None,
        video_urls: List[str] = None,
    ):
        self.add_document_param = add_document_param
        self.auto_role_recognition_video_url = auto_role_recognition_video_url
        self.deduplication_id = deduplication_id
        self.exclude_generate_options = exclude_generate_options
        self.face_identity_similarity_min_score = face_identity_similarity_min_score
        self.frame_sample_method = frame_sample_method
        self.generate_options = generate_options
        self.language = language
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.snapshot_interval = snapshot_interval
        self.split_interval = split_interval
        self.split_type = split_type
        self.text_process_tasks = text_process_tasks
        self.video_caption_info = video_caption_info
        self.video_extra_info = video_extra_info
        self.video_model_custom_prompt_template = video_model_custom_prompt_template
        self.video_model_id = video_model_id
        self.video_roles = video_roles
        self.video_shot_face_identity_count = video_shot_face_identity_count
        self.video_url = video_url
        self.video_urls = video_urls

    def validate(self):
        if self.add_document_param:
            self.add_document_param.validate()
        if self.frame_sample_method:
            self.frame_sample_method.validate()
        if self.text_process_tasks:
            for v1 in self.text_process_tasks:
                 if v1:
                    v1.validate()
        if self.video_caption_info:
            self.video_caption_info.validate()
        if self.video_roles:
            for v1 in self.video_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_document_param is not None:
            result['addDocumentParam'] = self.add_document_param.to_map()

        if self.auto_role_recognition_video_url is not None:
            result['autoRoleRecognitionVideoUrl'] = self.auto_role_recognition_video_url

        if self.deduplication_id is not None:
            result['deduplicationId'] = self.deduplication_id

        if self.exclude_generate_options is not None:
            result['excludeGenerateOptions'] = self.exclude_generate_options

        if self.face_identity_similarity_min_score is not None:
            result['faceIdentitySimilarityMinScore'] = self.face_identity_similarity_min_score

        if self.frame_sample_method is not None:
            result['frameSampleMethod'] = self.frame_sample_method.to_map()

        if self.generate_options is not None:
            result['generateOptions'] = self.generate_options

        if self.language is not None:
            result['language'] = self.language

        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template

        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.snapshot_interval is not None:
            result['snapshotInterval'] = self.snapshot_interval

        if self.split_interval is not None:
            result['splitInterval'] = self.split_interval

        if self.split_type is not None:
            result['splitType'] = self.split_type

        result['textProcessTasks'] = []
        if self.text_process_tasks is not None:
            for k1 in self.text_process_tasks:
                result['textProcessTasks'].append(k1.to_map() if k1 else None)

        if self.video_caption_info is not None:
            result['videoCaptionInfo'] = self.video_caption_info.to_map()

        if self.video_extra_info is not None:
            result['videoExtraInfo'] = self.video_extra_info

        if self.video_model_custom_prompt_template is not None:
            result['videoModelCustomPromptTemplate'] = self.video_model_custom_prompt_template

        if self.video_model_id is not None:
            result['videoModelId'] = self.video_model_id

        result['videoRoles'] = []
        if self.video_roles is not None:
            for k1 in self.video_roles:
                result['videoRoles'].append(k1.to_map() if k1 else None)

        if self.video_shot_face_identity_count is not None:
            result['videoShotFaceIdentityCount'] = self.video_shot_face_identity_count

        if self.video_url is not None:
            result['videoUrl'] = self.video_url

        if self.video_urls is not None:
            result['videoUrls'] = self.video_urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addDocumentParam') is not None:
            temp_model = main_models.SubmitVideoAnalysisTaskRequestAddDocumentParam()
            self.add_document_param = temp_model.from_map(m.get('addDocumentParam'))

        if m.get('autoRoleRecognitionVideoUrl') is not None:
            self.auto_role_recognition_video_url = m.get('autoRoleRecognitionVideoUrl')

        if m.get('deduplicationId') is not None:
            self.deduplication_id = m.get('deduplicationId')

        if m.get('excludeGenerateOptions') is not None:
            self.exclude_generate_options = m.get('excludeGenerateOptions')

        if m.get('faceIdentitySimilarityMinScore') is not None:
            self.face_identity_similarity_min_score = m.get('faceIdentitySimilarityMinScore')

        if m.get('frameSampleMethod') is not None:
            temp_model = main_models.SubmitVideoAnalysisTaskRequestFrameSampleMethod()
            self.frame_sample_method = temp_model.from_map(m.get('frameSampleMethod'))

        if m.get('generateOptions') is not None:
            self.generate_options = m.get('generateOptions')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')

        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('snapshotInterval') is not None:
            self.snapshot_interval = m.get('snapshotInterval')

        if m.get('splitInterval') is not None:
            self.split_interval = m.get('splitInterval')

        if m.get('splitType') is not None:
            self.split_type = m.get('splitType')

        self.text_process_tasks = []
        if m.get('textProcessTasks') is not None:
            for k1 in m.get('textProcessTasks'):
                temp_model = main_models.SubmitVideoAnalysisTaskRequestTextProcessTasks()
                self.text_process_tasks.append(temp_model.from_map(k1))

        if m.get('videoCaptionInfo') is not None:
            temp_model = main_models.SubmitVideoAnalysisTaskRequestVideoCaptionInfo()
            self.video_caption_info = temp_model.from_map(m.get('videoCaptionInfo'))

        if m.get('videoExtraInfo') is not None:
            self.video_extra_info = m.get('videoExtraInfo')

        if m.get('videoModelCustomPromptTemplate') is not None:
            self.video_model_custom_prompt_template = m.get('videoModelCustomPromptTemplate')

        if m.get('videoModelId') is not None:
            self.video_model_id = m.get('videoModelId')

        self.video_roles = []
        if m.get('videoRoles') is not None:
            for k1 in m.get('videoRoles'):
                temp_model = main_models.SubmitVideoAnalysisTaskRequestVideoRoles()
                self.video_roles.append(temp_model.from_map(k1))

        if m.get('videoShotFaceIdentityCount') is not None:
            self.video_shot_face_identity_count = m.get('videoShotFaceIdentityCount')

        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')

        if m.get('videoUrls') is not None:
            self.video_urls = m.get('videoUrls')

        return self

class SubmitVideoAnalysisTaskRequestVideoRoles(DaraModel):
    def __init__(
        self,
        is_auto_recognition: bool = None,
        role_info: str = None,
        role_name: str = None,
        time_intervals: List[main_models.SubmitVideoAnalysisTaskRequestVideoRolesTimeIntervals] = None,
        urls: List[str] = None,
    ):
        self.is_auto_recognition = is_auto_recognition
        self.role_info = role_info
        self.role_name = role_name
        self.time_intervals = time_intervals
        self.urls = urls

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

        if self.role_info is not None:
            result['roleInfo'] = self.role_info

        if self.role_name is not None:
            result['roleName'] = self.role_name

        result['timeIntervals'] = []
        if self.time_intervals is not None:
            for k1 in self.time_intervals:
                result['timeIntervals'].append(k1.to_map() if k1 else None)

        if self.urls is not None:
            result['urls'] = self.urls

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isAutoRecognition') is not None:
            self.is_auto_recognition = m.get('isAutoRecognition')

        if m.get('roleInfo') is not None:
            self.role_info = m.get('roleInfo')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        self.time_intervals = []
        if m.get('timeIntervals') is not None:
            for k1 in m.get('timeIntervals'):
                temp_model = main_models.SubmitVideoAnalysisTaskRequestVideoRolesTimeIntervals()
                self.time_intervals.append(temp_model.from_map(k1))

        if m.get('urls') is not None:
            self.urls = m.get('urls')

        return self

class SubmitVideoAnalysisTaskRequestVideoRolesTimeIntervals(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class SubmitVideoAnalysisTaskRequestVideoCaptionInfo(DaraModel):
    def __init__(
        self,
        video_caption_file_url: str = None,
        video_captions: List[main_models.SubmitVideoAnalysisTaskRequestVideoCaptionInfoVideoCaptions] = None,
    ):
        self.video_caption_file_url = video_caption_file_url
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
        if self.video_caption_file_url is not None:
            result['videoCaptionFileUrl'] = self.video_caption_file_url

        result['videoCaptions'] = []
        if self.video_captions is not None:
            for k1 in self.video_captions:
                result['videoCaptions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoCaptionFileUrl') is not None:
            self.video_caption_file_url = m.get('videoCaptionFileUrl')

        self.video_captions = []
        if m.get('videoCaptions') is not None:
            for k1 in m.get('videoCaptions'):
                temp_model = main_models.SubmitVideoAnalysisTaskRequestVideoCaptionInfoVideoCaptions()
                self.video_captions.append(temp_model.from_map(k1))

        return self

class SubmitVideoAnalysisTaskRequestVideoCaptionInfoVideoCaptions(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        speaker: str = None,
        start_time: int = None,
        text: str = None,
    ):
        self.end_time = end_time
        self.speaker = speaker
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

        if self.speaker is not None:
            result['speaker'] = self.speaker

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('speaker') is not None:
            self.speaker = m.get('speaker')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class SubmitVideoAnalysisTaskRequestTextProcessTasks(DaraModel):
    def __init__(
        self,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
    ):
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template

        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')

        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        return self

class SubmitVideoAnalysisTaskRequestFrameSampleMethod(DaraModel):
    def __init__(
        self,
        interval: float = None,
        method_name: str = None,
        pixel: int = None,
    ):
        self.interval = interval
        self.method_name = method_name
        self.pixel = pixel

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['interval'] = self.interval

        if self.method_name is not None:
            result['methodName'] = self.method_name

        if self.pixel is not None:
            result['pixel'] = self.pixel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')

        if m.get('pixel') is not None:
            self.pixel = m.get('pixel')

        return self

class SubmitVideoAnalysisTaskRequestAddDocumentParam(DaraModel):
    def __init__(
        self,
        dataset_id: int = None,
        dataset_name: str = None,
        document: main_models.SubmitVideoAnalysisTaskRequestAddDocumentParamDocument = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.document = document

    def validate(self):
        if self.document:
            self.document.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.document is not None:
            result['document'] = self.document.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('document') is not None:
            temp_model = main_models.SubmitVideoAnalysisTaskRequestAddDocumentParamDocument()
            self.document = temp_model.from_map(m.get('document'))

        return self

class SubmitVideoAnalysisTaskRequestAddDocumentParamDocument(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        title: str = None,
    ):
        self.doc_id = doc_id
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

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

