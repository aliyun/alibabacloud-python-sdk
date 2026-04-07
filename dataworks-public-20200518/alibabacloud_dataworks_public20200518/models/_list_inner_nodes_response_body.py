# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListInnerNodesResponseBody(DaraModel):
    def __init__(
        self,
        paging: main_models.ListInnerNodesResponseBodyPaging = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The pagination information.
        self.paging = paging
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.paging:
            self.paging.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging is not None:
            result['Paging'] = self.paging.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Paging') is not None:
            temp_model = main_models.ListInnerNodesResponseBodyPaging()
            self.paging = temp_model.from_map(m.get('Paging'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInnerNodesResponseBodyPaging(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.ListInnerNodesResponseBodyPagingNodes] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of inner nodes.
        self.nodes = nodes
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of inner nodes returned.
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ListInnerNodesResponseBodyPagingNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInnerNodesResponseBodyPagingNodes(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        business_id: int = None,
        connection: str = None,
        cron_express: str = None,
        description: str = None,
        dqc_description: str = None,
        dqc_type: str = None,
        node_id: int = None,
        node_name: str = None,
        owner_id: str = None,
        param_values: str = None,
        priority: int = None,
        program_type: str = None,
        project_id: int = None,
        repeat_interval: int = None,
        repeatability: bool = None,
        res_group_name: str = None,
        scheduler_type: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The workflow ID.
        self.business_id = business_id
        # The connection string.
        self.connection = connection
        # The CRON expression.
        self.cron_express = cron_express
        # The description of the inner node.
        self.description = description
        # The table and partition filter expression in Data Quality that are associated with the inner node.
        self.dqc_description = dqc_description
        # Indicates whether the inner node is associated with a monitoring rule in Data Quality. Valid values: 0 and 1. The value 0 indicates that the inner node is associated with a monitoring rule in Data Quality. The value 1 indicates that the inner node is not associated with a monitoring rule in Data Quality.
        self.dqc_type = dqc_type
        # The inner node ID.
        self.node_id = node_id
        # The name of the inner node.
        self.node_name = node_name
        # The owner ID.
        self.owner_id = owner_id
        # The additional parameters.
        self.param_values = param_values
        # The priority of the inner node. Valid values: 1, 3, 5, 7, and 8.
        self.priority = priority
        # The type of the inner node.
        self.program_type = program_type
        # The workspace ID.
        self.project_id = project_id
        # The interval at which the inner node is rerun after the inner node fails to run.
        self.repeat_interval = repeat_interval
        # Indicates whether the inner node can be rerun.
        self.repeatability = repeatability
        # The name of the resource group.
        self.res_group_name = res_group_name
        # The scheduling type of the inner node. Valid values:
        # 
        # *   NORMAL: The inner node is an auto triggered node.
        # *   MANUAL: The inner node is a manually triggered node. The scheduling system does not run the node on a regular basis.
        # *   PAUSE: The inner node is a paused node.
        # *   SKIP: The inner node is a dry-run node. Dry-run nodes are started as scheduled, but the scheduling system sets the status of the nodes to successful when it starts to run them.
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

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

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

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

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

        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')

        if m.get('Repeatability') is not None:
            self.repeatability = m.get('Repeatability')

        if m.get('ResGroupName') is not None:
            self.res_group_name = m.get('ResGroupName')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        return self

