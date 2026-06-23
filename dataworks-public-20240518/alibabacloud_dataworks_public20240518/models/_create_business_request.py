# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBusinessRequest(DaraModel):
    def __init__(
        self,
        business_name: str = None,
        description: str = None,
        owner: str = None,
        project_id: int = None,
        project_identifier: str = None,
        use_type: str = None,
    ):
        # Name of the Business Process.<br>
        # The name must be unique within the same project space.
        # 
        # This parameter is required.
        self.business_name = business_name
        # Description of the Business Process.
        self.description = description
        # The Alibaba Cloud account ID of the owner responsible for the Business Process.<br>
        # You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console), move the mouse pointer over the profile picture in the upper-right corner of the menu bar, and view the Account ID. If this parameter is empty, the Alibaba Cloud account ID of the invoker is used by default.
        self.owner = owner
        # The ID of the DataWorks workspace.<br>
        # You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console), go to the Workspace Management page, and view the ID.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace, which is the English identifier displayed when you switch workspaces at the top of the Data Development page. You must specify either this parameter or the projectid parameter to identify the DataWorks project for this API call.
        self.project_identifier = project_identifier
        # Function module to which the Business Process belongs. Valid values:
        # 
        # - NORMAL (Data Development)
        # 
        # - MANUAL_BIZ (manually triggered workflow)
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.description is not None:
            result['Description'] = self.description

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

