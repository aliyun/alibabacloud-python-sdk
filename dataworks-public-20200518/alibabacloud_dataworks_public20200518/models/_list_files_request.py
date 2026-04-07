# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFilesRequest(DaraModel):
    def __init__(
        self,
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
        # The exact matching file name. The file name of the query result is exactly the same as this parameter.
        self.exact_file_name = exact_file_name
        # The path of the folder to which files belong.
        self.file_folder_path = file_folder_path
        # The file ID list. The File ID set of the query result can only be a subset of the list. You can specify up to 50 fileids at a time.
        self.file_id_in = file_id_in
        # The types of the code in the files.
        # 
        # Valid values: 6 (Shell), 10 (ODPS SQL), 11 (ODPS MR), 23 (Data Integration), 24 (ODPS Script), 97 (PAI), 98 (node group), 99 (zero load), 221 (PyODPS 2), 225 (ODPS Spark), 227 (EMR Hive), 228 (EMR Spark), 229 (EMR Spark SQL), 230 (EMR MR), 239 (OSS object inspection), 257 (EMR Shell), 258 (EMR Spark Shell), 259 (EMR Presto), 260 (EMR Impala), 900 (real-time synchronization), 1002 (PAI inner node), 1089 (cross-tenant collaboration), 1091 (Hologres development), 1093 (Hologres SQL), 1100 (assignment), 1106 (for-each), and 1221 (PyODPS 3).
        self.file_types = file_types
        # The keyword in the file names. The keyword is used to perform a fuzzy match. You can specify a keyword to query all files whose names contain the keyword.
        self.keyword = keyword
        # The ID of the Alibaba Cloud account that is used to last modify the file.
        self.last_edit_user = last_edit_user
        # Whether the query result contains the path of the folder where the file is located.
        self.need_absolute_folder_path = need_absolute_folder_path
        # Whether the query results contain file content (for files with more content, there may be a long network transmission delay).
        self.need_content = need_content
        # The ID of the node that is scheduled. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the ID of the node.
        self.node_id = node_id
        # The owner of the files.
        self.owner = owner
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the workspace ID.
        # 
        # You must configure either the ProjectId or ProjectIdentifier parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace Management page to obtain the workspace name.
        # 
        # You must configure either the ProjectId or ProjectIdentifier parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_identifier = project_identifier
        # The module to which the files belong. Valid values:
        # 
        # *   NORMAL: The files are used for DataStudio.
        # *   MANUAL: The files are used for manually triggered nodes.
        # *   MANUAL_BIZ: The files are used for manually triggered workflows.
        # *   SKIP: The files are used for dry-run nodes in DataStudio.
        # *   ADHOCQUERY: The files are used for ad hoc queries.
        # *   COMPONENT: The files are used for snippets.
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

