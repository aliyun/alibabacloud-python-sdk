# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDevObjectDependencyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dev_object_dependency_list: List[main_models.GetDevObjectDependencyResponseBodyDevObjectDependencyList] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dev_object_dependency_list = dev_object_dependency_list
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.dev_object_dependency_list:
            for v1 in self.dev_object_dependency_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['DevObjectDependencyList'] = []
        if self.dev_object_dependency_list is not None:
            for k1 in self.dev_object_dependency_list:
                result['DevObjectDependencyList'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        self.dev_object_dependency_list = []
        if m.get('DevObjectDependencyList') is not None:
            for k1 in m.get('DevObjectDependencyList'):
                temp_model = main_models.GetDevObjectDependencyResponseBodyDevObjectDependencyList()
                self.dev_object_dependency_list.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDevObjectDependencyResponseBodyDevObjectDependencyList(DaraModel):
    def __init__(
        self,
        auto_parse: bool = None,
        biz_type: str = None,
        biz_unit_id: str = None,
        biz_unit_name: str = None,
        cron_expression: str = None,
        custom_cron_expression: bool = None,
        depend_field_list: List[str] = None,
        dependency_period: main_models.GetDevObjectDependencyResponseBodyDevObjectDependencyListDependencyPeriod = None,
        dependency_strategy: str = None,
        dim_mid_node: bool = None,
        effect_field_list: List[str] = None,
        external_biz_info: str = None,
        manually_add: bool = None,
        node_id: str = None,
        node_name: str = None,
        node_output_name: str = None,
        node_output_table_name: str = None,
        node_type: str = None,
        output_context_param_list: List[main_models.GetDevObjectDependencyResponseBodyDevObjectDependencyListOutputContextParamList] = None,
        owner_list: List[main_models.GetDevObjectDependencyResponseBodyDevObjectDependencyListOwnerList] = None,
        period_diff: int = None,
        project_id: int = None,
        project_name: str = None,
        schedule_type: str = None,
        self_depend: bool = None,
        sub_biz_type: str = None,
        valid: bool = None,
    ):
        self.auto_parse = auto_parse
        self.biz_type = biz_type
        self.biz_unit_id = biz_unit_id
        self.biz_unit_name = biz_unit_name
        self.cron_expression = cron_expression
        self.custom_cron_expression = custom_cron_expression
        self.depend_field_list = depend_field_list
        self.dependency_period = dependency_period
        self.dependency_strategy = dependency_strategy
        self.dim_mid_node = dim_mid_node
        self.effect_field_list = effect_field_list
        self.external_biz_info = external_biz_info
        self.manually_add = manually_add
        self.node_id = node_id
        self.node_name = node_name
        self.node_output_name = node_output_name
        self.node_output_table_name = node_output_table_name
        self.node_type = node_type
        self.output_context_param_list = output_context_param_list
        self.owner_list = owner_list
        self.period_diff = period_diff
        self.project_id = project_id
        self.project_name = project_name
        self.schedule_type = schedule_type
        self.self_depend = self_depend
        self.sub_biz_type = sub_biz_type
        self.valid = valid

    def validate(self):
        if self.dependency_period:
            self.dependency_period.validate()
        if self.output_context_param_list:
            for v1 in self.output_context_param_list:
                 if v1:
                    v1.validate()
        if self.owner_list:
            for v1 in self.owner_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_parse is not None:
            result['AutoParse'] = self.auto_parse

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.biz_unit_name is not None:
            result['BizUnitName'] = self.biz_unit_name

        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.custom_cron_expression is not None:
            result['CustomCronExpression'] = self.custom_cron_expression

        if self.depend_field_list is not None:
            result['DependFieldList'] = self.depend_field_list

        if self.dependency_period is not None:
            result['DependencyPeriod'] = self.dependency_period.to_map()

        if self.dependency_strategy is not None:
            result['DependencyStrategy'] = self.dependency_strategy

        if self.dim_mid_node is not None:
            result['DimMidNode'] = self.dim_mid_node

        if self.effect_field_list is not None:
            result['EffectFieldList'] = self.effect_field_list

        if self.external_biz_info is not None:
            result['ExternalBizInfo'] = self.external_biz_info

        if self.manually_add is not None:
            result['ManuallyAdd'] = self.manually_add

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_output_name is not None:
            result['NodeOutputName'] = self.node_output_name

        if self.node_output_table_name is not None:
            result['NodeOutputTableName'] = self.node_output_table_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        result['OutputContextParamList'] = []
        if self.output_context_param_list is not None:
            for k1 in self.output_context_param_list:
                result['OutputContextParamList'].append(k1.to_map() if k1 else None)

        result['OwnerList'] = []
        if self.owner_list is not None:
            for k1 in self.owner_list:
                result['OwnerList'].append(k1.to_map() if k1 else None)

        if self.period_diff is not None:
            result['PeriodDiff'] = self.period_diff

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.self_depend is not None:
            result['SelfDepend'] = self.self_depend

        if self.sub_biz_type is not None:
            result['SubBizType'] = self.sub_biz_type

        if self.valid is not None:
            result['Valid'] = self.valid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoParse') is not None:
            self.auto_parse = m.get('AutoParse')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('BizUnitName') is not None:
            self.biz_unit_name = m.get('BizUnitName')

        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('CustomCronExpression') is not None:
            self.custom_cron_expression = m.get('CustomCronExpression')

        if m.get('DependFieldList') is not None:
            self.depend_field_list = m.get('DependFieldList')

        if m.get('DependencyPeriod') is not None:
            temp_model = main_models.GetDevObjectDependencyResponseBodyDevObjectDependencyListDependencyPeriod()
            self.dependency_period = temp_model.from_map(m.get('DependencyPeriod'))

        if m.get('DependencyStrategy') is not None:
            self.dependency_strategy = m.get('DependencyStrategy')

        if m.get('DimMidNode') is not None:
            self.dim_mid_node = m.get('DimMidNode')

        if m.get('EffectFieldList') is not None:
            self.effect_field_list = m.get('EffectFieldList')

        if m.get('ExternalBizInfo') is not None:
            self.external_biz_info = m.get('ExternalBizInfo')

        if m.get('ManuallyAdd') is not None:
            self.manually_add = m.get('ManuallyAdd')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeOutputName') is not None:
            self.node_output_name = m.get('NodeOutputName')

        if m.get('NodeOutputTableName') is not None:
            self.node_output_table_name = m.get('NodeOutputTableName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        self.output_context_param_list = []
        if m.get('OutputContextParamList') is not None:
            for k1 in m.get('OutputContextParamList'):
                temp_model = main_models.GetDevObjectDependencyResponseBodyDevObjectDependencyListOutputContextParamList()
                self.output_context_param_list.append(temp_model.from_map(k1))

        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k1 in m.get('OwnerList'):
                temp_model = main_models.GetDevObjectDependencyResponseBodyDevObjectDependencyListOwnerList()
                self.owner_list.append(temp_model.from_map(k1))

        if m.get('PeriodDiff') is not None:
            self.period_diff = m.get('PeriodDiff')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('SelfDepend') is not None:
            self.self_depend = m.get('SelfDepend')

        if m.get('SubBizType') is not None:
            self.sub_biz_type = m.get('SubBizType')

        if m.get('Valid') is not None:
            self.valid = m.get('Valid')

        return self

class GetDevObjectDependencyResponseBodyDevObjectDependencyListOwnerList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetDevObjectDependencyResponseBodyDevObjectDependencyListOutputContextParamList(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        description: str = None,
        key: str = None,
    ):
        self.default_value = default_value
        self.description = description
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class GetDevObjectDependencyResponseBodyDevObjectDependencyListDependencyPeriod(DaraModel):
    def __init__(
        self,
        period_offset: int = None,
        period_type: str = None,
    ):
        self.period_offset = period_offset
        self.period_type = period_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.period_offset is not None:
            result['PeriodOffset'] = self.period_offset

        if self.period_type is not None:
            result['PeriodType'] = self.period_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeriodOffset') is not None:
            self.period_offset = m.get('PeriodOffset')

        if m.get('PeriodType') is not None:
            self.period_type = m.get('PeriodType')

        return self

