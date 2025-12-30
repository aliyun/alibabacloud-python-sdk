# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SendFileRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        file_group: str = None,
        file_mode: str = None,
        file_owner: str = None,
        name: str = None,
        node_id_list: List[str] = None,
        overwrite: bool = None,
        target_dir: str = None,
        timeout: int = None,
    ):
        # The content of the file. The file must not exceed 32 KB in size after it is encoded in Base64.
        # 
        # *   If `ContentType` is set to `PlainText`, the value of Content is in plaintext.
        # *   If `ContentType` is set to `Base64`, the value of Content is Base64-encoded.
        # 
        # This parameter is required.
        self.content = content
        # The content type of the file. Valid values:
        # 
        # PlainText Base64 Default value: PlainText.
        self.content_type = content_type
        # The description of the file. The description can be up to 512 characters in length and can contain any characters.
        self.description = description
        # The user group of the file. This parameter takes effect only on Linux instances. Default value: root. The value can be up to 64 characters in length.
        # 
        # Note If you want to use a non-root user group, make sure that the user group exists in the instances.
        self.file_group = file_group
        # The permissions on the file. This parameter takes effect only on Linux instances. You can configure this parameter in the same way as you configure the chmod command.
        # 
        # Default value: 0644: the owner of the file has the read and write permission. The user group of the file and other users have read-only permission.
        self.file_mode = file_mode
        # The owner of the file. This parameter takes effect only on Linux instances. Default value: root.
        self.file_owner = file_owner
        # The file name. The name can be up to 255 characters in length and can contain any characters.
        # 
        # This parameter is required.
        self.name = name
        # The node list.
        # 
        # This parameter is required.
        self.node_id_list = node_id_list
        # Specifies whether to overwrite file with the same name in the destination directory.
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.overwrite = overwrite
        # The directory in the Lingjun node to which the file is sent. If the specified directory does not exist, the system creates the directory automatically.
        # 
        # This parameter is required.
        self.target_dir = target_dir
        # The timeout period for the file sending task. Unit: seconds.
        # 
        # *   A timeout error occurs when a file cannot be sent because the process slows down or because a specific module or Cloud Assistant Agent does not exist.
        # *   If the specified timeout period is less than 10 seconds, the system sets the timeout period to 10 seconds to ensure that the file can be sent.
        # 
        # Default value: 60.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.description is not None:
            result['Description'] = self.description

        if self.file_group is not None:
            result['FileGroup'] = self.file_group

        if self.file_mode is not None:
            result['FileMode'] = self.file_mode

        if self.file_owner is not None:
            result['FileOwner'] = self.file_owner

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileGroup') is not None:
            self.file_group = m.get('FileGroup')

        if m.get('FileMode') is not None:
            self.file_mode = m.get('FileMode')

        if m.get('FileOwner') is not None:
            self.file_owner = m.get('FileOwner')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

