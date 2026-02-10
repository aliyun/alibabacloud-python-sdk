# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadedHoneyPotFileRequest(DaraModel):
    def __init__(
        self,
        file_key: str = None,
        file_name: str = None,
        file_type: str = None,
        honeypot_image_name: str = None,
        lang: str = None,
        node_id: str = None,
        template_extra: str = None,
    ):
        # The file key that you use to upload the file.
        # 
        # >  The key is in the format of HONEYPOT_FILE/{Timestamp}_{Custom file name}.
        # 
        # This parameter is required.
        self.file_key = file_key
        # The name of the file that you want to upload.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The file type.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The name of the honeypot image.
        # 
        # This parameter is required.
        self.honeypot_image_name = honeypot_image_name
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the management node to which the honeypot belongs.
        # 
        # >  You can call the [ListHoneypotNode](~~ListHoneypotNode~~) operation to obtain the IDs of management nodes. operation to query the management node ID.
        self.node_id = node_id
        # The prompt template that corresponds to the file.
        # 
        # This parameter is required.
        self.template_extra = template_extra

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.honeypot_image_name is not None:
            result['HoneypotImageName'] = self.honeypot_image_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.template_extra is not None:
            result['TemplateExtra'] = self.template_extra

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('HoneypotImageName') is not None:
            self.honeypot_image_name = m.get('HoneypotImageName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('TemplateExtra') is not None:
            self.template_extra = m.get('TemplateExtra')

        return self

