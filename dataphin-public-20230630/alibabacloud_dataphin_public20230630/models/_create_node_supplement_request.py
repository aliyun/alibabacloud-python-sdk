# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateNodeSupplementRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateNodeSupplementRequestCreateCommand = None,
        env: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The data backfill request.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The environment identifier. Valid values:
        # - DEV: Development environment. 
        # - PROD (default): Production environment.
        self.env = env
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.env is not None:
            result['Env'] = self.env

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateNodeSupplementRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class CreateNodeSupplementRequestCreateCommand(DaraModel):
    def __init__(
        self,
        contain_all_down_stream: bool = None,
        down_stream_node_id_list: List[main_models.CreateNodeSupplementRequestCreateCommandDownStreamNodeIdList] = None,
        end_biz_date: str = None,
        filter_list: List[main_models.CreateNodeSupplementRequestCreateCommandFilterList] = None,
        global_param_list: List[main_models.CreateNodeSupplementRequestCreateCommandGlobalParamList] = None,
        max_due_time: str = None,
        min_due_time: str = None,
        name: str = None,
        node_id_list: List[main_models.CreateNodeSupplementRequestCreateCommandNodeIdList] = None,
        node_params_list: List[main_models.CreateNodeSupplementRequestCreateCommandNodeParamsList] = None,
        parallelism: int = None,
        project_id: int = None,
        run_immediately: bool = None,
        start_biz_date: str = None,
    ):
        # Specifies whether to include all downstream nodes in batch mode. Default value: false.
        self.contain_all_down_stream = contain_all_down_stream
        # The IDs of downstream nodes to run. This parameter takes effect only when ContainAllDownStream is set to false.
        self.down_stream_node_id_list = down_stream_node_id_list
        # The end business date.
        # 
        # This parameter is required.
        self.end_biz_date = end_biz_date
        # The list of filters. This parameter is used together with ContainAllDownStream to include or exclude nodes based on criteria such as project or node. Default value: empty.
        self.filter_list = filter_list
        # The runtime global parameters.
        self.global_param_list = global_param_list
        # The latest trigger time in the HH:MM format. This parameter is applicable only to hourly nodes.
        self.max_due_time = max_due_time
        # The earliest trigger time in the HH:MM format. This parameter is applicable only to hourly nodes.
        self.min_due_time = min_due_time
        # The name of the data backfill. If this parameter is not specified, the system automatically generates a name.
        self.name = name
        # The root nodes for data backfill. Multiple root nodes are supported.
        # 
        # This parameter is required.
        self.node_id_list = node_id_list
        # The runtime custom parameters configured by node.
        self.node_params_list = node_params_list
        # The concurrency. Default value: 1.
        self.parallelism = parallelism
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Corresponds to the "Task Run Time" option in the data backfill dialog box. If this parameter is set to true, the scheduled run time of instances is ignored and all instances run immediately. If this parameter is set to false, instances wait for their scheduled run time before running. Default value: true.
        self.run_immediately = run_immediately
        # The start business date.
        # 
        # This parameter is required.
        self.start_biz_date = start_biz_date

    def validate(self):
        if self.down_stream_node_id_list:
            for v1 in self.down_stream_node_id_list:
                 if v1:
                    v1.validate()
        if self.filter_list:
            for v1 in self.filter_list:
                 if v1:
                    v1.validate()
        if self.global_param_list:
            for v1 in self.global_param_list:
                 if v1:
                    v1.validate()
        if self.node_id_list:
            for v1 in self.node_id_list:
                 if v1:
                    v1.validate()
        if self.node_params_list:
            for v1 in self.node_params_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contain_all_down_stream is not None:
            result['ContainAllDownStream'] = self.contain_all_down_stream

        result['DownStreamNodeIdList'] = []
        if self.down_stream_node_id_list is not None:
            for k1 in self.down_stream_node_id_list:
                result['DownStreamNodeIdList'].append(k1.to_map() if k1 else None)

        if self.end_biz_date is not None:
            result['EndBizDate'] = self.end_biz_date

        result['FilterList'] = []
        if self.filter_list is not None:
            for k1 in self.filter_list:
                result['FilterList'].append(k1.to_map() if k1 else None)

        result['GlobalParamList'] = []
        if self.global_param_list is not None:
            for k1 in self.global_param_list:
                result['GlobalParamList'].append(k1.to_map() if k1 else None)

        if self.max_due_time is not None:
            result['MaxDueTime'] = self.max_due_time

        if self.min_due_time is not None:
            result['MinDueTime'] = self.min_due_time

        if self.name is not None:
            result['Name'] = self.name

        result['NodeIdList'] = []
        if self.node_id_list is not None:
            for k1 in self.node_id_list:
                result['NodeIdList'].append(k1.to_map() if k1 else None)

        result['NodeParamsList'] = []
        if self.node_params_list is not None:
            for k1 in self.node_params_list:
                result['NodeParamsList'].append(k1.to_map() if k1 else None)

        if self.parallelism is not None:
            result['Parallelism'] = self.parallelism

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.run_immediately is not None:
            result['RunImmediately'] = self.run_immediately

        if self.start_biz_date is not None:
            result['StartBizDate'] = self.start_biz_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainAllDownStream') is not None:
            self.contain_all_down_stream = m.get('ContainAllDownStream')

        self.down_stream_node_id_list = []
        if m.get('DownStreamNodeIdList') is not None:
            for k1 in m.get('DownStreamNodeIdList'):
                temp_model = main_models.CreateNodeSupplementRequestCreateCommandDownStreamNodeIdList()
                self.down_stream_node_id_list.append(temp_model.from_map(k1))

        if m.get('EndBizDate') is not None:
            self.end_biz_date = m.get('EndBizDate')

        self.filter_list = []
        if m.get('FilterList') is not None:
            for k1 in m.get('FilterList'):
                temp_model = main_models.CreateNodeSupplementRequestCreateCommandFilterList()
                self.filter_list.append(temp_model.from_map(k1))

        self.global_param_list = []
        if m.get('GlobalParamList') is not None:
            for k1 in m.get('GlobalParamList'):
                temp_model = main_models.CreateNodeSupplementRequestCreateCommandGlobalParamList()
                self.global_param_list.append(temp_model.from_map(k1))

        if m.get('MaxDueTime') is not None:
            self.max_due_time = m.get('MaxDueTime')

        if m.get('MinDueTime') is not None:
            self.min_due_time = m.get('MinDueTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.node_id_list = []
        if m.get('NodeIdList') is not None:
            for k1 in m.get('NodeIdList'):
                temp_model = main_models.CreateNodeSupplementRequestCreateCommandNodeIdList()
                self.node_id_list.append(temp_model.from_map(k1))

        self.node_params_list = []
        if m.get('NodeParamsList') is not None:
            for k1 in m.get('NodeParamsList'):
                temp_model = main_models.CreateNodeSupplementRequestCreateCommandNodeParamsList()
                self.node_params_list.append(temp_model.from_map(k1))

        if m.get('Parallelism') is not None:
            self.parallelism = m.get('Parallelism')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RunImmediately') is not None:
            self.run_immediately = m.get('RunImmediately')

        if m.get('StartBizDate') is not None:
            self.start_biz_date = m.get('StartBizDate')

        return self

class CreateNodeSupplementRequestCreateCommandNodeParamsList(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        param_list: List[main_models.CreateNodeSupplementRequestCreateCommandNodeParamsListParamList] = None,
    ):
        # The node ID.
        self.node_id = node_id
        # The parameter list.
        self.param_list = param_list

    def validate(self):
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.CreateNodeSupplementRequestCreateCommandNodeParamsListParamList()
                self.param_list.append(temp_model.from_map(k1))

        return self

class CreateNodeSupplementRequestCreateCommandNodeParamsListParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The parameter.
        self.key = key
        # The parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateNodeSupplementRequestCreateCommandNodeIdList(DaraModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
    ):
        # The list of field IDs. This parameter is applicable when the node ID is a logical table node ID. If this parameter is not specified, all fields in the table are used by default.
        self.field_id_list = field_id_list
        # The node ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class CreateNodeSupplementRequestCreateCommandGlobalParamList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The parameter.
        self.key = key
        # The parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateNodeSupplementRequestCreateCommandFilterList(DaraModel):
    def __init__(
        self,
        exclude: bool = None,
        key: str = None,
        value_list: List[str] = None,
    ):
        # Specifies whether to exclude the matched items. Default value: false.
        self.exclude = exclude
        # The filter key. Valid values:
        # - PROJECT: project
        # - NODE_OUTPUT_NAME: node output name
        # - NODE_NAME: node name
        # - NODE_ID: node ID
        # - TARGETS: specified endpoints
        # - SOURCES: specified start points
        self.key = key
        # The list of filter values.
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.key is not None:
            result['Key'] = self.key

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class CreateNodeSupplementRequestCreateCommandDownStreamNodeIdList(DaraModel):
    def __init__(
        self,
        field_id_list: List[str] = None,
        id: str = None,
    ):
        # The field ID.
        self.field_id_list = field_id_list
        # The node ID.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_id_list is not None:
            result['FieldIdList'] = self.field_id_list

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldIdList') is not None:
            self.field_id_list = m.get('FieldIdList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

