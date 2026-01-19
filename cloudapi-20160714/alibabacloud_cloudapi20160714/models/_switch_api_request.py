# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchApiRequest(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        description: str = None,
        group_id: str = None,
        history_version: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        # The API ID.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The description. The description can be up to 200 characters in length.
        # 
        # This parameter is required.
        self.description = description
        # The API group ID.
        self.group_id = group_id
        # The historical version number of the API.
        # 
        # This parameter is required.
        self.history_version = history_version
        self.security_token = security_token
        # The environment. Valid values:
        # 
        # *   **RELEASE**: the production environment
        # *   **PRE**: the staging environment
        # *   **TEST**: the test environment
        # 
        # This parameter is required.
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.history_version is not None:
            result['HistoryVersion'] = self.history_version

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HistoryVersion') is not None:
            self.history_version = m.get('HistoryVersion')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

