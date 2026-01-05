# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFilesRequest(DaraModel):
    def __init__(
        self,
        commit_status: int = None,
        exact_file_name: str = None,
        file_folder_path: str = None,
        file_id_in: str = None,
        file_types: str = None,
        keyword: str = None,
        last_edit_user: str = None,
        need_absolute_folder_path: bool = None,
        need_content: bool = None,
        node_id: int = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        project_identifier: str = None,
        use_type: str = None,
    ):
        # The current commit status of the file. Valid values: 0 (the latest code is not committed) and 1 (the latest code is committed).
        self.commit_status = commit_status
        # The exact file name. The file name in the query result must exactly match this parameter.
        self.exact_file_name = exact_file_name
        # The path to the folder where the file is located.
        self.file_folder_path = file_folder_path
        # The list of file IDs. The file IDs in the query result must be a subset of this list. You can specify up to 50 file IDs at a time.
        self.file_id_in = file_id_in
        # The code type of the file.
        # 
        # The code type of the file. Common code types and their corresponding file types include: 6 (Shell), 10 (ODPS SQL), 11 (ODPS MR), 23 (Data Integration), 24 (ODPS Script), 97 (PAI), 98 (Combined node), 99 (Virtual node), 221 (PyODPS 2), 225 (ODPS Spark), 227 (EMR Hive), 228 (EMR Spark), 229 (EMR Spark SQL), 230 (EMR MR), 239 (OSS object inspection), 257 (EMR Shell), 258 (EMR Spark Shell), 259 (EMR Presto), 260 (EMR Impala), 900 (Real-time sync), 1002 (PAI internal node), 1089 (Cross-tenant node), 1091 (Hologres development), 1093 (Hologres SQL), 1100 (Assignment node), 1106 (ForEach node), 1221 (PyODPS 3).
        self.file_types = file_types
        # The keyword for the file name. Fuzzy match is supported. You can enter a keyword to query all files that contain the keyword.
        self.keyword = keyword
        # The Alibaba Cloud account ID of the user who last updated the file.
        self.last_edit_user = last_edit_user
        # Specifies whether the query result includes the path to the folder where the file is located.
        self.need_absolute_folder_path = need_absolute_folder_path
        # Specifies whether the query result includes the file content. For files with large content, network transmission delays may occur.
        self.need_content = need_content
        # The ID of the scheduling node. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to obtain the node ID.
        self.node_id = node_id
        # The ID of the file owner.
        self.owner = owner
        # The page number for pagination.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the ID.
        # 
        # You must configure either this parameter or the ProjectIdentifier parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_id = project_id
        # The DataWorks workspace name. To obtain the workspace name, log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and navigate to the workspace configuration page.
        # 
        # You must specify either this parameter or ProjectId to identify the target DataWorks workspace for this API call.
        self.project_identifier = project_identifier
        # The functional module to which the file belongs. Valid values:
        # 
        # *   NORMAL: Data Studio
        # *   MANUAL: Manually triggered node
        # *   MANUAL_BIZ: Manually triggered workflow
        # *   SKIP: Dry-run scheduling in Data Studio
        # *   ADHOCQUERY: Ad hoc query
        # *   COMPONENT: Component management
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commit_status is not None:
            result['CommitStatus'] = self.commit_status

        if self.exact_file_name is not None:
            result['ExactFileName'] = self.exact_file_name

        if self.file_folder_path is not None:
            result['FileFolderPath'] = self.file_folder_path

        if self.file_id_in is not None:
            result['FileIdIn'] = self.file_id_in

        if self.file_types is not None:
            result['FileTypes'] = self.file_types

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.last_edit_user is not None:
            result['LastEditUser'] = self.last_edit_user

        if self.need_absolute_folder_path is not None:
            result['NeedAbsoluteFolderPath'] = self.need_absolute_folder_path

        if self.need_content is not None:
            result['NeedContent'] = self.need_content

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        if self.use_type is not None:
            result['UseType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitStatus') is not None:
            self.commit_status = m.get('CommitStatus')

        if m.get('ExactFileName') is not None:
            self.exact_file_name = m.get('ExactFileName')

        if m.get('FileFolderPath') is not None:
            self.file_folder_path = m.get('FileFolderPath')

        if m.get('FileIdIn') is not None:
            self.file_id_in = m.get('FileIdIn')

        if m.get('FileTypes') is not None:
            self.file_types = m.get('FileTypes')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('LastEditUser') is not None:
            self.last_edit_user = m.get('LastEditUser')

        if m.get('NeedAbsoluteFolderPath') is not None:
            self.need_absolute_folder_path = m.get('NeedAbsoluteFolderPath')

        if m.get('NeedContent') is not None:
            self.need_content = m.get('NeedContent')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        if m.get('UseType') is not None:
            self.use_type = m.get('UseType')

        return self

