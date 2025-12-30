# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEditingProjectRequest(DaraModel):
    def __init__(
        self,
        project_id: str = None,
        request_source: str = None,
    ):
        # The ID of the online editing project.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The ID of the request source. Valid values:
        # 
        # \\- OpenAPI (default): Timeline conversion is not performed.
        # 
        # \\- WebSDK: If you specify this value, the project timeline is automatically converted into the frontend style, and the materials in the timeline are associated with the project to enable preview by using frontend web SDKs.
        self.request_source = request_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        return self

