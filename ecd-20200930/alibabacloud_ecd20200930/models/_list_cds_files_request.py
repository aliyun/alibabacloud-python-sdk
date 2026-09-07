# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCdsFilesRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: str = None,
        file_ids: List[str] = None,
        group_id: str = None,
        max_results: int = None,
        next_token: str = None,
        order_type: str = None,
        parent_file_id: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The enterprise cloud drive ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The ID of the user to whom the cloud drive is assigned.
        self.end_user_id = end_user_id
        # The list of file IDs to query.
        self.file_ids = file_ids
        # The team space ID.
        self.group_id = group_id
        # The maximum number of entries per page in a paging query. Default value: 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        # The sort order of the file list.
        self.order_type = order_type
        # The parent file ID. You can obtain this value from the FileId response parameter of this operation.
        self.parent_file_id = parent_file_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        self.region_id = region_id
        # The file status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.file_ids is not None:
            result['FileIds'] = self.file_ids

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.parent_file_id is not None:
            result['ParentFileId'] = self.parent_file_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FileIds') is not None:
            self.file_ids = m.get('FileIds')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ParentFileId') is not None:
            self.parent_file_id = m.get('ParentFileId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

