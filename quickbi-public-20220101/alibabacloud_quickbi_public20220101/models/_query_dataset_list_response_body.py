# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryDatasetListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryDatasetListResponseBodyResult = None,
        success: bool = None,
    ):
        # The keyword used to search for the dataset name.
        self.request_id = request_id
        # Test dataset
        self.result = result
        # Whether to recursively wrap the dataset in the subdirectory. Valid values:
        # 
        # *   true: returns datasets in all recursive subdirectories in the directoryId directory.
        # *   false: Only datasets in the directory specified by directoryId are returned, excluding subdirectories.
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
            temp_model = main_models.QueryDatasetListResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDatasetListResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryDatasetListResponseBodyResultData] = None,
        page_num: int = None,
        page_size: int = None,
        total_num: int = None,
        total_pages: int = None,
    ):
        # Returns the pagination results of the dataset list. The detailed information of the dataset list is stored in the response parameter Data.
        self.data = data
        # The number of rows per page in a paged query.
        # 
        # *   Default value: 10.
        # *   Maximum value: 1,000.
        self.page_num = page_num
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.page_size = page_size
        # The ID of the request.
        self.total_num = total_num
        # Current page number for dataset list:
        # 
        # *   Pages start from page 1.
        # *   Default value: 1.
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
                temp_model = main_models.QueryDatasetListResponseBodyResultData()
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

class QueryDatasetListResponseBodyResultData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_source: main_models.QueryDatasetListResponseBodyResultDataDataSource = None,
        dataset_id: str = None,
        dataset_name: str = None,
        description: str = None,
        directory: main_models.QueryDatasetListResponseBodyResultDataDirectory = None,
        modify_time: str = None,
        open_offline_acceleration: bool = None,
        owner_id: str = None,
        owner_name: str = None,
        row_level: bool = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The details of the dataset list.
        self.create_time = create_time
        # Test Space
        self.data_source = data_source
        # The name of the workspace.
        self.dataset_id = dataset_id
        # Tom
        self.dataset_name = dataset_name
        # The number of rows per page set when the interface is requested.
        self.description = description
        # The information about the data source to which the dataset belongs.
        self.directory = directory
        # The nickname of the dataset owner.
        self.modify_time = modify_time
        self.open_offline_acceleration = open_offline_acceleration
        # The creation time.
        self.owner_id = owner_id
        # Whether to enable row-level permissions. Valid values:
        # 
        # *   true: The VIP Netty channel is enabled.
        # *   false: The incremental log backup feature is disabled.
        self.owner_name = owner_name
        # The total number of pages returned.
        self.row_level = row_level
        # The page number of the returned page.
        self.workspace_id = workspace_id
        # The description of the dataset.
        self.workspace_name = workspace_name

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.directory:
            self.directory.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.open_offline_acceleration is not None:
            result['OpenOfflineAcceleration'] = self.open_offline_acceleration

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.row_level is not None:
            result['RowLevel'] = self.row_level

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSource') is not None:
            temp_model = main_models.QueryDatasetListResponseBodyResultDataDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            temp_model = main_models.QueryDatasetListResponseBodyResultDataDirectory()
            self.directory = temp_model.from_map(m.get('Directory'))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('OpenOfflineAcceleration') is not None:
            self.open_offline_acceleration = m.get('OpenOfflineAcceleration')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('RowLevel') is not None:
            self.row_level = m.get('RowLevel')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

class QueryDatasetListResponseBodyResultDataDirectory(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        path_id: str = None,
        path_name: str = None,
    ):
        # The ID of the directory path.
        self.id = id
        # The ID of the data source.
        self.name = name
        # The type of the data source.
        self.path_id = path_id
        # The name of the data source.
        self.path_name = path_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.path_id is not None:
            result['PathId'] = self.path_id

        if self.path_name is not None:
            result['PathName'] = self.path_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathId') is not None:
            self.path_id = m.get('PathId')

        if m.get('PathName') is not None:
            self.path_name = m.get('PathName')

        return self

class QueryDatasetListResponseBodyResultDataDataSource(DaraModel):
    def __init__(
        self,
        ds_id: str = None,
        ds_name: str = None,
        ds_type: str = None,
    ):
        # The ID of the training dataset that you want to remove from the specified custom linguistic model.
        self.ds_id = ds_id
        # The time when the scaling group was modified.
        self.ds_name = ds_name
        # The user ID of the dataset owner in the Quick BI.
        self.ds_type = ds_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.ds_name is not None:
            result['DsName'] = self.ds_name

        if self.ds_type is not None:
            result['DsType'] = self.ds_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('DsName') is not None:
            self.ds_name = m.get('DsName')

        if m.get('DsType') is not None:
            self.ds_type = m.get('DsType')

        return self

