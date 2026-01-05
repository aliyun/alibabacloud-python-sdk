# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDataSourcesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDataSourcesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataSourcesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        data_sources: List[main_models.ListDataSourcesResponseBodyPagingInfoDataSources] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The data source groups. Each element in the array indicates a data source group. Each data source group contains data sources in the development environment (if any) and the production environment.
        self.data_sources = data_sources
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.ListDataSourcesResponseBodyPagingInfoDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataSourcesResponseBodyPagingInfoDataSources(DaraModel):
    def __init__(
        self,
        data_source: List[main_models.ListDataSourcesResponseBodyPagingInfoDataSourcesDataSource] = None,
        name: str = None,
        type: str = None,
    ):
        # The data sources. Each element is the information of a single data source with a unique data source ID.
        self.data_source = data_source
        # The name of the data source.
        self.name = name
        # The type of the data source.
        self.type = type

    def validate(self):
        if self.data_source:
            for v1 in self.data_source:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSource'] = []
        if self.data_source is not None:
            for k1 in self.data_source:
                result['DataSource'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source = []
        if m.get('DataSource') is not None:
            for k1 in m.get('DataSource'):
                temp_model = main_models.ListDataSourcesResponseBodyPagingInfoDataSourcesDataSource()
                self.data_source.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataSourcesResponseBodyPagingInfoDataSourcesDataSource(DaraModel):
    def __init__(
        self,
        connection_properties: Any = None,
        connection_properties_mode: str = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        qualified_name: str = None,
    ):
        # The connection configurations of the data source, including the connection address, access identity, and environment information. The envType parameter specifies the environment in which the data source is used. Valid values of the envType parameter:
        # 
        # *   Dev: development environment
        # *   Prod: production environment
        # 
        # The parameters that you need to configure for the data source vary based on the mode in which the data source is added. For more information, see [Data source connection information (ConnectionProperties)](https://help.aliyun.com/document_detail/2852465.html).
        self.connection_properties = connection_properties
        # The mode in which the data source is added. The mode varies based on the data source type. Valid values:
        # 
        # *   InstanceMode: instance mode
        # *   UrlMode: connection string mode
        self.connection_properties_mode = connection_properties_mode
        # The time when the data source was added. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the user who adds the data source.
        self.create_user = create_user
        # The description of the data source.
        self.description = description
        # The ID of the data source.
        self.id = id
        # The time when the data source was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The ID of the user who modifies the data source.
        self.modify_user = modify_user
        # The unique business key of the data source. For example, the unique business key of a Hologres data source is in the `${tenantOwnerId}:${regionId}:${type}:${instanceId}:${database}` format.
        self.qualified_name = qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties

        if self.connection_properties_mode is not None:
            result['ConnectionPropertiesMode'] = self.connection_properties_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')

        if m.get('ConnectionPropertiesMode') is not None:
            self.connection_properties_mode = m.get('ConnectionPropertiesMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        return self

