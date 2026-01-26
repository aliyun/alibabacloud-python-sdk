# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetRecallManagementServiceVersionResponseBody(DaraModel):
    def __init__(
        self,
        configs: main_models.GetRecallManagementServiceVersionResponseBodyConfigs = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        is_default: str = None,
        is_effective: bool = None,
        name: str = None,
        recall_management_service_version_id: str = None,
        request_id: str = None,
    ):
        self.configs = configs
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.is_default = is_default
        self.is_effective = is_effective
        self.name = name
        self.recall_management_service_version_id = recall_management_service_version_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.is_effective is not None:
            result['IsEffective'] = self.is_effective

        if self.name is not None:
            result['Name'] = self.name

        if self.recall_management_service_version_id is not None:
            result['RecallManagementServiceVersionId'] = self.recall_management_service_version_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            temp_model = main_models.GetRecallManagementServiceVersionResponseBodyConfigs()
            self.configs = temp_model.from_map(m.get('Configs'))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('IsEffective') is not None:
            self.is_effective = m.get('IsEffective')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecallManagementServiceVersionId') is not None:
            self.recall_management_service_version_id = m.get('RecallManagementServiceVersionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRecallManagementServiceVersionResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        merge_config: main_models.GetRecallManagementServiceVersionResponseBodyConfigsMergeConfig = None,
        recall_configs: List[main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigs] = None,
    ):
        self.merge_config = merge_config
        self.recall_configs = recall_configs

    def validate(self):
        if self.merge_config:
            self.merge_config.validate()
        if self.recall_configs:
            for v1 in self.recall_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.merge_config is not None:
            result['MergeConfig'] = self.merge_config.to_map()

        result['RecallConfigs'] = []
        if self.recall_configs is not None:
            for k1 in self.recall_configs:
                result['RecallConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MergeConfig') is not None:
            temp_model = main_models.GetRecallManagementServiceVersionResponseBodyConfigsMergeConfig()
            self.merge_config = temp_model.from_map(m.get('MergeConfig'))

        self.recall_configs = []
        if m.get('RecallConfigs') is not None:
            for k1 in m.get('RecallConfigs'):
                temp_model = main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigs()
                self.recall_configs.append(temp_model.from_map(k1))

        return self

class GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigs(DaraModel):
    def __init__(
        self,
        description: str = None,
        extended_config: str = None,
        item_condition_array: str = None,
        item_condition_expression: str = None,
        item_vector_field: str = None,
        item_vector_recall_management_table_id: str = None,
        name: str = None,
        operators: List[main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperators] = None,
        priority: int = None,
        recall_management_service_version_config_id: str = None,
        recall_management_table_id: str = None,
        recall_type: str = None,
        user_vector_field: str = None,
        user_vector_recall_management_table_id: str = None,
    ):
        self.description = description
        self.extended_config = extended_config
        self.item_condition_array = item_condition_array
        self.item_condition_expression = item_condition_expression
        self.item_vector_field = item_vector_field
        self.item_vector_recall_management_table_id = item_vector_recall_management_table_id
        self.name = name
        self.operators = operators
        self.priority = priority
        self.recall_management_service_version_config_id = recall_management_service_version_config_id
        self.recall_management_table_id = recall_management_table_id
        self.recall_type = recall_type
        self.user_vector_field = user_vector_field
        self.user_vector_recall_management_table_id = user_vector_recall_management_table_id

    def validate(self):
        if self.operators:
            for v1 in self.operators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config

        if self.item_condition_array is not None:
            result['ItemConditionArray'] = self.item_condition_array

        if self.item_condition_expression is not None:
            result['ItemConditionExpression'] = self.item_condition_expression

        if self.item_vector_field is not None:
            result['ItemVectorField'] = self.item_vector_field

        if self.item_vector_recall_management_table_id is not None:
            result['ItemVectorRecallManagementTableId'] = self.item_vector_recall_management_table_id

        if self.name is not None:
            result['Name'] = self.name

        result['Operators'] = []
        if self.operators is not None:
            for k1 in self.operators:
                result['Operators'].append(k1.to_map() if k1 else None)

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.recall_management_service_version_config_id is not None:
            result['RecallManagementServiceVersionConfigId'] = self.recall_management_service_version_config_id

        if self.recall_management_table_id is not None:
            result['RecallManagementTableId'] = self.recall_management_table_id

        if self.recall_type is not None:
            result['RecallType'] = self.recall_type

        if self.user_vector_field is not None:
            result['UserVectorField'] = self.user_vector_field

        if self.user_vector_recall_management_table_id is not None:
            result['UserVectorRecallManagementTableId'] = self.user_vector_recall_management_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')

        if m.get('ItemConditionArray') is not None:
            self.item_condition_array = m.get('ItemConditionArray')

        if m.get('ItemConditionExpression') is not None:
            self.item_condition_expression = m.get('ItemConditionExpression')

        if m.get('ItemVectorField') is not None:
            self.item_vector_field = m.get('ItemVectorField')

        if m.get('ItemVectorRecallManagementTableId') is not None:
            self.item_vector_recall_management_table_id = m.get('ItemVectorRecallManagementTableId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.operators = []
        if m.get('Operators') is not None:
            for k1 in m.get('Operators'):
                temp_model = main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperators()
                self.operators.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RecallManagementServiceVersionConfigId') is not None:
            self.recall_management_service_version_config_id = m.get('RecallManagementServiceVersionConfigId')

        if m.get('RecallManagementTableId') is not None:
            self.recall_management_table_id = m.get('RecallManagementTableId')

        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')

        if m.get('UserVectorField') is not None:
            self.user_vector_field = m.get('UserVectorField')

        if m.get('UserVectorRecallManagementTableId') is not None:
            self.user_vector_recall_management_table_id = m.get('UserVectorRecallManagementTableId')

        return self

class GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperators(DaraModel):
    def __init__(
        self,
        feature_config: main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsFeatureConfig = None,
        filter_config: main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsFilterConfig = None,
        join_config: main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsJoinConfig = None,
        operator_type: str = None,
        trigger_config: main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsTriggerConfig = None,
    ):
        self.feature_config = feature_config
        self.filter_config = filter_config
        self.join_config = join_config
        self.operator_type = operator_type
        self.trigger_config = trigger_config

    def validate(self):
        if self.feature_config:
            self.feature_config.validate()
        if self.filter_config:
            self.filter_config.validate()
        if self.join_config:
            self.join_config.validate()
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_config is not None:
            result['FeatureConfig'] = self.feature_config.to_map()

        if self.filter_config is not None:
            result['FilterConfig'] = self.filter_config.to_map()

        if self.join_config is not None:
            result['JoinConfig'] = self.join_config.to_map()

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConfig') is not None:
            temp_model = main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsFeatureConfig()
            self.feature_config = temp_model.from_map(m.get('FeatureConfig'))

        if m.get('FilterConfig') is not None:
            temp_model = main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsFilterConfig()
            self.filter_config = temp_model.from_map(m.get('FilterConfig'))

        if m.get('JoinConfig') is not None:
            temp_model = main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsJoinConfig()
            self.join_config = temp_model.from_map(m.get('JoinConfig'))

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('TriggerConfig') is not None:
            temp_model = main_models.GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsTriggerConfig()
            self.trigger_config = temp_model.from_map(m.get('TriggerConfig'))

        return self

class GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsTriggerConfig(DaraModel):
    def __init__(
        self,
        field: str = None,
        field_quantity_limit: str = None,
        is_rand_sort: str = None,
        sort_field: str = None,
    ):
        self.field = field
        self.field_quantity_limit = field_quantity_limit
        self.is_rand_sort = is_rand_sort
        self.sort_field = sort_field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.field_quantity_limit is not None:
            result['FieldQuantityLimit'] = self.field_quantity_limit

        if self.is_rand_sort is not None:
            result['IsRandSort'] = self.is_rand_sort

        if self.sort_field is not None:
            result['SortField'] = self.sort_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('FieldQuantityLimit') is not None:
            self.field_quantity_limit = m.get('FieldQuantityLimit')

        if m.get('IsRandSort') is not None:
            self.is_rand_sort = m.get('IsRandSort')

        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')

        return self

class GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsJoinConfig(DaraModel):
    def __init__(
        self,
        field: str = None,
        output_fields: List[str] = None,
        recall_management_table_id: str = None,
    ):
        self.field = field
        self.output_fields = output_fields
        self.recall_management_table_id = recall_management_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['Field'] = self.field

        if self.output_fields is not None:
            result['OutputFields'] = self.output_fields

        if self.recall_management_table_id is not None:
            result['RecallManagementTableId'] = self.recall_management_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('OutputFields') is not None:
            self.output_fields = m.get('OutputFields')

        if m.get('RecallManagementTableId') is not None:
            self.recall_management_table_id = m.get('RecallManagementTableId')

        return self

class GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsFilterConfig(DaraModel):
    def __init__(
        self,
        experession: str = None,
    ):
        self.experession = experession

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.experession is not None:
            result['Experession'] = self.experession

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Experession') is not None:
            self.experession = m.get('Experession')

        return self

class GetRecallManagementServiceVersionResponseBodyConfigsRecallConfigsOperatorsFeatureConfig(DaraModel):
    def __init__(
        self,
        expression: str = None,
        name: str = None,
        type: str = None,
    ):
        self.expression = expression
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['Expression'] = self.expression

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetRecallManagementServiceVersionResponseBodyConfigsMergeConfig(DaraModel):
    def __init__(
        self,
        extended_config: str = None,
        filter_expression: str = None,
        filter_recall_management_table_ids: List[str] = None,
        item_recall_management_table_id: str = None,
        item_table_fields: List[str] = None,
        merge_type: str = None,
        recall_management_service_version_config_id: str = None,
    ):
        self.extended_config = extended_config
        self.filter_expression = filter_expression
        self.filter_recall_management_table_ids = filter_recall_management_table_ids
        self.item_recall_management_table_id = item_recall_management_table_id
        self.item_table_fields = item_table_fields
        self.merge_type = merge_type
        self.recall_management_service_version_config_id = recall_management_service_version_config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config

        if self.filter_expression is not None:
            result['FilterExpression'] = self.filter_expression

        if self.filter_recall_management_table_ids is not None:
            result['FilterRecallManagementTableIds'] = self.filter_recall_management_table_ids

        if self.item_recall_management_table_id is not None:
            result['ItemRecallManagementTableId'] = self.item_recall_management_table_id

        if self.item_table_fields is not None:
            result['ItemTableFields'] = self.item_table_fields

        if self.merge_type is not None:
            result['MergeType'] = self.merge_type

        if self.recall_management_service_version_config_id is not None:
            result['RecallManagementServiceVersionConfigId'] = self.recall_management_service_version_config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')

        if m.get('FilterExpression') is not None:
            self.filter_expression = m.get('FilterExpression')

        if m.get('FilterRecallManagementTableIds') is not None:
            self.filter_recall_management_table_ids = m.get('FilterRecallManagementTableIds')

        if m.get('ItemRecallManagementTableId') is not None:
            self.item_recall_management_table_id = m.get('ItemRecallManagementTableId')

        if m.get('ItemTableFields') is not None:
            self.item_table_fields = m.get('ItemTableFields')

        if m.get('MergeType') is not None:
            self.merge_type = m.get('MergeType')

        if m.get('RecallManagementServiceVersionConfigId') is not None:
            self.recall_management_service_version_config_id = m.get('RecallManagementServiceVersionConfigId')

        return self

