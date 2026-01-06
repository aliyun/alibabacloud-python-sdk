# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetInstanceInspectionsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetInstanceInspectionsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The details.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, Successful is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetInstanceInspectionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetInstanceInspectionsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetInstanceInspectionsResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The detailed information.
        self.list = list
        # The page number. The value returned is a positive integer. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetInstanceInspectionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetInstanceInspectionsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        auto_function: main_models.GetInstanceInspectionsResponseBodyDataListAutoFunction = None,
        data: Dict[str, Any] = None,
        enable_das_pro: int = None,
        end_time: int = None,
        gmt_create: int = None,
        instance: main_models.GetInstanceInspectionsResponseBodyDataListInstance = None,
        score: int = None,
        score_map: Dict[str, Any] = None,
        start_time: int = None,
        state: int = None,
        task_type: int = None,
    ):
        # Indicates whether the autonomy service is enabled.
        self.auto_function = auto_function
        # The data returned.
        self.data = data
        # Indicates whether DAS Enterprise Edition is enabled. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        # *   **2**: not supported.
        self.enable_das_pro = enable_das_pro
        # The end time of the inspection and scoring task. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time.
        self.end_time = end_time
        # The time when the task was created. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.gmt_create = gmt_create
        # The information about the instance.
        self.instance = instance
        # The inspection score of the instance.
        self.score = score
        # The scores that are deducted for the instance.
        self.score_map = score_map
        # The start time of the inspection and scoring task. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The state of the inspection and scoring task. Valid values:
        # 
        # *   **0**: The task is waiting for execution.
        # *   **1**: The task is in progress.
        # *   **2**: The task is complete.
        self.state = state
        # The mode in which the inspection and scoring task was initiated. Valid values:
        # 
        # *   **0**: automatic mode.
        # *   **1**: manual mode.
        self.task_type = task_type

    def validate(self):
        if self.auto_function:
            self.auto_function.validate()
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_function is not None:
            result['AutoFunction'] = self.auto_function.to_map()

        if self.data is not None:
            result['Data'] = self.data

        if self.enable_das_pro is not None:
            result['EnableDasPro'] = self.enable_das_pro

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance is not None:
            result['Instance'] = self.instance.to_map()

        if self.score is not None:
            result['Score'] = self.score

        if self.score_map is not None:
            result['ScoreMap'] = self.score_map

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.state is not None:
            result['State'] = self.state

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoFunction') is not None:
            temp_model = main_models.GetInstanceInspectionsResponseBodyDataListAutoFunction()
            self.auto_function = temp_model.from_map(m.get('AutoFunction'))

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('EnableDasPro') is not None:
            self.enable_das_pro = m.get('EnableDasPro')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Instance') is not None:
            temp_model = main_models.GetInstanceInspectionsResponseBodyDataListInstance()
            self.instance = temp_model.from_map(m.get('Instance'))

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('ScoreMap') is not None:
            self.score_map = m.get('ScoreMap')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class GetInstanceInspectionsResponseBodyDataListInstance(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        category: str = None,
        cpu: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_alias: str = None,
        instance_area: str = None,
        instance_class: str = None,
        instance_id: str = None,
        memory: int = None,
        network_type: str = None,
        node_id: str = None,
        region: str = None,
        storage: int = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        # The account ID. You can view the ID of the logon account by moving the pointer over the profile in the Alibaba Cloud management console.
        self.account_id = account_id
        # The connection mode of the instance. Valid values:
        # 
        # *   **standard**: standard mode.
        # *   **safe**: database proxy mode.
        self.category = category
        # The CPU specification of the instance. For example, if a value of 8 is returned, the instance has eight CPU cores.
        self.cpu = cpu
        # The database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **Redis**
        # *   **PolarDBMySQL**
        self.engine = engine
        # The version number of the database engine.
        self.engine_version = engine_version
        # The instance name.
        self.instance_alias = instance_alias
        # The type of the instance on which the database is deployed. Valid values:
        # 
        # *   **RDS**: an Alibaba Cloud database instance.
        # *   **ECS**: an Elastic Compute Service (ECS) instance on which a self-managed database is deployed.
        # *   **IDC**: a self-managed database instance that is not deployed on Alibaba Cloud.
        # 
        # >  The value IDC indicates that the instance is deployed in a data center.
        self.instance_area = instance_area
        # The instance type.
        self.instance_class = instance_class
        # The instance ID.
        self.instance_id = instance_id
        # The memory capacity of the database that is deployed on the instance. Unit: MB.
        self.memory = memory
        # The network type of the instance.
        self.network_type = network_type
        # The ID of the node on the instance.
        self.node_id = node_id
        # The region ID of the instance.
        self.region = region
        # The storage space of the instance. Unit: GB.
        self.storage = storage
        # The unique identifier of the instance.
        self.uuid = uuid
        # The ID of the virtual private cloud (VPC) in which the instance is deployed.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.category is not None:
            result['Category'] = self.category

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.region is not None:
            result['Region'] = self.region

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetInstanceInspectionsResponseBodyDataListAutoFunction(DaraModel):
    def __init__(
        self,
        auto_index: int = None,
        auto_limited_sql: int = None,
        auto_resource_optimize: int = None,
        auto_scale: int = None,
        event_subscription: int = None,
    ):
        # Indicates whether the feature of automatically creating and deleting indexes is enabled. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        # *   **2**: not supported.
        self.auto_index = auto_index
        # Indicates whether the automatic throttling feature is enabled. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        # *   **2**: not supported.
        self.auto_limited_sql = auto_limited_sql
        # Indicates whether the automatic fragment recycling feature is enabled. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        # *   **2**: not supported.
        self.auto_resource_optimize = auto_resource_optimize
        # Indicates whether the auto scaling feature is enabled. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        # *   **2**: not supported.
        self.auto_scale = auto_scale
        # Indicates whether the event subscription feature is enabled. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        # *   **2**: not supported.
        self.event_subscription = event_subscription

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_index is not None:
            result['AutoIndex'] = self.auto_index

        if self.auto_limited_sql is not None:
            result['AutoLimitedSql'] = self.auto_limited_sql

        if self.auto_resource_optimize is not None:
            result['AutoResourceOptimize'] = self.auto_resource_optimize

        if self.auto_scale is not None:
            result['AutoScale'] = self.auto_scale

        if self.event_subscription is not None:
            result['EventSubscription'] = self.event_subscription

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIndex') is not None:
            self.auto_index = m.get('AutoIndex')

        if m.get('AutoLimitedSql') is not None:
            self.auto_limited_sql = m.get('AutoLimitedSql')

        if m.get('AutoResourceOptimize') is not None:
            self.auto_resource_optimize = m.get('AutoResourceOptimize')

        if m.get('AutoScale') is not None:
            self.auto_scale = m.get('AutoScale')

        if m.get('EventSubscription') is not None:
            self.event_subscription = m.get('EventSubscription')

        return self

