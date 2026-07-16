# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallPolarClawSkillResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        message: str = None,
        ok: bool = None,
        request_id: str = None,
        slug: str = None,
        target_dir: str = None,
        version: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The response message.
        self.message = message
        # Indicates whether the operation was successful.
        self.ok = ok
        # Id of the request
        self.request_id = request_id
        # The identifier of the installed Skill.
        self.slug = slug
        # The installation directory.
        self.target_dir = target_dir
        # The version number of the installed Skill.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.ok is not None:
            result['Ok'] = self.ok

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Ok') is not None:
            self.ok = m.get('Ok')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

