# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveCdsFileRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        conflict_policy: str = None,
        end_user_id: str = None,
        file_id: str = None,
        group_id: str = None,
        parent_folder_id: str = None,
        region_id: str = None,
    ):
        # The enterprise cloud disk ID.
        self.cds_id = cds_id
        # The policy for handling files with the same name.
        self.conflict_policy = conflict_policy
        # The ID of the user who uses the cloud disk.
        self.end_user_id = end_user_id
        # The file ID. You can call [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) to query the ID of the file.
        self.file_id = file_id
        # The team space ID.
        self.group_id = group_id
        # The ID of the parent folder at the destination. You can call [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) to query the ID of the file. Set this parameter to `root` if you want to move the file to the root directory.
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
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.conflict_policy is not None:
            result['ConflictPolicy'] = self.conflict_policy

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('ConflictPolicy') is not None:
            self.conflict_policy = m.get('ConflictPolicy')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

