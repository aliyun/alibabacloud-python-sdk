# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class AsyncUploadVideoRequest(DaraModel):
    def __init__(
        self,
        anlysis_prompt: str = None,
        face_identity_similarity_min_score: float = None,
        reference_video: main_models.AsyncUploadVideoRequestReferenceVideo = None,
        remove_subtitle: bool = None,
        source_videos: List[main_models.AsyncUploadVideoRequestSourceVideos] = None,
        split_interval: int = None,
        video_roles: List[main_models.AsyncUploadVideoRequestVideoRoles] = None,
        video_shot_face_identity_count: int = None,
        workspace_id: str = None,
    ):
        self.anlysis_prompt = anlysis_prompt
        self.face_identity_similarity_min_score = face_identity_similarity_min_score
        self.reference_video = reference_video
        self.remove_subtitle = remove_subtitle
        # This parameter is required.
        self.source_videos = source_videos
        self.split_interval = split_interval
        self.video_roles = video_roles
        self.video_shot_face_identity_count = video_shot_face_identity_count
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.reference_video:
            self.reference_video.validate()
        if self.source_videos:
            for v1 in self.source_videos:
                 if v1:
                    v1.validate()
        if self.video_roles:
            for v1 in self.video_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anlysis_prompt is not None:
            result['AnlysisPrompt'] = self.anlysis_prompt

        if self.face_identity_similarity_min_score is not None:
            result['FaceIdentitySimilarityMinScore'] = self.face_identity_similarity_min_score

        if self.reference_video is not None:
            result['ReferenceVideo'] = self.reference_video.to_map()

        if self.remove_subtitle is not None:
            result['RemoveSubtitle'] = self.remove_subtitle

        result['SourceVideos'] = []
        if self.source_videos is not None:
            for k1 in self.source_videos:
                result['SourceVideos'].append(k1.to_map() if k1 else None)

        if self.split_interval is not None:
            result['SplitInterval'] = self.split_interval

        result['VideoRoles'] = []
        if self.video_roles is not None:
            for k1 in self.video_roles:
                result['VideoRoles'].append(k1.to_map() if k1 else None)

        if self.video_shot_face_identity_count is not None:
            result['VideoShotFaceIdentityCount'] = self.video_shot_face_identity_count

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnlysisPrompt') is not None:
            self.anlysis_prompt = m.get('AnlysisPrompt')

        if m.get('FaceIdentitySimilarityMinScore') is not None:
            self.face_identity_similarity_min_score = m.get('FaceIdentitySimilarityMinScore')

        if m.get('ReferenceVideo') is not None:
            temp_model = main_models.AsyncUploadVideoRequestReferenceVideo()
            self.reference_video = temp_model.from_map(m.get('ReferenceVideo'))

        if m.get('RemoveSubtitle') is not None:
            self.remove_subtitle = m.get('RemoveSubtitle')

        self.source_videos = []
        if m.get('SourceVideos') is not None:
            for k1 in m.get('SourceVideos'):
                temp_model = main_models.AsyncUploadVideoRequestSourceVideos()
                self.source_videos.append(temp_model.from_map(k1))

        if m.get('SplitInterval') is not None:
            self.split_interval = m.get('SplitInterval')

        self.video_roles = []
        if m.get('VideoRoles') is not None:
            for k1 in m.get('VideoRoles'):
                temp_model = main_models.AsyncUploadVideoRequestVideoRoles()
                self.video_roles.append(temp_model.from_map(k1))

        if m.get('VideoShotFaceIdentityCount') is not None:
            self.video_shot_face_identity_count = m.get('VideoShotFaceIdentityCount')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class AsyncUploadVideoRequestVideoRoles(DaraModel):
    def __init__(
        self,
        role_info: str = None,
        role_name: str = None,
        role_urls: List[main_models.AsyncUploadVideoRequestVideoRolesRoleUrls] = None,
    ):
        self.role_info = role_info
        self.role_name = role_name
        self.role_urls = role_urls

    def validate(self):
        if self.role_urls:
            for v1 in self.role_urls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_info is not None:
            result['RoleInfo'] = self.role_info

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        result['RoleUrls'] = []
        if self.role_urls is not None:
            for k1 in self.role_urls:
                result['RoleUrls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleInfo') is not None:
            self.role_info = m.get('RoleInfo')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        self.role_urls = []
        if m.get('RoleUrls') is not None:
            for k1 in m.get('RoleUrls'):
                temp_model = main_models.AsyncUploadVideoRequestVideoRolesRoleUrls()
                self.role_urls.append(temp_model.from_map(k1))

        return self

class AsyncUploadVideoRequestVideoRolesRoleUrls(DaraModel):
    def __init__(
        self,
        role_file_name: str = None,
        role_file_url: str = None,
    ):
        self.role_file_name = role_file_name
        self.role_file_url = role_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_file_name is not None:
            result['RoleFileName'] = self.role_file_name

        if self.role_file_url is not None:
            result['RoleFileUrl'] = self.role_file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleFileName') is not None:
            self.role_file_name = m.get('RoleFileName')

        if m.get('RoleFileUrl') is not None:
            self.role_file_url = m.get('RoleFileUrl')

        return self

class AsyncUploadVideoRequestSourceVideos(DaraModel):
    def __init__(
        self,
        video_extra_info: str = None,
        video_name: str = None,
        video_url: str = None,
    ):
        self.video_extra_info = video_extra_info
        # This parameter is required.
        self.video_name = video_name
        # This parameter is required.
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_extra_info is not None:
            result['VideoExtraInfo'] = self.video_extra_info

        if self.video_name is not None:
            result['VideoName'] = self.video_name

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoExtraInfo') is not None:
            self.video_extra_info = m.get('VideoExtraInfo')

        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

class AsyncUploadVideoRequestReferenceVideo(DaraModel):
    def __init__(
        self,
        video_extra_info: str = None,
        video_name: str = None,
        video_url: str = None,
    ):
        self.video_extra_info = video_extra_info
        self.video_name = video_name
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_extra_info is not None:
            result['VideoExtraInfo'] = self.video_extra_info

        if self.video_name is not None:
            result['VideoName'] = self.video_name

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoExtraInfo') is not None:
            self.video_extra_info = m.get('VideoExtraInfo')

        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        return self

