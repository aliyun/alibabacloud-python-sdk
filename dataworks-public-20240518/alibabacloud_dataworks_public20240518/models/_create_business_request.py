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
        # The name of the business process. The name must be unique within the same workspace.
        # 
        # This parameter is required.
        self.business_name = business_name
        # The description of the business process.
        self.description = description
        # The Alibaba Cloud account ID of the owner of the business process. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and hover over the profile picture in the upper-right corner of the top navigation bar to view the account ID. If this parameter is left empty, the Alibaba Cloud account ID of the caller is used by default.
        self.owner = owner
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace management page to view the ID.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace, which is the English identifier displayed in the workspace switcher at the top of the DataStudio page. You must specify either this parameter or ProjectId to determine the DataWorks workspace on which the API operation is performed.
        self.project_identifier = project_identifier
        # The functional module to which the business process belongs. Valid values:
        # 
        # - NORMAL: DataStudio.
        # - MANUAL_BIZ: Manual business process.
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

