# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListConnectionsResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The query results for data sources that are returned on multiple pages.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.ListConnectionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListConnectionsResponseBodyData(DaraModel):
    def __init__(
        self,
        connections: List[main_models.ListConnectionsResponseBodyDataConnections] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The data sources.
        self.connections = connections
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of data sources returned.
        self.total_count = total_count

    def validate(self):
        if self.connections:
            for v1 in self.connections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connections'] = []
        if self.connections is not None:
            for k1 in self.connections:
                result['Connections'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k1 in m.get('Connections'):
                temp_model = main_models.ListConnectionsResponseBodyDataConnections()
                self.connections.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListConnectionsResponseBodyDataConnections(DaraModel):
    def __init__(
        self,
        binding_calc_engine_id: int = None,
        connect_status: int = None,
        connection_type: str = None,
        content: str = None,
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
        # The ID of the compute engine with which the data source is associated.
        self.binding_calc_engine_id = binding_calc_engine_id
        # The status of the data source. Valid values:
        # 
        # *   1: The data source is normal.
        # *   2: The data source is disabled.
        self.connect_status = connect_status
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
        self.connection_type = connection_type
        # The details of the data source. Examples of details of some common data sources:
        # 
        # *   odps
        # 
        # <!---->
        # 
        #     {
        #       "accessId": "xssssss",
        #       "accessKey": "xsaxsaxsa",
        #       "authType": 2,
        #       "endpoint": "http://service.odps.aliyun.com/api",
        #       "project": "xsaxsax",
        #       "tag": "public"
        #     }
        # 
        # *   mysql
        # 
        # <!---->
        # 
        #     {
        #       "database": "xsaxsa",
        #       "instanceName": "rm-xsaxsa",
        #       "password": "xsaxsa",
        #       "rdsOwnerId": "xasxsa",
        #       "regionId": "cn-shanghai",
        #       "tag": "rds",
        #       "username": "xsaxsa"
        #     }
        # 
        # *   rds
        # 
        # <!---->
        # 
        #     {
        #       "configType": 1,
        #       "tag": "rds",
        #       "database": "xsaxsa",
        #       "username": "xsaxsa",
        #       "password": "xssaxsa$32050",
        #       "instanceName": "rm-xsaxs",
        #       "rdsOwnerId": "11111111"
        #     }
        # 
        # *   oss
        # 
        # <!---->
        # 
        #     {
        #       "accessId": "sssssxx",
        #       "accessKey": "xsaxaxsaxs",
        #       "bucket": "xsa-xs-xs",
        #       "endpoint": "http://oss-cn-shanghai.aliyuncs.com",
        #       "tag": "public"
        #     }
        # 
        # *   sqlserver
        # 
        # <!---->
        # 
        #     {
        #       "jdbcUrl": "jdbc:sqlserver://xsaxsa-xsaxsa.database.xxx.cn:123;DatabaseName=xsxs-xsxs",
        #       "password": "sdasda$fs",
        #       "tag": "public",
        #       "username": "sxaxacdacdd"
        #     }
        # 
        # *   polardb
        # 
        # <!---->
        # 
        #     {
        #       "clusterId": "pc-sdadsadsa",
        #       "database": "dsadsadsa",
        #       "ownerId": "121212122",
        #       "password": "sdasdafssa",
        #       "region": "cn-shanghai",
        #       "tag": "polardb",
        #       "username": "asdadsads"
        #     }
        # 
        # *   oracle
        # 
        # <!---->
        # 
        #     {
        #       "jdbcUrl": "jdbc:oracle:saaa:@xxxxx:1521:PROD",
        #       "password": "sxasaxsa",
        #       "tag": "public",
        #       "username": "sasfadfa"
        #     }
        # 
        # *   mongodb
        # 
        # <!---->
        # 
        #     {
        #       "address": "[\\"xsaxxsa.mongodb.rds.aliyuncs.com:3717\\"]",
        #       "database": "admin",
        #       "password": "sadsda@",
        #       "tag": "public",
        #       "username": "dsadsadas"
        #     }
        # 
        # *   emr
        # 
        # <!---->
        # 
        #     {
        #       "accessId": "xsaxsa",
        #       "emrClusterId": "C-dsads",
        #       "emrResourceQueueName": "default",
        #       "emrEndpoint": "emr.aliyuncs.com",
        #       "accessKey": "dsadsad",
        #       "emrUserId": "224833315798889783",
        #       "name": "sasdsadsa",
        #       "emrAccessMode": "simple",
        #       "region": "cn-shanghai",
        #       "authType": "2",
        #       "emrProjectId": "FP-sdadsad"
        #     }
        # 
        # *   postgresql
        # 
        # <!---->
        # 
        #     {
        #       "jdbcUrl": "jdbc:postgresql://xxxx:1921/ssss",
        #       "password": "sdadsads",
        #       "tag": "public",
        #       "username": "sdsasda"
        #     }
        # 
        # *   analyticdb_for_mysql
        # 
        # <!---->
        # 
        #     {
        #       "instanceId": "am-sadsada",
        #       "database": "xsxsx",
        #       "username": "xsxsa",
        #       "password": "asdadsa",
        #       "connectionString": "am-xssxsxs.ads.aliyuncs.com:3306"
        #     }
        # 
        # *   hybriddb_for_postgresql
        # 
        # <!---->
        # 
        #     {
        #       "connectionString": "gp-xsaxsaxa-master.gpdbmaster.rds.aliyuncs.com",
        #       "database": "xsaxsaxas",
        #       "password": "xsaxsaxsa@11",
        #       "instanceId": "gp-xsaxsaxsa",
        #       "port": "541132",
        #       "ownerId": "xsaxsaxsas",
        #       "username": "sadsad"
        #     }
        # 
        # *   holo
        # 
        # <!---->
        # 
        #     {
        #       "accessId": "xsaxsaxs",
        #       "accessKey": "xsaxsaxsa",
        #       "database": "xsaxsaxsa",
        #       "instanceId": "xsaxa",
        #       "tag": "aliyun"
        #     }
        # 
        # *   kafka
        # 
        # <!---->
        # 
        #     {
        #       "instanceId": "xsax-cn-xsaxsa",
        #       "regionId": "cn-shanghai",
        #       "tag": "aliyun",
        #       "ownerId": "1212121212112"
        #     }
        self.content = content
        # Indicates whether the compute engine that is associated with the data source is the default compute engine used by data sources of the same type.
        self.default_engine = default_engine
        # The description of the data source.
        self.description = description
        # The environment in which the data source is used. Valid values:
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
        # The ID of the Alibaba Cloud account that is used to last modify the data source.
        self.operator = operator
        # The ID of the workspace with which the data source is associated.
        self.project_id = project_id
        # The field that is used to sort data sources. Data sources are sorted in descending order based on the value of this parameter.
        self.sequence = sequence
        # Indicates whether the data source is a shared data source.
        self.shared = shared
        # The status of the data source. Valid values:
        # 
        # *   1: The data source is normal.
        # *   2: The data source is disabled.
        self.status = status
        # The subtype of the data source. This parameter is used in scenarios where a type includes subtypes. The following type and subtypes are supported:
        # 
        # *   Type: `rds`
        # *   Subtypes: `mysql`, `sqlserver`, and `postgresql`.
        self.sub_type = sub_type
        # The tenant ID.
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

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.content is not None:
            result['Content'] = self.content

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

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('Content') is not None:
            self.content = m.get('Content')

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

