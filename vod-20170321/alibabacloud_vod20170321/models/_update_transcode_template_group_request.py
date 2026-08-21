# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTranscodeTemplateGroupRequest(DaraModel):
    def __init__(
        self,
        locked: str = None,
        name: str = None,
        transcode_template_group_id: str = None,
        transcode_template_list: str = None,
    ):
        # The lock state of the template group. Valid values:
        # 
        # - **Enabled**: locked. A locked template group cannot be modified.
        # - **Disabled** (default): unlocked.
        # 
        # Default value: **Disabled**. If you specify this parameter, the lock state of the template group is changed, while the name and configurations of the transcoding template group remain unchanged.
        self.locked = locked
        # The name of the transcoding template group.
        # 
        # - The name can be up to 128 bytes in length.
        # - The name is encoded in UTF-8.
        self.name = name
        # The ID of the transcoding template group.
        # 
        # This parameter is required.
        self.transcode_template_group_id = transcode_template_group_id
        # The transcoding template configurations (a JSON string). For more information about the parameter structure, see [TranscodeTemplate](~~52839#title-9mb-8o2-uu6~~).
        self.transcode_template_list = transcode_template_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.locked is not None:
            result['Locked'] = self.locked

        if self.name is not None:
            result['Name'] = self.name

        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id

        if self.transcode_template_list is not None:
            result['TranscodeTemplateList'] = self.transcode_template_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locked') is not None:
            self.locked = m.get('Locked')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')

        if m.get('TranscodeTemplateList') is not None:
            self.transcode_template_list = m.get('TranscodeTemplateList')

        return self

