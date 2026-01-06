# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartSparkSQLEngineRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        dbcluster_id: str = None,
        jars: str = None,
        max_executor: int = None,
        min_executor: int = None,
        resource_group_name: str = None,
        slot_num: int = None,
    ):
        # The configuration that is required to start the Spark SQL engine. Specify this value in the JSON format. For more information, see [Conf configuration parameters](https://help.aliyun.com/document_detail/471203.html).
        self.config = config
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The Object Storage Service (OSS) paths of third-party JAR packages that are required to start the Spark SQL engine. Separate multiple OSS paths with commas (,).
        self.jars = jars
        # The maximum number of executors that are required to execute SQL statements. Valid values: 1 to 2000. If this value exceeds the total number of executes that are supported by the resource group, the Spark SQL engine fails to be started.
        self.max_executor = max_executor
        # The minimum number of executors that are required to execute SQL statements. Valid values: 0 to 2000. A value of 0 indicates that no executors are permanent if no SQL statements are executed. If this value exceeds the total number of executors that are supported by the resource group, the Spark SQL engine fails to be started. The value must be less than the value of MaxExecutor.
        self.min_executor = min_executor
        # The name of the resource group.
        # 
        # This parameter is required.
        self.resource_group_name = resource_group_name
        # The maximum number of slots that are required to maintain Spark sessions for executing SQL statements. Valid values: 1 to 500.
        self.slot_num = slot_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.jars is not None:
            result['Jars'] = self.jars

        if self.max_executor is not None:
            result['MaxExecutor'] = self.max_executor

        if self.min_executor is not None:
            result['MinExecutor'] = self.min_executor

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.slot_num is not None:
            result['SlotNum'] = self.slot_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Jars') is not None:
            self.jars = m.get('Jars')

        if m.get('MaxExecutor') is not None:
            self.max_executor = m.get('MaxExecutor')

        if m.get('MinExecutor') is not None:
            self.min_executor = m.get('MinExecutor')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('SlotNum') is not None:
            self.slot_num = m.get('SlotNum')

        return self

