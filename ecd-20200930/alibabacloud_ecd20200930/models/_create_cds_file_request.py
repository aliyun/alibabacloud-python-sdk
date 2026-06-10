# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCdsFileRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        conflict_policy: str = None,
        end_user_id: str = None,
        file_hash: str = None,
        file_length: int = None,
        file_name: str = None,
        file_type: str = None,
        group_id: str = None,
        parent_file_id: str = None,
        region_id: str = None,
    ):
        # Enterprise cloud disk ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # How to handle files with the same name.
        self.conflict_policy = conflict_policy
        # User ID.
        self.end_user_id = end_user_id
        # SHA-1 hash value of the file.
        self.file_hash = file_hash
        # File size. Unit: Byte.
        # 
        # This parameter is required.
        self.file_length = file_length
        # File name.
        # 
        # This parameter is required.
        self.file_name = file_name
        # File type.
        # 
        # This parameter is required.
        self.file_type = file_type
        # Team space ID.
        self.group_id = group_id
        # Parent file ID. Get this from the `FileId` parameter returned by the [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) API.
        self.parent_file_id = parent_file_id
        # Region ID. Call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to list regions supported by WUYING Workspace.
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

        if self.file_hash is not None:
            result['FileHash'] = self.file_hash

        if self.file_length is not None:
            result['FileLength'] = self.file_length

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.parent_file_id is not None:
            result['ParentFileId'] = self.parent_file_id

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

        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')

        if m.get('FileLength') is not None:
            self.file_length = m.get('FileLength')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ParentFileId') is not None:
            self.parent_file_id = m.get('ParentFileId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

