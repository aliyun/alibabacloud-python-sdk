# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ExportDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ExportDataSourcesResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the exported data sources.
        self.data = data
        # The HTTP status code returned. Valid values:
        # 
        # *   200: The request was successful.
        # *   Other values: The request failed. You can troubleshoot issues based on the HTTP status code returned.
        self.http_status_code = http_status_code
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ExportDataSourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ExportDataSourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        data_sources: List[main_models.ExportDataSourcesResponseBodyDataDataSources] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The details of the exported data sources. The value is an array. The following parameters are the elements in the array. The sample values of these parameters show the details of a sample data source.
        self.data_sources = data_sources
        # The page number. Pages start from page 1.
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
                temp_model = main_models.ExportDataSourcesResponseBodyDataDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ExportDataSourcesResponseBodyDataDataSources(DaraModel):
    def __init__(
        self,
        binding_calc_engine_id: int = None,
        connect_status: int = None,
        content: str = None,
        data_source_type: str = None,
        default_engine: bool = None,
        description: str = None,
        env_type: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        operator: str = None,
        project_id: int = None,
        sequence: int = None,
        shared: bool = None,
        status: int = None,
        sub_type: str = None,
        tenant_id: int = None,
    ):
        # The ID of the compute engine that is added as the data source.
        self.binding_calc_engine_id = binding_calc_engine_id
        # Indicates whether the data source is connected to an exclusive resource group. Valid values:
        # 
        # *   1: The data source is connected to at least one exclusive resource group.
        # *   0: The data source is not connected to any exclusive resource group.
        self.connect_status = connect_status
        # The configuration of the data source.
        self.content = content
        # The type of the data source. Valid values:
        # 
        # *   odps
        # *   mysql
        # *   rds
        # *   oss
        # *   sqlserver
        # *   polardb
        # *   oracle
        # *   mongodb
        # *   emr
        # *   postgresql
        # *   analyticdb_for_mysql
        # *   hybriddb_for_postgresql
        # *   holo
        self.data_source_type = data_source_type
        # Indicates whether the compute engine that is added as the data source is the default compute engine. Valid values:
        # 
        # *   true: The compute engine is the default compute engine.
        # *   false: The compute engine is not the default compute engine.
        self.default_engine = default_engine
        # The description of the data source.
        self.description = description
        # The environment in which the data source resides. Valid values:
        # 
        # *   0: development environment
        # *   1: production environment
        self.env_type = env_type
        # The time when the data source was created. Example: Mar 17, 2021 4:09:32 PM.
        self.gmt_create = gmt_create
        # The time when the data source was last modified. Example: Mar 17, 2021 4:09:32 PM.
        self.gmt_modified = gmt_modified
        # The data source ID.
        self.id = id
        # The name of the data source.
        self.name = name
        # The ID of the user who exported the data source.
        self.operator = operator
        # The ID of the DataWorks workspace to which the data source belongs.
        self.project_id = project_id
        # The sequence number of the data source.
        self.sequence = sequence
        # Indicates whether the data source can be shared. Valid values:
        # 
        # *   true: The data source can be shared.
        # *   false: The data source cannot be shared.
        self.shared = shared
        # Indicates whether the data source is available. Valid values:
        # 
        # *   1: The data source is available.
        # *   0: The data source is unavailable.
        self.status = status
        # The subtype of the data source. This parameter takes effect only when the DataSourceType parameter is set to rds.
        # 
        # If the value of the DataSourceType parameter is rds, the value of this parameter can be mysql, sqlserver, or postgresql.
        self.sub_type = sub_type
        # The ID of the Alibaba Cloud account to which the data source belongs.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_calc_engine_id is not None:
            result['BindingCalcEngineId'] = self.binding_calc_engine_id

        if self.connect_status is not None:
            result['ConnectStatus'] = self.connect_status

        if self.content is not None:
            result['Content'] = self.content

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.default_engine is not None:
            result['DefaultEngine'] = self.default_engine

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sequence is not None:
            result['Sequence'] = self.sequence

        if self.shared is not None:
            result['Shared'] = self.shared

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingCalcEngineId') is not None:
            self.binding_calc_engine_id = m.get('BindingCalcEngineId')

        if m.get('ConnectStatus') is not None:
            self.connect_status = m.get('ConnectStatus')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DefaultEngine') is not None:
            self.default_engine = m.get('DefaultEngine')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')

        if m.get('Shared') is not None:
            self.shared = m.get('Shared')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

