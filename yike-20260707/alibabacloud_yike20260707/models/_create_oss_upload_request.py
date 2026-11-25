# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOssUploadRequest(DaraModel):
    def __init__(
        self,
        biz_config: str = None,
        credential_type: str = None,
        file_ext: str = None,
        file_type: str = None,
        target_bucket: str = None,
    ):
        # The **business configuration JSON**, which includes ProductionId and FolderId.
        self.biz_config = biz_config
        # The credential type. This is a reserved parameter. The current version always returns STS temporary credentials, and this parameter does not take effect.
        self.credential_type = credential_type
        # The file name extension, such as mp4, wav, or png. Do not include the dot. If this parameter is missing, `MissingParameter` is returned.
        # 
        # This parameter is required.
        self.file_ext = file_ext
        # The file type. Valid values: `Media` (default), `StoryboardInput`, `ImageFusion`, `AIAppParams`, `Workflow`, and `CommonFile`. If an invalid value is specified, `InvalidParameter` is returned. This value is used as a path segment in the `ObjectKey` and is converted to lowercase.
        self.file_type = file_type
        # The explicitly specified target bucket.
        self.target_bucket = target_bucket

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_config is not None:
            result['BizConfig'] = self.biz_config

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.file_ext is not None:
            result['FileExt'] = self.file_ext

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.target_bucket is not None:
            result['TargetBucket'] = self.target_bucket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizConfig') is not None:
            self.biz_config = m.get('BizConfig')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('FileExt') is not None:
            self.file_ext = m.get('FileExt')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('TargetBucket') is not None:
            self.target_bucket = m.get('TargetBucket')

        return self

