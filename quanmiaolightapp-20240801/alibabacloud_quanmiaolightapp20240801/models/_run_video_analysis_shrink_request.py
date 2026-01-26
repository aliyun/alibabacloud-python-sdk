# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunVideoAnalysisShrinkRequest(DaraModel):
    def __init__(
        self,
        add_document_param_shrink: str = None,
        auto_role_recognition_video_url: str = None,
        exclude_generate_options_shrink: str = None,
        face_identity_similarity_min_score: float = None,
        frame_sample_method_shrink: str = None,
        generate_options_shrink: str = None,
        language: str = None,
        model_custom_prompt_template: str = None,
        model_custom_prompt_template_id: str = None,
        model_id: str = None,
        original_session_id: str = None,
        snapshot_interval: float = None,
        split_interval: int = None,
        split_type: str = None,
        task_id: str = None,
        text_process_tasks_shrink: str = None,
        video_caption_info_shrink: str = None,
        video_extra_info: str = None,
        video_model_custom_prompt_template: str = None,
        video_model_id: str = None,
        video_roles_shrink: str = None,
        video_shot_face_identity_count: int = None,
        video_url: str = None,
        video_urls_shrink: str = None,
    ):
        self.add_document_param_shrink = add_document_param_shrink
        self.auto_role_recognition_video_url = auto_role_recognition_video_url
        self.exclude_generate_options_shrink = exclude_generate_options_shrink
        self.face_identity_similarity_min_score = face_identity_similarity_min_score
        self.frame_sample_method_shrink = frame_sample_method_shrink
        self.generate_options_shrink = generate_options_shrink
        self.language = language
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_prompt_template_id = model_custom_prompt_template_id
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.snapshot_interval = snapshot_interval
        self.split_interval = split_interval
        self.split_type = split_type
        self.task_id = task_id
        self.text_process_tasks_shrink = text_process_tasks_shrink
        self.video_caption_info_shrink = video_caption_info_shrink
        self.video_extra_info = video_extra_info
        self.video_model_custom_prompt_template = video_model_custom_prompt_template
        self.video_model_id = video_model_id
        self.video_roles_shrink = video_roles_shrink
        self.video_shot_face_identity_count = video_shot_face_identity_count
        self.video_url = video_url
        self.video_urls_shrink = video_urls_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_document_param_shrink is not None:
            result['addDocumentParam'] = self.add_document_param_shrink

        if self.auto_role_recognition_video_url is not None:
            result['autoRoleRecognitionVideoUrl'] = self.auto_role_recognition_video_url

        if self.exclude_generate_options_shrink is not None:
            result['excludeGenerateOptions'] = self.exclude_generate_options_shrink

        if self.face_identity_similarity_min_score is not None:
            result['faceIdentitySimilarityMinScore'] = self.face_identity_similarity_min_score

        if self.frame_sample_method_shrink is not None:
            result['frameSampleMethod'] = self.frame_sample_method_shrink

        if self.generate_options_shrink is not None:
            result['generateOptions'] = self.generate_options_shrink

        if self.language is not None:
            result['language'] = self.language

        if self.model_custom_prompt_template is not None:
            result['modelCustomPromptTemplate'] = self.model_custom_prompt_template

        if self.model_custom_prompt_template_id is not None:
            result['modelCustomPromptTemplateId'] = self.model_custom_prompt_template_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.original_session_id is not None:
            result['originalSessionId'] = self.original_session_id

        if self.snapshot_interval is not None:
            result['snapshotInterval'] = self.snapshot_interval

        if self.split_interval is not None:
            result['splitInterval'] = self.split_interval

        if self.split_type is not None:
            result['splitType'] = self.split_type

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.text_process_tasks_shrink is not None:
            result['textProcessTasks'] = self.text_process_tasks_shrink

        if self.video_caption_info_shrink is not None:
            result['videoCaptionInfo'] = self.video_caption_info_shrink

        if self.video_extra_info is not None:
            result['videoExtraInfo'] = self.video_extra_info

        if self.video_model_custom_prompt_template is not None:
            result['videoModelCustomPromptTemplate'] = self.video_model_custom_prompt_template

        if self.video_model_id is not None:
            result['videoModelId'] = self.video_model_id

        if self.video_roles_shrink is not None:
            result['videoRoles'] = self.video_roles_shrink

        if self.video_shot_face_identity_count is not None:
            result['videoShotFaceIdentityCount'] = self.video_shot_face_identity_count

        if self.video_url is not None:
            result['videoUrl'] = self.video_url

        if self.video_urls_shrink is not None:
            result['videoUrls'] = self.video_urls_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addDocumentParam') is not None:
            self.add_document_param_shrink = m.get('addDocumentParam')

        if m.get('autoRoleRecognitionVideoUrl') is not None:
            self.auto_role_recognition_video_url = m.get('autoRoleRecognitionVideoUrl')

        if m.get('excludeGenerateOptions') is not None:
            self.exclude_generate_options_shrink = m.get('excludeGenerateOptions')

        if m.get('faceIdentitySimilarityMinScore') is not None:
            self.face_identity_similarity_min_score = m.get('faceIdentitySimilarityMinScore')

        if m.get('frameSampleMethod') is not None:
            self.frame_sample_method_shrink = m.get('frameSampleMethod')

        if m.get('generateOptions') is not None:
            self.generate_options_shrink = m.get('generateOptions')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('modelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('modelCustomPromptTemplate')

        if m.get('modelCustomPromptTemplateId') is not None:
            self.model_custom_prompt_template_id = m.get('modelCustomPromptTemplateId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('originalSessionId') is not None:
            self.original_session_id = m.get('originalSessionId')

        if m.get('snapshotInterval') is not None:
            self.snapshot_interval = m.get('snapshotInterval')

        if m.get('splitInterval') is not None:
            self.split_interval = m.get('splitInterval')

        if m.get('splitType') is not None:
            self.split_type = m.get('splitType')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('textProcessTasks') is not None:
            self.text_process_tasks_shrink = m.get('textProcessTasks')

        if m.get('videoCaptionInfo') is not None:
            self.video_caption_info_shrink = m.get('videoCaptionInfo')

        if m.get('videoExtraInfo') is not None:
            self.video_extra_info = m.get('videoExtraInfo')

        if m.get('videoModelCustomPromptTemplate') is not None:
            self.video_model_custom_prompt_template = m.get('videoModelCustomPromptTemplate')

        if m.get('videoModelId') is not None:
            self.video_model_id = m.get('videoModelId')

        if m.get('videoRoles') is not None:
            self.video_roles_shrink = m.get('videoRoles')

        if m.get('videoShotFaceIdentityCount') is not None:
            self.video_shot_face_identity_count = m.get('videoShotFaceIdentityCount')

        if m.get('videoUrl') is not None:
            self.video_url = m.get('videoUrl')

        if m.get('videoUrls') is not None:
            self.video_urls_shrink = m.get('videoUrls')

        return self

