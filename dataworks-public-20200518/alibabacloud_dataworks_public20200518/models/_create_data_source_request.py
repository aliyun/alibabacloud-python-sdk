# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataSourceRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        data_source_type: str = None,
        description: str = None,
        env_type: int = None,
        name: str = None,
        project_id: int = None,
        sub_type: str = None,
    ):
        # The details of the data source. Examples of details of some common data sources:
        # 
        # *   odps
        # 
        #         {
        #           "accessId": "*****",
        #           "accessKey": "*****",
        #           "authType": 2,
        #           "endpoint": "http://service.odps.aliyun.com/api",
        #           "project": "xsaxsax",
        #           "tag": "public"
        #         }
        # 
        # *   mysql
        # 
        #         {
        #           "database": "xsaxsa",
        #           "instanceName": "rm-xsaxsa",
        #           "password": "xsaxsa",
        #           "rdsOwnerId": "xasxsa",
        #           "regionId": "cn-shanghai",
        #           "tag": "rds",
        #           "username": "xsaxsa"
        #         }
        # 
        # *   rds
        # 
        #         {
        #           "configType": 1,
        #           "tag": "rds",
        #           "database": "xsaxsa",
        #           "username": "xsaxsa",
        #           "password": "xssaxsa$32050",
        #           "instanceName": "rm-xsaxs",
        #           "rdsOwnerId": "11111111"
        #         }
        # 
        # *   oss
        # 
        #         {
        #           "accessId": "*****",
        #           "accessKey": "*****",
        #           "bucket": "xsa-xs-xs",
        #           "endpoint": "http://oss-cn-shanghai.aliyuncs.com",
        #           "tag": "public"
        #         }
        # 
        # *   sqlserver
        # 
        #         {
        #           "jdbcUrl": "jdbc:sqlserver://xsaxsa-xsaxsa.database.xxx.cn:123;DatabaseName=xsxs-xsxs",
        #           "password": "sdasda$fs",
        #           "tag": "public",
        #           "username": "sxaxacdacdd"
        #         }
        # 
        # *   polardb
        # 
        #         {
        #           "clusterId": "pc-sdadsadsa",
        #           "database": "dsadsadsa",
        #           "ownerId": "121212122",
        #           "password": "sdasdafssa",
        #           "region": "cn-shanghai",
        #           "tag": "polardb",
        #           "username": "asdadsads"
        #         }
        # 
        # *   redis
        # 
        #         {    
        #         "password": "xxxxxx",   
        #          "address":"[{\\"host\\":\\"xxxxxxx.redis.rds.aliyuncs.com\\",\\"port\\":6379}]",    
        #         "tag": "public"
        #         }
        # 
        # *   oracle
        # 
        #         {
        #           "jdbcUrl": "jdbc:oracle:saaa:@xxxxx:1521:PROD",
        #           "password": "sxasaxsa",
        #           "tag": "public",
        #           "username": "sasfadfa"
        #         }
        # 
        # *   mongodb
        # 
        #         {
        #           "address": "[\\"xsaxxsa.mongodb.rds.aliyuncs.com:3717\\"]",
        #           "database": "admin",
        #           "password": "sadsda@",
        #           "tag": "public",
        #           "username": "dsadsadas"
        #         }
        # 
        # *   emr
        # 
        #         {
        #           "accessId": "*****",
        #           "emrClusterId": "C-dsads",
        #           "emrResourceQueueName": "default",
        #           "emrEndpoint": "emr.aliyuncs.com",
        #           "accessKey": "*****",
        #           "emrUserId": "224833315798889783",
        #           "name": "sasdsadsa",
        #           "emrAccessMode": "simple",
        #           "region": "cn-shanghai",
        #           "authType": "2",
        #           "emrProjectId": "FP-sdadsad"
        #         }
        # 
        # *   postgresql
        # 
        #         {
        #           "jdbcUrl": "jdbc:postgresql://xxxx:1921/ssss",
        #           "password": "sdadsads",
        #           "tag": "public",
        #           "username": "sdsasda"
        #         }
        # 
        # *   analyticdb_for_mysql
        # 
        #         {
        #           "instanceId": "am-sadsada",
        #           "database": "xsxsx",
        #           "username": "xsxsa",
        #           "password": "asdadsa",
        #           "connectionString": "am-xssxsxs.ads.aliyuncs.com:3306"
        #         }
        # 
        # *   hybriddb_for_postgresql
        # 
        #         {
        #           "connectionString": "gp-xsaxsaxa-master.gpdbmaster.rds.aliyuncs.com",
        #           "database": "xsaxsaxas",
        #           "password": "xsaxsaxsa@11",
        #           "instanceId": "gp-xsaxsaxsa",
        #           "port": "541132",
        #           "ownerId": "xsaxsaxsas",
        #           "username": "sadsad"
        #         }
        # 
        # *   holo
        # 
        #         {
        #           "accessId": "*****",
        #           "accessKey": "*****",
        #           "database": "xsaxsaxsa",
        #           "instanceId": "xsaxa",
        #           "tag": "aliyun"
        #         }
        # 
        # *   kafka
        # 
        #         {
        #           "instanceId": "xsax-cn-xsaxsa",
        #           "regionId": "cn-shanghai",
        #           "tag": "aliyun",
        #           "ownerId": "1212121212112"
        #         }
        # 
        # This parameter is required.
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
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The description of the data source.
        self.description = description
        # The environment in which the data source is used. Valid values: 0 and 1. The value 0 indicates the development environment. The value 1 indicates the production environment.
        # 
        # This parameter is required.
        self.env_type = env_type
        # The name of the data source.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the DataWorks workspace to which the data source belongs. You can call the [ListProjects](https://help.aliyun.com/document_detail/2780068.html) operation to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The subtype of the data source.
        # 
        # *   This parameter takes effect only if you set the DataSourceType parameter to rds.
        # *   If the DataSourceType parameter is set to rds, this parameter can be set to mysql, sqlserver, or postgresql.
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        return self

