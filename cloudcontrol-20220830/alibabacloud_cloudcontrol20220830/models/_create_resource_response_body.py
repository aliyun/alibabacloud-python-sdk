# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
        resource_path: str = None,
        task_id: str = None,
    ):
        # The ID of a request.
        self.request_id = request_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The path of the resources. The relative resource ID. The resource path contains the complete resource location (parent resource/child resource).
        self.resource_path = resource_path
        # The ID of the asynchronous task. If the operation is asynchronous, this field is returned. In this case, the HTTP status code 202 is returned.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_path is not None:
            result['resourcePath'] = self.resource_path

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourcePath') is not None:
            self.resource_path = m.get('resourcePath')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

