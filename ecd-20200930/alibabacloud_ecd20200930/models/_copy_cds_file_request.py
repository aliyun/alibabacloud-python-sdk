# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyCdsFileRequest(DaraModel):
    def __init__(
        self,
        auto_rename: bool = None,
        cds_id: str = None,
        end_user_id: str = None,
        file_id: str = None,
        file_receiver_id: str = None,
        file_receiver_type: str = None,
        group_id: str = None,
        parent_folder_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether to automatically rename the file if a file that has the same name exists in the folder to which you want to copy the file. Default value: false.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.auto_rename = auto_rename
        # The ID of the cloud disk.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The user ID that you want to use to access the cloud disk.
        self.end_user_id = end_user_id
        # The file ID. You can call the CreateCdsFile operation to query the file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # 目标复制文件所在的个人空间ID（即UserId，您可以在DescribeCloudDriveUsers接口返回的报文中获取。）或者目标复制文件所在的团队空间ID（即GroupId，您可以在DescribeCloudDriveGroups接口返回的报文中获取。）
        # > FileReceiverId和FileReceiverType都为空时，默认复制到文件所在的个人空间。
        # >
        self.file_receiver_id = file_receiver_id
        # 文件所属的空间类型。
        self.file_receiver_type = file_receiver_type
        self.group_id = group_id
        # The ID of the parent folder of the folder to which you want to copy the file. If you want to copy the file to the root directory, set this parameter to root.
        # 
        # This parameter is required.
        self.parent_folder_id = parent_folder_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_rename is not None:
            result['AutoRename'] = self.auto_rename

        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_receiver_id is not None:
            result['FileReceiverId'] = self.file_receiver_id

        if self.file_receiver_type is not None:
            result['FileReceiverType'] = self.file_receiver_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRename') is not None:
            self.auto_rename = m.get('AutoRename')

        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileReceiverId') is not None:
            self.file_receiver_id = m.get('FileReceiverId')

        if m.get('FileReceiverType') is not None:
            self.file_receiver_type = m.get('FileReceiverType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

