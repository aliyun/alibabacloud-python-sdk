# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetRoutineStagingCodeUploadInfoResponseBody(DaraModel):
    def __init__(
        self,
        code_version: str = None,
        oss_post_config: Dict[str, Any] = None,
        request_id: str = None,
    ):
        # The code version.
        self.code_version = code_version
        # The configuration information that can be used to upload to OSS.
        self.oss_post_config = oss_post_config
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_version is not None:
            result['CodeVersion'] = self.code_version

        if self.oss_post_config is not None:
            result['OssPostConfig'] = self.oss_post_config

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')

        if m.get('OssPostConfig') is not None:
            self.oss_post_config = m.get('OssPostConfig')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

