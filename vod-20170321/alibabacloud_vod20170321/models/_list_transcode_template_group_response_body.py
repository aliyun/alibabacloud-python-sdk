# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListTranscodeTemplateGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        transcode_template_group_list: List[main_models.ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The transcoding template groups.
        self.transcode_template_group_list = transcode_template_group_list

    def validate(self):
        if self.transcode_template_group_list:
            for v1 in self.transcode_template_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TranscodeTemplateGroupList'] = []
        if self.transcode_template_group_list is not None:
            for k1 in self.transcode_template_group_list:
                result['TranscodeTemplateGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.transcode_template_group_list = []
        if m.get('TranscodeTemplateGroupList') is not None:
            for k1 in m.get('TranscodeTemplateGroupList'):
                temp_model = main_models.ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList()
                self.transcode_template_group_list.append(temp_model.from_map(k1))

        return self

class ListTranscodeTemplateGroupResponseBodyTranscodeTemplateGroupList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        creation_time: str = None,
        is_default: str = None,
        locked: str = None,
        modify_time: str = None,
        name: str = None,
        transcode_template_group_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The time when the template group was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # Indicates whether the template group is the default one. Valid values:
        # 
        # *   **Default**: The template group is the default one.
        # *   **NotDefault**: The template group is not the default one.
        self.is_default = is_default
        # The lock status of the transcoding template group. Valid values:
        # 
        # *   **Disabled**: The template group is not locked.
        # *   **Enabled**: The template group is locked.
        self.locked = locked
        # The time when the template group was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modify_time = modify_time
        # The name of the template group.
        self.name = name
        # The ID of the transcoding template group.
        self.transcode_template_group_id = transcode_template_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.locked is not None:
            result['Locked'] = self.locked

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Locked') is not None:
            self.locked = m.get('Locked')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')

        return self

