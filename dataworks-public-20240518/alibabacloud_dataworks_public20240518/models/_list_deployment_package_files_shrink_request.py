# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeploymentPackageFilesShrinkRequest(DaraModel):
    def __init__(
        self,
        business_id: int = None,
        change_type: int = None,
        commit_from: str = None,
        commit_to: str = None,
        commit_user_id: str = None,
        file_ids_shrink: str = None,
        file_name: str = None,
        file_type: int = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        solution_id: int = None,
    ):
        # The workflow ID. You can call the [ListBusiness](https://help.aliyun.com/document_detail/173945.html) operation to query the workflow ID by name.
        self.business_id = business_id
        # The change type. Valid values:
        # 
        # *   0: addition
        # *   1: update
        # *   2: deletion
        self.change_type = change_type
        # The start date for committing. Specify the date in the yyyy-MM-dd format.
        self.commit_from = commit_from
        # The end date (included) for committing. Specify the date in the yyyy-MM-dd format.
        self.commit_to = commit_to
        # The ID of the user who commits the file.
        self.commit_user_id = commit_user_id
        # The IDs of the files to be queried.
        self.file_ids_shrink = file_ids_shrink
        # The name of the file.
        self.file_name = file_name
        # The type of the code for the file.
        # 
        # The code for files varies based on the file type. For more information, see [DataWorks nodes](https://help.aliyun.com/document_detail/600169.html). You can call the [ListFileType](https://help.aliyun.com/document_detail/212428.html) operation to query the type of the code for the file.
        self.file_type = file_type
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The solution ID.
        self.solution_id = solution_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.commit_from is not None:
            result['CommitFrom'] = self.commit_from

        if self.commit_to is not None:
            result['CommitTo'] = self.commit_to

        if self.commit_user_id is not None:
            result['CommitUserId'] = self.commit_user_id

        if self.file_ids_shrink is not None:
            result['FileIds'] = self.file_ids_shrink

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('CommitFrom') is not None:
            self.commit_from = m.get('CommitFrom')

        if m.get('CommitTo') is not None:
            self.commit_to = m.get('CommitTo')

        if m.get('CommitUserId') is not None:
            self.commit_user_id = m.get('CommitUserId')

        if m.get('FileIds') is not None:
            self.file_ids_shrink = m.get('FileIds')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')

        return self

