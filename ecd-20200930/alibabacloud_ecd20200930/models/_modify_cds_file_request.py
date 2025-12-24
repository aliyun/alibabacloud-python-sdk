# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCdsFileRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        conflict_policy: str = None,
        end_user_id: str = None,
        file_id: str = None,
        file_name: str = None,
        group_id: str = None,
        region_id: str = None,
    ):
        # The enterprise drive ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The processing policy when a file with the same name appears.
        # 
        # Valid values:
        # 
        # *   refuse: If you want to create a file that uses the same name as an existing file in the cloud, the system denies your request and returns the details of the existing file.
        # *   auto_rename: automatically renames a file if the file has the same name as an existing file in the cloud. By default, the current point in time is appended to the end of the original file name. Example: xxx20240102_150405.
        # *   ignore: allows the file to be with the same name.
        # *   over_write: After you create a file that uses the same name as an existing file in the cloud, the new file overwrites the existing file.
        self.conflict_policy = conflict_policy
        # The ID of the user who uses the network disk.
        self.end_user_id = end_user_id
        # The ID of the file. You can call the [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) operation to query the ID of the file.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The name of the file.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The ID of the team space.
        self.group_id = group_id
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
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

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

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

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

