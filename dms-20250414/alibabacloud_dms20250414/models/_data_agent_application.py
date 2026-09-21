# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataAgentApplication(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        app_name: str = None,
        application_extra_info: str = None,
        creator_name: str = None,
        creator_uid: str = None,
        description: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        main_uid: str = None,
        region: str = None,
        session_id: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        # The ID of the currently associated Data Agent.
        self.agent_id = agent_id
        # The stable identifier of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The extension information of the application.
        self.application_extra_info = application_extra_info
        # The name of the application creator.
        self.creator_name = creator_name
        # The UID of the application owner.
        self.creator_uid = creator_uid
        # The description of the application. The description can be up to 250 characters in length.
        self.description = description
        # The time when the application was created.
        self.gmt_created = gmt_created
        # The time when the application was last modified.
        self.gmt_modified = gmt_modified
        # The UID of the Alibaba Cloud account.
        self.main_uid = main_uid
        # The region.
        self.region = region
        # The ID of the current or most recently associated session.
        self.session_id = session_id
        # The status of the application. Valid values:
        # - REGISTERED
        # - DEPLOYING
        # - DEPLOYED
        self.status = status
        # The ID of the workspace.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.application_extra_info is not None:
            result['ApplicationExtraInfo'] = self.application_extra_info

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.creator_uid is not None:
            result['CreatorUid'] = self.creator_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.main_uid is not None:
            result['MainUid'] = self.main_uid

        if self.region is not None:
            result['Region'] = self.region

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status is not None:
            result['Status'] = self.status

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ApplicationExtraInfo') is not None:
            self.application_extra_info = m.get('ApplicationExtraInfo')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('CreatorUid') is not None:
            self.creator_uid = m.get('CreatorUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MainUid') is not None:
            self.main_uid = m.get('MainUid')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

