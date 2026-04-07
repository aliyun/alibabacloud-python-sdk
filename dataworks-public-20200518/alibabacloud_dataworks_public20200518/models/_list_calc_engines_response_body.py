# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListCalcEnginesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListCalcEnginesResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The query results for compute engines that are returned on multiple pages.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.ListCalcEnginesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCalcEnginesResponseBodyData(DaraModel):
    def __init__(
        self,
        calc_engines: List[main_models.ListCalcEnginesResponseBodyDataCalcEngines] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The compute engines.
        self.calc_engines = calc_engines
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of compute engine instances.
        self.total_count = total_count

    def validate(self):
        if self.calc_engines:
            for v1 in self.calc_engines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CalcEngines'] = []
        if self.calc_engines is not None:
            for k1 in self.calc_engines:
                result['CalcEngines'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.calc_engines = []
        if m.get('CalcEngines') is not None:
            for k1 in m.get('CalcEngines'):
                temp_model = main_models.ListCalcEnginesResponseBodyDataCalcEngines()
                self.calc_engines.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCalcEnginesResponseBodyDataCalcEngines(DaraModel):
    def __init__(
        self,
        binding_project_id: int = None,
        binding_project_name: str = None,
        calc_engine_type: str = None,
        dw_region: str = None,
        engine_id: int = None,
        engine_info: Dict[str, Any] = None,
        env_type: str = None,
        gmt_create: str = None,
        is_default: bool = None,
        name: str = None,
        region: str = None,
        task_auth_type: str = None,
        tenant_id: int = None,
    ):
        # The ID of the workspace with which the compute engine is associated.
        self.binding_project_id = binding_project_id
        # The name of the workspace with which the compute engine is associated.
        self.binding_project_name = binding_project_name
        # The type of the compute engine.
        self.calc_engine_type = calc_engine_type
        # The region where the DataWorks workspace with which the compute engine is associated resides.
        self.dw_region = dw_region
        # The compute engine ID.
        self.engine_id = engine_id
        # The details of the compute engine.
        # 
        # *   ODPS
        # 
        #         {
        #           "pubEndpoint": "service.cn.maxcompute.aliyun.com/api",
        #           "endpoint": "service.cn.maxcompute.aliyun-inc.com/api",
        #           "initProperties": " 
        #           {\\"odpsTypeMode\\":\\"STANDARD\\",\\"openPai\\":false,\\"openPaiGpu\\":false}",
        #           "resourceGroupType": "ODPS",
        #           "resourceGroupId": "361826516****",
        #           "vpcEndpoint": "service.cn.maxcompute.aliyun-inc.com/api",
        #           "projectName": "onefall_test_zjk",
        #           "taskSameAsOwner": "true"
        #         }
        # 
        # *   EMR
        # 
        #         {
        #           "emrClusterId": "C-xxx",
        #           "specs": "{\\"emrClusterId\\":\\"C-xxx\\",\\"emrAccessMode\\":\\"simple\\",\\"emrResourceQueueName\\":\\"default\\",\\"emrProjectId\\":\\"FP-xxx\\"}",
        #           "endpoint": "emr.aliyuncs.com",
        #           "emrResourceQueueName": "default",
        #           "emrAccessMode": "simple",
        #           "resourceGroupType": "DW",
        #           "projectName": "xx-xxxx",
        #           "emrProjectId": "FP-xxxx",
        #           "taskSameAsOwner": "false"
        #         }   
        # 
        # *   BLINK
        # 
        #         {
        #           "bayesProjectId": "xxxx",
        #           "bayesProjectName": "xc_blxxixxxnk_1",
        #           "cluster": "xxxssxsx",
        #           "endpoint": "https://stream.console.aliyun.com",
        #           "engineType": "BLINK",
        #           "name": "xsxsxxxxx",
        #           "projectName": "xc_blxxxsxink_1",
        #           "queue": "root.xc_blxsxxxxxxink_1",
        #           "resourceGroupType": "DW",
        #           "specs": "{\\"cluster\\":\\"xxxxxx\\",\\"bayesProjectName\\":\\"xc_blxxixxxnk_1\\",\\"bayesProjectId\\":\\"ssxxxsa\\",\\"name\\":\\"sxsxsxxx\\",\\"queue\\":\\"root.sxxsxxsx\\"}",
        #           "taskSameAsOwner": false
        #         }
        # 
        # *   HOLO
        # 
        #         {
        #           "endpoint": "hgprecn-cn-xsxssxsx-cn-shanghai-internal.hologres.aliyuncs.com:80",
        #           "engineType": "ODPS",
        #           "odpsEndpoint": "hgprecn-cn-xsxssxxs-cn-shanghai-internal.hologres.aliyuncs.com:80",
        #           "odpsProjectName": "xsxssxsxsx",
        #           "projectName": "xsxssxsxsx",
        #           "resourceGroupType": "DW",
        #           "specs": "{\\"pubEndpoint\\":\\"hgprecn-cn-xsxssxsxs-cn-shanghai.hologres.aliyuncs.com:80\\",\\"commonBuyInstanceId\\":\\"hgprecn-cn-xsxsxsxs\\",\\"project\\":\\"holo_upxsxgrade1\\",\\"common_buy_instance_id\\":\\"hgprecn-cn-xsxsxs\\",\\"endpoint\\":\\"hgprecn-cn-xsxxsxs-cn-shanghai-internal.hologres.aliyuncs.com:80\\",\\"port\\":\\"80\\",\\"host\\":\\"hgprecn-cn-xsxsxsxs-cn-shanghai-internal.hologres.aliyuncs.com\\",\\"vpcEndpoint\\":\\"hgprecn-cn-xsxsxsxs-cn-shanghai-vpc.hologres.aliyuncs.com:80\\",\\"authType\\":2,\\"region\\":\\"cn-shanghai\\"}",
        #           "taskSameAsOwner": false
        #         }
        # 
        # *   MaxGraph
        # 
        #         {
        #           "endpoint": "http://pre-graphcompute.aliyuncs.com",
        #           "engineType": "ODPS",
        #           "odpsEndpoint": "http://pre-graphcompute.aliyuncs.com",
        #           "odpsProjectName": "xsxsxsxs",
        #           "projectName": "xsxsxsxs",
        #           "resourceGroupType": "DW",
        #           "taskSameAsOwner": false
        #         }
        # 
        # *   HYBRIDDB_FOR_POSTGRESQL
        # 
        #         {
        #           "endpoint": "hybriddb_for_postgresql_mo12121ck_endpoint",
        #           "engineType": "ODPS",
        #           "odpsEndpoint": "hybriddb_for_postgresql_m121212ock_endpoint",
        #           "odpsProjectName": "sxasaxsaxaxas",
        #           "projectName": "sxasaxsaxaxas",
        #           "resourceGroupType": "DW",
        #           "specs": "{\\"connectionString\\":\\"gp-xsxsxsxxs.gpdb.rds.aliyuncs.com\\",\\"database\\":\\"xsxsxxsxs\\",\\"password\\":\\"xxxxxxx\\",\\"instanceId\\":\\"gp-cdcdacdacda\\",\\"port\\":\\"3432\\",\\"ownerId\\":\\"12121212\\",\\"username\\":\\"sdasaddsa\\"}",
        #           "taskSameAsOwner": false
        #         }
        # 
        # *   ADB_MYSQL
        # 
        #         {
        #           "endpoint": "adb_mysql_mock_endpoint",
        #           "engineType": "ODPS",
        #           "odpsEndpoint": "adb_mysql_mock_endpoint",
        #           "odpsProjectName": "am-xsaxaxa",
        #           "projectName": "am-xsxsaxa",
        #           "resourceGroupType": "DW",
        #           "specs": "{\\"connectionString\\":\\"am-xsaxsa.ads.aliyuncs.com:3306\\",\\"database\\":\\"xsaxsaxa\\",\\"password\\":\\"xsaxsaxassxsa\\",\\"instanceId\\":\\"am-xsaxsasx\\",\\"username\\":\\"xsaxsadsd\\"}",
        #           "taskSameAsOwner": false
        #         }
        # 
        # *   HADOOP_CDH
        # 
        #         {
        #           "bindingBaseId": "xsaxsaxs",
        #           "endpoint": "xsaaaaa",
        #           "engineType": "ODPS",
        #           "odpsEndpoint": "axsxaxssxs",
        #           "odpsProjectName": "ssxxax",
        #           "projectName": "xsaxsaxsa",
        #           "resourceGroupId": 45208xxxxxx,
        #           "resourceGroupType": "GATEWAY",
        #           "specs": "{\\"cluster\\":{\\"hive\\":{\\"hiveServer2Url\\":\\"jdbc:hive2://xxxxxxer-1-cn-shanghai-pre-kerberos-1:10000\\",\\"hiveMetastore\\":\\"thrift://xxxxxxxr-1-cn-shanghai-pre-kerberos-1:9083\\",\\"version\\":\\"2.1.1\\"},\\"configFiles\\":{\\"coreSite\\":\\"4534574xxxxxx\\",\\"hdfsSite\\":\\"453457919xxxxxxx\\",\\"mapredSite\\":\\"45345750xxxxxx\\",\\"yarnSite\\":\\"4534575xxxxx\\",\\"krb5Conf\\":\\"4534576xxxxx1\\",\\"hiveSite\\":\\"453457xxxxx20\\"},\\"spark\\":{\\"version\\":\\"2.4.0\\"},\\"cdh\\":{\\"version\\":\\"6.3.2\\"},\\"hdfs\\":{\\"version\\":\\"3.0.0\\"},\\"impala\\":{\\"impalaUrl\\":\\"jdbc:impala://cdh-xsxssxxsx-1-cn-shanghai-pre-kerberos-1:21050\\",\\"version\\":\\"3.2.0\\"},\\"yarn\\":{\\"YarnUrl\\":\\"http://cdh-xsxsxsxsxs-1-cn-shanghai-pre-kerberos-1:8032\\",\\"webUrl\\":\\"http://cdh-xsxsxssxxssx-1-cn-shanghai-pre-kerberos-1:8088\\",\\"version\\":\\"3.0.0\\"},\\"presto\\":{\\"prestoUrl\\":\\"jdbc:presto://cdh-xssxsxxsxsxs-1-cn-shanghai-pre-kerberos-1:8080/hive/default\\",\\"version\\":\\"0.244.1\\"}},\\"instanceId\\":161sdads733,\\"authDetail\\":{\\"principal\\":\\"hive@HADOOP.COM\\",\\"keytabFileId\\":\\"45345815xsxsxs3\\",\\"type\\":\\"kerberos\\",\\"username\\":\\"xsxsxsxsa@HADOOP.COM\\"},\\"resGroupStatus\\":\\"\\",\\"hadoopAuthType\\":\\"kerberos\\",\\"clusterIdentifier\\":\\"xssxsxsxsx\\",\\"clusterId\\":xsxsx,\\"resGroupId\\":4520870619xsxssxxs,\\"accessMode\\":\\"security\\",\\"authType\\":2}",
        #           "taskSameAsOwner": false
        #         }
        self.engine_info = engine_info
        # The environment in which the compute engine is used. Valid values:
        # 
        # *   **DEV**
        # *   **PRD**
        self.env_type = env_type
        # The time when the compute engine was created.
        self.gmt_create = gmt_create
        # Indicates whether the compute engine is the default engine of the current type.
        self.is_default = is_default
        # The display name of the compute engine.
        self.name = name
        # The region where the compute engine resides.
        self.region = region
        # The identity that is used to access the compute engine. Valid values:
        # 
        # *   **USER**: the current user
        # *   **PROJECT**: the workspace executor
        # *   **SUBACCOUNT**: a RAM user
        # *   **STS_ROLE**: the Security Token Service (STS) role
        self.task_auth_type = task_auth_type
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_project_id is not None:
            result['BindingProjectId'] = self.binding_project_id

        if self.binding_project_name is not None:
            result['BindingProjectName'] = self.binding_project_name

        if self.calc_engine_type is not None:
            result['CalcEngineType'] = self.calc_engine_type

        if self.dw_region is not None:
            result['DwRegion'] = self.dw_region

        if self.engine_id is not None:
            result['EngineId'] = self.engine_id

        if self.engine_info is not None:
            result['EngineInfo'] = self.engine_info

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.region is not None:
            result['Region'] = self.region

        if self.task_auth_type is not None:
            result['TaskAuthType'] = self.task_auth_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingProjectId') is not None:
            self.binding_project_id = m.get('BindingProjectId')

        if m.get('BindingProjectName') is not None:
            self.binding_project_name = m.get('BindingProjectName')

        if m.get('CalcEngineType') is not None:
            self.calc_engine_type = m.get('CalcEngineType')

        if m.get('DwRegion') is not None:
            self.dw_region = m.get('DwRegion')

        if m.get('EngineId') is not None:
            self.engine_id = m.get('EngineId')

        if m.get('EngineInfo') is not None:
            self.engine_info = m.get('EngineInfo')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('TaskAuthType') is not None:
            self.task_auth_type = m.get('TaskAuthType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

