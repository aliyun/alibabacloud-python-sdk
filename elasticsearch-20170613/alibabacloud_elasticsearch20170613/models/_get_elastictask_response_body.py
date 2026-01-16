# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetElastictaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetElastictaskResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetElastictaskResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetElastictaskResponseBodyResult(DaraModel):
    def __init__(
        self,
        elastic_expansion_task: main_models.GetElastictaskResponseBodyResultElasticExpansionTask = None,
        elastic_shrink_task: main_models.GetElastictaskResponseBodyResultElasticShrinkTask = None,
    ):
        self.elastic_expansion_task = elastic_expansion_task
        self.elastic_shrink_task = elastic_shrink_task

    def validate(self):
        if self.elastic_expansion_task:
            self.elastic_expansion_task.validate()
        if self.elastic_shrink_task:
            self.elastic_shrink_task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_expansion_task is not None:
            result['elasticExpansionTask'] = self.elastic_expansion_task.to_map()

        if self.elastic_shrink_task is not None:
            result['elasticShrinkTask'] = self.elastic_shrink_task.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticExpansionTask') is not None:
            temp_model = main_models.GetElastictaskResponseBodyResultElasticExpansionTask()
            self.elastic_expansion_task = temp_model.from_map(m.get('elasticExpansionTask'))

        if m.get('elasticShrinkTask') is not None:
            temp_model = main_models.GetElastictaskResponseBodyResultElasticShrinkTask()
            self.elastic_shrink_task = temp_model.from_map(m.get('elasticShrinkTask'))

        return self

class GetElastictaskResponseBodyResultElasticShrinkTask(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        elastic_node_count: int = None,
        replica_count: int = None,
        target_indices: List[str] = None,
        trigger_type: str = None,
    ):
        self.cron_expression = cron_expression
        self.elastic_node_count = elastic_node_count
        self.replica_count = replica_count
        self.target_indices = target_indices
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count

        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count

        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')

        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')

        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

class GetElastictaskResponseBodyResultElasticExpansionTask(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        elastic_node_count: int = None,
        replica_count: int = None,
        target_indices: List[str] = None,
        trigger_type: str = None,
    ):
        self.cron_expression = cron_expression
        self.elastic_node_count = elastic_node_count
        self.replica_count = replica_count
        self.target_indices = target_indices
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.elastic_node_count is not None:
            result['elasticNodeCount'] = self.elastic_node_count

        if self.replica_count is not None:
            result['replicaCount'] = self.replica_count

        if self.target_indices is not None:
            result['targetIndices'] = self.target_indices

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('elasticNodeCount') is not None:
            self.elastic_node_count = m.get('elasticNodeCount')

        if m.get('replicaCount') is not None:
            self.replica_count = m.get('replicaCount')

        if m.get('targetIndices') is not None:
            self.target_indices = m.get('targetIndices')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

