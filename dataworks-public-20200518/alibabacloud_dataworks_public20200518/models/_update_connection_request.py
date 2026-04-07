# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateConnectionRequest(DaraModel):
    def __init__(
        self,
        connection_id: int = None,
        content: str = None,
        description: str = None,
        env_type: int = None,
        status: str = None,
    ):
        # The data source ID. You can call the [ListConnections](https://help.aliyun.com/document_detail/173911.html) operation to query the ID.
        # 
        # This parameter is required.
        self.connection_id = connection_id
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
        # The description of the data source.
        self.description = description
        # The environment in which the data source is used. Valid values: 0 and 1. The value 0 indicates the development environment. The value 1 indicates the production environment.
        self.env_type = env_type
        # The status of the data source. Valid values: ENABLED and DISABLED. The value ENABLED indicates that the data source is in the normal state. The value DISABLED indicates that the data source is in an abnormal state.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

