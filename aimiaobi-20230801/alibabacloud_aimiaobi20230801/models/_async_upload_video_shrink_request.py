# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AsyncUploadVideoShrinkRequest(DaraModel):
    def __init__(
        self,
        anlysis_prompt: str = None,
        face_identity_similarity_min_score: float = None,
        reference_video_shrink: str = None,
        remove_subtitle: bool = None,
        source_videos_shrink: str = None,
        split_interval: int = None,
        video_roles_shrink: str = None,
        video_shot_face_identity_count: int = None,
        workspace_id: str = None,
    ):
        self.anlysis_prompt = anlysis_prompt
        self.face_identity_similarity_min_score = face_identity_similarity_min_score
        self.reference_video_shrink = reference_video_shrink
        self.remove_subtitle = remove_subtitle
        # This parameter is required.
        self.source_videos_shrink = source_videos_shrink
        self.split_interval = split_interval
        self.video_roles_shrink = video_roles_shrink
        self.video_shot_face_identity_count = video_shot_face_identity_count
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anlysis_prompt is not None:
            result['AnlysisPrompt'] = self.anlysis_prompt

        if self.face_identity_similarity_min_score is not None:
            result['FaceIdentitySimilarityMinScore'] = self.face_identity_similarity_min_score

        if self.reference_video_shrink is not None:
            result['ReferenceVideo'] = self.reference_video_shrink

        if self.remove_subtitle is not None:
            result['RemoveSubtitle'] = self.remove_subtitle

        if self.source_videos_shrink is not None:
            result['SourceVideos'] = self.source_videos_shrink

        if self.split_interval is not None:
            result['SplitInterval'] = self.split_interval

        if self.video_roles_shrink is not None:
            result['VideoRoles'] = self.video_roles_shrink

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
            self.reference_video_shrink = m.get('ReferenceVideo')

        if m.get('RemoveSubtitle') is not None:
            self.remove_subtitle = m.get('RemoveSubtitle')

        if m.get('SourceVideos') is not None:
            self.source_videos_shrink = m.get('SourceVideos')

        if m.get('SplitInterval') is not None:
            self.split_interval = m.get('SplitInterval')

        if m.get('VideoRoles') is not None:
            self.video_roles_shrink = m.get('VideoRoles')

        if m.get('VideoShotFaceIdentityCount') is not None:
            self.video_shot_face_identity_count = m.get('VideoShotFaceIdentityCount')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

