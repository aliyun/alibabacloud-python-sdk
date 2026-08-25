# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserProvisioningConfigurationRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        new_default_landing_page: str = None,
        new_session_duration: int = None,
    ):
        # The ID of the resource directory.
        self.directory_id = directory_id
        # The new default URL for a CloudSSO user who logs on to the Alibaba Cloud Management Console.
        # 
        # Default value: https://homenew.console.aliyun.com.
        self.new_default_landing_page = new_default_landing_page
        # The new duration of the logon session.
        # 
        # Unit: hours.
        # 
        # Valid values: 1 to 24.
        # 
        # Default value: 6.
        self.new_session_duration = new_session_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.new_default_landing_page is not None:
            result['NewDefaultLandingPage'] = self.new_default_landing_page

        if self.new_session_duration is not None:
            result['NewSessionDuration'] = self.new_session_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('NewDefaultLandingPage') is not None:
            self.new_default_landing_page = m.get('NewDefaultLandingPage')

        if m.get('NewSessionDuration') is not None:
            self.new_session_duration = m.get('NewSessionDuration')

        return self

