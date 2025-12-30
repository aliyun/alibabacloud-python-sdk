# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListSmartSysAvatarModelsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        smart_sys_avatar_model_list: List[main_models.ListSmartSysAvatarModelsResponseBodySmartSysAvatarModelList] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried digital humans.
        self.smart_sys_avatar_model_list = smart_sys_avatar_model_list
        # The total number of system digital human images returned.
        self.total_count = total_count

    def validate(self):
        if self.smart_sys_avatar_model_list:
            for v1 in self.smart_sys_avatar_model_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SmartSysAvatarModelList'] = []
        if self.smart_sys_avatar_model_list is not None:
            for k1 in self.smart_sys_avatar_model_list:
                result['SmartSysAvatarModelList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.smart_sys_avatar_model_list = []
        if m.get('SmartSysAvatarModelList') is not None:
            for k1 in m.get('SmartSysAvatarModelList'):
                temp_model = main_models.ListSmartSysAvatarModelsResponseBodySmartSysAvatarModelList()
                self.smart_sys_avatar_model_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSmartSysAvatarModelsResponseBodySmartSysAvatarModelList(DaraModel):
    def __init__(
        self,
        avatar_id: str = None,
        avatar_name: str = None,
        bitrate: int = None,
        cover_url: str = None,
        height: int = None,
        output_mask: bool = None,
        video_url: str = None,
        width: int = None,
    ):
        # The ID of the digital human. The ID is required to submit a separate digital human rendering job or use the digital human image in an intelligent timeline.
        self.avatar_id = avatar_id
        # The name of the digital human.
        self.avatar_name = avatar_name
        # The video bitrate.
        self.bitrate = bitrate
        # The sample thumbnail URL of the digital human.
        self.cover_url = cover_url
        # The video height.
        self.height = height
        # Indicates whether portrait mask rendering is supported.
        self.output_mask = output_mask
        # The sample video URL of the digital human.
        self.video_url = video_url
        # The video width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        if self.avatar_name is not None:
            result['AvatarName'] = self.avatar_name

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.height is not None:
            result['Height'] = self.height

        if self.output_mask is not None:
            result['OutputMask'] = self.output_mask

        if self.video_url is not None:
            result['VideoUrl'] = self.video_url

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        if m.get('AvatarName') is not None:
            self.avatar_name = m.get('AvatarName')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('OutputMask') is not None:
            self.output_mask = m.get('OutputMask')

        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

