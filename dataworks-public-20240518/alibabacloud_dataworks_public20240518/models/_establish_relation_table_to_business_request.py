# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EstablishRelationTableToBusinessRequest(DaraModel):
    def __init__(
        self,
        business_id: str = None,
        folder_id: str = None,
        project_id: int = None,
        project_identifier: str = None,
        table_guid: str = None,
    ):
        # The workflow ID. You can call the [ListBusiness](https://help.aliyun.com/document_detail/173945.html) operation to obtain the workflow ID.
        # 
        # This parameter is required.
        self.business_id = business_id
        # The ID of the folder. You can call the [GetFolder](https://help.aliyun.com/document_detail/173952.html) or [ListFolders](https://help.aliyun.com/document_detail/173955.html) operation to obtain the folder ID.
        self.folder_id = folder_id
        # The ID of the DataWorks workspace. You can click the wrench icon in the top-right corner to access the workspace management page and view the ID.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace. This is the identifier shown in the workspace switcher at the top of the Data Studio page.
        # 
        # Either this parameter or ProjectId must be specified to determine which DataWorks workspace this API call operates on.
        self.project_identifier = project_identifier
        # The UUID of the table. You can call the [SearchMetaTables](https://help.aliyun.com/document_detail/173919.html) operation to obtain the table UUID.
        # 
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

