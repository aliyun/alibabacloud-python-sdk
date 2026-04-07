# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgRunSensIdentifyRequest(DaraModel):
    def __init__(
        self,
        es_meta_params: List[main_models.DsgRunSensIdentifyRequestEsMetaParams] = None,
        tenant_id: str = None,
    ):
        # The parameters that you need to configure to scan specified metadata.
        self.es_meta_params = es_meta_params
        # The tenant ID. To obtain the tenant ID, perform the following steps: Log on to the [DataWorks console](https://workbench.data.aliyun.com/console). Find your workspace and go to the DataStudio page. On the DataStudio page, click the logon username in the upper-right corner and click User Info in the Menu section.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        if self.es_meta_params:
            for v1 in self.es_meta_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EsMetaParams'] = []
        if self.es_meta_params is not None:
            for k1 in self.es_meta_params:
                result['EsMetaParams'].append(k1.to_map() if k1 else None)

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.es_meta_params = []
        if m.get('EsMetaParams') is not None:
            for k1 in m.get('EsMetaParams'):
                temp_model = main_models.DsgRunSensIdentifyRequestEsMetaParams()
                self.es_meta_params.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class DsgRunSensIdentifyRequestEsMetaParams(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_type: str = None,
        instance_id: int = None,
        project_name: str = None,
        schema_name: str = None,
        table_name: str = None,
        table_name_list: List[str] = None,
        user: str = None,
    ):
        # The cluster ID. You can obtain the ID based on the data source you use.
        self.cluster_id = cluster_id
        # The type of the data source. Valid values:
        # 
        # *   ODPS.ODPS
        # *   EMR
        # *   HOLO.POSTGRES
        self.db_type = db_type
        # The instance ID. You can obtain the ID based on the data source you use.
        self.instance_id = instance_id
        # The name of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the name.
        self.project_name = project_name
        # The name of the schema.
        self.schema_name = schema_name
        # The name of the table.
        self.table_name = table_name
        # The names of the tables.
        self.table_name_list = table_name_list
        # The username of the operator. We recommend that you enter the username of your Alibaba Cloud account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_name_list is not None:
            result['TableNameList'] = self.table_name_list

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableNameList') is not None:
            self.table_name_list = m.get('TableNameList')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

