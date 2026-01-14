# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListFavoriteReportsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.ListFavoriteReportsResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Returns the query result.
        self.result = result
        # Indicates whether the request was successful. Possible values:
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListFavoriteReportsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListFavoriteReportsResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListFavoriteReportsResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # List of works queried.
        self.data = data
        # Page number.
        self.page_num = page_num
        # Number of rows per page set when requesting the interface.
        self.page_size = page_size
        # Total number of rows.
        self.total_num = total_num
        # Total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListFavoriteReportsResponseBodyResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class ListFavoriteReportsResponseBodyResultData(DaraModel):
    def __init__(
        self,
        favorite: bool = None,
        favorite_date: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        has_edit_auth: bool = None,
        has_view_auth: bool = None,
        name: str = None,
        owner_name: str = None,
        owner_num: str = None,
        publish_status: int = None,
        tree_id: str = None,
        type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # Indicates whether the user has favorited the work.
        self.favorite = favorite
        # The timestamp when the work was favorited.
        self.favorite_date = favorite_date
        # Timestamp of the work creation.
        self.gmt_create = gmt_create
        # Timestamp of the work modification.
        self.gmt_modified = gmt_modified
        # Indicates whether the user has edit permission for the work.
        self.has_edit_auth = has_edit_auth
        # Check if the user has the permission to view the work.
        self.has_view_auth = has_view_auth
        # Name of the work.
        self.name = name
        # Alibaba Cloud account name of the work owner.
        self.owner_name = owner_name
        # UserID of the work owner.
        self.owner_num = owner_num
        # Publication status of the work. Value range:
        # - 0: Not published
        # - 1: Published
        # - 2: Saved with modifications, not published
        # - 3: Offline
        self.publish_status = publish_status
        # Work ID.
        self.tree_id = tree_id
        # Type of the work. Value range:
        # - DATAPRODUCT: Data Portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        self.type = type
        # The ID of the workspace to which the work belongs.
        self.workspace_id = workspace_id
        # The name of the workspace to which the work belongs.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.favorite is not None:
            result['Favorite'] = self.favorite

        if self.favorite_date is not None:
            result['FavoriteDate'] = self.favorite_date

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.has_edit_auth is not None:
            result['HasEditAuth'] = self.has_edit_auth

        if self.has_view_auth is not None:
            result['HasViewAuth'] = self.has_view_auth

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_num is not None:
            result['OwnerNum'] = self.owner_num

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.tree_id is not None:
            result['TreeId'] = self.tree_id

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')

        if m.get('FavoriteDate') is not None:
            self.favorite_date = m.get('FavoriteDate')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HasEditAuth') is not None:
            self.has_edit_auth = m.get('HasEditAuth')

        if m.get('HasViewAuth') is not None:
            self.has_view_auth = m.get('HasViewAuth')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerNum') is not None:
            self.owner_num = m.get('OwnerNum')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('TreeId') is not None:
            self.tree_id = m.get('TreeId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

