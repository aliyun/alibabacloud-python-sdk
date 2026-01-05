# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBusinessRequest(DaraModel):
    def __init__(
        self,
        business_id: int = None,
        business_name: str = None,
        description: str = None,
        owner: str = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # The workflow ID.
        # 
        # You can call the [ListBusiness](https://help.aliyun.com/document_detail/173945.html) operation to query the ID.
        # 
        # This parameter is required.
        self.business_id = business_id
        # The name of the workflow.
        # 
        # You can call the [ListBusiness](https://help.aliyun.com/document_detail/173945.html) operation to query the name.
        self.business_name = business_name
        # The description of the workflow.
        self.description = description
        # The owner of the workflow.
        # 
        # You can call the [ListBusiness](https://help.aliyun.com/document_detail/173945.html) operation to query the owner.
        self.owner = owner
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/workspace/list) and go to the Workspace page to obtain the workspace ID. You must configure either this parameter or the `ProjectIdentifier` parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://dataworks.console.aliyun.com/workspace/list) and go to the Workspace page to obtain the name. You must configure either this parameter or the `ProjectId` parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_identifier = project_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['BusinessId'] = self.business_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

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

        return self

