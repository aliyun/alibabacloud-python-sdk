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
        # Specifies whether to automatically rename the file when a file with the same name exists in the destination folder.
        self.auto_rename = auto_rename
        # The enterprise cloud drive ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The ID of the user who is logged on to the cloud drive.
        self.end_user_id = end_user_id
        # The file ID. You can call [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) to query the ID of the file.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the personal drive (which can be obtained from the `UserId` response parameter of the [DescribeCloudDriveUsers](https://help.aliyun.com/document_detail/2357237.html) operation) or the team space ID (which can be obtained from the `GroupId` response parameter of the [DescribeCloudDriveGroups](https://help.aliyun.com/document_detail/609896.html) operation) at the copy destination.
        # > If both `FileReceiverId` and `FileReceiverType` are empty, the file is copied to the personal drive where the file currently resides by default.
        self.file_receiver_id = file_receiver_id
        # The type of space to which the file belongs.
        self.file_receiver_type = file_receiver_type
        # The team space ID.
        self.group_id = group_id
        # The ID of the parent folder at the copy destination. You can call [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) to query the ID of the folder. Set this parameter to `root` if you want to copy the file to the root directory.
        # 
        # This parameter is required.
        self.parent_folder_id = parent_folder_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
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

