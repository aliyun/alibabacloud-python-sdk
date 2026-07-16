# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class CreateRenderingProjectRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        project_name: str = None,
        session_attribs: main_models.CreateRenderingProjectRequestSessionAttribs = None,
    ):
        # The description of the project. The description can be 0 to 255 characters in length.
        self.description = description
        # The custom name of the project. This name is the unique identifier for the project.
        # The name must meet the following requirements:
        # 
        # 1. Be 1 to 128 characters in length.
        # 
        # 2. Contain only lowercase letters, digits, underscores (_), hyphens (-), and periods (.).
        # 
        # 3. Start and end with a letter or a digit.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The session properties.
        self.session_attribs = session_attribs

    def validate(self):
        if self.session_attribs:
            self.session_attribs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.session_attribs is not None:
            result['SessionAttribs'] = self.session_attribs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SessionAttribs') is not None:
            temp_model = main_models.CreateRenderingProjectRequestSessionAttribs()
            self.session_attribs = temp_model.from_map(m.get('SessionAttribs'))

        return self

class CreateRenderingProjectRequestSessionAttribs(DaraModel):
    def __init__(
        self,
        start_mode: str = None,
    ):
        # The mode to start the cloud application service for the session. Valid values:
        # 
        # 1. Async: asynchronous
        # 
        # 2. Sync: synchronous
        self.start_mode = start_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start_mode is not None:
            result['StartMode'] = self.start_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartMode') is not None:
            self.start_mode = m.get('StartMode')

        return self

