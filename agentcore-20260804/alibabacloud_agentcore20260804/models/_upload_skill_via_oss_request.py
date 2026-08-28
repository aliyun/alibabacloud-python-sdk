# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UploadSkillViaOssRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UploadSkillViaOssRequestBody = None,
    ):
        # The request body.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UploadSkillViaOssRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UploadSkillViaOssRequestBody(DaraModel):
    def __init__(
        self,
        commit_msg: str = None,
        oss_object_name: str = None,
        overwrite: bool = None,
        target_version: str = None,
    ):
        # The commit message. This parameter is optional.
        self.commit_msg = commit_msg
        # The OSS object name (path).
        # 
        # This parameter is required.
        self.oss_object_name = oss_object_name
        # Specifies whether to overwrite an existing Skill. Default value: false.
        self.overwrite = overwrite
        # The upload version number. This parameter is optional and used as a fallback when the ZIP package contains no version information.
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit_msg is not None:
            result['commitMsg'] = self.commit_msg

        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name

        if self.overwrite is not None:
            result['overwrite'] = self.overwrite

        if self.target_version is not None:
            result['targetVersion'] = self.target_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commitMsg') is not None:
            self.commit_msg = m.get('commitMsg')

        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')

        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')

        if m.get('targetVersion') is not None:
            self.target_version = m.get('targetVersion')

        return self

