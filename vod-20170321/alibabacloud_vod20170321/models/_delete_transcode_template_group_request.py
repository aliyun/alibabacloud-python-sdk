# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTranscodeTemplateGroupRequest(DaraModel):
    def __init__(
        self,
        force_del_group: str = None,
        transcode_template_group_id: str = None,
        transcode_template_ids: str = None,
    ):
        # Indicates whether to force delete the entire transcoding template group. Valid values:
        # 
        # - **true**: Force deletes the entire template group and all its transcoding templates.
        # - **false** (default): Deletes only the specified transcoding templates.
        self.force_del_group = force_del_group
        # The ID of the transcoding template group.
        # 
        # This parameter is required.
        self.transcode_template_group_id = transcode_template_group_id
        # The IDs of the transcoding templates that you want to delete.
        # 
        # - Separate multiple IDs with commas (,).
        # - A maximum of 10 template IDs are supported.
        # - This parameter is required if the ForceDelGroup parameter is empty or set to false.
        self.transcode_template_ids = transcode_template_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_del_group is not None:
            result['ForceDelGroup'] = self.force_del_group

        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id

        if self.transcode_template_ids is not None:
            result['TranscodeTemplateIds'] = self.transcode_template_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDelGroup') is not None:
            self.force_del_group = m.get('ForceDelGroup')

        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')

        if m.get('TranscodeTemplateIds') is not None:
            self.transcode_template_ids = m.get('TranscodeTemplateIds')

        return self

