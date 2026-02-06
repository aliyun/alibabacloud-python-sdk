# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddTranscodeTemplateGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        name: str = None,
        transcode_template_group_id: str = None,
        transcode_template_list: str = None,
    ):
        # The application ID. Default value: **app-1000000**. For more information, see [Use the multi-application service](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The name of the transcoding template group.
        # 
        # *   The name can be up to 128 bytes in length.
        # *   The value must be encoded in UTF-8.
        # 
        # > You must specify TranscodeTemplateGroupId or Name in the request.
        self.name = name
        # The ID of the transcoding template group. If a transcoding template group ID is specified, you can add transcoding templates to the template group.
        # 
        # > You must specify TranscodeTemplateGroupId or Name in the request.
        self.transcode_template_group_id = transcode_template_group_id
        # The configurations of the transcoding template. The value is a string in JSON format. For more information about the data structure, see [TranscodeTemplate](https://help.aliyun.com/document_detail/52839.html).
        # 
        # > *   If you do not specify this parameter, the transcoding job cannot be automatically created after you upload a video.
        # > *   If you do not need to set Width or Height, do not specify the corresponding parameter. You cannot set the value to an empty string, such as "Height":"".
        self.transcode_template_list = transcode_template_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.name is not None:
            result['Name'] = self.name

        if self.transcode_template_group_id is not None:
            result['TranscodeTemplateGroupId'] = self.transcode_template_group_id

        if self.transcode_template_list is not None:
            result['TranscodeTemplateList'] = self.transcode_template_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TranscodeTemplateGroupId') is not None:
            self.transcode_template_group_id = m.get('TranscodeTemplateGroupId')

        if m.get('TranscodeTemplateList') is not None:
            self.transcode_template_list = m.get('TranscodeTemplateList')

        return self

