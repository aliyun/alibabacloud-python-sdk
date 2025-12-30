# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAvatarTrainingJobRequest(DaraModel):
    def __init__(
        self,
        avatar_description: str = None,
        avatar_name: str = None,
        job_id: str = None,
        portrait: str = None,
        thumbnail: str = None,
        transparent: bool = None,
        video: str = None,
    ):
        # *   The description of the digital human.
        # *   The description can be up to 1,000 characters in length.
        self.avatar_description = avatar_description
        # *   The name of the digital human.
        # *   The name can be up to seven characters in length.
        self.avatar_name = avatar_name
        # The ID of the digital human training job.
        # 
        # This parameter is required.
        self.job_id = job_id
        # *   The media asset ID of the portrait image.
        # *   The value must be 32 characters in length.
        self.portrait = portrait
        # *   The thumbnail URL.
        # *   After the digital human is trained, the thumbnail is uploaded to this URL.
        # *   The URL must be a valid public Object Storage Service (OSS) URL.
        # *   The URL can be up to 512 characters in length.
        # *   The URL cannot be updated after the digital human is trained.
        self.thumbnail = thumbnail
        # *   Indicates whether the input video supports alpha channels.
        # 
        # *   You can modify this parameter only if the job is in the Init or Fail state.
        # 
        #     **
        # 
        #     **Note**: Make sure that the current settings are consistent with those of the submitted training video. Otherwise, the digital human may malfunction.
        self.transparent = transparent
        # *   The ID of the video used for training.
        # *   The value must be 32 characters in length.
        # *   Supported formats: MP4, MOV, and WebM.
        # *   The duration of the video must be 5 to 15 minutes.
        # *   The resolution of the video must be 1920×1080 or 1080×1920.
        self.video = video

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_description is not None:
            result['AvatarDescription'] = self.avatar_description

        if self.avatar_name is not None:
            result['AvatarName'] = self.avatar_name

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.portrait is not None:
            result['Portrait'] = self.portrait

        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail

        if self.transparent is not None:
            result['Transparent'] = self.transparent

        if self.video is not None:
            result['Video'] = self.video

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarDescription') is not None:
            self.avatar_description = m.get('AvatarDescription')

        if m.get('AvatarName') is not None:
            self.avatar_name = m.get('AvatarName')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')

        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')

        if m.get('Transparent') is not None:
            self.transparent = m.get('Transparent')

        if m.get('Video') is not None:
            self.video = m.get('Video')

        return self

