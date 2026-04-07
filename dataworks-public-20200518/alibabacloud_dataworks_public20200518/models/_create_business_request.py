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
        # The name of the business process. The name of the business process in the same project must be unique.
        # 
        # This parameter is required.
        self.business_name = business_name
        # The description of the business process.
        self.description = description
        # The Alibaba Cloud account ID of the owner of the business process. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and hover over the user avatar on the right side of the top menu bar to view the account ID. If this parameter is empty, the caller\\"s Alibaba Cloud account ID is used by default.
        self.owner = owner
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace ID.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the workspace name. You must configure either this parameter or ProjectId parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_identifier = project_identifier
        # The module to which the workflow belongs. Valid values:
        # 
        # *   NORMAL: The workflow belongs to auto triggered workflows.
        # *   MANUAL_BIZ: The workflow belongs to manually triggered workflows.
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

