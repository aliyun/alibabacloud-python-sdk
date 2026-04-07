# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListNodesByOutputResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListNodesByOutputResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The nodes returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListNodesByOutputResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListNodesByOutputResponseBodyData(DaraModel):
    def __init__(
        self,
        node_list: List[main_models.ListNodesByOutputResponseBodyDataNodeList] = None,
        output: str = None,
    ):
        # The information about the nodes returned.
        self.node_list = node_list
        # The output name of the current node.
        self.output = output

    def validate(self):
        if self.node_list:
            for v1 in self.node_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeList'] = []
        if self.node_list is not None:
            for k1 in self.node_list:
                result['NodeList'].append(k1.to_map() if k1 else None)

        if self.output is not None:
            result['Output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_list = []
        if m.get('NodeList') is not None:
            for k1 in m.get('NodeList'):
                temp_model = main_models.ListNodesByOutputResponseBodyDataNodeList()
                self.node_list.append(temp_model.from_map(k1))

        if m.get('Output') is not None:
            self.output = m.get('Output')

        return self

class ListNodesByOutputResponseBodyDataNodeList(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        connection: str = None,
        cron_express: str = None,
        description: str = None,
        dqc_description: str = None,
        dqc_type: int = None,
        file_type: str = None,
        node_id: int = None,
        node_name: str = None,
        owner_id: str = None,
        param_values: str = None,
        priority: int = None,
        program_type: str = None,
        project_id: int = None,
        related_flow_id: int = None,
        repeat_interval: int = None,
        repeatability: bool = None,
        res_group_name: str = None,
        scheduler_type: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The name of the data source.
        self.connection = connection
        # The CRON expression.
        self.cron_express = cron_express
        # The description of the node.
        self.description = description
        # The table and partition filter expression in Data Quality that are associated with the node.
        self.dqc_description = dqc_description
        # Indicates whether the node is associated with a monitoring rule in Data Quality. Valid values: 0 and 1. The value 0 indicates that the node is associated with a monitoring rule in Data Quality. The value 1 indicates that the node is not associated with a monitoring rule in Data Quality.
        self.dqc_type = dqc_type
        # The node type. Valid values:
        # 
        # 6 (Shell), 10 (ODPS SQL), 11 (ODPS MR), 23 (Data Integration), 24 (ODPS Script), 99 (zero load), 221 (PyODPS 2), 225 (ODPS Spark), 227 (EMR Hive), 228 (EMR Spark), 229 (EMR Spark SQL), 230 (EMR MR), 239 (OSS object inspection), 257 (EMR Shell), 258 (EMR Spark Shell), 259 (EMR Presto), 260 (EMR Impala), 900 (real-time synchronization), 1089 (cross-tenant collaboration), 1091 (Hologres development), 1093 (Hologres SQL), 1100 (assignment), and 1221 (PyODPS 3)
        self.file_type = file_type
        # The node ID.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The owner ID.
        self.owner_id = owner_id
        # The scheduling parameters of the node.
        self.param_values = param_values
        # The priority of the node. Valid values: 1, 3, 5, 7, and 8. A greater value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The node type. This parameter is deprecated. For more information about node types, see valid values of the FileType parameter.
        self.program_type = program_type
        # The workspace ID.
        self.project_id = project_id
        # The ID of the workflow to which the node belongs.
        self.related_flow_id = related_flow_id
        # The interval at which the node is rerun after the node fails to run.
        self.repeat_interval = repeat_interval
        # Indicates whether the node can be rerun.
        self.repeatability = repeatability
        # The name of the resource group.
        self.res_group_name = res_group_name
        # The scheduling type of the node. Valid values:
        # 
        # *   NORMAL: The node is an auto triggered node. The scheduling system regularly runs the node.
        # *   MANUAL: The node is a manually triggered node. The scheduling system does not regularly run the node.
        # *   PAUSE: The node is a frozen node. The scheduling system regularly runs the node but sets the status of the node to failed when the scheduling system starts to run the node.
        # *   SKIP: The node is a dry-run node. The scheduling system regularly runs the node but sets the status of the node to successful when the scheduling system starts to run the node.
        self.scheduler_type = scheduler_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.connection is not None:
            result['Connection'] = self.connection

        if self.cron_express is not None:
            result['CronExpress'] = self.cron_express

        if self.description is not None:
            result['Description'] = self.description

        if self.dqc_description is not None:
            result['DqcDescription'] = self.dqc_description

        if self.dqc_type is not None:
            result['DqcType'] = self.dqc_type

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.param_values is not None:
            result['ParamValues'] = self.param_values

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.program_type is not None:
            result['ProgramType'] = self.program_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.related_flow_id is not None:
            result['RelatedFlowId'] = self.related_flow_id

        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval

        if self.repeatability is not None:
            result['Repeatability'] = self.repeatability

        if self.res_group_name is not None:
            result['ResGroupName'] = self.res_group_name

        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('Connection') is not None:
            self.connection = m.get('Connection')

        if m.get('CronExpress') is not None:
            self.cron_express = m.get('CronExpress')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DqcDescription') is not None:
            self.dqc_description = m.get('DqcDescription')

        if m.get('DqcType') is not None:
            self.dqc_type = m.get('DqcType')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParamValues') is not None:
            self.param_values = m.get('ParamValues')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProgramType') is not None:
            self.program_type = m.get('ProgramType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RelatedFlowId') is not None:
            self.related_flow_id = m.get('RelatedFlowId')

        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')

        if m.get('Repeatability') is not None:
            self.repeatability = m.get('Repeatability')

        if m.get('ResGroupName') is not None:
            self.res_group_name = m.get('ResGroupName')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        return self

