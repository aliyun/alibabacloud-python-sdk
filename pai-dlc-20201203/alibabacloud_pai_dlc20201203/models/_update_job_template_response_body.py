# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateJobTemplateResponseBody(DaraModel):
    def __init__(
        self,
        default_version: int = None,
        gmt_modify_time: str = None,
        request_id: str = None,
        version: int = None,
        version_created: bool = None,
    ):
        self.default_version = default_version
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modify_time = gmt_modify_time
        # 本次请求的 ID，用于诊断和答疑。
        self.request_id = request_id
        self.version = version
        self.version_created = version_created

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.version is not None:
            result['Version'] = self.version

        if self.version_created is not None:
            result['VersionCreated'] = self.version_created

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionCreated') is not None:
            self.version_created = m.get('VersionCreated')

        return self

