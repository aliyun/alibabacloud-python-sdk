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
        operation: str = None,
        request_id: str = None,
        slug: str = None,
        state: str = None,
        target_dir: str = None,
        task_id: str = None,
        version: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The returned status code.
        self.code = code
        # The returned message.
        self.message = message
        # Indicates whether the operation is successful. This parameter is returned when Async is set to false.
        self.ok = ok
        # The name of the operation. This parameter is returned when Async is set to true.
        self.operation = operation
        # The request ID.
        self.request_id = request_id
        # The identifier of the installed skill. This parameter is returned during synchronous execution.
        self.slug = slug
        # The initial state of the task. This parameter is returned when Async is set to true.
        self.state = state
        # The installation directory. This parameter is returned during synchronous execution.
        self.target_dir = target_dir
        # The ID of the asynchronous task. This parameter is returned when Async is set to true.
        self.task_id = task_id
        # The installed version number. This parameter is returned during synchronous execution.
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

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slug is not None:
            result['Slug'] = self.slug

        if self.state is not None:
            result['State'] = self.state

        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir

        if self.task_id is not None:
            result['TaskId'] = self.task_id

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

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Slug') is not None:
            self.slug = m.get('Slug')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

