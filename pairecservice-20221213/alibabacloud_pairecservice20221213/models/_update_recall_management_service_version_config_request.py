# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class UpdateRecallManagementServiceVersionConfigRequest(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        instance_id: str = None,
        merge_config: main_models.UpdateRecallManagementServiceVersionConfigRequestMergeConfig = None,
        recall_config: main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfig = None,
    ):
        # The type of the recall management version configuration. Valid values are `Recall` for the recall configuration and `Merge` for the merge configuration.
        self.config_type = config_type
        # The instance ID.
        self.instance_id = instance_id
        # The merge configuration.
        self.merge_config = merge_config
        # The recall configuration.
        self.recall_config = recall_config

    def validate(self):
        if self.merge_config:
            self.merge_config.validate()
        if self.recall_config:
            self.recall_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.merge_config is not None:
            result['MergeConfig'] = self.merge_config.to_map()

        if self.recall_config is not None:
            result['RecallConfig'] = self.recall_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MergeConfig') is not None:
            temp_model = main_models.UpdateRecallManagementServiceVersionConfigRequestMergeConfig()
            self.merge_config = temp_model.from_map(m.get('MergeConfig'))

        if m.get('RecallConfig') is not None:
            temp_model = main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfig()
            self.recall_config = temp_model.from_map(m.get('RecallConfig'))

        return self

class UpdateRecallManagementServiceVersionConfigRequestRecallConfig(DaraModel):
    def __init__(
        self,
        description: str = None,
        extended_config: str = None,
        item_condition_array: str = None,
        item_condition_expression: str = None,
        item_vector_field: str = None,
        item_vector_recall_management_table_id: str = None,
        name: str = None,
        operators: List[main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperators] = None,
        priority: int = None,
        recall_management_table_id: str = None,
        recall_type: str = None,
        sort_fields: str = None,
        user_vector_field: str = None,
        user_vector_recall_management_table_id: str = None,
    ):
        # The recall description.
        self.description = description
        # The extended configuration. Reserved for future use.
        self.extended_config = extended_config
        # The data format of the item condition.
        self.item_condition_array = item_condition_array
        # The item condition expression.
        self.item_condition_expression = item_condition_expression
        # The item vector field.
        self.item_vector_field = item_vector_field
        # The ID of the item vector recall management table.
        self.item_vector_recall_management_table_id = item_vector_recall_management_table_id
        # The recall name.
        self.name = name
        # A list of operators.
        self.operators = operators
        # The priority. A smaller value indicates a higher priority.
        self.priority = priority
        # The ID of the recall management table.
        self.recall_management_table_id = recall_management_table_id
        # The recall type.
        self.recall_type = recall_type
        # The sort fields.
        self.sort_fields = sort_fields
        # The user vector field.
        self.user_vector_field = user_vector_field
        # The ID of the user vector recall management table.
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

        if self.recall_management_table_id is not None:
            result['RecallManagementTableId'] = self.recall_management_table_id

        if self.recall_type is not None:
            result['RecallType'] = self.recall_type

        if self.sort_fields is not None:
            result['SortFields'] = self.sort_fields

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
                temp_model = main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperators()
                self.operators.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RecallManagementTableId') is not None:
            self.recall_management_table_id = m.get('RecallManagementTableId')

        if m.get('RecallType') is not None:
            self.recall_type = m.get('RecallType')

        if m.get('SortFields') is not None:
            self.sort_fields = m.get('SortFields')

        if m.get('UserVectorField') is not None:
            self.user_vector_field = m.get('UserVectorField')

        if m.get('UserVectorRecallManagementTableId') is not None:
            self.user_vector_recall_management_table_id = m.get('UserVectorRecallManagementTableId')

        return self

class UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperators(DaraModel):
    def __init__(
        self,
        feature_config: main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsFeatureConfig = None,
        filter_config: main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsFilterConfig = None,
        join_config: main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsJoinConfig = None,
        operator_type: str = None,
        trigger_config: main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsTriggerConfig = None,
    ):
        # The configuration for the `Feature` operator.
        self.feature_config = feature_config
        # The configuration for the `Filter` operator.
        self.filter_config = filter_config
        # The configuration for the `Join` operator.
        self.join_config = join_config
        # The operator type.
        self.operator_type = operator_type
        # The configuration for the `Trigger` operator.
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
            temp_model = main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsFeatureConfig()
            self.feature_config = temp_model.from_map(m.get('FeatureConfig'))

        if m.get('FilterConfig') is not None:
            temp_model = main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsFilterConfig()
            self.filter_config = temp_model.from_map(m.get('FilterConfig'))

        if m.get('JoinConfig') is not None:
            temp_model = main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsJoinConfig()
            self.join_config = temp_model.from_map(m.get('JoinConfig'))

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('TriggerConfig') is not None:
            temp_model = main_models.UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsTriggerConfig()
            self.trigger_config = temp_model.from_map(m.get('TriggerConfig'))

        return self

class UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsTriggerConfig(DaraModel):
    def __init__(
        self,
        field: str = None,
        field_quantity_limit: int = None,
        is_rand_sort: bool = None,
        sort_field: str = None,
    ):
        # The field name.
        self.field = field
        # The maximum number of fields.
        self.field_quantity_limit = field_quantity_limit
        # Specifies whether to perform a random sort.
        self.is_rand_sort = is_rand_sort
        # The sort field.
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

class UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsJoinConfig(DaraModel):
    def __init__(
        self,
        field: str = None,
        output_fields: List[str] = None,
        recall_management_table_id: str = None,
    ):
        # The join field.
        self.field = field
        # The fields to return from the join.
        self.output_fields = output_fields
        # The ID of the table to join.
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

class UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsFilterConfig(DaraModel):
    def __init__(
        self,
        experession: str = None,
    ):
        # The filter expression.
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

class UpdateRecallManagementServiceVersionConfigRequestRecallConfigOperatorsFeatureConfig(DaraModel):
    def __init__(
        self,
        expression: str = None,
        name: str = None,
        type: str = None,
    ):
        # The feature expression.
        self.expression = expression
        # The feature name.
        self.name = name
        # The feature type.
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

class UpdateRecallManagementServiceVersionConfigRequestMergeConfig(DaraModel):
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
        # Additional configurations for the merge. Reserved for future use.
        self.extended_config = extended_config
        # The filter expression.
        self.filter_expression = filter_expression
        # A list of recall management table IDs to use for filtering.
        self.filter_recall_management_table_ids = filter_recall_management_table_ids
        # The ID of the item recall management table.
        self.item_recall_management_table_id = item_recall_management_table_id
        # The output fields from the item table.
        self.item_table_fields = item_table_fields
        # The merge type. Valid values: `Weight` and `Alternate`.
        self.merge_type = merge_type
        # The ID of the recall management service version configuration.
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

