# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListLhTaskFlowAndScenarioResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        raw_daglist: main_models.ListLhTaskFlowAndScenarioResponseBodyRawDAGList = None,
        request_id: str = None,
        scenario_daglist: main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGList = None,
        success: bool = None,
    ):
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The task flows in the default business scenario.
        self.raw_daglist = raw_daglist
        # The ID of the request.
        self.request_id = request_id
        # The task flows in other business scenarios.
        self.scenario_daglist = scenario_daglist
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.
        # - **false**: The request fails.
        self.success = success

    def validate(self):
        if self.raw_daglist:
            self.raw_daglist.validate()
        if self.scenario_daglist:
            self.scenario_daglist.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.raw_daglist is not None:
            result['RawDAGList'] = self.raw_daglist.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scenario_daglist is not None:
            result['ScenarioDAGList'] = self.scenario_daglist.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RawDAGList') is not None:
            temp_model = main_models.ListLhTaskFlowAndScenarioResponseBodyRawDAGList()
            self.raw_daglist = temp_model.from_map(m.get('RawDAGList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScenarioDAGList') is not None:
            temp_model = main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGList()
            self.scenario_daglist = temp_model.from_map(m.get('ScenarioDAGList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGList(DaraModel):
    def __init__(
        self,
        scenario_dag: List[main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAG] = None,
    ):
        self.scenario_dag = scenario_dag

    def validate(self):
        if self.scenario_dag:
            for v1 in self.scenario_dag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ScenarioDAG'] = []
        if self.scenario_dag is not None:
            for k1 in self.scenario_dag:
                result['ScenarioDAG'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scenario_dag = []
        if m.get('ScenarioDAG') is not None:
            for k1 in m.get('ScenarioDAG'):
                temp_model = main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAG()
                self.scenario_dag.append(temp_model.from_map(k1))

        return self

class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAG(DaraModel):
    def __init__(
        self,
        dag_list: main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagList = None,
        scenario: main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGScenario = None,
    ):
        # The list of task flows.
        self.dag_list = dag_list
        # The information about the business scenario.
        self.scenario = scenario

    def validate(self):
        if self.dag_list:
            self.dag_list.validate()
        if self.scenario:
            self.scenario.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_list is not None:
            result['DagList'] = self.dag_list.to_map()

        if self.scenario is not None:
            result['Scenario'] = self.scenario.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagList') is not None:
            temp_model = main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagList()
            self.dag_list = temp_model.from_map(m.get('DagList'))

        if m.get('Scenario') is not None:
            temp_model = main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGScenario()
            self.scenario = temp_model.from_map(m.get('Scenario'))

        return self

class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGScenario(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        description: str = None,
        scenario_name: str = None,
    ):
        # The ID of the user who creates the business scenario.
        self.creator_id = creator_id
        # The description of the business scenario.
        self.description = description
        # The name of the business scenario.
        self.scenario_name = scenario_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.description is not None:
            result['Description'] = self.description

        if self.scenario_name is not None:
            result['ScenarioName'] = self.scenario_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ScenarioName') is not None:
            self.scenario_name = m.get('ScenarioName')

        return self

class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagList(DaraModel):
    def __init__(
        self,
        dag: List[main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagListDag] = None,
    ):
        self.dag = dag

    def validate(self):
        if self.dag:
            for v1 in self.dag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dag'] = []
        if self.dag is not None:
            for k1 in self.dag:
                result['Dag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dag = []
        if m.get('Dag') is not None:
            for k1 in m.get('Dag'):
                temp_model = main_models.ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagListDag()
                self.dag.append(temp_model.from_map(k1))

        return self

class ListLhTaskFlowAndScenarioResponseBodyScenarioDAGListScenarioDAGDagListDag(DaraModel):
    def __init__(
        self,
        can_edit: bool = None,
        creator_id: str = None,
        creator_nick_name: str = None,
        dag_name: str = None,
        dag_owner_id: str = None,
        dag_owner_nick_name: str = None,
        data_flow_id: int = None,
        demo_id: str = None,
        deploy_id: int = None,
        id: int = None,
        is_deleted: bool = None,
        latest_instance_status: int = None,
        latest_instance_time: int = None,
        scenario_id: int = None,
        space_id: int = None,
        status: int = None,
    ):
        # Indicates whether the task flow can be modified. Valid values:
        # 
        # - **true**: The task flow can be modified.
        # - **false**: The task flow cannot be modified.
        self.can_edit = can_edit
        # The ID of the user who creates the task flow.
        self.creator_id = creator_id
        # The name of the user who creates the workspace.
        self.creator_nick_name = creator_nick_name
        # The name of the task flow.
        self.dag_name = dag_name
        # The user ID of the task flow owner.
        self.dag_owner_id = dag_owner_id
        # The name of the task flow owner.
        self.dag_owner_nick_name = dag_owner_nick_name
        # The extended field. No meaning is specified for this field.
        self.data_flow_id = data_flow_id
        # The extended field. No meaning is specified for this field.
        self.demo_id = demo_id
        # The ID of the latest deployment record.
        self.deploy_id = deploy_id
        # The ID of the task flow.
        self.id = id
        # Indicates whether the task flow is deleted. Valid values:
        # 
        # - **true**: deleted
        # - **false**: not deleted
        self.is_deleted = is_deleted
        # The status of the latest execution. Valid values:
        # 
        # - 0: invalid
        # - 1: scheduling disabled
        # - 2: waiting to be scheduled
        self.latest_instance_status = latest_instance_status
        # The time when the latest execution record was generated.
        self.latest_instance_time = latest_instance_time
        # The ID of the business scenario.
        self.scenario_id = scenario_id
        # The ID of the workspace.
        self.space_id = space_id
        # The status of the task flow. Valid values:
        # 
        # - **0**: invalid
        # - **1**: scheduling disabled
        # - **2**: waiting to be scheduled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_edit is not None:
            result['CanEdit'] = self.can_edit

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_nick_name is not None:
            result['CreatorNickName'] = self.creator_nick_name

        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.dag_owner_id is not None:
            result['DagOwnerId'] = self.dag_owner_id

        if self.dag_owner_nick_name is not None:
            result['DagOwnerNickName'] = self.dag_owner_nick_name

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.demo_id is not None:
            result['DemoId'] = self.demo_id

        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id

        if self.id is not None:
            result['Id'] = self.id

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.latest_instance_status is not None:
            result['LatestInstanceStatus'] = self.latest_instance_status

        if self.latest_instance_time is not None:
            result['LatestInstanceTime'] = self.latest_instance_time

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanEdit') is not None:
            self.can_edit = m.get('CanEdit')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorNickName') is not None:
            self.creator_nick_name = m.get('CreatorNickName')

        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('DagOwnerId') is not None:
            self.dag_owner_id = m.get('DagOwnerId')

        if m.get('DagOwnerNickName') is not None:
            self.dag_owner_nick_name = m.get('DagOwnerNickName')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DemoId') is not None:
            self.demo_id = m.get('DemoId')

        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('LatestInstanceStatus') is not None:
            self.latest_instance_status = m.get('LatestInstanceStatus')

        if m.get('LatestInstanceTime') is not None:
            self.latest_instance_time = m.get('LatestInstanceTime')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListLhTaskFlowAndScenarioResponseBodyRawDAGList(DaraModel):
    def __init__(
        self,
        dag: List[main_models.ListLhTaskFlowAndScenarioResponseBodyRawDAGListDag] = None,
    ):
        self.dag = dag

    def validate(self):
        if self.dag:
            for v1 in self.dag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dag'] = []
        if self.dag is not None:
            for k1 in self.dag:
                result['Dag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dag = []
        if m.get('Dag') is not None:
            for k1 in m.get('Dag'):
                temp_model = main_models.ListLhTaskFlowAndScenarioResponseBodyRawDAGListDag()
                self.dag.append(temp_model.from_map(k1))

        return self

class ListLhTaskFlowAndScenarioResponseBodyRawDAGListDag(DaraModel):
    def __init__(
        self,
        can_edit: bool = None,
        creator_id: str = None,
        creator_nick_name: str = None,
        dag_name: str = None,
        dag_owner_id: str = None,
        dag_owner_nick_name: str = None,
        data_flow_id: int = None,
        demo_id: str = None,
        deploy_id: int = None,
        id: int = None,
        is_deleted: bool = None,
        latest_instance_status: int = None,
        latest_instance_time: int = None,
        scenario_id: int = None,
        space_id: int = None,
        status: int = None,
    ):
        # Indicates whether the task flow can be modified. Valid values:
        # 
        # *   **true**: The task flow can be modified.
        # *   **false**: The task flow cannot be modified.
        self.can_edit = can_edit
        # The ID of the user who creates the task flow.
        self.creator_id = creator_id
        # The name of the user who creates the workspace.
        self.creator_nick_name = creator_nick_name
        # The name of the task flow.
        self.dag_name = dag_name
        # The user ID of the task flow owner.
        self.dag_owner_id = dag_owner_id
        # The name of the task flow owner.
        self.dag_owner_nick_name = dag_owner_nick_name
        # The extended field. No meaning is specified for this field.
        self.data_flow_id = data_flow_id
        # The extended field. No meaning is specified for this field.
        self.demo_id = demo_id
        # The ID of the latest deployment record.
        self.deploy_id = deploy_id
        # The ID of the task flow.
        self.id = id
        # Indicates whether the task flow is deleted. Valid values:
        # 
        # *   **true**: deleted
        # *   **false**: not deleted
        self.is_deleted = is_deleted
        # The status of the latest execution. Valid values:
        # 
        # *   **0**: invalid
        # *   **1**: scheduling disabled
        # *   **2**: waiting to be scheduled
        self.latest_instance_status = latest_instance_status
        # The time when the latest execution record was generated.
        self.latest_instance_time = latest_instance_time
        # The ID of the business scenario.
        self.scenario_id = scenario_id
        # The ID of the workspace.
        self.space_id = space_id
        # The status of the task flow. Valid values:
        # 
        # *   **0**: invalid
        # *   **1**: scheduling disabled
        # *   **2**: waiting to be scheduled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_edit is not None:
            result['CanEdit'] = self.can_edit

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_nick_name is not None:
            result['CreatorNickName'] = self.creator_nick_name

        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.dag_owner_id is not None:
            result['DagOwnerId'] = self.dag_owner_id

        if self.dag_owner_nick_name is not None:
            result['DagOwnerNickName'] = self.dag_owner_nick_name

        if self.data_flow_id is not None:
            result['DataFlowId'] = self.data_flow_id

        if self.demo_id is not None:
            result['DemoId'] = self.demo_id

        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id

        if self.id is not None:
            result['Id'] = self.id

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.latest_instance_status is not None:
            result['LatestInstanceStatus'] = self.latest_instance_status

        if self.latest_instance_time is not None:
            result['LatestInstanceTime'] = self.latest_instance_time

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanEdit') is not None:
            self.can_edit = m.get('CanEdit')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorNickName') is not None:
            self.creator_nick_name = m.get('CreatorNickName')

        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('DagOwnerId') is not None:
            self.dag_owner_id = m.get('DagOwnerId')

        if m.get('DagOwnerNickName') is not None:
            self.dag_owner_nick_name = m.get('DagOwnerNickName')

        if m.get('DataFlowId') is not None:
            self.data_flow_id = m.get('DataFlowId')

        if m.get('DemoId') is not None:
            self.demo_id = m.get('DemoId')

        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('LatestInstanceStatus') is not None:
            self.latest_instance_status = m.get('LatestInstanceStatus')

        if m.get('LatestInstanceTime') is not None:
            self.latest_instance_time = m.get('LatestInstanceTime')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

